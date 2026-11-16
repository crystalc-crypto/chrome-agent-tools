# Update Type: Missing Entity Updater

Identifies Wix product entities and semantic triples that should be present in the article but aren't, based on the article's content bucket and topic. Also checks for AIO citation losses if that criterion was selected.

---

## AIO Check (for Criteria 3: run during Phase 3 of SKILL.md)

When checking whether an article lost AIO citations, use the following Ahrefs approach:

```
mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__brand-radar-impressions-overview
  → (check if Wix's AI Overview impressions dropped for this URL)
```

Or alternatively, use site explorer to look at search impressions:
```
mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__site-explorer-metrics
  → target: [article URL]
  → mode: "url"
```

Compare current AI Overview citation counts with the previous period. An article qualifies for `[aio-loss]` tagging if it lost more than 10 AI Overview citations compared to the prior period.

If the Ahrefs tools don't return AIO-specific data, fall back to: use `mcp__2d8298e5-0e48-4a84-b96f-1acaf19b65e1__gsc-keyword-history` with the article URL to see if AI Overview impression data is accessible via GSC integration.

---

## Entity Update Workflow

### Step 1: Establish the product entity set for this article

Based on the article's **content bucket** (from Phase 1 of SKILL.md), determine which Wix products are most relevant to check for:

| Content Bucket | Primary entities to check |
|----------------|--------------------------|
| How to make a website | Website builder, AI website builder, Wix Harmony |
| Website examples | Website builder, templates, Wix Harmony |
| Branded | Website builder, Wix brand, Wix Harmony |
| How to start a business | Website builder, Ecommerce, Blog, Domains |
| Business names | Domains, Website builder |
| Business ideas | Website builder, Ecommerce, Blog |
| Domains | Domains, Website builder |
| Ecommerce | Wix Ecommerce, Selling online, Website builder |
| Dropshipping | Wix Ecommerce, Selling online |
| Print on demand | Wix Ecommerce, Selling online |
| Portfolio | Portfolio, Website builder |
| Blog | Blog, Website builder |

For each primary entity, check whether the article currently contains:
1. A **semantic triple**: a sentence where Wix is the subject, the product is the object, and there is a benefit/capability stated (e.g., "Wix's website builder lets you create a professional site in minutes")
2. A **named entity mention**: the product name appears at least once in the article
3. An **anchor link**: the product name is hyperlinked to the correct Wix product page

---

### Step 2: Read the article

If you haven't already read the article in this session:
1. `mcp__Claude_in_Chrome__navigate` → target article URL
2. `mcp__Claude_in_Chrome__get_page_text` for text content
3. Also extract hyperlinks via `mcp__Claude_in_Chrome__javascript_tool`:

```javascript
Array.from(document.querySelectorAll('article a[href]'))
  .map(a => ({text: a.textContent.trim(), href: a.href}))
  .filter(l => l.text && l.href);
```

---

### Step 3: Audit entity coverage

For each entity from Step 1, check:

| Entity | Semantic triple? | Named mention? | Anchor link? |
|--------|-----------------|----------------|--------------|
| Website builder | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| AI website builder | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| Wix Harmony | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| ... | | | |

**Reference URLs for anchor links:**

| Product | Canonical URL |
|---------|--------------|
| Website builder | `https://www.wix.com/website/builder` |
| AI website builder | `https://www.wix.com/ai-website-builder` |
| Wix Harmony | `https://www.wix.com/harmony` |
| Wix Ecommerce | `https://www.wix.com/ecommerce/website` |
| Portfolio | `https://www.wix.com/website/portfolio-website` |
| Blog | `https://www.wix.com/blog-website` |
| Domains | `https://www.wix.com/domain/names` |
| Selling online | `https://www.wix.com/ecommerce/sell-online` |

---

### Step 4: Generate missing entity recommendations

For each gap found in Step 3, generate a specific, ready-to-insert recommendation:

**Missing semantic triple:**
Write a natural-sounding sentence in the form: "[Wix / Wix's] [product] [capability verb] [benefit]" that fits the article's topic and tone. The sentence should read like it belongs in the article: not like a marketing tagline dropped in from nowhere.

**Missing named mention:**
Identify the nearest paragraph that discusses the product's topic area and suggest how to mention it naturally.

**Missing anchor link:**
Identify where the product name appears in the article and suggest wrapping it with the correct anchor link.

---

### Step 5: Present recommendations

Display all recommendations in a clear before/after format:

```
---
🔍 MISSING ENTITY: [Product name]

Issue: No semantic triple found for [product]

**Recommended addition:**
"[Triple sentence]"
→ Insert after: [location in article]

[APPROVE] | [EDIT] | [SKIP]
```

For missing anchor links specifically:
```
🔗 MISSING LINK: [Product name]

**Current text:** "...uses a website builder to..."
**Recommended:** "...uses a [website builder](https://www.wix.com/website/builder) to..."
→ Location: [section name], paragraph starting with "..."

[APPROVE] | [SKIP]
```

Show all recommendations at once. Ask the user to approve, edit, or skip each one.

---

### Step 6: Push to Wix blog

Collect all approved changes (insertions and link additions). Follow **Phase 7** of the main SKILL.md to push them. All Wix links must use `target: "SELF"` and external links `target: "BLANK"` + noreferrer (see `link-rules.md`).

After pushing: "✅ Entity coverage updated for [article title]: [N] semantic triples added, [N] anchor links added."

---

## Tips

**Semantic triples must sound natural.** Don't insert robotic-sounding triples. Read the surrounding text and write something that flows. A bad triple that sounds forced is worse than no triple at all: flag it for the user to edit rather than inserting something stilted.

**First fold priority.** At least one semantic triple for the primary product should appear no lower than the end of the first fold. In non-branded articles it goes in the main CTA paragraph or the first body section after the TL;DR, never the intro paragraphs (Gate 1c).

**Don't over-link.** Add anchor links for the most important product mentions: typically one per product per article is sufficient. Don't link every single mention.

**New links only: anchor text enforcement.** Any new blog link must use an approved anchor from board `5557032877` (KW column). Any new transactional link must use board `5817666262`. Keep anchor text exact and reshape the surrounding sentence to fit.
