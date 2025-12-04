---
title: "Privacy-Respecting Search Engines: Alternatives to Google"
tags: [privacy, search-engines, digital-security, anonymity, surveillance-prevention]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Security Researchers]
topics: ["Search Engines", "Online Privacy", "Digital Security"]
summary: "Comprehensive guide to privacy-focused search engines that don't build advertising profiles from your searches."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic internet browsing knowledge"]
estimated_read_time: "8 minutes"
---

# Privacy-Respecting Search Engines

Use a search engine that doesn't build an advertising profile based on your searches. The recommendations below do not collect personally identifying information (PII) based on each service's privacy policy.

> **Note:** Consider using a [VPN](https://www.privacyguides.org/en/vpn/) or [Tor](https://www.privacyguides.org/en/tor/) if your threat model requires hiding your IP address from the search provider.

## Recommended Providers Overview

| Provider | Search Index | Tor Hidden Service | Logging Policy | Country |
| --- | --- | --- | --- | --- |
| **Brave Search** | Independent | ✓ | Anonymized | United States |
| **Startpage** | Google and Bing | ✓ | Anonymized | Netherlands |
| **DuckDuckGo** | Bing | ✓ | Anonymized | United States |
| **Mullvad Leta** | Brave and Google | ✓ | Anonymized | Sweden |

---

## Brave Search

**Brave Search** is developed by Brave and features an independent search index. Notable features include:

- **Discussions**: Highlights conversation-focused results from forum posts
- Default search engine for the Brave Browser
- Tor hidden service available

**Privacy Considerations:**
- If using a Premium account, Brave may correlate search queries with your account
- Disable "Anonymous usage metrics" in settings (enabled by default)

**Links:** [Homepage](https://search.brave.com/) | [Onion Service](https://search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/) | [Privacy Policy](https://search.brave.com/help/privacy-policy)

---

## DuckDuckGo

**DuckDuckGo** is one of the most mainstream private search options. Key features include:

- **Bangs**: Shortcuts to search other sites directly (e.g., `!w` for Wikipedia)
- **Instant answers**: Quick information without clicking through
- Default search engine for Tor Browser
- Available on Apple Safari

**Alternative Versions:**
- JavaScript-free versions available at `/lite` or `/html` endpoints
- Works with Tor hidden address

**Links:** [Homepage](https://duckduckgo.com/) | [Onion Service](https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/) | [Privacy Policy](https://duckduckgo.com/privacy)

---

## Mullvad Leta

**Mullvad Leta** is developed by Mullvad VPN and uses a shared cache system to limit API calls. Characteristics include:

- Currently provides text search results only
- Default search engine for Mullvad Browser
- Useful for users who disable JavaScript
- **Audited** by Assured AB in March 2023 with all issues addressed

**Links:** [Homepage](https://leta.mullvad.net/) | [Onion Service](http://uxngojcovdcyrmwkmkltyy2q7enzzvgv7vlqac64f2vl6hcrrqtlskqd.onion/) | [Privacy Policy](https://leta.mullvad.net/terms-of-service)

---

## Startpage

**Startpage** provides Google search results with privacy protection. Unique features:

- **Anonymous View**: Standardizes user activity to reduce fingerprinting
- Official Tor hidden service available (as of 2024)
- No longer blocks VPN or Tor users

**Ownership Note:** Majority shareholder is System1 (an adtech company), but they maintain a separate privacy policy. Privacy Guides verified their practices in 2020.

> **Caution:** Anonymous View is not a substitute for true anonymity—use Tor Browser for that purpose.

**Links:** [Homepage](https://startpage.com/) | [Onion Service](http://startpagel6srwcjlue4zgq3zevrujfaow726kjytqbbjyrswwmjzcqd.onion/) | [Privacy Policy](https://startpage.com/en/privacy-policy)

---

## Metasearch Engines

### SearXNG

**SearXNG** is an open-source, self-hostable metasearch engine that aggregates results from multiple search engines without storing information itself.

**Important Considerations:**
- Acts as a proxy—your queries still reach the underlying search engines
- When self-hosting, ensure other users share your instance to blend queries
- Public instances have varying privacy policies—always review before use
- Some instances run as Tor hidden services

**Links:** [Homepage](https://searxng.org/) | [Public Instances](https://searx.space/) | [Source Code](https://github.com/searxng/searxng)

---

## Selection Criteria

### Minimum Requirements
- Must not collect PII per their privacy policy
- Must not require account creation

### Best-Case Criteria
- Based on open-source software
- Does not block Tor exit node IP addresses

---

## Logging Details by Provider

| Provider | What They Log | What They Don't Log |
| --- | --- | --- |
| **Brave Search** | Aggregated metrics (OS, user agent) | IP addresses, PII |
| **DuckDuckGo** | Searches (for product improvement) | IP addresses, PII |
| **Mullvad Leta** | Hashed searches in RAM cache (30-day expiry) | PII |
| **Startpage** | OS, user agent, language | IP addresses, search queries, PII |