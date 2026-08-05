import json
import os
import sys
import time

api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("CRITICAL ERROR: GEMINI_API_KEY secret is missing!")
    sys.exit(1)

try:
    from google import genai
    client = genai.Client(api_key=api_key)
except Exception as e:
    print(f"Error initializing GenAI client: {e}")
    sys.exit(1)

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
    
    prompt = f"Create a clean, complete HTML webpage for {title}. Target audience: CFOs and accountants. Affiliate link: {link}. Include inline CSS styles. Return ONLY valid HTML code without markdown code blocks."

    response = None
    for model_name in ['gemini-2.5-flash', 'gemini-1.5-flash']:
        try:
            print(f"Generating page for {title} using {model_name}...")
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            if response and response.text:
                print(f"Successfully generated {filename}!")
                break
        except Exception as err:
            print(f"Model {model_name} failed: {err}")
            time.sleep(10)  # Wait if rate limited

    if not response or not response.text:
        print(f"ERROR: Could not generate content for {title}.")
        sys.exit(1)

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
    time.sleep(5)  # 5-second pause to prevent 429 rate limit errors

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
