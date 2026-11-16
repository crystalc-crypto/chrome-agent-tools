# CTA block definitions

Source: "Blog CTA blocks - for updater skill" (https://docs.google.com/document/d/1JU0Qy3_BzqQ8wv946eOicmCO-1fc7CjsfW8M3PTXu5s), November 2026. Match the article's cluster to the block below. Before inserting, copy the node structure from a live approved article in the same cluster (Gate 0 in `quality-gates.md`); the copy and URLs come from this file.

## Rules for every block

- **Placement:** top gate line above the hero image; main CTA paragraph + button right after the 2-paragraph intro, before the TL;DR; CTA image directly after the TL;DR list (see `article-structure.md`).
- **Bold:** only the first sentence of the main CTA paragraph.
- **Colour:** main CTA text runs use COLOR foreground `rgb(0,0,0)`, never on a link run (Headless is the exception: no foreground colour).
- **Spacing:** 1 empty paragraph before the CTA paragraph, 2 after the button.
- **Links:** every link opens in the same tab (`target:"SELF"`), dofollow.
- **Button:** pill style (template at the bottom). Trim whitespace in button text and URL; no leading spaces.
- **TLD articles override:** in an article about a single extension, the main CTA button and the CTA image link to `https://www.wix.com/domains/tld-list/tlds/<tld>-domain` (ccTLD overview: `https://www.wix.com/domains/tld-list/cctld`). Verify the page exists first.
- **Copy edits:** "grow without limits" becomes "grow" wherever it appears in a CTA.
- **Existing CTA blocks:** if the article already has a main CTA for this cluster, replace its copy, button text and URL with the current block below (with approval) rather than adding a second one. If it has none, insert the block.
- **CTA images follow `image-rules.md`.** Where the bucket media folder exists (Domains and Headless as of Nov 2026), the `-main` image in `[bucket] - CTAs` is the CTA image after the TL;DR and extra CTA images come from the same folder. The gate images and in-text banners listed per cluster below are the **fallback** when the folder is missing; if none is listed, copy the CTA image from a sibling article in the same cluster (Gate 0) and flag it if none exists. Either way the CTA image links to the cluster's button URL (TLD override applies), same tab.

---

## Cluster mapping

| Cluster / topic | Use this block |
|---|---|
| How to make a website | Website Builder |
| Website examples | None |
| AI Website Builder / Harmony | AI Website Builder |
| Domains | Domains |
| Email | Email |
| Ecommerce (Monday label "🛒 eCommerce") | Ecommerce |
| Dropshipping | Dropshipping |
| Print on demand | Print on Demand |
| Headless | Headless |
| Symphony | Symphony |
| Branded | Auto-detect from the article: identify the primary product and use its block |
| How to start a business, Business names, Business ideas, Portfolio, Blog | None (skip for now) |

---

## 1. Website Builder

**Top CTA (above hero image):** "Turn your ideas into a website → | Claim your domain →"
- "Turn your ideas into a website" → `https://www.wix.com/website-builder`
- "Claim your domain" → `https://www.wix.com/domains`

**Main CTA paragraph:** "**Choose a website builder that's flexible, powerful and easy to use.** Wix is trusted by millions of people to create beautiful websites for their businesses, projects and ideas. Try it for yourself and see what you can build."

**Button:** "Build your website" → `https://users.wix.com/signin/signup/password`

---

## 2. AI Website Builder

**Top CTA (above hero image):** "Turn your ideas into a live website in minutes with Wix's AI Website Builder →"
- "AI Website Builder" → `https://www.wix.com/ai-website-builder`

**Main CTA paragraph:** "**With Wix's AI website builder, you can generate a complete website with an AI agent, design direction and professional copy, then customize every detail to make it your own.** Go from idea to a polished, business-ready website in minutes."

**Button:** "Launch your AI website" → `https://www.wix.com/ai-website-builder`

**Fallback gate image (CTA image after TL;DR):** alt "AI website builder", link `https://www.wix.com/ai-website-builder`

**Fallback in-text banner 1:** alt "create a site with AI website builder", link `https://www.wix.com/ai-website-builder`. Place 2 sections after the gate image.

**Fallback in-text banner 2 (one of):**
- Option A: alt "domain name search", link `https://www.wix.com/domains/domain-name-search`
- Option B: alt "register a domain name", link `https://www.wix.com/domains`

Place 2 sections after in-text banner 1. Banners follow the image spacing rules in `formatting-audit.md` (never under a heading, 3+ paragraphs from other media).

---

## 3. Ecommerce

**Top CTA (above hero image):** "Get the perfect domain for your ecommerce store: find your domain →"
- "find your domain" → `https://www.wix.com/domains/domain-name-search`

**Main CTA paragraph:** "**Ready to start selling online?** Build a custom online store with Wix and get the tools to sell, manage and grow your business from one dashboard. Customize every detail, reach customers across channels and market your brand with built-in SEO and marketing tools."

**Button:** "Create your ecommerce site" OR "Create your online store" (choose based on the article topic) → `https://www.wix.com/ecommerce/online-store`

**Fallback gate image:** alt "create an online store", link `https://www.wix.com/ecommerce/online-store`

---

## 4. Dropshipping

**Top CTA (above hero image):** "Get the perfect domain for your dropshipping store: find your domain →"
- "find your domain" → `https://www.wix.com/domains/domain-name-search`

**Main CTA paragraph:** "**Build and grow your dropshipping business with Wix.** Find in-demand products, add them to your store and sell without managing stock. The built-in Modalyst integration helps you find suppliers and automate orders."

**Button:** "Start dropshipping" → `https://www.wix.com/ai-create-store`

**Fallback gate image:** alt "start dropshipping store", link `https://www.wix.com/ai-create-store`

---

## 5. Print on Demand

**Top CTA (above hero image):** "Get the perfect domain for your POD store: find your domain →"
- "find your domain" → `https://www.wix.com/domains/domain-name-search`

**Main CTA paragraph:** "**Start a print-on-demand business without inventory or shipping.** Choose products, add your designs and launch a fully customizable Wix store with built-in Printful integration. Manage orders and marketing from one dashboard."

**Button:** "Start a print-on-demand store" → `https://www.wix.com/merch-maker`

**Fallback gate image:** alt "create a print-on-demand store", link `https://www.wix.com/merch-maker`

---

## 6. Domains

**Top CTA (above hero image):** "The perfect domain is just a click away: find your domain →"
- "find your domain" → `https://www.wix.com/domains/domain-name-search` (single link; the old second arrow link to `/domains/?utm_campaign=toplink-domainshomepage` is dropped)

**Main CTA paragraph:** "**Secure your perfect domain in just a few clicks with Wix.** Get everything you need in one place: business email, reliable hosting, SSL protection and full privacy. With 24/7 support and no hidden fees, getting your site live is simple and worry-free."

**Button:** "Find and register your domain" → `https://www.wix.com/domains/domain-name-search`

Gate 1d note: this block is approved CTA copy. Don't add "WHOIS privacy" or "included" wording next to "no hidden fees" in surrounding copy.

---

## 7. Email

**Top CTA (above hero image):** "**Get your professional business email address →**" (whole line bold)
- "business email" → `https://www.wix.com/domains/business-email`

**Main CTA paragraph:** "**Get your business email up and running fast.** Wix provides built-in security, plenty of storage and real-time tools to help you stay on top of your work. Everything's backed by 24/7 support so you can focus on growing your business."

**Button:** "Get a business email" → `https://www.wix.com/domains/business-email`

---

## 8. Headless

Copy the structure from the live post `https://www.wix.com/blog/headless-cms-pricing` (Gate 0). This block overrides the generic colour rule: no `rgb(0,0,0)` foreground on Headless CTA runs.

**Top CTA (above hero image):** "Make any AI project business-ready in one prompt. Try Wix Headless →" (bold; link on the second run)
- "Try Wix Headless" → `https://www.wix.com/headless?utm_source=blog&utm_medium=blog`

**Main CTA paragraph:** bold first sentence "**Go from code to live site with Wix Headless.**", then " ", then the link run "Upload or drag in" → `https://www.wix.com/headless/drop?utm_source=blog&utm_medium=blog` (SELF), then " your HTML, CSS and JavaScript files to get your site live with a shareable URL. Wix handles the hosting and infrastructure, and you can add ecommerce, bookings, CMS, payments and more with a single prompt."

**Button:** "Try Wix Headless" → `https://www.wix.com/headless?utm_source=blog&utm_medium=blog`, `styles:{borderWidth:4,borderRadius:30,buttonSize:"LARGE"}`, target SELF.

**CTA image after the TL;DR list:** the `-main` image in `Headless bucket > headless - CTAs` (see `image-rules.md`), linked to `https://www.wix.com/headless` (SELF), alt text 2 to 5 words built around the keyword. Fallback if that folder can't be found: src id `df59d5_a34372e4b8f5410ebb1445c89e35328c~mv2.jpg`, 924x485.

---

## 9. Symphony

**Top CTA (above hero image):** "Running your business solo? Meet Symphony by Wix, your team of AI agents → Try for free"
- "Try for free" → `https://symphony.wix.com/`

**Main CTA paragraph:** "**Let AI agents take work off your plate.** Symphony by Wix learns how your business works and helps you find new clients, manage operations and handle daily tasks. Focus on growing your business while Symphony helps keep things running."

**Button:** "Try Symphony for free" → `https://symphony.wix.com/`

---

## Button node (Ricos format)

```json
{
  "type": "BUTTON",
  "id": "<rid>",
  "nodes": [],
  "buttonData": {
    "containerData": { "width": { "size": "ORIGINAL" }, "alignment": "CENTER", "spoiler": {}, "height": {}, "textWrap": true },
    "type": "LINK",
    "styles": { "borderWidth": 4, "borderRadius": 30, "buttonSize": "LARGE" },
    "text": "[Button text]",
    "link": { "url": "[Button URL]", "target": "SELF", "rel": { "noreferrer": false } }
  }
}
```

`styles:{}` renders flat and is wrong. A live button with `target:"TOP"` is also same tab and can stay.

## General rules

- Never place a blog link (`wix.com/blog/...` or `wix.com/studio/blog/...`) in the intro or TL;DR.
- Never turn a gate / transactional / CTA link into a LINK_PREVIEW card; these stay as inline links or buttons.
- No competing CTAs beside the main CTA.
- If the cluster has no defined CTA block, skip CTA insertion and continue with the other update types.
