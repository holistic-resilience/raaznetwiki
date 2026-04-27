---
title: "Secure Browsing and Web Hygiene"
tags:
  [
    browser-security,
    privacy,
    firefox,
    ublock-origin,
    digital-hygiene,
    https,
    tracking-protection,
  ]
category: "Technical Foundations"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  ["Web Browser Security", "Digital Hygiene", "Tracking Prevention", "Phishing"]
summary: "Comprehensive guide to securing web browsers, configuring privacy settings, and maintaining digital hygiene to protect against surveillance and tracking in Iran."
source: "RaazNet Aggregation"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites:
  ["Basic computer literacy", "Understanding of internet navigation"]
estimated_read_time: "15 minutes"
---

# Secure Browsing and Web Hygiene

The web browser is the primary window to the internet and, consequently, the most common entry point for surveillance, censorship, and malware. The regime's "National Information Network" (SHOMA) relies heavily on tracking user traffic, intercepting unencrypted connections, and identifying digital fingerprints.

This guide focuses on hardening your browsing environment, minimizing your digital footprint, and adopting hygiene habits that protect your identity and data.

> **Note:** While this guide covers secure browsing on the "clearnet," for high-risk activities requiring anonymity, you must use the **Tor Browser**. Please refer to the [Tor and Anonymity Networks](tor-and-anonymity-networks) guide.

---

## 1. Choosing a Trustworthy Browser

Most default browsers (Chrome, Edge, Safari) are designed by companies whose business models rely on data collection. For Iranian users, this tracking poses a significant privacy risk.

### Recommended: Mozilla Firefox

**Firefox** is the preferred browser for privacy and security professionals. It is open-source, highly auditable, and offers the most robust privacy configuration options.

- **Why Firefox?** It is not based on Chromium (Google's engine), preventing a monopoly on web standards. It supports advanced containerization (isolating websites from each other) and extensive "hardening" (modifying hidden settings for security).

### Alternatives

- **Brave:** A Chromium-based browser with built-in ad and tracker blocking. It is user-friendly but arguably less customizable than Firefox.
- **Mullvad Browser:** A privacy-focused fork of Firefox developed by the Tor Project and Mullvad VPN. It provides Tor-like fingerprinting protection without using the Tor network (best used with a VPN).
- **Librewolf:** A community-maintained version of Firefox that comes pre-configured with strong privacy settings (telemetry disabled, tracking protection enabled).

### What to Avoid

- **Google Chrome:** Tracks browsing history and ties it to your Google identity.
- **Microsoft Edge:** Sends extensive telemetry to Microsoft.
- **Iranian Domestic Browsers:** Any browser developed or promoted by the state (often advertised for "faster access" to domestic sites) likely contains root certificates or surveillance hooks allowing the regime to decrypt your traffic. **Avoid these at all costs.**

---

## 2. Hardening Browser Configuration

Installing a secure browser is only the first step. You must configure it to resist surveillance.

### Enable HTTPS-Only Mode

The "S" in HTTPS stands for "Secure" (Encrypted). It prevents ISPs and the government from seeing the _content_ of the page you are visiting (though they can still see the _domain_).

- **Risk in Iran:** Attackers often use "SSL Stripping" to downgrade connections from HTTPS to HTTP to steal passwords.
- **Action:**
  - **Firefox:** Settings > Privacy & Security > Scroll to bottom > Select **Enable HTTPS-Only Mode in all windows**.
  - **Brave/Chromium:** Settings > Privacy and Security > Security > Toggle **Always use secure connections**.

### Configure DNS over HTTPS (DoH)

Standard DNS queries (looking up website names) are unencrypted, allowing your ISP (and the regime) to see every domain you request. DoH encrypts these requests inside HTTPS traffic.

- **Action:**
  - **Firefox:** Settings > Privacy & Security > DNS over HTTPS > Select **Max Protection**. Choose a provider like Cloudflare or NextDNS, or a custom trusted provider.
  - **Note:** If the default DoH providers are blocked in Iran, you may need to set up a custom DoH server or rely on your VPN's DNS.

### Strict Tracking Protection

Modern browsers can block third-party cookies and trackers that follow you across the web.

- **Action:** Set "Enhanced Tracking Protection" to **Strict**.
- **Fingerprinting Resistance:** Websites can identify you by your screen resolution, installed fonts, and battery level. Firefox's Strict mode resists some of this, but the **Mullvad Browser** or **Tor Browser** offers the best protection against fingerprinting.

### Search Engine Selection

Google and Bing record your search queries, IP address, and user profile.

- **Recommended:**
  - **DuckDuckGo:** Does not track users or store search history.
  - **Startpage:** Provides Google search results but anonymizes your request (acts as a proxy between you and Google).
  - **Brave Search:** An independent search index focused on privacy.

---

## 3. Essential Privacy Extensions

Extensions can significantly enhance browser security, but installing too many makes you unique (fingerprintable). Stick to a few trusted, open-source extensions.

| Extension          | Purpose                                                                                         | Notes                                                             |
| :----------------- | :---------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| **uBlock Origin**  | The gold standard for content filtering. Blocks ads, trackers, and malware domains efficiently. | **Essential.** Do not confuse with "uBlock" (which is different). |
| **Privacy Badger** | Learns to block invisible trackers that slip past other filters.                                | Developed by EFF. Good supplement to uBlock Origin.               |
| **Bitwarden**      | Secure password management.                                                                     | Prevents browser-based password theft.                            |

> **Warning:** Be extremely cautious when installing extensions. Malicious extensions are a common vector for spying. Only install from official stores and check reviews/developer reputation.

---

## 4. Web Hygiene Habits

Technology alone cannot protect you; behavior is equally important.

### Stop Saving Passwords in the Browser

Browsers often store saved passwords in a way that is easily accessible to malware or anyone with physical access to your device.

- **Solution:** Disable the browser's built-in password manager. Use a dedicated, encrypted password manager like **KeePassXC** (offline) or **Bitwarden** (cloud-synced but encrypted).

### Compartmentalization (Containers)

Don't let your social media activity mix with your browsing.

- **Firefox Multi-Account Containers:** This extension lets you isolate sites. You can keep "Google" in one container and "News Reading" in another. Google cannot see what you read in the other container because cookies are separated.
- **Profile Separation:** Use one browser (e.g., Firefox) for sensitive research and another (e.g., Brave) for general entertainment.

### Verification of Certificates

When visiting sensitive sites (email, banking), click the "Lock" icon in the address bar.

- **Check the "Issued By" field:** Ensure the certificate authority (CA) is a recognized international entity (like Let's Encrypt, DigiCert, etc.) and not a suspicious or government-affiliated CA.
- **Never bypass SSL Warnings:** If your browser warns "Your connection is not private," **do not proceed**. In Iran, this often indicates an active Man-in-the-Middle (MITM) attack where the state is trying to intercept your encrypted connection.

### Managing History and Data

- **Auto-Delete:** Configure your browser to clear cookies and history when you close it.
  - _Firefox:_ Settings > Privacy & Security > History > Select "Use custom settings for history" > Check **Clear history when Firefox closes**.
- **Private Browsing:** Use Private/Incognito windows for one-off searches. Remember: **Private mode does NOT hide your activity from your ISP.** It only prevents data from being saved on your local device.

---

## 5. Metadata and Downloads

When downloading files (documents, images, PDFs), remember that they contain "Metadata" (data about data), such as:

- Author name
- Creation date
- Software version used
- GPS location (for photos)

**Hygiene Tip:** Before sharing or uploading files, use tools like **MAT2** (Metadata Anonymisation Toolkit) or basic OS tools to strip this information.

---

## Summary Checklist

1.  [ ] **Install Firefox** (or Mullvad Browser).
2.  [ ] **Install uBlock Origin**.
3.  [ ] **Set Default Search Engine** to DuckDuckGo or Startpage.
4.  [ ] **Enable HTTPS-Only Mode**.
5.  [ ] **Enable DNS over HTTPS (DoH)** (Max Protection).
6.  [ ] **Disable Built-in Password Saving** and use a dedicated manager.
7.  [ ] **Configure "Clear History on Exit"**.
8.  [ ] **Never ignore SSL certificate warnings**.

By following these steps, you significantly raise the cost and difficulty for mass surveillance systems to track your digital life.
