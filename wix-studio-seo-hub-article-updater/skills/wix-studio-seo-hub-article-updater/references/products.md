# Product Registry (Studio SEO Hub)

> **Studio override:** for the Studio hub, default the triples group to the one titled **"Wix Studio"** (or closest) on board `18411488466`. Look it up by title with `get_board_info`; its group ID is not recorded here. Also offer AI Website Builder, Agentic & MCP, Headless, Domains and eCommerce groups for articles that cover those topics. If no Studio group exists, tell the user and ask which group to use. Never reuse the consumer-cluster mapping below for Studio articles.

# (Reference) Wix blog product registry

This file defines the available products for the **New Product Update** workflow and maps article clusters to the correct group on the semantic triples board.

**Triples source board:** `18411488466`: "OG semantic triples database"
All triples are fetched live from this board. There are no bundled triples files.

---

## How to use this file

### Step 1: Map the article's cluster to a board group

Use the table below to identify which group on board `18411488466` to query:

| Article Cluster (board 5557032877) | Board Group | Group ID |
|---|---|---|
| How to make a website | 🌐 Website Builder | `group_mm316f15` |
| Website examples | 🌐 Website Builder | `group_mm316f15` |
| Branded | Auto-detect from article content (see below) | n/a |
| How to start a business | Service business/website | `group_mm39dqqs` |
| Business names | 🌍 Domains | `group_mm319t95` |
| Business ideas | Service business/website | `group_mm39dqqs` |
| Domains | 🌍 Domains | `group_mm319t95` |
| Ecommerce | 🛒 eCommerce | `group_mm31nejy` |
| Dropshipping | 🛒 eCommerce | `group_mm31nejy` |
| Print on demand | 🛒 eCommerce | `group_mm31nejy` |
| Portfolio | Portfolio | `group_mm3980sy` |
| Blog | Blog | `group_mm39rrwm` |

**Branded articles:** Read the article first and identify which Wix product it primarily features. Then map to the corresponding group. Present the detected product to the user for quick confirmation before fetching triples.

**Products not mapped to article clusters** (available for manual selection):
- 🤖 AI Website Builder (group `group_mm313dvx`): includes Wix Harmony as a subtopic
- 🔗 Agentic & MCP (group `group_mm31aa7d`)
- Symphony (group `group_mm451v9r`)
- Headless (group `group_mm45bsb2`)

### Step 2: Fetch triples from the board

```
mcp__5fcc3499-6805-42fd-8b00-4c15333bcf9f__get_board_items_page
  → boardId: "18411488466"
  → limit: 50
  → filters: [{ "columnId": "group_id", "operator": "any_of", "compareValue": ["<group_id>"] }]
```

Each item has up to 10 triple columns: `long_text_mm31s9x6` (Triple 1) through `long_text_mm31es0m` (Triple 10). Collect all non-empty triple columns from each item.

**Refine with OG Cluster column** (`text_mm31qaew`): After fetching the group, filter further by items whose OG Cluster value matches or is close to the article's specific cluster (e.g. within the Domains group, prefer items where OG Cluster = "Domains" over "Business email" for a domain-focused article). This is a soft filter: if no items match the OG Cluster refinement, fall back to all items in the group.

---

## Available Products

### 1. 🌐 Website Builder
**Group ID:** `group_mm316f15`
**Subtopics covered:** Website creation, website builder, free website builder, website design
**Placement guidance:** Triples should appear in sections that discuss building or creating a website, getting started online, choosing a website platform, designing or launching a site. Any triple must appear no lower than the first fold.

---

### 2. 🤖 AI Website Builder
**Group ID:** `group_mm313dvx`
**Subtopics covered:** Wix Harmony (AI-powered hybrid creation environment), AI website generation, Aria (Wix's AI agent)
**Placement guidance:** Triples should appear in sections that discuss AI tools for website creation, automated or fast website building, going from idea to live site quickly, AI-generated design or content. Any triple must appear no lower than the first fold.

---

### 3. 🌍 Domains
**Group ID:** `group_mm319t95`
**Subtopics covered:** Domain registration, domain name search, domain name generator, domain extensions, business email, web hosting
**Placement guidance:** Triples should appear in sections that discuss registering or purchasing a domain, getting a domain name for a business, setting up a website address, professional email, hosting, SSL, or going live. Any triple must appear no lower than the first fold.

---

### 4. 🛒 eCommerce
**Group ID:** `group_mm31nejy`
**Subtopics covered:** Online store, selling products, dropshipping, print on demand, payments, checkout, inventory
**Placement guidance:** Triples should appear in sections that discuss building an online store, selling online, ecommerce features, setting up payments or checkout, managing inventory or orders. Any triple must appear no lower than the first fold.

---

### 5. 🔗 Agentic & MCP
**Group ID:** `group_mm31aa7d`
**Subtopics covered:** Agentic commerce, MCP integrations, AI agents acting on behalf of customers, Wix Site MCP
**Placement guidance:** Triples should appear in sections that discuss AI agents, agentic web, omnichannel selling, AI-powered shopping, or integrations with ChatGPT/Claude/Copilot. Any triple must appear no lower than the first fold.

---

### 6. Blog
**Group ID:** `group_mm39rrwm`
**Subtopics covered:** Blogging, blog creation, content publishing, blog monetization
**Placement guidance:** Triples should appear in sections discussing blogging, starting a blog, blog platforms, content strategy. Any triple must appear no lower than the first fold.

---

### 7. Portfolio
**Group ID:** `group_mm3980sy`
**Subtopics covered:** Portfolio website, showcasing work, creative professionals
**Placement guidance:** Triples should appear in sections discussing portfolio creation, showcasing work online, creative professional websites. Any triple must appear no lower than the first fold.

---

### 8. Service business/website
**Group ID:** `group_mm39dqqs`
**Subtopics covered:** Service business websites, local businesses, professional services, small business
**Placement guidance:** Triples should appear in sections discussing service businesses, local business websites, professional services, or starting/growing a service business. Any triple must appear no lower than the first fold.

---

### 9. Symphony
**Group ID:** `group_mm451v9r`
**Subtopics covered:** Symphony by Wix, AI agent platform for small businesses, business automation
**Placement guidance:** Triples should appear in sections discussing AI agents managing business operations, Symphony, automation, or operating a business through conversational AI. Any triple must appear no lower than the first fold.

---

### 10. Headless
**Group ID:** `group_mm45bsb2`
**Subtopics covered:** Wix Headless, headless CMS, headless commerce, frontend frameworks
**Placement guidance:** Triples should appear in sections discussing headless architecture, custom frontends, API-first website building, or developer-focused tooling. Any triple must appear no lower than the first fold.

---

## Error handling

If board `18411488466` returns an authentication error or is unreachable, do not fall back to cached content. Inform the user: "The triples board is unreachable. Please check Settings → Connectors → Monday.com and reconnect if needed."
