---
title: "Commercial Platform Hardening and Data Minimization"
tags:
  [
    hardening,
    privacy,
    data-minimization,
    social-media,
    google,
    android,
    tiktok,
    facebook,
  ]
category: "Device and Application Surveillance"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists]
topics:
  [
    "Platform Security",
    "Account Hardening",
    "Privacy Frontends",
    "Digital Hygiene",
  ]
summary: "A comprehensive guide to securing commercial accounts (Google, Meta, TikTok) and minimizing data collection through privacy settings and alternative frontends."
source: "Raaznet"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of account settings",
    "Familiarity with browser extensions",
  ]
estimated_read_time: "15 minutes"
---

# Commercial Platform Hardening and Data Minimization

Users often rely on commercial platforms like Google, Instagram, and WhatsApp for daily communication and information. However, these platforms inherently collect vast amounts of data—location history, browsing habits, and social graphs—that can be exploited by state actors through data breaches, legal requests, or account compromises.

This guide focuses on **hardening** your existing accounts on these platforms to reduce their attack surface and **minimizing** the data they collect about you.

---

## 1. Social Media Hardening

Social media platforms are primary targets for surveillance. Hardening these accounts reduces the risk of profiling and social graph mapping.

### TikTok

TikTok collects extensive device and usage data. For Iranian users, the primary risk is the correlation of this data with real-world identities.

- **Web Browser Access:** Whenever possible, use TikTok via a hardened web browser (like Firefox with uBlock Origin) instead of the mobile app. The app has significantly more access to device sensors and identifiers.
- **Privacy Settings:**
  - **Account Privacy:** Set your account to **Private** to restrict visibility.
  - **Suggest your account:** Disable "Suggest your account to others" to prevent algorithmic mapping of your social circle.
  - **Downloads:** Disable "Allow your videos to be downloaded."
  - **Ad Personalization:** Go to **Settings and privacy > Ads** and disable personalized ads.
- **Data Minimization:**
  - **Contacts:** Never sync your phone contacts or Facebook friends. This builds a social graph that can link your anonymous account to your real identity.
  - **Download Your Data:** Regularly request your data file (`Settings > Account > Download your data`) to inspect what information TikTok has stored about you.

### Meta (Facebook & Instagram)

Meta platforms are aggressive in tracking user behavior across the web.

- **Disable Link History:** Meta recently introduced a "Link History" feature that tracks every website you visit via the in-app browser.
  1.  Open the Facebook/Instagram app.
  2.  Go to **Settings & Privacy > Link History**.
  3.  **Disable** this feature to stop Meta from building a profile of your external browsing habits (e.g., news sites, political blogs).
- **Off-Facebook Activity:**
  - Go to **Settings > Your Information > Off-Facebook Activity**.
  - Select **Clear History** and then **Disconnect Future Activity**. This prevents Meta from associating your browsing on third-party sites/apps with your account.
- **Two-Factor Authentication (2FA):**
  - **Avoid SMS 2FA:** In Iran, SMS can be intercepted by mobile network operators. Use an authenticator app (like Aegis or Raivo) or a hardware key.

### Zoom

While often necessary for work or education, Zoom has had historical security flaws.

- **Use the Web Client:** If possible, join meetings via the browser (`Join from your browser` link) rather than installing the desktop client. This sandboxes the application.
- **Meeting Security:**
  - Always use **Waiting Rooms** to screen participants.
  - Require **Passcodes** for all meetings.
  - Disable "Join before host."
  - Limit screen sharing to the Host only.

---

## 2. Google Ecosystem & Android Hardening

Google's business model relies on data collection. Hardening a Google account significantly reduces your digital footprint.

### Google Account Controls

Visit [myaccount.google.com](https://myaccount.google.com/) to configure these settings:

- **Location History (Timeline):**
  - **Pause** this setting immediately.
  - If you have past history, enable **Auto-delete** (set to the minimum, e.g., 3 months) or manually delete all history.
  - _Risk:_ Location data can reveal attendance at protests or sensitive meetings.
- **Web & App Activity:**
  - Configure **Auto-delete** to 3 months. This limits the historical data available if your account is compromised.
- **Ad Personalization:**
  - Turn **OFF** Ad Personalization. While this doesn't stop ads, it reduces the detailed profiling Google performs based on your interests.
- **Find My Device:**
  - _Trade-off:_ This feature allows you to wipe a lost phone, but it also constantly tracks your device's location.
  - _Recommendation:_ If you are attending a protest or high-risk event, disable "Find My Device" or leave the phone at home.

### Android Device Hardening

- **App Isolation (Work Profiles):**
  - Use **Shelter** or **Insular** (FOSS apps) to create a "Work Profile" on your device.
  - Install invasive apps (like WhatsApp, Instagram, or Google Play Services) _inside_ the Work Profile.
  - You can "freeze" the entire Work Profile with one tap, effectively killing all background processes and tracking from those apps.
- **Android 15 Private Space:**
  - If you have a newer device running Android 15+, use the native **Private Space** feature. This creates a hidden, locked environment for sensitive apps that is isolated from the main system.
- **Advertising ID:**
  - Go to **Settings > Privacy > Ads**.
  - Select **Delete advertising ID**. This prevents apps from tracking your behavior across different applications to build a profile.
- **Permissions Management:**
  - Regularly audit permissions (**Settings > Privacy > Permission Manager**).
  - Remove **Location** and **Microphone** access from apps that do not strictly need them.
  - Use "Only this time" or "While using the app" for necessary permissions.

---

## 3. Data Minimization via Privacy Frontends

One of the most effective ways to minimize data collection is to access content _without_ logging into the platform. "Frontends" are open-source intermediaries that fetch content for you, shielding your IP and identity from the commercial platform.

> **Note:** Commercial platforms frequently block these frontends. If one instance is down, try another or switch to a localized VPN.

### YouTube Alternatives

Watching YouTube directly exposes your viewing habits to Google.

- **NewPipe (Android):** A lightweight, FOSS client that plays YouTube videos without a Google account. It supports background play, downloads, and creates a local (offline) subscription feed.
- **LibreTube (Android):** Uses the Piped API to proxy video streams, meaning you never connect directly to Google servers.
- **Invidious / Piped (Web):** Web interfaces that allow you to watch YouTube videos without JavaScript or ads.
  - _Warning:_ Public instances are often unstable due to Google's blocking.
  - _Recommendation:_ Use **`yt-dlp`** (command line tool) on a computer to download videos for offline viewing if streaming is throttled or blocked.

### Reddit & TikTok Alternatives

- **Redlib (formerly Libreddit):** An open-source frontend for Reddit. It is lightweight, works without JavaScript, and prevents Reddit from tracking your reading habits.
- **ProxiTok:** A web frontend for TikTok. It allows you to view content and user profiles without installing the invasive app or creating an account.

### Twitter / X

- **Nitter:** While historically popular, Nitter instances are currently unreliable due to platform changes.
- **Recommendation:** If you must browse X, use the **Tor Browser** and a "burner" account created with an anonymous email. Do not use your personal account for viewing sensitive political content.

---

## 4. Browser Hardening

Your web browser is the gateway to the internet. Hardening it prevents fingerprinting and tracking.

- **Extensions:**
  - **uBlock Origin:** The gold standard for content blocking. It blocks ads, trackers, and malware domains.
    - _Tip:_ Enable "Medium Mode" or strict filtering lists for better protection in high-risk environments.
  - **Avoid Redundant Extensions:** Uninstall extensions you don't use. Each extension adds a unique "fingerprint" to your browser and increases the attack surface.
- **Firefox Configuration:**
  - Enable **Enhanced Tracking Protection** (set to "Strict").
  - Enable **HTTPS-Only Mode** to prevent unencrypted connections.
  - Configure the browser to **delete cookies and site data** when closed.

---

## 5. Privacy-Preserving Alternatives

Where possible, replace commercial services with privacy-focused alternatives that do not monetize your data.

| Category         | Commercial Tool        | Privacy Alternative                                                    |
| :--------------- | :--------------------- | :--------------------------------------------------------------------- |
| **File Sharing** | Google Drive / Dropbox | **OnionShare** (Anonymous, Tor-based) or **Syncthing** (P2P, no cloud) |
| **Calendar**     | Google Calendar        | **Proton Calendar** or **Tuta** (End-to-End Encrypted)                 |
| **Translation**  | Google Translate       | **DeepL** (Better privacy policy) or **Lingva Translate** (Frontend)   |
| **News**         | Google News / Feed     | **RSS Readers** (Feeder, Newsboat) - Curate your own sources           |

### Iranian Context Summary

- **VPN Leaks:** When using commercial platforms, ensure your VPN "Kill Switch" is active. A momentary drop in VPN connection can reveal your real Iranian IP address to the platform, linking your activity to your physical location.
- **App Stores:** Avoid third-party Iranian app stores if possible, as they may host modified versions of apps. Download tools like **NewPipe** or **Signal** directly from their official websites or F-Droid.
