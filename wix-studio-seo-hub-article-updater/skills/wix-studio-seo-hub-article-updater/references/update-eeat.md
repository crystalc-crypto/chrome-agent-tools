# Update Type: EEAT Updater

Adds expert quotes to a blog article to strengthen its Experience, Expertise, Authority, and Trust (EEAT) signals. Quotes are sourced from the unified Wix Blog Quotes Library on Monday, then inserted into the article with full attribution (name + role/title).

---

## Quote source

**Board:** `18413807018`: "Wix Blog: Official Quotes Library (EEAT)"
407 items. All groups are usable **except** "To be reviewed" (group ID: `topics`): skip all items from that group.

**Board structure:**
- `name`: Person's name + title (e.g. "Jane Smith, Head of SEO at Wix")
- `color_mm3gy1y6`: Source type: Internal (1), External (2), User (3)
- `color_mm3gszgt`: Topic tag (see tag IDs below)
- `text_mm3g9qxw`: Quote 1: credibility description ("what makes this person credible"): use for attribution context, NOT as a quote
- `long_text_mm3gc56c`: Quote 2: strongest verbatim quote, ready to use ✅
- `long_text_mm3g91pc`: Quote 3: second verbatim quote ✅
- `long_text_mm3gqd9j`: Quote 4: third verbatim quote ✅
- `long_text_mm3g4kqc`: Quote 5: extractable facts (for experts only)
- `long_text_mm3g7v16`: Quote 6: ready-to-paste attribution line ✅
- Quote 7–15: additional text columns: read if populated

**Board groups (all usable except "To be reviewed"):**
- `group_mm3gjs63`: Website building & design
- `group_mm3g3re0`: Domains, hosting & infrastructure
- `group_mm3gkc6e`: Blogging & content
- `group_mm3g7j48`: Business & eCommerce
- `group_mm3gd9rz`: Marketing
- `group_mm3grp9t`: AI & Apps
- `group_mm3gfj48`: Wix Studio
- `group_mm3g18bg`: Base44
- `group_mm4tzqrx`: Wix Headless
- `group_mm5668n0`: Symphony by Wix

---

## Step 1: Identify the article's topic and relevant quote tags

If you haven't already read the article in this session:
1. `mcp__Claude_in_Chrome__navigate` → article URL
2. `mcp__Claude_in_Chrome__get_page_text`
3. Note: article title, all H2/H3 headings, key topics covered, and the sections most likely to benefit from an expert voice (introductions of key concepts, sections making strong claims, tips/best practices sections).

Map the article's topic to the 1–3 most relevant Topic tag IDs:

| Topic | Tag ID |
|---|---|
| Website (creation, design, builder) | `1` |
| Marketing | `2` |
| Wix Harmony | `3` |
| Wixel (logo) | `4` |
| Apps | `5` |
| Logo | `6` |
| AI | `7` |
| Infrastructure | `8` |
| Domains | `9` |
| Blogging | `10` |
| Business | `11` |
| eCommerce | `12` |
| Base44 | `13` |
| Wix Studio | `14` |
| Wix Headless | `15` |
| Symphony | `16` |

---

## Step 2: Ask which source types to include

Ask the user (plain conversation, no `AskUserQuestion` needed):

> "I'll find expert quotes to add to this article. Should I pull from:
> 1. Internal Wix experts only
> 2. External experts only
> 3. Wix users only
> 4. All types (recommended)"

Default to "all types" if they say "yes" or "go ahead."

---

## Step 3: Fetch quotes from the board

```
mcp__5fcc3499-6805-42fd-8b00-4c15333bcf9f__get_board_items_page
  → boardId: "18413807018"
  → limit: 50
  → filters: [
      { "columnId": "color_mm3gszgt", "operator": "any_of", "compareValue": [<relevant tag id(s)>] }
    ]
```

After fetching, manually exclude any items from the "To be reviewed" group (`topics`).

If the user selected specific source types, further filter by `color_mm3gy1y6`: Internal=1, External=2, User=3.

From each item, extract:
- `name` → expert name + title (item name field)
- `text_mm3g9qxw` → credibility context (use for attribution, not as a quote)
- `long_text_mm3gc56c`, `long_text_mm3g91pc`, `long_text_mm3gqd9j` → verbatim quotes (use these)
- `long_text_mm3g7v16` → ready-to-paste attribution line
- Source type from `color_mm3gy1y6`

---

## Step 4: Curate and present quote candidates

After fetching, filter down to the **3–6 most relevant quotes**. Relevance criteria:
- The quote speaks directly to a topic the article covers
- The quote adds genuine insight or authority (not a marketing slogan)
- The speaker's expertise matches the article's subject matter

Present candidates clearly, one per item:

```
---
💬 QUOTE CANDIDATE [N]
Source: [Group name]
Type: [Internal / External / User]
Expert: [Full name], [Title/Role]

Credibility: [Quote 1 content: why this person is credible]

"[Best verbatim quote: Quote 2, 3, or 4]"

Best placement: After the "[section name]" section: because [brief reason why this expert voice adds value here]

[USE] | [SKIP]
```

If you found more quotes than you're presenting, note: "I also found [N] additional quotes: let me know if you'd like to see more."

---

## Step 5: User review and placement confirmation

Tell the user: "Here are [N] expert quotes I found for this article. Reply USE or SKIP for each. For any you USE, I'll add it after the suggested section: or tell me a different placement."

Wait for their responses. Allow the user to specify a different placement for any quote they approve.

Build a final list of approved quotes with confirmed placements.

---

## Step 6: Format quotes for the blog

Each approved quote is inserted as a **BLOCKQUOTE node** followed by an **attribution paragraph**. In Ricos format:

```json
// Empty spacing paragraph before (always include)
{ "type": "PARAGRAPH", "id": "<rid>", "nodes": [], "paragraphData": {} }

// The blockquote
{ "type": "BLOCKQUOTE", "id": "<rid>", "nodes": [
    { "type": "PARAGRAPH", "id": "<rid>", "nodes": [
        { "type": "TEXT", "id": "", "nodes": [],
          "textData": { "text": "[quote text]", "decorations": [{ "type": "COLOR", "colorData": { "background": "transparent" } }] } }
      ], "paragraphData": { "textStyle": { "textAlignment": "AUTO" } } }
  ]
}

// Attribution line
{ "type": "PARAGRAPH", "id": "<rid>", "nodes": [
    { "type": "TEXT", "id": "", "nodes": [],
      "textData": { "text": "[Full Name], [Title/Role]", "decorations": [{ "type": "COLOR", "colorData": { "background": "transparent" } }] } }
  ], "paragraphData": { "textStyle": { "textAlignment": "AUTO" } }
}

// Empty spacing paragraph after: only if the next existing node is not already an empty paragraph
{ "type": "PARAGRAPH", "id": "<rid>", "nodes": [], "paragraphData": {} }
```

**Attribution format rules:**
- Copy the attribution format from a live approved article with an expert quote first (Gate 0 in `quality-gates.md`). Never use an em-dash in the attribution line.
- Always include full name and role/title: `Jane Smith, Head of SEO at Wix`
- For External source type: include their company: `John Doe, CEO of Example Co.`
- For User source type: use `[Name], Wix user`
- Use Quote 6 (ready-to-paste attribution line) if populated, removing any leading em-dash
- Never omit the attribution: a blockquote without a named, credentialed expert does not serve EEAT
- Never edit a figure inside a direct quote (Gate 1)

---

## Step 7: Push to Wix blog

Follow **Phase 7** of the main SKILL.md to push all approved quote insertions. Each quote is an **insertion** at the confirmed anchor point.

After pushing: "✅ [N] expert quote(s) added to [article title]. The article now includes attributed quotes from: [list of expert names]."

---

## Tips

**Quality over quantity.** 1–2 well-placed quotes from genuine experts are more valuable than 5 generic ones.

**Placement matters for EEAT.** The most impactful spots are: (a) early in the article, lending credibility to the core premise; (b) in sections making strong claims or recommendations; (c) in tips/best practices sections where expert validation helps the reader trust the advice.

**Don't stack quotes.** Avoid placing multiple quotes in the same section or back-to-back. Each quote should have room to breathe and clearly support the content around it.

**The attribution line is non-negotiable.** A blockquote without a named, credentialed expert doesn't help EEAT.

**No em-dashes anywhere.** Not in quotes, attribution lines or surrounding text. Use commas, colons, parentheses or rewrite the sentence (see `formatting-audit.md`).
