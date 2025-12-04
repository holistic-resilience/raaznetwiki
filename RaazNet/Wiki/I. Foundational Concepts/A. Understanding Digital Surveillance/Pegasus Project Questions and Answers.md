---
title: "Pegasus Project Questions and Answers"
tags: [pegasus, spyware, nso-group, mobile-security, surveillance, zero-day-exploits]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [Journalists, Human Rights Defenders, Activists, Privacy-Conscious Users]
topics: ["Spyware", "Mobile Security", "Government Surveillance", "Digital Forensics"]
summary: "Q&A guide explaining the Pegasus spyware investigation, how the malware works, and protective measures for potential targets."
source: "Security in a Box (Tactical Tech)"
content_type: "Educational Guide"
security_level: "Critical"
language: "English"
prerequisites: ["Basic smartphone usage", "Understanding of malware concepts"]
estimated_read_time: "8 minutes"
author: "Mohammed Al-Maskati"
date_published: 2021-07-23
---

# Pegasus Project Questions and Answers

## Overview

Amnesty International and the media platform Forbidden Stories published an investigation into the use of an Israeli surveillance tool to spy on individuals worldwide. The investigation was called the [Pegasus Project](https://forbiddenstories.org/case/the-pegasus-project/).

## Key Facts

### What is Pegasus?

Pegasus is spyware developed by [NSO Group](https://en.wikipedia.org/wiki/NSO_Group), an Israeli company that claims to sell surveillance tools to governments for targeting criminals.

### How was this discovered?

Forbidden Stories and Amnesty International gained access to a leak of more than 50,000 records of phone numbers targeted by NSO clients.

### Who are the victims?

According to the [documents](https://cdn.occrp.org/projects/project-p/#/), victims include:
- Journalists
- Human rights defenders
- Political activists
- Politicians in various countries and international organizations

### Were all 50,000 people infected?

Not necessarily. While 50,000 phone numbers appeared in the targeting list, Amnesty International's Security Lab performed technical analysis on dozens of phones and confirmed that **at least 67 devices** were infected with the software.

## How Pegasus Works

### Infection Methods

NSO has exploited vulnerabilities in operating systems and applications on both iPhones and Android devices, including:

- **Malicious links**: Sending links to fake websites designed to look legitimate; clicking installs the malware
- **Application vulnerabilities**: Exploiting flaws in apps like [WhatsApp](https://www.theguardian.com/technology/2020/jul/17/us-judge-whatsapp-lawsuit-against-israeli-spyware-firm-nso-can-proceed)
- **iMessage exploits**: Recent attacks have targeted vulnerabilities in Apple's iMessage application

These attacks use [zero-day vulnerabilities](https://en.wikipedia.org/wiki/Zero-day_(computing))—security flaws unknown to developers and therefore unpatched at the time of exploitation.

### Capabilities

Once a device is infected, attackers gain complete access as if they had physical possession of an unlocked phone:

- Read phone and email messages
- View photos
- Eavesdrop on calls
- Track location
- Activate the camera remotely
- Access all applications and information

Pegasus developers continuously improve the software to hide traces, making detection increasingly difficult.

## Detection and Verification

### Can I check if my device is infected?

Pegasus is highly sophisticated and difficult to detect using standard anti-malware programs. If you believe you may be a target, contact a digital security expert for assistance, though results may not be definitive.

### What about Amnesty's detection tool?

Amnesty International released [Mobile Verification Toolkit (MVT)](https://github.com/mvt-project/mvt), a technical method for checking devices. **Important**: This tool is designed for technical experts, not average users.

### Are only iPhone users affected?

No. Both iPhone and Android users have been targeted and infected.

## Protective Measures

### If You Suspect Infection

1. Sign out of all accounts
2. Change passwords for all accounts
3. Enable two-factor authentication on all accounts
4. Stop using the device and disconnect from all internet networks
5. Contact a digital security expert for assistance

### General Protection Practices

- **Keep systems updated**: Immediately update operating systems and all applications when updates become available
- **Periodic factory resets**: Reset your phone periodically to erase potential malware
  - [Android reset instructions](https://support.google.com/android/answer/6088915)
  - [iOS reset instructions](https://support.apple.com/en-us/HT201252)
- **Use official app stores only**: Do not download applications from unofficial sources
- **Use a VPN**: Enable a Virtual Private Network on mobile phones and computers
- **Verify links before clicking**: Use [VirusTotal.com](https://www.virustotal.com/) to check suspicious links
- **Use anti-malware software**: Install reputable security applications
- **Audit installed apps**: Review your phone for unnecessary applications and uninstall or disable them

### Additional Resources

- [Security in a Box: Basic Security for Android](https://securityinabox.org/en/guide/basic-security/android/)
- [Security in a Box: Basic Security for iOS](https://securityinabox.org/en/guide/basic-security/ios/)
- [iOS update instructions](https://support.apple.com/en-gb/guide/iphone/iph3e504502/ios)

## Important Note

While the situation is concerning, worry without action does not improve your security. Use this concern as motivation to develop your digital protection knowledge and strengthen the security of your devices and communications.