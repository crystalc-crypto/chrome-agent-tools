# Monday logging (after every publish)

Log every published update on **Content Pipeline - SEO Hub** (`2709452345`, workspace "SEO Marketing") in the group **Agentic updates** (`group_mm9c1yka`). Never skip it. If a Monday call fails, report the error and finish the Wix work regardless; the article is already live. If Monday asks for more permissions, the user must reconnect the connector (Settings > Connectors).

The old Blog SEO & Content Squad board (`5546696573`) and the EN Blogs Clusters board (`5557032877`) belong to other blogs. Do not write to them.

## Step 1: one item per article per day

Search the Agentic updates group for an item whose URL column matches the article. If one exists, **update it** (append to the summary, never create a second item for the same article). If none exists, create it. Never delete Monday items; surface duplicates and let the user remove them. Never move or edit the article's original item in the Published or Refresh groups.

## Step 2: build the exact column values

Call `get_board_info` (columns only) first and resolve labels and IDs from it. Do not guess.

| Column | Value |
|---|---|
| item name | Article title |
| `text` (URL) | `https://www.wix.com/seo/learn/resource/<slug>` (or the `/studio/blog/` URL) |
| `status` (Article status) | `Published` after a successful publish; `To review` while a draft awaits approval |
| `multiple_person_mm3jf7j3` (People) | the user running the skill: `{"personsAndTeams":[{"id":<id>,"kind":"person"}]}` from `get_user_context`; ask if it fails |
| `date5` (Publish date) | only if the article was republished with a new `firstPublishedDate`; otherwise leave blank |

The board has no summary or update-type column. Put the summary in an **item update** (`create_update`): what changed, claim ledger, sources used, and anything dropped and why. Add the update-note line used on the article (e.g. "Originally written by X. Updated by Y on <date>.").

## Step 3: verify

Re-read the item and confirm the group, URL, status and the update text. Report the item link to the user.

## Open
- Confirm whether the original item should also change status after a refresh. Default: leave it alone.
