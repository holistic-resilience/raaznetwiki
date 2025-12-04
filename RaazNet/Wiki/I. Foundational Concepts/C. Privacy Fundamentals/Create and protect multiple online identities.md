---
title: "Create and Protect Multiple Online Identities"
tags: [privacy, anonymity, identity-management, opsec, digital-security, pseudonymity]
category: "Identity Protection"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, At-Risk Individuals]
topics: ["Online Privacy", "Identity Separation", "Anonymity Tools", "Operational Security"]
summary: "Comprehensive guide to creating, managing, and protecting separate online identities to safeguard privacy and reduce cross-domain risks."
source: "Security in a Box (Tactical Tech)"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of online privacy concepts", "Familiarity with VPNs and Tor"]
estimated_read_time: "25 minutes"
related_topics: ["VPN usage", "Tor Browser", "Email security", "Social media privacy"]
last_updated: "2024-09-09"
---

# Create and Protect Multiple Online Identities

This guide helps you understand why you may want to create alternative online identities and provides methods to secure these identities, making it difficult to connect them to your private life or other online personas.

## Table of Contents

- [[#Develop Your Strategy]]
- [[#Check What Information Already Exists About You Online]]
- [[#Remove Unwanted Information and Old Identities]]
- [[#Map Your Social Domains]]
- [[#Create and Secure an Alternative Identity]]
- [[#Keep Your Identities Separate]]
- [[#Compartmentalize Using Different Devices or Environments]]
- [[#Use Anonymous Payment Methods]]
- [[#Manage Identities in Physical Spaces]]
- [[#Advanced: Create an Anonymous Website]]

---

## Develop Your Strategy

Strategies for maintaining separate identities range from full transparency to complete anonymity. Your choice depends on your risk level, situation, needs, and goals.

### Real Identity

Publishing content under your official name makes sense when your identity provides credibility and trust. Being transparent doesn't mean exposing your entire private life—you can use your legal name for professional contributions while maintaining pseudonymous profiles for personal communications.

**Key principle:** Always apply basic practices to keep your public and private activities separate.

### Persistent Pseudonymity

Using an alternative name consistently over time allows you to:
- Mitigate threats like political or economic retribution
- Build an online reputation under your pseudonym
- Enable trust-based community interactions

You can maintain multiple pseudonyms for different purposes (e.g., activism vs. hobbies). Alternative identities can also be managed collectively, though this requires strong coordination and security practices.

### Anonymity

Complete anonymity involves using short-lived identities to achieve specific goals without leaving traces. This is appropriate for high-risk situations but is difficult to achieve and maintain.

> **Caution:** In some countries, authorities may interpret anonymization efforts as suspicious behavior. Consider alternative approaches when appropriate.

For anonymization tools and strategies, see resources on [[Tor Browser]] and anonymous communications.

### Strategy Comparison

| Strategy | Risk to You | Reputation Building | Effort Required |
|----------|-------------|---------------------|-----------------|
| Real Identity | Higher | Strong | Lower |
| Persistent Pseudonymity | Moderate | Moderate | Moderate |
| Anonymity | Lower | Minimal | Higher |

---

## Check What Information Already Exists About You Online

Before creating alternative identities, research what the internet reveals about you—a practice called "self-doxing."

**Recommended resources:**
- [Access Now Helpline's self-doxing guide](https://guides.accessnow.org/self-doxing.html)
- [New York Times guide to finding and removing personal information](https://open.nytimes.com/how-to-dox-yourself-on-the-internet-d2892b4c5954)

> **Why this matters:** Malicious actors gather information from all available sources to identify targets. Self-doxing helps you discover and remove data before it can be used against you.

---

## Remove Unwanted Information and Old Identities

If you find images, videos, or information that could connect your identities:

1. **Document everything** you want removed (follow the [Digital First Aid Kit documentation guide](https://digitalfirstaid.org/documentation/))
2. **File takedown requests:**
   - Request Google to [remove personal contact information from search results](https://support.google.com/websearch/answer/12719076?hl=en)
   - EU residents can request removal of results containing their name

> **Key insight:** Think of each identity as disposable. Periodically removing old information, pictures, videos, and accounts reduces your attack surface.

---

## Map Your Social Domains

Before creating multiple identities, map your social domains to identify overlaps that could enable cross-domain attacks.

**Process:**
1. List your different activities and networks (online and offline)
2. Assess the sensitivity of each domain
3. Identify intersections between domains
4. Plan which identities you need to separate sensitive activities

> **Why this matters:** We often secure work or activism communications more than casual social interactions. Adversaries exploit these intersections—for example, sending malware disguised as content related to a known hobby. Separating domains prevents these attacks.

---

## Create and Secure an Alternative Identity

### Choose a Name

Select a name that platforms will find credible. Consider that:
- Some platforms (notably Facebook) require "everyday" names
- Using a pseudonym risks account suspension
- Research thoroughly to ensure the name isn't already in use

### Get a Different Phone Number

Phone numbers often link to official identity, making them a weak point. Options include:
- Pre-paid SIM cards (registration requirements vary by country)
- Online services: [Hushed](https://hushed.com/), [Google Voice](https://voice.google.com/about), [Twilio](https://www.twilio.com/en-us/phone-numbers)

### Hide Your IP Address

Prevent your ISP and online platforms from linking identities:
- **VPN:** Hides your IP but requires trusting the provider
- **Tor:** Provides stronger anonymity with no single point of trust

Use IP protection when creating accounts AND when managing them.

### Create a New Email Account

Register a new email address for your alternative identity. Options include:
- New accounts with privacy-focused providers
- Email aliases from your current provider
- Disposable email services (for temporary needs)

Always use IP protection when creating and checking this email.

---

## Keep Your Identities Separate

### Basic Practices

- Use private profiles for personal details, accessible only to selected contacts
- Consider whether shared information could identify or endanger someone
- Ask permission before posting about others; post event details only after events conclude
- Use [[Strong Passwords|strong, unique passwords]] and [[Two-Factor Authentication|two-factor authentication]] for every account
- Learn to [[Reduce Browser Tracking|reduce tracking when browsing]]

### Remove Identifying Information from Files

Delete metadata from images, videos, and documents before uploading. Metadata can reveal:
- Date, time, and location
- Device information
- Other identifying details

### Use Different Accounts and Platforms

Each identity should have:
- Separate social media and messaging accounts
- Different IP addresses, phone numbers, and email addresses
- Distinct registration information

### Maintain True Separation

- Use dedicated devices, browsers, or apps for each persona
- Review privacy settings on all accounts
- Be cautious with profile information, pictures, and cover photos (often publicly visible)
- Create a full character with a distinct story and personality if developing a persona
- **Avoid:**
  - Following your own accounts across identities
  - Having the same contacts follow multiple identities
  - Reposting or liking content between your accounts
- Disable location sharing; verify settings on photo/video platforms
- Remove metadata from all uploaded content
- Consider scheduling posts at different times for different identities

---

## Compartmentalize Using Different Devices or Environments

### Computer Options

| Method | Security Level | Resource Requirements | IP Protection |
|--------|---------------|----------------------|---------------|
| Separate devices | High | High (multiple computers) | No (add VPN/Tor) |
| Tails USB | Very High | Low | Yes (built-in Tor) |
| Qubes OS | Very High | High (system requirements) | Configurable |
| Whonix VM | Very High | Moderate | Yes (built-in Tor) |
| Standard VMs | Moderate | High | No (add VPN/Tor) |
| Sandboxie (Windows) | Moderate | Low | No |
| Separate user accounts | Low | Low | No |
| Different browsers/profiles | Low | Low | No |

**Browser-based options:**
- Use different browsers for different identities
- Create separate browser profiles
- Use containerization extensions:
  - [Firefox Multi-Account Containers](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
  - [SessionBox for Chrome](https://chromewebstore.google.com/detail/sessionbox-multi-login-to/megbklhjamjbcafknkgmokldgolkdfig?hl=en)

### Phone Options

| Method | Security Level | Notes |
|--------|---------------|-------|
| Separate devices | High | Ensure devices receive security updates |
| Different Android accounts | Low | Doesn't protect against device inspection |
| Shelter (Android) | Low-Moderate | Sandboxes work profile; no IP protection |
| Tor Browser (Android) / Onion Browser (iOS) | Moderate | Different IP for browser activities |

> **Why compartmentalization matters:** Separating identities prevents human errors (like responding from the wrong account) and defeats device/browser fingerprinting techniques used to link accounts.

---

## Use Anonymous Payment Methods

For purchases related to pseudonymous identities:
- **Prepaid cards:** Purchase with cash at retail stores
- **Virtual credit cards:** Some banks offer cards that hide your identity from sellers
- **Cryptocurrency:** Provides anonymity but requires technical knowledge to use safely

---

## Manage Identities in Physical Spaces

If your alternative identity involves offline activities:

- Plan how to separate everyday life from your persona's physical activities
- Consider disguises or masks for public appearances
- Only show your face in trusted spaces where photography is prohibited
- Be aware of surveillance (security cameras) on routes to trusted spaces
- Create disposable identities for new acquaintances until trust is established

---

## Advanced: Create an Anonymous Website

To prevent your website from being traced to you:

1. **Check domain privacy options:**
   - Verify your registrar offers privacy protection
   - Note that some top-level domains don't support privacy protection

2. **Use anonymous registration:**
   - [Njalla](https://njal.la/) accepts encrypted requests and cryptocurrency payments
   - Provides registration without revealing your identity to the registrar

> **Important:** Standard WHOIS lookups reveal domain owner information unless privacy protection is enabled. This varies by registrar and domain type.

---

## Additional Resources

- [[Anonymity Tools and Strategies]]
- [[Secure Email Practices]]
- [[Social Media Privacy Settings]]
- [[Metadata Removal Guide]]
- [[VPN Selection Guide]]
- [Gendersec guide on creating credible personas](https://gendersec.tacticaltech.org/wiki/index.php/Step_1#Creating_a_credible_persona)