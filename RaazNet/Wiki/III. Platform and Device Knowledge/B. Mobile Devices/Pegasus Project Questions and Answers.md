---
title: "Pegasus Project Questions and Answers"
tags: [spyware, pegasus, nso-group, mobile-security, surveillance, malware]
category: "Threat Intelligence"
difficulty: "Intermediate"
audience: [Journalists, Human Rights Defenders, Activists, Privacy-Conscious Users]
topics: ["Spyware", "Mobile Security", "Surveillance", "Digital Self-Defense"]
summary: "Q&A guide explaining the Pegasus spyware investigation, how the malware works, and practical protection steps."
source: "Security in a Box (Front Line Defenders)"
content_type: "Educational Guide"
security_level: "Critical"
language: "English"
prerequisites: ["Basic smartphone usage", "Understanding of apps and operating systems"]
estimated_read_time: "8 minutes"
---

# Pegasus Project Questions and Answers

*By Mohammed Al-Maskati | July 23, 2021*

## What Happened?

Amnesty International and the media platform Forbidden Stories published an investigation into the use of an Israeli surveillance tool to spy on individuals worldwide. The investigation was called the [Pegasus Project](https://forbiddenstories.org/case/the-pegasus-project/).

## How Was This Information Obtained?

Forbidden Stories and Amnesty International gained access to a leak of more than 50,000 records of phone numbers that were targeted by NSO clients.

## Who Is NSO and What Is Pegasus?

[NSO Group](https://en.wikipedia.org/wiki/NSO_Group) is an Israeli company that develops and sells spyware. Pegasus is their flagship surveillance tool. NSO claims to sell these tools exclusively to governments for targeting criminals, though investigations have revealed widespread abuse against civil society.

## Who Are the Victims?

According to the [published documents](https://cdn.occrp.org/projects/project-p/#/), victims include:
- Journalists
- Human rights defenders
- Political activists
- Politicians in various countries and international organizations

## Were All 50,000 Numbers Actually Infected?

Not necessarily. While 50,000 phone numbers appeared in the targeting list, it's impossible to confirm all were successfully compromised. However, the Amnesty International Security Lab performed technical analysis on dozens of phones and confirmed that **at least 67 devices were infected** with Pegasus.

## How Does the Infection Happen?

NSO has exploited vulnerabilities in operating systems and applications on both iPhones and Android devices. Attack methods include:

- **Malicious links**: Sending links to fake websites designed to look legitimate. Clicking these links installs malware on the device.
- **App vulnerabilities**: Exploiting security flaws in apps like [WhatsApp](https://www.theguardian.com/technology/2020/jul/17/us-judge-whatsapp-lawsuit-against-israeli-spyware-firm-nso-can-proceed)
- **Zero-click attacks**: More recently, exploiting vulnerabilities in iMessage that require no user interaction

These attacks often use [zero-day vulnerabilities](https://en.wikipedia.org/wiki/Zero-day_(computing))—security flaws unknown to developers, meaning no fix exists at the time of exploitation.

## What Can Pegasus Do?

When a device is infected with Pegasus, attackers gain complete access—as if you handed your unlocked phone to a stranger. Capabilities include:

- Reading phone and email messages
- Viewing photos
- Eavesdropping on calls
- Tracking location
- Activating the camera to take photos
- Accessing all apps and stored information

Pegasus developers continuously improve the software's ability to hide traces, making detection increasingly difficult.

## Can I Check If My Device Is Infected?

Pegasus is highly sophisticated and difficult to detect using standard anti-malware programs. If you believe you may be a target, contact a digital security expert for assistance, though results may not be definitive.

Amnesty International released the [Mobile Verification Toolkit (MVT)](https://github.com/mvt-project/mvt) for checking devices, but this tool is designed for technical experts, not average users.

## Are Only iPhone Users Affected?

No. Both iPhone and Android users have been targeted and infected.

## Has Apple Fixed These Vulnerabilities?

Apple released iOS version [14.7](https://support.apple.com/en-gb/HT212601) on July 19, 2021, which addressed some serious security vulnerabilities. However, this update did not cover all vulnerabilities being exploited by NSO.

**We strongly recommend updating your device immediately.** See [iOS update instructions](https://support.apple.com/en-gb/guide/iphone/iph3e504502/ios).

## Should I Be Worried?

Concern is natural, but worry without action doesn't improve your security. Channel that concern into motivation to strengthen your digital protection practices.

---

## Practical Protection Steps

### If You Suspect You're Compromised

1. Stop using the device and disconnect from all networks
2. Sign out of all accounts
3. Change passwords for all accounts (from a different, trusted device)
4. Enable two-factor authentication on all accounts
5. Contact a digital security expert for assistance

### Ongoing Protection Practices

- **Keep everything updated**: Install operating system and app updates immediately when available
- **Review basic security guides**: See Security in a Box guides for [Android](https://securityinabox.org/en/guide/basic-security/android/) and [iOS](https://securityinabox.org/en/guide/basic-security/ios/)
- **Factory reset periodically**: Consider resetting your phone from time to time to remove potential malware. See instructions for [Android](https://support.google.com/android/answer/6088915) and [iOS](https://support.apple.com/en-us/HT201252)
- **Use official app stores only**: Never download applications from unofficial sources
- **Use a VPN**: Enable a Virtual Private Network on mobile phones and computers
- **Verify links before clicking**: Use [VirusTotal.com](https://www.virustotal.com/) to check suspicious links
- **Use anti-malware software**: While not foolproof against Pegasus, it helps against other threats
- **Audit your apps**: Remove unnecessary applications; disable those that can't be uninstalled