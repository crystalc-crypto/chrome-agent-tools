# Update Type: Accurate Product Update

Cross-checks the article's Wix product claims against official Wix support documentation, flags inaccuracies for user review and approval, then optionally inserts a nuance block adjacent to any claim that needs balancing.

---

## Step 1: Ask which product this article should support

Use `AskUserQuestion` with these options:

1. Website builder
2. AI website builder / Wix Harmony
3. Wix Ecommerce
4. Portfolio
5. Blog
6. Selling online
7. Domains
8. Symphony
9. Headless

The user must choose one. This tells you which product lens to apply when cross-referencing the article.

---

## Step 2: Read the article

If you haven't already read the article in this session:
1. `mcp__Claude_in_Chrome__navigate` → the target article URL
2. `mcp__Claude_in_Chrome__get_page_text` to capture full text
3. Identify and list every sentence or paragraph that:
   - Names the selected product specifically (or Wix generally)
   - Makes a feature claim ("Wix lets you do X")
   - States a limitation or capability ("you can/can't...")
   - Describes UI elements or steps in the product
   - Mentions pricing, plans, or availability

Build a checklist of these "product claim sentences": you'll cross-reference each one against the support docs.

---

## Step 3: Find relevant Wix support articles

Search for official support documentation about the chosen product. Run both in parallel:

1. `WebSearch` with query: `[product name] site:support.wix.com` and `allowed_domains: ["support.wix.com"]`
2. Navigate to `https://support.wix.com/en` in Chrome and search for the product name if web search returns thin results.

Prioritize finding:
- An overview or "introducing" article for the product
- A features/capabilities article
- A limitations or known issues article
- A "getting started" guide
- Any FAQ or comparison article

Read 3–5 of the most relevant articles using Chrome browser tools (`navigate` + `get_page_text`). From each support article, extract:
- All confirmed features and how they work
- Explicit limitations (what's not supported, what's "coming soon", region/language restrictions)
- Pricing or plan requirements
- UI locations or step-by-step flows
- Any deprecations or changes from previous versions

---

## Step 4: Compare and flag inconsistencies

Go through each "product claim sentence" from Step 2 and compare it to what the support docs say.

Flag a sentence if:
- It claims a feature the support docs say doesn't exist or isn't available yet
- It omits an important limitation the support docs explicitly state
- It describes a UI flow that no longer matches the current product
- It uses outdated terminology or product names
- It makes a capability claim that goes beyond what support docs confirm

**Do not flag**: general marketing language, promotional phrasing, or claims that are directionally accurate even if not verbatim from support docs. Focus on things a reader would genuinely be misled by.

---

## Step 5: Present inconsistencies and recommended edits

For each flagged issue, present it in this format:

```
---
⚠️ INCONSISTENCY FOUND

**Current text in article:**
"[exact quote from article]"

**What the support docs say:**
[1–2 sentence summary of what support.wix.com says instead]
Source: [support article URL]

**Recommended edit:**
"[replacement text]"

[APPROVE] or [EDIT YOURSELF] or [SKIP]
```

Show all flagged items at once so the user can review the full scope before approving anything.

Then ask: "Please review these [N] inconsistencies. Type APPROVE next to each one you want to push, or type your own replacement text to override my suggestion. Type SKIP to leave any item unchanged."

---

## Step 6: Collect approvals

Wait for the user to respond with their decisions. Parse their response:
- `APPROVE` next to an item → use the recommended edit text
- Custom text next to an item → use the user's text instead
- `SKIP` → do not change that item

Build a final list of confirmed edits (original text → replacement text).

---

## Step 7: Nuance block check

After collecting all approved edits, review the article and the corrections together to determine whether any corrected or confirmed claims need a nuance block.

**Rules for inserting a nuance block (all three must be true):**

1. **The claim needs balancing.** Either the article is strongly positive about a feature (an honest limitation block adds credibility) or it addresses a pain point or sceptical question (a positive surprise block rebalances it). If the section is already balanced, no block is needed.

2. **The block adds new information.** If the article already addresses the limitation or capability the block covers, inserting it is redundant. Only propose a block when it adds something the reader wouldn't otherwise get from the article.

3. **The block matches the specific claim**: not just the general topic. An ecommerce article about setting up a store gets a different block than an article about scaling one, even though both are ecommerce.

**Volume cap:** Maximum 2 nuance blocks per article. Default is 1. Count any nuance blocks already present in the article (identify them by their opener patterns: "Worth knowing:", "One honest note:", "A practical note:", "Good to know:", "Something to factor in:", "Something worth knowing:", "One thing worth knowing:", "Genuinely underused:", "Not obvious but genuinely useful:", etc.). If the article already has 2 or more nuance blocks, skip this step entirely.

**If a nuance block is warranted:**

1. Open `references/nuance-blocks.md` and find the cluster section that matches the article's product topic.
2. Identify the block whose specific claim most closely matches the section being corrected or confirmed.
3. Present the candidate block to the user:

```
---
💡 NUANCE BLOCK SUGGESTION

For the section about [topic]:

Type: [Honest limitation / Positive surprise / Practical context]

Proposed block:
"[full nuance block text]"

→ Would insert: directly after the paragraph that says "[relevant claim]"

[INSERT] | [SKIP]
```

4. If the user approves, add the block to the confirmed edits list with its insertion point.

**Placement:** The block goes directly after the paragraph that makes the relevant claim: not at the top as a disclaimer, not at the bottom as an afterthought.

---

## Step 8: Push approved edits to Wix blog

Follow **Phase 7** of the main SKILL.md to push all confirmed edits (inaccuracy corrections + any approved nuance block). Each inaccuracy edit is a targeted text replacement; the nuance block is an insertion.

After pushing: "✅ [N] product accuracy corrections published to [article title]." + if a nuance block was inserted: "1 nuance block added after [section name]."

---

## Tips

- Be conservative: only flag genuine inaccuracies, not stylistic differences between marketing copy and support docs.
- If the support docs don't clearly address a claim, don't flag it: only flag things where you have clear evidence of a discrepancy.
- Always quote the exact article text and the exact support doc language so the user can make an informed decision.
- No em-dashes in any replacement text or nuance block copy.
