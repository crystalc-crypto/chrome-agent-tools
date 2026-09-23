#!/usr/bin/env python3
"""Turn a YouTube video into a Google Slides webinar deck.

One slide per transcript segment: a screenshot from that segment as the
slide image, the segment's transcript text as the speaker notes.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SCOPES = [
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/drive.file",
]

SLIDE_W_EMU = 9144000  # 16:9 default Slides page size (EMU)
SLIDE_H_EMU = 5143500


def run(cmd):
    subprocess.run(cmd, check=True)


def download_video_and_captions(url, out_dir: Path) -> tuple[Path, Path]:
    """Downloads the video and its best available caption track.

    Returns (video_path, vtt_path).
    """
    video_tmpl = str(out_dir / "video.%(ext)s")
    run([
        "yt-dlp", "-f", "bv*[height<=720]+ba/b[height<=720]",
        "--merge-output-format", "mp4",
        "-o", video_tmpl,
        url,
    ])
    videos = list(out_dir.glob("video.*"))
    videos = [v for v in videos if v.suffix != ".vtt"]
    if not videos:
        sys.exit("yt-dlp did not produce a video file")
    video_path = videos[0]

    run([
        "yt-dlp", "--skip-download",
        "--write-auto-sub", "--write-sub",
        "--sub-lang", "en.*",
        "--sub-format", "vtt",
        "-o", str(out_dir / "captions.%(ext)s"),
        url,
    ])
    vtts = list(out_dir.glob("captions*.vtt"))
    if not vtts:
        sys.exit("No English captions found for this video (auto or manual).")
    return video_path, vtts[0]


TIME_RE = re.compile(r"(\d\d):(\d\d):(\d\d)\.(\d\d\d)")


def _ts_to_seconds(ts: str) -> float:
    h, m, s, ms = TIME_RE.match(ts).groups()
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_vtt(vtt_path: Path):
    """Returns list of (start_sec, end_sec, text) cue tuples, deduped/cleaned."""
    raw = vtt_path.read_text(encoding="utf-8", errors="ignore")
    blocks = raw.split("\n\n")
    cues = []
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip()]
        time_line = next((l for l in lines if "-->" in l), None)
        if not time_line:
            continue
        start_ts, end_ts = [t.strip().split(" ")[0] for t in time_line.split("-->")]
        try:
            start, end = _ts_to_seconds(start_ts), _ts_to_seconds(end_ts)
        except AttributeError:
            continue
        text_lines = lines[lines.index(time_line) + 1:]
        text = " ".join(text_lines)
        text = re.sub(r"<[^>]+>", "", text)  # strip inline vtt tags
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            cues.append((start, end, text))

    # Auto-captions repeat/roll text across cues; dedupe consecutive repeats.
    deduped = []
    for start, end, text in cues:
        if deduped and text == deduped[-1][2]:
            deduped[-1] = (deduped[-1][0], end, text)
            continue
        if deduped and text.startswith(deduped[-1][2]):
            deduped[-1] = (deduped[-1][0], end, text)
            continue
        deduped.append((start, end, text))
    return deduped


def segment_cues(cues, min_gap: float, max_words: int):
    """Groups cues into segments, breaking on pauses or word-count overflow."""
    segments = []
    cur_start, cur_end, cur_words = None, None, []
    prev_end = None

    def flush():
        if cur_words:
            segments.append({
                "start": cur_start,
                "end": cur_end,
                "text": " ".join(cur_words),
            })

    for start, end, text in cues:
        gap = (start - prev_end) if prev_end is not None else 0
        words = text.split()
        would_overflow = cur_words and (len(cur_words) + len(words) > max_words)
        if cur_words and (gap > min_gap or would_overflow):
            flush()
            cur_start, cur_words = start, []
        elif not cur_words:
            cur_start = start
        cur_words.extend(words)
        cur_end = end
        prev_end = end
    flush()
    return segments


def extract_frame(video_path: Path, timestamp: float, out_path: Path):
    run([
        "ffmpeg", "-y", "-ss", str(timestamp), "-i", str(video_path),
        "-frames:v", "1", "-q:v", "2", str(out_path),
    ])


def build_creds(credentials_path: str, out_dir: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    token_path = Path(credentials_path).with_name("token.json")
    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json())
    return creds


def upload_image_public(drive_service, image_path: Path) -> str:
    from googleapiclient.http import MediaFileUpload

    media = MediaFileUpload(str(image_path), mimetype="image/jpeg")
    file = drive_service.files().create(
        body={"name": image_path.name}, media_body=media, fields="id"
    ).execute()
    file_id = file["id"]
    drive_service.permissions().create(
        fileId=file_id, body={"role": "reader", "type": "anyone"}
    ).execute()
    return f"https://drive.google.com/uc?id={file_id}"


def build_presentation(slides_service, drive_service, title: str, segments, out_dir: Path):
    presentation = slides_service.presentations().create(
        body={"title": title}
    ).execute()
    presentation_id = presentation["presentationId"]
    default_slide_id = presentation["slides"][0]["objectId"]

    requests = []
    slide_ids = []
    for i, seg in enumerate(segments):
        slide_id = f"slide_{i}"
        slide_ids.append(slide_id)
        requests.append({
            "createSlide": {
                "objectId": slide_id,
                "slideLayoutReference": {"predefinedLayout": "BLANK"},
            }
        })
    requests.append({"deleteObject": {"objectId": default_slide_id}})
    slides_service.presentations().batchUpdate(
        presentationId=presentation_id, body={"requests": requests}
    ).execute()

    for i, (slide_id, seg) in enumerate(zip(slide_ids, segments)):
        image_url = upload_image_public(drive_service, Path(seg["image_path"]))
        image_id = f"image_{i}"
        img_requests = [{
            "createImage": {
                "objectId": image_id,
                "url": image_url,
                "elementProperties": {
                    "pageObjectId": slide_id,
                    "size": {
                        "height": {"magnitude": SLIDE_H_EMU, "unit": "EMU"},
                        "width": {"magnitude": SLIDE_W_EMU, "unit": "EMU"},
                    },
                    "transform": {
                        "scaleX": 1, "scaleY": 1, "translateX": 0, "translateY": 0,
                        "unit": "EMU",
                    },
                },
            }
        }]
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id, body={"requests": img_requests}
        ).execute()

        page = slides_service.presentations().pages().get(
            presentationId=presentation_id, pageObjectId=slide_id
        ).execute()
        notes_page = page.get("slideProperties", {}).get("notesPage", {})
        notes_shape_id = None
        for el in notes_page.get("pageElements", []):
            placeholder = el.get("shape", {}).get("placeholder", {})
            if placeholder.get("type") == "BODY":
                notes_shape_id = el["objectId"]
                break
        if notes_shape_id:
            note_requests = [{
                "insertText": {
                    "objectId": notes_shape_id,
                    "text": seg["text"],
                    "insertionIndex": 0,
                }
            }]
            slides_service.presentations().batchUpdate(
                presentationId=presentation_id, body={"requests": note_requests}
            ).execute()

    return f"https://docs.google.com/presentation/d/{presentation_id}/edit"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--title", default="Webinar Deck", help="Deck title")
    parser.add_argument("--credentials", required=True, help="Path to Google OAuth credentials.json")
    parser.add_argument("--min-gap", type=float, default=1.2, help="Seconds of pause treated as a topic break")
    parser.add_argument("--max-words", type=int, default=130, help="Max words per slide's notes")
    parser.add_argument("--out-dir", default=None, help="Working directory for downloads/frames (default: temp dir)")
    parser.add_argument("--dump-segments", action="store_true", help="Write segments.json and exit before building the deck")
    args = parser.parse_args()

    out_dir = Path(args.out_dir) if args.out_dir else Path(tempfile.mkdtemp(prefix="yt_deck_"))
    out_dir.mkdir(parents=True, exist_ok=True)
    frames_dir = out_dir / "frames"
    frames_dir.mkdir(exist_ok=True)

    print(f"Working dir: {out_dir}")
    video_path, vtt_path = download_video_and_captions(args.url, out_dir)
    cues = parse_vtt(vtt_path)
    segments = segment_cues(cues, args.min_gap, args.max_words)
    print(f"Segmented transcript into {len(segments)} slides.")

    for i, seg in enumerate(segments):
        mid = (seg["start"] + seg["end"]) / 2
        frame_path = frames_dir / f"frame_{i:03d}.jpg"
        extract_frame(video_path, mid, frame_path)
        seg["image_path"] = str(frame_path)

    if args.dump_segments:
        dump = [{"start": s["start"], "end": s["end"], "text": s["text"]} for s in segments]
        (out_dir / "segments.json").write_text(json.dumps(dump, indent=2))
        print(f"Wrote {out_dir / 'segments.json'}; skipping deck build (--dump-segments).")
        return

    from googleapiclient.discovery import build

    creds = build_creds(args.credentials, out_dir)
    slides_service = build("slides", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    url = build_presentation(slides_service, drive_service, args.title, segments, out_dir)
    print(f"\nDeck created: {url}")


if __name__ == "__main__":
    main()
