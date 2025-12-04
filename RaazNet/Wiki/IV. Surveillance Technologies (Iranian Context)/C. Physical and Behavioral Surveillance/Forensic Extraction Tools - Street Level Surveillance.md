---
title: "Forensic Extraction Tools"
tags: [forensic-tools, mobile-security, law-enforcement, digital-privacy, surveillance-technology, device-extraction]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Digital Security", "Law Enforcement Surveillance", "Mobile Device Privacy", "Civil Liberties"]
summary: "EFF guide explaining how police use forensic extraction tools to access mobile device data, the privacy threats they pose, and how to protect yourself."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of mobile devices", "Awareness of digital privacy concepts"]
estimated_read_time: "8 minutes"
---

# Forensic Extraction Tools

In today's world, we carry a detailed dossier of our lives around with us. Our mobile devices contain our most intimate details, acting as our private messenger, photo album, scheduler, navigator, address book, notebook, and even wallet all in one. Our devices are a window into our souls—making us extremely vulnerable when the information they contain is accessed by those we don't trust.

Police can use "forensic tools" to extract information from our devices and create a detailed report on our activities and communications.

## How Forensic Tools Work

To use forensic tools, police generally need physical access to your device. The first step is to unlock it. Security features in our mobile devices can help thwart such police intrusion, such as an iOS device's [Secure Enclave](https://en.wikipedia.org/wiki/IOS#Secure_Enclave). But these protections [have sometimes been defeated](https://hipsterpixel.co/2017/02/22/cellebrite-now-able-to-bypass-apple-s-secure-enclave/) by forensic devices.

This can be viewed as an ongoing arms race between vendors building secure devices for users versus vendors building forensic tools for police. It is important for users to practice surveillance self-defense by:

- [Choosing a secure passphrase](https://ssd.eff.org/module/creating-strong-passwords)
- [Not unlocking phones](https://ssd.eff.org/module/attending-protest) when [police pressure them](https://www.eff.org/deeplinks/2021/01/so-called-consent-searches-harm-our-digital-rights) to do so

After police plug your device into their forensic tool, they can extract either:
- The entirety of the device contents (sometimes called an "image" of your device)
- Particular contents such as your entire photo album or a subset of photos

Police might also use a forensic tool to automatically search a user's device for particular types of content, such as all images that contain a unique digital "fingerprint" (sometimes called a "[hash](https://www.eff.org/deeplinks/2019/11/why-adding-client-side-scanning-breaks-end-end-encryption)").

After extraction, a forensic tool can be coupled with other law enforcement technology, such as a workstation linked by software. Police can generate reports about a device's content that are easily read and suitable for submission as evidence in court.

## What Data Forensic Tools Collect

Forensic tools collect a wide swath of information from your devices, including:

- **Photos and videos** from your photo album
- **Text files** and documents
- **Contacts** and address book entries
- **Private and group conversations** (even from encrypted messaging apps such as Signal and WhatsApp)
- **Location data** (e.g., from map applications)
- **Calendar events**
- **Browsing history**
- **Digital wallets and payment methods**

In some cases, an advanced physical extraction of the device can recover content that the user thought they "deleted," but was really still stored on the device. This provides unprecedented access to your private life for anyone willing and able to retrieve this data.

## How Law Enforcement Uses Forensic Tools

Forensic tools are [widely deployed](https://www.upturn.org/work/mass-extraction/) by law enforcement across multiple agencies:

- Local police departments
- Federal agencies
- Border control
- Even specialized agencies like the US [Fish and Wildlife Service](https://theintercept.com/2022/02/08/cellebrite-phone-hacking-government-agencies/)

While hacking methods are not uncommon to unlock a phone, police may simply [ask you to unlock it](https://www.eff.org/deeplinks/2021/01/so-called-consent-searches-harm-our-digital-rights) to gain access. Once unlocked, the contents of your phone can be read by the officer manually, or the device can be plugged into a forensic extraction tool for comprehensive analysis.

**This is why it is important to make it clear that you [do not consent](https://supporters.eff.org/shop/i-do-not-consent-search-device-sticker-3-pack-0) to a [search](https://www.eff.org/issues/know-your-rights) of your device.**

Once a report is generated of the device contents, police can submit it as evidence in court or use it to further their investigations. Often it is stored for months or years on a workstation, creating risk of data breach or misuse by an officer with ill intentions.

## Major Forensic Tool Vendors

### Cellebrite

- **Headquarters**: Israel
- **Customer base**: 2,800 customers in North America; approximately 7,000 worldwide (as of June 2022)
- **Main product**: [Cellebrite UFED](https://en.wikipedia.org/wiki/Cellebrite_UFED) (Universal Forensics Extraction Device)
- **Pricing**: Various price points depending on extraction level desired

### Grayshift

- **Headquarters**: Atlanta, Georgia
- **Initial focus**: iOS extraction (now includes Android devices)
- **Main product**: [GrayKey](https://www.forbes.com/sites/thomasbrewster/2018/03/05/apple-iphone-x-graykey-hack/)
- **Pricing**: $15,000 for a 300-use license; $30,000 for unlimited-use license

### Security Concerns with These Tools

Both companies have experienced vulnerabilities and security breaches:

- **2018**: Hackers [leaked segments](https://fossbytes.com/graykey-code-leaked-random-2-btc/) of GrayKey code left unsecured at a customer site
- **2021**: Security researcher Moxie Marlinspike [demonstrated a security vulnerability](https://gridinsoft.com/blogs/moxie-marlinspike-demonstrates-cellebrite-tools-vulnerabilities/) in Cellebrite UFED workstation software

The powerful and invasive ability to do forensic imaging of mobile devices is becoming more widespread, increasingly available to even small police departments and sheriff's offices.

## Threats Posed by Forensic Tools

### 1. Privacy Violations
Forensic tools can vacuum and automatically scrutinize all of the information in our devices, exposing our most intimate details.

### 2. First Amendment Concerns
These tools can expose protected activities including:
- Location data showing attendance at protests
- Communications between reporters and confidential sources
- Social media posts on controversial subjects

Widespread police use of forensic tools can chill and deter people from exercising their First Amendment rights.

### 3. Discriminatory Impact
Forensic tools will disparately burden people of color, immigrants, and other vulnerable groups. Police unfairly subject them to a [disparately large share](https://www.ppic.org/publication/racial-disparities-in-law-enforcement-stops/) of traffic stops, sidewalk stops, and searches during those encounters. Forensic tools become the newest layer of this discriminatory stack.

### 4. Data Security Risks
Forensic tools increase the reservoirs of data held by law enforcement agencies, which can be:
- Stolen by data thieves
- Misused by rule-breaking officers

## Protecting Yourself

- **Use strong passcodes**: Choose a secure passphrase rather than simple PINs
- **Know your rights**: Understand that you can refuse consent to device searches
- **Don't unlock voluntarily**: Police may pressure you, but you generally don't have to comply
- **Stay informed**: Keep up with evolving device security features

## EFF's Work on Forensic Tools

EFF advocates for new legal limits on [so-called "consent" searches](https://www.eff.org/deeplinks/2021/01/so-called-consent-searches-harm-our-digital-rights). After police use this troubling tactic to coerce people into unlocking their devices, police all-too-often use forensic tools to copy and automatically search the data in these devices.

## Additional Resources

- [Digital Forensics Unit (Legal Aid Society)](https://legalaidnyc.org/programs-projects-units/digital-forensics-unit/)
- [Cellebrite asks cops to keep its phone hacking tech 'hush hush' (TechCrunch)](https://techcrunch.com/2023/08/19/cellebrite-asks-cops-to-keep-its-phone-hacking-tech-hush-hush/)
- [Mass Extraction Report (Upturn)](https://www.upturn.org/work/mass-extraction/)
- [Know Your Rights (EFF)](https://www.eff.org/issues/know-your-rights)