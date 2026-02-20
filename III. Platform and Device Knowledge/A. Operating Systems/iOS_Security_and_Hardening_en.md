---
title: "iOS Security and Hardening"
tags:
  [
    ios,
    mobile-security,
    privacy,
    hardening,
    apple,
    surveillance-circumvention,
    iran,
    anti-forensics,
  ]
category: "Device Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "iOS Security",
    "Device Hardening",
    "Anti-Forensics",
    "Privacy Settings",
    "Censorship Circumvention",
  ]
summary: "Comprehensive guide to securing iOS devices against state surveillance, physical seizure, and censorship, tailored for the Iranian context."
source: "Raaznet"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  ["iOS 17 or later recommended", "Basic familiarity with iOS Settings"]
estimated_read_time: "20 minutes"
last_updated: "2026-02-18"
---

# iOS Security and Hardening

Securing an iOS device requires balancing protection against two distinct threats: **remote surveillance** (state-sponsored spyware, traffic interception) and **physical access** (device seizure by security forces). While iOS is generally secure, the "walled garden" approach presents unique challenges in Iran due to sanctions and censorship, often forcing users into risky behaviors like installing dangerous certificates to access local apps.

This guide details how to harden your iPhone against these specific threats.

---

## 1. Core Security & Updates

### Keep iOS Updated

State-sponsored spyware often relies on "zero-day" or "N-day" exploits—vulnerabilities that Apple patches in updates. Running an outdated iOS version makes you an easy target.

- **Action:** Go to **Settings > General > Software Update**.
- **Enable Automatic Updates:** Turn on "Download iOS Updates", "Install iOS Updates", and "Security Responses & System Files".
- **Legacy Devices:** If your device no longer receives iOS updates (e.g., iPhone X or older), it is unsafe for sensitive work.

### Enable Lockdown Mode (Critical for High-Risk Users)

If you are an activist, journalist, or political target, **Lockdown Mode** is your strongest defense against mercenary spyware (like Pegasus or Predator). It reduces the "attack surface" of your phone by blocking complex web technologies, message attachments, and unsolicited calls.

- **Action:** Go to **Settings > Privacy & Security > Lockdown Mode** and tap **Turn On Lockdown Mode**.
- **Trade-offs:** Some web pages may load slowly, and you cannot receive attachments in Messages from unknown senders.

---

## 2. Physical Security & Anti-Forensics

In Iran, the risk of device confiscation at checkpoints or during arrest is high. You must configure your device to resist forensic extraction tools (like Cellebrite).

### Passcode Strength

A 4 or 6-digit PIN can be brute-forced by forensic tools in minutes or hours. You need an **Alphanumeric Passphrase**.

- **Action:** **Settings > Face ID & Passcode > Change Passcode > Passcode Options > Custom Alphanumeric Code**.
- **Recommendation:** Use a sentence or random phrase (minimum 7-10 words/characters) that includes letters and numbers.

### Managing Biometrics (Face ID / Touch ID)

Biometrics are convenient but dangerous if you are detained, as security forces may force you to look at your phone or press your finger against it.

- **Option A (Safest):** Disable biometrics entirely and rely only on your alphanumeric passphrase.
- **Option B (Daily Use):** Keep Face ID enabled but learn the **Panic Button** (SOS) command to instantly disable it.

> **How to "Panic Disable" Face ID:**
> Hold the **Power button** and **either Volume button** simultaneously for 3 seconds until the slide-to-power-off screen appears. This creates a "BFU" (Before First Unlock) state for biometrics, requiring your passcode to re-enable them. Do this _immediately_ if approaching a checkpoint.

### Stolen Device Protection

Introduced in recent iOS versions, this feature adds a security delay when changing settings (like your Apple ID password) away from familiar locations.

- **Action:** **Settings > Face ID & Passcode > Stolen Device Protection > On**.

### USB Restricted Mode

Prevents forensic tools from connecting to your iPhone via the charging port if it has been locked for more than an hour.

- **Action:** **Settings > Face ID & Passcode**. Scroll down to "Allow Access When Locked" and ensure **Accessories** is **OFF**.

---

## 3. The "Enterprise Certificate" Trap (Iran-Specific)

Due to Apple App Store sanctions, many Iranian apps (banking, Snapp, ride-sharing) ask users to install "Enterprise Profiles" or "Root Certificates" to bypass restrictions.

**⚠️ WARNING: Do NOT install these profiles.**

Installing a configuration profile or root certificate from an untrusted source allows the creator to:

1.  **Intercept your encrypted traffic** (Man-in-the-Middle attack).
2.  **Push malicious apps** to your device without review.
3.  **Remotely wipe or manage** your device.

**Safe Alternative: Progressive Web Apps (PWAs)**
Most Iranian services offer a web version that functions like an app without the security risk.

1.  Open **Safari** and navigate to the service's website (e.g., the web version of your bank or ride-sharing service).
2.  Tap the **Share** icon (square with arrow).
3.  Select **Add to Home Screen**.
4.  This creates an app icon that runs safely in a browser sandbox.

---

## 4. iCloud & Data Privacy

Apple holds the encryption keys for standard iCloud backups, meaning they could technically be compelled to hand over data. You must take control of your keys.

### Advanced Data Protection (ADP)

ADP enables end-to-end encryption (E2EE) for iCloud Backups, Photos, Notes, and Drive. Even Apple cannot access your data.

- **Action:** **Settings > [Your Name] > iCloud > Advanced Data Protection > Turn On**.
- **Recovery Key:** You will be forced to set up a Recovery Key. **Write this down and hide it.** If you lose this key and your password, your data is gone forever.

### Local Backups (Alternative)

If you cannot use ADP (e.g., region restrictions or shared family account issues), disable iCloud Backup and back up locally to a computer using iTunes/Finder.

- **Action:** When backing up, check **"Encrypt local backup"** and set a strong password. This encrypts the backup so that even forensic extraction of the computer cannot easily read the iPhone data.

---

## 5. Network Privacy & Circumvention

### Wi-Fi Privacy

Prevent Wi-Fi networks (cafes, universities) from tracking your device across sessions.

- **Action:** **Settings > Wi-Fi > [Tap 'i' on network] > Private Wi-Fi Address > Fixed** (or "Rotating" in iOS 18+).

### Lockdown AirDrop

AirDrop can leak your identity (phone number hash) to anyone nearby.

- **Action:** **Settings > General > AirDrop > Receiving Off**. Only enable it temporarily when needed.

### VPN Configuration

A VPN is essential for bypassing censorship.

- **Kill Switch:** iOS does _not_ offer a true, system-wide permanent kill switch for third-party VPN apps. Some traffic (Apple services) may leak.
- **Recommendation:** Use a reputable protocol like **V2Ray**, **WireGuard**, or **OpenVPN**. Avoid "Free VPNs" on the App Store that collect data.

---

## 6. App Permissions & Hygiene

### Review Sensitive Permissions

Go to **Settings > Privacy & Security** and review:

- **Location Services:** Set to "Never" or "While Using" for all apps. Disable "Precise Location" unless necessary for navigation.
- **Tracking:** **Settings > Privacy & Security > Tracking > Allow Apps to Request to Track > OFF**.
- **Microphone/Camera:** Revoke access for any app that doesn't strictly need it.

### Keyboard Security

Third-party keyboards (Gboard, custom Persian keyboards) can technically log keystrokes if "Full Access" is granted.

- **Recommendation:** Use the stock Apple keyboard. It processes data on-device and supports Persian fully. If you must use a third-party keyboard, deny it "Full Access" in settings, though this limits functionality.

---

## 7. Emergency Procedures

### The "BFU" Reboot

If you are traveling or expect a high risk of seizure, **power off your phone**.

- A phone that has been powered off and restarted but _not yet unlocked_ is in **BFU (Before First Unlock)** state.
- In BFU, encryption keys are evicted from memory. Forensic tools find it significantly harder (often impossible) to extract data from a device in BFU compared to AFU (After First Unlock).

### Erase Data Option

You can set your phone to wipe itself after 10 failed passcode attempts.

- **Action:** **Settings > Face ID & Passcode > Erase Data**.
- **Risk:** A malicious actor could intentionally trigger this to destroy your data. Enable only if you have secure backups and the risk of data compromise outweighs the risk of data loss.

---

## Checklist for Iranian Users

| Action                              | Priority           | Impact                                             |
| :---------------------------------- | :----------------- | :------------------------------------------------- |
| **Update iOS**                      | Critical           | Patches security holes used by spyware.            |
| **Enable Lockdown Mode**            | High               | Blocks sophisticated attack vectors.               |
| **Set Alphanumeric Passcode**       | Critical           | Prevents brute-force access.                       |
| **Enable Advanced Data Protection** | High               | Encrypts iCloud data against Apple/Legal requests. |
| **Remove "Enterprise Profiles"**    | Critical           | Prevents traffic interception/malicious apps.      |
| **Disable AirDrop Receiving**       | Medium             | Prevents identity leakage in public.               |
| **Reboot to BFU**                   | High (Situational) | Protects data during transport/checkpoints.        |
