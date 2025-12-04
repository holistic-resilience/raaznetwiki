---
title: "Pegasus Project Questions and Answers"
tags: [surveillance, spyware, pegasus, nso-group, mobile-security, targeted-attacks]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [Journalists, Human Rights Defenders, Activists, Privacy-Conscious Users]
topics: ["Spyware", "Mobile Security", "Targeted Surveillance", "Digital Self-Defense"]
summary: "Q&A guide explaining the Pegasus spyware investigation, how the malware works, and practical protection steps."
source: "Security in a Box (Front Line Defenders)"
content_type: "Educational Guide"
security_level: "Critical"
language: "English"
prerequisites: ["Basic smartphone usage", "Understanding of malware concepts"]
estimated_read_time: "8 minutes"
author: "Mohammed Al-Maskati"
date_published: "2021-07-23"
---

# Pegasus Project Questions and Answers

## What Happened?

Amnesty International and the media platform Forbidden Stories published an investigation into the use of an Israeli surveillance tool to spy on individuals worldwide. The investigation was called the [Pegasus Project](https://forbiddenstories.org/case/the-pegasus-project/).

## How Was This Information Obtained?

Forbidden Stories and Amnesty International gained access to a leak of more than 50,000 records of phone numbers that were targeted by NSO clients.

## What Is NSO and Pegasus?

[NSO Group](https://en.wikipedia.org/wiki/NSO_Group) is an Israeli company that sells spyware and surveillance tools to governments, claiming the tools are intended to target criminals. **Pegasus** is their flagship spyware product.

## Who Are the Victims?

According to the [investigation documents](https://cdn.occrp.org/projects/project-p/#/), victims include:
- Journalists
- Human rights defenders
- Political activists
- Politicians in various countries and international organizations

## Were All 50,000 Numbers Actually Infected?

Not necessarily. While 50,000 phone numbers appeared in the targeting list, it's impossible to confirm all were successfully compromised. However, the Amnesty International Security Lab performed technical analysis on dozens of phones and confirmed that **at least 67 devices were infected** with Pegasus.

## How Does the Infection Occur?

NSO has exploited vulnerabilities in operating systems and applications on both iPhones and Android devices:

- **Malicious links**: Sending links to fake websites designed to look legitimate. Clicking these links installs the malware.
- **Application exploits**: Vulnerabilities in apps like [WhatsApp](https://www.theguardian.com/technology/2020/jul/17/us-judge-whatsapp-lawsuit-against-israeli-spyware-firm-nso-can-proceed) and iMessage have been exploited.
- **Zero-click attacks**: More recent versions can infect devices without any user interaction.

These attacks often use [zero-day vulnerabilities](https://en.wikipedia.org/wiki/Zero-day_(computing))—security flaws unknown to developers, meaning no fix exists at the time of exploitation.

## What Can Pegasus Do?

When a device is infected with Pegasus, attackers gain complete access—as if you handed your unlocked phone to a stranger. Capabilities include:

- Reading phone and email messages
- Viewing photos
- Eavesdropping on calls
- Tracking location
- Activating the camera to take photos
- Accessing all apps and data

Pegasus developers continuously improve the software to hide traces, making detection increasingly difficult.

## Can I Check If My Device Is Infected?

Pegasus is highly sophisticated and difficult to detect with standard anti-malware programs. 

Amnesty International released the [Mobile Verification Toolkit (MVT)](https://github.com/mvt-project/mvt), but this tool is designed for **technical experts**, not average users.

If you believe you may be a target, contact a digital security expert for assistance. However, results may not be definitive.

## Are Only iPhone Users Affected?

No. Both **iPhone and Android** users have been targeted.

## Has Apple Fixed These Vulnerabilities?

As of the original publication (July 2021), Apple's iOS 14.7 update addressed some serious vulnerabilities but did **not cover the newest exploits** used by NSO.

**Recommendation**: Always update your device immediately when updates become available. See [iOS update instructions](https://support.apple.com/en-gb/guide/iphone/iph3e504502/ios).

---

## Practical Protection Steps

### If You Suspect You're Compromised

1. **Stop using the device** and disconnect from all networks
2. Sign out of all accounts
3. Change passwords for all accounts
4. Enable two-factor authentication on all accounts
5. Contact a digital security expert for assistance

### Ongoing Protection Measures

- **Keep systems updated**: Immediately install operating system and app updates when available
- **Review basic security guides**: See Security in a Box guides for [Android](https://securityinabox.org/en/guide/basic-security/android/) and [iOS](https://securityinabox.org/en/guide/basic-security/ios/)
- **Periodic factory reset**: Consider resetting your phone periodically to remove potential hidden malware ([Android instructions](https://support.google.com/android/answer/6088915) | [iOS instructions](https://support.apple.com/en-us/HT201252))
- **Use official app stores only**: Never download apps from unofficial sources
- **Use a VPN**: Protect your network traffic on mobile and desktop
- **Verify links before clicking**: Use [VirusTotal.com](https://www.virustotal.com/) to check suspicious links
- **Use anti-malware software**: Add an additional layer of protection
- **Audit installed apps**: Remove unnecessary apps; disable those you cannot uninstall

---

## Should I Be Worried?

Concern is understandable, but worry without action doesn't improve your security. Channel that concern into:

- Developing your digital protection knowledge
- Strengthening the security of your devices and communications
- Implementing the practical steps outlined above