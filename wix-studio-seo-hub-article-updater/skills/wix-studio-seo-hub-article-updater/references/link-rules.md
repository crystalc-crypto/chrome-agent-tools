# Link rules (whole article, every update)

These checks run on **every link in the article**, not only links added this session. Fixes to link targets, rel, colour and encyclopedia URLs are mechanical and can be approved as one grouped line. Anchor text is never changed except for spelling fixes ("ecommerce", WHOIS casing).

---

## 1. Same tab for every Wix link

- Every link to `wix.com` or a Wix subdomain (`support.wix.com`, `symphony.wix.com`, `manage.wix.com`, `users.wix.com`, etc.) opens in the same tab: `target:"SELF"`. Inside a `LINK_PREVIEW`, `target:"TOP"` is the live convention and also counts as same tab.
- Check TEXT `LINK` decorations, `buttonData.link`, `linkPreviewData.link` and IMAGE links.
- After publishing, assert 0 `wix.com` links with `target:"BLANK"`.

## 2. External links open in a new tab with noreferrer

- Every non-Wix link: `target:"BLANK"` and `rel.noreferrer:true`. Keep any other `rel` keys that are already there.
- Assert on the live post after publishing.

## 3. Broken links (404s), when asked

When the user asks for a 404 check, test every external source and every internal link. Report what was checked; remove only links that actually fail (with approval).

## 4. Link target matches anchor

Enumerate every link (anchor text + URL) and read the list. Found live: "What is DNS?" pointing at `/blog/best-ai-logo-generators`, and ".net" pointing at the .online encyclopedia page. Fix mismatches to the correct target (approved anchor's post) with approval.

## 5. Link colour

- An anchor TEXT node carries ONLY `LINK` (plus BOLD / FONT_SIZE where the style calls for it). A `COLOR` with a **foreground** overrides link blue. Correct blue is `rgb(22, 106, 234)`.
- A `COLOR` decoration with only `background: "transparent"` is harmless and is the existing convention; remove only foreground colours.
- Never apply the body-text COLOR helper (for example the CTA `rgb(0,0,0)` foreground) to an anchor run.
- After any linking pass, assert no LINK node carries a foreground COLOR.

## 6. Buttons have a link

Every BUTTON has `buttonData.link.url`, trimmed.

## 7. Never link inside a TABLE

Check the ancestor chain before adding a link.

## 8. Encyclopedia links resolve to their 301 destination

Replace every `/encyclopedia/definition/<term>` link with the URL it 301-redirects to. **Check the verified lists below first.** For a term not on either list, resolve it: open the URL in the browser (`mcp__Claude_in_Chrome__navigate`, wix.com is blocked to WebFetch) and read the final URL or the `canonical`. If it can't be resolved, ask the user. Never guess.

### Verified redirects (term > destination)

| Encyclopedia term | Destination |
|---|---|
| https | /blog/what-is-https |
| web-address | /blog/what-is-a-web-address |
| domain-management | /blog/domain-name-management |
| domain-name-system-dns | /blog/what-is-the-domain-name-system-dns |
| website-traffic | /blog/what-is-website-traffic |
| web-privacy | /blog/what-is-web-privacy |
| content-management-system-cms | /blog/what-is-a-cms |
| domain-spoofing | /blog/what-is-domain-spoofing |
| cache | /blog/what-is-cache |
| secure-sockets-layer-ssl | /blog/how-to-get-an-ssl-certificate |
| content-delivery-network-cdn | /blog/what-is-a-content-delivery-network-cdn |
| lazy-loading | /blog/what-is-lazy-loading |
| ddos-distributed-denial-of-service | /blog/what-is-ddos |
| web-browser | /blog/what-is-a-web-browser |
| co-domain | /blog/what-is-co-domain |
| domain-privacy | /blog/what-is-domain-privacy-protection |
| domain-history | /blog/what-is-domain-history |
| parked-domain | /blog/parked-domain |
| uptime | /blog/what-is-uptime |
| web-server | /blog/what-is-a-web-server |
| hosted-services | /blog/what-are-hosted-services |
| ip-internet-protocol-address | /blog/what-is-an-ip-internet-protocol-address |
| domain-expiration | /blog/what-is-domain-expiration |
| website-backup | /blog/website-backup |
| parts-of-a-url | /blog/what-are-the-parts-of-a-url |
| managed-hosting | /blog/what-is-managed-hosting |
| web-content | /blog/what-is-web-content |
| tech-domain, info-domain, digital-domain (and other TLD terms) | /domains/tld-list/tlds/<tld>-domain |
| co-uk-domain | /domains/tld-list/tlds/co.uk-domain |
| phishing | replace with anchor "What is email security?" > /blog/what-is-email-security |

All destinations are on `https://www.wix.com`.

### Do NOT redirect (verified non-redirecting, leave alone)

trademark, copyright, parent-company, html-hypertext-markup-language, application-programming-software-api, javascript, virtual-private-network-vpn, sitemap, cloud-communications, software-as-a-service-saas, database, domain-authority, domain-lifecycle, scalability, computer-security, malware, ransomware, and the business-terms family: sole-proprietorship, limited-liability-company-llc, partnership, corporation, c-corporation, nonprofit-corporation, business-entity, business-operations, concept-statement, operating-expenses, net-profit, corporate-tax, expense-report, start-up-capital, unique-selling-proposition-usp, key-performance-indicator-kpi, franchising, bootstrapping, angel-investors, business-incubator, business-ethics, business-cycle, inventory, networking.

After the pass, report: encyclopedia links found, redirected, left alone (verified non-redirecting), and unresolved (should be 0).

## 9. TLD pages

- Slug pattern: `/domains/tld-list/tlds/{com,net,org,co,biz,xyz,online,blog,co-uk}-domain`. Confirm the page exists before linking.
- `.uk` has no page: unlink ".uk".
- Merge split ".co.uk" link runs into one link.

---

## Anchor rules for new or changed inline links

- **Blog links:** the anchor must be approved for the target on 🌌 EN Blogs Clusters (`5557032877`): `long_text` (KW) column or item name. Look up with `get_board_items_page`, `url contains_text <slug>`; batch several filters with `filtersOperator: "or"`.
- **Gate links:** anchor from the Cheat Sheet (`5817666262`). Most are SUBITEMS on board `5818081875`: read `text` / `text7` / `text72` / `long_text`, matched on `text23` (URL), with `includeSubItems:true`.
- Keep anchor text exact and reshape the surrounding sentence to fit, never the other way around.
- Never invent anchors or use vague ones ("here", "click here").
- These rules govern inline text links only. A `LINK_PREVIEW` card has no anchor text; anchor approval never blocks a preview card.
- Gate links (wix.com product pages) are allowed in the intro. Blog links are not allowed in the intro or TL;DR.
- Each article links to a given target exactly once. Check whether a link already exists before adding it.

## Anti-stuffing

- Never add content or an awkward sentence just to place a link; drop the link instead.
- At most one link per bullet, and only a minority of bullets linked.
- Strip links from illustrative example URLs (for example "yourbusiness.com").

## Link tables (when the user supplies a list of links to add)

Confirm scope and alternative rows first; keep paragraphs coherent; verify product claims; only add a link where a section genuinely fits. A link pass is also a full update pass (all gates apply).
