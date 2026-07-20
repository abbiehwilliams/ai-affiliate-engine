import json
import os
from google import genai

# Read API Key explicitly
api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable is missing.")
    exit(1)

client = genai.Client(api_key=api_key)

if not os.path.exists('links.json'):
    print("No links.json found.")
    exit(0)

with open('links.json', 'r') as f:
    links = json.load(f)

os.makedirs('pages', exist_ok=True)
generated_guides = []

for key, link in links.items():
    filename = f"{key}.html"
    filepath = os.path.join('pages', filename)
    title = key.replace('-', ' ').title()
    
    prompt = f"Create a clean, complete HTML webpage for {title}. Target audience: CFOs and accountants. Affiliate link: {link}. Include inline CSS styles. Return ONLY valid HTML code without markdown code blocks."

    # Updated to gemini-3.5-flash
    response = client.models.generate_content(
        model='gemini-3.5-flash',
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

cards_html = ""
for item in generated_guides:
    cards_html += f'<li class="card">📌 <a href="/pages/{item["slug"]}">{item["title"]} Setup Guide</a></li>\n'

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stack Manuals</title>
  <style>
    body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; }}
    ul {{ list-style: none; padding: 0; }}
    .card {{ border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 6px; }}
    .card a {{ text-decoration: none; color: #0070f3; font-weight: bold; }}
  </style>
</head>
<body>
  <h1>🛠️ Stack Manuals</h1>
  <ul>{cards_html}</ul>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Build completed successfully!")
