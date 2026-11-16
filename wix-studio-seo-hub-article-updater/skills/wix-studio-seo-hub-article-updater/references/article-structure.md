# Article structure, top-of-article rules and block templates

Copy every block from a live approved article first (Gate 0 in `quality-gates.md`). The templates below describe the convention; the live article wins if they differ.

---

## Canonical top-of-article structure (always)

1. Top gate-link line (from `cta-blocks.md`)
2. Hero / featured image
3. **Intro: exactly 2 short paragraphs**
4. **Main CTA paragraph + button** (bold only the first sentence)
5. **TL;DR:** H2 `TL;DR: how to <topic>` > ONE paragraph > bold "You'll learn:" > bulleted list
6. **CTA image** directly after the TL;DR list (2 empty paragraphs between the list and the image): the bucket's `-main` CTA image, see `image-rules.md`
7. Body sections

- A **video** never belongs in the intro. Move it before the first numbered step heading.
- Articles are found live with the CTA block **after** the TL;DR. Fix it, but check node order before measuring anything, since it breaks naive intro and echo detection.
- If an article has no CTA block, clone one from a sibling article in the same cluster (Gate 0), using the copy in `cta-blocks.md`.
- No competing CTAs beside the main CTA.
- Duplicate expert quotes: keep the stronger one (ask before removing).

## Intro

- Exactly 2 short paragraphs, **60 to 90 words total**. Split a single long block at a sentence boundary; condense 3+.
- Topic-specific, never generic. No "If you have a passion for…", "Do you have specialized expertise…", "Are you drawn to…" openers.
- No "Keep reading…", "In this guide we'll walk you through…".
- No lists or "other names" blocks. No byline in the body.
- **No blog links; gate links only.** No Wix mention in non-branded articles (Gate 1c).
- Cut unsourced claims (Gate 1).
- Counting gotcha: exclude the CTA paragraph and any secondary CTA.

## TL;DR

- H2 > ONE short paragraph > EITHER a "You'll learn:" list OR a table, never both. Prefer the list. No blog links.
- All Gate 3 checks (A to G) in `quality-gates.md`.
- "You'll learn:" keeps exactly one empty paragraph before its list.
- Two empty paragraphs between the TL;DR list and the CTA image.

## Relocating blog links when rewriting the intro or TL;DR

Never drop blog links. Before rewriting, record every blog link in the old intro/TL;DR. Relocate each to a relevant body section with its approved anchor (EN Blogs Clusters board `5557032877`): add it to an existing "Learn more" list, add a new "Learn more" list at the end of the relevant section, or (single link, no adjacent media) a preview card. After publishing, assert each one still appears exactly once.

## Main CTA conventions

- Text + button right after the intro. Bold ONLY the first sentence. 1 empty paragraph before the CTA paragraph, 2 after the button.
- CTA text runs use COLOR foreground `rgb(0,0,0)` (except the Headless cluster, see `cta-blocks.md`). "grow without limits" becomes "grow".
- Pill button `styles:{borderWidth:4,borderRadius:30}`; `styles:{}` renders flat and is wrong. Trim whitespace in URL and text.
- **TLD articles:** in articles about a single extension, the main CTA button and the CTA image after the TL;DR link to `https://www.wix.com/domains/tld-list/tlds/<tld>-domain`. The ccTLD overview article uses `https://www.wix.com/domains/tld-list/cctld`. Verify the TLD page exists before linking. Generic domain articles keep the Domains block URL.

## Product mentions in informational sections

Flagged live: "Cloud hosting also suits headless apps, where a custom frontend connects to a separate backend, and Wix Headless provides that backend…" read as promotional and too technical.

- In a section that explains a concept in general, the new sentence first explains the idea for everyone, in plain words, with no brand.
- Wix comes last, framed as an example: "Wix Headless is one example: …", "With Wix, for example, you can …".
- If the combined text exceeds 4 rows, the Wix example gets its own paragraph.
- Inside a Wix entry or Wix section, Wix can lead, but the wording stays plain.
- This applies to semantic triples, nuance blocks and stats inserted by the Phase 5 update types too.

Approved examples:
- "Cloud hosting is also a good fit for headless websites and apps. In a headless setup, the part visitors see (the design) is built separately from the part that stores your content and handles orders, and cloud hosting lets both parts handle more visitors as your site grows." New paragraph: "Wix Headless is one example: it gives a site built in code ready-made tools for content, online sales and payments, and hosts it on servers around the world."
- "If your site is already built in code, you don't need to set up a server to put it online. With Wix, for example, you can drag and drop your site files to deploy on managed cloud hosting, with a secure connection and fast loading worldwide included."

### Jargon replacement table (for a non-professional reader)

| Instead of | Write |
|---|---|
| frontend | the part visitors see / the design |
| backend | the part that stores content and handles orders |
| API | a connection that lets one system request data from another |
| framework | the coding toolkit developers build with |
| decoupled | kept separate |
| monolithic | all in one system |
| global CDN | servers around the world / fast loading worldwide |
| auto-scaling | adds capacity when traffic rises |
| SSL | a secure connection |
| static site | a site built in code |
| per-API-call fees | a fee each time the site requests data |

---

## Block templates (change types)

Clone each from a live approved article before inserting (Gate 0).

- **A: "Domain registration with Wix" H2**, placed before the FAQ. Use the standard WHOIS-safe sentence from Gate 1d: "Beyond registration, Wix includes built-in tools for DNS management and domain security, along with a free SSL certificate to help protect your site and visitors. Wix also offers private registration to keep your contact details out of public records."
- **B: Top gate line** (from `cta-blocks.md`).
- **C: Main CTA paragraph + button** after the intro (from `cta-blocks.md`).
- **E1 intro / E2 TL;DR:** rules above.
- **E3 preview card:**
  ```json
  {"type":"LINK_PREVIEW","id":"<rid>","nodes":[],"linkPreviewData":{"containerData":{"alignment":"CENTER","textWrap":true},"link":{"url":"<blog url>","target":"TOP"},"title":"<post title>","thumbnailUrl":"https://static.wixstatic.com/media/{id}/v1/fill/w_920,h_608,al_c,q_85/{id}","description":"<post excerpt>"}}
  ```
  Title, excerpt and cover come from the target post.
- **E4 image:** which image and alt text from `image-rules.md`; placement rules in `formatting-audit.md`; use existing Media Manager files (media id + real width/height), never re-upload.
- **E5 remove iframe:** only with approval.
- **E6 encyclopedia links:** see `link-rules.md`.
- **E7 table:** header cells background `#3910ED`, text BOLD + white foreground, paragraph CENTER, no FONT_SIZE; body cells `tableCellData:{}`, foreground `rgb(0,0,0)`, paragraph AUTO; `tableData.dimensions.rowsHeight` per row, no `rowHeader`. Never put links inside a table.
- **E9 FAQ:** `COLLAPSIBLE_LIST`, 4 to 5 questions, no links. `COLLAPSIBLE_ITEM` > [`COLLAPSIBLE_ITEM_TITLE` > `HEADING` level 3 > TEXT] + [`COLLAPSIBLE_ITEM_BODY` > `PARAGRAPH`]. Live convention: body TEXT `decorations: []`, `initialExpandedItems:"FIRST"`. When converting plain H3 + paragraph pairs, capture **every** node between one H3 and the next and assert nothing was left unconsumed.
- **E10 learn-more:** a single link = bold on the whole phrase; multiple links = a real BULLETED_LIST under a bold "Learn more:" label.
- **Editor's note (prices):** italic (`{"type":"ITALIC","italicData":true}`), placed before the FAQ: *"Editor's note: prices are current as of <Month D, YYYY> and are subject to change at any time."* Refresh the date or add one if missing (see `verified-facts.md`).
