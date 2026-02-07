---
title: "Encryption at Rest and Storage Security"
tags:
  [
    encryption,
    data-at-rest,
    veracrypt,
    cryptomator,
    full-disk-encryption,
    mobile-security,
    digital-privacy,
    iran-security,
  ]
category: "Technical Foundations"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public in Iran]
topics:
  [
    "Disk Encryption",
    "File Encryption",
    "Mobile Device Security",
    "Plausible Deniability",
  ]
summary: "A comprehensive guide to protecting digital data stored on devices against physical seizure and forensic analysis, tailored for the Iranian threat landscape."
source: "Raaznet Aggregation"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic operating system knowledge",
    "Understanding of passwords vs. encryption",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-06"
---

# Encryption at Rest and Storage Security

In the context of digital security in Iran, the threat is not limited to remote interception of data over the internet. Physical seizure of devices—whether during a street checkpoint, a house raid by security forces, or confiscation at borders—is a primary risk.

**Encryption at Rest** ensures that even if your laptop, phone, or hard drive is physically stolen or seized by the Cyber Police (FATA) or other agents, the data remains unreadable without the decryption key (passphrase).

## The Core Concept: At Rest vs. In Transit

- **Data in Transit:** Information moving through the internet (e.g., a Signal message sending). Protected by TLS/SSL and End-to-End protocols.
- **Data at Rest:** Information stored on a hard drive, flash memory, or cloud server. Protected by **Disk and File Encryption**.

> **Critical Warning for Iranian Users:** Encryption protects your data mathematically. However, it does not protect you from "rubber-hose cryptanalysis" (coercion or torture to reveal passwords). Where possible, use **Plausible Deniability** (Hidden Volumes) and **Duress Passwords**.

---

## 1. Full Disk Encryption (FDE)

FDE encrypts the entire storage drive. Without the password, the operating system cannot even boot, and files cannot be accessed by mounting the drive on another computer.

### Windows: VeraCrypt (Recommended) vs. BitLocker

While Windows Pro/Enterprise includes **BitLocker**, it is closed-source and, on "Home" editions, often automatically uploads recovery keys to Microsoft servers (which poses a privacy risk).

**Raaznet Recommendation:** Use **VeraCrypt** for maximum security.

- **Type:** Open Source.
- **Audit Status:** Independently audited.
- **Key Feature:** Supports Hidden Operating Systems (Plausible Deniability).

**How to use VeraCrypt for System Encryption:**

1.  Download from the [official website](https://veracrypt.fr/).
2.  Select "Encrypt the System Partition/Drive."
3.  **Hash Algorithm:** Select SHA-512.
4.  **Encryption:** Select AES.
5.  **PIM (Personal Iterations Multiplier):** Increase this value to make brute-force attacks harder, though it slows down boot time.

### macOS: FileVault

macOS users should enable **FileVault** immediately.

- **Go to:** System Settings > Privacy & Security > FileVault.
- **Key Management:** Do **not** allow your iCloud account to unlock your disk. Choose to create a "Local Recovery Key" and store it physically safe (not with the device).

### Linux: LUKS

The Linux Unified Key Setup (LUKS) is the standard for Linux distributions.

- **Setup:** Best configured during the installation of the OS (e.g., Ubuntu, Fedora, Debian).
- **Security:** Ensure your `/boot` partition is also secured or that you are aware of "Evil Maid" attack vectors, though FDE is sufficient for most seizure scenarios.

---

## 2. Mobile Device Security

Smartphones are the most commonly seized devices in Iran. Modern Android and iOS devices are encrypted by default, _but_ this encryption is only as strong as your passcode and settings.

### Secure Your Screen Lock

- **Disable Biometrics:** FaceID and Fingerprint scanners can be forced open by agents physically holding the device or forcing your finger onto the sensor. **Use a strong alphanumeric passphrase instead.**
- **Disable Smart Lock (Android):** Ensure your phone does not stay unlocked when connected to a "trusted" Bluetooth device or location.

### Android: Specialized Configurations

- **BFU (Before First Unlock):** When an Android phone is rebooted, it is in a "BFU" state. Data is heavily encrypted. Once you unlock it once (AFU - After First Unlock), keys are loaded into memory.
  - _OpSec Advice:_ If you are approaching a high-risk area (protest zone, checkpoint), **power off your phone completely**.
- **Molly (Signal Fork):**
  - While Signal encrypts messages in transit, the database on your phone is often accessible if the phone is unlocked.
  - **Molly** (an open-source fork of Signal) allows you to encrypt the local database with a separate passphrase. This means even if your phone is unlocked, your messages remain encrypted.

### iOS: Lockdown Mode

- Enable **Lockdown Mode** (iOS 16+) if you are a high-risk target (journalist, activist). It reduces the attack surface for sophisticated spyware like Pegasus.

---

## 3. Container and Cloud Encryption

If you must use cloud storage (Google Drive, Dropbox) or transfer files via USB, never upload or transfer "naked" files.

### Cryptomator (For Cloud Storage)

Cloud providers (Google, Microsoft) have access to your data. To prevent this:

1.  Install **Cryptomator** (Open Source).
2.  Create a "Vault" inside your cloud sync folder.
3.  Cryptomator encrypts files _before_ they sync to the cloud.
4.  **Result:** The cloud provider only sees encrypted gibberish. They cannot see file contents or filenames.

### VeraCrypt Containers (For USB/Storage)

Instead of encrypting a whole drive, you can create a file container.

- This looks like a random file (e.g., `movie.mp4` or `data.dat`) but acts as a virtual encrypted disk when mounted in VeraCrypt.
- **Hidden Volumes:** You can create a specialized container with two passwords.
  - **Password A:** Opens a "Decoy" volume (safe, non-sensitive files).
  - **Password B:** Opens the "Hidden" volume (sensitive files).
  - _Scenario:_ If forced to give a password, give Password A. It is mathematically impossible to prove the Hidden volume exists.

---

## 4. Encrypted Backups

Losing a device to seizure often means losing the data permanently if you don't have backups. However, backups are a security vulnerability if not encrypted.

### Signal Secure Backups

Signal messages are stored locally.

1.  Go to **Settings > Chats > Chat backups**.
2.  Enable backups.
3.  **Write down the 30-digit passphrase.**
4.  Store the backup file off the device (e.g., on a computer or USB).
5.  _Note:_ Without the passphrase, the backup is useless. Signal (the organization) cannot recover it for you.

### Zero-Knowledge Cloud Storage

Consider moving away from Google Drive for sensitive documents. Use providers that offer Zero-Access encryption by default:

- **Proton Drive:** Swiss-based, end-to-end encrypted.
- **Filen:** Highly secure, open-source architecture.
- **Sync.com:** Canadian-based zero-knowledge storage.

---

## 5. Metadata and File Sanitation

Encryption hides the _content_, but sometimes the file structure or metadata remains.

- **Metadata:** Information about the data (Author name, GPS location in photos, creation date).
- **Sanitization:** Before storing sensitive photos or documents in a long-term archive, remove metadata.
  - **Tools:** ExifTool, Scrambled Exif (Android), or the "Remove Properties" feature in Windows.

## 6. Secure Deletion

Deleting a file (moving to Trash) does not remove it from the disk; it just marks the space as "available." Forensic tools used by Iranian authorities can recover these files.

- **Solid State Drives (SSDs) & Flash Memory:** Modern SSDs use "TRIM," which makes secure wiping difficult. The only way to securely delete data on an SSD is **Full Disk Encryption**. If the drive is encrypted and you "forget" the key, the data is effectively erased.
- **Mechanical Hard Drives (HDDs):** Use tools like `BleachBit` or the `shred` command (Linux) to overwrite data.
  - Command: `shred -u -z -n 3 filename` (Overwrites 3 times, zeroes it, and removes the file).

## Summary Checklist for Iranian Users

| Priority     | Action                      | Tool/Method                                                      |
| :----------- | :-------------------------- | :--------------------------------------------------------------- |
| **Critical** | Encrypt Computer Hard Drive | VeraCrypt (Windows) / FileVault (macOS) / LUKS (Linux)           |
| **Critical** | Secure Phone Screen Lock    | Disable Biometrics; Use 6+ digit/alphanumeric code               |
| **High**     | Encrypt Cloud Files         | Cryptomator                                                      |
| **High**     | Secure Message Storage      | Use **Molly** (Android) or enable Disappearing Messages (Signal) |
| **High**     | Travel OpSec                | Power off devices completely before checkpoints (BFU state)      |
| **Advanced** | Plausible Deniability       | VeraCrypt Hidden Volumes                                         |

---

_Disclaimer: Security is a moving target. While these tools provide strong protection, no system is 100% invulnerable. Assess your personal risk level and stay updated on the latest circumventing technologies used by state actors._
