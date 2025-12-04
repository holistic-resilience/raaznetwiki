```yaml
---
title: "How the Internet Works and How It Can Be Censored"
tags: [internet-censorship, privacy, digital-rights, network-security, circumvention]
category: "Internet Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Internet Infrastructure", "Censorship Circumvention", "Network Privacy"]
summary: "Explains how internet connections work, methods governments use to block websites, and tools available to bypass censorship."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of web browsers"]
estimated_read_time: "8 minutes"
---
```

# How the Internet Works and How It Can Be Censored

Understanding how the internet functions is essential for recognizing how censorship operates and how to circumvent it. This guide explains the technical foundations of internet connectivity and the methods used to block or filter online content.

## How the Internet Works

The internet is an international public resource composed of computers, phones, servers, routers, and other devices connected to each other. It was designed to continue providing service even if part of the network was destroyed.

> No one person, company, organization, or government runs the internet.
> — [Wikipedia: Internet Governance](https://en.wikipedia.org/wiki/Internet_governance)

However, national and international bodies have some control over internet infrastructure within their jurisdiction. Many countries prevent users from accessing certain websites or online services. Businesses, schools, libraries, and other institutions may use similar filters to restrict access to material they consider harmful or distracting.

You can often bypass these filters by installing software that uses intermediary servers located in other countries to pass content between blocked services and your device.

## Understanding How Blocking Works

Research by organizations like the [Open Observatory of Network Interference (OONI)](https://ooni.org/) and [Reporters Without Borders (RSF)](https://rsf.org/en/recherche?text=censorship) indicates that many countries filter social, political, and "national security" content without publishing lists of what they block. Governments also block VPNs and proxies they are aware of, as well as websites offering circumvention tools.

Article 19 of the Universal Declaration of Human Rights guarantees free access to information. Despite this, the number of countries censoring the internet continues to increase. As censorship spreads, so does access to anti-blocking tools created by activists, programmers, and volunteers with support from various governments and NGOs concerned with free speech.

## Your Internet Connection

When you request a website or use an app, your request and the content you receive travel through multiple network devices:

1. Your device uses a wired, wireless, or mobile data connection to reach your **Internet Service Provider (ISP)**
2. Your ISP assigns an **IP address** to your local network or device
3. Your ISP uses network infrastructure to connect you with the rest of the world
4. The website or service you're accessing has its own IP address from an ISP in its country

### Who Knows What About Your Connection

| Entity | What They Can Know |
|--------|-------------------|
| **Mobile provider** | Precise physical location via cell tower triangulation |
| **ISP** | Building-level location |
| **Internet cafe/library/business** | Which computer you used and when, or your device's local IP address |
| **Government agencies** | Potentially all of the above through their influence |

## How Websites Are Blocked

When viewing a web page, your device:

1. Connects to a **Domain Name Service (DNS)** to look up the IP address associated with the website's domain name (e.g., `securityinabox.org` → `172.105.249.143`)
2. Asks your ISP to send a request to the ISP managing that IP address
3. Receives content from the web server

### Recognizing Blocked Content

You might not always know when you've requested blocked content. Sometimes you'll receive an explanation of why content was censored, but more often you'll see misleading error messages claiming the page couldn't be found or the address was misspelled.

### Assume the Worst

When assessing blocking, assume:

- Blocking is implemented nationally, at the ISP level, **and** on your local network
- DNS lookups **and** content requests are blocked
- Blocklists exist for both domain names and IP addresses
- Unencrypted internet traffic is monitored for keywords
- No indication or reason will be given for blocking

## How Circumvention Tools Work

Tools like VPNs and proxies connect you to an intermediary server in another country, which then accesses blocked content on your behalf. The safest and most effective tools work regardless of the type of block you face.

### Blocking Resistance Techniques

Government agencies or blocking software providers may eventually identify proxy servers and add them to blocklists. Several techniques help maintain access:

| Technique | How It Works |
|-----------|--------------|
| **Hidden proxies** | Distributed to users in ways that prevent censors from finding them all at once |
| **Private proxies** | Limited access makes them harder for authorities to discover and block |
| **Disposable proxies** | Replaced faster than they can be blocked |
| **Obfuscation** | Disguises proxy traffic as normal internet traffic |
| **Domain fronting** | Makes blocking difficult because it would also block popular services like Google |

You can create a private proxy using tools like [Outline](https://securityinabox.org/en/internet-connection/tools/#outline-vpn) or [Algo](https://securityinabox.org/en/internet-connection/tools/#algo-vpn).

## Further Reading

- EFF Surveillance Self-Defense: [How to Understand and Circumvent Network Censorship](https://ssd.eff.org/module/understanding-and-circumventing-network-censorship)
- Security in a Box: [Accessing Blocked Websites](https://securityinabox.org/en/internet-connection/circumvention)
- Security in a Box: [Choosing the Right Circumvention Tool](https://securityinabox.org/en/internet-connection/circumvention)