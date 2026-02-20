---
title: "Privacy-Preserving Software Alternatives"
tags:
  [
    privacy,
    open-source,
    anti-surveillance,
    iran-security,
    censorship-circumvention,
    foss,
  ]
category: "Device and Application Surveillance"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists]
topics: ["Digital Privacy", "Censorship Circumvention", "FOSS Alternatives"]
summary: "A curated list of privacy-respecting software alternatives tailored for Iranian users to bypass censorship and minimize surveillance risks."
source: "Raaznet Aggregation"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of app installation", "Access to a working VPN or Tor"]
estimated_read_time: "15 minutes"
---

# Privacy-Preserving Software Alternatives

Choosing the right software is not just about "privacy" in the abstract—it is a matter of safety. The Islamic Republic utilizes Deep Packet Inspection (DPI), DNS hijacking, and collaboration with domestic tech companies to monitor citizens.

This guide provides **Free and Open Source Software (FOSS)** alternatives to popular proprietary applications. These tools are selected based on three criteria relevant to Iran:

1.  **Minimization of Data Collection:** They do not store user data that could be subpoenaed or intercepted.
2.  **Censorship Resilience:** They often use decentralized or proxy-based methods to bypass the filtering of international platforms.
3.  **Security:** They offer strong encryption to protect against local network surveillance.

> [!danger] **CRITICAL WARNING: Avoid Domestic Iranian Apps**
> Do **not** use domestic messaging or social media applications such as **Rubika, Soroush, Bale, Eitaa, or iGap**.
>
> - These apps lack end-to-end encryption. \* They are legally required to store data on servers inside Iran, accessible to intelligence services.
> - They are often promoted with "free data" incentives to lure users into the surveillance net.
>
> If you are forced to use them (e.g., for banking or university administrative tasks), install them **only** inside an isolated profile using **Shelter** (see below) and never grant them permissions to your contacts, location, or microphone.

---

## 1. Secure Messaging & Communication

Standard SMS and unencrypted calls in Iran are monitored. While WhatsApp and Telegram are popular, they have metadata risks or require trusting a central server.

### Signal (Recommended)

**Signal** is the gold standard for encrypted communication. However, it is blocked in Iran.

- **Why use it:** End-to-End Encryption (E2EE) for messages, calls, and metadata.
- **How to connect in Iran:** You must use a **Signal Proxy**.
  - Find proxies via Twitter/X using hashtags like `#IRanASignalProxy` or via trusted channels.
  - Go to _Settings > Data and Storage > Use Proxy_.
- **Security Tip:** Enable "Registration Lock" to prevent SIM swapping attacks, a common tactic in Iran.

### Session

**Session** is a decentralized messenger that requires **no phone number** to sign up.

- **Why use it:** Removes the risk of your account being tied to a SIM card (which is registered to your national ID).
- **Resilience:** Uses an onion-routing network (Lokinet) which is harder to block than centralized servers.

---

## 2. Social Media Frontends (Bypassing Blocks & Tracking)

Directly accessing platforms like YouTube, Reddit, or Twitter often requires a high-bandwidth VPN. "Frontends" are lightweight, privacy-focused viewers that allow you to access this content—often without an account and with lower bandwidth usage.

### YouTube Alternatives

Watching educational or news content on YouTube is difficult due to throttling.

- **NewPipe (Android):**
  - **Features:** Background play, offline downloading (essential for unstable internet), no Google account required.
  - **Privacy:** Does not send playback data to Google.
- **Invidious / Piped (Web):**
  - **Usage:** Web-based viewers. If one "instance" (server) is blocked by the filtering committee, you can simply switch to another.
  - **Benefit:** valid for low-speed connections; no JavaScript required.

### Instagram & TikTok Alternatives

- **ProxiTok (TikTok):** Allows viewing TikTok content without the invasive app.
- **Barinsta (Instagram - _Use with Caution_):** Open-source Instagram client. _Note: Instagram aggressively bans accounts using third-party clients. Use a "burner" account, not your main identity._

### Reddit Alternatives

- **Redlib:** A private frontend for Reddit.
  - **Why:** Reddit is frequently disrupted or blocked. Redlib instances often remain accessible when the main domain is not.
  - **Privacy:** No ads, no tracking pixels, works without JavaScript.

---

## 3. App Isolation (Sandboxing)

In Iran, users are often forced to install insecure apps for banking (`Hamrah Card`, `Ap`), ride-hailing (`Snapp`, `Tapsi`), or government services (`My Irancell`). These apps often demand invasive permissions.

### Shelter (Android)

**Shelter** uses the "Work Profile" feature of Android to isolate apps.

- **Strategy:** Install **Shelter** from F-Droid.
- **Action:** Install all domestic Iranian apps (Snapp, Rubika, Banking apps) _inside_ the Shelter profile.
- **Benefit:**
  - These apps **cannot** access your personal contacts, photos, or files in your main profile.
  - You can "Freeze" the work profile with one tap, instantly killing all background processes of these surveillance apps.

---

## 4. Web Browsing & Privacy Extensions

### Browser: Firefox (or Mull)

Avoid Google Chrome. Use **Firefox** or **Mull** (a hardened version of Firefox for Android).

- **Configuration:** Set "Enhanced Tracking Protection" to _Strict_.
- **DoH:** Enable "DNS over HTTPS" (e.g., Cloudflare or NextDNS) to bypass basic DNS-level censorship.

### Essential Extensions

Install these add-ons to block trackers and reduce data usage:

1.  **uBlock Origin:** The most efficient ad blocker.
    - _Iran Context:_ Blocks malicious ads often served on Persian download sites.
2.  **Privacy Badger:** Automatically learns to block invisible trackers.
3.  **LocalCDN:** Emulates Content Delivery Networks locally. This speeds up browsing (crucial for slow Iranian internet) and prevents tracking requests to Google/Microsoft servers.

---

## 5. File Sharing & Cloud Storage

Avoid Google Drive or Dropbox for sensitive materials (scans of IDs, protest evidence, etc.).

### Syncthing

**Syncthing** synchronizes files between devices (e.g., your phone and laptop) without a cloud server.

- **Why:** It is Peer-to-Peer (P2P). Data never sits on a third-party server.
- **Resilience:** Harder to block than a central URL like `drive.google.com`.

### OnionShare

**OnionShare** allows you to securely send files of any size using the Tor network.

- **Use Case:** Sending large video files to journalists or activists anonymously.
- **Security:** The recipient does not need an account, just the Tor Browser and the link you generate.

---

## 6. Utilities & Tools

### Translation: LibreTranslate / DeepL

Avoid Google Translate for sensitive documents.

- **LibreTranslate:** An open-source, self-hostable translation engine. Use public instances that do not log your text.
- **DeepL:** Generally has better privacy policies than Google, but still closed source.

### Keyboard: OpenBoard

Keyboard apps can log keystrokes (passwords, messages).

- **Recommendation:** **OpenBoard** (Android) or standard AOSP keyboard with network access blocked.
- **Action:** Block network access for your keyboard app using a firewall (like NetGuard) to ensure it never "phones home."

---

## Summary Table

| Category        | Proprietary / Dangerous                              | Recommended Alternative                | Iranian Context Note                         |
| :-------------- | :--------------------------------------------------- | :------------------------------------- | :------------------------------------------- |
| **Messaging**   | SMS, WhatsApp, Telegram (Standard), **Rubika/Eitaa** | **Signal**, **Session**                | Use Signal Proxy; Session needs no SIM.      |
| **Video**       | YouTube                                              | **NewPipe**, **Invidious**             | Download offline; bypass throttling.         |
| **Browser**     | Chrome, Samsung Internet                             | **Firefox**, **Mull**, **Tor Browser** | Use uBlock Origin to save bandwidth/privacy. |
| **Social**      | Twitter, Reddit, Instagram                           | **Mastodon**, **Redlib**, **ProxiTok** | Access content without accounts/tracking.    |
| **Cloud**       | Google Drive, Dropbox                                | **Syncthing**, **Proton Drive**        | P2P sync avoids central server censorship.   |
| **Translation** | Google Translate                                     | **LibreTranslate**                     | Prevent text logging.                        |
| **Isolation**   | _(None)_                                             | **Shelter**                            | Mandatory for domestic banking/gov apps.     |

---

_Last Updated: February 2026_
