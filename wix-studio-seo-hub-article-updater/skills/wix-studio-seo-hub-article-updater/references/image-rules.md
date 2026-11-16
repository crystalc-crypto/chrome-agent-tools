# Image rules: featured images, CTA images and infographics

Source: "Image rules for article skills (featured, CTAs, infographics)" (https://docs.google.com/document/d/1n5RriUuDqSy36B3Nm1v562r_RK4j-kKdIDX4Wpf2vLg), Nov 2026, plus API details from article-updater-2.

Runs as part of **every update** (Phase 6b) and the image plan goes in the approval package (Phase 6d). Where a bucket folder exists, these rules override the per-cluster gate images in `cta-blocks.md`. The placement and spacing rules in `formatting-audit.md` (never directly under a heading, 3+ paragraphs from other images and cards, spacing) still apply to every image.

---

## Media folder structure

Images live in the blog site's Wix Media Manager (Wix Studio SEO Hub, `1bd95b49-a53d-4ff9-917d-cdcc422f879e`; folders may not exist yet, so look them up and fall back to sibling-article images), under Site Files. Each content bucket (cluster) has one parent folder with three subfolders:

| Level | Folder name pattern | Domains example |
|---|---|---|
| Bucket folder | `[Bucket] bucket` | Domains bucket |
| Featured | `[bucket] - featured images` | domains - featured images |
| CTAs | `[bucket] - CTAs` | domains - CTAs |
| Infographics | `[bucket] - infographics` | domains - infographics |

Match folder names case-insensitively. Ready as of Nov 2026: **Domains** and **Headless**. More buckets will be added, so always look the folder up at run time; never assume it is missing.

**API:**
- List root folders: `GET https://www.wixapis.com/site-media/v1/folders?parentFolderId=media-root&paging.limit=100`
- List a bucket folder's subfolders: same call with `parentFolderId=<bucket folder id>`
- List images in a subfolder: `GET https://www.wixapis.com/site-media/v1/files?parentFolderId=<id>&mediaTypes=IMAGE&paging.limit=100`

---

## Step 1: Find the bucket folder

1. The bucket is the article's content bucket (Phase 1) / cluster.
2. Look for `[Bucket] bucket` under Site Files, then list the files in each of its three subfolders.
3. **If the bucket folder, any of its three subfolders, or a subfolder's files are missing,** flag it to the user and ask them to create it:
   > "There is no image folder for the [bucket] bucket yet. Please create '[Bucket] bucket' in the blog Media Manager with the subfolders '[bucket] - featured images', '[bucket] - CTAs' and '[bucket] - infographics', add the images, and tell me when it is ready."
4. **Fallback while the folder is missing (approved Nov 2026):** keep working on everything else, and use the existing cluster image convention: the gate image / in-text banners listed for the cluster in `cta-blocks.md`, or the CTA image copied from a sibling article in the same cluster (Gate 0). Mark the image rows "Fallback: folder missing" in the image plan. If the user creates the folder before the push, re-check and use the folder images instead. Say which was used in the final report.
5. With no folder, skip the featured-image and infographic steps (keep the current cover; note "no folder" in the plan).

---

## Step 2: Featured image

- Choose the image in `[bucket] - featured images` that best matches the article's topic and primary keyword. Judge by file name and by viewing the image.
- It is the post's cover (`media.wixMedia.image` on the draft), never inside the body.
- If none is a good match, use the closest as a placeholder and flag it: "No featured image in [bucket] - featured images fits this topic. I used [file name] as a placeholder. Consider adding a dedicated one."
- **Existing articles:** don't replace the current cover without approval. Compare it with the folder; if a folder image fits better, propose it in the image plan. Always check the cover's alt text against Step 5.

---

## Step 3: CTA images

**Main CTA image:** the file in `[bucket] - CTAs` with `-main` in its name.
- Place it **directly after the TL;DR list** by default (2 empty paragraphs between the list and the image), or where the user asks.
- Every article gets the main CTA image. If no `-main` file exists, flag it and ask which image to use.
- If the main CTA image is already after the TL;DR, don't add it again. If a different (older) CTA image sits there, propose replacing it with the `-main` image in the plan.

**Additional CTA images (1 to 2, only when they fit):**
- Use a CTA image whose message matches the section it follows (for example a domain search CTA after a section on choosing a domain name).
- Place it lower in the article, between sections: at the end of the relevant section, before the next H2.
- Never two CTA images next to each other; spread them through the article.
- If the folder holds only the main image, or no other CTA image fits, use the main image only. No flag needed; note "main CTA only" in the plan.

**Links:** every CTA image links to the cluster's CTA URL (the same gate / product URL as the cluster's CTA button in `cta-blocks.md`, including the TLD-page override for single-TLD articles), `target:"SELF"`.

---

## Step 4: Infographics

- Look in `[bucket] - infographics` for 1 to 2 that match the article's content.
- Place each in the section it illustrates, right after the paragraph that introduces the topic it shows.
- If none fits, add none and flag it: "No infographic in [bucket] - infographics fits this article."

**New infographic suggestion:** if a topic would clearly be easier to follow or more useful for SEO with an infographic (step-by-step process, comparison, checklist, decision guide) and no existing one covers it:
1. Create it with the latest infographic creator skill (currently **infographic-creator-2**).
2. Suggest it in the image plan with placement and alt text, and attach the file for review.
3. **Only after the user approves it:** upload the JPG to `[bucket] - infographics` (for example with `UploadImageToWixSite`, then move or upload into that folder), and insert it. Never insert an unapproved infographic.

---

## Step 5: Alt text (every image, including the featured image)

- 2 to 5 words.
- Includes the primary or a secondary keyword, worded naturally.
- Describes what the image shows; never starts with "image of" or "picture of".
- Unique per image in the article; no keyword stuffing.
- WHOIS in capitals; "ecommerce" spelling rules; no `\n`.

Examples for "how to choose a domain name": featured "choosing a domain name"; main CTA "search for a domain"; infographic "domain name checklist".

On updates, fix existing alt texts that break these rules (list them in the plan).

---

## Step 6: Image plan (in the Phase 6d approval package)

| Type | File name | Placement | Alt text | Link | Status / flag |
|---|---|---|---|---|---|
| Featured | … | Cover image | … | None | OK / Placeholder / Keep current / Propose replace |
| CTA (main) | …-main… | After TL;DR | … | Cluster CTA URL | OK / Already present |
| CTA | … | End of section "…" | … | Cluster CTA URL | OK |
| Infographic | … | After paragraph "…" in "…" | … | None | OK / New, needs approval |
| Existing image | … | Current position | old > new alt | … | Alt fix / Move (under heading) / Propose replace |

List every flag under the table: missing folder (and the fallback used), placeholder featured image, no `-main` file, no relevant infographic, new infographic awaiting approval.

---

## Step 7: Insert and verify

- Use existing Media Manager files (media ID or `wix:image` URL, with the file's real width and height) as `IMAGE` nodes. Never re-upload images already in the bucket folders.
- Don't remove or replace existing images without approval.
- After publishing, read the draft back and check: each planned image is in place with its alt text; CTA images link to the cluster CTA URL in the same tab; the cover is set; no image sits directly under a heading; 3+ paragraphs between images and cards.
- Report the final image list and any open flags in the final report.
