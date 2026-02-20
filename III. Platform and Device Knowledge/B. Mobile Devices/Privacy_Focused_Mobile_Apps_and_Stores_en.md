---
title: "Privacy-Focused Mobile Apps and Stores"
tags:
  [
    mobile-security,
    privacy-tools,
    app-stores,
    android,
    ios,
    iran-security,
    censorship-circumvention,
  ]
category: "Platform and Device Knowledge"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, High-Risk Users]
topics:
  [
    "App Stores",
    "Secure Browsers",
    "Encrypted Messaging",
    "Two-Factor Authentication",
    "Documentation Tools",
  ]
summary: "A curated list of privacy-respecting mobile applications and safe app stores tailored for Iranian users to bypass censorship and avoid state surveillance."
source: "Raaznet Aggregated Knowledge"
content_type: "Resource List"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of app installation",
    "Familiarity with sideloading (Android)",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-18"
---

# Privacy-Focused Mobile Apps and Stores

For Iranian users, the choice of mobile applications is not merely about convenience—it is a critical component of personal safety. The Islamic Republic’s digital ecosystem relies heavily on compromised local app stores and state-monitored "super-apps" to track citizens.

This guide provides a curated list of trusted, open-source, and privacy-focused alternatives to the tools commonly pushed by state actors. It focuses on minimizing data collection, bypassing the "Filternet" (censorship), and securing communications against interception.

---

## 1. Safe App Stores and Installation Sources

Using the right source to download apps is the first line of defense. Malicious updates are a common vector for state-sponsored malware.

### ⚠️ Danger Zone: Sources to Avoid

- **Cafe Bazaar & Myket:** These local Iranian app stores comply with state regulations. They have a history of serving "fake updates" to redirect payment gateways or install compromised versions of popular apps (e.g., Signal or Telegram). **Do not use them for sensitive applications.**
- **Direct APKs from Telegram Channels:** Unless verified against a developer's official fingerprint, APKs forwarded in Telegram channels are a high risk for malware injection.

### Recommended Sources (Android)

| Store                                                          | Type              | Best For                | Notes                                                                                                                                                                 |
| :------------------------------------------------------------- | :---------------- | :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Obtainium](https://github.com/ImranR98/Obtainium)**         | App Manager       | **Advanced Users**      | Downloads apps directly from the developer's GitHub/GitLab releases. Bypasses all store intermediaries. Highly recommended for apps like Signal or Tella.             |
| **[Aurora Store](https://auroraoss.com/)**                     | Play Store Client | **General Users**       | An anonymous interface for the Google Play Store. Allows you to download Play Store apps without a Google Account, reducing Google's tracking profile of your device. |
| **[F-Droid Basic](https://f-droid.org/)**                      | FOSS Repository   | **Privacy Enthusiasts** | A modern, faster client for F-Droid, the catalogue of Free and Open Source Software (FOSS). All apps here are tracker-free and open source.                           |
| **[GrapheneOS App Store](https://github.com/GrapheneOS/Apps)** | Specialized Repo  | **High Security**       | Provides specific hardened apps like the _Auditor_ and _Secure Camera_. Works on any Android 12+ device.                                                              |

> **Note for iOS Users:** You are generally restricted to the Apple App Store. To maintain privacy, ensure you use a dedicated Apple ID for your device that is not linked to your real identity or Iranian phone number if possible.

---

## 2. Privacy-Respecting Web Browsers

Your choice of browser determines how easily the government can track your internet activity or fingerprint your device.

### For Anonymity & Censorship Circumvention

- **[Tor Browser](https://www.torproject.org/download/) (Android)**: The gold standard for anonymity. It routes traffic through the Tor network, masking your IP address and bypassing local filtering.
  - _Iran Tip:_ You will likely need to configure **Bridges** (specifically **Snowflake** or **Meek-azure**) to connect to Tor from within Iran.
- **[Onion Browser](https://onionbrowser.com/) (iOS)**: The recommended Tor client for iPhone users.

### For Daily Use (Hardened Privacy)

- **[Mull](https://github.com/DivestOS/Mull-Fenix) (Android)**: A privacy-hardened fork of Firefox available on F-Droid. It strips out Mozilla's telemetry. Pair with **uBlock Origin** for maximum protection.
- **[Brave Browser](https://brave.com/) (Android/iOS)**: User-friendly and fast. Built-in ad and tracker blocking.
  - _Configuration:_ Go to Settings > Shields & Privacy. Set blocking to "Aggressive" and enable "Block Fingerprinting".
- **[Cromite](https://github.com/uazo/cromite) (Android)**: A fork of Chromium (like Chrome) but with all Google tracking removed and built-in adblocking. A good alternative if you prefer the Chrome interface but want privacy.

---

## 3. Secure Communication

State-monitored messengers like **Rubika**, **Eitaa**, **Soroush**, and **Bale** log every interaction. Avoid them entirely for private communication.

| App                                    | Status                 | Notes for Iranian Context                                                                                                                                                                          |
| :------------------------------------- | :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Signal](https://signal.org/)**      | **Recommended**        | The gold standard. Metadata is minimal. Use **Registration Lock** to prevent SIM swapping attacks. Use **Signal Proxy** to bypass blocking.                                                        |
| **[Briar](https://briarproject.org/)** | **Critical (Offline)** | A peer-to-peer messenger that works via **Bluetooth** and **Wi-Fi** without internet. Essential for **protests** and internet shutdowns (shutdown-proof).                                          |
| **Telegram**                           | **Use with Caution**   | extremely popular in Iran but **NOT** end-to-end encrypted by default. State actors can read "Saved Messages" and regular chats if they compromise your account. **Only "Secret Chats" are safe.** |
| **WhatsApp**                           | **Avoid if possible**  | Encrypted content, but leaks significant **metadata** (who you talk to, when, and where) to Meta/Facebook, which can be subpoenaed.                                                                |

---

## 4. Documentation & Physical Safety (Protests)

If you are documenting human rights violations or attending protests, standard camera apps are dangerous because they leave photos visible in your gallery.

- **[Tella](https://tella-app.org/) (Android/iOS)**: Designed specifically for activists.
  - **Encryption:** Photos/Videos taken in Tella are encrypted immediately and hidden from the main gallery.
  - **Camouflage:** You can change the app icon to look like a calculator or game.
  - **Quick Delete:** A panic button can wipe all sensitive data instantly.
- **[Scrambled Exif](https://f-droid.org/en/packages/com.jarsilio.android.scrambled.exif/) (Android)**: A utility to strip metadata (location, device model, time) from photos before you share them on social media.
- **[Magic Earth](https://www.magicearth.com/)**: A privacy-focused map app that allows offline navigation. Download the map of your city/region and use it in "Airplane Mode" to avoid location tracking via cell towers.

---

## 5. Account Security (2FA)

SMS 2-Step Verification is vulnerable to interception by Iranian mobile operators (MCI/Irancell). Use App-based Authenticators instead.

- **[Aegis Authenticator](https://getaegis.app/) (Android)**: Free, open-source, and secure. Allows encrypted backups of your 2FA codes (crucial if you lose your phone).
- **[Ente Auth](https://ente.io/auth/) (iOS/Android)**: The recommended open-source alternative for iOS users. Supports end-to-end encrypted backups and offline generation.
- **Avoid:** _Google Authenticator_ (limited backup security in some modes) and _Authy_ (history of breaches and lack of export options).

---

## 6. Utilities & System Hardening

- **[Shelter](https://gitea.angry.im/PeterCxy/Shelter) (Android)**: Uses the "Work Profile" feature to isolate apps. You can install invasive apps (like WhatsApp or Google Maps) inside Shelter and "freeze" them when not in use, preventing them from running in the background.
- **[NewPipe](https://newpipe.net/) (Android)**: A YouTube client that doesn't require a Google Account. It bypasses Google tracking while allowing you to subscribe to channels and download videos for offline viewing.
- **[Orbot](https://orbot.app/) (Android)**: A "VPN" mode that forces _other_ apps on your phone to route their traffic through Tor. Useful for forcing an app that is blocked to connect via Tor.

## 7. Health & Wellness

Reproductive health data is sensitive. Avoid apps that store data in the cloud.

- **[Drip](https://bloodyhealth.gitlab.io/)**: Open-source menstrual tracking. All data stays **locally** on your device.
- **[Euki](https://eukiapp.org/)**: Sexual health and reproductive tracker with strong privacy features (PIN protection, local storage).

---

## Summary of Best Practices for Iran

1.  **Delete Local Store Apps:** Uninstall Cafe Bazaar or Myket immediately.
2.  **Update Manually:** Use Obtainium or F-Droid Basic to keep apps updated. Outdated apps have security holes.
3.  **Segregate Identity:** Do not link your real Iranian phone number to Telegram or Signal if possible; use a virtual number or foreign SIM for high-risk accounts.
4.  **Disconnect:** During protests, turn off Mobile Data and use **Briar** or **Silence** (for encrypted SMS) to communicate.
