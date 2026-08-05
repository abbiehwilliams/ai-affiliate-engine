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

for key, link in links.items():
    filename = f"{key}.html"
    filepath = os.path.join('pages', filename)
    title = key.replace('-', ' ').title()
    
    # Pure HTML template generated cleanly without external API limits
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Integration & Setup Guide</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      max-width: 800px;
      margin: 40px auto;
      padding: 0 20px;
      line-height: 1.6;
      color: #1a202c;
    }}
    h1 {{ font-size: 2.2rem; color: #111827; }}
    .badge {{ display: inline-block; background: #e0f2fe; color: #0369a1; padding: 4px 12px; border-radius: 9999px; font-weight: 600; font-size: 0.875rem; }}
    .cta-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; margin: 30px 0; text-align: center; }}
    .btn {{ display: inline-block; background: #0070f3; color: white; text-decoration: none; padding: 12px 24px; border-radius: 6px; font-weight: bold; font-size: 1rem; margin-top: 12px; }}
    .btn:hover {{ background: #0051a2; }}
    ul {{ padding-left: 20px; }}
    li {{ margin-bottom: 8px; }}
  </style>
</head>
<body>
  <span class="badge">Technical Guide</span>
  <h1>{title} Integration & Workflow Guide</h1>
  <p>This document provides setup steps for configuring {title} for CFOs, financial managers, and accounting departments.</p>
  
  <h2>Key Capabilities</h2>
  <ul>
    <li>Multi-entity data consolidation and automated reporting workflows.</li>
    <li>Direct synchronization with primary ledger platforms (Xero, QuickBooks, NetSuite).</li>
    <li>Audit-ready report exports and custom variance tracking templates.</li>
  </ul>

  <div class="cta-box">
    <h3>Ready to deploy {title}?</h3>
    <p>Access the official platform setup portal below:</p>
    <a href="{link}" class="btn" target="_blank" rel="noopener">Launch {title} Portal &rarr;</a>
  </div>

  <p><a href="/" style="color: #666; text-decoration: none;">&larr; Back to Stack Manuals</a></p>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content.strip())

    generated_guides.append({'slug': filename, 'title': title})

cards_html = ""
for item in generated_guides:
    cards_html += f'<li class="card">📌 <a href="/pages/{item["slug"]}">{item["title"]} Setup Guide</a></li>\n'

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stack Manuals - B2B SaaS Integration Guides</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      max-width: 800px;
      margin: 40px auto;
      padding: 0 20px;
      color: #333;
    }}
    h1 {{ font-size: 2.2rem; }}
    p.subtitle {{ color: #666; font-size: 1.1rem; margin-bottom: 30px; }}
    ul {{ list-style: none; padding: 0; }}
    .card {{
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 12px;
      transition: all 0.2s ease;
    }}
    .card:hover {{
      border-color: #0070f3;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    .card a {{
      text-decoration: none;
      color: #0070f3;
      font-weight: 600;
      font-size: 1.1rem;
    }}
  </style>
</head>
<body>
  <h1>🛠️ Stack Manuals</h1>
  <p class="subtitle">Technical documentation, workflow integrations, and setup manuals for B2B SaaS tools.</p>

  <h2>Available Documentation Guides</h2>
  <ul>
    {cards_html}
  </ul>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Build completed successfully!")
