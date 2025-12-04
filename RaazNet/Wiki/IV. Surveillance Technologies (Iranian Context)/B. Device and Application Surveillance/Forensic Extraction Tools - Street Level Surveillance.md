---
title: "Forensic Extraction Tools"
tags: [forensic-tools, mobile-forensics, phone-extraction, law-enforcement-technology, digital-privacy, cellebrite]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Digital Forensics", "Law Enforcement Technology", "Mobile Device Security", "Privacy Rights"]
summary: "Overview of police forensic tools that extract data from mobile devices, including how they work, privacy threats, and legal considerations."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of mobile device security", "Familiarity with digital privacy concepts"]
estimated_read_time: "8 minutes"
---

# Forensic Extraction Tools

In today's world, we carry a detailed dossier of our lives around with us. Our mobile devices contain our most intimate details, acting as our private messenger, photo album, scheduler, navigator, address book, notebook, and even wallet all in one. Our devices are a window into our souls—making us extremely vulnerable when the information these devices contain is accessed by those we don't trust.

Police can use "forensic tools" to extract information from our devices and create detailed reports on our activities and communications.

## How Forensic Tools Work

To use forensic tools, police generally need physical access to your device. The first step is to unlock it. Security features in mobile devices can help thwart such police intrusion, such as an iOS device's [Secure Enclave](https://en.wikipedia.org/wiki/IOS#Secure_Enclave). But these protections [have sometimes been defeated](https://hipsterpixel.co/2017/02/22/cellebrite-now-able-to-bypass-apple-s-secure-enclave/) by forensic devices.

This can be viewed as an ongoing arms race between vendors building secure devices for users versus vendors building forensic tools for police. It is important for users to practice surveillance self-defense by:

- [Choosing a secure passphrase](https://ssd.eff.org/module/creating-strong-passwords)
- [Not unlocking phones](https://ssd.eff.org/module/attending-protest) when [police pressure them](https://www.eff.org/deeplinks/2021/01/so-called-consent-searches-harm-our-digital-rights) to do so

After police plug your device into their forensic tool, they can extract:

- **Full device image**: The entirety of device contents
- **Selective extraction**: Particular contents such as your entire photo album or a subset of photos
- **Automated searches**: Scanning for particular types of content, such as images containing a unique digital "fingerprint" (sometimes called a "[hash](https://www.eff.org/deeplinks/2019/11/why-adding-client-side-scanning-breaks-end-end-encryption)")

After extraction, forensic tools can be coupled with workstation software to generate reports about device content that are easily read and suitable for submission as evidence in court.

## What Kinds of Data Forensic Tools Collect

Forensic tools collect a wide swath of information from devices, including:

- **Media**: Photo album pictures and videos
- **Communications**: Text files, contacts, private and group conversations (even from encrypted messaging apps such as Signal and WhatsApp)
- **Location data**: Stored location information from map applications
- **Personal information**: Calendar events, browsing history, digital wallets and payment methods
- **Deleted content**: In some cases, advanced physical extraction can recover content that the user thought they "deleted" but was still stored on the device

This provides unprecedented access to your private life for anyone willing and able to retrieve this data.

## How Law Enforcement Uses Forensic Tools

Forensic tools are [widely deployed](https://www.upturn.org/work/mass-extraction/) by law enforcement across multiple contexts:

- Local and federal police departments
- Border enforcement agencies
- Specialized agencies like the US [Fish and Wildlife Service](https://theintercept.com/2022/02/08/cellebrite-phone-hacking-government-agencies/)

While hacking methods are not uncommon to unlock a phone, police may simply [ask you to unlock it](https://www.eff.org/deeplinks/2021/01/so-called-consent-searches-harm-our-digital-rights) to gain access. Once unlocked, device contents can be read manually by the officer or plugged into a forensic extraction tool for comprehensive analysis.

This is why it is important to make it clear that you [do not consent](https://supporters.eff.org/shop/i-do-not-consent-search-device-sticker-3-pack-0) to a [search](https://www.eff.org/issues/know-your-rights) of your device—it likely contains the most intimate details of your life.

Once a report is generated, police can submit it as evidence in court or use it to further investigations. Often data is stored for months or years on workstations, creating risk of data breach or misuse by officers with ill intentions.

## Major Forensic Tool Vendors

### Cellebrite

- **Headquarters**: Israel
- **Customer base**: [2,800 customers](https://theintercept.com/2022/02/08/cellebrite-phone-hacking-government-agencies/) in North America; [7,000 worldwide](https://web.archive.org/web/20230222235107/https://investors.cellebrite.com/static-files/bc824a6b-1e62-4788-93a6-3bcc4a96c716) (as of June 2022)
- **Main product**: [Cellebrite UFED](https://en.wikipedia.org/wiki/Cellebrite_UFED) (Universal Forensics Extraction Device), available at various price points depending on extraction level

### Grayshift

- **Headquarters**: Atlanta, Georgia
- **Focus**: Initially iOS extraction, now expanded to Android devices
- **Main product**: [GrayKey](https://www.forbes.com/sites/thomasbrewster/2018/03/05/apple-iphone-x-graykey-hack/)
  - $15,000 for a 300-use license
  - $30,000 for an unlimited-use license

### Known Security Issues

Both companies have experienced vulnerabilities and security breaches:

- **2018**: Hackers [leaked segments](https://fossbytes.com/graykey-code-leaked-random-2-btc/) of GrayKey code left unsecured at a customer site
- **2021**: Security researcher Moxie Marlinspike [demonstrated a security vulnerability](https://gridinsoft.com/blogs/moxie-marlinspike-demonstrates-cellebrite-tools-vulnerabilities/) in Cellebrite UFED workstation software

## Threats Posed by Forensic Tools

### Privacy Threat

Forensic tools can vacuum and automatically scrutinize all information in our devices, representing a fundamental threat to personal privacy.

### First Amendment Concerns

These tools can expose constitutionally protected activity, including:

- Location data showing attendance at protests
- Communications between reporters and confidential sources
- Social media posts on controversial subjects

Widespread police use of forensic tools can chill and deter people from exercising their First Amendment rights.

### Disparate Impact on Vulnerable Communities

Forensic tools will disproportionately burden people of color, immigrants, and other vulnerable groups. Police already subject these communities to a [disparately large share](https://www.ppic.org/publication/racial-disparities-in-law-enforcement-stops/) of traffic stops, sidewalk stops, and searches during those encounters. Forensic tools become another layer in this discriminatory stack.

### Data Security Risks

Forensic tools increase the reservoirs of data held by law enforcement agencies, which can be:

- Stolen by data thieves
- Misused by rule-breaking officers

## EFF's Work on Forensic Tools

EFF advocates for new legal limits on [so-called "consent" searches](https://www.eff.org/deeplinks/2021/01/so-called-consent-searches-harm-our-digital-rights). After police use this troubling tactic to coerce people into unlocking their devices, they all-too-often use forensic tools to copy and automatically search the data.

The powerful and invasive ability to do forensic imaging of mobile devices is becoming more widespread, increasingly available to even small police departments and sheriff's offices. It is time to rein this power in.

## Additional Resources

- [Digital Forensics Unit (Legal Aid Society)](https://legalaidnyc.org/programs-projects-units/digital-forensics-unit/)
- [Cellebrite asks cops to keep its phone hacking tech 'hush hush' (TechCrunch)](https://techcrunch.com/2023/08/19/cellebrite-asks-cops-to-keep-its-phone-hacking-tech-hush-hush/)
- [EFF Street Level Surveillance - Technologies](https://sls.eff.org/)