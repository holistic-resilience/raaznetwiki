---
title: "Internet Privacy: Browsers, VPNs, and Tor"
tags:
  [
    internet-privacy,
    browsers,
    vpn,
    tor,
    censorship-circumvention,
    digital-security,
    iran,
    opsec,
  ]
category: "Operational Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  ["Browser Security", "VPN Selection", "Censorship Circumvention", "Anonymity"]
summary: "A comprehensive guide to securing your web browsing, selecting trustworthy VPNs, and using Tor to bypass censorship and surveillance in the Iranian context."
source: "Raaznet Wiki Aggregation"
content_type: "Guide"
security_level: "Basic"
language: "English"
prerequisites:
  ["Basic understanding of internet usage", "Ability to install software"]
estimated_read_time: "15 minutes"
---

# Internet Privacy: Browsers, VPNs, and Tor

For Iranian users, the internet is a contested space. The state apparatus employs extensive filtering, surveillance, and traffic analysis mechanisms. Securing your web traffic is not just about avoiding targeted ads; it is about protecting your identity, accessing unrestricted information, and communicating safely. This guide covers the essential tools for internet privacy: secure web browsers, Virtual Private Networks (VPNs), and the Tor network.

## 1. Secure Web Browsers

Your web browser is your primary window to the internet. Default browsers like Google Chrome, Microsoft Edge, or Safari are often designed to collect user data for advertising purposes or lack strict privacy configurations out of the box.

### Why Avoid Standard Browsers?

- **Tracking:** Browsers like Chrome are tied to advertising ecosystems (Google), collecting vast amounts of data about your browsing habits.
- **Lack of Privacy Controls:** Default settings often permit third-party cookies and trackers.
- **Closed Source (Edge/Safari):** You cannot verify the code for potential backdoors or vulnerabilities.

### Recommended Browsers

#### **Mozilla Firefox (Hardened)**

Firefox is open-source and highly customizable. It is currently one of the best options for privacy when configured correctly.

- **Pros:** Open-source, non-profit backer (Mozilla), extensive extension support, "Multi-Account Containers" to isolate sites (e.g., keeping Facebook tracking separate from your work).
- **Configuration:**
  - Set **Enhanced Tracking Protection** to "Strict".
  - Enable **HTTPS-Only Mode** to force encrypted connections.
  - Change the default search engine to **DuckDuckGo** or **Startpage**.
  - Disable "Telemetry" and "Studies" in settings to stop sending usage data to Mozilla.

#### **Brave Browser**

Brave is a Chromium-based browser that blocks ads and trackers by default.

- **Pros:** Works like Chrome but with better privacy, built-in Tor window (though standalone Tor Browser is safer), fast.
- **Cons:** Cryptocurrency features can be bloatware (can be disabled).
- **Configuration:**
  - Go to `Settings > Shields` and set Trackers & Ads blocking to "Aggressive".
  - Enable "Upgrade connections to HTTPS".
  - Disable "Brave Rewards" and crypto wallet features if not used to reduce attack surface.

#### **Tor Browser**

(See the [Tor Network](#3-the-tor-network-and-anonymity) section below for details). This is the gold standard for anonymity.

### Essential Browser Extensions

Extensions can introduce risks, but a few open-source ones are essential for security.

1.  **uBlock Origin:** The most efficient ad and tracker blocker. It protects against "malvertising" (malicious ads) and reduces data usage.
    - _Warning:_ Do not confuse with "uBlock". Use **uBlock Origin** by Raymond Hill.
2.  **Privacy Badger:** Automatically learns to block invisible trackers.
3.  **HTTPS Everywhere:** _Note: Modern browsers now have "HTTPS-Only" mode built-in. If your browser has this feature, enable it instead of installing this extension._

### Browser Hygiene

- **Update Regularly:** Outdated browsers are the easiest target for malware. Enable automatic updates.
- **Manage Cookies:** Configure your browser to delete cookies when you close it (or use an extension like Cookie AutoDelete).
- **Do Not Save Passwords:** Browsers are not secure vaults. Use a dedicated [Password Manager](../../technical-foundations/authentication-and-access-control/secure-password-storage-and-managers) (like KeePassXC or Bitwarden) instead of the browser's built-in password saver.

---

## 2. Virtual Private Networks (VPNs)

A VPN creates an encrypted tunnel between your device and a server outside Iran. It hides your IP address from websites and hides the websites you visit from the ISP (and by extension, the government).

### The Iranian Context: The Risk of "Free" VPNs

In Iran, the market is flooded with "Free VPNs." **Avoid these.**

- **Data Farming:** Many free VPNs sell user data to third parties.
- **Government Honey Pots:** Some free VPNs are operated by state intelligence to monitor users.
- **Malware:** Free VPN apps often contain spyware.

### Criteria for a Secure VPN

When choosing a VPN service for use in Iran, consider:

1.  **No-Logs Policy:** The provider must not store records of your activity. Ideally, this has been proven in court or via independent audit.
2.  **Jurisdiction:** Avoid VPNs based in "14 Eyes" countries or countries with weak privacy laws. Ideally, look for Switzerland, Panama, or privacy-friendly EU nations.
3.  **Obfuscation (Stealth Mode):** The Islamic Republic uses Deep Packet Inspection (DPI) to identify and block OpenVPN and WireGuard protocols. A good VPN must offer obfuscation (e.g., Shadowsocks, V2Ray, Obfsproxy) to disguise VPN traffic as normal HTTPS traffic.
4.  **Payment Methods:** Ability to pay via cryptocurrency or cash (if possible via third parties) adds a layer of anonymity.

### Recommended Providers

Based on privacy community standards and resilience:

- **Mullvad:** Excellent privacy (no email required), flat pricing. _Note: May require bridge/obfuscation configuration in Iran._
- **IVPN:** rigorous privacy audits, supports obfuscation (Obfsproxy).
- **Proton VPN:** Based in Switzerland, free tier is trustworthy (unlike most others), uses "Stealth" protocol to bypass censorship.

### VPN vs. Proxy (Shadowsocks/V2Ray)

While VPNs tunnel _all_ system traffic, proxies (like V2RayNG, Nekobox) are often more effective at bypassing the Great Firewall of Iran because they are designed specifically for censorship circumvention rather than just encryption.

- **Recommendation:** For general browsing and bypassing heavy filtering, V2Ray/Xray configurations are often more reliable than commercial VPN apps in Iran. Ensure you get configurations from trusted sources to avoid malicious nodes.

---

## 3. The Tor Network and Anonymity

Tor (The Onion Router) routes your traffic through three random volunteer nodes around the world, encrypting it at each step. It is the best tool for **anonymity**.

### When to Use Tor

- Accessing blocked news sites securely.
- Whistleblowing or communicating sensitive political information.
- Preventing your ISP from knowing _what_ you are doing (they can only see you are using Tor).

### Bypassing Tor Blocking in Iran

Tor nodes are public and often blocked. You must use **Bridges**.

- **Pluggable Transports:** These disguise Tor traffic.
  - **Snowflake:** Highly effective in Iran. It routes traffic through temporary proxies run by volunteers in free countries.
  - **obfs4:** Makes Tor traffic look like random unreadable data.

### Tor Browser Mobile

- **Android:** Use the official **Tor Browser**.
- **iOS:** Use **Onion Browser** (official recommendation). _Note: Due to iOS limitations, it is not as secure as the Android/Desktop version, but it is the best option available._

---

## 4. Advanced Privacy Concepts

### DNS over HTTPS (DoH)

Even with a secure browser, your DNS requests (the "phonebook" lookup for website names like `google.com`) might be visible to the ISP.

- **Enable DoH:** This encrypts your DNS queries inside HTTPS traffic. Most modern browsers (Firefox, Brave, Chrome) support this.
- **Warning:** In Iran, ensure your DoH provider (e.g., Cloudflare, Quad9) is not blocked. If blocked, the browser may fail to load sites.

### Browser Fingerprinting

Websites can identify you without cookies by analyzing your screen resolution, installed fonts, and battery level.

- **Defense:** Use **Tor Browser** (which standardizes these values for all users) or **Mullvad Browser**. Avoid installing too many extensions on Firefox/Chrome, as your unique combination of extensions makes you more identifiable.

### Search Engines

Google records your search history to build a profile. Switch to:

- **DuckDuckGo:** No tracking, US-based.
- **Startpage:** Google search results, but anonymized.
- **Brave Search:** Independent index, privacy-focused.

## Summary Checklist

1.  [ ] **Switch Browser:** Move from Chrome/Edge to Firefox or Brave.
2.  [ ] **Harden Settings:** Enable HTTPS-Only mode and Strict Tracking Protection.
3.  [ ] **Install uBlock Origin:** Block ads and malicious scripts.
4.  [ ] **Get a Trusted VPN:** Avoid free VPNs; use Mullvad, IVPN, or Proton.
5.  [ ] **Use Tor for High Risk:** Configure Tor Browser with Snowflake bridges for sensitive work.
6.  [ ] **Mobile Hygiene:** Use Firefox/Brave on Android and Onion Browser on iOS. Avoid using dedicated apps for services (like Facebook/Twitter) that can be accessed via a secure browser.
