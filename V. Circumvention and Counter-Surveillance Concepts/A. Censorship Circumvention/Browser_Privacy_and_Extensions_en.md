---
title: "Browser Privacy and Extensions"
tags:
  [
    privacy,
    browser-security,
    ublock-origin,
    firefox,
    webrtc,
    fingerprinting,
    iran-context,
  ]
category: "Circumvent and Counter-Surveil"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists]
topics:
  ["Browser Hardening", "Content Blocking", "Anti-Fingerprinting", "WebRTC"]
summary: "Guide to hardening web browsers against surveillance and tracking, with a focus on essential extensions like uBlock Origin and critical configurations for the Iranian context."
source: "Raaznet Aggregated Resources"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites: ["Basic browser usage", "Understanding of extensions"]
estimated_read_time: "10 minutes"
---

# Browser Privacy and Extensions

Your web browser is your primary window to the internet and a major target for surveillance. For users in Iran, the threat is twofold: global commercial tracking (surveillance capitalism) and state-level monitoring (censorship and identification).

This guide focuses on **hardening** your browser to minimize data leaks and maximize privacy without breaking the functionality you need.

> [!WARNING] **The Principle of Minimalism**
> Every extension you install increases your "attack surface" (more code that can be hacked) and makes your browser more unique ("fingerprinting"). **Only install extensions you strictly need.** If a browser setting can achieve the same goal (e.g., HTTPS-Only Mode), use the setting instead of an extension.

---

## Browser Selection

For privacy-conscious users in Iran, **Mozilla Firefox** is the recommended browser.

- **Why Firefox?** It allows deep configuration (via `about:config`) to disable risky features like WebRTC without relying on third-party extensions. It also fully supports powerful ad-blockers like uBlock Origin, unlike Chrome's new "Manifest V3" standard which limits them.
- **Chromium Browsers (Chrome, Edge, Brave):** If you must use these, Brave is the most private out-of-the-box, but Firefox remains the gold standard for customization.

---

## Critical Configurations (Do This First)

Before installing extensions, configure these built-in settings to close major security gaps.

### 1. Disable WebRTC (Mandatory for VPN Users)

**WebRTC** is a protocol for audio/video calls in the browser. It is notorious for leaking your **real IP address** even when you are using a VPN. In the Iranian context, this leak can reveal your identity to the ISP or website.

- **Firefox:**
  1.  Type `about:config` in the address bar and press Enter.
  2.  Click "Accept the Risk and Continue".
  3.  Search for: `media.peerconnection.enabled`
  4.  Double-click it to set it to **`false`**.
- **Chrome/Edge:** You cannot fully disable WebRTC in the settings. You **must** use an extension (see below) or use a browser like Brave which has a toggle in Settings > Privacy.

### 2. HTTPS-Only Mode

Unencrypted HTTP traffic allows Iranian ISPs to see exactly which pages you are visiting and inject censorship or malware.

- **Firefox:** Settings > Privacy & Security > Scroll to bottom > Select **"Enable HTTPS-Only Mode in all windows"**.
- **Chrome:** Settings > Privacy and security > Security > Toggle **"Always use secure connections"**.

### 3. Encrypted DNS (DoH)

DNS-over-HTTPS (DoH) encrypts your DNS requests, preventing the ISP from seeing which domains you are looking up.

- **The Iranian Context:** Many standard DoH providers (Cloudflare, Google) are frequently blocked or tampered with by Iranian firewalls.
  - **Recommendation:** Enable it, but if you experience connection failures, try switching providers (e.g., NextDNS) or rely on your trusted VPN's DNS instead.
  - **Firefox:** Settings > Privacy & Security > DNS over HTTPS > Max Protection.

---

## Essential Extensions

### uBlock Origin

**uBlock Origin** is not just an ad-blocker; it is a "wide-spectrum content blocker" essential for security. It blocks trackers, malware domains, and scripts that slow down your connection.

- **Installation:** [Firefox Add-ons](https://addons.mozilla.org/firefox/addon/ublock-origin/) | [Chrome Web Store](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
- **Configuration for Iran:**
  1.  Click the uBlock icon > Open the Dashboard (Gears icon).
  2.  Go to the **Filter lists** tab.
  3.  Expand **"Regions, languages"**.
  4.  Check **"PER: PersianBlocker"** or **"IRN: Adblock-Iran"** (if available). This blocks ads and trackers specific to Iranian websites.
  5.  Click **"Apply changes"** and **"Update now"**.

> [!TIP] **uBlock Origin Lite (for Chrome Users)**
> If you are using Google Chrome, you may be forced to use "uBlock Origin Lite" due to recent changes (Manifest V3). It is less powerful but still better than nothing. For maximum protection, switch to Firefox.

### WebRTC Control (Chrome Only)

If you use Chrome and cannot switch to Firefox, you need this extension to prevent IP leaks.

- **Action:** Install **WebRTC Control** or **WebRTC Leak Prevent**. Ensure the icon indicates that WebRTC is "Blocked".
- **Verify:** Visit [browserleaks.com/webrtc](https://browserleaks.com/webrtc) with your VPN on. If you see your real Iranian IP, you are not safe.

---

## Extensions to AVOID

- **"Free" VPN Extensions:** Most free VPN extensions (e.g., "Hola", generic "Unblock Iran" tools) are data-mining operations. They often log your traffic and sell it, or they have weak encryption that DPI (Deep Packet Inspection) can easily penetrate.
- **Unverified "Anti-Censorship" Tools:** Be cautious of extensions claiming to "Unblock Everything" unless they are open-source and widely audited (like Snowflake or Ceno). Malicious extensions can act as a "Man-in-the-Middle," stealing passwords and data.
- **Redundant Blockers:** Do not install AdBlock Plus _and_ uBlock Origin. They conflict and slow down your browser.

---

## Advanced Concept: Browser Fingerprinting

Websites and trackers can identify you not just by cookies, but by your "fingerprint"—the unique combination of your screen resolution, installed fonts, browser version, and **extensions**.

- **The Risk:** The more extensions you install, the more unique your fingerprint becomes. A user with a standard Firefox setup is one of millions. A user with Firefox + 15 specific extensions is likely the _only_ one, making you easy to track across the web even without cookies.
- **Mitigation:**
  - Stick to the "Essential" list above.
  - Use **Tor Browser** for high-risk activities. Tor Browser standardizes this fingerprint (e.g., same window size, same fonts) for all users.
  - **Do not maximize** the Tor Browser window, as your screen size is a key fingerprinting metric.

---

## Mobile Privacy

Mobile browsers are often more limited in their privacy capabilities.

- **Android:**
  - **Firefox for Android:** Supports **uBlock Origin** as an add-on. This is the best option for privacy on Android.
  - **Mull Browser:** A hardened version of Firefox for Android (available on F-Droid), recommended for advanced users.
- **iOS (iPhone/iPad):**
  - Apple restricts all browsers to use the WebKit engine, meaning Firefox on iOS is essentially a "skin" over Safari.
  - **AdGuard for iOS:** Since extensions are limited, use the AdGuard app to block ads and trackers in Safari.
  - **Onion Browser:** The recommended way to access the Tor network on iOS.

---

## Summary Recommendations

| Platform             | Browser         | Essential Add-ons               | Critical Settings                                                        |
| :------------------- | :-------------- | :------------------------------ | :----------------------------------------------------------------------- |
| **Desktop (PC/Mac)** | **Firefox**     | uBlock Origin                   | `media.peerconnection.enabled = false` (About:Config)<br>HTTPS-Only Mode |
| **Android**          | **Firefox**     | uBlock Origin                   | HTTPS-Only Mode                                                          |
| **iOS**              | **Safari**      | AdGuard (App)                   | Disable JavaScript (if high threat)<br>iCloud Private Relay (if trusted) |
| **High Anonymity**   | **Tor Browser** | _None (Do not install add-ons)_ | Use "Safest" Security Level                                              |
