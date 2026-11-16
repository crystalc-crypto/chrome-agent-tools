# Verified facts, prices and primary sources

Everything here is a **baseline, not a Gate 1 source.** Re-verify any figure you publish in the current session. Apply Gate 1b (scope and context) before deciding whether a passage needs a Wix figure at all.

When two sources disagree, don't pick one silently: report the conflict, say which you believe and why, and leave the copy alone until it is settled.

---

## Domain prices (mandatory when an article contains domain prices)

### Vizion is the source of truth for Wix domain prices

`https://bo.wix.com/_serverless/vizion-platform/#premium/domains/domain-pricing-comparison` (VPN, browser only)

Set **First non-NTT = true**, pick the TLD (auto-fills Offer Name, Spec, Dyn. Product, Bundle). Read the **Yearly** row: `0` = initial, `1` = renewal. USD unless asked otherwise.

Vizion initial prices are often far below the public marketing pages. Publish the Vizion figure. Don't "correct" upward, and don't mix sources in one table.

**Baseline (initial / renewal, USD), re-verify every session:** .xyz 0.98 / 23.82 · .co.uk 4.90 / 7.90 · .org 6.90 / 22.90 · .online 6.90 / 40.90 · .com 7.90 / 21.35 · .biz 7.90 / 35.90 · .info 7.90 / 39.90 · .top 8.90 / 12.90 · .net 11.90 / 22.90 · .blog 14.90 / 44.90 · .de 14.95 / no renewal data

### Driving the Vizion dashboard

- An Okta sign-in that times out is an **authentication** wall, not VPN. Ask the user to sign in; never enter credentials.
- It renders in an **iframe**: read via `document.querySelector('iframe').contentDocument`.
- Inputs are `input.ss-input`, ten per plan (Plan A 0 to 9, Plan B 10 to 19). Use Plan B for a second TLD instead of clearing Plan A.
- Comboboxes are React-controlled: native value setter + `input` event, then click the `.ss-item` with the full `pointerdown, mousedown, pointerup, mouseup, click` sequence. Set **First non-NTT** before the TLD.
- Use top-level `await` in the JS tool; an async IIFE returns an empty object.
- Verify the plan title matches the TLD before reading, since the previous table lingers.
- Some extensions have no renewal data (.de). State the gap; never infer.

### What to fix once verified

- Correct every figure in body, table, TL;DR and intro (usually 3 to 5 places). Re-derive any stated range.
- Renewals commonly run higher than the intro rate, so "renewals match first-year" is false, and so is a renewal range below the real renewal.
- Add or refresh the dated italic **editor's note** before the FAQ: *"Editor's note: prices are current as of <Month D, YYYY> and are subject to change at any time."*
- Never edit a price inside a direct quote (Gate 1).

---

## Non-domain figures: route to the primary source

Retrieve each in the current session.

- **USPTO trademark fees** (uspto.gov): TEAS Plus and TEAS Standard were **abolished 18 January 2025**, replaced by a single **base application fee of $350 per class**, plus surcharges of $100 per class (incomplete) and $200 per class (free-form text instead of the Trademark ID Manual).
- **TLS certificate lifetimes** (cabforum.org): Ballot SC-081v3 caps certificates at **200 days from 15 March 2026**, 100 days from 2027, 47 days from 2029.
- **Google Business Profile** (support.google.com): a new owner or manager waits **7 days** before taking primary ownership; on a request for access, the current owner has **3 days** to respond.
- **Wix business email plans** (wix.com/domains/business-email): Starter / Standard / Plus at $7 / $14 / $22 per user per month.
- **Google Workspace storage is POOLED, not per user.** Business Starter contributes 30GB per licence to an organization-wide total, Standard 2TB, Plus 5TB; one user can exceed what their own licence contributes unless an admin sets limits. Confirmed by support.google.com and support.wix.com. An article claiming isolated per-user allowances is wrong. The Wix business email marketing page has been seen showing 2TB on Starter (the Standard allowance on the wrong card): trust Google's spec and report the page error rather than editing the article.

## State business costs (verify per state, per entity type)

Search the current Secretary of State fee for each figure, and check the recurring cost as well as formation.

Baseline, verified August 2026 (formation / recurring, LLC unless noted):

| State | Formation and recurring |
|---|---|
| Alabama | $200 + mandatory $25 name reservation |
| Arizona | $50 + transaction privilege tax licence |
| California | $70 + $20 initial Statement of Information within 90 days + $800 minimum franchise tax in year one |
| Connecticut | $120, annual report $80 |
| Georgia | $110 flat since Sept 2025, $50 sales tax permit |
| Illinois | $150, no statewide general business licence |
| Indiana | $95 online / $100 mail, Business Entity Report $32 biennially |
| Maryland | $100 online / $170 mail, $300 annual report |
| Minnesota | $50, free renewal if on time |
| Missouri | about $50 online, no annual report |
| New York | $200 + newspaper publication for six consecutive weeks within 120 days + $50 Certificate of Publication |
| North Carolina | $125 + $200 annual report |
| Oregon | $100 + $100 annual report |
| Pennsylvania | $125, annual report replaces the decennial filing |
| South Carolina | $110, no annual report for a standard LLC |
| Virginia | $100 + $50 annual registration |
| Washington | $180 + $70 annual report, plus B&O tax |
| Wisconsin | $130 online / $170 paper, annual report $25 / $40 |

## Verified Wix Headless claims

- **/headless:** no developer pricing, no API fees, no enterprise tiers; free to connect; backend for CMS, ecommerce, bookings, events and payments; Wix-managed hosting with global CDN, SSL, auto-scaling and 99.99% uptime.
- **/headless/cms (Oct 2026):** free to connect, no time limit, no credit card; a paid plan is needed only for accepting live payments, connecting a custom domain and advanced analytics; Wix-managed or self-managed hosting; connect via a skill.md prompt in AI coding tools, or start from the Headless page into Lovable, Base44, Bolt.new. NOT verified: "no content cap" (cut it).
- **/headless/drop:** drag and drop HTML, CSS and JS (up to 20MB); live on a Wix URL in seconds; free managed hosting with SSL and a global CDN.
- **/headless/commerce:** not live as of 30 Sept 2026.
- Headless is **not** automatically faster than a traditional site. Never state "headless is faster" as fact.
