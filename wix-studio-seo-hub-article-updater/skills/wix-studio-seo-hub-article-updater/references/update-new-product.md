# Update Type: New Product Update (Semantic Triples)

Inserts semantically appropriate product triples from the live Monday triples board into the target article.

---

## Step 1: Ask which product to update

Read `references/products.md` and present the available products as a single-select `AskUserQuestion`. The user must choose exactly one product per run of this update type.

If the article's cluster is already known from Phase 1, pre-select the mapped product and ask the user to confirm rather than re-asking from scratch.

---

## Step 2: Fetch triples from Monday board 18411488466

Use the group ID for the chosen product from `references/products.md`.

**Step 2a: Fetch items from the group:**
```
mcp__5fcc3499-6805-42fd-8b00-4c15333bcf9f__get_board_items_page
  → boardId: "18411488466"
  → limit: 50
  → filters: [{ "columnId": "group_id", "operator": "any_of", "compareValue": ["<group_id>"] }]
```

**Step 2b: Extract triples from each item:**

Each item may have up to 10 triple columns. Read all non-empty ones:

| Column ID | Label |
|---|---|
| `long_text_mm31s9x6` | Semantic Triple 1 |
| `long_text_mm31t4kd` | Semantic Triple 2 |
| `long_text_mm316m2x` | Semantic Triple 3 |
| `long_text_mm315pxn` | Semantic Triple 4 |
| `long_text_mm3158r4` | Semantic Triple 5 |
| `long_text_mm31nktt` | Semantic Triple 6 |
| `long_text_mm31t89f` | Semantic Triple 7 |
| `long_text_mm31z23k` | Semantic Triple 8 |
| `long_text_mm31anxc` | Semantic Triple 9 |
| `long_text_mm31es0m` | Semantic Triple 10 |

Also note the item's `Priority` column (`numeric_mm318n0h`) and `OG Cluster` column (`text_mm31qaew`): use these for selection in Step 4.

**Step 2c: Refine by OG Cluster (soft filter):**

Compare each item's `OG Cluster` value against the article's specific cluster. Prefer items where OG Cluster matches or is closely related. If no items match on OG Cluster, use all items from the group.

**Error handling:** If the board is unreachable, stop and tell the user: "The triples board is unreachable. Please reconnect Monday.com in Settings → Connectors." Do not invent triples.

---

## Step 3: Read the article content

If you haven't already read the article in this session:
1. `mcp__Claude_in_Chrome__navigate` → the target article URL
2. `mcp__Claude_in_Chrome__get_page_text` → capture full text
3. Identify the first fold: the intro paragraph(s) and content before the first H2 heading.
4. Note all section headings (H2, H3) in order: you'll use these to identify the best insertion points.
5. Scan the article for any triples already present: a triple is a sentence where Wix is the subject, the product is the object, and a benefit/capability is stated. Record which triples (or semantically equivalent sentences) are already in the article so you don't duplicate them.

---

## Step 4: Select 2 semantic triples

From the fetched triples, pick 2 that:
- Are **not already present** in the article (or semantically equivalent to something already there)
- Are the **best thematic fit** for the article's content and structure
- Have the highest **Priority** value if multiple triples are equally relevant

Present them to the user in a clear numbered list:

```
Here are 2 semantic triples I'd like to add:

**Triple 1:**
"[triple text]"
→ Would insert after: [section name / paragraph description]

**Triple 2:**
"[triple text]"
→ Would insert after: [section name / paragraph description]
```

Then ask (plain text question, not `AskUserQuestion`): "Do you approve these, or would you like me to choose 2 different ones?"

---

## Step 5: Handle the approval loop

- If the user **approves**: proceed to Step 6.
- If the user says **"choose again"** or similar: select 2 different triples from the fetched set (don't repeat already-shown ones). Re-present and ask again. Continue until the user approves or all options are exhausted.
- If you run out of unused triples: tell the user and ask if they'd like to reuse any previously shown ones.

---

## Step 6: Determine insertion points

For each approved triple, find the best insertion point in the article:

- The triple must appear **no lower than the first fold** (i.e., within the intro or first H2 section). If the best thematic match is deeper in the article but the first-fold requirement isn't met, place a version of the triple in the first fold as well.
- **Branded vs non-branded (Gate 1c):** in a non-branded informational article, never put the triple in the intro paragraphs; use the main CTA paragraph or the first body section after the TL;DR. In general sections, explain the concept first and bring Wix in last as an example (`article-structure.md`).
- Any figure in a triple that lands in the intro or TL;DR must pass the claim ledger (Gate 1).
- Look for a paragraph that discusses the same topic the triple covers.
- The triple should read naturally: insert it as a new sentence at the end of a paragraph or as its own sentence within a paragraph. Avoid awkward juxtapositions.

Confirm insertion points with the user before proceeding:

```
**Insertion plan:**
- Triple 1: Insert at the end of the intro paragraph (currently ends with "...")
- Triple 2: Insert after the paragraph in "[H2 section name]" that starts with "..."
```

Ask: "Does this placement look right, or would you like to adjust?"

---

## Step 7: Push to Wix blog

Once placements are approved, follow **Phase 7** of the main SKILL.md to push the changes to the Wix blog. This includes Step 7d: always ask the user to approve the publish date before pushing. The edit is: insert each approved triple sentence at its confirmed location in the article content.

After pushing, confirm: "✅ [N] semantic triples added to [article title] and published on [date]."
