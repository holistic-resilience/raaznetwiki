```yaml
---
title: "How the Internet Works and How It Can Be Censored"
tags: [internet-censorship, network-infrastructure, circumvention, digital-rights, privacy]
category: "Internet Connection"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Internet Infrastructure", "Censorship", "Circumvention Tools", "Network Security"]
summary: "Explains how internet connections work, methods governments use to block websites, and techniques for bypassing censorship."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of basic networking concepts"]
estimated_read_time: "8 minutes"
---
```

# How the Internet Works and How It Can Be Censored

## Overview

The internet is an international public resource made up of computers, phones, servers, routers, and other devices connected to each other. It was designed to continue providing service even if part of the network was destroyed.

> No one person, company, organization, or government runs the internet.
> — [Wikipedia: Internet Governance](https://en.wikipedia.org/wiki/Internet_governance)

However, national and international bodies have some control over internet infrastructure within their jurisdiction. Many countries prevent users from accessing certain websites or online services. Businesses, schools, libraries, and other institutions may use similar filters to restrict access to material they consider harmful or distracting.

You can often bypass these filters by installing software that uses intermediary servers located in other countries to pass content between blocked services and your device.

## Understanding How Websites Can Be Blocked

Research by organizations like the [Open Observatory of Network Interference (OONI)](https://ooni.org/) and [Reporters Without Borders (RSF)](https://rsf.org/en/recherche?text=censorship) shows that many countries filter social, political, and "national security" content without publishing lists of what they block. Governments also block VPNs and proxies they are aware of, as well as websites offering circumvention tools and instructions.

Article 19 of the Universal Declaration of Human Rights guarantees free access to information. Despite this, the number of countries censoring the internet continues to increase. As this practice spreads, so does access to anti-blocking tools created by activists, programmers, and volunteers with funding from governments, NGOs, and other bodies concerned with free speech.

## Your Internet Connection

When you ask your computer to access a website or your phone to use an app, your request passes through multiple network devices:

1. Your device uses its wired, wireless, or mobile data connection to reach your **Internet Service Provider (ISP)**
2. Your ISP assigns an **IP address** to your local network or device
3. Your ISP uses network infrastructure to connect you with the rest of the world
4. The website or service you're accessing has its own IP address from an ISP in its country

### Who Knows What About Your Connection

| Entity | What They Can Know |
|--------|-------------------|
| **Mobile provider** | Precise physical location via cell tower triangulation |
| **ISP** | Your general location (typically building-level) |
| **Internet cafe/library/business** | Which computer you used or which local IP was assigned to your device |
| **Government agencies** | Potentially all of the above through their authority and influence |

## How Websites Are Blocked

When you view a web page, your device:

1. Connects to a **Domain Name Service (DNS)** to look up the IP address associated with the website's domain name
2. Asks your ISP to send a request to the ISP in charge of that IP address
3. Requests the web server for the website's contents

### Blocking Indicators

You might not always know when you've requested blocked content. You may receive:
- An explanation of why content was censored
- A misleading error message claiming the page couldn't be found
- A message suggesting the address was misspelled

### Assume the Worst

For security purposes, assume:
- Blocking is implemented nationally, at the ISP level, **and** on your local network
- Both DNS lookups and content requests are blocked
- Blocklists exist for both domain names and IP addresses
- Your unencrypted internet traffic is monitored for keywords
- No indication or reason will be given for blocking

The safest and most effective anti-blocking tools should work regardless of the type of block you face.

## How Circumvention Tools Work

Circumvention tools route your traffic through intermediary servers to bypass blocks. However, authorities may eventually identify these servers and add them to blocklists.

### Blocking Resistance Techniques

| Technique | How It Works |
|-----------|--------------|
| **Hidden proxies** | Distributed to users in ways that prevent censors from finding them all at once |
| **Private proxies** | Limited access makes them harder for authorities to discover and block |
| **Disposable proxies** | Replaced faster than they can be blocked |
| **Obfuscation** | Disguises proxy traffic as normal internet traffic |
| **Domain fronting** | Makes blocking difficult because it would also block access to popular services |

You can create a private proxy using tools like [Outline](https://securityinabox.org/en/internet-connection/tools/#outline-vpn) or [Algo](https://securityinabox.org/en/internet-connection/tools/#algo-vpn).

## Further Reading

- EFF Surveillance Self-Defense: [How to Understand and Circumvent Network Censorship](https://ssd.eff.org/module/understanding-and-circumventing-network-censorship)
- Security in a Box: [Accessing Blocked Websites](https://securityinabox.org/en/internet-connection/circumvention)