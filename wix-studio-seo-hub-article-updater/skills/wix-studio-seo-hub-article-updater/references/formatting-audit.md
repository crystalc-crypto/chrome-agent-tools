# Formatting audit (Gate 6) and whole-article formatting rules

Run on the **whole article** on every update, in code, before every publish. Fix every hit and re-run until the audit returns nothing. Present the hits (with the fix) in the approval message alongside the other changes. Pure mechanical fixes (spacing, decorations, link targets, em-dashes, spelling) can be grouped into one approval line; anything that removes or rewrites copy is listed individually.

---

## Gate 6 checklist

- **Spacing:** 2 empty paragraphs before every heading, 1 after; 2 after a button; 2 between the TL;DR list and the CTA image; 1 between all other blocks (no double gaps); 1 between a colon-ending body paragraph and its list; 0 between a short cue label and its list; 1 after "You'll learn:".
- **Heading decorations:** every HEADING's TEXT decorations are `[]`.
- **Pill button:** every BUTTON has `styles:{borderWidth:4,borderRadius:30}` (plus `buttonSize:"LARGE"` where the live convention uses it). `styles:{}` renders flat and is wrong. Trim whitespace in URL and text.
- **Buttons have a link:** `buttonData.link.url` is set on every BUTTON.
- **Main CTA destination:** the cluster's URL from `cta-blocks.md`; TLD page for single-TLD articles; the headless convention for the Headless cluster.
- **Long bullets not split**, paragraph-length bullets, buried "Tip:" runs, paragraphs over 320 characters, one-paragraph TL;DR.
- **`\n`, double spaces, em-dashes** anywhere.
- **"eCommerce"** anywhere, and mid-sentence "Ecommerce", in body AND schema (see `ecommerce-spelling.md`).
- **WHOIS** casing and WHOIS privacy wording in body AND schema (Gate 1d in `quality-gates.md`).
- **Links:** Wix links opening in a new tab; external links not new tab + noreferrer; anchors with a foreground COLOR; encyclopedia links; anchor/target mismatch (see `link-rules.md`).
- **Media:** adjacent media, images directly under a heading, missing or bad alt text.
- **Headings:** duplicate H2 text; stacked bare headings.

---

## Junk-node sweep (run before re-spacing)

```js
function isJunk(n) {
  if (n.type === 'HEADING' && txt(n).trim() === '') return true;
  if ((n.type === 'BULLETED_LIST' || n.type === 'ORDERED_LIST') && (!n.nodes || !n.nodes.length)) return true;
  if (n.type === 'BLOCKQUOTE' && txt(n).trim() === '') return true;
  return false;
}
```

## Deterministic re-spacing routine

Junk sweep, strip **every** empty PARAGRAPH, then rebuild in one pass:

- default **1** between blocks
- before a HEADING **2** (none if it is the first node)
- after a HEADING **1**
- after a BUTTON **2**
- between the TL;DR list and the following IMAGE **2**
- between a colon-ending body paragraph and its list **1**
- between a short cue label ("Learn more:", "Read more:", a bold-only label) and its list **0**
- after "You'll learn:" **1**

Rebuild from the stripped list, assert the invariant, and abort if any run of 3+ empties survives. Don't preserve old double gaps.

A body paragraph that ends with a colon ("…others can learn from:") is NOT a cue label: it keeps one empty paragraph before its list.

---

## Lists, subsections, paragraphs

- **Bullets over ~90 characters:** each bullet becomes its own single-item BULLETED_LIST with ONE empty paragraph between them. One-row bullets stay as one list.
- **Paragraph-length bullets** (3+ sentences or ~300+ characters) become subsections: a heading one level below the parent, named with the bold label; then a paragraph that starts with the term; fix lead-in counts ("these five steps").
- **"Tip:" runs** inside other blocks become their own paragraph.
- **Body paragraphs max 4 rows (~320 characters).** Split at natural sentence boundaries and keep back-references with their sentence. Never split inside a link run, the TL;DR or a direct quote. Rewrite single sentences over 320 characters into two.
- When splitting a paragraph with multiple styled runs, split at the sentence boundary and distribute the runs, splitting only the run that straddles the cut and preserving its decorations.
- Strip `\n` runs inside bullets and alt text. No double spaces.

## Headings

- Heading TEXT decorations are `[]`.
- **Find sections by true `HEADING` nodes only.** Articles repeat step names in an overview list near the top, so a text search can land in the overview. Verify by walking back to the nearest preceding HEADING.
- Numbered steps sit at one level; a step's subsections one level below.
- Break long sections into H3 subsections.
- No two H2s with the same text; rename the second to describe its own content.
- Summary tables go in the section they summarize, never directly under the TL;DR.
- Adding a second axis to a "types of X" section: add a grouping H3 plus a one-line bridge. Never stack two headings with no prose between them.

## Off-topic asides

"Good to know: / Did you know: / Worth a look:" paragraphs about unrelated domain extensions (.gratis on a free-hosting article, .systems on a hosting listicle) are off-topic. On every update, list any such asides and propose removing the ones unrelated to the article's topic. **Ask when unsure**, since they may belong to a TLD linking project. Judged live: .hosting on a cheapest-extensions article and .click on a domain-forwarding article were removed; .country on a ccTLD article and .support on a subdomain article were kept. (Pre-approved nuance blocks from `nuance-blocks.md` that start with "Good to know" or "Worth knowing" are NOT off-topic asides.)

---

## Images and preview cards: placement and spacing

Check the WHOLE article on every update, not only images you added.

- **Never place an image directly under a heading** (H2 or H3), even with empty paragraphs between them.
- **Move it to the END of its section:** the last block before the next heading of the same or higher level. If an H2 has H3 subsections, the section end is the end of the last H3 under that H2.
- **If the section ends with a learn-more element** ("Learn more:" / "Read more:" line, or label + list), place the image BELOW it.
- **At least 3 paragraphs** (non-empty body blocks; headings don't count) between any image or LINK_PREVIEW and the nearest other image or card, in both directions. The hero image and the CTA image after the TL;DR count as images.
- If the section end breaks the 3-paragraph rule, step back through the section to the last spot that satisfies it (never directly after a heading, never between a label and its list). If no spot works, leave the image and report it.
- **Spacing after a move:** 1 empty paragraph before the image (2 after a list), 1 after it (2 if a heading follows).
- **Two-pass move:** remove all images that need moving first, then place them, so a waiting image isn't counted against another one's spacing.
- After adding any image, check its neighbours. Move a second adjacent image or preview to the section it illustrates.
- **Alt text on every image** (full rules in `image-rules.md` Step 5): 2 to 5 words, descriptive, built around the primary or a secondary keyword, never starting with "image of" / "picture of", unique per image, no stuffing, WHOIS in capitals.
- Never remove or replace an existing image without approval.

## Preview cards from learn-more lines

- A body line with a cue label ("Learn more:", "Read more:", "Read also:", "Explore:") and exactly ONE link to a `www.wix.com/studio/blog/<slug>` post becomes a LINK_PREVIEW card.
- **Only when** no image, preview card or CTA (button, CTA paragraph, "Try Wix Headless" line) is the block directly before or after it, AND the card ends up at least 3 paragraphs from every other image or card. Lines that fail stay as text; report each skip and why.
- Work top to bottom and count each new card against the next candidates.
- Card data comes from the target post (`GET /blog/v3/posts/slugs/<slug>?fieldsets=URL`): `title`, `excerpt` as `description`, cover `media.wixMedia.image.id` as `thumbnailUrl` = `https://static.wixstatic.com/media/{id}/v1/fill/w_920,h_608,al_c,q_85/{id}`. `link.target` same tab (`TOP`, the live convention). Skip non-blog targets (product pages have no card data).
- Lines with 2+ links, and "Learn more:" label + list blocks, stay as lists.
- **Supplementary link lists:** convert only the LAST link of a list of 3+ items into a card, so a stranded single link isn't left behind; only when no image or CTA is adjacent.
- Several stacked single-link cue lines (mixed "Learn more"/"Read more", mixed bold) get merged into ONE bold "Learn more:" label followed directly by a bulleted list of capitalized descriptive anchors.
- Gate / transactional / CTA links never become cards.

---

## Writing style (whole article, not only new copy)

- **No em-dashes anywhere**, including pre-existing copy, quotes and quote attribution lines. Extract every em-dash with its surrounding text and choose per instance: comma for an appositive, semicolon or full stop between independent clauses, colon before a list, parentheses when the aside already contains commas. An em-dash inside an H3 title pattern becomes a colon. Quote attribution lines follow Gate 0 (copy the live convention) without an em-dash.
- **US spelling** ("organization", not "organisation"), even when the requester's draft uses British spelling.
- **"ecommerce"** rules from `ecommerce-spelling.md`, in body and `seoData` schema text. Judge sentence start on the whole block's text, not per TEXT run.
- Plain register (Gate 2) and neutral commercial tone (Gate 3 Check F).
- **Text matching:** live copy uses curly apostrophes (’) and non-breaking spaces; some URLs carry a leading space. Match by a distinctive, apostrophe-free substring with whitespace-tolerant regex, then replace the whole TEXT node. When a replacement doesn't fire, dump the TEXT nodes and their decorations rather than guessing again.
