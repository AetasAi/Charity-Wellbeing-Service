# Charity Wellbeing Service

A static website for the Charity Wellbeing Service — a joint proposition between **Adena Street** and **Aetas in the Workplace**, built specifically for charities and not-for-profit organisations.

**Live site:** https://charitywellbeing.aetaspartners.com

---

## What the site covers

The Charity Wellbeing Service brings together three areas of structured support:

1. **Governance** — offered by Adena Street. Independent governance support for trustees and boards, including Investment Policy Statements, trustee training, and Charity Commission compliance.
2. **Financial Guidance** — offered by Adena Street. Independent review of investment performance, fee transparency, cash management, and investment manager search.
3. **Financial Wellbeing** — powered by Aetas in the Workplace. Consultancy-led financial wellbeing for charity staff, covering benefits consultancy, resilience workshops, one-to-one guidance, and wellbeing initiatives.

---

## Site structure

All pages are static HTML files deployed via GitHub Pages.

| File | Description |
|------|-------------|
| `index.html` | Homepage — overview of the full service |
| `governance.html` | Governance service detail page |
| `financial-guidance.html` | Financial Guidance service detail page |
| `financial-wellbeing.html` | Financial Wellbeing service detail page |
| `insights.html` | Insights and articles |
| `faqs.html` | Frequently asked questions |
| `diagnostic.html` | 12-question self-assessment diagnostic tool |
| `book-a-meeting.html` | Discovery conversation booking page |
| `CNAME` | Custom domain configuration (`charitywellbeing.aetaspartners.com`) |
| `manifest.webmanifest` | PWA manifest |
| `robots.txt` | Search engine crawl instructions |
| `schema.json` | Structured data for search engines |
| `llms.txt` / `llms-full.txt` | AI crawler guidance |

---

## Design and technology

- Pure static HTML, CSS, and vanilla JavaScript — no build tools or frameworks
- Custom design system using CSS variables (`--forest`, `--gold`, `--cream`, etc.)
- Typography: Cormorant Garamond (headings) and Jost (body), loaded via Google Fonts
- Fully responsive; mobile nav collapses at 960px
- Deployed automatically via GitHub Pages on every push to `main`

---

## Updating the site

**To edit a page:** open the relevant `.html` file in this repository, make your changes, and commit directly to `main`. GitHub Pages will redeploy automatically within about a minute.

**To add a new page:** create a new `.html` file, copy the nav and footer from an existing page, and update the `class="active"` attribute on the relevant nav link.

**Nav consistency:** every page uses the same nav block. If nav links need to change, update all `.html` files. The nav brand links to `index.html` (relative) and all nav links are relative paths within the site.

---

## Partnership

| Partner | Role | Contact |
|---------|------|---------|
| **Adena Street** | Governance and Financial Guidance | adenastreet.co.uk |
| **Aetas in the Workplace** | Staff Financial Wellbeing | aetas-partners.com |

Financial wellbeing education and consultancy services do not constitute regulated financial advice. Where regulated advice is required, this is provided by Aetas Wealth, a trading style of Insight Financial Associates Limited, authorised and regulated by the FCA (registration 458421).

---

## Contact

Matthew Steiner — matthew.steiner@aetas-partners.com · 020 3633 0579
