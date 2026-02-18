---
title: "Android Security and Hardening"
tags:
  [
    android,
    mobile-security,
    privacy,
    hardening,
    iran,
    censorship-circumvention,
    grapheneos,
    aurora-store,
    app-isolation,
  ]
category: "Platform and Device Knowledge"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "Android Security Model",
    "Device Hardening",
    "App Management",
    "Anti-Surveillance",
    "Iranian Context",
  ]
summary: "Comprehensive guide to securing Android devices for Iranian users, focusing on OS hardening, app isolation, safe software acquisition, and defenses against local surveillance."
source: "Raaznet Aggregated Resources"
content_type: "Configuration Guide"
security_level: "High"
language: "English"
last_updated: "2026-02-18"
prerequisites: ["Basic Android familiarity", "Access to device settings"]
estimated_read_time: "20 minutes"
---

# Android Security and Hardening

For Iranian users, securing an Android device is a dual challenge: protecting against global cyber threats and navigating the specific risks posed by the Islamic Republic's surveillance apparatus, internet censorship, and state-sponsored malware.

This guide outlines how to harden your Android device, manage applications securely in a restricted environment, and protect your data from physical and digital seizure.

---

## 1. The Android Security Model

Understanding the basics helps you make better decisions. Modern Android is built on strong security principles:

- **Sandboxing:** Every app runs in its own isolated area. A malicious calculator app cannot read your WhatsApp messages unless you explicitly grant it permission.
- **Verified Boot:** Ensures the operating system has not been tampered with. If malware tries to modify the core OS, the phone will refuse to boot. **Never unlock your bootloader unless you are installing a signed custom OS like GrapheneOS.**
- **Encryption:** Modern Android uses File-Based Encryption (FBE). Your data is unreadable without your passcode.

> **Warning for Iranian Users:** Rooting your device breaks this security model. Do not "root" your phone to bypass restrictions or install cheats. Rooting makes it significantly easier for state-sponsored malware (often disguised as VPNs or proxies) to gain total control over your device.

---

## 2. Device Selection and Operating Systems

### Recommended Hardware

If purchasing a new device, prioritize **Google Pixel** phones. They include the **Titan M2** security chip, which handles encryption and protects against physical attacks. They also support the installation of **GrapheneOS**, the gold standard for Android privacy.

### Operating System Choice

1.  **GrapheneOS (Best):** Available only for Pixel devices. It provides hardened security, a sandboxed version of Google Play, and rapid updates. It removes all Google tracking by default.
2.  **Stock Android (Good):** Standard Android on Pixel or Samsung devices (with Knox) is secure _if_ kept updated.
3.  **Avoid:** "Rooted" custom ROMs (like generic LineageOS builds without verified boot) or devices that have reached their End-of-Life (EOL) and no longer receive security patches.

---

## 3. Safe App Management in Iran

The Google Play Store is often filtered in Iran, leading users to unsafe third-party stores (like Cafe Bazaar or Myket) or direct Telegram downloads. These sources are rife with malware.

### A. How to Download Apps Safely

Do not use Iranian app stores for sensitive applications. Use these alternatives:

- **Aurora Store:** An anonymous client for the Google Play Store. It allows you to download apps directly from Google's servers without a Google account, bypassing some censorship blocks.
  - _Download from:_ [F-Droid](https://f-droid.org/packages/com.aurora.store/) or [GitLab](https://gitlab.com/AuroraOSS/AuroraStore).
- **Obtainium:** Allows you to install and update open-source apps directly from their releases page (GitHub/GitLab). This is excellent for tools like Signal, V2RayNG, or Tor Browser.
  - _Download from:_ [GitHub](https://github.com/ImranR98/Obtainium).
- **F-Droid Basic:** A repository of free and open-source software (FOSS). Use the "Basic" version for better security and automatic updates.
  - _Download from:_ [F-Droid.org](https://f-droid.org/).

### B. Isolating Domestic Apps (The "Shelter" Strategy)

Iranian citizens are often forced to install domestic apps for banking, ride-sharing (Snapp, Tapsi), or government services (Sejam). These apps may collect excessive data or contain surveillance code.

**Never run domestic Iranian apps in your main personal profile.**

1.  **Install [Shelter](https://gitea.angry.im/PeterCxy/Shelter):** This app uses Android's "Work Profile" feature to create a separate container on your phone.
2.  **Isolate:** Install all domestic apps (Snapp, Divar, Rubika, Eitaa, banking apps) _inside_ the Shelter (Work Profile).
3.  **Freeze:** Use Shelter to "Freeze" these apps when not in use. This prevents them from running in the background, tracking your location, or using the microphone.
4.  **Private Space (Android 15+):** If you have Android 15, use the native "Private Space" feature for even better isolation of sensitive apps.

---

## 4. Network Security and Censorship Circumvention

### A. VPN Configuration

A VPN is essential not just for bypassing censorship, but for encrypting traffic against ISP deep packet inspection (DPI).

1.  **Kill Switch:** Go to **Settings > Network & internet > VPN**. Click the gear icon next to your VPN. Enable **"Always-on VPN"** and **"Block connections without VPN"**. This ensures no data leaks if the VPN drops.
2.  **Avoid Free VPNs:** Most "Free VPNs" advertised on Telegram or Instagram are data-harvesting operations or state-affiliated honey pots. Use trusted tools like **V2RayNG**, **Hiddify**, or **Mullvad**.

### B. Private DNS

ISPs (MCI, Irancell) use DNS manipulation to block sites and log requests.

1.  Go to **Settings > Network & internet > Private DNS**.
2.  Select **Private DNS provider hostname**.
3.  Enter a trusted provider (e.g., `dns.quad9.net` or `1dot1dot1dot1.cloudflare-dns.com`). _Note: In times of severe internet throttling, standard encrypted DNS may be blocked, and you may need to rely on your VPN's DNS._

### C. Disable 2G (Prevention of SMS Interception)

State actors use cell-site simulators (Stingrays) to downgrade connections to 2G, allowing them to intercept SMS (including 2FA codes).

- **Android 12+:** Go to **Settings > Network & internet > SIMs > Allow 2G** and toggle it **OFF**.

---

## 5. Privacy Configuration

### A. Permissions Audit

Regularly check **Settings > Privacy > Permission Manager**.

- **Location:** Set to "While Using the App" or "Never". Never grant "All the time" to domestic apps.
- **Microphone/Camera:** Revoke access for any app that doesn't strictly need it.
- **Sensors:** Android 10+ allows you to disable all sensors (mic, camera, GPS, gyroscope) via a Developer Tile.
  - _Enable Developer Options (Tap Build Number 7 times) > System > Developer Options > Quick settings developer tiles > Sensors Off._ This adds a button to your Quick Settings to instantly kill all sensors.

### B. Google Settings (Stock Android)

If you are not using GrapheneOS, harden Google Play Services:

1.  **Delete Advertising ID:** **Settings > Privacy > Ads > Delete advertising ID**. This breaks the profile advertisers and trackers build of you.
2.  **Turn off Location History:** **Settings > Location > Location Services > Google Location History**.

---

## 6. Physical Security and Border Crossings

In Iran, device seizure by plainclothes officers (Basij) or at checkpoints is a real threat.

### A. Encryption and Passwords

- **Strong Passphrase:** Use a 10+ character alphanumeric passphrase. Do not use a 4 or 6-digit PIN.
- **Disable Biometrics:** Fingerprint and Face Unlock can be forced. Disable them before attending protests or crossing borders.
  - _Emergency:_ Hold the Power button and select **"Lockdown"** (if enabled in settings) to instantly disable biometrics and hide notifications on the lock screen.

### B. Before First Unlock (BFU)

When your phone is fully powered off and then turned on, it is in a "Before First Unlock" state. In this state, your data is fully encrypted and encryption keys are not in memory.

- **Recommendation:** If you are approaching a checkpoint or expect a seizure, **power off your device completely**. A powered-off phone is significantly harder to forensically examine than a phone that is merely locked.

### C. Hidden Apps and Data

- **User Profiles:** Create a secondary "Guest" or "Travel" user profile (**Settings > System > Multiple Users**) with innocuous apps installed. If forced to unlock your phone, log into this clean profile.
- **Note:** Forensic tools (like Cellebrite) can detect multiple users. This strategy works against quick manual searches by officers on the street, not detailed forensic labs.

---

## 7. Specific Iranian Threat Mitigations

### A. SMS Phishing (Smishing)

A primary vector for compromising Iranian Android devices is fake SMS messages claiming to be from the Judiciary (Sana), Registry (Sejam), or Post Office. These contain links to download malware.

- **Rule:** Never click links in SMS. Government agencies generally do not send links via SMS numbers.
- **Defense:** If you accidentally download an APK from an SMS link, **do not install it**. If installed, perform a Factory Reset immediately.

### B. "Stalkerware" and Family Tracking

State-sponsored malware often masquerades as "Family Locators" or "Parental Control" apps. Periodically audit your **Device Admin Apps** (**Settings > Apps > Special app access > Device admin apps**). If you see anything you don't recognize having "Admin" privileges, revoke it and uninstall immediately.

### C. Dealing with Confiscation

If your device is confiscated:

1.  Assume it is compromised. Even if returned, it may have rootkits installed.
2.  Use **Find My Device** (if enabled and safe to do so) to remote wipe it.
3.  Revoke all active sessions (Telegram, Instagram, Google) from a secure computer immediately.

---

## 8. Summary Checklist for Hardening

| Priority        | Action                                                              |
| :-------------- | :------------------------------------------------------------------ |
| 🔴 **Critical** | Set a strong alphanumeric passphrase (10+ chars).                   |
| 🔴 **Critical** | Install **Shelter** and isolate all Iranian domestic apps.          |
| 🔴 **Critical** | Configure VPN with "Always-on" and "Block connections without VPN". |
| 🔴 **Critical** | Disable 2G connectivity to prevent SMS interception.                |
| 🟠 **High**     | Switch to **Aurora Store** and **Obtainium**; avoid Cafe Bazaar.    |
| 🟠 **High**     | Delete Advertising ID.                                              |
| 🟡 **Medium**   | Enable "Sensors Off" tile for quick privacy.                        |
| 🟡 **Medium**   | Switch default browser to **Brave** or **Mull** (hardened Firefox). |

---

_Sources:_

- _Privacy Guides: Android Overview & Hardening_
- _Certfa: Mobile Security & SIM Swapping_
- _Security in a Box: Protect Your Android Device_
- _Tactical Tech: Mobile Safety for Activists_
