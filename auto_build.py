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
        "title": "How to Consolidate Multiple Xero & QuickBooks Accounts (Beginner Guide)",
        "tool": "Joiin",
        "headline": "Combining Multi-Company Accounts into One Financial Report",
        "intro": "Trying to combine multiple Xero or QuickBooks company accounts in Excel every month leads to formula errors and broken links. This beginner-proof guide shows you how to automate group financial reports in under 10 minutes.",
        "time": "10 Mins",
        "steps": [
            {"title": "Connect Your Accounting Apps", "desc": "Sign in to Joiin, click Companies -> Add Company, and select Xero or QuickBooks Online. Authorize 1-click read access.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Group Your Business Entities", "desc": "Check the boxes next to each subsidiary or franchise company you want to combine into your group balance sheet.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"},
            {"title": "Run & Export Consolidated Reports", "desc": "Navigate to Reports -> Profit & Loss. View side-by-side totals and export a presentation-ready board pack PDF.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"}
        ]
    },
    "multi-currency-financial-reporting": {
        "title": "Multi-Currency Financial Consolidation Setup Guide",
        "tool": "Joiin",
        "headline": "Combine Foreign Currency Accounts (USD, EUR, GBP, AUD)",
        "intro": "When your entities trade in different native currencies, manual FX rate math ruins financial reports. Learn how to translate foreign balances automatically.",
        "time": "8 Mins",
        "steps": [
            {"title": "Select Master Base Currency", "desc": "Set your group presentation currency in Joiin Settings (e.g., USD).", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Automatic Daily FX Conversions", "desc": "Joiin pulls official average and spot rates daily to convert P&L and Balance Sheet accounts effortlessly.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "intercompany-eliminations-guide": {
        "title": "Automating Intercompany Balance & Loan Eliminations",
        "tool": "Joiin",
        "headline": "Remove Internal Trading & Double-Counted Revenue",
        "intro": "Internal management fees and intercompany loans artificially inflate group income. Here is how to strip out internal trading cleanly.",
        "time": "7 Mins",
        "steps": [
            {"title": "Tag Intercompany GL Accounts", "desc": "Select the specific Chart of Accounts used for internal trading between parent and child companies.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Toggle One-Click Eliminations", "desc": "Apply the elimination rule to instantly remove internal revenue/expenses from your grand totals.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "automated-board-packs-and-kpi-reports": {
        "title": "How to Build Branded Executive Board Packs in Minutes",
        "tool": "Joiin",
        "headline": "Create Professional PDF Management Packs for Directors",
        "intro": "Stop spending hours copying numbers into PowerPoint. Learn how to generate branded financial presentation decks automatically.",
        "time": "5 Mins",
        "steps": [
            {"title": "Upload Brand Assets", "desc": "Add your logo and company brand colors in Joiin Settings.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Build & Export Pack", "desc": "Combine P&L, Balance Sheets, Cash Flow, and visual charts into a single downloadable PDF.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },

    # --- GEO TARGETLY GUIDES ---
    "geo-redirect-website-visitors-by-country": {
        "title": "How to Automatically Redirect Website Visitors by Country",
        "tool": "Geo Targetly",
        "headline": "Set Up Location-Based IP Redirection for Websites",
        "intro": "If you operate localized websites (e.g., .com for US, .co.uk for UK), manually sending users to the right version hurts sales. Learn how to auto-redirect traffic by IP address.",
        "time": "5 Mins",
        "steps": [
            {"title": "Create Geo Redirect Location Rule", "desc": "In Geo Targetly, set location rules (e.g., If visitor IP is in United Kingdom, redirect to /uk-store).", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Paste Script Tag on Website", "desc": "Copy the lightweight JavaScript snippet into your site header (WordPress, Shopify, Webflow, or HTML).", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "auto-currency-switcher-location": {
        "title": "How to Display Local Currency Based on Visitor Location",
        "tool": "Geo Targetly",
        "headline": "Automate Currency Switchers for Global E-Commerce",
        "intro": "Showing USD prices to European or UK shoppers leads to high cart abandonment. Here is how to automatically display prices in local currency.",
        "time": "6 Mins",
        "steps": [
            {"title": "Configure Currency Rules", "desc": "Set local target currencies (USD, EUR, GBP, CAD) based on visitor country detection.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Enable Automatic Price Conversion", "desc": "Embed the code on your store page so product prices instantly match the shopper's location.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "block-unwanted-country-traffic-website": {
        "title": "How to Block Traffic or Restrict Access by Country",
        "tool": "Geo Targetly",
        "headline": "Block Specific Countries or Regions from Viewing Your Site",
        "intro": "Prevent fraud, spam, or licensing violations by restricting access from specific geographic locations.",
        "time": "4 Mins",
        "steps": [
            {"title": "Set Blacklist / Whitelist Rules", "desc": "Choose which countries to block or allow in the Geo Targetly control panel.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Deploy Access Restriction Page", "desc": "Redirect blocked visitors to an alternative notification page or 403 screen.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "location-based-popup-banners": {
        "title": "How to Show Location-Specific Popups & Announcement Banners",
        "tool": "Geo Targetly",
        "headline": "Display Targeted Promotions Based on Visitor City or Country",
        "intro": "Increase conversions by showing targeted shipping offers, local events, or localized announcements.",
        "time": "5 Mins",
        "steps": [
            {"title": "Design Geo Popup Widget", "desc": "Customize banner text, offers, and CTA buttons for specific countries or cities.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Activate Geo Targeting Trigger", "desc": "Embed the embed code once; Geo Targetly serves the correct banner to each location.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },

    # --- AUDIORISTA GUIDES ---
    "convert-articles-audio-app-podcast": {
        "title": "How to Turn Written Articles & Content into Audio Apps",
        "tool": "Audiorista",
        "headline": "Convert Blog Posts & Text into Custom Audio Streams",
        "intro": "Publishers and creators can easily turn written content into high-quality audio feeds, private podcasts, and branded mobile apps.",
        "time": "6 Mins",
        "steps": [
            {"title": "Upload Text or Connect RSS Feed", "desc": "Import your blog posts or text manuscripts into Audiorista.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Generate AI Voiceovers or Upload Audio", "desc": "Convert text into natural AI speech or upload recorded audio tracks.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "monetize-audiobooks-private-audio-apps": {
        "title": "How to Sell Audiobooks & Premium Podcasts on Your Own App",
        "tool": "Audiorista",
        "headline": "Monetize Audio Content Directly Without Platform Fees",
        "intro": "Avoid massive app store cuts and build a subscription platform for audiobooks and courses.",
        "time": "8 Mins",
        "steps": [
            {"title": "Upload Audio Tracks & Set Paywall", "desc": "Organize chapters and configure paywall pricing options in Audiorista.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Connect Stripe Payments", "desc": "Accept direct subscriptions from listeners on iOS, Android, and Web.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "publish-white-label-audiobook-app": {
        "title": "How to Build a White-Label Audiobook App for Authors",
        "tool": "Audiorista",
        "headline": "Launch Your Own Branded Audio Streaming App",
        "intro": "Publish an iOS and Android app under your company name without writing custom code.",
        "time": "10 Mins",
        "steps": [
            {"title": "Upload Brand Branding & Assets", "desc": "Upload logo, splash screens, and layout themes inside Audiorista.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "One-Click App Store Publishing", "desc": "Submit your custom app directly to Apple App Store and Google Play.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    },
    "branded-audio-app-for-creators": {
        "title": "Branded Audio Streaming Platform Setup Guide for Creators",
        "tool": "Audiorista",
        "headline": "Build Private Podcasts & Paid Audio Communities",
        "intro": "Engage your audience with exclusive audio content, subscriber feeds, and branded mobile apps.",
        "time": "5 Mins",
        "steps": [
            {"title": "Create Subscriber Audio Portal", "desc": "Set up private access links and audio playlists for members.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Distribute Member Access Links", "desc": "Send instant access invites to your newsletter subscribers or community.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
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
        "steps": [
            {"title": "Initialize Setup", "desc": "Log in and configure your workspace settings.", "img": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png"},
            {"title": "Complete Integration", "desc": "Test the live setup and verify data outputs.", "img": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png"}
        ]
    })
    
    steps_html = ""
    for idx, s in enumerate(cfg['steps'], 1):
        steps_html += f"""
        <div class="step-card">
          <div class="step-header">
            <span class="step-badge">STEP {idx}</span>
            <h2 class="step-title">{s['title']}</h2>
          </div>
          <p class="step-text">{s['desc']}</p>
          <div class="img-container">
            <img src="{s['img']}" alt="{s['title']} screenshot" loading="lazy">
            <div class="img-caption">📸 Step {idx}: Interface configuration console</div>
          </div>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cfg['title']}</title>
  <style>
    :root {{ --primary: #0070f3; --border: #e2e8f0; }}
    * {{ box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 850px; margin: 0 auto; padding: 30px 20px; color: #0f172a; background: #f8fafc; line-height: 1.6; }}
    .container {{ background: white; border: 1px solid var(--border); border-radius: 12px; padding: 35px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }}
    .badge {{ display: inline-block; background: #e0f2fe; color: #0369a1; padding: 4px 12px; border-radius: 999px; font-weight: 700; font-size: 0.8rem; text-transform: uppercase; }}
    h1 {{ font-size: 2rem; margin: 15px 0; color: #0f172a; }}
    .intro {{ font-size: 1.1rem; color: #475569; margin-bottom: 25px; }}
    .pills {{ display: flex; gap: 15px; background: #f1f5f9; padding: 12px 18px; border-radius: 8px; font-weight: 600; font-size: 0.9rem; margin-bottom: 30px; }}
    .step-card {{ border: 1px solid var(--border); border-radius: 8px; padding: 24px; margin-bottom: 25px; background: white; }}
    .step-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }}
    .step-badge {{ background: var(--primary); color: white; padding: 4px 8px; border-radius: 4px; font-weight: 800; font-size: 0.75rem; }}
    .step-title {{ font-size: 1.3rem; margin: 0; }}
    .img-container {{ border: 1px solid var(--border); border-radius: 6px; overflow: hidden; margin-top: 15px; }}
    .img-container img {{ width: 100%; display: block; }}
    .img-caption {{ background: #f8fafc; padding: 8px; text-align: center; font-size: 0.85rem; color: #64748b; border-top: 1px solid var(--border); }}
    .cta {{ background: #0f172a; color: white; border-radius: 10px; padding: 30px; text-align: center; margin-top: 35px; }}
    .cta h2 {{ color: white; margin-top: 0; }}
    .btn {{ display: inline-block; background: var(--primary); color: white; text-decoration: none; padding: 14px 28px; border-radius: 6px; font-weight: bold; font-size: 1.1rem; margin-top: 15px; }}
  </style>
</head>
<body>
<div class="container">
  <span class="badge">Technical Setup Manual</span>
  <h1>{cfg['headline']}</h1>
  <p class="intro">{cfg['intro']}</p>

  <div class="pills">
    <div>⏱️ Estimated Time: {cfg['time']}</div>
    <div>⚡ Target Software: {cfg['tool']}</div>
  </div>

  {steps_html}

  <div class="cta">
    <h2>Ready to implement {cfg['tool']}?</h2>
    <p>Access official platform tools and start your trial in minutes.</p>
    <a href="{link}" class="btn" target="_blank" rel="noopener">Launch {cfg['tool']} Portal &rarr;</a>
  </div>

  <p style="margin-top: 30px;"><a href="/" style="color: #64748b; text-decoration: none;">&larr; Back to Stack Manuals Index</a></p>
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
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 900px; margin: 0 auto; padding: 40px 20px; color: #0f172a; background: #f8fafc; }}
    .header {{ text-align: center; margin-bottom: 40px; }}
    h1 {{ font-size: 2.5rem; margin-bottom: 10px; }}
    p.subtitle {{ color: #64748b; font-size: 1.1rem; }}
    .grid {{ display: grid; gap: 16px; margin-top: 30px; }}
    .card {{ background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px 24px; display: flex; align-items: center; justify-content: space-between; }}
    .card-tag {{ font-size: 0.75rem; font-weight: 700; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 4px; text-transform: uppercase; }}
    .card h3 {{ margin: 6px 0 0 0; font-size: 1.1rem; }}
    .card h3 a {{ text-decoration: none; color: #0f172a; }}
    .card-arrow {{ font-size: 1.5rem; color: #0070f3; text-decoration: none; font-weight: bold; padding-left: 15px; }}
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
