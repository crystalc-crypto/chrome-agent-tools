# Monday logging (after every publish)

Log every published update on **📝 Content schedule | Blog SEO & Content Squad** (`5546696573`) and update the article's cluster item on **🌌 EN Blogs Clusters** (`5557032877`). Never skip it. If a Monday call fails, report the error and finish the Wix work regardless; the article is already live.

If Monday returns "connector requires additional permissions", the user needs to reconnect the connector (Settings > Connectors). Report it.

---

## Step 1: one item per article per day

Before creating anything, look for an existing item for this article created or updated today (match on the article title and the connected cluster item). If one exists, **update it** (re-type it if the scope grew, append to `text3`). Never create a second item for the same article on the same day. A second same-day pass once produced four duplicates that had to be consolidated by hand.

**Never delete Monday items.** Surface duplicates and let the user remove them. Before anyone deletes a duplicate cluster item, check which content items link to each copy, ask which to keep and move the links over first.

## Step 2: find the group

`get_board_info` on `5546696573`. Use the current month's updates group, named **"Q3/Q4 Updates <Month> <Year>"** (for example "Q3/Q4 Updates November 2026"). Match case-insensitively on the month and year. If there's no group for the current month, ask the user which group to use rather than defaulting.

## Step 3: owner

The owner is the **user running the skill**: `get_user_context` gives their Monday user ID. If that fails, ask the user (fallback Rebecca Tomasis `25036305` only if they confirm).

## Step 4: update type (status_1)

Definitions (Nesia, Oct 2026):

| Update | Label |
|---|---|
| Semantic Triples Updater ran (new product triples inserted) | **Product update** (index `108`) |
| Mostly intro, CTA and/or TL;DR, plus link, spacing, image, card and other mechanical fixes | **light Update** (index `2`) |
| Link plus mechanical fixes only | **light Update** (index `2`) |
| New or substantially rewritten body sections, accuracy fixes in the body, added quotes or stats | **mid Update** (index `9`) |
| Price correction plus restructure plus new sections | **heavy Update** (resolve the index by label name from `get_board_info`) |

If several apply, use the highest: Product update > heavy > mid > light. When in doubt, resolve labels by name from `get_board_info` rather than trusting an index.

## Step 5: build the exact column values, then create or update

Find the cluster item first: `items_page_by_column_values(board_id: 5557032877, columns: [{column_id: "url", column_values: ["<article url>"]}])` (variable type `[String]!`).

| Column | Value |
|---|---|
| item name | Article title |
| `status_1` | Update type from Step 4 |
| `people` | `{"personsAndTeams":[{"id":<owner id>,"kind":"person"}]}` |
| `dropdown_mkwzfbhw` | Content bucket (use the board's own label text, for example "🛒 eCommerce"; Monday labels keep their spelling) |
| `status2` | `{"label":"Live"}` |
| `text7` | Reason for the update (the Phase 2 criteria tags, for example "6mo, rank-drop", plus the user's reason if given) |
| `checkbox_3` | `{"checked":"true"}` only if an FAQ was added |
| `text3` | Short, specific summary: what is live now, plus what was dropped and why. Mention the whole-article audit passes (links, encyclopedia, formatting) |
| `connect_boards` | `{"item_ids":[<cluster item id>]}` |

**Never send placeholder values.** Build the exact final string for every column before the mutation. When updating an existing item, read `text3` first so it can be restored.

## Step 6: set the dates

Set today's date on BOTH the post (`firstPublishedDate`, done in Phase 7) and the cluster item's `date` column on `5557032877`. The content schedule's Publish column mirrors the cluster item's `date`. Skip this only for an approved silent fix (see SKILL.md, sitewide sweeps).

## Step 7: verify

Re-read the item. `text` and `value` both return null for board-relation columns, which looks like a missing connection. Query the fragment instead, or you'll "fix" something that was never broken:

```graphql
column_values(ids:["connect_boards"]){ ... on BoardRelationValue { linked_item_ids linked_items { id name } } }
```

## After every later round

Update Monday after EVERY round of changes on the same article: `text3` = what is live now plus what was dropped. Same-scope follow-ups append a note to the existing item's `text3` rather than creating a new item. Re-type the item when the scope grows. At the end of the session, re-read all items and cluster dates touched.
