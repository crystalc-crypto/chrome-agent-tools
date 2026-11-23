# Wix Studio SEO Hub overrides (read first)

This skill was adapted from the main Wix blog updater. Wherever another reference file conflicts with this one, **this file wins**.

## Confirmed facts (looked up Nov 2026)

| Item | Value |
|---|---|
| Wix site | "Wix Studio SEO Hub", `1bd95b49-a53d-4ff9-917d-cdcc422f879e` |
| Not this site | main blog `1faf9cf8-5bbb-49dd-99ff-3a182f82629d`, Wix Studio Academy `27c78b34-3286-45fc-931d-cd9025c7c891` |
| Live URL pattern | `https://www.wix.com/seo/learn/resource/<slug>` (SEO Learn Hub, confirmed via API on this site); Monday also holds `https://www.wix.com/studio/blog/<slug>` items |
| Article source and logging | Monday board **Content Pipeline - SEO Hub** `2709452345`; queue groups Published 2026 `group_mm09krvw`, Published OLD `new_group3683`, Refresh `new_group65130`; update log group **Agentic updates** `group_mm9c1yka` |
| Columns | URL `text`, Publish date `date5`, Article status `status`, People `multiple_person_mm3jf7j3` (no "Last updated" or priority column) |
| EEAT quotes | board `18411479018`, group `group_mm3gfj48` "Wix Studio" (see `update-eeat.md`) |
| Not used | `5557032877` EN Blogs Clusters and `5546696573` Blog SEO & Content Squad (other blogs); `4146974906` SEO Hub clusters (legacy) |

## Audience and tone (changes vs the main blog)

The Studio hub readers are agencies, freelancers, web designers and developers, not first-time site builders. Therefore:
- Do not apply beginner jargon-glossing rules from `article-structure.md` to terms such as breakpoint, CMS collection, Velo, responsive layout.
- Nuance blocks in `nuance-blocks.md` under "Wix Studio" are the relevant ones; consumer-site blocks (Wix Editor, free plans, domains for beginners) usually do not apply.
- Studio articles are **branded by nature**: Gate 1c ("no Wix in non-branded intros") applies only when the Monday column `color_mm8rkf6z` says "Non branded". Default to branded when unset, and confirm with the user.

## Must be resolved before the first push (open items)

These could not be retrieved while adapting. Ask the user, or look them up, and then fill in this table; do not invent them.

1. **CTA blocks:** `cta-blocks.md` holds consumer-cluster CTAs (Website Builder, Domains, ...). Studio needs its own block (copy, button text, destination, gate image). Until supplied, **do not insert or replace CTAs**; copy the CTA node from a live approved Studio hub article (Gate 0) and report the CTA audit as "no spec".
2. **Image folders:** no Studio folder is recorded in `image-rules.md`. Look up the Media Manager on the hub site at run time; if absent, skip the featured/CTA/infographic rules and flag.
3. **Monday logging:** resolved: logs to `2709452345`, group Agentic updates. Still open: whether the original item should change status after a refresh.
4. **Triples group:** see `products.md` override.
5. **Verified facts:** `verified-facts.md` is about domain and consumer pricing. For Studio plans/pricing/features use the Wix Studio help center and pricing page, rendered in a browser; add an editor's note per the usual convention.
6. **Slug resolution:** `GET /blog/v3/posts/slugs/<slug>?fieldsets=URL&fieldsets=RICH_CONTENT` works on this site for `/seo/learn/resource/<slug>` articles (verified on `microsoft-clarity-for-ux-and-conversions`). The `/studio/blog/` slug probed earlier 404d: unresolved.
7. **GSC project:** `3213842` was for the main blog; confirm it covers `/studio/blog/`.
8. **Encyclopedia and ecommerce-spelling files** are carried over from the consumer blog and should be reviewed for relevance.
9. **Ahrefs / Monday / Wix connector IDs** in tool names (`mcp__<uuid>__...`) are connector-specific; use whatever the current session exposes.
