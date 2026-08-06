import json
import os
import sys

if not os.path.exists('links.json'):
    print("No links.json found.")
    sys.exit(0)

with open('links.json', 'r') as f:
    links = json.load(f)

os.makedirs('pages', exist_ok=True)

TOPIC_CONFIGS = {
    # --- AHASLIDES GUIDES ---
    "interactive-presentation-live-polls-quiz": {
        "title": "How to Create Interactive Presentations with Live Polls and Quizzes",
        "tool": "AhaSlides",
        "category": "Presentations & Audience Engagement",
        "headline": "Transform Static Decks into Live Audience-Engaging Presentations",
        "author": "Technical Documentation Team",
        "date": "Updated 2026",
        "summary": "Static PowerPoint slides often lead to passive audiences and low engagement. This step-by-step guide explains how to convert static presentations into live interactive sessions where participants vote, answer quizzes, and submit feedback using their smartphones in real time.",
        "time": "5 Minutes",
        "prereqs": [
            "Active AhaSlides account or free trial",
            "Existing presentation topic or slide outline (or PowerPoint/Google Slides file)",
            "Display screen or webinar screen-sharing software"
        ],
        "toc": [
            "Understanding Live Presentation Engagement",
            "Step 1: Initialize Workspace and Import Slides",
            "Step 2: Add Live Polling and Quiz Elements",
            "Step 3: Launch Session and Display Join Credentials",
            "Best Practices and Optimization"
        ],
        "steps": [
            {
                "title": "Initialize Workspace and Import Slides",
                "desc": "Sign in to your AhaSlides dashboard and click the <strong>Create Presentation</strong> button. If you already have an existing presentation deck, click <strong>Import</strong> to upload your PowerPoint (.pptx) or PDF file directly. The platform automatically converts your slides into an online presentation while preserving original layouts."
            },
            {
                "title": "Add Live Polling and Quiz Elements",
                "desc": "Select the exact point in your slide deck where you want audience interaction and click <strong>Add Slide</strong>. Choose your desired interaction type from the right-hand panel: <em>Multiple Choice, Live Quiz, Word Cloud, or Rating Scale</em>. Type your question in plain language and set response choices. For competitive quizzes, assign point values and time limits per question."
            },
            {
                "title": "Launch Session and Display Join Credentials",
                "desc": "Click the <strong>Present</strong> button in the top right corner. AhaSlides automatically displays a large QR code and a short joining URL at the top of your screen. Instruct your audience to point their mobile phone cameras at the QR code to join immediately—no app installation or login is required. Results update dynamically on screen as votes are submitted."
            }
        ],
        "tip": "Enable the Leaderboard option on quiz slides to automatically tally participant scores and display live rankings after each question round."
    },
    "host-live-qa-sessions-events-webinars": {
        "title": "How to Host Live Moderated Q&A Sessions for Events and Webinars",
        "tool": "AhaSlides",
        "category": "Presentations & Audience Engagement",
        "headline": "Host Structured, Upvoted Audience Q&A Sessions",
        "author": "Technical Documentation Team",
        "date": "Updated 2026",
        "summary": "Managing live audience questions verbally during events often leads to crosstalk and disorganization. This guide explains how to set up a digital Q&A queue with real-time audience upvoting and automated moderation filters.",
        "time": "6 Minutes",
        "prereqs": [
            "AhaSlides presenter account",
            "Webinar software or event stage display screen"
        ],
        "toc": [
            "Benefits of Digital Q&A Moderation",
            "Step 1: Create a Q&A Slide Module",
            "Step 2: Configure Upvoting and Moderation Filters",
            "Step 3: Manage Live Questions During Event",
            "Operational Guidelines"
        ],
        "steps": [
            {
                "title": "Create a Q&A Slide Module",
                "desc": "Inside your presentation workspace, click <strong>Add Slide</strong> and select <strong>Q&A</strong>. Choose whether the Q&A feature remains accessible only during a dedicated slide or stays open continuously throughout your entire presentation via a mobile bottom navigation bar."
            },
            {
                "title": "Configure Upvoting and Moderation Filters",
                "desc": "Open the settings panel on the right side of the screen. Toggle on <strong>Profanity Filter</strong> to block inappropriate language automatically. For corporate meetings, enable <strong>Moderate Questions</strong>. This routes incoming submissions to a private dashboard where a team member can review and approve questions before they appear on screen."
            },
            {
                "title": "Manage Live Questions During Event",
                "desc": "During the live presentation, display the Q&A screen. Audience members can upvote questions submitted by peers, pushing the most relevant topics to the top of the list. As you answer each question, click <strong>Mark as Answered</strong> to remove it from the active queue and keep the screen organized."
            }
        ],
        "tip": "Enabling anonymous question submission encourages higher engagement during sensitive corporate town halls or Q&A panels."
    },

    # --- UPTIMEROBOT GUIDES ---
    "monitor-website-downtime-alerts": {
        "title": "How to Set Up Automated Website Downtime Monitoring and Alerts",
        "tool": "UptimeRobot",
        "category": "Uptime & Server Monitoring",
        "headline": "Detect Server Downtime Instantly via SMS, Email, or Slack",
        "author": "Infrastructure Support Group",
        "date": "Updated 2026",
        "summary": "Unmonitored website crashes lead to lost sales, poor user experience, and dropped search rankings. This guide demonstrates how to configure continuous HTTP/HTTPS monitoring with automated incident alerts.",
        "time": "5 Minutes",
        "prereqs": [
            "Target domain URL or server IP address",
            "Access to team communication tools (Email, Slack, or Microsoft Teams)"
        ],
        "toc": [
            "Understanding Server Monitoring",
            "Step 1: Add HTTP Endpoint Monitor",
            "Step 2: Configure Checking Intervals",
            "Step 3: Connect Notification Channels",
            "Alert Escalation Best Practices"
        ],
        "steps": [
            {
                "title": "Add HTTP Endpoint Monitor",
                "desc": "Log into your UptimeRobot dashboard and click <strong>Add New Monitor</strong>. Select <strong>HTTP(s)</strong> as the monitor type. Enter a descriptive name for your monitor (such as <em>Primary Storefront</em>) and paste your complete website address including `https://`."
            },
            {
                "title": "Configure Checking Intervals",
                "desc": "Set your monitoring interval (such as every 60 seconds for critical web applications). Optionally enable <strong>Keyword Monitoring</strong> to verify that a specific word renders on page load, ensuring the server is not serving a blank screen."
            },
            {
                "title": "Connect Notification Channels",
                "desc": "Under the <em>Alert Contacts To Notify</em> section, select your email address, phone number for SMS, or link your team Slack webhook. UptimeRobot monitors your website continuously and sends an instant alert if an HTTP 500 server error or timeout is detected."
            }
        ],
        "tip": "Set up a secondary alert contact with a 5-minute delay so management is notified if on-call staff miss the initial alert."
    },
    "status-page-setup-incident-communication": {
        "title": "How to Build a Public Status Page for Incident Communication",
        "tool": "UptimeRobot",
        "category": "Uptime & Server Monitoring",
        "headline": "Create Transparent Public Status Pages for Customers",
        "author": "Infrastructure Support Group",
        "date": "Updated 2026",
        "summary": "During unexpected system outages, support teams face heavy volumes of repetitive customer inquiries. Learn how to launch a public status page that communicates system health in real time.",
        "time": "6 Minutes",
        "prereqs": [
            "Active UptimeRobot monitors",
            "Domain registrar DNS access (for custom domain setup)"
        ],
        "toc": [
            "The Purpose of Public Status Dashboards",
            "Step 1: Create Status Page Module",
            "Step 2: Apply Custom Branding and Subdomain",
            "Step 3: Publish and Link to Support Channels",
            "Maintenance Guidelines"
        ],
        "steps": [
            {
                "title": "Create Status Page Module",
                "desc": "Navigate to the <strong>Status Pages</strong> tab in UptimeRobot and click <strong>Add Status Page</strong>. Name your status portal and select which specific monitors (web applications, APIs, or databases) to display publicly."
            },
            {
                "title": "Apply Custom Branding and Subdomain",
                "desc": "Upload your corporate logo, set custom brand colors, and specify a custom web address (such as `status.yourcompany.com`). Inside your domain provider (such as Namecheap or GoDaddy), create a CNAME record pointing `status` to `stats.uptimerobot.com`."
            },
            {
                "title": "Publish and Link to Support Channels",
                "desc": "Save your configuration and publish the page. The status page displays historical uptime charts and real-time operational status without revealing sensitive backend IP details."
            }
        ],
        "tip": "Include a link to your public status page inside your website footer and help center to reduce support tickets during unexpected outages."
    },

    # --- JOIIN GUIDES ---
    "consolidate-xero-quickbooks": {
        "title": "How to Consolidate Multiple Xero and QuickBooks Accounts",
        "tool": "Joiin",
        "category": "Financial Consolidation",
        "headline": "Combining Multi-Company Accounts into One Financial Report",
        "author": "Financial Systems Audit Team",
        "date": "Updated 2026",
        "summary": "Combining financial reports across multiple companies in spreadsheets often results in broken formulas and reporting errors. This guide explains how to automate multi-entity financial consolidation cleanly.",
        "time": "10 Minutes",
        "prereqs": [
            "Admin access to Xero, QuickBooks Online, or Sage",
            "Active Joiin account or trial subscription"
        ],
        "toc": [
            "Overview of Multi-Entity Financial Consolidation",
            "Step 1: Connect Accounting Platforms",
            "Step 2: Map Custom Chart of Accounts",
            "Step 3: Generate and Export Consolidated Statements",
            "Financial Reporting Guidelines"
        ],
        "steps": [
            {
                "title": "Connect Accounting Platforms",
                "desc": "Log into your Joiin workspace, navigate to <strong>Companies &rarr; Add Company</strong>, and select your accounting software (Xero, QuickBooks Online, or Sage). Follow the prompt to authorize secure read-only access for each business entity."
            },
            {
                "title": "Map Custom Chart of Accounts",
                "desc": "Open the <strong>Chart of Accounts Mapping</strong> tool. If your subsidiaries use different account numbers or names for the same expenses, assign them to standardized master reporting categories so data combines accurately."
            },
            {
                "title": "Generate and Export Consolidated Statements",
                "desc": "Navigate to <strong>Reports &rarr; Profit & Loss</strong>. Review side-by-side revenue totals across all entities and click <strong>Export</strong> to download a PDF board pack or create a shareable report link."
            }
        ],
        "tip": "Save mapped account structures as templates to automatically apply identical reporting rules whenever new companies are added."
    },
    "multi-currency-financial-reporting": {
        "title": "Multi-Currency Financial Consolidation Setup Guide",
        "tool": "Joiin",
        "category": "Financial Consolidation",
        "headline": "Combine Foreign Currency Accounts (USD, EUR, GBP, AUD)",
        "author": "Financial Systems Audit Team",
        "date": "Updated 2026",
        "summary": "When company entities trade in different native currencies, manual exchange rate calculations can introduce accounting mistakes. Learn how to convert foreign balance sheets and income statements automatically.",
        "time": "8 Minutes",
        "prereqs": [
            "Logins for accounting software in foreign subsidiaries",
            "Selected group base currency"
        ],
        "toc": [
            "Multi-Currency Consolidation Standards",
            "Step 1: Set Master Group Currency",
            "Step 2: Automate FX Exchange Conversions",
            "Audit and Compliance Notes"
        ],
        "steps": [
            {
                "title": "Set Master Group Currency",
                "desc": "Open <strong>Workspace Settings</strong> in Joiin and choose your primary base reporting currency (such as USD or EUR). All subsidiary accounts will automatically convert into this currency for final reporting."
            },
            {
                "title": "Automate FX Exchange Conversions",
                "desc": "Joiin syncs daily currency rates automatically from central bank records. Profit and Loss statement items are converted using monthly average rates, while Balance Sheet accounts use official period-end closing rates."
            }
        ],
        "tip": "You can enter custom exchange rates manually for specific period-end dates if required by internal financial audits."
    },

    # --- GEO TARGETLY GUIDES ---
    "geo-redirect-website-visitors-by-country": {
        "title": "How to Automatically Redirect Website Visitors by Country",
        "tool": "Geo Targetly",
        "category": "Website Location & Traffic",
        "headline": "Set Up Location-Based IP Redirection for Websites",
        "author": "Web Operations Team",
        "date": "Updated 2026",
        "summary": "Directing international visitors to the correct regional website manually can cause lost sales and high bounce rates. Learn how to set up automated IP-based geographic redirection.",
        "time": "5 Minutes",
        "prereqs": [
            "Website header code access or Google Tag Manager"
        ],
        "toc": [
            "Principles of IP Geolocation Routing",
            "Step 1: Create Location Routing Rules",
            "Step 2: Embed JavaScript Tag",
            "Testing and Validation"
        ],
        "steps": [
            {
                "title": "Create Location Routing Rules",
                "desc": "Log into Geo Targetly, select <strong>Geo Redirect</strong>, and create a new rule. Define your target country and destination URL (for example: <em>If visitor IP is from United Kingdom, redirect to `/uk-store`</em>)."
            },
            {
                "title": "Embed JavaScript Tag",
                "desc": "Copy the lightweight code snippet generated by Geo Targetly. Paste the code into the `<head>` section of your website HTML or publish it using your tag manager."
            }
        ],
        "tip": "Enable 'First Visit Only' redirection so returning visitors can switch country versions manually without being forced back."
    },

    # --- AUDIORISTA GUIDES ---
    "convert-articles-audio-app-podcast": {
        "title": "How to Turn Written Content into Audio Apps",
        "tool": "Audiorista",
        "category": "Audio Publishing & Mobile Apps",
        "headline": "Convert Articles & Text into Custom Audio Streams",
        "author": "Digital Publishing Group",
        "date": "Updated 2026",
        "summary": "Publishers and creators can expand audience reach by converting written articles into clear audio streams, private podcasts, and dedicated mobile apps.",
        "time": "6 Minutes",
        "prereqs": [
            "Website RSS feed URL or text manuscript files"
        ],
        "toc": [
            "Overview of Text-to-Audio Publishing",
            "Step 1: Import Content or Connect RSS",
            "Step 2: Generate Audio Narrations",
            "Distribution Best Practices"
        ],
        "steps": [
            {
                "title": "Import Content or Connect RSS",
                "desc": "Log into Audiorista and import your text articles directly, or paste your blog RSS feed URL to enable automatic content synchronization whenever new posts are published."
            },
            {
                "title": "Generate Audio Narrations",
                "desc": "Select a clear AI text-to-speech voice model to generate narration automatically, or upload your own pre-recorded MP3 audio files for manual episode creation."
            }
        ],
        "tip": "Combine narration with subtle background audio tracks to create a high-quality listening experience."
    },

    # --- EMAILLISTVERIFY GUIDES ---
    "bulk-verify-email-lists-reduce-bounces": {
        "title": "How to Bulk Verify Email Lists and Reduce Bounce Rates",
        "tool": "EmailListVerify",
        "category": "Email Verification & Deliverability",
        "headline": "Scrub Marketing & Sales Lists Before Campaign Sending",
        "author": "Email Deliverability Team",
        "date": "Updated 2026",
        "summary": "High email bounce rates damage domain sender reputation and can cause account suspensions. Learn how to clean email lists before running outbound sales campaigns.",
        "time": "4 Minutes",
        "prereqs": [
            "CSV or TXT file containing email addresses"
        ],
        "toc": [
            "Importance of Email List Sanitation",
            "Step 1: Upload Contact File",
            "Step 2: Export Verified Addresses",
            "Deliverability Maintenance"
        ],
        "steps": [
            {
                "title": "Upload Contact File",
                "desc": "Sign in to EmailListVerify, click <strong>Verify List &rarr; Upload File</strong>, and select your CSV file containing contact records."
            },
            {
                "title": "Export Verified Addresses",
                "desc": "The verification system automatically scans email syntax, checks domain MX records, and verifies mailboxes. Download the final list containing only verified, deliverable email addresses."
            }
        ],
        "tip": "Verify any contact list that has not been emailed in over 60 days to remove inactive or closed corporate mailboxes."
    },

    # --- ICOMPASS GUIDES ---
    "automated-remote-team-task-management": {
        "title": "How to Automate Task Management for Distributed Remote Teams",
        "tool": "iCompass",
        "category": "Remote Work & Team Management",
        "headline": "Streamline Remote Team Collaboration & Project Tracking",
        "author": "Operations Management Group",
        "date": "Updated 2026",
        "summary": "Managing remote teams without centralized organization leads to missed project deadlines. Learn how to configure clear task workflows for remote teams.",
        "time": "8 Minutes",
        "prereqs": [
            "Admin user account on iCompass"
        ],
        "toc": [
            "Structuring Remote Operations",
            "Step 1: Create Team Workspaces",
            "Step 2: Assign Directives and Deadlines",
            "Workflow Monitoring"
        ],
        "steps": [
            {
                "title": "Create Team Workspaces",
                "desc": "Log into iCompass and set up dedicated project boards categorized by department, client account, or internal initiative."
            },
            {
                "title": "Assign Directives and Deadlines",
                "desc": "Create specific task items, assign responsible team members, attach relevant documents, and configure status updates to track progress."
            }
        ],
        "tip": "Set up automated weekly email summaries to review team progress without scheduling unnecessary status meetings."
    },

    # --- WARMUP INBOX GUIDES ---
    "warm-up-new-email-domain-cold-outreach": {
        "title": "How to Warm Up a New Email Domain for Cold Outreach",
        "tool": "Warmup Inbox",
        "category": "Email Deliverability & Outreach",
        "headline": "Automate Domain Warmup to Reach Primary Inboxes",
        "author": "Outreach Operations Group",
        "date": "Updated 2026",
        "summary": "Sending outbound emails from a brand-new domain often causes messages to land in spam folders. Learn how to warm up a domain automatically to build sender reputation.",
        "time": "5 Minutes",
        "prereqs": [
            "Email account with SMTP/IMAP enabled",
            "Configured SPF, DKIM, and DMARC DNS records"
        ],
        "toc": [
            "Domain Warmup Mechanics",
            "Step 1: Connect Mailbox Account",
            "Step 2: Enable Automated Network Exchange",
            "Reputation Monitoring"
        ],
        "steps": [
            {
                "title": "Connect Mailbox Account",
                "desc": "Log into Warmup Inbox, click <strong>Add Inbox</strong>, and sign in with your Google Workspace, Microsoft 365, or custom SMTP account."
            },
            {
                "title": "Enable Automated Network Exchange",
                "desc": "Warmup Inbox automatically connects your mailbox to a network of real inboxes that send, open, reply to, and un-spam your emails to build domain trust."
            }
        ],
        "tip": "Keep domain warmup running in the background even after launching sales campaigns to maintain positive engagement metrics."
    },

    # --- WOODPECKER GUIDES ---
    "automated-cold-email-drip-campaigns": {
        "title": "How to Set Up Automated Cold Email Drip Campaigns",
        "tool": "Woodpecker",
        "category": "Sales Automation & Cold Outreach",
        "headline": "Launch Personalised Outbound Email Sequences at Scale",
        "author": "Outreach Operations Group",
        "date": "Updated 2026",
        "summary": "Sending outbound sales emails manually takes time and lacks follow-up tracking. Learn how to set up automated email sequences with adaptive sending schedules.",
        "time": "8 Minutes",
        "prereqs": [
            "Woodpecker account",
            "Clean CSV lead list"
        ],
        "toc": [
            "Outbound Automation Setup",
            "Step 1: Connect Sending Mailbox",
            "Step 2: Build Multi-Step Email Sequences",
            "Step 3: Import Leads and Launch",
            "Campaign Optimization"
        ],
        "steps": [
            {
                "title": "Connect Sending Mailbox",
                "desc": "Sign in to Woodpecker and link your outbound email account. The platform checks settings automatically to protect deliverability."
            },
            {
                "title": "Build Multi-Step Email Sequences",
                "desc": "Write your opening email message and configure conditional follow-ups (for example: <em>If no response after 3 days, send Follow-up B</em>)."
            },
            {
                "title": "Import Leads and Launch",
                "desc": "Upload your verified contact CSV file and click <strong>Start Campaign</strong>. Woodpecker sends emails with human-like delays between messages."
            }
        ],
        "tip": "Use personalization tags such as {{FIRST_NAME}} and {{COMPANY}} to customize every email and increase reply rates."
    }
}

tools_dict = {}

for key, link in links.items():
    filename = f"{key}.html"
    filepath = os.path.join('pages', filename)
    
    cfg = TOPIC_CONFIGS.get(key, {
        "title": f"How to Set Up {key.replace('-', ' ').title()}",
        "tool": "Official Portal",
        "category": "General Integration",
        "headline": f"Integration Guide for {key.replace('-', ' ').title()}",
        "author": "Technical Documentation Team",
        "date": "Updated 2026",
        "summary": "Follow this step-by-step technical manual to complete your software implementation.",
        "time": "5 Minutes",
        "prereqs": ["Admin access to platform dashboard"],
        "toc": [
            "Overview",
            "Step 1: Initialize Configuration",
            "Step 2: Verify Setup Status",
            "Summary"
        ],
        "steps": [
            {"title": "Initialize Configuration", "desc": "Log into your software dashboard and navigate to administrative workspace settings to begin implementation."},
            {"title": "Verify Setup Status", "desc": "Run system diagnostic checks to ensure your configuration is active and data is transferring properly."}
        ],
        "tip": "Double-check administrative credentials before finalizing your setup."
    })
    
    prereqs_html = "".join([f"<li>{p}</li>" for p in cfg.get('prereqs', ["Admin account access"])])
    
    toc_html = "".join([f"<li><a href='#section-{idx}'>{item}</a></li>" for idx, item in enumerate(cfg.get('toc', []), 1)])
    
    steps_html = ""
    for idx, s in enumerate(cfg['steps'], 1):
        steps_html += f"""
        <div class="step-card" id="section-{idx}">
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
      --pastel-blue-bg: #f0f4f9;
      --pastel-blue-card: #ffffff;
      --pastel-blue-border: #dbe4ef;
      --pastel-blue-accent: #3b82f6;
      --pastel-blue-header: #1e3a8a;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --box-light: #eef4fb;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 0;
      color: var(--text-main);
      background: var(--pastel-blue-bg);
      line-height: 1.65;
    }}
    .navbar {{
      background: #ffffff;
      border-bottom: 1px solid var(--pastel-blue-border);
      padding: 16px 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .navbar-brand {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--pastel-blue-header);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .navbar-btn {{
      background: var(--pastel-blue-accent);
      color: white;
      text-decoration: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.9rem;
    }}
    .hero-banner {{
      background: #ffffff;
      border-bottom: 1px solid var(--pastel-blue-border);
      padding: 40px 20px;
      text-align: center;
    }}
    .hero-banner-inner {{
      max-width: 860px;
      margin: 0 auto;
    }}
    .category-badge {{
      display: inline-block;
      background: var(--box-light);
      color: var(--pastel-blue-header);
      padding: 4px 14px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 15px;
    }}
    h1 {{
      font-size: 2.2rem;
      color: var(--pastel-blue-header);
      margin: 0 0 15px 0;
      line-height: 1.25;
      font-weight: 800;
    }}
    .author-line {{
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 0;
    }}
    .content-wrapper {{
      max-width: 860px;
      margin: 40px auto 80px auto;
      padding: 0 20px;
    }}
    .main-card {{
      background: var(--pastel-blue-card);
      border: 1px solid var(--pastel-blue-border);
      border-radius: 12px;
      padding: 40px;
      box-shadow: 0 4px 16px rgba(30, 58, 138, 0.04);
    }}
    .hero-image-placeholder {{
      background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
      color: white;
      border-radius: 10px;
      padding: 40px 20px;
      text-align: center;
      margin-bottom: 30px;
    }}
    .hero-image-placeholder h2 {{
      color: white;
      margin: 0 0 10px 0;
      font-size: 1.5rem;
    }}
    .summary-text {{
      font-size: 1.1rem;
      color: var(--text-main);
      margin-bottom: 30px;
    }}
    .toc-box {{
      background: var(--box-light);
      border: 1px solid var(--pastel-blue-border);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 35px;
    }}
    .toc-box h3 {{
      margin: 0 0 12px 0;
      font-size: 1rem;
      color: var(--pastel-blue-header);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .toc-box ul {{
      margin: 0;
      padding-left: 20px;
      color: var(--pastel-blue-accent);
    }}
    .toc-box li {{ margin-bottom: 8px; }}
    .toc-box a {{
      color: var(--pastel-blue-accent);
      text-decoration: none;
      font-weight: 600;
    }}
    .toc-box a:hover {{ text-decoration: underline; }}
    .prereq-box {{
      background: #ffffff;
      border: 1px solid var(--pastel-blue-border);
      border-left: 4px solid var(--pastel-blue-accent);
      border-radius: 4px;
      padding: 20px 24px;
      margin-bottom: 35px;
    }}
    .prereq-box h3 {{
      margin: 0 0 10px 0;
      font-size: 1rem;
      color: var(--pastel-blue-header);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .prereq-box ul {{
      margin: 0;
      padding-left: 20px;
      color: var(--text-main);
    }}
    .prereq-box li {{ margin-bottom: 6px; }}
    .section-heading {{
      font-size: 1.5rem;
      color: var(--pastel-blue-header);
      margin: 40px 0 20px 0;
      border-bottom: 2px solid var(--box-light);
      padding-bottom: 8px;
    }}
    .step-card {{
      border: 1px solid var(--pastel-blue-border);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 24px;
      background: #ffffff;
    }}
    .step-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .step-number {{
      background: var(--pastel-blue-accent);
      color: white;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.9rem;
    }}
    .step-title {{
      font-size: 1.25rem;
      margin: 0;
      color: var(--pastel-blue-header);
    }}
    .step-desc {{
      margin: 0;
      color: var(--text-main);
      font-size: 1.02rem;
    }}
    .tip-box {{
      background: var(--box-light);
      border: 1px solid var(--pastel-blue-border);
      border-radius: 8px;
      padding: 20px 24px;
      margin-top: 30px;
      font-size: 0.98rem;
      color: var(--pastel-blue-header);
    }}
    .cta-banner {{
      background: var(--pastel-blue-header);
      color: white;
      border-radius: 10px;
      padding: 35px 25px;
      text-align: center;
      margin-top: 45px;
    }}
    .cta-banner h2 {{
      color: white;
      margin: 0 0 10px 0;
      font-size: 1.6rem;
    }}
    .cta-banner p {{
      color: #93c5fd;
      margin: 0 0 20px 0;
      font-size: 1.05rem;
    }}
    .btn {{
      display: inline-block;
      background: var(--pastel-blue-accent);
      color: white;
      text-decoration: none;
      padding: 14px 30px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 1.05rem;
    }}
    .back-link {{
      display: inline-block;
      margin-top: 30px;
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
    }}
    .back-link:hover {{ color: var(--pastel-blue-accent); }}
  </style>
</head>
<body>

<nav class="navbar">
  <a href="/" class="navbar-brand">Stack Manuals</a>
  <a href="{link}" class="navbar-btn" target="_blank" rel="noopener">Access {cfg['tool']} &rarr;</a>
</nav>

<header class="hero-banner">
  <div class="hero-banner-inner">
    <span class="category-badge">{cfg.get('category', 'Technical Documentation')}</span>
    <h1>{cfg['headline']}</h1>
    <p class="author-line">By {cfg.get('author', 'Technical Documentation Team')} &bull; {cfg.get('date', 'Updated 2026')}</p>
  </div>
</header>

<div class="content-wrapper">
  <div class="main-card">

    <div class="hero-image-placeholder">
      <h2>{cfg['headline']}</h2>
      <p>Official Integration Guide for {cfg['tool']}</p>
    </div>

    <p class="summary-text">{cfg.get('summary', '')}</p>

    <div class="toc-box">
      <h3>Table of Contents</h3>
      <ul>
        {toc_html}
      </ul>
    </div>

    <div class="prereq-box">
      <h3>Prerequisites and System Requirements</h3>
      <ul>
        {prereqs_html}
      </ul>
    </div>

    <h2 class="section-heading">Step-by-Step Implementation Procedure</h2>

    {steps_html}

    <div class="tip-box">
      <strong>Best Practice:</strong> {cfg.get('tip', 'Follow standard administrative guidelines to maintain system security.')}
    </div>

    <div class="cta-banner">
      <h2>Ready to implement {cfg['tool']}?</h2>
      <p>Access official portal tools and initialize your workspace in minutes.</p>
      <a href="{link}" class="btn" target="_blank" rel="noopener">Launch {cfg['tool']} Portal &rarr;</a>
    </div>

    <a href="/" class="back-link">&larr; Back to Stack Manuals Directory</a>
  </div>
</div>

</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content.strip())

    tool_name = cfg['tool']
    if tool_name not in tools_dict:
        tools_dict[tool_name] = []
    
    tools_dict[tool_name].append({
        'slug': filename,
        'title': cfg['headline'],
        'category': cfg.get('category', 'SaaS Manuals')
    })

sections_html = ""
for tool, manuals in tools_dict.items():
    cards_in_section = ""
    for item in manuals:
        cards_in_section += f"""
        <div class="card manual-card" data-title="{item['title'].lower()}" data-tool="{tool.lower()}">
          <div>
            <span class="card-tag">{item['category']}</span>
            <h3><a href="/pages/{item['slug']}">{item['title']}</a></h3>
          </div>
          <a href="/pages/{item['slug']}" class="card-arrow">&rarr;</a>
        </div>
        """
    
    sections_html += f"""
    <div class="tool-section" data-section-tool="{tool.lower()}">
      <div class="tool-header">
        <h2>{tool} Integration Manuals</h2>
        <span class="tool-count">{len(manuals)} Guides</span>
      </div>
      <div class="grid">
        {cards_in_section}
      </div>
    </div>
    """

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stack Manuals - Technical SaaS Integration Directory</title>
  <style>
    :root {{
      --pastel-blue-bg: #f0f4f9;
      --pastel-blue-card: #ffffff;
      --pastel-blue-border: #dbe4ef;
      --pastel-blue-accent: #3b82f6;
      --pastel-blue-header: #1e3a8a;
      --text-main: #1e293b;
      --text-muted: #64748b;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 0;
      color: var(--text-main);
      background: var(--pastel-blue-bg);
      line-height: 1.6;
    }}
    .navbar {{
      background: #ffffff;
      border-bottom: 1px solid var(--pastel-blue-border);
      padding: 16px 40px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .navbar-brand {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--pastel-blue-header);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .hero {{
      background: #ffffff;
      border-bottom: 1px solid var(--pastel-blue-border);
      padding: 60px 20px 40px 20px;
      text-align: center;
    }}
    h1 {{
      font-size: 2.6rem;
      margin: 0 0 12px 0;
      color: var(--pastel-blue-header);
      font-weight: 800;
    }}
    p.subtitle {{
      color: var(--text-muted);
      font-size: 1.15rem;
      margin: 0 0 35px 0;
    }}
    .search-box-wrapper {{
      position: relative;
      max-width: 620px;
      margin: 0 auto;
    }}
    .search-input {{
      width: 100%;
      padding: 16px 22px;
      font-size: 1.05rem;
      border: 2px solid var(--pastel-blue-border);
      border-radius: 8px;
      outline: none;
      background: #ffffff;
      box-shadow: 0 4px 12px rgba(30, 58, 138, 0.03);
      transition: all 0.2s ease;
    }}
    .search-input:focus {{
      border-color: var(--pastel-blue-accent);
      box-shadow: 0 4px 16px rgba(59, 130, 246, 0.15);
    }}
    .container {{
      max-width: 920px;
      margin: 40px auto 80px auto;
      padding: 0 20px;
    }}
    .tool-section {{
      margin-bottom: 50px;
    }}
    .tool-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid var(--pastel-blue-border);
      padding-bottom: 12px;
      margin-bottom: 20px;
    }}
    .tool-header h2 {{
      font-size: 1.4rem;
      margin: 0;
      color: var(--pastel-blue-header);
    }}
    .tool-count {{
      background: #e0f2fe;
      color: #0369a1;
      font-weight: 700;
      font-size: 0.8rem;
      padding: 4px 12px;
      border-radius: 999px;
    }}
    .grid {{
      display: grid;
      gap: 16px;
    }}
    .card {{
      background: #ffffff;
      border: 1px solid var(--pastel-blue-border);
      border-radius: 8px;
      padding: 22px 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .card:hover {{
      border-color: var(--pastel-blue-accent);
      box-shadow: 0 6px 16px rgba(30, 58, 138, 0.06);
      transform: translateY(-1px);
    }}
    .card-tag {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--pastel-blue-accent);
      background: #eef4fb;
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
      color: var(--pastel-blue-header);
      font-weight: 700;
    }}
    .card-arrow {{
      font-size: 1.5rem;
      color: var(--pastel-blue-accent);
      text-decoration: none;
      font-weight: bold;
      padding-left: 20px;
    }}
    .no-results {{
      display: none;
      text-align: center;
      padding: 40px;
      color: var(--text-muted);
      font-size: 1.1rem;
    }}
  </style>
</head>
<body>

  <nav class="navbar">
    <a href="/" class="navbar-brand">Stack Manuals</a>
  </nav>

  <div class="hero">
    <h1>Technical Integration Manuals</h1>
    <p class="subtitle">Searchable setup guides, configuration manuals, and SaaS tutorials.</p>

    <div class="search-box-wrapper">
      <input type="text" id="manualSearch" class="search-input" placeholder="Search guides (e.g., 'Xero', 'downtime', 'polls', 'email')..." onkeyup="filterManuals()">
    </div>
  </div>

  <div class="container">
    <div id="noResults" class="no-results">
      No integration manuals found matching your query.
    </div>

    <div id="sectionsContainer">
      {sections_html}
    </div>
  </div>

  <script>
    function filterManuals() {{
      const query = document.getElementById('manualSearch').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.manual-card');
      const sections = document.querySelectorAll('.tool-section');
      let visibleCount = 0;

      cards.forEach(card => {{
        const title = card.getAttribute('data-title');
        const tool = card.getAttribute('data-tool');

        if (title.includes(query) || tool.includes(query)) {{
          card.style.display = 'flex';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      sections.forEach(section => {{
        const visibleCardsInSection = section.querySelectorAll('.manual-card[style*="display: flex"]');
        if (visibleCardsInSection.length === 0 && query !== '') {{
          section.style.display = 'none';
        }} else {{
          section.style.display = 'block';
        }}
      }});

      const noResults = document.getElementById('noResults');
      if (visibleCount === 0 && query !== '') {{
        noResults.style.display = 'block';
      }} else {{
        noResults.style.display = 'none';
      }}
    }}
  </script>

</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Build completed successfully!")
