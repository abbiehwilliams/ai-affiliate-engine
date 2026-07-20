import json
import os
from google import genai

# Load links
if not os.path.exists('links.json'):
    print("No links.json found.")
    exit(0)

with open('links.json', 'r') as f:
    links = json.load(f)

client = genai.Client()

os.makedirs('pages', exist_ok=True)

generated_guides = []

for key, link in links.items():
    filename = f"{key}.html"
    filepath = os.path.join('pages', filename)
    title = key.replace('-', ' ').title()
    
    prompt = f"""
    Create a clean, full-featured HTML webpage for a guide on '{title}'.
    Target audience: CFOs, accountants, and finance managers.
    Include step-by-step instructions and how this tool fixes multi-entity reporting / software integration issues.
    The primary affiliate link for {title} is: {link}
    Add a prominent call to action button linking to {link}.
    Return ONLY valid, complete HTML code including <!DOCTYPE html>, <html>, <head> with clean CSS styles, and <body>. Do not wrap in markdown ```html block.
    """

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )

    html_content = response.text.strip()
    if html_content.startswith("```html"):
        html_content = html_content[7:]
    if html_content.startswith("```"):
        html_content = html_content[3:]
    if html_content.endswith("```"):
        html_content = html_content[:-3]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content.strip())

    generated_guides.append({'slug': filename, 'title': title})

# Build index.html
cards_html = ""
for item in generated_guides:
    cards_html += f"""
    <li class="card">
      📌 <a href="/pages/{item['slug']}">{item['title']} Setup & Integration Guide</a>
    </li>
    """

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stack Manuals - B2B SaaS Setup Guides</title>
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
  <p class="subtitle">Step-by-step technical guides and workflow integration manuals for modern SaaS tools.</p>

  <h2>Available Documentation Guides</h2>
  <ul>
    {cards_html}
  </ul>

</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Build completed successfully!")
