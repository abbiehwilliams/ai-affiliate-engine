import json
import os
import sys

if not os.path.exists('links.json'):
    print("No links.json found.")
    sys.exit(0)

with open('links.json', 'r') as f:
    links = json.load(f)

os.makedirs('pages', exist_ok=True)
generated_guides = []

TOPIC_CONFIGS = {
    # --- JOIIN GUIDES ---
    "consolidate-xero-quickbooks": {
        "title": "How to Consolidate Multiple Xero & QuickBooks Accounts",
        "tool": "Joiin",
        "headline": "Combining Multi-Company Accounts into One Financial Report",
        "intro": "Trying to combine multiple Xero or QuickBooks company accounts in Excel every month leads to formula errors and broken links. This technical guide shows you how to automate group financial reporting in under 10 minutes.",
        "time": "10 Mins",
        "prereqs": ["Admin access to Xero, QuickBooks Online, or Sage", "Active Joiin account or trial subscription"],
        "steps": [
            {"title": "Connect Your Accounting Platforms", "desc": "Sign in to Joiin, navigate to <strong>Companies &rarr; Add Company</strong>, and select Xero, QuickBooks Online, or Sage. Complete the single-sign-on workflow to authorize read access for each entity."},
            {"title": "Configure Group Business Entities", "desc": "Access the <strong>Companies</strong> dashboard tab and select the checkbox next to each subsidiary or franchise entity you want to include in your combined financial statement calculations."},
            {"title": "Generate & Export Consolidated Statements", "desc": "Navigate to <strong>Reports &rarr; Profit & Loss</strong>. Review side-by-side totals across entities and export a presentation-ready board pack PDF or live web report link."}
        ]
    },
    "multi-currency-financial-reporting": {
        "title": "Multi-Currency Financial Consolidation Setup Guide",
        "tool": "Joiin",
        "headline": "Combine Foreign Currency Accounts (USD, EUR, GBP, AUD)",
        "intro": "When your entities trade in different native currencies, manual FX rate math ruins financial reports. Learn how to translate foreign balances automatically.",
        "time": "8 Mins",
        "prereqs": ["Logins for foreign subsidiary accounting accounts", "Target base presentation currency specified"],
        "steps": [
            {"title": "Select Master Base Currency", "desc": "Open <strong>Workspace Settings</strong> in Joiin and choose your primary target presentation currency (e.g., USD or EUR). All group total columns will compile in this currency."},
            {"title": "Automatic Daily FX Rate Synchronization", "desc": "Joiin automatically fetches daily exchange rates from official central banks. P&L line items translate using monthly average rates, while Balance Sheet items apply spot closing rates."}
        ]
    },
    "intercompany-eliminations-guide": {
        "title": "Automating Intercompany Balance & Loan Eliminations",
        "tool": "Joiin",
        "headline": "Remove Internal Trading & Double-Counted Revenue",
        "intro": "Internal management fees and intercompany loans artificially inflate group income. Here is how to strip out internal trading cleanly.",
        "time": "7 Mins",
        "prereqs": ["Chart of Accounts numbers for internal trading accounts"],
        "steps": [
            {"title": "Tag Intercompany GL Accounts", "desc": "In the Joiin dashboard, navigate to <strong>Eliminations</strong> and select the general ledger accounts used for internal management fees or intercompany loans."},
            {"title": "Apply One-Click Elimination Rules", "desc": "Toggle the <strong>Apply Eliminations</strong> filter on your Profit & Loss or Balance Sheet to deduct internal trading amounts from your grand totals."}
        ]
    },
    "automated-board-packs-and-kpi-reports": {
        "title": "How to Build Branded Executive Board Packs in Minutes",
        "tool": "Joiin",
        "headline": "Create Professional PDF Management Packs for Directors",
        "intro": "Stop spending hours copying numbers into PowerPoint. Learn how to generate branded financial presentation decks automatically.",
        "time": "5 Mins",
        "prereqs": ["High-resolution brand logo file (PNG/SVG)"],
        "steps": [
            {"title": "Upload Brand Style Assets", "desc": "Navigate to <strong>Settings &rarr; Branding</strong>. Upload your corporate logo and set custom brand hex colors for tables and headers."},
            {"title": "Compile & Export Report Pack", "desc": "Click <strong>Report Packs &rarr; Create Pack</strong>. Combine Profit & Loss statements, Balance Sheets, and visual KPI widgets into a single exportable PDF package."}
        ]
    },

    # --- GEO TARGETLY GUIDES ---
    "geo-redirect-website-visitors-by-country": {
        "title": "How to Automatically Redirect Website Visitors by Country",
        "tool": "Geo Targetly",
        "headline": "Set Up Location-Based IP Redirection for Websites",
        "intro": "If you operate localized websites (e.g., .com for US, .co.uk for UK), manually sending users to the right version hurts sales. Learn how to auto-redirect traffic by IP address.",
        "time": "5 Mins",
        "prereqs": ["Admin access to website header code or tag manager"],
        "steps": [
            {"title": "Create Location Rules", "desc": "Inside Geo Targetly, create a new <strong>Geo Redirect</strong> location rule (e.g., If visitor IP matches United Kingdom, redirect to /uk-store)."},
            {"title": "Embed Script Tag", "desc": "Copy the provided JavaScript snippet and paste it into the `<head>` tag of your website HTML or tag manager."}
        ]
    },
    "auto-currency-switcher-location": {
        "title": "How to Display Local Currency Based on Visitor Location",
        "tool": "Geo Targetly",
        "headline": "Automate Currency Switchers for Global E-Commerce",
        "intro": "Showing USD prices to European or UK shoppers leads to high cart abandonment. Here is how to automatically display prices in local currency.",
        "time": "6 Mins",
        "prereqs": ["E-Commerce store admin access"],
        "steps": [
            {"title": "Configure Target Currencies", "desc": "Set local target currencies (USD, EUR, GBP, CAD) based on country detection in your Geo Targetly dashboard."},
            {"title": "Activate Automatic Price Conversion", "desc": "Paste the snippet onto product pages to automatically render converted prices based on the user's IP geolocation."}
        ]
    },
    "block-unwanted-country-traffic-website": {
        "title": "How to Block Traffic or Restrict Access by Country",
        "tool": "Geo Targetly",
        "headline": "Block Specific Countries or Regions from Viewing Your Site",
        "intro": "Prevent fraud, spam, or licensing violations by restricting access from specific geographic locations.",
        "time": "4 Mins",
        "prereqs": ["Target list of blocked or whitelisted countries"],
        "steps": [
            {"title": "Set Blacklist Rules", "desc": "Select the specific geographic regions or countries you wish to block in the Geo Targetly control panel."},
            {"title": "Configure Restriction Response Page", "desc": "Choose whether blocked visitors see a customized access-denied message or get redirected to an external URL."}
        ]
    },
    "location-based-popup-banners": {
        "title": "How to Show Location-Specific Popups & Banners",
        "tool": "Geo Targetly",
        "headline": "Display Targeted Promotions Based on Visitor City or Country",
        "intro": "Increase conversions by showing targeted shipping offers, local events, or localized announcements.",
        "time": "5 Mins",
        "prereqs": ["Banner image or promo copy text"],
        "steps": [
            {"title": "Design Location Banner Widget", "desc": "Customize banner text, button links, and layout rules for target city or country demographics."},
            {"title": "Deploy Embed Code", "desc": "Add the single embed script to your site; Geo Targetly automatically filters banner visibility based on visitor location."}
        ]
    },

    # --- AUDIORISTA GUIDES ---
    "convert-articles-audio-app-podcast": {
        "title": "How to Turn Written Content into Audio Apps",
        "tool": "Audiorista",
        "headline": "Convert Articles & Text into Custom Audio Streams",
        "intro": "Publishers and creators can easily turn written content into high-quality audio feeds, private podcasts, and branded mobile apps.",
        "time": "6 Mins",
        "prereqs": ["RSS feed URL or blog manuscript files"],
        "steps": [
            {"title": "Import Text Manuscripts or Connect RSS", "desc": "Import text articles directly into Audiorista or connect your website's RSS feed for automatic syncing."},
            {"title": "Generate AI Voiceovers or Upload Audio", "desc": "Use high-fidelity AI text-to-speech engines or upload custom recorded MP3 tracks to create your audio stream."}
        ]
    },
    "monetize-audiobooks-private-audio-apps": {
        "title": "How to Sell Audiobooks & Premium Podcasts on Your App",
        "tool": "Audiorista",
        "headline": "Monetize Audio Content Directly Without Platform Fees",
        "intro": "Avoid massive app store cuts and build a subscription platform for audiobooks and courses.",
        "time": "8 Mins",
        "prereqs": ["Stripe account for direct payments"],
        "steps": [
            {"title": "Organize Audio Chapters & Paywall Rules", "desc": "Upload audio files, arrange content playlists, and set subscription or single-purchase pricing tiers."},
            {"title": "Connect Payment Processing", "desc": "Link your Stripe merchant account to accept direct payments across web, iOS, and Android platforms."}
        ]
    },
    "publish-white-label-audiobook-app": {
        "title": "How to Build a White-Label Audiobook App",
        "tool": "Audiorista",
        "headline": "Launch Your Own Branded Audio Streaming App",
        "intro": "Publish an iOS and Android app under your company name without writing custom code.",
        "time": "10 Mins",
        "prereqs": ["Apple Developer & Google Play Developer accounts"],
        "steps": [
            {"title": "Customize App Branding Assets", "desc": "Upload app icons, splash screen artwork, and brand color palettes inside Audiorista."},
            {"title": "Submit App for Publishing", "desc": "Follow the automated wizard to submit your custom-branded app directly to the Apple App Store and Google Play Store."}
        ]
    },
    "branded-audio-app-for-creators": {
        "title": "Branded Audio Platform Setup Guide for Creators",
        "tool": "Audiorista",
        "headline": "Build Private Podcasts & Paid Audio Communities",
        "intro": "Engage your audience with exclusive audio content, subscriber feeds, and branded mobile apps.",
        "time": "5 Mins",
        "prereqs": ["Existing audience or email list"],
        "steps": [
            {"title": "Configure Subscriber Audio Portal", "desc": "Build exclusive audio playlists and configure access permissions inside Audiorista."},
            {"title": "Distribute Member Invites", "desc": "Share private streaming access links or embed modern web players into your membership site."}
        ]
    }
}

for key, link in links.items():
    filename = f"{key}.html"
    filepath = os.path.join('pages', filename)
    
    cfg = TOPIC_CONFIGS.get(key, {
        "title": f"How to Set Up {key.replace('-', ' ').title()}",
        "tool": "Official Portal",
        "headline": f"Integration Guide for {key.replace('-', ' ').title()}",
        "intro": "Follow this beginner-friendly step-by-step setup guide.",
        "time": "5 Mins",
        "prereqs": ["Admin access to platform dashboard"],
        "steps": [
            {"title": "Initialize Integration", "desc": "Log in to the management dashboard and configure your workspace settings."},
            {"title": "Verify Deployment", "desc": "Test the connection and verify live data syncs."}
        ]
    })
    
    prereqs_html = "".join([f"<li>{p}</li>" for p in cfg.get('prereqs', ["Admin account access"])])
    
    steps_html = ""
    for idx, s in enumerate(cfg['steps'], 1):
        steps_html += f"""
        <div class="step-card">
          <div class="step-header">
            <span class="step-number">{idx}</span>
            <h2 class="step-title">{s['title']}</h2>
          </div>
          <p class="step-desc">{s['desc']}</p>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cfg['title']} - Stack Manuals</title>
  <style>
    :root {{
      --primary: #0070f3;
      --primary-hover: #0051a2;
      --slate-900: #0f172a;
      --slate-800: #1e293b;
      --slate-600: #475569;
      --slate-100: #f1f5f9;
      --border: #e2e8f0;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      max-width: 820px;
      margin: 0 auto;
      padding: 40px 20px 80px 20px;
      color: var(--slate-900);
      background: #f8fafc;
      line-height: 1.65;
    }}
    .container {{
      background: white;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 40px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .badge-bar {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 15px;
    }}
    .badge {{
      background: #e0f2fe;
      color: #0369a1;
      padding: 4px 12px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .status-badge {{
      background: #dcfce7;
      color: #166534;
      padding: 4px 12px;
      border-radius: 999px;
      font-weight: 600;
      font-size: 0.75rem;
    }}
    h1 {{
      font-size: 2.1rem;
      color: var(--slate-900);
      margin: 0 0 15px 0;
      line-height: 1.3;
    }}
    .intro {{
      font-size: 1.1rem;
      color: var(--slate-600);
      margin-bottom: 25px;
    }}
    .meta-card {{
      background: var(--slate-100);
      border-radius: 8px;
      padding: 16px 20px;
      display: flex;
      gap: 25px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--slate-800);
      margin-bottom: 30px;
    }}
    .prereq-box {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      border-radius: 8px;
      padding: 20px 24px;
      margin-bottom: 35px;
    }}
    .prereq-box h3 {{
      margin: 0 0 10px 0;
      font-size: 1rem;
      color: #0369a1;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .prereq-box ul {{
      margin: 0;
      padding-left: 20px;
      color: var(--slate-800);
    }}
    .prereq-box li {{ margin-bottom: 6px; }}
    .section-heading {{
      font-size: 1.4rem;
      margin: 35px 0 20px 0;
      border-bottom: 2px solid var(--slate-100);
      padding-bottom: 8px;
    }}
    .step-card {{
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 24px;
      margin-bottom: 20px;
      background: white;
      box-shadow: 0 2px 4px rgba(0,0,0,0.01);
    }}
    .step-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .step-number {{
      background: var(--primary);
      color: white;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.85rem;
    }}
    .step-title {{
      font-size: 1.25rem;
      margin: 0;
      color: var(--slate-900);
    }}
    .step-desc {{
      margin: 0;
      color: var(--slate-600);
      font-size: 1.02rem;
    }}
    .cta-banner {{
      background: var(--slate-900);
      color: white;
      border-radius: 12px;
      padding: 35px 25px;
      text-align: center;
      margin-top: 40px;
    }}
    .cta-banner h2 {{
      color: white;
      margin: 0 0 10px 0;
      font-size: 1.6rem;
    }}
    .cta-banner p {{
      color: #94a3b8;
      margin: 0 0 20px 0;
      font-size: 1.05rem;
    }}
    .btn {{
      display: inline-block;
      background: var(--primary);
      color: white;
      text-decoration: none;
      padding: 14px 28px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 1.05rem;
      transition: background 0.2s ease;
    }}
    .btn:hover {{ background: var(--primary-hover); }}
    .back-link {{
      display: inline-block;
      margin-top: 30px;
      color: var(--slate-600);
      text-decoration: none;
      font-weight: 600;
    }}
    .back-link:hover {{ color: var(--primary); }}
  </style>
</head>
<body>
<div class="container">
  <div class="badge-bar">
    <span class="badge">Verified Technical Manual</span>
    <span class="status-badge">✓ Updated 2026</span>
  </div>
  
  <h1>{cfg['headline']}</h1>
  <p class="intro">{cfg['intro']}</p>

  <div class="meta-card">
    <div>⏱️ Estimated Setup Time: {cfg['time']}</div>
    <div>⚡ Target Platform: {cfg['tool']}</div>
  </div>

  <div class="prereq-box">
    <h3>Prerequisites & System Requirements</h3>
    <ul>
      {prereqs_html}
    </ul>
  </div>

  <h2 class="section-heading">Step-by-Step Implementation Procedure</h2>

  {steps_html}

  <div class="cta-banner">
    <h2>Ready to implement {cfg['tool']}?</h2>
    <p>Access official portal tools and initialize your workspace in minutes.</p>
    <a href="{link}" class="btn" target="_blank" rel="noopener">Launch {cfg['tool']} Portal &rarr;</a>
  </div>

  <a href="/" class="back-link">&larr; Back to Stack Manuals Index</a>
</div>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content.strip())

    generated_guides.append({'slug': filename, 'title': cfg['headline'], 'tool': cfg['tool']})

cards_html = ""
for item in generated_guides:
    cards_html += f"""
    <div class="card">
      <div>
        <span class="card-tag">{item['tool']}</span>
        <h3><a href="/pages/{item['slug']}">{item['title']}</a></h3>
      </div>
      <a href="/pages/{item['slug']}" class="card-arrow">&rarr;</a>
    </div>
    """

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stack Manuals - Technical SaaS Integration Manuals</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      max-width: 880px;
      margin: 0 auto;
      padding: 50px 20px;
      color: #0f172a;
      background: #f8fafc;
    }}
    .header {{
      text-align: center;
      margin-bottom: 45px;
    }}
    h1 {{
      font-size: 2.4rem;
      margin: 0 0 10px 0;
      color: #0f172a;
    }}
    p.subtitle {{
      color: #64748b;
      font-size: 1.15rem;
      margin: 0;
    }}
    .grid {{
      display: grid;
      gap: 16px;
      margin-top: 30px;
    }}
    .card {{
      background: white;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 22px 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 2px 4px rgba(0,0,0,0.01);
      transition: all 0.2s ease;
    }}
    .card:hover {{
      border-color: #0070f3;
      box-shadow: 0 6px 16px rgba(0,0,0,0.04);
      transform: translateY(-1px);
    }}
    .card-tag {{
      font-size: 0.75rem;
      font-weight: 700;
      color: #0369a1;
      background: #e0f2fe;
      padding: 3px 10px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .card h3 {{
      margin: 8px 0 0 0;
      font-size: 1.15rem;
    }}
    .card h3 a {{
      text-decoration: none;
      color: #0f172a;
      font-weight: 600;
    }}
    .card-arrow {{
      font-size: 1.5rem;
      color: #0070f3;
      text-decoration: none;
      font-weight: bold;
      padding-left: 20px;
    }}
  </style>
</head>
<body>
  <div class="header">
    <h1>🛠️ Stack Manuals</h1>
    <p class="subtitle">Step-by-step setup guides, integration manuals, and SaaS tutorials.</p>
  </div>
  <div class="grid">{cards_html}</div>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Build completed successfully!")
