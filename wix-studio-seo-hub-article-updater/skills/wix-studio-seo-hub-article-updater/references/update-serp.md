# Update Type: SERP Updater

Compares the target article against the top 5 ranking pages for its main keyword and GSC performance data to identify missing content sections, then lets the user review and approve proposed additions before pushing them live.

---

## Step 1: Ask for the main keyword

Ask the user (plain conversation, no `AskUserQuestion` needed): "What is the main keyword this article should rank for?"

Wait for their answer. This keyword drives the entire SERP analysis.

---

## Step 2: Pull data from Ahrefs and GSC in parallel

Run both in parallel:

**2a: Ahrefs SERP overview:**
```
mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__serp-overview
  → keyword: [user's keyword]
  → country: "us"
```
From the results, extract the top 5 organic results (positions 1–5): position, URL, title, traffic estimate.

**2b: GSC page history (performance check):**
```
mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__gsc-page-history
  → project_id: 3213842
  → pages: [article URL]
  → date_from: [3 months ago]
  → date_to: [today]
  → history_grouping: "monthly"
```
Note whether clicks, impressions, or CTR have been declining. This context informs which gaps are most urgent: prioritize sections that align with queries losing impressions.

Also run `gsc-keyword-history` for the main keyword to see position trend:
```
mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__gsc-keyword-history
  → project_id: 3213842
  → pages: [article URL]
  → date_from: [3 months ago]
  → date_to: [today]
```

---

## Step 3: Read the target article

If you haven't already read the article in this session:
1. `mcp__Claude_in_Chrome__navigate` → target article URL
2. `mcp__Claude_in_Chrome__get_page_text`
3. Extract: all headings (H1, H2, H3), topic coverage per section, FAQs present, key questions answered.

---

## Step 4: Read the top 5 ranking articles

For each of the 5 competitor URLs:

1. Try `WebFetch` first for speed.
2. If blocked (EGRESS_BLOCKED), use Chrome: `mcp__Claude_in_Chrome__navigate` + `mcp__Claude_in_Chrome__get_page_text`.
3. If neither works, extract maximum insight from the Ahrefs SERP snippet. Note it as "limited data" for that URL.

From each competitor page, record:
- All H2 and H3 headings
- Topics and subtopics covered
- FAQs or "people also ask" questions answered
- Any unique angles, data points, tools, or frameworks mentioned
- Approximate word count and depth

---

## Step 5: Gap analysis

Compare the target article's content structure against all 5 competitor pages. Identify:

**Missing sections**: H2/H3 topics that 2 or more competitor pages cover that the target article doesn't address at all. Highest priority.

**Underdeveloped sections**: Topics the target article touches on but where competitors go significantly deeper.

**Missing FAQs**: Questions that appear in competitor FAQ sections or "people also ask" patterns that the target article doesn't answer.

**Missing entities / angles**: Specific tools, concepts, or keywords that competitors mention prominently but are absent from the target article.

Rank gaps by: (1) frequency across the 5 competitors, (2) alignment with queries losing impressions in GSC, (3) relevance to the keyword's search intent.

---

## Step 6: Propose additions

For each gap, propose:

1. **What to add**: the section topic or question
2. **Where to add it**: after which existing section/paragraph, and why
3. **Draft text**: a complete, ready-to-publish paragraph or section: with a stat woven in where relevant (see Stats enrichment below)

**Stats enrichment (automatic, no separate approval):**

After drafting each proposed section, query board `18413546794` for a matching stat to strengthen the text:

```
mcp__5fcc3499-6805-42fd-8b00-4c15333bcf9f__get_board_items_page
  → boardId: "18413546794"
  → limit: 20
  → filters: [
      { "columnId": "color_mm3xw9k2", "operator": "any_of", "compareValue": [4] }
    ]
  → groupIds: [<most relevant group for this section's topic: see mapping below>]
```

Exclude any items from the "⏳ Pending Approval" group (`group_mm3w3532`).

**Group → topic mapping:**

| Section topic | Board group ID |
|---|---|
| Website building, small business | `group_mm3eg4vd` |
| eCommerce, online selling | `group_mm3e3f3b` |
| Dropshipping, affiliate marketing | `group_mm3ep3mr` |
| Print on demand, merch | `group_mm3evpac` |
| Domain names | `group_mm3ejsfk` |
| SEO, organic traffic | `group_mm3e1y8` |
| AI, website technology | `group_mm3enm2q` |
| Blogging, content marketing | `group_mm3ebgpe` |
| Mobile, web design | `group_mm3ekxhv` |
| Web hosting | `group_mm3e5nsx` |
| Video marketing | `group_mm3em88h` |

From the returned items, find the stat whose `Best used in articles about` column (`text_mm3ed3ps`) best matches the section topic. If a good match exists, weave the **pull-quote** (`long_text_mm3ee1rf`) naturally into the draft paragraph as a supporting sentence. The source name (`text_mm3epanc`) is hyperlinked to the source URL (`link_mm3ezewr`) and placed organically in the sentence.

Default pattern: "According to [Source](URL), [pull-quote]."
Fallbacks: "Data from [Source](URL) shows that [pull-quote]." / "[Source](URL) found that [pull-quote]."
If the pull-quote already contains "According to...", hyperlink the source name within that existing phrasing.

Source links are external: `target: "BLANK"` with `rel.noreferrer: true` (see `link-rules.md`).

Example: "Email marketing continues to deliver strong returns for small businesses. According to [Litmus](https://litmus.com/...), email generates $36 for every $1 spent, making it one of the highest-ROI channels available."

If no matching stat is found, or the match is weak, draft the paragraph without one: do not force a stat that doesn't fit.

**Writing guidelines for all proposed content:**

- **Answer search intent first.** After the TL;DR, move straight into the section that best answers the primary intent. Only include a "What is..." section if it's necessary for the reader to understand what follows: don't add it by default.
- **Wix placement.** Prioritize educational content over product promotion. Keep the first part of any new section focused on answering the question. Introduce Wix later, once the reader understands the topic.
- **Write for beginners.** Use simple, conversational language. Avoid unnecessary technical jargon. Explain complex concepts with concrete examples.
- **Keep paragraphs concise.** Short paragraphs that are easy to scan. Break up any section longer than three short paragraphs with a descriptive subtitle (H3).
- **SEO.** Naturally include the primary keyword and relevant secondary keywords in headings and content where it improves the article naturally. Use headings to target long-tail keywords when it's a genuine fit.
- **No em-dashes.** Never use em-dashes anywhere in the article, including existing copy (see `formatting-audit.md`). Use commas, colons, parentheses, or rewrite the sentence.

**Anchor text for new links:**
Any new blog links added in proposed content must use an approved anchor from board `5557032877` (KW column for the target post). Any new gate/transactional links must use an approved anchor from board `5817666262`. Keep anchor text exact: reshape the sentence to fit the anchor, not the other way around.

Present all proposals at once:

```
---
📌 GAP: [Section/Topic name]
Found in: [N]/5 competitor pages (positions X, Y, Z)
GSC signal: [declining impressions for related query / no signal]

**Where to add:** After the "[existing section name]" section, because [brief reason]

**Proposed heading:** [H2 or H3 heading text, if new section]

**Proposed text:**
[Full draft paragraph(s) ready to publish]

[APPROVE] | [EDIT] | [SKIP]
```

---

## Step 7: User review and editing

Tell the user: "Here are [N] content gaps I found. For each one, reply APPROVE to use my draft, EDIT followed by your revised text to use your version, or SKIP to leave it out."

Wait for their responses. Allow them to provide their own text for any item: their version takes precedence over the draft.

Build a final list of approved additions with confirmed placements and final text.

---

## Step 8: Push to Wix blog

Follow **Phase 7** of the main SKILL.md to push all approved additions. Each addition is an **insertion**: new content inserted after the identified anchor point. Never remove existing content unless the user explicitly instructs it.

After pushing: "✅ [N] content additions published to [article title]. The article now covers topics found in the top-ranking pages for '[keyword]'."

---

## Tips

**EGRESS_BLOCKED is the norm.** Most competitor domains block WebFetch. Use Chrome for reading competitor pages.

**Don't invent data.** Only report gaps you actually found. If you couldn't read a competitor page, note it as limited data.

**Structure-first.** The value here is finding structural gaps (missing sections, missing questions), not just missing sentences. Propose complete sections with headings.

**Intent matters.** If the competitor section covers a tangential topic that doesn't serve the article's core keyword intent, don't recommend adding it just because 3 competitors have it.

**GSC informs priority.** If GSC shows impressions dropping for a specific query, and a competitor ranks for it with a section the article lacks, that gap is the highest priority regardless of how many competitors have it.
