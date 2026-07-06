import re, os, glob

BOOK_URL = "https://charities.aetas-wealth.com/book-a-meeting"
BASE_URL = "https://charities.aetas-wealth.com"

# ============================================================
# NEW NAV — matches Workplace pattern, charity-specific solutions
# ============================================================
NEW_NAV = '''<header class="site-header">
<div class="container nav-inner">
  <a href="{PREFIX}./" class="brand" aria-label="Aetas for Charities home">
    <span class="brand-mark"><img fetchpriority="high" src="{PREFIX}aetas-mark.svg" alt="Aetas" width="52" height="52"></span>
    <span class="brand-text">
      <span class="brand-name">AETAS</span>
      <span class="brand-division">for Charities</span>
    </span>
  </a>
  <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links">
    <li><a href="{PREFIX}">Home</a></li>
    <li class="nav-dropdown">
      <a href="#" class="nav-dropdown-toggle" aria-haspopup="true" aria-expanded="false">Solutions <span class="nav-caret">&#9660;</span></a>
      <ul class="nav-dropdown-menu">
        <li><a href="{PREFIX}charities">Charity Performance Audit</a></li>
        <li><a href="{PREFIX}financial-wellbeing">Financial Wellbeing</a></li>
        <li><a href="{PREFIX}roei">ROEI Framework</a></li>
        <li><a href="{PREFIX}diagnostic">Diagnostic</a></li>
        <li><a href="{PREFIX}calculator">Calculator</a></li>
      </ul>
    </li>
    <li><a href="{PREFIX}insights">Insights</a></li>
    <li><a href="{PREFIX}faqs">FAQs</a></li>
    <li><a href="{PREFIX}book-a-meeting" class="nav-cta">Book an Initial Conversation</a></li>
  </ul>
</div>
</header>'''

# ============================================================
# NEW FOOTER
# ============================================================
NEW_FOOTER = '''<!-- SHARED: site-footer -->
<footer class="site-footer">
<div class="container">
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="brand" style="margin-bottom:1rem;">
        <span class="brand-mark" style="background:#fff;padding:4px;border-radius:4px;">
          <img src="{PREFIX}aetas-mark.svg" alt="Aetas" width="36" height="36">
        </span>
        <span class="brand-text">
          <span class="brand-name" style="color:#fff;">AETAS</span>
          <span class="brand-division" style="color:var(--aetas-turquoise,#00747E);">for Charities</span>
        </span>
      </div>
      <p style="color:#c8d0e0;font-size:0.9rem;">Organisational performance and resilience consultancy for UK charities and not-for-profit organisations.</p>
      <p style="margin-top:0.75rem;font-size:0.88rem;"><a href="mailto:matthew.steiner@aetas-wealth.com" style="color:rgba(255,255,255,0.7);">matthew.steiner@aetas-wealth.com</a></p>
    </div>
    <div>
      <h4>Navigate</h4>
      <ul>
        <li><a href="{PREFIX}">Home</a></li>
        <li><a href="{PREFIX}charities">Charity Performance Audit</a></li>
        <li><a href="{PREFIX}financial-wellbeing">Financial Wellbeing</a></li>
        <li><a href="{PREFIX}roei">ROEI Framework</a></li>
        <li><a href="{PREFIX}pricing">Pricing</a></li>
        <li><a href="{PREFIX}faqs">FAQs</a></li>
        <li><a href="{PREFIX}insights">Insights</a></li>
      </ul>
    </div>
    <div>
      <h4>Tools</h4>
      <ul>
        <li><a href="{PREFIX}diagnostic">Charity Diagnostic</a></li>
        <li><a href="{PREFIX}calculator">ROEI Calculator</a></li>
      </ul>
      <h4 style="margin-top:1.5rem;">Also part of Aetas</h4>
      <ul>
        <li><a href="https://aetas-wealth.com/" target="_blank" rel="noopener">Aetas Wealth</a></li>
        <li><a href="https://workplace.aetas-wealth.com/" target="_blank" rel="noopener">Aetas in the Workplace</a></li>
      </ul>
    </div>
    <div>
      <h4>Offices</h4>
      <p style="font-weight:600;color:#fff;margin:0 0 0.3rem;">London</p>
      <ul style="margin-bottom:1.25rem;">
        <li>13 Hanover Square</li>
        <li>Mayfair, London</li>
        <li>W1S 1HN</li>
      </ul>
      <p style="font-weight:600;color:#fff;margin:0 0 0.3rem;">Norwich</p>
      <ul>
        <li>Insight House</li>
        <li>7a Alkmaar Way</li>
        <li>Norwich NR6 6BF</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom" style="border-top:1px solid rgba(255,255,255,0.12);margin-top:3rem;padding-top:1.5rem;">
    <p style="font-size:0.82rem;color:rgba(255,255,255,0.6);">Aetas for Charities provides financial wellbeing, governance and consultancy services. Where regulated financial advice is required, this is provided by Aetas Wealth, a trading style of Insight Financial Associates Limited, authorised and regulated by the Financial Conduct Authority (FCA registration: 458421).</p>
    <p style="font-size:0.82rem;color:rgba(255,255,255,0.5);margin-top:0.75rem;">&#169; <span data-year>2026</span> Aetas for Charities. All rights reserved. <a href="{PREFIX}privacy" style="text-decoration:underline;color:rgba(255,255,255,0.5);">Privacy Policy</a></p>
  </div>
</div>
</footer>
<!-- /site-footer -->'''

# ============================================================
# BRAND CSS — same as Workplace
# ============================================================
BRAND_CSS = '''
/* ---- Master brand hierarchy ---- */
.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
}
.brand-mark {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  flex-shrink: 0;
}
.brand-mark img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}
.brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1;
  gap: 3px;
}
.brand-name {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--aetas-blue, #00205B);
  line-height: 1;
}
.brand-text .brand-division {
  font-size: 0.68rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  font-style: italic;
  text-transform: none;
  color: var(--aetas-turquoise, #00747E);
  line-height: 1;
}

/* ---- Nav dropdown ---- */
.nav-dropdown { position: relative; }
.nav-dropdown-menu {
  display: none;
  position: absolute;
  top: calc(100% + 0.5rem);
  left: 0;
  background: var(--aetas-blue, #00205B);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 4px;
  min-width: 220px;
  padding: 0.5rem 0;
  list-style: none;
  z-index: 200;
  box-shadow: 0 8px 24px rgba(0,0,0,0.18);
}
.nav-dropdown-menu li a {
  display: block;
  padding: 0.6rem 1.25rem;
  color: rgba(255,255,255,0.85);
  font-size: 0.9rem;
  text-decoration: none;
  transition: color 0.15s, background 0.15s;
}
.nav-dropdown-menu li a:hover { color: #fff; background: rgba(255,255,255,0.08); }
.nav-dropdown:hover .nav-dropdown-menu { display: block; }
.nav-caret { font-size: 0.6rem; margin-left: 0.3rem; vertical-align: middle; }
@media (max-width: 768px) {
  .nav-dropdown-menu { position: static; box-shadow: none; border: none; background: transparent; padding: 0 0 0 1rem; }
  .nav-dropdown-menu li a { color: rgba(0,32,91,0.7); padding: 0.4rem 0; font-size: 0.88rem; }
  .nav-dropdown:hover .nav-dropdown-menu { display: none; }
  .nav-dropdown.is-open .nav-dropdown-menu { display: block; }
}
'''

NAV_DROPDOWN_JS = '''
  // Dropdown nav on mobile
  document.querySelectorAll('.nav-dropdown-toggle').forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      if (window.innerWidth <= 1024) {
        e.preventDefault();
        var parent = btn.closest('.nav-dropdown');
        parent.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', parent.classList.contains('is-open') ? 'true' : 'false');
      }
    });
  });
'''

CTA_BLOCK = '''<!-- BOOK CTA -->
<section class="section section-blue" id="book">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow" style="color:#d4a847;">Get started</span>
      <h2 style="color:#fff;">Book an Initial Conversation</h2>
      <p style="color:rgba(255,255,255,0.78);">A focused conversation with Matthew Steiner, at no cost and with no obligation. Thirty minutes to understand where your organisation stands and what, if anything, would make a measurable difference.</p>
    </div>
    <div class="grid grid-3" style="margin-top:2.5rem;">
      <div style="text-align:center;padding:1.5rem;background:rgba(255,255,255,0.07);border-radius:4px;border:1px solid rgba(255,255,255,0.14);">
        <p style="font-size:1.6rem;margin:0 0 0.5rem;color:#fff;">30</p>
        <p style="color:rgba(255,255,255,0.7);margin:0;font-size:0.9rem;">minutes</p>
      </div>
      <div style="text-align:center;padding:1.5rem;background:rgba(255,255,255,0.07);border-radius:4px;border:1px solid rgba(255,255,255,0.14);">
        <p style="font-size:1.6rem;margin:0 0 0.5rem;color:#fff;">No</p>
        <p style="color:rgba(255,255,255,0.7);margin:0;font-size:0.9rem;">cost or obligation</p>
      </div>
      <div style="text-align:center;padding:1.5rem;background:rgba(255,255,255,0.07);border-radius:4px;border:1px solid rgba(255,255,255,0.14);">
        <p style="font-size:1.6rem;margin:0 0 0.5rem;color:#fff;">Clear</p>
        <p style="color:rgba(255,255,255,0.7);margin:0;font-size:0.9rem;">next steps either way</p>
      </div>
    </div>
    <div class="text-center" style="margin-top:2.5rem;">
      <a href="''' + BOOK_URL + '''" class="btn btn-primary btn-arrow">Book an Initial Conversation</a>
    </div>
  </div>
</section>'''

ECOSYSTEM_BLOCK = '''<!-- ECOSYSTEM -->
<section class="section section-soft">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Also part of Aetas</span>
      <h2>One group. Three specialist practices.</h2>
      <p>Whether the need is personal financial planning, workplace performance, or charity governance, Aetas covers the full picture across the organisations and individuals it works with.</p>
    </div>
    <div class="grid grid-2" style="margin-top:2.5rem;">
      <a href="https://aetas-wealth.com/" target="_blank" rel="noopener" class="card" style="text-decoration:none;">
        <div class="card-icon" style="font-size:0.7rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">Wealth</div>
        <h3>Aetas Wealth</h3>
        <p>Personal financial planning for directors, business owners and senior professionals. Retirement, inheritance, investment and protection through the Lifetime to Legacy framework.</p>
        <span class="card-link">Visit Aetas Wealth</span>
      </a>
      <a href="https://workplace.aetas-wealth.com/" target="_blank" rel="noopener" class="card" style="text-decoration:none;">
        <div class="card-icon" style="font-size:0.7rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;">Workplace</div>
        <h3>Aetas in the Workplace</h3>
        <p>Financial wellbeing, employee benefits and workplace performance consultancy for SME employers. Delivered through the ROEI framework.</p>
        <span class="card-link">Visit Aetas in the Workplace</span>
      </a>
    </div>
  </div>
</section>'''

def remove_em_dashes(html):
    for pat in ['\u2014', '&mdash;', '&#8212;', '&#x2014;']:
        html = html.replace(pat, ', ')
    return html

def fix_nav(html, depth=0):
    prefix = '../' * depth
    nav = NEW_NAV.replace('{PREFIX}', prefix)
    old = re.search(r'<header class="site-header">[\s\S]*?</header>', html)
    if old:
        html = html[:old.start()] + nav + html[old.end():]
    return html

def fix_footer(html, depth=0):
    prefix = '../' * depth
    footer = NEW_FOOTER.replace('{PREFIX}', prefix)
    old = re.search(r'<!-- SHARED: site-footer -->[\s\S]*?<!-- /site-footer -->|<footer class="site-footer">[\s\S]*?</footer>', html)
    if old:
        html = html[:old.start()] + footer + html[old.end():]
    return html

def inject_brand_css(html):
    if '.brand-name' not in html:
        html = html.replace('</style>', BRAND_CSS + '\n</style>', 1)
    return html

def inject_dropdown_js(html):
    if 'nav-dropdown-toggle' not in html or 'is-open' not in html:
        if "'use strict';" in html:
            html = html.replace("'use strict';", "'use strict';\n" + NAV_DROPDOWN_JS, 1)
        elif '<script>' in html:
            html = html.replace('<script>', '<script>\n' + NAV_DROPDOWN_JS, 1)
        else:
            html = html.replace('</body>', '<script>' + NAV_DROPDOWN_JS + '</script>\n</body>', 1)
    return html

def fix_meta(html, title=None, desc=None, canon=None, ai_sum=None, og_title=None, og_desc=None):
    if title:
        html = re.sub(r'<title[^>]*>.*?</title>', f'<title>{title}</title>', html, flags=re.S)
    if desc:
        p = r'<meta\s+name=["\']description["\'][^>]*/?>|<meta\s+content=["\'][^"\']*["\'][^>]*name=["\']description["\'][^>]*/?>'
        nt = f'<meta name="description" content="{desc}">'
        if re.search(p, html): html = re.sub(p, nt, html, count=1)
        else: html = html.replace('</head>', f'  {nt}\n</head>', 1)
    if canon:
        p = r'<link[^>]*rel=["\']canonical["\'][^>]*/?>|<link[^>]*canonical[^>]*/?>'
        nt = f'<link rel="canonical" href="{canon}">'
        if re.search(p, html): html = re.sub(p, nt, html, count=1)
        else: html = html.replace('</head>', f'  {nt}\n</head>', 1)
    if ai_sum and 'ai-agent-summary' not in html:
        html = html.replace('<meta name="viewport"', f'<meta name="ai-agent-summary" content="{ai_sum}">\n  <meta name="viewport"', 1)
    if og_title:
        p = r'<meta\s+property=["\']og:title["\'][^>]*/?>'
        nt = f'<meta property="og:title" content="{og_title}">'
        if re.search(p, html): html = re.sub(p, nt, html, count=1)
        else: html = html.replace('</head>', f'  {nt}\n</head>', 1)
    if og_desc:
        p = r'<meta\s+property=["\']og:description["\'][^>]*/?>'
        nt = f'<meta property="og:description" content="{og_desc}">'
        if re.search(p, html): html = re.sub(p, nt, html, count=1)
        else: html = html.replace('</head>', f'  {nt}\n</head>', 1)
    return html

def inject_cta_and_ecosystem(html):
    if 'id="book"' not in html:
        footer_marker = '<!-- SHARED: site-footer -->'
        if footer_marker not in html:
            footer_marker = '<footer class="site-footer">'
        if footer_marker in html:
            html = html.replace(footer_marker, CTA_BLOCK + '\n\n' + footer_marker, 1)
    if 'Also part of Aetas' not in html:
        cta_marker = '<!-- BOOK CTA -->'
        if cta_marker not in html:
            cta_marker = '<footer class="site-footer">'
        if cta_marker in html:
            html = html.replace(cta_marker, ECOSYSTEM_BLOCK + '\n\n' + cta_marker, 1)
    return html

def add_faq_schema(html, faqs):
    if 'FAQPage' in html:
        return html
    items = '\n'.join([f'''    {{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}''' for q,a in faqs])
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'
    html = html.replace('</head>', schema + '\n</head>', 1)
    return html

# Page-specific meta and FAQ data
PAGE_DATA = {
    'index.html': {
        'title': 'Aetas for Charities | Charity Performance Consultancy',
        'desc': 'Helping UK charities improve organisational performance, financial resilience and governance. Start with a no-cost Charity Performance Audit.',
        'canon': BASE_URL + '/',
        'ai_sum': 'Aetas for Charities is a specialist consultancy for UK charities and not-for-profits. Delivers financial wellbeing, governance support, trustee training and organisational performance programmes. Entry point: no-cost Charity Performance Audit. Delivered by Aetas Wealth (FCA 458421).',
        'og_title': 'Aetas for Charities | Charity Performance Consultancy',
        'og_desc': 'Helping UK charities improve performance, financial resilience and governance. Start with a no-cost Charity Performance Audit.',
        'faqs': [
            ("What does Aetas for Charities do?", "Aetas for Charities provides financial wellbeing, governance support and organisational performance consultancy to UK charities and not-for-profit organisations."),
            ("How does the Charity Performance Audit work?", "The Audit is a no-cost, no-obligation conversation with Matthew Steiner to identify where financial pressure or governance gaps are affecting your organisation."),
            ("Is there a cost to the initial conversation?", "No. The initial Charity Performance Audit is provided at no cost and carries no obligation.")
        ]
    },
    'charities.html': {
        'title': 'Charity Performance Audit | Aetas for Charities',
        'desc': 'The Charity Performance Audit identifies where financial pressure and governance gaps are affecting your organisation. No cost, no obligation.',
        'canon': BASE_URL + '/charities',
        'ai_sum': 'The Charity Performance Audit is the entry point for Aetas for Charities. A structured no-cost conversation identifying financial pressure, governance gaps and organisational performance issues in UK charities.',
        'faqs': [
            ("What is the Charity Performance Audit?", "A structured no-cost conversation that identifies where financial pressure, governance gaps or wellbeing issues are affecting your charity's performance and resilience."),
            ("Who is the Charity Performance Audit for?", "CEOs, finance directors, trustees and HR leads at UK charities and not-for-profit organisations of any size."),
            ("What happens after the Audit?", "You receive a written summary of findings and recommendations. No commitment is required until you have reviewed the proposal.")
        ]
    },
    'financial-wellbeing.html': {
        'title': 'Financial Wellbeing for Charities | Aetas for Charities',
        'desc': 'Practical financial wellbeing programmes for charity staff and volunteers. Workshops, one-to-one guidance and ongoing support tailored for the third sector.',
        'canon': BASE_URL + '/financial-wellbeing',
        'ai_sum': 'Financial wellbeing programmes for UK charities. Covers staff workshops, one-to-one financial guidance and ongoing support. Delivered by Aetas for Charities.',
        'faqs': [
            ("What financial wellbeing support does Aetas offer charities?", "Aetas offers staff workshops, one-to-one financial guidance sessions with a regulated financial planner, and ongoing access to tools and support."),
            ("How is charity financial wellbeing different from corporate programmes?", "Charity staff often face unique financial pressures including lower pay, sector uncertainty and pension provision gaps. Aetas designs programmes specifically for the third sector context."),
            ("Does financial wellbeing support count as regulated advice?", "The education and workshop elements are not regulated advice. Where individual regulated financial advice is needed, this is provided through Aetas Wealth, FCA registered (FRN 458421).")
        ]
    },
    'roei.html': {
        'ai_sum': 'ROEI (Return on Employee Investment) framework applied to UK charities. Measures the commercial and organisational return on investment in staff, benefits and wellbeing programmes.',
    },
    'insights.html': {
        'title': 'Insights | Aetas for Charities',
        'desc': 'Research, commentary and practical thinking on charity governance, financial wellbeing and organisational performance from Aetas for Charities.',
        'canon': BASE_URL + '/insights',
        'ai_sum': 'Insights hub for Aetas for Charities. Covers charity governance, trustee responsibilities, financial wellbeing for charity staff and organisational performance.',
        'faqs': [
            ("What topics does Aetas for Charities cover in its insights?", "Topics include charity governance, CC14 trustee guidance, financial wellbeing for charity staff, investment policy statements, legacy giving and financial anxiety in the third sector."),
            ("Who writes the Aetas for Charities insights?", "Insights are produced by Matthew Steiner, Managing Director of Aetas, drawing on more than 20 years in financial services and specialist charity sector experience."),
            ("Are the Aetas insights free to read?", "Yes. All insights are freely available on the Aetas for Charities website with no registration required.")
        ]
    },
    'faqs.html': {
        'ai_sum': 'Frequently asked questions about Aetas for Charities, covering the Charity Performance Audit, fees, financial wellbeing programmes and how the service works for trustees and charity leaders.',
    },
    'pricing.html': {
        'ai_sum': 'Pricing information for Aetas for Charities. Three programme tiers covering the Charity Performance Audit, financial wellbeing delivery and ongoing governance support.',
    },
    'calculator.html': {
        'ai_sum': 'The Aetas Charity ROEI Calculator estimates the cost of financial pressure in your charity workforce. Provides a baseline for the Charity Performance Audit.',
    },
    'diagnostic.html': {
        'ai_sum': 'The Aetas Charity Financial Wellbeing Diagnostic. A self-assessment tool for charity leaders to measure their organisation readiness and identify where financial pressure is affecting performance.',
    },
    'book-a-meeting.html': {
        'title': 'Book an Initial Conversation | Aetas for Charities',
        'desc': 'Book your no-cost Charity Performance Audit with Matthew Steiner. A 30-minute conversation to understand where your charity stands and what could make a measurable difference.',
        'ai_sum': 'Booking page for the Aetas for Charities initial conversation and Charity Performance Audit.',
    },
}

INSIGHT_FAQS = {
    'cash-management-charity-treasurers': [
        ("What should charity treasurers consider for cash management?", "Charity treasurers should review cash reserves policy, ensure appropriate diversification across banking providers, and consider whether cash is working appropriately in the current interest rate environment."),
        ("How much cash should a charity hold in reserve?", "The Charity Commission recommends charities hold reserves sufficient to cover three to six months of operating costs. The exact level depends on income volatility and the nature of the charity's activities."),
        ("What is the role of the treasurer in a charity?", "The treasurer is responsible for overseeing the financial health of the charity, presenting financial reports to the board, and ensuring that the charity's resources are managed responsibly in line with its objects.")
    ],
    'charity-commission-cc14-trustees': [
        ("What is the Charity Commission CC14 guidance?", "CC14 is the Charity Commission's guidance on investment for charities. It sets out the legal framework for trustee investment decisions, including the duty to take advice and consider social investments."),
        ("Do charity trustees have a duty to invest?", "Yes. Trustees have a duty to make any funds not immediately needed for the charity's purposes work appropriately. This includes reviewing cash held on deposit and considering whether an investment policy statement is needed."),
        ("What should a charity investment policy statement include?", "An IPS should cover the charity's investment objectives, risk appetite, ethical considerations, asset allocation, performance benchmarks and review frequency.")
    ],
    'financial-anxiety-staff-charities': [
        ("Why is financial anxiety particularly prevalent in charities?", "Charity sector salaries are often lower than equivalent private sector roles, and staff frequently face sector uncertainty and funding pressures. These structural factors increase financial stress among charity employees."),
        ("What can charity employers do to reduce financial anxiety among staff?", "Practical steps include reviewing pension provision, offering financial education workshops, providing access to confidential guidance, and ensuring staff understand and value their existing benefits."),
        ("How does financial anxiety affect charity performance?", "Financial anxiety reduces focus and productivity, increases absence, and contributes to the high staff turnover that many charities experience. Addressing it has a direct impact on organisational performance.")
    ],
    'investment-fees-charities': [
        ("Are charity investment fees tax deductible?", "Investment management fees charged to a charity's investment portfolio are generally an allowable expense. Trustees should ensure fees are reasonable and well-documented."),
        ("How should charity trustees review investment manager fees?", "Trustees should benchmark fees against comparable mandates, understand the full cost including platform charges, and ensure the investment manager's performance justifies the fee over a reasonable time horizon."),
        ("What is a reasonable investment management fee for a charity?", "Fees vary by mandate size and complexity. For pooled charity funds, total expense ratios of 0.3 to 0.8 per cent are typical. For bespoke mandates, fees of 0.5 to 1.0 per cent are common. Trustees should seek competitive quotes.")
    ],
    'ips-review-charity': [
        ("What is an Investment Policy Statement for a charity?", "An IPS is a document that sets out how a charity's investment assets will be managed. It covers objectives, risk tolerance, ethical exclusions, asset allocation, performance benchmarks and review procedures."),
        ("How often should a charity review its IPS?", "The Charity Commission recommends an annual review of the IPS, or more frequently if there are significant changes to the charity's financial position or objectives."),
        ("Who is responsible for the IPS in a charity?", "The full board of trustees is responsible for the IPS, not just the treasurer or finance committee. All trustees should understand and have approved the investment policy.")
    ],
    'legacy-giving-programme-charity': [
        ("What is a legacy giving programme for charities?", "A legacy giving programme encourages supporters to leave a gift to the charity in their will. It is one of the most valuable long-term income streams available to charities of any size."),
        ("How do charities start a legacy programme?", "Charities typically start by identifying existing supporters who might consider a legacy gift, developing appropriate communication materials, and ensuring the charity has the infrastructure to acknowledge and administer legacy gifts."),
        ("What types of legacy can supporters leave to charities?", "The main types are pecuniary legacies (a specific sum), residuary legacies (a share of the estate after other bequests) and specific legacies (a particular asset). Residuary legacies are typically the most valuable to charities.")
    ],
}

# ============================================================
# PROCESS ALL FILES
# ============================================================
files = sorted(glob.glob('/home/claude/Charity-Wellbeing-Service/**/*.html', recursive=True) +
               glob.glob('/home/claude/Charity-Wellbeing-Service/*.html'))
skip = {'google4bf7b0394b6b5986.html'}
seen = set()
processed = 0
errors = []

for path in files:
    if os.path.basename(path) in skip:
        continue
    real = os.path.realpath(path)
    if real in seen:
        continue
    seen.add(real)

    try:
        with open(path, encoding='utf-8') as f:
            html = f.read()

        rel = os.path.relpath(path, '/home/claude/Charity-Wellbeing-Service')
        depth = rel.count(os.sep)
        name = os.path.basename(path)
        parent = os.path.basename(os.path.dirname(path))

        # 1. Em dashes
        html = remove_em_dashes(html)

        # 2. Brand CSS
        html = inject_brand_css(html)

        # 3. Dropdown JS
        html = inject_dropdown_js(html)

        # 4. Nav
        html = fix_nav(html, depth)

        # 5. Footer
        html = fix_footer(html, depth)

        # 6. Page-specific meta
        slug = name.replace('.html', '')
        page_key = rel if rel in PAGE_DATA else name
        if page_key in PAGE_DATA:
            pd = PAGE_DATA[page_key]
            html = fix_meta(html,
                title=pd.get('title'),
                desc=pd.get('desc'),
                canon=pd.get('canon'),
                ai_sum=pd.get('ai_sum'),
                og_title=pd.get('og_title'),
                og_desc=pd.get('og_desc')
            )
            if 'faqs' in pd:
                html = add_faq_schema(html, pd['faqs'])

        # 7. Insight article FAQs
        if parent == 'insights' and slug in INSIGHT_FAQS:
            html = add_faq_schema(html, INSIGHT_FAQS[slug])

        # 8. CTA + Ecosystem on main pages
        if depth == 0 and name not in {'privacy.html', 'book-a-meeting.html', 'google4bf7b0394b6b5986.html'}:
            html = inject_cta_and_ecosystem(html)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        processed += 1
        print(f'OK  {rel}')

    except Exception as e:
        errors.append((path, str(e)))
        print(f'ERR {rel}: {e}')

print(f'\nProcessed: {processed}, Errors: {len(errors)}')
