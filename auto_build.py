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
        "title": "How to Create Interactive Presentations with Live Polls & Quizzes",
        "tool": "AhaSlides",
        "category": "Presentations & Audience Engagement",
        "headline": "Transform Static Decks into Live Audience-Engaging Presentations",
        "intro": "Boring PowerPoint slides alienate audiences. Learn how to convert static presentations into live interactive sessions where participants vote, answer quizzes, and submit feedback via their smartphones in real time.",
        "time": "5 Mins",
        "prereqs": ["Existing presentation topic or slide outline", "Smartphone or computer for host setup"],
        "steps": [
            {"title": "Initialize Your Interactive Deck", "desc": "Log in to AhaSlides and click <strong>Create Presentation</strong>. Choose whether to start from scratch or import existing PowerPoint (.pptx) or Google Slides files into the cloud editor."},
            {"title": "Embed Live Interactive Poll & Quiz Slides", "desc": "Click <strong>Add Slide</strong> and select your desired interaction type: Multiple Choice Poll, Live Quiz, Word Cloud, or Rating Scale. Type your question and configure answer choices or point values."},
            {"title": "Display QR Code & Launch Live Presentation", "desc": "Click <strong>Present</strong>. A large QR code and URL join-code will render at the top of the screen. Audience members scan the code with their mobile cameras to join and interact instantly without downloading an app."}
        ],
        "tip": "Enable background music and countdown timers in the slide settings to keep energy high during live competitive quiz rounds."
    },
    "host-live-qa-sessions-events-webinars": {
        "title": "How to Host Live Moderated Q&A Sessions for Events & Webinars",
        "tool": "AhaSlides",
        "category": "Presentations & Audience Engagement",
        "headline": "Host Structured, Upvoted Audience Q&A Sessions",
        "intro": "Managing live event questions verbally leads to crosstalk and awkward silences. This guide shows you how to capture, filter, and prioritize live audience questions digitally.",
        "time": "6 Mins",
        "prereqs": ["Webinar software or physical event stage display"],
        "steps": [
            {"title": "Add a Dedicated Q&A Slide", "desc": "In your AhaSlides workspace, select <strong>Q&A Slide</strong>. Enable question upvoting so the audience can vote for the queries they want answered most."},
            {"title": "Configure Content Moderation Filters", "desc": "Toggle <strong>Profanity Filter</strong> and <strong>Moderate Questions</strong> in the settings tab. This allows a co-host or moderator to approve questions behind the scenes before they appear on the public screen."},
            {"title": "Run the Live Segment & Mark Answered", "desc": "During the Q&A window, display the live question feed. As you address each query, click <strong>Mark as Answered</strong> to clear the queue and keep the stage view structured."}
        ],
        "tip": "Enable 'Anonymous Submissions' if your event covers sensitive business topics—it increases audience question volume by up to 3x."
    },
    "word-cloud-generator-audience-feedback": {
        "title": "How to Generate Real-Time Word Clouds from Audience Input",
        "tool": "AhaSlides",
        "category": "Presentations & Audience Engagement",
        "headline": "Create Dynamic Real-Time Word Clouds in Meetings",
        "intro": "Collecting open-ended feedback from teams or audiences usually yields scattered notes. Learn how to generate live, visually striking word clouds that grow dynamically as participants submit responses.",
        "time": "4 Mins",
        "prereqs": ["Presenter dashboard access"],
        "steps": [
            {"title": "Select Word Cloud Slide Template", "desc": "Inside AhaSlides, choose <strong>Word Cloud</strong> from the slide library. Type your prompt (e.g., 'What is our biggest priority for Q3 in one word?')."},
            {"title": "Set Response Rules & Submission Limits", "desc": "Configure maximum allowed entries per participant (e.g., 3 words max) and set a time limit (e.g., 60 seconds)."},
            {"title": "Broadcast Live Word Visualization", "desc": "Launch the slide. As participants type words into their phones, the entries display live on screen—popular terms automatically scale larger in real-time."}
        ],
        "tip": "Use word clouds as icebreakers at the start of remote Zoom or Teams meetings to boost participant engagement before deep-dive topics."
    },
    "spinner-wheel-random-name-picker-events": {
        "title": "How to Set Up a Live Spinner Wheel for Giveaways & Name Picking",
        "tool": "AhaSlides",
        "category": "Presentations & Audience Engagement",
        "headline": "Add Gamification with Custom Interactive Spinner Wheels",
        "intro": "Adding gamification to webinars, classrooms, or team meetings boosts retention. Here is how to create a custom interactive spinner wheel for prize draws and random participant selection.",
        "time": "4 Mins",
        "prereqs": ["List of participant names or prize items"],
        "steps": [
            {"title": "Add Spinner Wheel Slide", "desc": "In AhaSlides, select <strong>Spinner Wheel</strong>. Paste your list of entries (names, team names, or prize awards) into the text input box."},
            {"title": "Customize Wheel Sound Effects & Animation Speed", "desc": "Select your color theme, spin duration (e.g., 5 seconds), and toggle celebratory confetti animations upon landing."},
            {"title": "Spin Live & Remove Winning Entries", "desc": "Click <strong>Spin</strong> during your presentation. Once a winning entry lands, click <strong>Remove Entry</strong> so names are not picked twice in subsequent rounds."}
        ],
        "tip": "Pre-load attendee rosters into the wheel before launching a meeting to instantly pick random presenters without bias."
    },

    # --- UPTIMEROBOT GUIDES ---
    "monitor-website-downtime-alerts": {
        "title": "How to Set Up Automated Website Downtime Monitoring & Alerts",
        "tool": "UptimeRobot",
        "category": "Uptime & Server Monitoring",
        "headline": "Detect Server Downtime Instantly via SMS, Email, or Slack",
        "intro": "When your website or API crashes, every offline minute costs money and damages brand trust. Learn how to monitor server availability 24/7 with instant incident notifications.",
        "time": "5 Mins",
        "prereqs": ["Target website URL or server IP address"],
        "steps": [
            {"title": "Create HTTP(s) Monitor", "desc": "Sign in to UptimeRobot and click <strong>Add New Monitor</strong>. Select monitor type <strong>HTTP(s)</strong> and enter your target URL (e.g., https://yourwebsite.com)."},
            {"title": "Configure Check Intervals & Timeout Rules", "desc": "Set your monitoring check frequency (e.g., every 60 seconds) and configure HTTP status code expectations (200 OK)."},
            {"title": "Add Notification Integration Channels", "desc": "Choose where alerts send when downtime occurs: Email, SMS, Slack channel, Microsoft Teams webhook, or Push notification."}
        ],
        "tip": "Set up a secondary alert contact so key team members get notified if primary engineers don't acknowledge the incident within 5 minutes."
    },
    "status-page-setup-incident-communication": {
        "title": "How to Build a Public Status Page for Incident Communication",
        "tool": "UptimeRobot",
        "category": "Uptime & Server Monitoring",
        "headline": "Create Transparent Public Status Pages for Customers",
        "intro": "During outages, support inboxes get flooded with ticket inquiries. Here is how to set up a clean public status page that communicates real-time system health transparently.",
        "time": "6 Mins",
        "prereqs": ["Active UptimeRobot monitors", "Custom CNAME domain record (optional)"],
        "steps": [
            {"title": "Initialize Public Status Page", "desc": "In UptimeRobot, navigate to <strong>Status Pages &rarr; Add Status Page</strong>. Name your page (e.g., 'Acme Corp System Status')."},
            {"title": "Select Services to Display", "desc": "Check the boxes for the specific website, API, or database monitors you want visible on the public dashboard."},
            {"title": "Custom Domain Mapping & Branding", "desc": "Upload your corporate logo, set custom CSS colors, and add a CNAME record (e.g., status.yourcompany.com) for professional white-labeling."}
        ],
        "tip": "Link your status page URL directly in your app's footer and support portal to reduce support tickets during unexpected outages."
    },
    "ssl-certificate-expiry-monitoring-alerts": {
        "title": "How to Monitor SSL Certificate Expiry & Prevent Security Warnings",
        "tool": "UptimeRobot",
        "category": "Uptime & Server Monitoring",
        "headline": "Prevent Broken SSL Certificates with Automated Expiry Reminders",
        "intro": "Expired SSL certificates display terrifying 'Your connection is not private' browser warnings that scare away visitors. Learn how to automate SSL expiry tracking.",
        "time": "4 Mins",
        "prereqs": ["HTTPS enabled domain name"],
        "steps": [
            {"title": "Enable SSL Monitoring on Active Monitors", "desc": "In your UptimeRobot dashboard, edit your existing HTTP(s) monitor and check the box for <strong>SSL Certificate Monitoring</strong>."},
            {"title": "Set Expiry Warning Thresholds", "desc": "Configure advance notification thresholds (e.g., alert 30 days, 14 days, and 7 days prior to SSL expiration)."},
            {"title": "Track SSL Chain Health & Protocol Compliance", "desc": "Review SSL diagnostic details including certificate authority, cipher suites, and revocation status."}
        ],
        "tip": "Even if you use auto-renewing certificates like Let's Encrypt, server cron job failures can block renewals. This monitor acts as your ultimate safety net."
    },
    "ping-cron-job-heartbeat-monitoring": {
        "title": "How to Monitor Background Cron Jobs & Database Heartbeats",
        "tool": "UptimeRobot",
        "category": "Uptime & Server Monitoring",
        "headline": "Ensure Silent Background Jobs Run Successfully",
        "intro": "Background tasks like night backups, database syncs, or email queues fail silently without throwing web errors. Learn how to monitor scheduled cron jobs with Heartbeat pings.",
        "time": "5 Mins",
        "prereqs": ["Access to server crontab or scheduled task script"],
        "steps": [
            {"title": "Create a Heartbeat Monitor Endpoint", "desc": "In UptimeRobot, select monitor type <strong>Heartbeat</strong>. Name your monitor (e.g., 'Daily Database Backup Cron')."},
            {"title": "Set Expected Execution Intervals", "desc": "Specify how frequently the job runs (e.g., every 24 hours) plus an allowed grace period (e.g., 15 minutes)."},
            {"title": "Attach Ping URL to Server Script", "desc": "Copy the generated unique HTTP ping URL. Append a `curl` command at the end of your server script so it pings UptimeRobot upon successful completion."}
        ],
        "tip": "If UptimeRobot does not receive a ping within the specified timeframe, it assumes the cron job failed or hung and alerts your team immediately."
    },

    # --- JOIIN GUIDES ---
    "consolidate-xero-quickbooks": {
        "title": "How to Consolidate Multiple Xero & QuickBooks Accounts",
        "tool": "Joiin",
        "category": "Financial Consolidation",
        "headline": "Combining Multi-Company Accounts into One Financial Report",
        "intro": "Trying to combine multiple Xero or QuickBooks company accounts in Excel leads to formula errors and broken links. This guide shows you how to automate group financial reporting in under 10 minutes.",
        "time": "10 Mins",
        "prereqs": ["Admin access to Xero, QuickBooks Online, or Sage", "Active Joiin account or trial subscription"],
        "steps": [
            {"title": "Connect Your Accounting Platforms", "desc": "Sign in to Joiin, navigate to <strong>Companies &rarr; Add Company</strong>, and select Xero, QuickBooks Online, or Sage. Complete single sign-on authorization for each entity."},
            {"title": "Configure Group Business Entities", "desc": "Access the <strong>Companies</strong> dashboard tab and select the checkbox next to each subsidiary or franchise entity to include in combined financial statements."},
            {"title": "Generate & Export Consolidated Statements", "desc": "Navigate to <strong>Reports &rarr; Profit & Loss</strong>. Review side-by-side totals across entities and export a presentation-ready board pack PDF."}
        ],
        "tip": "Create custom Chart of Accounts mapping rules to align non-identical GL account numbers across different subsidiary files automatically."
    },
    "multi-currency-financial-reporting": {
        "title": "Multi-Currency Financial Consolidation Setup Guide",
        "tool": "Joiin",
        "category": "Financial Consolidation",
        "headline": "Combine Foreign Currency Accounts (USD, EUR, GBP, AUD)",
        "intro": "When entities trade in different native currencies, manual FX rate math ruins financial reports. Learn how to translate foreign balances automatically.",
        "time": "8 Mins",
        "prereqs": ["Logins for foreign subsidiary accounting accounts", "Target base presentation currency specified"],
        "steps": [
            {"title": "Select Master Base Currency", "desc": "Open <strong>Workspace Settings</strong> in Joiin and choose your primary target presentation currency (e.g., USD or EUR). All group total columns compile in this currency."},
            {"title": "Automatic Daily FX Rate Synchronization", "desc": "Joiin automatically fetches daily exchange rates from central bank feeds. P&L line items translate using monthly average rates, while Balance Sheet items apply spot closing rates."}
        ],
        "tip": "You can manually override automated exchange rates for specific month-end closing dates if required by internal auditors."
    },
    "intercompany-eliminations-guide": {
        "title": "Automating Intercompany Balance & Loan Eliminations",
        "tool": "Joiin",
        "category": "Financial Consolidation",
        "headline": "Remove Internal Trading & Double-Counted Revenue",
        "intro": "Internal management fees and intercompany loans artificially inflate group income. Here is how to strip out internal trading cleanly.",
        "time": "7 Mins",
        "prereqs": ["Chart of Accounts numbers for internal trading accounts"],
        "steps": [
            {"title": "Tag Intercompany GL Accounts", "desc": "In the Joiin dashboard, navigate to <strong>Eliminations</strong> and select the general ledger accounts used for internal management fees or intercompany loans."},
            {"title": "Apply One-Click Elimination Rules", "desc": "Toggle the <strong>Apply Eliminations</strong> filter on your Profit & Loss or Balance Sheet to deduct internal trading amounts from your grand totals."}
        ],
        "tip": "Joiin flags unposted or asymmetrical intercompany invoices automatically so you can reconcile mismatches before finalizing board packs."
    },
    "automated-board-packs-and-kpi-reports": {
        "title": "How to Build Branded Executive Board Packs in Minutes",
        "tool": "Joiin",
        "category": "Financial Consolidation",
        "headline": "Create Professional PDF Management Packs for Directors",
        "intro": "Stop spending hours copying numbers into PowerPoint. Learn how to generate branded financial presentation decks automatically.",
        "time": "5 Mins",
        "prereqs": ["High-resolution brand logo file (PNG/SVG)"],
        "steps": [
            {"title": "Upload Brand Style Assets", "desc": "Navigate to <strong>Settings &rarr; Branding</strong>. Upload your corporate logo and set custom brand hex colors for tables and headers."},
            {"title": "Compile & Export Report Pack", "desc": "Click <strong>Report Packs &rarr; Create Pack</strong>. Combine Profit & Loss statements, Balance Sheets, and visual KPI widgets into an exportable PDF package."}
        ],
        "tip": "Save finished report layouts as templates to reuse them every month with one-click live data refreshes."
    },

    # --- GEO TARGETLY GUIDES ---
    "geo-redirect-website-visitors-by-country": {
        "title": "How to Automatically Redirect Website Visitors by Country",
        "tool": "Geo Targetly",
        "category": "Website Location & Traffic",
        "headline": "Set Up Location-Based IP Redirection for Websites",
        "intro": "Operating localized websites (e.g., .com for US, .co.uk for UK) manually hurts conversion rates. Learn how to auto-redirect traffic by IP address.",
        "time": "5 Mins",
        "prereqs": ["Admin access to website header code or tag manager"],
        "steps": [
            {"title": "Create Location Rules", "desc": "Inside Geo Targetly, create a new <strong>Geo Redirect</strong> rule (e.g., If visitor IP matches United Kingdom, redirect to /uk-store)."},
            {"title": "Embed Script Tag", "desc": "Copy the provided JavaScript snippet and paste it into the `<head>` tag of your website HTML or tag manager."}
        ],
        "tip": "Set up a 'First Visit Only' redirection rule so returning users can manually switch country versions without getting forced back."
    },
    "auto-currency-switcher-location": {
        "title": "How to Display Local Currency Based on Visitor Location",
        "tool": "Geo Targetly",
        "category": "Website Location & Traffic",
        "headline": "Automate Currency Switchers for Global E-Commerce",
        "intro": "Showing USD prices to European or UK shoppers leads to high cart abandonment. Here is how to automatically display prices in local currency.",
        "time": "6 Mins",
        "prereqs": ["E-Commerce store admin access"],
        "steps": [
            {"title": "Configure Target Currencies", "desc": "Set local target currencies (USD, EUR, GBP, CAD) based on country detection in your Geo Targetly dashboard."},
            {"title": "Activate Automatic Price Conversion", "desc": "Paste the snippet onto product pages to automatically render converted prices based on visitor IP geolocation."}
        ],
        "tip": "Ensure your payment gateway supports multi-currency checkout so customers pay in the exact currency displayed."
    },
    "block-unwanted-country-traffic-website": {
        "title": "How to Block Traffic or Restrict Access by Country",
        "tool": "Geo Targetly",
        "category": "Website Location & Traffic",
        "headline": "Block Specific Countries or Regions from Viewing Your Site",
        "intro": "Prevent fraud, spam, or licensing violations by restricting access from specific geographic locations.",
        "time": "4 Mins",
        "prereqs": ["Target list of blocked or whitelisted countries"],
        "steps": [
            {"title": "Set Blacklist Rules", "desc": "Select the specific geographic regions or countries you wish to block in the Geo Targetly control panel."},
            {"title": "Configure Restriction Response Page", "desc": "Choose whether blocked visitors see a customized access-denied message or get redirected to an external URL."}
        ],
        "tip": "Whitelist search engine bot IP addresses (like Googlebot) so blocking certain countries doesn't harm your SEO index."
    },
    "location-based-popup-banners": {
        "title": "How to Show Location-Specific Popups & Banners",
        "tool": "Geo Targetly",
        "category": "Website Location & Traffic",
        "headline": "Display Targeted Promotions Based on Visitor City or Country",
        "intro": "Increase conversions by showing targeted shipping offers, local events, or localized announcements.",
        "time": "5 Mins",
        "prereqs": ["Banner image or promo copy text"],
        "steps": [
            {"title": "Design Location Banner Widget", "desc": "Customize banner text, button links, and layout rules for target city or country demographics."},
            {"title": "Deploy Embed Code", "desc": "Add the embed script to your site; Geo Targetly automatically filters banner visibility based on visitor location."}
        ],
        "tip": "Use city-level geo targeting to promote localized pop-up events or regional free shipping thresholds."
    },

    # --- AUDIORISTA GUIDES ---
    "convert-articles-audio-app-podcast": {
        "title": "How to Turn Written Content into Audio Apps",
        "tool": "Audiorista",
        "category": "Audio Publishing & Mobile Apps",
        "headline": "Convert Articles & Text into Custom Audio Streams",
        "intro": "Publishers and creators can turn written content into high-quality audio feeds, private podcasts, and branded mobile apps.",
        "time": "6 Mins",
        "prereqs": ["RSS feed URL or blog manuscript files"],
        "steps": [
            {"title": "Import Text Manuscripts or Connect RSS", "desc": "Import text articles directly into Audiorista or connect your website RSS feed for automatic syncing."},
            {"title": "Generate AI Voiceovers or Upload Audio", "desc": "Use high-fidelity AI text-to-speech engines or upload custom recorded MP3 tracks to create your audio stream."}
        ],
        "tip": "Pair AI audio narration with background music beds to create a polished podcast-style listening experience."
    },
    "monetize-audiobooks-private-audio-apps": {
        "title": "How to Sell Audiobooks & Premium Podcasts on Your App",
        "tool": "Audiorista",
        "category": "Audio Publishing & Mobile Apps",
        "headline": "Monetize Audio Content Directly Without Platform Fees",
        "intro": "Avoid massive app store cuts and build a subscription platform for audiobooks and courses.",
        "time": "8 Mins",
        "prereqs": ["Stripe account for direct payments"],
        "steps": [
            {"title": "Organize Audio Chapters & Paywall Rules", "desc": "Upload audio files, arrange content playlists, and set subscription or single-purchase pricing tiers."},
            {"title": "Connect Payment Processing", "desc": "Link your Stripe merchant account to accept direct payments across web, iOS, and Android platforms."}
        ],
        "tip": "Offer a free sample chapter before triggering the paywall to boost conversion rates on paid audiobook courses."
    },
    "publish-white-label-audiobook-app": {
        "title": "How to Build a White-Label Audiobook App",
        "tool": "Audiorista",
        "category": "Audio Publishing & Mobile Apps",
        "headline": "Launch Your Own Branded Audio Streaming App",
        "intro": "Publish an iOS and Android app under your company name without writing custom code.",
        "time": "10 Mins",
        "prereqs": ["Apple Developer & Google Play Developer accounts"],
        "steps": [
            {"title": "Customize App Branding Assets", "desc": "Upload app icons, splash screen artwork, and brand color palettes inside Audiorista."},
            {"title": "Submit App for Publishing", "desc": "Follow the automated wizard to submit your custom-branded app directly to the Apple App Store and Google Play Store."}
        ],
        "tip": "Enable offline download modes so your users can listen to audio content during flights or commutes."
    },
    "branded-audio-app-for-creators": {
        "title": "Branded Audio Platform Setup Guide for Creators",
        "tool": "Audiorista",
        "category": "Audio Publishing & Mobile Apps",
        "headline": "Build Private Podcasts & Paid Audio Communities",
        "intro": "Engage your audience with exclusive audio content, subscriber feeds, and branded mobile apps.",
        "time": "5 Mins",
        "prereqs": ["Existing audience or email list"],
        "steps": [
            {"title": "Configure Subscriber Audio Portal", "desc": "Build exclusive audio playlists and configure access permissions inside Audiorista."},
            {"title": "Distribute Member Invites", "desc": "Share private streaming access links or embed web players into your membership site."}
        ],
        "tip": "Use push notifications inside your branded app to notify listeners instantly when a new episode drops."
    },

    # --- EMAILLISTVERIFY GUIDES ---
    "bulk-verify-email-lists-reduce-bounces": {
        "title": "How to Bulk Verify Email Lists & Reduce Bounce Rates",
        "tool": "EmailListVerify",
        "category": "Email Verification & Deliverability",
        "headline": "Scrub Marketing & Sales Lists Before Campaign Sending",
        "intro": "High email bounce rates ruin domain sender reputation and trigger account suspensions. Here is how to scrub email lists clean before sending.",
        "time": "4 Mins",
        "prereqs": ["CSV or TXT file of email addresses"],
        "steps": [
            {"title": "Upload Email List CSV", "desc": "Sign in to EmailListVerify and click <strong>Verify List &rarr; Upload File</strong>. Select your CSV or TXT file."},
            {"title": "Download Cleaned Contact File", "desc": "The verification engine automatically checks MX records, syntax, and invalid mailboxes. Export the filtered list of 100% valid addresses."}
        ],
        "tip": "Scrub any contact list that hasn't been emailed in over 60 days to purge abandoned or deactivated corporate mailboxes."
    },
    "clean-spam-traps-email-marketing": {
        "title": "How to Identify & Remove Spam Traps from Email Lists",
        "tool": "EmailListVerify",
        "category": "Email Verification & Deliverability",
        "headline": "Protect Sender Reputation by Eliminating Spam Traps",
        "intro": "Spam traps hidden inside purchased or old contact lists will blacklist your domain. Learn how to detect and remove spam trap records.",
        "time": "5 Mins",
        "prereqs": ["Connected email provider or list export file"],
        "steps": [
            {"title": "Run Spam Trap Verification Engine", "desc": "Import your subscriber list into EmailListVerify's automated detection engine."},
            {"title": "Review Risk Classifications", "desc": "Filter out flagged records classified as spam traps, disposable emails, or catch-all accounts before launching your campaign."}
        ],
        "tip": "Never buy unverified cold email lists—always run them through a syntax and MX record verification layer first."
    },
    "real-time-api-email-verification-forms": {
        "title": "How to Validate Email Addresses on Website Forms in Real-Time",
        "tool": "EmailListVerify",
        "category": "Email Verification & Deliverability",
        "headline": "Block Fake Email Signups on Web Forms Automatically",
        "intro": "Stop fake signups and typos from entering your CRM by validating email inputs in real time directly on your signup forms.",
        "time": "6 Mins",
        "prereqs": ["EmailListVerify API Key", "Web form admin access"],
        "steps": [
            {"title": "Generate Real-Time API Key", "desc": "Navigate to <strong>API Settings</strong> in EmailListVerify and generate a dedicated verification API key."},
            {"title": "Connect Web Form Endpoint", "desc": "Paste the JavaScript validation code into your sign-up form to trigger immediate background validation before submission."}
        ],
        "tip": "Prompt users with 'Did you mean @gmail.com?' when a typo like @gmai.com is detected on your forms."
    },
    "prevent-domain-blacklisting-deliverability": {
        "title": "How to Prevent Email Domain Blacklisting & Fix MX Records",
        "tool": "EmailListVerify",
        "category": "Email Verification & Deliverability",
        "headline": "Monitor Domain Blacklists & MX Health Checks",
        "intro": "If your domain hits a spam blacklist, open rates drop to zero. Learn how to run automated blacklist checks and maintain sender health.",
        "time": "5 Mins",
        "prereqs": ["Domain name (e.g., yourcompany.com)"],
        "steps": [
            {"title": "Run Domain & MX Health Audit", "desc": "Enter your sending domain into EmailListVerify's blacklist scanner tool."},
            {"title": "Review Blacklist Status", "desc": "Identify if your IP or domain is listed on global DNS blacklists and execute automated delisting resolution steps."}
        ],
        "tip": "Keep your bounce rate strictly below 2% to ensure major ISPs like Google and Microsoft don't flag your domain."
    },

    # --- ICOMPASS GUIDES ---
    "automated-remote-team-task-management": {
        "title": "How to Automate Task Management for Distributed Remote Teams",
        "tool": "iCompass",
        "category": "Remote Work & Team Management",
        "headline": "Streamline Remote Team Collaboration & Project Tracking",
        "intro": "Managing hybrid or distributed teams without centralized tracking leads to missed deadlines. Here is how to configure remote team task management.",
        "time": "8 Mins",
        "prereqs": ["Admin user account on iCompass"],
        "steps": [
            {"title": "Set Up Team Workspace Directory", "desc": "Log in to iCompass and create team project boards grouped by department or client initiative."},
            {"title": "Assign Directives & Track Milestones", "desc": "Assign individual tasks, attach documentation, and enable real-time status notifications for team members."}
        ],
        "tip": "Set up automated weekly email summaries so executives get progress updates without holding status meetings."
    },
    "time-zone-tracking-distributed-teams": {
        "title": "How to Coordinate Cross-Border Teams Across Time Zones",
        "tool": "iCompass",
        "category": "Remote Work & Team Management",
        "headline": "Manage Time Zone Synchronization for Remote Organizations",
        "intro": "Scheduling meetings across global time zones creates confusion. Learn how to track team availability automatically.",
        "time": "5 Mins",
        "prereqs": ["Team member location roster"],
        "steps": [
            {"title": "Configure Global User Time Zones", "desc": "Set local time zones for each team member profile inside your iCompass unified directory."},
            {"title": "Coordinate Asynchronous Workflows", "desc": "Utilize time-zone tracking calendars to schedule meeting windows and asynchronous task handoffs."}
        ],
        "tip": "Rely on recorded video updates attached to iCompass tasks instead of forcing early or late meeting times."
    },
    "secure-document-sharing-remote-portal": {
        "title": "How to Set Up a Secure Portal for Remote Document Sharing",
        "tool": "iCompass",
        "category": "Remote Work & Team Management",
        "headline": "Centralize Enterprise Documents with Unified SSL Security",
        "intro": "Sending sensitive corporate documents via email creates security vulnerabilities. Learn how to build a secure file-sharing repository.",
        "time": "6 Mins",
        "prereqs": ["Corporate documents & permission group roster"],
        "steps": [
            {"title": "Create Secure Knowledge Base Folders", "desc": "Navigate to the <strong>Portal Software</strong> module and create password-protected document repositories."},
            {"title": "Set SSL Granular Permissions", "desc": "Assign role-based access rights (View, Edit, Admin) to ensure team members only access authorized files."}
        ],
        "tip": "Enable auto-expiring document download links when sharing confidential files with external vendors."
    },
    "employee-activity-performance-monitoring": {
        "title": "How to Monitor Remote Staff Productivity & Time Allocation",
        "tool": "iCompass",
        "category": "Remote Work & Team Management",
        "headline": "Track Remote Employee Productivity & Project Hours",
        "intro": "Gain full visibility into project hours and output across remote teams without micromanaging.",
        "time": "7 Mins",
        "prereqs": ["Active iCompass staff organization structure"],
        "steps": [
            {"title": "Enable Time Tracking & Activity Logging", "desc": "Activate the <strong>Employee Activity Monitoring</strong> feature inside iCompass for active project assignments."},
            {"title": "Analyze Utilization Metrics", "desc": "Generate real-time activity reports to review resource allocation, completed tasks, and operational efficiency."}
        ],
        "tip": "Review weekly time distribution reports to identify overloaded staff members before burnout occurs."
    },

    # --- WARMUP INBOX GUIDES ---
    "warm-up-new-email-domain-cold-outreach": {
        "title": "How to Warm Up a New Email Domain for Cold Outreach",
        "tool": "Warmup Inbox",
        "category": "Email Deliverability & Outreach",
        "headline": "Automate Domain Warmup to Reach Primary Inboxes",
        "intro": "Sending cold outreach from a brand new email domain will land your emails directly in spam folders. Here is how to warm up your inbox automatically.",
        "time": "5 Mins",
        "prereqs": ["Email account with SMTP/IMAP access enabled", "SPF/DKIM DNS records configured"],
        "steps": [
            {"title": "Connect Mailbox via SMTP/IMAP", "desc": "Sign in to Warmup Inbox, click <strong>Add Inbox</strong>, and authenticate your Google Workspace, Outlook, or SMTP account."},
            {"title": "Enable Automated Engagement Network", "desc": "Warmup Inbox connects your account to 30,000+ real inboxes that exchange, open, reply, and rescue your messages from spam automatically."}
        ],
        "tip": "Keep your warmup running in the background even after launching active campaigns to maintain positive engagement signals."
    },
    "fix-cold-emails-going-to-spam": {
        "title": "How to Fix Cold Emails Going to Spam & Improve Placement",
        "tool": "Warmup Inbox",
        "category": "Email Deliverability & Outreach",
        "headline": "Diagnose Deliverability Drop-offs & Rescue Spam Placement",
        "intro": "If your open rates suddenly drop below 20%, your domain is likely hitting spam folders. Learn how to repair sender reputation.",
        "time": "6 Mins",
        "prereqs": ["Warmup Inbox connected account"],
        "steps": [
            {"title": "Run Deliverability & DNS Audit", "desc": "Check your inbox health score inside Warmup Inbox to review SPF, DKIM, and DMARC record status."},
            {"title": "Increase Spam Rescue Activity", "desc": "Set your daily warmup volume to automatically move landed emails out of spam folders and rebuild domain trust."}
        ],
        "tip": "Pause outbound sales sending for 5 days while keeping Warmup Inbox running at max volume if health drops below 70%."
    },
    "blacklist-monitoring-auto-delisting": {
        "title": "How to Set Up Daily Blacklist Monitoring & Auto-Delisting",
        "tool": "Warmup Inbox",
        "category": "Email Deliverability & Outreach",
        "headline": "Monitor 100+ Email Blacklists with Automated Alerts",
        "intro": "Getting listed on a major email blacklist halts all outbound campaigns. Here is how to set up daily monitoring and automated delisting.",
        "time": "4 Mins",
        "prereqs": ["Sending domain IP address"],
        "steps": [
            {"title": "Activate Daily Blacklist Scanner", "desc": "Warmup Inbox automatically scans your sending domain against 100+ global DNS blacklists daily."},
            {"title": "Trigger Automated Delisting Protocols", "desc": "If a listing occurs, follow automated delisting workflows inside the dashboard to clear your domain status."}
        ],
        "tip": "Set up instant SMS alerts for blacklist hits so you can halt automated campaigns before further damage occurs."
    },
    "language-specific-email-warmup-guide": {
        "title": "How to Run Language-Specific Email Warmup for Global Outreach",
        "tool": "Warmup Inbox",
        "category": "Email Deliverability & Outreach",
        "headline": "Warm Up Inboxes in Native Target Market Languages",
        "intro": "Warming up a domain with English messages when targeting European or Asian markets causes spam filters to flag incongruent activity. Here is the fix.",
        "time": "5 Mins",
        "prereqs": ["Pro or Max Warmup Inbox plan"],
        "steps": [
            {"title": "Select Target Campaign Language", "desc": "Inside inbox settings, choose your primary target language (e.g., German, French, Spanish)."},
            {"title": "Run Contextual Warmup Peer Conversations", "desc": "The network generates natural, language-specific email exchanges to establish local ISP sender credibility."}
        ],
        "tip": "Align your warmup language precisely with the language used in your primary outbound sales scripts."
    },

    # --- WOODPECKER GUIDES ---
    "automated-cold-email-drip-campaigns": {
        "title": "How to Set Up Automated Cold Email Drip Campaigns",
        "tool": "Woodpecker",
        "category": "Sales Automation & Cold Outreach",
        "headline": "Launch Personalised Outbound Email Sequences at Scale",
        "intro": "Sending cold emails manually takes hours and lacks automated follow-ups. Learn how to launch multi-stage email campaigns with adaptive sending.",
        "time": "8 Mins",
        "prereqs": ["Woodpecker account", "Prospect CSV list or B2B lead list"],
        "steps": [
            {"title": "Connect Outbound Mailbox", "desc": "Sign in to Woodpecker and link your email account with built-in deliverability monitoring."},
            {"title": "Build Multi-Step Sequence & Condition Triggers", "desc": "Write your initial cold email and set conditional follow-ups (e.g., If no reply after 3 days, send Follow-up B)."},
            {"title": "Import Prospects & Launch", "desc": "Upload your verified lead list and click <strong>Start Campaign</strong> to begin human-like adaptive sending."}
        ],
        "tip": "Use snippet tags like {{FIRST_NAME}} and {{COMPANY}} to personalize every email and increase response rates."
    },
    "linkedin-cold-outreach-automation-guide": {
        "title": "How to Automate LinkedIn & Email Multichannel Outreach",
        "tool": "Woodpecker",
        "category": "Sales Automation & Cold Outreach",
        "headline": "Combine LinkedIn Automation with Cold Email Sequences",
        "intro": "Combining cold email with LinkedIn profile visits and message connection requests dramatically increases meeting booking rates.",
        "time": "10 Mins",
        "prereqs": ["LinkedIn account credentials"],
        "steps": [
            {"title": "Connect LinkedIn Integration", "desc": "Link your LinkedIn account inside Woodpecker's campaign workflow console."},
            {"title": "Add LinkedIn Action Steps to Sequence", "desc": "Insert automated LinkedIn profile visits, connection invites, and direct messages alongside your email steps."}
        ],
        "tip": "Visit a prospect's LinkedIn profile 1 day before sending a cold email to increase name recognition when your message hits their inbox."
    },
    "inbox-rotation-deliverability-cold-email": {
        "title": "How to Set Up Inbox Rotation to Scale Outbound Email",
        "tool": "Woodpecker",
        "category": "Sales Automation & Cold Outreach",
        "headline": "Distribute Campaign Sending Across Multiple Mailboxes",
        "intro": "Sending 500 emails a day from one email account triggers spam filters. Learn how to rotate sending across multiple accounts seamlessly.",
        "time": "7 Mins",
        "prereqs": ["2 or more secondary email accounts"],
        "steps": [
            {"title": "Add Sending Accounts to Rotation Pool", "desc": "In Woodpecker, connect multiple sending domains to your organization account."},
            {"title": "Enable Campaign Inbox Rotation", "desc": "Assign the inbox pool to your active campaign. Woodpecker automatically distributes sending volume evenly across all accounts."}
        ],
        "tip": "Limit daily sending volume to 50 emails per inbox to keep account reputation pristine."
    },
    "b2b-prospect-lead-database-outreach": {
        "title": "How to Find & Export B2B Leads for Cold Email Campaigns",
        "tool": "Woodpecker",
        "category": "Sales Automation & Cold Outreach",
        "headline": "Search B2B Lead Databases & Import Directly to Campaigns",
        "intro": "Finding verified decision-maker email addresses takes hours. Here is how to search a B2B database and populate campaign sequences instantly.",
        "time": "6 Mins",
        "prereqs": ["Target ideal customer profile (ICP) criteria"],
        "steps": [
            {"title": "Search B2B Lead Finder", "desc": "Use Woodpecker's B2B Lead Finder tool to filter contacts by industry, job title, company size, and location."},
            {"title": "Export Verified Leads to Campaign", "desc": "Select target contacts and import them directly into your active cold email campaign with built-in verification."}
        ],
        "tip": "Filter by job title changes in the last 90 days to target newly hired executives eager to implement new tools."
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
        "intro": "Follow this step-by-step technical implementation manual.",
        "time": "5 Mins",
        "prereqs": ["Admin access to platform dashboard"],
        "steps": [
            {"title": "Initialize Configuration", "desc": "Log in to the administration portal and configure settings."},
            {"title": "Verify Deployment Status", "desc": "Run integration diagnostics to confirm live operation."}
        ],
        "tip": "Double-check your credentials before publishing live setups."
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
    .tip-box {{
      background: #fefce8;
      border: 1px solid #fef08a;
      border-radius: 8px;
      padding: 18px 22px;
      margin-top: 30px;
      font-size: 0.95rem;
      color: #713f12;
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

  <div class="tip-box">
    💡 <strong>Pro-Tip & Best Practice:</strong> {cfg.get('tip', 'Follow vendor configuration best practices to ensure continuous uptime and deliverability.')}
  </div>

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
        <h2>🔧 {tool} Manuals</h2>
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
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      max-width: 920px;
      margin: 0 auto;
      padding: 50px 20px;
      color: #0f172a;
      background: #f8fafc;
    }}
    .header {{
      text-align: center;
      margin-bottom: 35px;
    }}
    h1 {{
      font-size: 2.5rem;
      margin: 0 0 10px 0;
      color: #0f172a;
    }}
    p.subtitle {{
      color: #64748b;
      font-size: 1.15rem;
      margin: 0 0 30px 0;
    }}
    .search-box-wrapper {{
      position: relative;
      max-width: 600px;
      margin: 0 auto 40px auto;
    }}
    .search-input {{
      width: 100%;
      padding: 16px 20px;
      font-size: 1.05rem;
      border: 2px solid #e2e8f0;
      border-radius: 10px;
      outline: none;
      box-shadow: 0 4px 12px rgba(0,0,0,0.02);
      transition: all 0.2s ease;
    }}
    .search-input:focus {{
      border-color: #0070f3;
      box-shadow: 0 4px 16px rgba(0, 112, 243, 0.12);
    }}
    .tool-section {{
      margin-bottom: 45px;
    }}
    .tool-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 10px;
      margin-bottom: 20px;
    }}
    .tool-header h2 {{
      font-size: 1.4rem;
      margin: 0;
      color: #0f172a;
    }}
    .tool-count {{
      background: #e2e8f0;
      color: #475569;
      font-weight: 700;
      font-size: 0.8rem;
      padding: 4px 10px;
      border-radius: 999px;
    }}
    .grid {{
      display: grid;
      gap: 16px;
    }}
    .card {{
      background: white;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 20px 24px;
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
      font-size: 1.1rem;
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
    .no-results {{
      display: none;
      text-align: center;
      padding: 40px;
      color: #64748b;
      font-size: 1.1rem;
    }}
  </style>
</head>
<body>

  <div class="header">
    <h1>🛠️ Stack Manuals</h1>
    <p class="subtitle">Searchable step-by-step technical guides, integration manuals, and SaaS tutorials.</p>

    <div class="search-box-wrapper">
      <input type="text" id="manualSearch" class="search-input" placeholder="🔍 Search guides (e.g., 'Xero', 'downtime', 'polls', 'email')..." onkeyup="filterManuals()">
    </div>
  </div>

  <div id="noResults" class="no-results">
    No guides found matching your search. Try searching for "Email", "Polls", or "Downtime".
  </div>

  <div id="sectionsContainer">
    {sections_html}
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
