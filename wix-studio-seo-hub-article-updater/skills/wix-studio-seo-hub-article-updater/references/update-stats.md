# Update Type: Stats Updater

Scans the article for existing paragraphs that make broad or unsupported claims, fetches matching pre-approved statistics from the Wix Blog Statistics Library, and inserts them inline as natural supporting sentences. No per-stat approval: all stats on this board are pre-checked. A summary is shown before pushing.

---

## Stats source

**Board:** `18413546794`: "Wix Blog: Statistics Library (EEAT)"
440 items. EN only. Exclude "⏳ Pending Approval" group (`group_mm3w3532`).

**Column map:**
- `long_text_mm3e1jnm`: The stat (raw)
- `long_text_mm3ee1rf`: Pull-quote (copy-paste ready) ✅ use this
- `text_mm3epanc`: Primary source (for attribution)
- `link_mm3ezewr`: Source URL
- `text_mm3esm6v`: Data year
- `text_mm3ed3ps`: Best used in articles about (for matching)

**Group → topic mapping:**

| Topic | Group ID |
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

---

## Step 1: Map the article's content bucket to board groups

Based on the content bucket from Phase 1 of SKILL.md, determine which board groups are most relevant for this article:

| Content Bucket | Primary groups to query |
|---|---|
| How to make a website | `group_mm3eg4vd`, `group_mm3ekxhv` |
| Website examples | `group_mm3eg4vd`, `group_mm3ekxhv` |
| Branded | `group_mm3eg4vd` |
| How to start a business | `group_mm3eg4vd`, `group_mm3e3f3b` |
| Business names | `group_mm3eg4vd`, `group_mm3ejsfk` |
| Business ideas | `group_mm3eg4vd`, `group_mm3e3f3b` |
| Domains | `group_mm3ejsfk` |
| eCommerce | `group_mm3e3f3b` |
| Dropshipping | `group_mm3ep3mr` |
| Print on demand | `group_mm3evpac` |
| Portfolio | `group_mm3eg4vd` |
| Blog | `group_mm3ebgpe` |

---

## Step 2: Read the article

If you haven't already read the article in this session:
1. `mcp__Claude_in_Chrome__navigate` → article URL
2. `mcp__Claude_in_Chrome__get_page_text`
3. Walk through the article and identify **3–5 target paragraphs**: paragraphs that:
   - Make a broad or unsubstantiated claim ("businesses that blog get more traffic", "email marketing is effective", "most shoppers abandon carts")
   - State a trend or pattern without citing evidence
   - Could be meaningfully strengthened by a real data point
   - Do **not** already contain a number, percentage, or citation

Avoid: intro paragraphs, TL;DR, CTA sections, headings, and paragraphs that already contain statistics.

---

## Step 3: Fetch stats from the board

For each relevant group (from Step 1), fetch up to 20 EN stats:

```
mcp__5fcc3499-6805-42fd-8b00-4c15333bcf9f__get_board_items_page
  → boardId: "18413546794"
  → limit: 20
  → filters: [
      { "columnId": "color_mm3xw9k2", "operator": "any_of", "compareValue": [4] }
    ]
  → groupIds: ["<group_id>"]
```

Run queries for each relevant group in parallel. After fetching, exclude any items from group `group_mm3w3532` (Pending Approval).

From each item, extract:
- `long_text_mm3ee1rf` → pull-quote text (what gets inserted)
- `text_mm3epanc` → primary source (for attribution)
- `text_mm3esm6v` → data year
- `text_mm3ed3ps` → best used in articles about (for matching)

---

## Step 4: Match stats to paragraphs

For each of the 3–5 target paragraphs identified in Step 2, find the stat whose `Best used in articles about` field most closely matches the paragraph's specific topic.

Matching rules:
- One stat per paragraph: do not insert two stats into the same paragraph
- Do not use the same stat twice in one article
- If no stat matches a paragraph well enough to feel natural, skip that paragraph: do not force a stat that doesn't fit the surrounding text

---

## Step 5: Draft the insertions

For each matched stat, write a natural sentence that weaves the pull-quote into the existing paragraph. The stat should support or illustrate the claim already being made: not contradict it or introduce a tangential point.

**Insertion format:**
The stat sentence goes inside the existing paragraph: either at the end of it, or directly after the sentence making the claim it supports. Do not create a new paragraph.

**Attribution format: organic inline link:**
The source name is hyperlinked to the source URL (`link_mm3ezewr`) and woven naturally into the sentence. Default pattern:

> "According to [Source](URL), [pull-quote text]."

Use the data year in parentheses after the pull-quote only if it adds meaningful context (e.g. the stat is time-sensitive). Otherwise omit it.

**Fallback patterns** for cases where the default reads awkwardly:
- Pull-quote already starts with "According to..." → hyperlink the source name within the existing phrasing instead of prepending
- Pull-quote is a question or imperative → use "Data from [Source](URL) shows that [pull-quote]." or "[Source](URL) found that [pull-quote]."
- Source is a well-known body (e.g. "McKinsey", "Statista") → "A [Source](URL) study found that [pull-quote]." also works

Example: existing paragraph: "Email is one of the most effective ways to stay in touch with your customers and drive repeat sales."
After insertion: "Email is one of the most effective ways to stay in touch with your customers and drive repeat sales. According to [Litmus](https://litmus.com/...), for every $1 spent, email marketing generates an average of $36 in return."

**In Ricos,** the hyperlinked source name is a separate TEXT node with a LINK decoration (`target: "BLANK"` + `rel.noreferrer: true`, external site), immediately followed by a plain TEXT node with the rest of the stat sentence:

```json
// TEXT node: "According to "
{
  "type": "TEXT", "id": "", "nodes": [],
  "textData": {
    "text": "According to ",
    "decorations": [{ "type": "COLOR", "colorData": { "background": "transparent" } }]
  }
}
// TEXT node: linked source name
{
  "type": "TEXT", "id": "", "nodes": [],
  "textData": {
    "text": "[Primary source name]",
    "decorations": [
      {
        "type": "LINK",
        "linkData": { "link": { "url": "[source URL]", "target": "BLANK", "rel": { "noreferrer": true } } }
      },
      { "type": "COLOR", "colorData": { "background": "transparent" } }
    ]
  }
}
// TEXT node: rest of sentence
{
  "type": "TEXT", "id": "", "nodes": [],
  "textData": {
    "text": ", [pull-quote text].",
    "decorations": [{ "type": "COLOR", "colorData": { "background": "transparent" } }]
  }
}
```

Append these three TEXT nodes to the target PARAGRAPH's `nodes` array (after its existing TEXT children).

**No em-dashes** in the inserted sentence. Use commas, colons, or parentheses instead.

---

## Step 6: Show summary and confirm

Present a summary table of all planned insertions before pushing:

```
📊 STATS TO ADD: [N] insertions planned

| # | Paragraph (first 10 words) | Stat to insert | Source |
|---|---|---|---|
| 1 | "Email is one of the most..." | "For every $1 spent, email..." | Litmus, 2025 |
| 2 | "Most online shoppers will..." | "69% of online shopping carts..." | Baymard, 2025 |
...

Ready to insert all [N] stats? Reply YES to push, or tell me which numbers to skip.
```

Wait for the user to reply. If they say YES (or equivalent), push all. If they name specific numbers to skip, exclude those and push the rest.

---

## Step 7: Push to Wix blog

Follow **Phase 7** of the main SKILL.md to push all insertions. Each stat is a **text modification**: the stat sentence is added to the end of (or within) the existing paragraph's TEXT nodes.

**In Ricos format**, this means locating the target PARAGRAPH node, finding its last TEXT child node, and appending the stat sentence to `textData.text`. Keep all existing decorations intact.

If the paragraph has multiple TEXT children (e.g. some text is bold or linked), append a new plain TEXT child node with the stat sentence and attribution:

```json
{
  "type": "TEXT",
  "id": "",
  "nodes": [],
  "textData": {
    "text": " [Stat sentence]. ([Primary source], [Data year])",
    "decorations": [
      { "type": "COLOR", "colorData": { "background": "transparent" } }
    ]
  }
}
```

Push all insertions in a single PATCH call.

After pushing: "✅ [N] stats added to [article title]. Sources: [list of primary sources used]."

---

## Tips

**Quality over quantity.** 2–3 well-matched stats are better than 5 forced ones. If the article doesn't have 3 good candidate paragraphs, insert fewer.

**The pull-quote is ready to use.** Don't rephrase it: the pull-quote column already contains copy-paste-ready text. You can trim it if it's too long, but don't rewrite it.

**The attribution is non-negotiable.** Every stat must carry its source and year in parentheses. A stat without attribution undermines EEAT rather than supporting it.

**Don't stack stats.** One stat per paragraph. Two statistics in the same paragraph reads as data-dumping, not evidence-based writing.
