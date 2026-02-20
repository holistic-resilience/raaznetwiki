---
title: "Browser Security and Tracking Prevention"
tags:
  [
    browser-security,
    privacy,
    fingerprinting,
    firefox-hardening,
    censorship-circumvention,
    web-rtc,
    iran-cybersecurity,
  ]
category: "Device and Application Surveillance"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "Browser Hardening",
    "Digital Fingerprinting",
    "Man-in-the-Middle Attacks",
    "Extensions Security",
  ]
summary: "A comprehensive guide to securing web browsers against Iranian state surveillance, including Firefox hardening, preventing WebRTC leaks, and avoiding malicious domestic certificates."
source: "Raaznet Aggregation"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of browser settings", "Familiarity with extensions"]
estimated_read_time: "15 minutes"
---

# Browser Security and Tracking Prevention

The web browser is your primary gateway to information and your first line of defense against surveillance. The Islamic Republic employs sophisticated methods to intercept, monitor, and manipulate web traffic. This guide focuses on hardening your browser to resist these specific threats, preventing digital tracking, and maintaining access to the free internet.

## The Iranian Threat Landscape

Before configuring your browser, it is critical to understand the specific risks facing users in Iran:

### 1. Man-in-the-Middle (MitM) & Root Certificates

The Iranian government frequently attempts **Man-in-the-Middle attacks** to decrypt secure (HTTPS) traffic. They achieve this by:

- **Fake Root Certificates:** Attempting to issue fraudulent security certificates (e.g., the DigiNotar incident or state-issued CAs).
- **Domestic Browsers:** Promoting local browsers (e.g., **Saina**, **Salam**, or **Zarafa**) which often come pre-installed with government root certificates. **Warning:** Using these browsers allows the state to read your encrypted emails, chats, and search history without any warning signs.

### 2. WebRTC IP Leaks

Standard browsers use **WebRTC** (Web Real-Time Communication) for video and voice calls. However, WebRTC can reveal your **real IP address** even when you are using a VPN. This vulnerability is actively exploited by Iranian state actors to deanonymize users bypassing censorship.

### 3. Browser Fingerprinting

Even if your IP is hidden, you can be tracked via **fingerprinting**. Trackers collect data on your screen resolution, installed fonts, battery level, and browser version to create a unique "fingerprint" of your device. This is used to link your browsing history across different sessions and websites.

---

## Selecting a Secure Browser

### Recommended Browsers

1.  **Mozilla Firefox (Highly Recommended):**
    - **Why:** It is open-source, audited, and offers the most granular control for "hardening" (modifying deep privacy settings). It does not rely on the Chromium engine (controlled by Google).
2.  **Brave Browser:**
    - **Why:** Good out-of-the-box privacy with built-in ad and tracker blocking. Easier for beginners who cannot spend time configuring Firefox.
3.  **Tor Browser:**
    - **Why:** The gold standard for anonymity. It routes traffic through the Tor network and standardizes your fingerprint so you look the same as every other Tor user.
    - _Note:_ Accessing Tor in Iran often requires bridges (e.g., Snowflake).

### Browsers to Avoid

- **All Domestic Iranian Browsers:** Never use browsers developed or promoted by Iranian state entities (e.g., Saina). They are fundamentally compromised.
- **Google Chrome:** While secure against hackers, it is a tracking tool for Google and limits the effectiveness of ad-blockers (Manifest V3 transition).

---

## Hardening Firefox for the Iranian Context

If you use Firefox, you must configure it to close security gaps relevant to Iran.

### 1. Disable WebRTC (Critical for VPN Users)

To prevent your real IP from leaking:

1.  Type `about:config` in the address bar and press Enter.
2.  Accept the risk warning.
3.  Search for `media.peerconnection.enabled`.
4.  Double-click it to set it to **`false`**.

### 2. Enable HTTPS-Only Mode

This forces the browser to use encryption and alerts you if a site (or a government interception portal) tries to downgrade you to HTTP.

- Go to **Settings** > **Privacy & Security**.
- Scroll to bottom: Select **"Enable HTTPS-Only Mode in all windows"**.

### 3. Encrypt DNS Queries (DoH)

To prevent your ISP (e.g., MCI, Irancell) from seeing which websites you visit via DNS requests:

- Go to **Settings** > **Privacy & Security**.
- Scroll down to **DNS over HTTPS**.
- Select **Max Protection**.
- _Note:_ If standard providers (Cloudflare/NextDNS) are blocked, you may need to rely on your VPN’s DNS or search for a functioning custom provider.

### 4. Enhance Tracking Protection

- Go to **Settings** > **Privacy & Security**.
- Set **Enhanced Tracking Protection** to **Strict**.

---

## Essential Privacy Extensions

Keep your extensions to a minimum. Each extension increases your "attack surface" and makes your browser more unique (fingerprintable). Use only trusted, open-source tools.

### 1. uBlock Origin (Content Blocking)

**uBlock Origin** is not just an ad-blocker; it is a wide-spectrum content blocker that neutralizes trackers and malicious scripts.

- **Recommended Settings:**
  - Go to Dashboard (Settings) > **Filter lists**.
  - Enable **"AdGuard URL Tracking Protection"**.
  - Enable regional lists (e.g., "Persian/Iranian" filters if available to block domestic trackers).
- _Note:_ Do not use "uBlock" (the non-Origin version) or "AdBlock Plus". They are less effective and allow "acceptable ads."

### 2. CanvasBlocker (Anti-Fingerprinting)

If you cannot use Tor Browser, this extension helps prevent websites from reading your HTML5 canvas data to fingerprint your device.

- _Alternative:_ Firefox's built-in `privacy.resistFingerprinting` (in `about:config`) is powerful but may break some websites (like maps).

### 3. Snowflake (Circumvention Aid)

If you have a stable uncensored connection, installing the **Snowflake** extension allows you to become a temporary bridge, helping other users in censored regions (like Iran) access the Tor network.

- _Security Note:_ This does not compromise your own privacy; you are merely a conduit for encrypted traffic.

---

## Managing Extensions & Avoiding Malware

Malicious browser extensions are a common vector for spyware. Iranian threat actors have been known to use fake extensions (e.g., fake VPNs or "downloader" tools) to infect targets.

### Safety Checklist

1.  **Audit Regularly:** Periodically review `about:addons`. Remove any extension you do not use or do not remember installing.
2.  **Verify Sources:** Only install extensions from the official Mozilla Add-ons store or Chrome Web Store. Avoid "sideloading" .xpi or .crx files from Telegram channels.
3.  **Check Permissions:** Be wary of extensions that request "Access to your data for all websites" unless absolutely necessary (like uBlock Origin).
4.  **Phishing Awareness:** Developers of popular extensions are sometimes targeted by phishing attacks. If a trusted extension suddenly requires new, invasive permissions after an update, remove it immediately.

---

## Advanced: Using Privacy Frontends

Many popular platforms (YouTube, Reddit, TikTok) require heavy JavaScript and aggressive tracking. Using "Frontends" allows you to view content without running proprietary code or connecting directly to the service's servers. This is highly effective for bypassing some forms of censorship and tracking.

| Platform    | Recommended Frontend            | Privacy Benefit                                                               |
| :---------- | :------------------------------ | :---------------------------------------------------------------------------- |
| **YouTube** | **Invidious** or **Piped**      | Watch videos without Google account tracking or ads. Bypasses some age-gates. |
| **TikTok**  | **ProxiTok**                    | Browse TikTok content without the invasive app or fingerprinting scripts.     |
| **Reddit**  | **Redlib** (formerly Libreddit) | Read threads without account requirements or tracking pixels.                 |

- **Tip:** Use the **LibRedirect** extension to automatically redirect standard links (e.g., `youtube.com`) to these privacy-respecting frontends.

---

## Summary Checklist for Iranian Users

1.  [ ] **Switch to Firefox** (or Tor Browser for high-risk activity).
2.  [ ] **Remove domestic browsers** (Saina, etc.) from all devices.
3.  [ ] **Disable WebRTC** in `about:config` to prevent VPN leaks.
4.  [ ] **Install uBlock Origin** and keep it updated.
5.  [ ] **Enable HTTPS-Only Mode** to detect interception attempts.
6.  [ ] **Use Frontends** for heavy media consumption (YouTube/TikTok).

**Related Topics:** [[VPN Security]] | [[DNS over HTTPS]] | [[Tor Browser and Bridges]]
