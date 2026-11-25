---
name: "wix-studio-seo-hub-article-updater"
description: "Identifies Wix Studio SEO Hub articles (www.wix.com/seo/learn/resource/* and www.wix.com/studio/blog/*) that need updating, diagnoses why, suggests targeted changes, runs a whole-article quality audit (claims, TL;DR, links, formatting, CTAs, images) and pushes approved edits to the Wix Studio SEO Hub blog with Monday logging (SEO Hub board). Use whenever the user wants to find stale Studio hub or Studio blog articles, refresh agency/freelancer/SEO content on the Studio blog, push content changes to the Studio SEO Hub, fix product inaccuracies about Wix Studio, or run any content refresh workflow for the Wix Studio SEO Hub. Also use it to apply approved rows from a Google Sheet of proposed changes. Trigger on phrases like \"update the Studio SEO hub\", \"apply the approved rows\", \"studio blog refresh\", \"which studio articles are stale\", \"push updates to the SEO hub\"."
---

# Wix Studio SEO Hub Article Updater

An end-to-end workflow for identifying, diagnosing, editing and publishing updates to Wix Studio SEO Hub articles (`www.wix.com/seo/learn/resource/*` and `www.wix.com/studio/blog/*`). The skill guides the user through selecting a content bucket, choosing articles based on staleness or performance criteria, picking update types, running the whole-article quality audit, approving changes and pushing them live to the Wix blog.

**Every update audits and fixes the whole article**, not only the content this skill adds. The quality gates (Gates 0 to 6) run on every article, whatever update types were picked, and publishing is blocked until they pass.

**State file:** progress is saved to `~/outputs/.studio-hub-article-updater-state.json` so the user can process one URL per session and return to the remaining list later.

---

## Reference files

Read the relevant reference file before each step. Don't work from memory of these files.

| File | When to read |
|------|-------------|
| `references/sheet-mode.md` | When the user gives a Google Sheet of proposed changes or says "apply approved rows": follow it instead of Phases 1 to 6. |
| `references/studio-overrides.md` | **Read FIRST, every run.** Studio hub differences (site, URLs, audience, bucket, branded rule, open items). Where it conflicts with any other file, it wins. |
| `references/quality-gates.md` | **Every update.** Gates 0 to 5b: copy the convention, claim ledger, claim scope, branded vs non-branded, WHOIS wording, tone, TL;DR test, never delete content, topic coverage |
| `references/formatting-audit.md` | **Every update.** Gate 6 formatting audit, re-spacing routine, lists, headings, images and preview cards, off-topic asides, writing style |
| `references/link-rules.md` | **Every update.** Same tab / new tab, link colour, anchor vs target, encyclopedia mappings and "leave alone" list, TLD pages, anchor rules |
| `references/article-structure.md` | **Every update.** Canonical top-of-article order, intro and TL;DR rules, CTA conventions, product-mention rules, jargon table, block templates (FAQ, table, preview card, learn-more, editor's note) |
| `references/image-rules.md` | **Every update.** Bucket media folders, featured image, main and extra CTA images, infographics, alt text, image plan |
| `references/cta-blocks.md` | CTA copy, buttons and gate images per cluster. Read before inserting, replacing or auditing CTAs |
| `references/verified-facts.md` | Any article with prices, fees, plans or Headless claims (Vizion, USPTO, CA/B Forum, Google, state costs) |
| `references/post-publish-checks.md` | After every publish: assertions and final report format |
| `references/monday-logging.md` | After every publish: Monday item, cluster date, connect_boards |
| `references/ecommerce-spelling.md` | Spelling rule for all copy, and the leftover scan |
| `references/products.md` | Cluster to product to triples board mapping |
| `references/update-new-product.md` | New Product Update (Semantic Triples) workflow |
| `references/update-accurate-product.md` | Accurate Product Update workflow |
| `references/update-serp.md` | SERP Updater workflow |
| `references/update-entity.md` | Missing Entity Updater workflow |
| `references/update-eeat.md` | EEAT Updater workflow (expert quotes) |
| `references/update-stats.md` | Stats Updater workflow (Statistics Library) |
| `references/nuance-blocks.md` | Pre-approved nuance block library |

---

## Mode check (before Phase 1)

If the user supplies a Google Sheet link or asks to apply approved rows, read `references/sheet-mode.md` and follow it in place of Phases 1 to 6, then continue at Phase 7. Otherwise run the phases below.

## Phase 1: Scope the SEO Hub queue

The queue is the Monday board **Content Pipeline – SEO Hub** (`2709452345`), not the EN Blogs Clusters board.

Use `AskUserQuestion` (single select) to choose which groups to pull from:
1. Published, 2026 (`group_mm09krvw`)
2. Published, OLD (`new_group3683`)
3. Refresh (`new_group65130`)
4. All of the above

Never queue items from Ideas, Brief, In progress, Next up or Backlog: they are not live. Skip items already in the **Agentic updates** group (`group_mm9c1yka`) as "already logged", but list them so the user can re-select one.

---

## Phase 2: Choose article criteria

Use `AskUserQuestion` with `multiSelect: true` to ask which types of articles to surface. Present all options: the user may pick any combination:

1. **Not updated in 3 months**: articles whose **Publish date** (`date5`) on the Monday board is more than 90 days ago (this board has no "Last updated" column; if an Agentic updates log item exists for the article, use its date instead) *(data source: Monday.com)*
2. **Not updated in 6 months**: articles whose **Publish date** (`date5`) is more than 180 days ago (same rule) *(data source: Monday.com)*
3. **Lost AIO citations (10+)**: articles that lost more than 10 AI Overview citations *(data source: Ahrefs)*
4. **Lost keyword rankings**: articles that dropped position for their highest-volume organic keyword *(data source: Ahrefs)*
5. **Declining GSC clicks**: articles that lost organic clicks over the past 3 months *(data source: Ahrefs/GSC, project_id: 3213842; verify the project covers `/studio/blog/` pages, else report that GSC criteria are unavailable)*
6. **GSC position drop**: articles whose average position dropped (higher number) over the past 3 months *(data source: Ahrefs/GSC, project_id: 3213842; verify the project covers `/studio/blog/` pages, else report that GSC criteria are unavailable)*

**Important:** Criteria 1 and 2 come from Monday data already fetched in Step 3a. Criteria 3 and 4 require per-URL Ahrefs calls run in Step 3c. Criteria 5 and 6 require GSC data via Ahrefs (project_id `3213842`): run in Step 3c only if selected.

Record which criteria were selected. Multiple criteria are allowed; each matching article will be tagged with all criteria it qualifies for.

---

## Phase 3: Fetch articles from the Monday board

### Step 3a: Fetch the board schema and items from Monday.com

```
get_board_info    → boardId: 2709452345   (columns only)
get_board_items_page → boardId: 2709452345, includeColumns: true,
  columnIds: ["text","date5","status","multiple_person_mm3jf7j3"], limit 100,
  filters: group any_of [<groups chosen in Phase 1>]
```
Key columns: `text` = URL, `date5` = Publish date, `status` = Article status, `multiple_person_mm3jf7j3` = People. Paginate with the cursor until `has_more` is false. Items with an empty URL are skipped and listed. If Monday returns an authentication error, ask the user to reconnect it in Settings > Connectors.

### Step 3b: Filter

Keep only items whose URL is on `www.wix.com/seo/learn/resource/` or `www.wix.com/studio/blog/`. The slug is the last path segment.

### Step 3c: Apply criteria filters

**Criteria 1 & 2 (Monday.com: date-based):**
Evaluated from data already fetched in Step 3a. Compare the `date5` Publish date to today's date:
- Tag the article with `[3mo]` if >90 days old
- Tag the article with `[6mo]` if >180 days old
No additional tool calls needed for these.

**Criteria 3 & 4 & 5 & 6 (Ahrefs / GSC: performance-based):**
Only run if the user selected the relevant criteria. Run all article checks in parallel.

**Criteria 3 (AIO citation loss: Ahrefs):**
- Call `mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__site-explorer-metrics` for the article URL
- Check if the site has lost AI Overview impressions/citations compared to the previous period
- Tag with `[aio-loss]` if >10 citations lost

**Criteria 4 (keyword ranking drop: Ahrefs):**
- Call `mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__site-explorer-organic-keywords` with:
  - `target`: the article URL
  - `mode`: `exact`
  - `select`: `keyword,volume,best_position,best_position_prev,best_position_diff`
  - `order_by`: `volume:desc`
  - `limit`: 1
  - `date`: today
  - `date_compared`: 3 months ago
  - `country`: `US`
- Tag with `[rank-drop]` if `best_position_diff > 0` (higher number = ranking dropped)

**Criteria 5 (declining GSC clicks):**
- Call `mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__gsc-page-history` with:
  - `project_id`: 3213842
  - `pages`: [article URL]
  - `date_from`: 3 months ago
  - `date_to`: today
  - `history_grouping`: "monthly"
- Compare first month vs. last month clicks. Tag with `[gsc-click-drop]` if clicks declined.

**Criteria 6 (GSC position drop):**
- Use the same `gsc-page-history` call as above (run in parallel with criteria 5)
- Compare average position across the period. Tag with `[gsc-pos-drop]` if average position number increased (ranking declined).

---

## Phase 4: Present the article list and let the user choose one URL

Show the filtered list as a table in the conversation:

```
| # | Article | URL | Publish date | Criteria |
|---|---------|-----|--------------|----------|
| 1 | How to Make a Website | wix.com/studio/blog/... | Jan 12, 2025 | [6mo] [rank-drop] |
| 2 | Website Builder Guide | wix.com/studio/blog/... | Feb 28, 2025 | [3mo] |
...
```

Then ask the user to type the number of the article they want to work on. They may only choose **one URL per session**.

**State file:** After the user selects a URL, save the full article list (including remaining unselected articles) and the selected URL to the state file so they can return later:

```json
{
  "content_bucket": "SEO Hub (2709452345)",
  "last_run": "2026-05-04",
  "selected_url": "https://www.wix.com/studio/blog/...",
  "remaining_articles": [
    {"title": "...", "url": "...", "criteria": ["6mo", "rank-drop"]},
    ...
  ]
}
```

Save state to: `~/outputs/.studio-hub-article-updater-state.json`

**Returning users:** At the start of the skill, check if this state file already exists. If it does, ask the user: "You have a saved list from [last_run date] in the **[content_bucket]** bucket with [N] articles remaining. Do you want to continue from where you left off, or start a fresh search?"

---

## Phase 5: Choose update types

Use `AskUserQuestion` with `multiSelect: true` to ask which update types to apply to the selected URL:

1. **Semantic Triples Updater:** insert semantic triples about a new Wix product into the article
2. **Accurate Product Update:** cross-check product claims against Wix support docs and fix inaccuracies
3. **SERP Updater:** identify content sections missing vs. top-ranking competitor articles (automatically enriches new sections with stats from the Statistics Library)
4. **EEAT Updater:** add expert quotes to strengthen Experience, Expertise, Authority and Trust signals
5. **Stats Updater:** enrich existing paragraphs with pre-approved statistics from the Wix Blog Statistics Library (board 18413546794)

Tell the user in one line that the **whole-article audit and the Gate 5b topic coverage check always run** on top of whatever they pick. The user may pick any combination of update types, or none (audit only). Execute them in sequence (1 > 2 > 3 > 4 > 5), reading the relevant reference file before each one.

---

## Phase 6: Diagnose, then propose every change in one approval package

### Step 6a: Set up the article

1. **Confirm today's date** with `date -u` before stamping anything. Session metadata has disagreed with the actual date by a day.
2. **Resolve the post ID** by slug (Step 7a). Never type a post ID from memory.
3. **Get the node tree:** draft with `?fieldsets=RICH_CONTENT` (and `SEO` when checking schema text). See Step 7b.
4. If the draft has `hasUnpublishedChanges: true`, someone else may be editing it: stop and ask before continuing.
5. **Read the live article** with `mcp__Claude_in_Chrome__navigate` + `mcp__Claude_in_Chrome__get_page_text`. Note headings, section structure and the first fold (intro and content before the first major H2).
6. **Gate 0:** GET a recent approved Studio hub article in the same cluster and note its conventions for TL;DR, CTA, FAQ, cards and quote attribution (`quality-gates.md`).
7. **Find the main keyword.** The SEO Hub board has no KW column: look the URL up on the EN Blogs Clusters board `5557032877` (read only, `url` column, KW in `long_text`); if absent, ask the user or take the top organic keyword from Ahrefs `site-explorer-organic-keywords` for the URL. Never write to `5557032877` (needed for Gate 5b, the SERP Updater and alt text).

### Step 6a-2: Read the user's source URLs (when given)

If the user supplies source URLs, read each one **in full** before drafting. Try in order: `WebFetch`, then `mcp__Claude_in_Chrome__navigate` + `get_page_text`. If a host fails to resolve (`ENOTFOUND`, blocked domain), say which host failed. `WebSearch` summaries are secondary: use them only to point at what to look for, never as a read of the page, and label any claim that rests on them `[verify]`. Never draft claims from a source you could not read. Ask the user to paste the text instead.

Every new fact in the draft must carry its source URL in the approval package (Phase 6d). Keep the original author's voice: sample the existing copy (person, asides, punctuation habits, sentence length) before writing, and match it.

### Step 6b: Run the standard whole-article audit (always)

Run every check on the **whole node tree**, not only the parts you will touch. Read each reference file first.

| # | Check | Reference |
|---|---|---|
| 1 | Canonical top-of-article order (gate line, hero, 2-paragraph intro, CTA + button, TL;DR, CTA image, body); CTA sitting after the TL;DR; video in the intro | `article-structure.md` |
| 2 | Intro: 2 paragraphs, 60 to 90 words, no blog links, no generic openers, no Wix in non-branded intros (Gate 1c) | `article-structure.md`, `quality-gates.md` |
| 3 | TL;DR: Gate 3 checks A to G | `quality-gates.md` |
| 4 | Claim ledger on intro + TL;DR (Gate 1) and claim scope (Gate 1b) | `quality-gates.md` |
| 5 | Tone sweep (Gate 2) | `quality-gates.md` |
| 6 | WHOIS wording and casing, body AND schema (Gate 1d) | `quality-gates.md` |
| 7 | CTA block matches the current copy in `cta-blocks.md` (top line, paragraph, button text, URL, pill style, bold, colour, TLD override) | `cta-blocks.md` |
| 8 | Links: same tab for Wix, new tab + noreferrer for external, colour, anchor vs target, buttons have links, no links in tables | `link-rules.md` |
| 9 | Encyclopedia links: verified mappings, "leave alone" list, resolve the rest | `link-rules.md` |
| 10 | Prices and facts: Vizion for Wix domain prices, primary sources for the rest, editor's note | `verified-facts.md` |
| 11 | Formatting audit (Gate 6): spacing, headings, lists, long paragraphs, em-dashes, `\n`, double spaces | `formatting-audit.md` |
| 12 | Images and preview cards: not under headings, 3+ paragraphs apart, learn-more lines to cards | `formatting-audit.md` |
| 12b | **Image rules:** look up the bucket media folder; featured image, `-main` CTA image after the TL;DR, extra CTA images, infographics, alt text on every image (fallback to the cluster images in `cta-blocks.md` if the folder is missing) | `image-rules.md` |
| 13 | Ecommerce spelling leftovers: visible copy now, hidden fields (alt text, SEO title, meta description, excerpt, schema) after Step 7b | `ecommerce-spelling.md` |
| 14 | Off-topic asides and duplicate expert quotes | `formatting-audit.md`, `article-structure.md` |
| 15 | **Gate 5b topic coverage check** (top 3 SERP, forums, AIO, gap list, section order, readability) | `quality-gates.md` |

### Step 6c: Execute each selected update type

Follow each update type's reference file to identify its changes. Where a reference file says to push its changes ("Follow Phase 7"), collect its approved changes instead: everything is pushed once, in Phase 7, after the pre-publish gate run. All copy written by any update type follows these rules:

- No em-dashes anywhere, including quote attribution lines. US spelling. "ecommerce" per `ecommerce-spelling.md`. WHOIS in capitals and Gate 1d wording.
- In general sections, explain the concept first in plain words and bring Wix in last as an example (`article-structure.md`).
- **First fold:** content naming Wix products or carrying semantic triples appears no lower than the end of the first fold. In non-branded articles it goes in the main CTA paragraph or the first body section after the TL;DR, never in the intro paragraphs (Gate 1c).
- New figures in the intro or TL;DR must pass Gate 1. Stats from the Statistics Library go in body paragraphs only.
- Anchor rules in `link-rules.md`; never add an awkward sentence just to place a link.

**Contributor articles:** if the article is by an external contributor, keep the byline and add an update note directly under it: "Originally written by <author>. Updated by <updater> on <Month D, YYYY>." Ask the user whether to keep the original `firstPublishedDate` (default for contributor pieces) or republish with today's date; never change it silently.

### Step 6d: Present one approval package

Show everything before anything is pushed, in this order:

1. **Audit fixes, mechanical** (spacing, decorations, link targets and rel, link colour, encyclopedia URLs, em-dashes, spelling, WHOIS casing, pill buttons): grouped counts plus a short list. One approval covers the group.
2. **Audit fixes that change copy** (intro, TL;DR, CTA copy, WHOIS wording, tone, long-paragraph splits, bullets to subsections, cut claims, image moves): before / after for each.
3. **Claim ledger** (always, even if empty: "Claim ledger: 0 claims").
4. **Gate 5b coverage summary and suggested sections** with placement and draft copy.
5. **Image plan** table and flags from `image-rules.md` (Step 6), including any new infographic attached for approval.
6. **Update-type changes** (triples, product fixes, SERP sections, quotes, stats): before / after per change.
7. **Decisions needed:** off-topic asides, duplicate quotes, removals, iframe removals, ambiguous Wix-vs-generic figures, source conflicts.

The user can approve, edit or skip each item. **Never push without explicit approval.** If the approved set has nothing substantive (mechanical fixes only), say so and ask whether to proceed (Gate 5).

---

## Phase 7: Push changes to the Wix blog

**Target site ID (hardcoded):** `1bd95b49-a53d-4ff9-917d-cdcc422f879e` ("Wix Studio SEO Hub"), serving `www.wix.com/seo/learn/resource/<slug>` (confirmed Nov 2026; the post API returns `url.base` + `url.path`) and possibly `www.wix.com/studio/blog/*`. Always use this ID. Never use the main blog site (`1faf9cf8-5bbb-49dd-99ff-3a182f82629d`), the legacy "Wix Blog" site, or "Wix Studio Academy" (`27c78b34-3286-45fc-931d-cd9025c7c891`). If a slug is not found, say so, never fall through to another site.

Use `ExecuteWixAPI` (writes need `hasMutations:true`). If you're unsure of a request or response shape, check it with `ReadFullDocsMethodSchema` rather than guessing.

### Step 7a: Find the blog post ID

```
mcp__3da1c945-aec7-4495-8843-de00acdd6a8c__ExecuteWixAPI
  → siteId: "1faf9cf8-5bbb-49dd-99ff-3a182f82629d"
  → GET https://www.wixapis.com/blog/v3/posts/slugs/<slug>?fieldsets=URL
```

Extract `post.id` (draft id == published id). Resolve it in the same run every time.

**Slug resolution (Studio):** the Monday URL is `https://www.wix.com/seo/learn/resource/<slug>` or `.../studio/blog/<slug>`. Use `<slug>` only. If `posts/slugs/<slug>` returns 404, do NOT guess: query the site's posts (`POST /blog/v3/posts/query`, paginate, match on `post.url` or `slug`) and confirm the match with the user before continuing. If this site does not use Blog v3 or the slug cannot be matched, stop and report.

### Step 7b: Retrieve the full draft post

```
mcp__3da1c945-aec7-4495-8843-de00acdd6a8c__ExecuteWixAPI
  → siteId: "1faf9cf8-5bbb-49dd-99ff-3a182f82629d"
  → GET https://www.wixapis.com/blog/v3/draft-posts/{postId}?fieldsets=RICH_CONTENT
```

`richContent` is NOT returned by default; always pass `fieldsets=RICH_CONTENT` (add `SEO` to read `seoData` for the schema sweeps). The nodes array is `draftPost.richContent.nodes`. If a response doesn't have the shape your code expects (keys from an unrelated operation have been returned twice), don't trust it: say it mismatched and re-run.

**Common node types:**
- `PARAGRAPH`: body text; `TEXT` children; `paragraphData`
- `HEADING`: `headingData.level` = 2/3/4; `TEXT` children
- `TEXT`: leaf; `textData.text`; `textData.decorations` (BOLD, ITALIC, LINK, COLOR, FONT_SIZE)
- `BLOCKQUOTE`: contains a `PARAGRAPH`
- `BUTTON`: `buttonData.text`, `buttonData.link`, `buttonData.styles`
- `LINK_PREVIEW`: `linkPreviewData.link`, `.title`, `.description`, `.thumbnailUrl`
- `IMAGE`: `imageData.image.src`, `imageData.altText`, `imageData.link`
- `BULLETED_LIST` / `ORDERED_LIST` > `LIST_ITEM` > `PARAGRAPH`
- `COLLAPSIBLE_LIST` (FAQ), `TABLE`, `DIVIDER`

**Finding text:** text is always inside `TEXT` children. Concatenate a block's TEXT children and match on a distinctive substring with whitespace- and apostrophe-tolerant regex (live copy has curly apostrophes and non-breaking spaces; text is often split across styled runs). Find sections by true `HEADING` nodes only.

### Step 7c: Apply the approved changes

**Insertions:** find the last **non-empty** node of the target section (never an empty spacer) and splice after it. Generate a unique 8-character alphanumeric `id` for every new node, never reusing an existing ID.

**Replacements:** update `textData.text` of the matched TEXT node(s) and keep existing decorations unless the change is to a decoration (link target, foreground colour, heading decorations).

**Whole-article fixes:** apply the approved audit fixes from Step 6b across the whole tree, including link targets and rel, link colour, encyclopedia URLs, button styles, em-dashes and spelling. Anchor text is never changed except for approved spelling fixes. Body content is never removed without approval.

**Link decoration templates:**

```json
// Wix link (same tab)
{ "type": "LINK", "linkData": { "link": { "url": "https://www.wix.com/...", "target": "SELF", "rel": { "noreferrer": false } } } }
// External link (new tab)
{ "type": "LINK", "linkData": { "link": { "url": "https://example.com/...", "target": "BLANK", "rel": { "noreferrer": true } } } }
```

An anchor run carries only `LINK` (plus BOLD / FONT_SIZE when the style calls for it), never a foreground `COLOR`.

**Images:** insert the approved images from the image plan (`image-rules.md` Step 7): existing Media Manager files by media ID with real width/height, alt text set, CTA images linked to the cluster CTA URL (SELF). Set the cover (`media.wixMedia.image`) only if a new featured image was approved. Upload an approved new infographic to the bucket's infographics folder before inserting it.

**Re-spacing:** after all edits, run the junk-node sweep and the deterministic re-spacing routine in `formatting-audit.md`.

**Schema:** if Gate 1d, ecommerce or other text fixes touched copy that also lives in `seoData.tags` (FAQ / HowTo JSON-LD), apply the same replacements there.

### Step 7d: Pre-publish gate run (blocking)

Run in code on the final node tree, and repeat until clean:

1. **Gate 4 word-count guard:** `wordsAfter >= expected - 20`, where `expected = wordsBefore - removedWords + addedWords`. Abort on failure.
2. **Gate 1 ledger check** on the new intro + TL;DR.
3. **Gate 2** regex, **Gate 3** checks, **Gate 1d** regex (body and schema).
4. **Gate 6** formatting audit and the link checks in `link-rules.md`.
5. Every approved insertion is present; every blog link moved out of the intro/TL;DR appears exactly once.

### Step 7e: Confirm the publish date

Ask the user to approve the publish date (plain-text question, not `AskUserQuestion`):

```
The article will be republished with today's date: **[YYYY-MM-DD]**.
Approve this date, or enter a different one (format: YYYY-MM-DD)?
```

Default to today's date from `date -u`. Record as `publishDate`.

### Step 7f: Publish

```
mcp__3da1c945-aec7-4495-8843-de00acdd6a8c__ExecuteWixAPI
  → siteId: "1faf9cf8-5bbb-49dd-99ff-3a182f82629d"
  → PATCH https://www.wixapis.com/blog/v3/draft-posts/{postId}
  → body: {
      "draftPost": {
        "id": "<postId>",
        "richContent": { "nodes": [ ... full updated nodes array ... ] },
        "firstPublishedDate": "<publishDate>T00:00:00.000Z"
        // add "seoData": {...} only when schema text changed
      },
      "action": "UPDATE_PUBLISH"
    }
```

`UPDATE_PUBLISH` updates and publishes in one call. If the endpoint needs a field mask, include `richContent`, `firstPublishedDate` (and `seoData` when sent). Alternative path: PATCH the draft, then `POST /blog/v3/draft-posts/{postId}/publish`.

**Operations rules:**
- **Timeouts and 503s may still have applied.** Large PATCHes often time out at 180s. Always re-GET and check before retrying. After a cut-off batch, check `hasUnpublishedChanges` and publish any patched draft that didn't go live.
- **Rate limits are aggressive.** Batches of about 8 light reads or 8 heading-only writes are usually safe; full restructures 2 to 3 at a time. On `Rate limit exceeded` back off (`sleep 170`) and probe with one small request before resuming.
- The live page may be cached: re-GET the draft, not the live page, before re-applying a change.
- **If a write is refused by a permission check, stop,** explain, and wait for explicit approval.

### Step 7g: Verify

Run every assertion in `references/post-publish-checks.md` on the re-fetched draft and live post. Don't report success on the strength of the PATCH response.

After a successful verify: "✅ Changes pushed to [article title] (published: [publishDate]). [Article URL]"

### Step 7h: Log to Monday

Follow `references/monday-logging.md`: one log item per article per day on board `2709452345`, in the **Agentic updates** group (`group_mm9c1yka`). Never delete or move the article's original item.

### Error handling

- **403 error:** the Wix connector may need reconnecting: ask the user to check Settings > Connectors > Wix.
- **Node not found for insertion:** dump the TEXT nodes of the nearest HEADING section and match by a distinctive substring; never guess.
- **Content lost:** follow the Gate 4 recovery path (web.archive.org first) and stop.

---

## Phase 8: Update state, report and offer the next article

1. Give the short final report from `post-publish-checks.md`: what was updated, claim ledger, final image list and open image flags, unsolved or dropped items, and the link to the post.
2. Remove the processed URL from `remaining_articles` in the state file.
3. Tell the user: "✅ Done with this article. You have **[N] articles remaining** in the [content bucket] queue. Come back any time to pick up the next one."
4. If `remaining_articles` is now empty, congratulate them and clear the state file.

---

## Sitewide sweeps (wording or casing fixes across many posts)

Only when the user asks for one:
- Can run as **silent fixes** only with approval: republish without changing `firstPublishedDate` and skip Monday items. Ask first.
- Skip posts whose draft has `hasUnpublishedChanges: true` and report them.
- Run batches of about 15 to 30 posts. When the list comes from a text match, re-query each batch, since fixed posts drop out of the match.
- Include `seoData` in the PATCH when schema text changed.

---

## General tips

**wix.com is blocked by WebFetch.** Use `mcp__Claude_in_Chrome__navigate` + `mcp__Claude_in_Chrome__get_page_text` for live Wix pages and for resolving encyclopedia redirects. Use a rendered browser for competitor pricing pages too.

**Retrieve, don't invent.** Post IDs, anchors, block conventions, prices and encyclopedia destinations are always looked up in the current session. When something can't be retrieved, ask.

**One URL per session.** The user processes one article at a time; the saved state list means they never lose track of what's left.

**Show before you push.** Never push changes without explicit approval. Always show before / after clearly.

**If a gate breach ships,** own it, fix it, and sweep every article touched in the run for the same class of error (`post-publish-checks.md`).

**Same section flagged twice:** list every requirement from the original instruction and check them all at once.
