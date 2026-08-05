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

# Customized configurations for each search intent topic
TOPIC_CONFIGS = {
    "consolidate-xero-quickbooks": {
        "title": "How to Consolidate Multiple Xero & QuickBooks Accounts",
        "description": "Step-by-step guide to combining separate Xero, QuickBooks, or Sage organizations into a single consolidated P&L and Balance Sheet.",
        "image_1": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png",
        "image_1_caption": "Visual dashboard combining multi-entity data across Xero and QuickBooks.",
        "image_2": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png",
        "image_2_caption": "Consolidated Group Profit & Loss statement export.",
        "step_1_title": "Connect Your Accounting Platforms",
        "step_1_desc": "Log into Joiin and click Add Company. Select Xero or QuickBooks Online to grant one-click secure API read access.",
        "step_2_title": "Select Entities for Group Statements",
        "step_2_desc": "Check the boxes for all parent and subsidiary entities you wish to include in your consolidated reporting workspace."
    },
    "multi-currency-financial-reporting": {
        "title": "Multi-Currency Financial Consolidation Setup Guide",
        "description": "How to automatically convert foreign currencies and generate global financial statements across USD, EUR, GBP, and AUD.",
        "image_1": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png",
        "image_1_caption": "Multi-currency reporting workspace showing automatic FX conversion rates.",
        "image_2": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png",
        "image_2_caption": "Converted balance sheet displayed in unified target base currency.",
        "step_1_title": "Set Base Group Currency",
        "step_1_desc": "Specify your overarching presentation currency (e.g., USD). Joiin automatically pulls real-time daily FX rates.",
        "step_2_title": "Apply Monthly FX Rate Adjustments",
        "step_2_desc": "Review average rate calculations for P&L accounts and closing spot rates for Balance Sheet items automatically."
    },
    "intercompany-eliminations-guide": {
        "title": "Automating Intercompany Balance & Loan Eliminations",
        "description": "Learn how to eliminate intercompany transactions, management fees, and internal loans without broken Excel formulas.",
        "image_1": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png",
        "image_1_caption": "Intercompany transaction workspace and reconciliation dashboard.",
        "image_2": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png",
        "image_2_caption": "Post-elimination consolidated report displaying accurate net balances.",
        "step_1_title": "Identify Intercompany Accounts",
        "step_1_desc": "Tag specific Chart of Accounts (COA) numbers designated for intercompany trading, loans, or shared service fees.",
        "step_2_title": "Apply One-Click Eliminations",
        "step_2_desc": "Toggle automatic intercompany eliminations to strip out internal revenue and expense duplicates instantly."
    },
    "automated-board-packs-and-kpi-reports": {
        "title": "Creating Automated Executive Board Packs & Management Reports",
        "description": "How to convert Xero and QuickBooks financial data into presentation-ready PDF report packs for board members and investors.",
        "image_1": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png",
        "image_1_caption": "Branded report pack builder with custom KPI widgets.",
        "image_2": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png",
        "image_2_caption": "Exported executive board pack in PDF format.",
        "step_1_title": "Choose Report Pack Template",
        "step_1_desc": "Select built-in financial packs including P&L, Balance Sheet, Cash Flow, and custom KPI summary graphs.",
        "step_2_title": "Add Company Branding & Export",
        "step_2_desc": "Upload your firm's logo, adjust color themes, and export as a presentation-ready PDF or live web link."
    },
    "multi-entity-accounting-for-agencies": {
        "title": "Scaling Multi-Client Financial Reporting for Accounting Firms",
        "description": "How fractional CFOs and accounting practices manage 10+ client entity groups efficiently under one platform.",
        "image_1": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png",
        "image_1_caption": "Multi-client practice console managing separate organization groups.",
        "image_2": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png",
        "image_2_caption": "Client-facing financial management dashboard view.",
        "step_1_title": "Structure Client Workspaces",
        "step_1_desc": "Set up distinct client environments while maintaining centralized staff access and permissions.",
        "step_2_title": "Automate Monthly Reporting Schedules",
        "step_2_desc": "Configure automated data syncs so client reports are populated instantly at month-end."
    },
    "cheaper-fathom-alternative-reporting": {
        "title": "Affordable Financial Consolidation: Joiin vs Enterprise Apps",
        "description": "Why growing companies use Joiin as a cost-effective alternative to Fathom, Syft, or NetSuite for multi-entity reporting.",
        "image_1": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png",
        "image_1_caption": "Streamlined consolidated dashboard interface.",
        "image_2": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png",
        "image_2_caption": "Fully detailed financial report generated without enterprise pricing.",
        "step_1_title": "Migrate Data from Spreadsheets",
        "step_1_desc": "Connect existing general ledgers without expensive implementation fees or long-term enterprise commitments.",
        "step_2_title": "Access Unlimited User Seats",
        "step_2_desc": "Grant report access to team leaders, department heads, and board members without per-user penalty fees."
    }
}

for key, link in links.items():
    filename = f"{key}.html"
    filepath = os.path.join('pages', filename)
    
    # Fetch fallback defaults if key is not explicitly mapped
    cfg = TOPIC_CONFIGS.get(key, {
        "title": f"How to Set Up {key.replace('-', ' ').title()} with Joiin",
        "description": f"Step-by-step technical guide for configuring {key.replace('-', ' ').title()} for group reporting.",
        "image_1": "https://images.ctfassets.net/3pr2433ts8v0/40wV3i9mZJzK2406kR36wE/2387140bdfadcf4ec163a8a81eb82d37/Joiin_Dashboard_Preview.png",
        "image_1_caption": "Joiin financial consolidation software dashboard view.",
        "image_2": "https://images.ctfassets.net/3pr2433ts8v0/53iR6aM3qL4kK110pR22wE/8267230bdfadcf4ec163a8a81eb82d38/Joiin_Report_Preview.png",
        "image_2_caption": "Exported multi-entity financial statement.",
        "step_1_title": "Initialize Platform Connection",
        "step_1_desc": "Connect your accounting entities to Joiin using official API integrations.",
        "step_2_title": "Generate Consolidated Reports",
        "step_2_desc": "Run real-time reports and export financial statements."
    })
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cfg['title']}</title>
  <meta name="description" content="{cfg['description']}">
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      max-width: 850px;
      margin: 40px auto;
      padding: 0 20px;
      line-height: 1.6;
      color: #1f2937;
    }}
    .badge {{ display: inline-block; background: #e0f2fe; color: #0369a1; padding: 4px 12px; border-radius: 9999px; font-weight: 600; font-size: 0.875rem; }}
    h1 {{ font-size: 2.1rem; color: #111827; margin-top: 10px; }}
    h2 {{ font-size: 1.4rem; color: #1f2937; border-bottom: 2px solid #f3f4f6; padding-bottom: 8px; margin-top: 35px; }}
    .meta-box {{ background: #f9fafb; border-left: 4px solid #0070f3; padding: 16px; margin: 20px 0; border-radius: 0 8px 8px 0; }}
    .step-number {{ display: inline-block; background: #0070f3; color: white; border-radius: 50%; width: 28px; height: 28px; text-align: center; line-height: 28px; font-weight: bold; margin-right: 8px; }}
    .img-card {{ background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; margin: 20px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }}
    .img-card img {{ width: 100%; height: auto; display: block; }}
    .img-card p {{ padding: 10px 14px; font-size: 0.875rem; color: #64748b; margin: 0; background: #f8fafc; text-align: center; border-top: 1px solid #f1f5f9; }}
    .cta-box {{ background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 12px; padding: 28px; margin: 40px 0; text-align: center; }}
    .btn {{ display: inline-block; background: #0070f3; color: white; text-decoration: none; padding: 14px 28px; border-radius: 8px; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
    .btn:hover {{ background: #0051a2; }}
  </style>
</head>
<body>

  <span class="badge">Technical Guide & Integration Manual</span>
  <h1>{cfg['title']}</h1>

  <div class="meta-box">
    <strong>Overview:</strong> {cfg['description']}
  </div>

  <h2>Step 1: {cfg['step_1_title']}</h2>
  <p>{cfg['step_1_desc']}</p>

  <div class="img-card">
    <img src="{cfg['image_1']}" alt="{cfg['step_1_title']} interface">
    <p>📸 Figure 1: {cfg['image_1_caption']}</p>
  </div>

  <h2>Step 2: {cfg['step_2_title']}</h2>
  <p>{cfg['step_2_desc']}</p>

  <div class="img-card">
    <img src="{cfg['image_2']}" alt="{cfg['step_2_title']} interface">
    <p>📸 Figure 2: {cfg['image_2_caption']}</p>
  </div>

  <div class="cta-box">
    <h2>Ready to automate this workflow?</h2>
    <p>Start generating consolidated reports in under 10 minutes using Joiin.</p>
    <a href="{link}" class="btn" target="_blank" rel="noopener">Launch Official Joiin Portal &rarr;</a>
  </div>

  <p><a href="/" style="color: #666; text-decoration: none;">&larr; Back to Stack Manuals Index</a></p>

</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content.strip())

    generated_guides.append({'slug': filename, 'title': cfg['title']})

# Generate homepage index.html
cards_html = ""
for item in generated_guides:
    cards_html += f'<li class="card">📌 <a href="/pages/{item["slug"]}">{item["title"]}</a></li>\n'

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stack Manuals - B2B SaaS Integration Guides</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 850px; margin: 40px auto; padding: 0 20px; color: #333; }}
    ul {{ list-style: none; padding: 0; }}
    .card {{ border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; margin-bottom: 12px; }}
    .card a {{ text-decoration: none; color: #0070f3; font-weight: 600; font-size: 1.05rem; }}
  </style>
</head>
<body>
  <h1>🛠️ Stack Manuals</h1>
  <p>Technical integration guides and financial consolidation procedures for modern SaaS platforms.</p>
  <ul>{cards_html}</ul>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Build completed successfully!")
