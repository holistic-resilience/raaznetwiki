```yaml
---
title: "Privacy-Focused Search Engines: Alternatives to Google"
tags: [privacy, search-engines, digital-security, anonymity, surveillance-capitalism]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Search Engines", "Online Privacy", "Data Protection"]
summary: "Guide to privacy-respecting search engines that don't build advertising profiles from your searches."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic internet browsing knowledge"]
estimated_read_time: "8 minutes"
---

# Privacy-Focused Search Engines

Use a search engine that doesn't build an advertising profile based on your searches. The recommendations below do not collect personally identifying information (PII) based on each service's privacy policy.

> **Note:** There is no guarantee that privacy policies are honored. Consider using a [[VPN]] or [[Tor]] if your threat model requires hiding your IP address from the search provider.

## Recommended Providers Overview

| Provider | Search Index | Tor Hidden Service | Logging | Country |
|----------|-------------|-------------------|---------|---------|
| Brave Search | Independent | ✓ | Anonymized | United States |
| Startpage | Google/Bing | ✓ | Anonymized | Netherlands |
| DuckDuckGo | Bing | ✓ | Anonymized | United States |
| Mullvad Leta | Brave/Google | ✓ | Anonymized | Sweden |

---

## Recommended Search Engines

### Brave Search

A search engine developed by Brave with an independent search index. Notable features include:

- **Discussions**: Highlights conversation-focused results from forum posts
- Default search engine for Brave Browser
- Tor hidden service available

**Privacy Considerations:**
- If logged into a Premium account, Brave may correlate search queries with your account
- Disable "Anonymous usage metrics" in settings (enabled by default)
- Collects aggregated usage metrics (OS, user agent) but not PII
- IP addresses temporarily processed for local results but not retained

**Links:** [Homepage](https://search.brave.com/) | [Onion Service](https://search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/) | [Privacy Policy](https://search.brave.com/help/privacy-policy)

---

### DuckDuckGo

One of the most mainstream private search engine options. Key features:

- **Bangs**: Quick shortcuts to search other sites directly
- **Instant answers**: Quick information without clicking through
- Default search engine for Tor Browser
- Available on Apple Safari browser

**Privacy Considerations:**
- Logs searches for product improvement but not IP addresses or PII
- Offers JavaScript-free versions: `/lite` and `/html` (with reduced features)
- Both versions work with Tor hidden service

**Links:** [Homepage](https://duckduckgo.com/) | [Onion Service](https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/) | [Privacy Policy](https://duckduckgo.com/privacy)

---

### Mullvad Leta

A search engine developed by Mullvad VPN using a shared cache system. Characteristics:

- Currently provides text search results only
- Default search engine for Mullvad Browser
- Works well with JavaScript disabled
- **Security audited** by Assured AB (March 2023) - all issues addressed

**Privacy Considerations:**
- Searches stored hashed with a secret in RAM-based cache
- Cache removed after 30 days or when application restarts
- No PII collected

**Links:** [Homepage](https://leta.mullvad.net/) | [Onion Service](http://uxngojcovdcyrmwkmkltyy2q7enzzvgv7vlqac64f2vl6hcrrqtlskqd.onion/) | [Audit Report](https://assured.se/publications/Assured_Mullvad_Leta_pentest_report_2023.pdf)

---

### Startpage

A private search engine using Google and Bing results. Unique features:

- **Anonymous View**: Standardizes user activity to reduce fingerprinting
- Official Tor hidden service available

**Privacy Considerations:**
- Logs OS, user agent, and language—but not IP addresses or search queries
- Majority shareholder is System1 (adtech company) but operates under separate privacy policy
- No longer blocks VPN or Tor users (as of April 2024)

> **Important:** Anonymous View helps with privacy but should not be relied upon for true anonymity. Use [[Tor Browser]] for anonymity requirements.

**Links:** [Homepage](https://startpage.com/) | [Onion Service](http://startpagel6srwcjlue4zgq3zevrujfaow726kjytqbbjyrswwmjzcqd.onion/) | [Privacy Policy](https://startpage.com/en/privacy-policy)

---

## Metasearch Engines

A metasearch engine aggregates results from multiple search engines without storing information itself.

### SearXNG

An open-source, self-hostable metasearch engine (actively maintained fork of SearX).

**Key Points:**
- Acts as a proxy between you and source search engines
- Your queries are still sent to aggregated search engines
- Can be self-hosted for maximum control

**Self-Hosting Considerations:**
- Ensure other users share your instance so queries blend together
- Be aware of legal implications if others search for illegal content
- Always review the privacy policy of any public instance you use

**Links:** [Homepage](https://searxng.org/) | [Public Instances](https://searx.space/) | [Source Code](https://github.com/searxng/searxng)

---

## Selection Criteria

### Minimum Requirements
- Must not collect PII per privacy policy
- Must not require account creation

### Best-Case Criteria
- Based on open-source software
- Does not block Tor exit node IP addresses

---

## Related Topics

- [[VPN Services]]
- [[Tor Browser]]
- [[Desktop Browsers]]
- [[Mobile Browsers]]
- [[Surveillance Capitalism]]
```