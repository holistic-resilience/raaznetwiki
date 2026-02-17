---
title: "Advanced Anonymity Networks: Tor, I2P, and Censorship Circumvention"
tags:
  [
    tor,
    i2p,
    anonymity,
    censorship-circumvention,
    bridges,
    snowflake,
    privacy,
    iran,
    internet-freedom,
  ]
category: "Circumvention and Counter-Surveillance"
difficulty: "Advanced"
audience:
  [
    Activists,
    Journalists,
    Human Rights Defenders,
    Users in High-Censorship Regions,
  ]
topics:
  [
    "Tor Network",
    "I2P",
    "Pluggable Transports",
    "Bridges",
    "Anonymous Browsing",
  ]
summary: "A comprehensive guide to using advanced anonymity networks like Tor and I2P to bypass censorship and surveillance in Iran, including configuration of bridges and specialized operating systems."
source: "Raaznet Wiki Aggregation"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites:
  [
    "Basic understanding of internet traffic",
    "Familiarity with VPNs",
    "Ability to install software",
  ]
estimated_read_time: "20 minutes"
last_updated: "2026-02-17"
---

# Advanced Anonymity Networks: Tor, I2P, and Censorship Circumvention

The internet is not just a utility but a battlefield. The "National Information Network" (SHOMA) and the extensive filtering apparatus create a digital environment where surveillance is pervasive and access to information is heavily restricted. While Virtual Private Networks (VPNs) are the most common tool for bypassing censorship, they require you to trust the VPN provider with your traffic.

**Advanced Anonymity Networks** like **Tor** and **I2P** operate differently. They distribute trust across a decentralized network of volunteer-run computers, making it mathematically difficult for any single entity—whether an ISP like MCI or Irancell, or the government itself—to track your online activity or block your access completely.

This guide explores how to effectively utilize these networks to achieve anonymity and circumvent the sophisticated blocking mechanisms deployed in Iran.

---

## The Tor Network (The Onion Router)

Tor is the most robust and widely used anonymity network. It routes your internet traffic through a series of at least three volunteer-operated servers (nodes) around the world.

### How Tor Works

1.  **Entry Node (Guard):** The first server you connect to. It sees your IP address (that you are in Iran) but does not know what website you are visiting.
2.  **Middle Node:** Passes encrypted traffic from the entry to the exit. It knows neither who you are nor where you are going.
3.  **Exit Node:** The final server that connects to the destination website. It sees the website you are visiting but does not know who you are (your IP address).

**Key Benefit:** No single point in the network knows both who you are and what you are doing.

### Accessing Tor in Iran: The Necessity of Bridges

In Iran, direct connections to the public Tor network are often blocked or throttled by the Telecommunication Company of Iran (TCI) and mobile operators. To bypass this, you must use **Bridges**.

**Bridges** are Tor relays that are not listed in the public directory, making them much harder for censors to block.

#### Pluggable Transports (Obfuscation)

Bridges use "Pluggable Transports" to disguise Tor traffic as regular, uninteresting traffic (like a video call or standard HTTPS browsing).

- **obfs4:** Makes Tor traffic look like random, unidentifiable data. This is the standard bridge type but is sometimes detected by advanced Deep Packet Inspection (DPI).
- **Snowflake:** Highly recommended for Iran. It routes your traffic through temporary proxies run by volunteers in free internet countries. It mimics a WebRTC video call, making it very difficult to distinguish from a regular WhatsApp or Skype call.
- **WebTunnel:** A newer transport that mimics HTTPS traffic (WebSockets) to a standard server, designed to blend in with regular web browsing.

**How to Get Bridges:**
If the built-in bridge options are blocked, you can request bridges via:

- **Telegram:** The `@GetBridgesBot` on Telegram.
- **Email:** Send an email to `bridges@torproject.org` from a Gmail or Riseup address with the body "get transport obfs4" (or snowflake).
- **Paskoocheh:** Download Tor Browser with pre-configured bridges or request them through the Paskoocheh app store.

### Tor Browser (Desktop & Android)

The **Tor Browser** (based on Firefox) is the official and most secure way to use Tor. It is pre-configured to protect against **fingerprinting**—a technique used to identify you based on your screen size, fonts, and browser version.

**Security Rules for Tor Browser:**

1.  **Do Not Maximize the Window:** Resizing the window creates a unique fingerprint. Keep it at the default size.
2.  **Do Not Install Extensions:** Additional add-ons (like ad-blockers) make you stand out from other Tor users.
3.  **Use HTTPS Only:** The Exit Node can see your traffic if it is unencrypted (HTTP). Tor Browser attempts to force HTTPS, but always verify the padlock icon.
4.  **Security Levels:** In `Settings > Privacy & Security`, set the Security Level to **Safer** or **Safest**. "Safest" disables JavaScript, which breaks some sites but offers maximum protection against malware and deanonymization attacks.

### Mobile Access: Orbot vs. Onion Browser

- **Orbot (Android):** A proxy app that routes traffic from _other_ apps on your phone through Tor. It acts like a "Tor VPN" for your device. Useful for routing Twitter or Telegram traffic through Tor.
  - _Note:_ Ensure you enable "VPN Mode" in Orbot settings.
- **Onion Browser (iOS):** The recommended browser for iPhone/iPad users. Due to Apple's restrictions (WebKit), it is **not** as secure as the desktop Tor Browser. It cannot fully protect against IP leaks via WebRTC. Use it for reading content, but avoid it for high-risk activities requiring absolute anonymity.

---

## I2P (The Invisible Internet Project)

While Tor is designed to let you access the "clear web" (normal websites) anonymously, **I2P** is designed primarily as a self-contained, anonymous network.

### Key Differences from Tor

- **Garlic Routing:** Encrypts multiple messages together, making traffic analysis harder.
- **Hidden Services Focus:** I2P is optimized for accessing "eepsites" (`.i2p` domains) and peer-to-peer (P2P) services hosted _inside_ the network.
- **Resilience:** It is fully distributed. There are no central directory servers to block, making it theoretically more resilient to the type of centralized filtering seen in Iran.

### When to Use I2P

- **P2P File Sharing:** Unlike Tor, I2P handles torrenting and file sharing well without slowing down the network or compromising anonymity.
- **Internal Communication:** For hosting anonymous blogs or chat services that never touch the public internet.
- **Severe Censorship:** If Tor bridges are entirely blocked, I2P's distributed nature might still function.

**Limitations:** You generally cannot use I2P to browse normal websites (like Google or Instagram) easily. It is an alternative ecosystem, not a gateway to the public web.

---

## Operating Systems for Maximum Anonymity

For high-risk users—such as political activists or journalists holding sensitive documents—software-level protection might not be enough. Specialized Operating Systems offer systemic protection.

### Tails (The Amnesic Incognito Live System)

Tails is a portable OS that you boot from a USB stick.

- **Amnesic:** It forgets everything after you shut it down. No history, passwords, or files are saved to the computer's hard drive.
- **Tor-Forced:** All internet connections are forced through Tor. If Tor fails, the internet cuts off (preventing leaks).
- **Use Case:** Traveling, using internet cafes, or working on compromised computers.

### Whonix

Whonix runs inside Virtual Machines (using VirtualBox or Qubes OS). It consists of two parts:

1.  **Gateway:** Forces all connections through Tor.
2.  **Workstation:** Where you browse and work.

- **Isolation:** Even if malware infects the Workstation, it cannot find your real IP address because the Workstation _only_ knows how to talk to the Gateway.

---

## Advanced Configurations and Risks

### VPN + Tor: A Layered Defense?

In Iran, ISPs actively monitor for Tor traffic patterns. While bridges obfuscate this, adding a VPN can provide a "hiding in the crowd" effect.

**Recommended Setup: You -> VPN -> Tor -> Internet**

1.  Connect to a trusted, secure VPN (e.g., Mullvad, Proton VPN, IVPN).
2.  Open Tor Browser.

- **Pros:** Your ISP (e.g., Irancell) only sees encrypted VPN traffic, not Tor traffic. The Tor entry node sees the VPN's IP, not your home IP.
- **Cons:** You must trust the VPN provider. If the VPN logs data, they know you are using Tor.

**Avoid: You -> Tor -> VPN**
This configuration is complex, rarely offers security benefits, and often harms anonymity by creating a permanent exit point for your traffic.

### Risks Specific to the Iranian Context

1.  **Fake Tor Apps:** Many apps on third-party stores or Telegram channels claim to be "Tor" or "Anti-Filter" tools but are actually malware or government honeypots. **Only download from official sources (Tor Project website, Google Play, F-Droid) or trusted distributors like Paskoocheh.**
2.  **Exit Node Surveillance:** Tor Exit nodes are run by volunteers. Malicious exit nodes can monitor traffic. **Never** log into accounts (email, banking) over Tor unless the website uses **HTTPS** (the padlock icon). Without HTTPS, the exit node can steal your passwords.
3.  **Global Traffic Analysis:** While difficult, powerful adversaries could theoretically correlate traffic entering and leaving the Tor network. This is less of a concern for bypassing local censorship but relevant for high-level espionage.

---

## Summary Checklist for Iranian Users

1.  **Download Securely:** Get Tor Browser via Paskoocheh or an official mirror if the main site is blocked.
2.  **Configure Bridges:** Do not try to connect directly. Use **Snowflake** first; if that fails, request **obfs4** bridges via Telegram or email.
3.  **No Modifications:** Do not add extensions or change window size in Tor Browser.
4.  **HTTPS Only:** Ensure you are using encrypted connections for any login activity.
5.  **Mobile Use:** Use **Orbot** (Android) with VPN mode enabled for routing apps, or **Onion Browser** (iOS) for basic browsing.
