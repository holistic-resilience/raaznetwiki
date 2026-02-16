---
title: "Backup and Recovery Strategies"
tags:
  [
    backup,
    data-recovery,
    encryption,
    3-2-1-rule,
    digital-resilience,
    iran-security,
    signal-backup,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  ["Data Backup", "Disaster Recovery", "Encrypted Storage", "Mobile Security"]
summary: "Comprehensive guide to creating resilient, encrypted backup strategies tailored for the Iranian context, including defense against device seizure and internet blackouts."
source: "Consolidated from Security in a Box, Privacy Guides, and Freedom of the Press Foundation"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites: ["Basic file management", "Familiarity with encryption tools"]
estimated_read_time: "15 minutes"
---

# Backup and Recovery Strategies

A backup strategy is not just about preventing data loss from accidental deletion; it is a critical defense against **device seizure**, **ransomware**, **internet blackouts**, and **state surveillance**.

If your device is confiscated by security forces (IRGC, FATA) or if the National Information Network (SHOMA) cuts off access to international cloud services, your ability to recover your digital life depends entirely on the strategy you implement _today_.

---

## The Golden Rule: 3-2-1 (Adapted for Iran)

The standard "3-2-1 Rule" states you should have 3 copies of data, on 2 different media, with 1 offsite. For Iranian users, we modify this to prioritize **encryption** and **accessibility during blackouts**.

1.  **3 Copies:** One primary (your device) + Two backups.
2.  **2 Media Types:** Example: Your laptop's internal drive + An external USB/Hard Drive.
3.  **1 _Encrypted_ Offsite:**
    - **Cloud:** Secure cloud storage (accessible only via VPN).
    - **Physical Offsite:** A hidden, encrypted USB drive stored at a trusted relative's house (crucial if the internet is shut down).

> **Warning:** Never store "offsite" backups in plain text. If a cloud provider is compromised or a physical drive is found, the data must be mathematically unreadable.

---

## Phase 1: Preparation and Mapping

You cannot back up what you do not track. Before installing tools, identify your assets.

### classify Your Data

- **Irreplaceable:** Family photos, unique work documents, research.
- **Recoverable:** Operating system files, downloaded applications (can be re-downloaded).
- **Sensitive:** ID documents, private chats, political writings.

### The "Primary Copy" Trap

Identify where your _newest_ work lives. If you edit a document on a USB drive at an internet cafe, that USB is now the **primary** copy. If you lose it, you lose the work, even if you have an old version on your laptop.

---

## Phase 2: Local Backups (The Offline Lifeline)

Local backups are your best defense against internet shutdowns.

### 1. Hardware Selection

- **USB Drives:** Easy to hide (sewn into clothes, hidden in household objects).
- **External SSDs:** Faster and more durable than HDDs.
- **MicroSD Cards:** Extremely easy to conceal.

### 2. Mandatory Encryption

**Never** copy files to an external drive without encryption. If physically seized, an unencrypted backup is a goldmine for interrogators.

- **VeraCrypt:** The gold standard for creating encrypted "containers" or encrypting entire drives.
  - _Strategy:_ Create a VeraCrypt container file (e.g., `system_data.hc`) on your USB drive. Mount it, drag your files in, and unmount. To an outsider, it looks like a random corrupt file.
  - _Plausible Deniability:_ VeraCrypt offers hidden volumes, allowing you to reveal a "decoy" partition while keeping the real data hidden.
- **LUKS (Linux):** Native full-disk encryption for Linux users.
- **BitLocker (Windows):** Better than nothing, but closed-source. Avoid if possible for highly sensitive data; prefer VeraCrypt.

### 3. Physical OpSec

- Do not label drives "Backups" or "Private."
- Store the backup drive in a location separate from your computer. If a raid occurs, they will take everything on your desk.

---

## Phase 3: Cloud Backups (The Offsite Lifeline)

Cloud backups protect you from fire, theft, or total house raids. However, in Iran, you face two risks: **blocking** (service becomes unreachable) and **trust** (provider snooping).

### Strategy A: Encrypted Providers

Use services that offer Zero-Knowledge / End-to-End Encryption (E2EE) by default. The provider cannot read your data.

- **Proton Drive:** Swiss-based, high security. _Note: Frequently throttled in Iran; requires a reliable VPN._
- **Filen:** German-based, strong E2EE.
- **Tresorit:** High security, expensive.

### Strategy B: The "Cloud Container"

If specialized privacy services are blocked, use major providers (Google Drive, OneDrive, Dropbox) **only as a dumb storage box**.

1.  Use **Cryptomator** to create an encrypted vault on your local machine.
2.  Place your files inside the Cryptomator vault.
3.  Sync the _locked_ vault files to Google Drive/Dropbox.
4.  **Result:** Google sees only encrypted nonsense. You get the speed and availability of Google's infrastructure without giving them your data.

> **Note on Internet Shutdowns:** Cloud backups are useless during a total blackout. Always maintain a Local Backup (Phase 2).

---

## Phase 4: Mobile & Messenger Backups

Mobile data is often the most vulnerable during an arrest.

### Signal (Critical)

Signal messages are **not** stored on Signal's servers. If you lose your phone, you lose your chats unless you have a backup.

- **Android:**
  1.  Settings > Chats > Chat backups > **Turn On**.
  2.  **Write down the 30-digit passphrase.** This is the _only_ key to your data.
  3.  A backup file is created on your phone.
  4.  **Crucial Step:** Move this file off your phone (to a PC or USB) regularly. If the phone is seized, the internal backup is lost with it.
- **iOS:** Signal iOS allows transferring data to a new device or iPad/Mac, but does not support traditional file-based backups like Android.

### 2FA Authenticator Apps

Losing your 2FA codes means losing access to your accounts.

- **Avoid SMS 2FA:** Iranian telcos can intercept SMS.
- **Avoid Authy:** Requires a phone number, which links to your identity.
- **Use Aegis (Android) or Ente Auth (iOS/Android):** Open-source apps that allow you to export an _encrypted_ backup of your 2FA seeds. Store this backup on your VeraCrypt drive.

### Photos

- **Ente Photos:** An E2EE alternative to Google Photos.
- **Manual Method:** Regularly transfer photos to your encrypted computer/USB and delete them from the phone (or move them to a Hidden Folder if deletion isn't an option).

---

## Phase 5: Recovery and Testing

A backup is a failure until you have successfully restored from it.

1.  **The Drill:** Once a month, pretend you have lost your laptop.
2.  **The Test:** Take your backup USB, plug it into a different machine, and try to open a critical file (e.g., a scanned ID or a thesis).
3.  **The Fix:** If the file is corrupt or the password doesn't work, fix the process immediately.

---

## Comparison of Tools

| Tool             | Type       | Best For           | Iranian Context Note                                                    |
| :--------------- | :--------- | :----------------- | :---------------------------------------------------------------------- |
| **VeraCrypt**    | Encryption | USB/HDD Encryption | Essential. Use "Hidden Volume" feature for high-risk situations.        |
| **Cryptomator**  | Encryption | Cloud Security     | Use this to safely use Google Drive/Dropbox.                            |
| **Syncthing**    | Sync       | P2P Sync           | Great for syncing between phone/laptop on local Wi-Fi without internet. |
| **Proton Drive** | Cloud      | Easy E2EE          | Good, but have a VPN ready as it may be filtered.                       |
| **Aegis**        | Mobile     | 2FA Backup         | Superior to Google Auth/Authy. Open source & offline.                   |

## Emergency Deletion

If you are in immediate danger of a raid, you may need to destroy your data rather than save it. Please refer to **[[Secure_Data_Deletion]]** for instructions on wiping drives and destroying physical media.
