---
title: "Web Tracking Technologies and Browser Security"
tags:
  [
    browser-security,
    firefox,
    fingerprinting,
    ech,
    doh,
    iran-surveillance,
    ublock-origin,
    manifest-v3,
  ]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, High-Risk Users]
topics:
  [
    "Browser Hardening",
    "Anti-Fingerprinting",
    "Encrypted Client Hello (ECH)",
    "DNS Privacy",
  ]
summary: "A comprehensive guide to securing web browsers against Iranian state surveillance, focusing on the post-2025 browser landscape (Manifest V3), bypassing SNI filtering with ECH, and mitigating advanced tracking."
source: "Raaznet Aggregation (EFF, Mozilla, OONI)"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of software installation",
    "Familiarity with VPN concepts",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-17"
---

# Web Tracking Technologies and Browser Security

The web browser is not just a tool for accessing information; it is the primary battleground between users and state surveillance mechanisms. The Islamic Republic’s _National Information Network_ (NIN/SHOMA) utilizes Deep Packet Inspection (DPI), DNS poisoning, and sophisticated traffic correlation to identify, track, and block users.

This guide details how to harden your browsing experience, protect against modern tracking techniques, and navigate the specific threats posed by Iran's internet architecture in 2026.

## I. The Browser Landscape in 2026: The "Manifest V3" Shift

As of late 2025, a major shift occurred in browser architecture known as **Manifest V3**. This change, pushed by Google, severely limited the capabilities of privacy extensions (like ad-blockers) in Chrome and Chromium-based browsers.

**Implication for Iranian Users:**
Extensions like **uBlock Origin**, which are essential for blocking tracking scripts and government spyware, no longer function at full capacity on Google Chrome. They cannot dynamically filter network requests as effectively as before.

### 🚫 Browsers to Avoid

- **Google Chrome / Microsoft Edge:** Due to Manifest V3 restrictions and heavy telemetry (data reporting to US corporations).
- **Iranian Domestic Browsers:** Browsers promoted by the state (e.g., _Salam_, _Zarafa_, or custom forks) often contain root certificates that allow the government to decrypt your HTTPS traffic. **Never use these.**
- **Opera:** Owned by a Chinese consortium with questionable privacy practices.

### ✅ Recommended Browsers

| Browser                | Best For                          | Notes                                                                                                                                                                                 |
| :--------------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Tor Browser**        | **Anonymity & Circumvention**     | The gold standard. Routes traffic through the Tor network. Essential for high-risk activity. In Iran, you will likely need to configure a **Bridge** (e.g., Snowflake) to connect.    |
| **Mullvad Browser**    | **Privacy & Anti-Fingerprinting** | Based on Firefox. Developed by Tor Project & Mullvad. Provides the anti-fingerprinting protections of Tor _without_ using the Tor network (faster, but requires a trustworthy VPN).   |
| **Firefox (Hardened)** | **Daily Driver**                  | The only major browser engine that still fully supports powerful privacy extensions. Highly customizable.                                                                             |
| **Brave**              | **Ease of Use**                   | Chromium-based but includes built-in blocking (Rust-based) that bypasses Manifest V3 limits. Good for novice users, but disable "Brave Rewards" and crypto features for better OpSec. |

---

## II. Network-Level Defenses: ECH and DNS

The Iranian filtering system has historically relied on inspecting the **SNI (Server Name Indication)**—a part of the connection handshake that reveals which website you are visiting, even if the content is encrypted.

### 1. Encrypted Client Hello (ECH)

**ECH** is the 2026 standard that replaces the older ESNI. It encrypts the SNI, preventing the ISP (and the Telecommunication Infrastructure Company of Iran) from seeing the specific domain you are visiting on a CDN (like Cloudflare).

- **Status:** Enabled by default in Firefox (v119+) and most modern browsers.
- **The Catch:** ECH relies on DNS to fetch encryption keys. If your DNS is unencrypted, the censor can block the ECH lookup.

### 2. DNS over HTTPS (DoH)

To make ECH work and to hide your destination from the ISP, you must encrypt your DNS queries.

- **The Iranian Context:** Standard DoH providers (e.g., `1.1.1.1` or `8.8.8.8`) are frequently blocked by the Great Firewall of Iran.
- **Solution:**
  1.  **Use a Trusted VPN:** A good VPN tunnels _all_ traffic, including DNS, wrapping it in encryption that the ISP cannot parse.
  2.  **Custom DoH:** If not using a VPN, configure "Obfuscated" or less common DoH providers in browser settings.

> **⚠️ Warning:** Never use the "Default" or "Automatic" DNS settings in Iran, as these often default to the ISP's DNS (MCI, Irancell, TCI), which logs every request and redirects banned sites to government landing pages.

---

## III. Digital Fingerprinting and Tracking

Even if you hide your IP address with a VPN, websites (and state actors monitoring traffic) can identify you through **Browser Fingerprinting**.

### How Fingerprinting Works

Scripts collect data points about your device to create a unique ID (Hash):

- **Canvas/WebGL:** How your graphics card renders specific shapes.
- **Audio Context:** Unique variations in your sound hardware.
- **Fonts:** The specific list of fonts installed on your OS.
- **Screen Resolution & Window Size.**

### Countermeasures

1.  **Resist Fingerprinting (RFP):** Firefox has a built-in configuration (`privacy.resistFingerprinting`) that standardizes these values (e.g., reporting a generic window size). Mullvad Browser and Tor Browser enable this by default.
2.  **Do Not Maximize Windows:** Maximizing a browser window reveals your exact screen resolution. Tor Browser warns against this.
3.  **Language Settings:** Stick to English (US) in browser headers if possible. A header requesting `fa-IR` (Persian) while coming from a German VPN IP is a flagging anomaly.

---

## IV. Critical Configuration and Extensions

To secure **Firefox** (or its forks) for the Iranian environment:

### 1. Essential Settings

- **HTTPS-Only Mode:** **Enable** in all windows. This forces the browser to drop any connection that is not encrypted. This prevents "SSL Stripping" attacks used by intermediaries.
- **Enhanced Tracking Protection:** Set to **Strict**.

### 2. Mandatory Extensions

- **uBlock Origin:** _Do not use "AdBlock Plus"._ uBlock Origin is a wide-spectrum content blocker.
  - _Action:_ Go to Settings > Filter lists > Enable "Malware domains" and region-specific lists if available (be careful with Persian lists unless verified, as some may be outdated).
  - _Why:_ It blocks third-party trackers, coin miners, and malicious scripts often injected into insecure HTTP pages.
- **Multi-Account Containers (Firefox):** Allows you to isolate identities. You can log into a Google account in one container and browse news in another, ensuring Google cannot correlate the activities.

### 3. Extensions to Avoid

- **Free VPN Extensions:** Most "Free VPN" extensions in the Chrome/Firefox stores are data harvesting operations.
- **"Do Not Track" requests:** These are voluntary signals that trackers ignore. Do not rely on them.

---

## V. Iran-Specific Threat: The "Fake Root" Attack

The Iranian government has previously attempted to issue fraudulent SSL certificates or force users to install "National" root certificates to access banking or university sites.

**The Danger:** If you install a government root certificate (CA) on your device, the government can perform a **Man-in-the-Middle (MitM)** attack. They can decrypt your HTTPS traffic (including Signal, Gmail, and Telegram Web) without your browser showing a warning.

**Defense Strategy:**

1.  **Never** install a certificate aimed at "improving access" or "banking security" sent via Telegram channels or SMS.
2.  **Verify Certificates:** If a site like Gmail looks suspicious or loads slowly, click the Padlock icon > Connection Secure > More Information. Ensure the "Verified by" field says "Google Trust Services" (or similar reputable CA), not an unknown Iranian entity.
3.  **Separate Browsers:** If you _must_ use a state-issued certificate for university or banking access:
    - Use a completely separate browser (e.g., a portable version of Brave) _only_ for that task.
    - Never log into social media or email on that compromised browser.

---

## VI. Mobile Browsing Considerations

Mobile security is critical as smartphones are the primary access point in Iran.

- **Android:**
  - **Firefox for Android:** Supports **uBlock Origin** (unlike Chrome for Android). This is the recommended mobile browser.
  - **Mull Browser:** A privacy-hardened fork of Firefox for Android available on F-Droid.
- **iOS:**
  - Due to Apple's restrictions, all browsers use the WebKit engine. **Onion Browser** (verified by Tor Project) or **Brave** are decent choices, but they are not as resistant to fingerprinting as desktop versions.

## VII. Post-Browsing Hygiene

- **Sanitizing History:** In high-risk situations (e.g., crossing borders/checkpoints), browser history can be incriminating.
  - Configure Firefox to **"Delete cookies and site data when Firefox is closed"**.
  - Better yet, use **Private/Incognito Mode** for all sensitive research.
- **Downloads:** Be aware that the "Downloads" folder retains files even after the browser history is cleared. Securely delete sensitive PDFs or images immediately after use.

---

**Related Topics:**

- [[Internet_Architecture_and_Censorship_Mechanisms]]
- [[Secure_Data_Transmission_and_IP_Privacy]]
