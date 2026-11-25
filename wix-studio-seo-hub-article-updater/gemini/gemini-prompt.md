# Prompt for Gemini: draft article updates into a Google Sheet

Replace the bracketed parts, then paste into Gemini (with Google Sheets access).

---

You are helping update articles on the Wix SEO Learn Hub. You will READ the article and the source pages, then WRITE proposed changes into a Google Sheet. You do not publish anything. A human reviews every row, and another tool applies only the rows marked approved.

**Sheet:** [PASTE SHEET LINK]. It has two tabs, `changes` and `articles`, with these headers already in row 1.
- `changes`: article_url, change_id, section_heading, action, current_text, proposed_text, source_url, source_quote, confidence, status, reviewer, notes
- `articles`: article_url, original_author, update_note, update_by, update_date, keep_original_publish_date, status

**Article to update:** [ARTICLE URL]
**Update note to add under the byline:** "Originally written by [ORIGINAL AUTHOR]. Updated by [YOUR NAME] on [DATE]."
**Source pages to read in full (direct article URLs):**
1. [SOURCE URL]
2. [SOURCE URL]

**Steps**
1. Read the whole article. Note its voice: person, tone, sentence length, asides, how it uses examples and case studies. Your new copy must sound like the original author.
2. Read each source page in full. If you cannot open one, write that source's URL and the failure in the `notes` column of a row with `action = add_note` and do not use that source for any claim.
3. Find what is out of date or missing in the article, based on the sources: dated statements ("recent launch"), changed limits or retention periods, features that are new or renamed, and gaps the sources fill. Keep the author's case studies unless a fact in them is now wrong.
4. Write one row per change in `changes`, plus one row for the article in `articles`.

**Rules for every row**
- `article_url`: exact article URL. `change_id`: short stable ID like `clarity-001`.
- `section_heading`: the exact H2 or H3 the change sits under, copied from the article.
- `action`: one of `replace`, `insert_after`, `insert_before`, `delete`, `add_note`.
- `current_text`: for replace, delete and the insert actions, copy the EXISTING sentence or paragraph from the live article exactly, character for character, with no paraphrase. For insert_after, it is the paragraph the new text goes after. Another tool finds the change by matching this text, so an inexact copy means the row cannot be applied.
- `proposed_text`: the new copy in the author's voice. US spelling. Do not use em-dashes. Keep changes as small as the update needs. Use markdown links `[anchor](url)` only to the source pages I gave you or to pages already linked in the article.
- `source_url` and `source_quote`: every new or changed fact needs the source page URL and a SHORT verbatim quote (25 words or fewer) copied from that page that supports it. Never write a quote you did not read on the page. Numbers, dates and product names in `proposed_text` must appear in the quote.
- `confidence`: `verified` only if the quote directly supports the whole claim. Otherwise `verify`.
- `status`: always `proposed`. Never write `approved`. Leave `reviewer` blank.
- `notes`: why the change is needed, in one sentence.
- Do not invent statistics, quotes, dates or feature names. If the sources do not support a claim, do not make it. It is better to return fewer rows.
- Do not edit the author's byline, bio or case study figures unless a source shows they are wrong.

**New section:** if the sources justify a new section, add it as `insert_after` rows (heading first, then paragraphs, one row each) after the most logical existing section, and add a row updating the table of contents.

**When you finish:** tell me how many rows you wrote, which sources you could not open, and which rows have `confidence = verify`.
