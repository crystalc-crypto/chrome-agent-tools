# Post-publish verification and reporting

**Don't declare done because the PATCH succeeded.** Re-GET the draft (`?fieldsets=RICH_CONTENT`, plus `SEO` if schema changed) and the live post, and assert every line below. Fix and republish until all pass.

## Assertions

- **Gate 1:** ledger complete; every top-of-article figure is KEEP.
- **Gate 2:** 0 sensationalism regex hits.
- **Gate 3:** checks A, B, E and F satisfied; echo < 5 measured with the correct intro window; TL;DR heading casing correct at level 2; Check G shape (one paragraph, 2 sentences, 35 to 50 words).
- **Gate 4:** word count >= expected; no stacked bare headings; every intended insertion actually present.
- **Gate 1d:** 0 WHOIS privacy "free / included" wording and 0 lowercase "whois" in body AND schema.
- 0 em-dashes.
- 0 unresolved `/encyclopedia/definition/` URLs (verified non-redirecting terms excepted).
- 0 `wix.com` links with `target:"BLANK"`; every external link `target:"BLANK"` + `rel.noreferrer:true`.
- 0 anchors with a foreground COLOR.
- 0 "eCommerce" and 0 mid-sentence "Ecommerce", in body and schema.
- Every HEADING has 2 empty paragraphs before and 1 after.
- 0 images directly under a heading; every image and LINK_PREVIEW at least 3 paragraphs from the next image or card.
- Every BUTTON has `buttonData.link.url`; pill styles present.
- **Images (`image-rules.md` Step 7):** each image in the approved plan is in place with its alt text; the main CTA image sits after the TL;DR; every CTA image links to the cluster CTA URL with `target:"SELF"`; the cover is set; every image has 2 to 5 word alt text.
- Every blog link that was in the old intro/TL;DR appears exactly once in the article.
- `firstPublishedDate` is today (or the approved date), except for an approved silent fix.
- Prices match this session's source; the editor's note is italic and dated.
- Monday item and cluster date verified (see `monday-logging.md`).

## Final report (short)

The report is a handover, not a narrative:

1. **What was updated**, one line per article.
2. **Claim ledger** (or "0 claims"), the **Gate 5b coverage summary** if not already shown, and the **final image list with open image flags** (missing folder and fallback used, placeholder, no infographic, infographic awaiting approval).
3. **Unsolved problems and anything dropped**, with the reason.
4. **Links to every updated post**, always, at the end: `https://www.wix.com/studio/blog/<slug>`.

No step-by-step recap, no restating instructions, no describing tool calls. If a fix needed three attempts, report the outcome. Always surface a correction to something previously reported as done.

## If a gate breach ships anyway

Own it plainly, fix it, then **sweep every article touched in the same run (or the remaining state-file queue already processed this session) for that class of error**, not just the reported one. Evidence: the batch with one invented figure also held another invented figure and three unverified superlatives; the Gate 3 sweep found 20 of 30 articles echoing their own intros; the bare-heading bug hit all 10 in its batch.

## Multi-round feedback is a signal

If the same person flags the same section twice, the first fix satisfied one requirement and broke another. Re-read the original instruction, list EVERY requirement as a separate checkable item, and verify against all of them at once. Also check whether the fix already shipped and was never reported. Always close a turn by stating what changed.
