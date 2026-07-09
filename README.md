# Aetas Impact

A static website for **Aetas Impact** — the purpose-led advisory arm of the Aetas group, helping charities, not-for-profits, social enterprises and purpose-led organisations build organisational and financial resilience.

Aetas Impact is a service provided by **Aetas Wealth**, a trading style of Insight Financial Associates Limited, authorised and regulated by the Financial Conduct Authority (registration 458421). It is not a separate company.

**Live site:** https://impact.aetas-wealth.com

---

## What the site covers

Aetas Impact works with purpose-led organisations through the **Aetas Impact System** — one operating model for building resilience: *measure the risk, build resilience, sustain the mission.* It works across four drivers (Financial Resilience, Financial Education, People & Wellbeing, Organisational Capability) and is measured by the **Mission Resilience Index (MRI)**, a benchmarked 0-100 score established at the Impact Review and tracked over time.

Service areas: the **Impact Review** (a free, no-obligation diagnostic entry point), **People** (benefits and pension review, financial education, employee guidance), **Governance** (trustee support, governance reporting, Charity Governance Code alignment), and **Capacity** (organisational resilience, income diversification, strategic clarity).

---

## Site structure

All pages are static HTML files deployed via Cloudflare Pages / GitHub.

| File | Description |
|------|-------------|
| `index.html` | Homepage |
| `approach.html` | Shared Aetas philosophy ("better decisions create better futures") |
| `impact-system.html` | The Aetas Impact System - stages, four drivers, MRI, journey |
| `charities.html` | How we help |
| `roei.html` | ROEI in a charity context (nested within People & Wellbeing) |
| `diagnostic.html` | Impact Diagnostic self-assessment |
| `pricing.html` | Pricing |
| `insights.html` / `insights/` | Insights and articles |
| `faqs.html` | Frequently asked questions |
| `book-a-meeting.html` | Impact Review booking page |
| `financial-wellbeing.html` | Staff financial wellbeing |
| `manifesto.html` | Manifesto |
| `privacy.html` | Privacy policy |
| `CNAME` | Custom domain (`impact.aetas-wealth.com`) |
| `manifest.webmanifest` | PWA manifest |
| `robots.txt` | Search engine crawl instructions |
| `schema.json` | Structured data reference |
| `sitemap.xml` / `image-sitemap.xml` | Sitemaps |
| `llms.txt` / `llms-full.txt` | AI crawler guidance |

---

## Design and technology

- Pure static HTML, CSS, and vanilla JavaScript - no build tools or frameworks
- Custom design system using CSS variables
- Fully responsive
- Deployed automatically on every push to `main`

---

## Updating the site

**To edit a page:** open the relevant `.html` file, make your changes, and commit to `main`. Deployment happens automatically within about a minute.

**Nav and footer consistency:** every page shares the same nav and footer blocks and the standard "The Aetas Group" footer linking to Aetas Wealth, Aetas Performance and Aetas Impact. If these change, update them across all pages.

---

## The Aetas group

Aetas Impact is one of three specialist services under Aetas Wealth:

- **Aetas Wealth** (https://aetas-wealth.com) - independent financial planning for individuals, families and business owners
- **Aetas Performance** (https://performance.aetas-wealth.com) - workplace financial wellbeing and business performance (measured by ROEI)
- **Aetas Impact** (https://impact.aetas-wealth.com) - advisory for purpose-led organisations (measured by the MRI)

Financial wellbeing education and consultancy services do not in themselves constitute regulated financial advice. Where regulated advice is required, it is provided by Aetas Wealth.

---

## Contact

Matthew Steiner - matthew.steiner@aetas-wealth.com
