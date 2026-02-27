---
title: "Google Services Privacy and Hardening"
tags:
  [
    google,
    privacy,
    security,
    hardening,
    gmail,
    youtube,
    android,
    censorship-circumvention,
    iran,
  ]
category: "Platform Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "Account Security",
    "Data Minimization",
    "De-Googling",
    "Surveillance Protection",
  ]
summary: "A comprehensive guide to securing Google accounts for Iranian users, minimizing data collection, and using privacy-focused alternatives and frontends."
source: "RaazNet Aggregated Resources"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Active Google Account",
    "Basic understanding of 2FA",
    "VPN/Circumvention tool",
  ]
estimated_read_time: "20 minutes"
---

# Google Services Privacy and Hardening

Google services are ubiquitous, offering convenience at the cost of massive data collection. For users in Iran, relying on Google presents a complex threat model. While Google generally does not comply with data requests from the Islamic Republic, the centralized nature of the data makes a Google account a "single point of failure." If regime actors compromise your account (via phishing or SMS interception), they gain access to your location history, emails, contacts, photos, and search logs.

Furthermore, Google services are subject to both local censorship and international sanctions, often requiring a VPN for reliable access. This guide focuses on **hardening your Google account** to prevent compromise and **minimizing your footprint** by using privacy-preserving alternatives.

---

## 1. The Core Threat: Account Security

The primary method the Iranian regime uses to access Google accounts is **credential theft** (phishing) and **2FA interception** (SMS hijacking). Securing the login process is your first line of defense.

### Two-Step Verification (2FA)

**Crucial:** Do not rely on SMS for Two-Step Verification. Telecommunication providers in Iran are state-controlled and can intercept SMS codes to hijack accounts.

1.  **Enable 2-Step Verification:** Go to [My Account > Security](https://myaccount.google.com/security).
2.  **Use an Authenticator App:** Use an app like **Raivo** (iOS), **Aegis** (Android), or **Ente Auth**. These generate codes locally on your device and cannot be intercepted by the network.
3.  **Use Security Keys (Best Practice):** If possible, use a hardware key (YubiKey, Nitrokey, or Google Titan). This makes phishing physically impossible.
4.  **Backup Codes:** Generate and print **Backup Codes**. Store them in a safe, physical location (not on your phone). These allow you to regain access if you lose your device or cannot access your VPN.
5.  **Remove Phone Numbers:** If your account allows it, remove your Iranian phone number from the "Recovery phone" section to prevent it from being used as a fallback verification method.

### The Advanced Protection Program

For high-risk users (journalists, activists), Google offers the **Advanced Protection Program**.

- **What it does:** Enforces the use of physical security keys (or Passkeys), blocks unauthorized third-party app access, and enables stricter scanning for malware.
- **Trade-off:** It may limit how you use your account on some older devices or third-party apps, but it provides the highest level of login security against targeted attacks.

### Suspicious Activity Monitoring

Regularly check for unauthorized access, especially if you have been detained or your device was confiscated.

- **Check Devices:** Go to [Your Devices](https://myaccount.google.com/device-activity). Sign out of any device you do not recognize or no longer control.
- **Check Sessions:** If you see logins from Iranian IPs when you were using a VPN, or logins from cities you are not in, change your password immediately.

---

## 2. Data Minimization: Activity Controls

If you must use Google services, prevent them from logging your every move. By default, Google records extensive history.

### Pause Activity Logging

Navigate to [Data & Privacy](https://myaccount.google.com/data-and-privacy) and **Pause** the following:

1.  **Web & App Activity:** Stops Google from saving your search history, Chrome browsing history, and activity on sites that use Google services.
2.  **Location History (Timeline):** Stops Google from creating a map of where you go with your devices. _Note: This is critical for physical safety in Iran._
3.  **YouTube History:** Stops Google from logging what you watch and search for on YouTube.

### Auto-Delete Controls

If you cannot pause these services for functionality reasons, set up **Auto-Delete** to the minimum duration (usually 3 months). This ensures that if your account is compromised later, older historical data is already gone.

### Ad Personalization

Turn **Off** "My Ad Center" / Ad Personalization. While this doesn't stop tracking entirely, it prevents Google from building a targeted profile based on your perceived interests, which can include political or social leanings.

---

## 3. Service-Specific Hardening

### Gmail

Gmail is not end-to-end encrypted. Google has the technical ability to read your emails, and anyone who hacks your account can read everything.

- **Use a Mail Client:** Instead of the web interface, use a client like **Thunderbird** (PC) or **K-9 Mail** (Android). These allow you to download emails for offline access and easily integrate PGP encryption.
- **End-to-End Encryption (PGP):** For sensitive communication, use **Mailvelope** (browser extension) or PGP integration in Thunderbird/K-9 Mail. This ensures that even if Google or a hacker accesses your inbox, they only see scrambled text.
- **Disable Smart Features:** In Gmail settings, turn off "Smart features and personalization." This stops Google from scanning your email content to offer "smart" suggestions.
- **Block Remote Images:** Configure Gmail to "Ask before displaying external images." Loading images can reveal your IP address and confirm you opened the email to the sender (tracking pixels).

### Google Drive & Photos

These services scan content for policy violations.

- **Encryption First:** Never upload sensitive documents (scans of IDs, protest evidence, contact lists) directly to Drive or Photos.
  - **Encrypt locally:** Use **Cryptomator** or **Veracrypt** to create an encrypted vault, then upload that vault file to Drive.
  - **Metadata Removal:** Before uploading photos, use tools like **ObscuraCam** or **ExifEraser** to remove GPS location and device data.
- **Face Grouping:** In Google Photos settings, disable "Face Grouping" to prevent Google from creating biometric maps of you and your contacts.

### Google Search

Google Search builds a detailed profile of your interests.

- **Alternative:** Use **DuckDuckGo**, **Brave Search**, or **Startpage**. Startpage fetches results from Google but strips your identity, giving you Google-quality results without the tracking.

---

## 4. YouTube: Privacy-Focused Viewing

YouTube is a vital source of information, but watching while logged in builds a permanent record of your political interests.

### Use Privacy Frontends

Frontends allow you to watch YouTube videos without connecting directly to Google's servers, without ads, and without an account.

- **Web (Browser):** Use **Invidious** or **Piped**. These are web interfaces that proxy your traffic. You can subscribe to channels without a Google account.
- **Android:** Use **NewPipe** or **LibreTube**. These open-source apps store your subscriptions locally on your device. They bypass censorship more easily and offer background play/download features essential for users with unstable internet.
- **Desktop:** Use **FreeTube**. It stores all data locally and allows you to watch anonymously.

### RSS Feeds

You can follow YouTube channels via RSS readers (like Feeder or Akregator) without an account.

- **Format:** `https://www.youtube.com/feeds/videos.xml?channel_id=[CHANNEL_ID]`

---

## 5. Android and the Play Store

On Android, a Google account is deeply integrated into the OS.

- **Avoid "Sign in with Google":** When using third-party apps, do not use the "Sign in with Google" button. Create standalone accounts with a dedicated email address or password manager. This prevents Google from knowing which apps you use and prevents a Google account ban from locking you out of other services.
- **Location Services:** On Android, ensure "Google Location Accuracy" (which sends Wi-Fi/Bluetooth data to Google) is turned **OFF**. Rely on "Device sensors only" (GPS) where possible.
- **App Store Alternatives:** You do not need a Google account to download apps.
  - **Aurora Store:** An anonymous frontend for the Google Play Store. It allows you to download apps without logging in.
  - **F-Droid:** A repository for Free and Open Source Software (FOSS). Use this for security-critical apps (VPNs, Messengers).

---

## 6. Alternatives (De-Googling)

The best way to protect your data from Google is to stop using their services where possible.

| Service           | Google Product       | Privacy-Focused Alternative                                 |
| :---------------- | :------------------- | :---------------------------------------------------------- |
| **Search**        | Google Search        | **Brave Search**, **DuckDuckGo**, **Startpage**             |
| **Browser**       | Chrome               | **Brave**, **Firefox** (Hardened), **Tor Browser**          |
| **Email**         | Gmail                | **Proton Mail**, **Tuta**, **Riseup**                       |
| **Cloud Storage** | Google Drive         | **Proton Drive**, **Tresorit**, **Nextcloud** (Self-hosted) |
| **Documents**     | Google Docs          | **Proton Docs**, **CryptPad**, **OnlyOffice**               |
| **Maps**          | Google Maps          | **Organic Maps**, **Magic Earth**, **OSMAnd**               |
| **2FA**           | Google Authenticator | **Aegis** (Android), **Raivo** (iOS), **Ente Auth**         |
| **Video**         | YouTube              | **NewPipe**, **Invidious**, **FreeTube**                    |

---

## 7. Emergency Checklist

If you believe your Google account has been targeted or compromised:

1.  **Change Password Immediately:** Use a strong, unique passphrase.
2.  **Revoke Sessions:** Force sign-out on all devices via the Security dashboard.
3.  **Check Recovery Info:** Ensure the recovery email/phone has not been changed by the attacker.
4.  **Review Forwarding:** Check Gmail settings to ensure your emails are not being auto-forwarded to an unknown address.
5.  **Check Third-Party Apps:** Revoke access to any app you do not recognize in the "Apps with access to your account" section.
