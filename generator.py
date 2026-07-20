import os
import json
from openai import OpenAI

# Reads the key securely from your system environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}

def load_tools(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def generate_guide(tool_name, tracking_link):
    print(f"⚡ Generating setup guide for: {tool_name}...")
    
    prompt = f"""
    Write a highly professional, step-by-step technical guide for setting up and configuring {tool_name} for business workflows.
    
    The guide must include:
    1. An introduction explaining what {tool_name} is best used for.
    2. Step-by-Step Setup & Configuration Guide.
    3. Top 3 Recommended Integration / Automation Use Cases.
    4. Common Field Mapping or Troubleshooting Tips.
    
    Format the entire output in clean Markdown.
    Do NOT include fake affiliate disclaimers in the text body.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior technical writer specializing in B2B SaaS software documentation and workflow automation."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content

    cta_block = f"\n\n---\n\n### 🚀 Ready to Get Started?\n" \
                f"Set up your official workspace and start building your workflows today: " \
                f"[{tool_name.capitalize()} Official Sign-Up]({tracking_link})\n"
    
    final_markdown = content + cta_block

    os.makedirs("pages", exist_ok=True)
    file_path = f"pages/{tool_name.lower().replace(' ', '-')}.md"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_markdown)
        
    print(f"✅ Saved guide to {file_path}")

def main():
    tools = load_tools("tools.txt")
    links = load_json("links.json")
    
    if not tools:
        print("❌ 'tools.txt' is empty or missing!")
        return

    for tool in tools:
        tracking_link = links.get(tool.lower(), "https://stackmanuals.com")
        generate_guide(tool, tracking_link)

    print("\n🎉 All manuals generated successfully in the /pages folder!")

if __name__ == "__main__":
    main()