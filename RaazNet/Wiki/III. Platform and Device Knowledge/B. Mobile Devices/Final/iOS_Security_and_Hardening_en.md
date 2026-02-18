---
title: "iOS Security and Hardening"
tags:
  [
    ios,
    apple,
    mobile-security,
    privacy,
    surveillance,
    iran,
    hardening,
    encryption,
  ]
category: "Platform and Device Knowledge"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, High-Risk Users]
topics:
  [
    "Device Hardening",
    "Anti-Forensics",
    "Communication Security",
    "Surveillance Defense",
  ]
summary: "A comprehensive guide to securing iOS devices against interrogation, confiscation, and digital surveillance, tailored for the Iranian threat landscape."
source: "Raaznet Aggregated Resources"
content_type: "Configuration Guide"
security_level: "High"
language: "English"
prerequisites:
  ["iOS device running iOS 17 or later", "Basic familiarity with Settings"]
estimated_read_time: "20 minutes"
last_updated: "2026-02-18"
---

# iOS Security and Hardening

While iOS is widely regarded as a secure operating system due to its "walled garden" architecture and encrypted file system, it is not invincible. For Iranian users, the threat model includes physical device confiscation by security forces (Basij/IRGC), forced biometric unlocking, targeted spyware (such as Pegasus), and network-level interception.

This guide focuses on reducing the "attack surface" of your iPhone or iPad, preventing unauthorized access during confiscation, and minimizing data leakage to Apple or third parties.

---

## 1. Core System Security

### Update Immediately

Vulnerabilities in iOS are discovered frequently and sold to state actors to deploy spyware. Staying outdated is the single biggest risk.

- **Action:** Go to **Settings > General > Software Update**.
- **Configuration:** Enable **Automatic Updates** for "Security Responses & System Files."
- **Legacy Devices:** If your device no longer receives security updates (e.g., iPhone 7 or older), it is **unsafe** for sensitive activism work.

### Lockdown Mode (Crucial for High-Risk Users)

Introduced in iOS 16, Lockdown Mode is the most effective defense against "zero-click" spyware exploits (like those used by NSO Group) often deployed against activists.

- **What it does:** Blocks most message attachments, disables link previews, blocks incoming FaceTime from strangers, and disables complex web technologies.
- **How to enable:** **Settings > Privacy & Security > Lockdown Mode**.
- **Recommendation:** If you are an activist or journalist in Iran, keep this **Enabled** permanently.

### Stronger Passcodes (Disable 4/6 Digits)

Forensic tools used by law enforcement (such as GrayKey or Cellebrite) can brute-force 4 or 6-digit numeric codes relatively quickly.

- **Action:** **Settings > Face ID & Passcode > Change Passcode**.
- **Select:** **Passcode Options > Custom Alphanumeric Code**.
- **Guidance:** Create a passphrase that is at least 10 characters long, mixing letters and numbers.
  - _Bad:_ `135790`, `tehran123`
  - _Good:_ `Blue-Sky-Azadi-99!`

### Biometric Security (FaceID/TouchID)

In Iran, security forces frequently force detainees to look at their phones to unlock them.

- **Recommendation:** For high-risk scenarios (protests, border crossings), **disable biometrics** entirely and rely on your strong alphanumeric passphrase.
- **Emergency SOS (The "Panic" Button):** If you are being approached by police and cannot change settings, quickly press and hold the **Side button and either Volume button** (or press the Power button 5 times rapidly) until the slider appears. This **immediately disables FaceID** and forces a passcode entry to unlock.

### Stolen Device Protection

This feature adds a layer of security if your device is stolen _while unlocked_ or if the thief observed your passcode.

- **Action:** **Settings > Face ID & Passcode > Stolen Device Protection**.
- **Set to:** **Always** (Note: Default is "Away from Familiar Locations," but "Always" is safer if your home is raided).

---

## 2. Connectivity and Network Hardening

Reducing radio silence prevents tracking via "IMSI Catchers" (Stingrays) and prevents malicious Wi-Fi hotspots from capturing traffic.

### Disable "Auto-Join" and Wi-Fi/Bluetooth Properly

The Control Center (swiping down) does _not_ fully turn off Wi-Fi or Bluetooth; it only disconnects the current session. Radios remain active for tracking.

- **Action:** Turn off Wi-Fi and Bluetooth via the **Settings app**, not the Control Center, when moving through high-risk areas.
- **Wi-Fi Privacy:** **Settings > Wi-Fi > [Information Icon] > Private Wi-Fi Address > Fixed** or **Rotating**. This prevents tracking via MAC address.

### AirDrop and Name Leaks

Researchers have demonstrated that AirDrop can leak phone numbers and hashes identifying the user, which authorities can use to identify protesters in a crowd.

- **Action:** **Settings > General > AirDrop > Receiving Off**.
- **Device Name:** Change your device name to something generic (e.g., "iPhone") via **Settings > General > About > Name**. Do not use your real name.

### USB Restricted Mode

Prevents forensic tools from connecting to your device via the charging port if it has been locked for more than an hour.

- **Action:** **Settings > Face ID & Passcode**. Scroll down to "Allow Access When Locked" and ensure **Accessories** is **OFF**.

---

## 3. iCloud and Data Encryption

By default, Apple holds the encryption keys for your iCloud backups. If presented with a legal order (or if the account is compromised), Apple can decrypt your data. You must take control of the keys.

### Advanced Data Protection (ADP)

This is the single most important cloud setting. It implements end-to-end encryption (E2EE) for iCloud Backups, Photos, Notes, and Drive. Even Apple cannot access your data.

- **Action:** **Settings > [Your Name] > iCloud > Advanced Data Protection > Turn On**.
- **Requirement:** You will need a recovery contact or a recovery key (write this down and hide it safely). If you lose this key, your data is gone forever.

### Local Encrypted Backups

Given the slow and censored internet in Iran, and the risk of cloud metadata analysis:

- **Recommendation:** Disable iCloud Backup entirely. Instead, back up your iPhone to a computer (macOS or Windows) using a cable.
- **Crucial:** When backing up, select **"Encrypt local backup"** and set a strong password. This encrypts the file on your computer so that if the computer is seized, the backup remains unreadable.

### Find My iPhone

- **Pros:** Activation Lock prevents a thief/agent from wiping and reselling the phone.
- **Cons:** If your phone is confiscated, it broadcasts its location even when powered off (on newer models).
- **Verdict:** Keep enabled for theft protection, but be aware that a confiscated phone in a police station signals its location.

---

## 4. App Privacy and Permissions

### Location Services

Limit location access strictly.

- **Action:** **Settings > Privacy & Security > Location Services**.
- **System Services:** Scroll to the bottom > **System Services**. Turn **OFF**:
  - Significant Locations (tracks your daily routine).
  - iPhone Analytics.
  - Routing & Traffic.
  - Location-Based Suggestions.

### Photos Access

Never grant "Full Access" to apps like Instagram or Telegram if not absolutely necessary.

- **Action:** Set permissions to **"Limited Access"** or **"None"**.
- **Metadata:** When sharing photos, tap "Options" at the top of the share sheet and turn off **Location**.

### Keyboard Security

Third-party keyboards (Gboard, etc.) can transmit keystrokes.

- **Recommendation:** Use the standard iOS keyboard. If you require a custom keyboard, revoke its "Full Access" permission in settings, though this may break some features.

---

## 5. Internet and Browsing (Safari)

### Safari Hardening

- **Settings > Apps > Safari**:
  - **Search Engine Suggestions:** Off.
  - **Preload Top Hit:** Off (prevents background connections).
  - **Prevent Cross-Site Tracking:** On.
  - **Hide IP Address:** From Trackers.
  - **Fraudulent Website Warning:** **OFF**. (Note: This feature sends browsed URLs to Google/Apple for checking. In a privacy context, it is safer to disable this to prevent URL leakage).

### VPN Leakage Warning

iOS has a known architectural flaw where some Apple proprietary traffic (Push Notifications, Maps, etc.) may bypass an active VPN tunnel.

- **Mitigation:** There is no perfect fix on non-jailbroken iOS. Always use a reputable VPN with a "Kill Switch" enabled, but assume that Apple services can still see your true IP address.

---

## 6. Operational Security (OpSec) for Protests

If you are attending a demonstration or expect detention:

### The "BFU" State (Before First Unlock)

The most secure state for an iPhone is immediately after a restart, before the passcode has been entered. In this state, the encryption keys are evicted from memory.

- **Action:** If you are in danger of imminent arrest, **power off your phone**.
- **Why:** Forensic tools have a much harder time extracting data from a device in BFU state compared to "After First Unlock" (AFU).

### Siri and Voice Control

Voice assistants can be triggered accidentally or by adversaries.

- **Action:** **Settings > Siri & Search**. Turn **OFF** "Listen for...", "Press Side Button for Siri", and "Allow Siri When Locked".

### Notification Previews

Prevent officers from reading 2FA codes or Signal messages on the lock screen.

- **Action:** **Settings > Notifications > Show Previews > When Unlocked** (or Never).

---

## 7. Spyware Checks (Forensics)

If you suspect your device has been compromised by advanced spyware (e.g., you are a high-profile journalist receiving strange SMS links):

1.  **Sysdiagnose:** Trigger a log dump by holding **Power + Vol Up + Vol Down** simultaneously until you feel a vibration (about 0.5s). Wait 10 minutes.
2.  **External Scan:** Use a computer to run **MVT (Mobile Verification Toolkit)** by Amnesty International or **iMazing** (which uses MVT) to scan the backup or logs for "Indicators of Compromise" (IOCs).
3.  **Warning:** These tools are not perfect. If you are a target of state-sponsored spyware, the safest course of action is to **stop using the device immediately** and switch to a new phone and Apple ID.

---

## Summary Checklist

1.  [ ] **OS Updated** to the latest version.
2.  [ ] **Lockdown Mode** Enabled.
3.  [ ] **Passcode** changed to Alphanumeric (10+ characters).
4.  [ ] **FaceID** disabled (or SOS trigger practiced).
5.  [ ] **Advanced Data Protection** Enabled for iCloud.
6.  [ ] **AirDrop** set to "Receiving Off".
7.  [ ] **Lock Screen Accessories** disabled.
8.  [ ] **Notifications** hidden on Lock Screen.
