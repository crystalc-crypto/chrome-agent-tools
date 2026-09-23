---
name: youtube-to-webinar-deck
description: Converts a YouTube video into a Google Slides deck for presenting as a webinar — extracts screenshots at natural topic/sentence breaks in the transcript and puts the corresponding transcript text into each slide's speaker notes. Use when the user gives a YouTube URL and wants a slide deck / webinar deck built from it, or asks to turn a video into slides with the transcript as notes. Runs locally (not in a cloud/remote session) because it needs yt-dlp, ffmpeg, and local Google OAuth credentials.
---

# YouTube → Webinar Deck

Turns a YouTube video into a Google Slides deck: one slide per topic segment,
each slide's image is a screenshot from that segment of the video, and the
segment's transcript text goes into the slide's speaker notes — so you can
present it like a live webinar just by reading your notes.

## Requirements (check/install once)

- `yt-dlp` — downloads the video and its transcript/captions.
- `ffmpeg` — extracts still frames from the video at given timestamps.
- Python 3.9+ with `google-api-python-client`, `google-auth-httplib2`,
  `google-auth-oauthlib` installed (`pip install -r scripts/requirements.txt`).
- A Google Cloud OAuth client (Desktop app type) with the Slides API and
  Drive API enabled, downloaded as `credentials.json`. First run opens a
  browser consent screen and caches a token in `token.json` next to it —
  only needs to be done once per machine.

If any of these are missing, tell the user exactly what to install/configure
before running the script — don't try to silently work around missing
tools.

## Workflow

1. Ask the user for the YouTube URL (and title for the deck, if not obvious)
   if not already given.
2. Run the build script:

   ```
   python skills/youtube-to-webinar-deck/scripts/build_deck.py \
     "<youtube-url>" \
     --title "<deck title>" \
     --credentials /path/to/credentials.json
   ```

   Useful flags:
   - `--min-gap` (default 1.2s) — minimum pause in the transcript's own
     timestamps that's treated as a topic boundary.
   - `--max-words` (default 130) — force a new slide if a segment grows
     past this many words even without a natural pause (keeps notes
     readable on one slide).
   - `--out-dir` — where to cache the downloaded video/frames/transcript
     (defaults to a temp dir; pass a real path to inspect intermediate
     files or resume).

3. The script prints the resulting Google Slides URL when done. Share that
   with the user — don't just report success without the link.

## How segmentation works

The script pulls YouTube's timed transcript (auto or manual captions),
groups consecutive lines into a segment, and starts a new segment when
either:
- there's a gap between caption timestamps larger than `--min-gap` (a
  natural pause — usually a topic/beat change in a talk), or
- the running segment exceeds `--max-words`.

For each segment it takes a frame from partway through the segment's time
range (not the very first frame, which is often mid-transition) via
`ffmpeg -ss <timestamp>`.

## Building the deck

One slide per segment: the frame image fills the slide, and the segment's
transcript text (cleaned of caption artifacts) is written to that slide's
speaker notes via the Slides API. The deck is created in the user's Google
Drive under "My Drive" root — move it afterward if they want it elsewhere.

## Notes / limitations

- Only works for videos with captions available (auto-generated captions
  work fine — YouTube generates them for almost all English-language
  videos).
- If the user wants tighter control over where breaks happen (e.g. exact
  slide-per-slide match to their manual deck), offer to let them review the
  segment list (script can dump it as JSON) before frame extraction and
  edit boundaries by hand.
- Rate limits: Slides API calls are batched per slide; a ~20-slide deck
  runs comfortably under quota.
