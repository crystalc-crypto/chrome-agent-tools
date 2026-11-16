# Quality gates (run on every update)

Source: article-updater-2 and article-updater-2-session-rules (Sept to Nov 2026). Where those two differed, the session rules won and that version is what is written here.

These gates run on the **whole article** on every update, whatever update types were picked in Phase 5. Publishing is blocked until every gate passes. Gate 6 (formatting audit) lives in `formatting-audit.md`; post-publish assertions live in `post-publish-checks.md`.

| Gate | What it blocks | When |
|---|---|---|
| 0 | Blocks built from memory | Before building any recurring block |
| 1 | Unsourced numbers in intro / TL;DR | Before every publish |
| 1b | Claims that are only true at some providers; off-context Wix figures; promo competitor prices | Before any price, term or policy goes live |
| 1c | Wix mentions in non-branded intros | Every update |
| 1d | WHOIS privacy described as free / included | Every update, body AND schema |
| 2 | Sensational tone | Every update |
| 3 | A TL;DR that fails checks A to G | Every update |
| 4 | Lost body content | Every restructure |
| 5 / 5b | Updates with no substance; missing topic coverage | Every update |
| 6 | Formatting errors | Before every publish (see `formatting-audit.md`) |

---

## Gate 0: copy the convention, don't invent it

Before building any recurring block (TL;DR, CTA, FAQ, learn-more list, preview card, editor's note, quote attribution), GET a recently approved live article and copy its exact structure: heading text, casing, heading level, decorations and node order. Don't build it from memory of this skill. The live approved articles ARE the convention.

```js
var ref = await wix.request({ method:'GET', url:'/blog/v3/posts/slugs/how-to-start-a-babysitting-business?fieldsets=RICH_CONTENT', scope:'site' });
// inspect heading text, casing, heading level, decorations, node order, then match it
```

Observed: a FAQ `COLLAPSIBLE_LIST` cloned from a live article used `decorations: []` on the body TEXT and `initialExpandedItems:"FIRST"`, not the COLOR foreground once described. A live `LINK_PREVIEW` used `target:"TOP"`, not `SELF`. The live article won both times.

The same failure produces fabricated post IDs and unsourced statistics: filling a gap with something plausible instead of retrieving the real thing. When in doubt, read a reference post. It costs one call.

---

## Gate 1: the claim ledger (before every publish)

**No number may appear in an intro or TL;DR unless it is in the Claim Ledger with a source you retrieved in THIS session.**

### Step 1: extract mechanically, don't eyeball

```js
function extractClaims(topText) {
  var pats = [
    /\$[\d,]+(?:\.\d+)?/g, /\b\d+(?:\.\d+)?\s?%/g,
    /\b\d[\d,]*(?:\.\d+)?\s*(?:billion|million|trillion|bn|m)\b/gi,
    /\b\d+\s+to\s+\d+\b/g, /\b(?:hundreds|thousands|dozens)\s+of\b/gi,
    /\b(?:cheapest|most expensive|highest|lowest|fastest|largest|best|worst|only)\b/gi,
    /\b(?:one of the|among the)\b/gi,
    /\b(?:most|majority of|typically|usually|average|averaging)\b/gi
  ];
  var found = [];
  for (var i = 0; i < pats.length; i++) { var m = topText.match(pats[i]); if (m) found = found.concat(m); }
  return found;
}
```

### Step 2: build the ledger, one row per claim, no blanks

| Claim (verbatim) | Where | Source retrieved THIS session | Verdict |
|---|---|---|---|
| $200 formation fee | TL;DR | Alabama SoS fee schedule, searched today | KEEP |
| $72,675 startup cost | TL;DR | none, copied from article body | **CUT** |

A source is a URL or named authority you opened this session. NOT sources: the article's own body copy, another Wix article, your memory, a figure another AI gave you, or arithmetic on any of those. Baselines in `verified-facts.md` are NOT Gate 1 sources either; re-verify them.

### Step 3: apply the verdict

Real source: KEEP. No source: CUT. Don't hedge, soften or round.

When you cut a figure out of a sentence, re-read the sentence. Removing "usually in the five-to-ten-dollar range" once left a dangling "typically," in live copy. Cutting is a text edit, not a delete.

### Step 4: publish is BLOCKED until the ledger is clean

```js
if (extractClaims(introText + ' ' + tldrText).length > ledger.filter(r => r.verdict === 'KEEP').length)
  throw new Error('BLOCKED: unsourced claim in top-of-article.');
```

### Step 5: the ledger goes in the approval message and the report, every time

If there are no numbers, say so explicitly ("Claim ledger: 0 claims"). Silence is not a pass.

### Quotes and restored copy

- **Never edit a figure inside a direct quote.** Attributed quotes from named people are their words. Leave quoted figures alone and say so in the report.
- **Restoring vs asserting.** When restoring deleted or archived body copy verbatim, keep the original figures even if weakly sourced, and flag them. Never promote a restored body figure into a TL;DR or intro without running Gate 1 on it.
- Stats added by the Stats Updater or SERP Updater come from the Statistics Library with a linked source; they belong in body paragraphs, never the intro or TL;DR.

---

## Gate 1b: scope and breadth of factual claims

Two tests, both required before a price, term or policy goes live.

### Test 1: is it true everywhere, or only at one provider?

For registration periods, renewal rules, transfer behaviour, grace periods and platform policies, publish it only if it is true at every provider.

- **Registry / standards level:** true everywhere, safe to state flatly. The .ai two-year minimum is set by the registry. CA/Browser Forum certificate lifetimes bind every publicly trusted CA. DNS label limits are RFC-level.
- **Registrar level:** varies, do NOT state as a general fact. Whether an incoming .ai transfer adds two years differs by registrar.

If a check shows inconsistency across providers, drop the item and report that you dropped it and why.

### Test 2: does the surrounding copy call for a Wix figure or a general one?

Context decides.

- Copy **about Wix** (a "Why buy X with Wix" section, "Wix business email features and plans", the Wix entry in a listicle): use the verified Wix figure (Vizion or the Wix product page).
- **Generic** copy (a general "How much does a domain cost?" FAQ): keep it generic and state the structural truth, for example that renewal is commonly higher than the first-year rate and varies by extension and registrar.

When a section is ambiguous, ask rather than guess.

### Competitor pricing

Third-party prices are region-specific, promotion-specific and often rendered by JavaScript. Verified live: three of four checked competitor figures were wrong, all the same way: a promotional rate quoted as the standard rate.

- Verify each vendor on its own pricing page in a **rendered browser**. WebFetch returns `$0.00` and `undefined% off` on client-rendered pricing pages.
- Quote the standard rate and note the promotion separately, never the promo alone.
- If a price sits behind a login, **cut the figure**. Never sign in.
- Free-tier and structural facts (user caps, storage, custom-domain support) are stable and worth stating precisely.

---

## Gate 1c: branded vs non-branded

- Informational, non-branded articles never mention Wix in the intro. A gate link on a generic phrase is fine.
- Keep the TL;DR generic ("Website builders bundle…") in non-branded articles.
- Move Wix copy to the Wix section or the CTA; never delete it.
- **Interaction with the first-fold rule:** in a non-branded article, the first-fold Wix mention (for example a semantic triple) goes in the main CTA paragraph or the first body section after the TL;DR, never in the intro paragraphs.

---

## Gate 1d: WHOIS privacy wording

Applies to body, headings, lists, tables, FAQ, TL;DR, "You'll learn" lists, alt text, captions AND the post's SEO structured data (FAQ / HowTo JSON-LD in `seoData.tags`), which keeps its own stale copy of old text.

1. **Wix WHOIS privacy (domain privacy, private registration) is a paid option.** Say Wix **offers** it **as an option you can add**. Never say it is:
   - free, "for free", "at no extra cost", "at no additional cost", "for no extra fee", "no-cost", "without extra fees or add-ons", "free with Wix", or next to "no hidden fees";
   - included, includes, built in, bundled, comes with, standard inclusion, automatic, by default, part of the price;
   - listed under a lead-in like "the price includes all of this" or "Wix includes…".

   Approved patterns:
   - "Wix offers WHOIS privacy as an option you can add when you register your domain."
   - "You can add private registration to keep your contact details out of public records."
   - "privacy protection (offered by Wix as an option)"
   - "Optional domain privacy protection to hide personal info" (feature list)
   - Standard "Domain registration with Wix" sentence: "Beyond registration, Wix includes built-in tools for DNS management and domain security, along with a free SSL certificate to help protect your site and visitors. Wix also offers private registration to keep your contact details out of public records."
   - Voucher: "The voucher does not cover premium domains or WHOIS privacy, which you can add separately when you register your domain."
   - Comparison-table column is "WHOIS privacy", never "Free WHOIS privacy".
2. **Never advise readers to prefer a registrar whose WHOIS privacy is free or included.** Rewrite to a neutral check:
   - ✅ "Choose a registrar that offers WHOIS privacy protection." ❌ "Many registrars offer WHOIS privacy for free. Prioritize these providers."
   - ✅ "Privacy: Check what privacy protection options each registrar offers." ❌ "Some registrars charge extra for privacy protection, while others include it."
   - ✅ "…includes SSL, offers WHOIS privacy and integrates with your site" ❌ "…includes SSL and WHOIS privacy in the price"
   - Remove WHOIS privacy from lists of features "some registrars include for free". Cost breakdowns can list it as a cost item without "often free".
   - Factual competitor details (another registrar includes free WHOIS privacy) can stay. "Free WHOIS lookup" (the tool) is fine.
3. **Always write WHOIS in capitals** in text, headings, FAQ, anchors, alt text and schema. Never change URLs or hostnames (`/domains/whois`, `whois.icann.org`).
4. **Sweep body AND schema on every update.** Claims are often split across two sentences or across styled runs around a link:
   - Check each privacy sentence together with the sentence before it, and resolve pronouns ("it", "this", "all of this").
   - Regex: `/\bwhois\b/i` where the match is not "WHOIS"; and `(free|included|includes|built[- ]in|bundl|comes with|automatic|by default|no extra|no additional|no cost|without extra)` within the same or previous sentence as `(WHOIS privacy|domain privacy|privacy protection|private registration)`.
   - Use whitespace-tolerant regex (`\s+`); runs contain non-breaking spaces. When a phrase spans a link run, edit the neighbouring runs and keep the link.
   - Apply the same replacements to `seoData.tags[].children` and `props.content` and PATCH `seoData` together with `richContent`.

---

## Gate 2: tone (plain, never sensational)

Grep the whole article (top-of-article first) and rewrite every hit:

```
the real (expense|cost|problem)|what most people miss|here's the catch|the part that catches|drives everything|determines everything|the single (decision|thing)|falls apart|forget to budget|nobody tells you|the truth is
```

State the fact and stop. No implied insider knowledge about what readers overlook. Absolutes are overstatement. Unverified comparatives are Gate 1 claims.

---

## Gate 3: the TL;DR test (checks A to G, all must pass)

Nesia's standing instruction: *"write a tldr that covers everything that is in the article in short: paragraph that answers the intent straightforwardly + a short list titled something like 'you'll learn'. the paragraph should not repeat the list or the intro."*

**Write the answer first, then adjust wording to avoid the echo.** Fixing Check C alone produces a paragraph assembled from leftovers, which reliably breaks A, B, E and F.

- **Check A: sentence one answers the title's question.** Test: if you deleted the article, would this paragraph tell someone what to do?
- **Check B: it covers the full H2 arc.** Map the H2s and touch the whole arc, compressed. A passing Check C is not a pass on Check B. Check B is always a human read.
- **Check C: no echo.** Fewer than 5 shared content words with the intro, and fewer than 5 with the joined bullets.

  ```js
  var STOP = {the:1,and:1,that:1,with:1,your:1,you:1,for:1,are:1,from:1,this:1,than:1,which:1,
    their:1,have:1,has:1,but:1,not:1,all:1,its:1,it:1,a:1,an:1,of:1,in:1,to:1,on:1,or:1,is:1,
    as:1,at:1,be:1,by:1,most:1,more:1,also:1,then:1,each:1,into:1,before:1,after:1,
    business:1,businesses:1,start:1,starting:1,rather:1,while:1,they:1,what:1,when:1,where:1};
  function contentWords(s){var o={},m=s.toLowerCase().match(/[a-z$0-9]{4,}/g)||[];for(var i=0;i<m.length;i++)if(!STOP[m[i]])o[m[i]]=1;return o;}
  function echoScore(a,b){var x=contentWords(a),y=contentWords(b),n=0;for(var k in x)if(y[k])n++;return n;}
  // >= 5 shared content words against the intro or the joined bullets = rewrite.
  ```

  Measure it correctly: the intro window ends at `Math.min(buttonIndex, tldrIndex)` (some articles put the TL;DR before the CTA button, which otherwise compares the paragraph to itself). Join nested child nodes (`COLLAPSIBLE_LIST`, `LIST_ITEM`) with a space so block boundaries don't merge tokens.
- **Check D: heading format and casing.** `TL;DR: how to <topic>` (for example `TL;DR: how to start a babysitting business`; match the wording of the Gate 0 reference post for question-style titles), HEADING level 2, no decorations. The word after the colon is lowercase; only genuine proper nouns keep capitals (`Wix`, `SSL`, `Google`, a leading TLD dot like `.ai vs .com`). A lowercased proper noun is also wrong.

  ```js
  /^TL;DR:\s+([a-z.]|Wix|SSL|DNS|Google)/.test(headingText) && headingNode.headingData.level === 2
  ```
- **Check E: the first sentence names its subject.** The paragraph is read standalone in search results and AI Overviews. Openers that failed live: "The suffix carries no industry signal…", "It is an ICANN-approved extension…", "Anyone can buy one…". Never let the non-repetition constraint choose the subject. If naming the subject pushes echo to 5, cut genuine restatement, not the subject.
- **Check F: neutral commercial tone.** Open with what it is and who it suits, no downside in sentence one. State trade-offs factually in the middle. Pair a downside with the constructive response where one honestly exists. Close neutrally. Never overcorrect into promotion (Gate 2 still binds).

  ```js
  var NEG=/spam|suspicion|caution|drawback|risk|beware|problem|worse|bad|penal/i;
  if (NEG.test(firstSentence(tldr))) throw new Error('negative framing in first sentence');
  ```
- **Check G: shape.** ONE paragraph, exactly 2 sentences, 35 to 50 words. Sentence 1 answers; sentence 2 gives the biggest driver or shortcut. Then bold "You'll learn:", a short list (one row per bullet) and the CTA image. Never split the TL;DR paragraph. No blog links. "Be specific" never means "invent a number".

Bullets are labels, the paragraph is the answer. The paragraph must not restate the list.

---

## Gate 4: never delete body content

A restructure pass once deleted 7 real paragraphs from each of two live articles by treating "everything between the hero image and the CTA button" as the intro. The CTA button often sits below the opening sections.

### Correct intro detection

```js
var introEnd = ctaPara;
if (firstHeadingAfterHero > -1 && firstHeadingAfterHero < introEnd) introEnd = firstHeadingAfterHero;
var introIdx = [];
for (var v = hero + 1; v < introEnd; v++)
  if (c[v].type === 'PARAGRAPH' && txt(c[v]).trim().length > 40) introIdx.push(v);
if (introIdx.length > 4) throw new Error('ABORT: intro window too wide, check CTA position');
```

Exclude the CTA paragraph (and any secondary CTA) before counting. Never report a defect you haven't confirmed on the node tree.

### Mandatory word-count guard on every restructure

```js
var expected = wordsBefore - removedWords + addedWords;
if (wordsAfter < expected - 20) throw new Error('ABORT: unexpected content loss');
```

Compute `expected` from what you actually changed. Known false positives: replacing a spaced em-dash with a colon removes a token; nesting Q&A inside a collapsible list merges tokens. Baseline the guard against the same transformation rather than loosening it.

### Insertion anchors must be non-empty nodes

Inserting "after the last node before the next H2" silently does nothing when that node is an empty spacer. Build the content-only array first, find the last **non-empty** node of the section, then splice. A silent no-op shows in the word delta (expected +114, landed +54). Always assert the new text is present in the re-GET.

### Structural check after a restructure

No HEADING immediately followed by another HEADING where the original had prose between them (an `H2 FAQ` followed by an `H3 question` is fine).

### If content is lost anyway

The Blog API has no revision endpoint. Recover in this order:
1. **web.archive.org**: restore verbatim and rebuild internal links (strip the `/web/<timestamp>/` prefix).
2. Wix dashboard version history, if available.
3. Rewrite as a last resort, clearly flagged as new copy.

Own it immediately and stop.

---

## Gate 5 / 5b: full topic coverage check (every update) and no update without substance

Run this before proposing changes on every update, and present the result as suggestions with exact placement and draft copy. Wait for approval before publishing new sections. If the SERP Updater was also picked, use this result as its starting point (see `update-serp.md`) rather than running the SERP pull twice.

1. **Main keyword:** from the cluster item's KW column (`long_text`) on 🌌 EN Blogs Clusters (`5557032877`). If empty, ask the user.
2. **Top 3 organic results:** Ahrefs `serp-overview` (country `us`, `select: position,url,title,type`). Fetch the top 3 organic pages (ignore ads and the AIO block) and list their H2/H3 arc.
3. **Forums:** Reddit, Quora and relevant forums (NamePros, Stack Exchange, vendor community threads). Reddit is often blocked to the fetcher; use thread titles and People Also Ask from the SERP data and snippets, and say what couldn't be read.
4. **AI answers:** the AI Overview block in the SERP data (which sources it cites) and synthesized answers as a proxy. Google's AIO and AI Mode panels can't be observed directly; say so.
5. **Gap list:** for each subtopic covered elsewhere but not in the article, confirm it is really absent (regex presence check on the live text; read the match, since loose regexes hit your own new copy). Filter to search intent; drop trivia and minority edge cases. Apply Gate 1 / 1b to any figures.
6. **Suggested sections and subsections:** heading level, exact placement (after which H2/H3), add vs edit, and draft copy.
7. **Section order:** definitions first, then comparison, then use cases / pros and cons, then how to choose or how to do it, then the Wix section, then FAQ. Suggest moves where the order breaks this.
8. **Readability for a non-professional reader:** every technical term explained in plain words on first use (jargon table in `article-structure.md`); where a name comes from when readers ask; table labels understandable without prior knowledge; a simple example or analogy where the concept is abstract. List each unclear passage with a plain rewrite.
9. **Report** in a short block: top 3 URLs, forum/AIO themes, gaps found, order issues, readability fixes, and what was dropped and why.

**No update ships without substance.** If a pass rewrites or adds nothing significant (only mechanical fixes), don't log it as done. Mechanical fixes alone reset the publish date without improving the content. Present the Gate 5b suggestions and ask the user how to proceed.

Gap checks have found: a live anchor "What is DNS?" pointing at an AI logo generators post; a "Types of SSL certificates" section omitting DV/OV/EV; a USPTO fee structure abolished 18 months earlier; an article asserting per-user email storage when the platform pools it.
