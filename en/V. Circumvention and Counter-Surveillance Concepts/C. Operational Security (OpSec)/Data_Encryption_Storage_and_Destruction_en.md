---
title: "Data Encryption, Storage, and Destruction"
tags:
  [
    data-security,
    encryption,
    backups,
    secure-deletion,
    veracrypt,
    metadata,
    digital-privacy,
    iran-security,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "Full Disk Encryption",
    "Secure Backups",
    "Data Sanitization",
    "Secure Deletion",
    "Hidden Volumes",
  ]
summary: "Comprehensive guide to protecting data at rest through encryption, managing secure backups, scrubbing metadata, and permanently destroying sensitive information to prevent forensic recovery."
source: "Raaznet Wiki"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic computer literacy",
    "Administrator access to devices",
    "Understanding of file systems",
  ]
estimated_read_time: "20 minutes"
---

# Data Encryption, Storage, and Destruction

Where device confiscation at checkpoints, border crossings, or during raids is a tangible threat, protecting data "at rest" (data stored on your device) is as critical as protecting data "in transit" (internet traffic).

This guide covers the lifecycle of sensitive data: how to lock it so only you can read it (**Encryption**), how to keep safe copies (**Storage & Backup**), how to clean hidden details (**Sanitization**), and how to ensure it is gone forever when you delete it (**Destruction**).

---

## 1. Data Encryption

Encryption scrambles your information using advanced mathematics. Without the correct password or key, the data looks like random noise. This is your primary defense if your laptop or phone is seized by authorities.

### Full-Disk Encryption (FDE)

FDE encrypts everything on your device. It functions best when the device is **completely powered off** (BFU - Before First Unlock). If your device is in sleep mode (AFU - After First Unlock), encryption keys are in memory and can potentially be extracted by forensic tools used by security agencies.

- **Android:** Encrypted by default on modern devices (Android 10+). Ensure you use a strong **passphrase** (not a pattern or short PIN).
- **iOS:** Encrypted by default once a passcode is set. Use a 6-digit PIN or, preferably, an alphanumeric passphrase. Enable "Erase Data" after 10 failed attempts if you have secure backups.
- **Windows:** Use **BitLocker** (Pro/Enterprise editions) or **Device Encryption** (Home edition). Ensure a TPM chip is enabled.
- **macOS:** Enable **FileVault** in System Settings > Privacy & Security.
- **Linux:** Enable **LUKS** encryption during the installation of your distribution (e.g., Ubuntu).

> **Iran Context:** Authorities may pressure you to unlock your device. Biometric unlock (FaceID/Fingerprint) is less legally secure than a passcode because it can be forced physically. **Disable biometrics** before entering high-risk areas (protests, borders).

### Encrypted Containers & External Drives

For highly sensitive files, do not rely solely on FDE. Use specialized tools to create encrypted "vaults" or to encrypt USB drives.

#### VeraCrypt

[VeraCrypt](https://veracrypt.io/) is the gold standard for cross-platform encryption (Windows, macOS, Linux).

- **Standard Volume:** Creates an encrypted file container that acts like a virtual USB drive.
- **Hidden Volume:** Crucial for high-risk threat models. It hides a secret volume _inside_ a standard volume. If forced to reveal your password, you can reveal the password for the "decoy" data, leaving the sensitive data undetectable.
  - _Usage:_ Keep non-sensitive, plausible personal data in the outer volume. Keep sensitive activist material in the hidden volume.

#### Cryptomator

[Cryptomator](https://cryptomator.org/) is ideal for encrypting files _before_ uploading them to cloud storage (Google Drive, Dropbox, etc.). Unlike VeraCrypt, it encrypts individual files, meaning you don't have to re-upload a massive container every time you change one document.

---

## 2. Secure Data Storage and Backups

Data loss can occur due to seizure, hardware failure, or malware. A robust backup strategy is essential, but backups must be as secure as the originals.

### The Backup Strategy

Follow an adapted **3-2-1 Rule**:

- **3** copies of your data.
- **2** different media types (e.g., laptop drive + external SSD).
- **1** off-site location (e.g., secure cloud or a drive stored at a trusted friend's house).

**Crucial:** All backups containing sensitive data **must be encrypted**.

### Secure Cloud Storage

Avoid storing sensitive data on unencrypted clouds like standard Google Drive, Dropbox, or iCloud (unless Advanced Data Protection is on), as these providers can access your data or hand it over to governments upon legal request.

**Recommended End-to-End Encrypted (E2EE) Providers:**

- **Proton Drive:** Swiss-based, open-source, integrated with Proton Mail.
- **Filen:** Zero-knowledge encryption, based in Germany.
- **Mega:** Offers generous free storage with user-controlled encryption.

### Physical Storage Hygiene

- **Tamper-Evidence:** If storing backup drives physically, use tamper-evident bags or seals (even glitter nail polish on screws) to detect if someone accessed them.
- **Compartmentalization:** Keep sensitive work data on a separate, encrypted USB drive (like Tails OS with Persistent Storage) rather than your main daily driver computer.

---

## 3. Data Sanitization & Hygiene

Files often contain hidden data (**metadata**) that can reveal your identity, location, and device details. Before sharing files publicly or sending them to journalists, you must sanitize them.

### Removing Metadata (Exif)

Photos often contain GPS coordinates, camera models, and timestamps.

- **Android:** Use **Scrambled Exif** (F-Droid) or **ExifEraser**. Share the photo to the app, and it saves a clean copy.
- **Desktop:** Use **MAT2** (Metadata Anonymisation Toolkit) or **ExifTool**.
  - _Command Line:_ `exiftool -all= filename.jpg`
- **Windows/macOS:** Built-in "Remove Properties" features often miss data. Use dedicated tools like MAT2 (via GUI or WSL).

### Document Sanitization: Dangerzone

[Dangerzone](https://dangerzone.rocks/) allows you to open suspicious documents (PDFs, Office files, Images) safely. It converts the document into raw pixels and then back into a clean PDF.

- **Usage 1 (Protection):** Open a suspicious attachment safely without risking malware infection.
- **Usage 2 (Redaction):** It strips all metadata, scripts, and hidden layers from your own documents before you share them.

### Visual Redaction

Never use "blur" or "swirl" effects to hide text or faces; these can often be reversed by AI tools.

- **Correct Method:** Use solid, opaque boxes (100% opacity) to cover sensitive info.
- **Tools:** Signal App (built-in blur tool), standard image editors with solid shapes.

---

## 4. Secure Data Destruction

When you "delete" a file (Empty Recycle Bin), the operating system only removes the reference to the file. The actual data remains on the disk until it is overwritten. Forensic tools can easily recover "deleted" files.

### Secure Deletion Tools

These tools overwrite the file's space with random data, making recovery impossible.

- **Windows:**
  - **BleachBit:** Use the "File Shredder" option. Also cleans temporary files, cache, and browser history securely.
  - **Eraser:** Adds a right-click context menu to securely erase files.
- **macOS:**
  - Modern Macs with SSDs make secure deletion difficult due to "wear leveling." The safest method is **Full Disk Encryption** (FileVault). If the key is destroyed (e.g., formatting the drive), the data is unrecoverable.
  - For external mechanical drives, you can use the `srm` command in Terminal (if installed) or Disk Utility's "Security Options" when formatting.
- **Linux:**
  - **BleachBit:** Available for Linux.
  - **Shred:** Command line tool (`shred -u filename`).
  - **Wipe:** Another robust command line utility.

### Wiping Free Space

If you have deleted files insecurely in the past, use BleachBit to "Wipe Free Space." This overwrites all empty space on your hard drive to ensure previously deleted files are unrecoverable.

### Physical Destruction

For extremely high-risk scenarios where software wiping is insufficient or time-consuming:

- **HDD (Spinning Drive):** Drill holes through the platters or dismantle and sand/shatter them.
- **SSD/Flash Memory:** Shredding or drilling through the memory chips is required. Standard magnetic degaussing does not work on SSDs.

---

## Summary Checklist for Iranian Users

1.  [ ] **Encrypt Everything:** Ensure FDE is active on your phone and laptop.
2.  [ ] **Hide Sensitive Data:** Use VeraCrypt hidden volumes for sensitive activist materials.
3.  [ ] **Backup Securely:** Use E2EE cloud storage (Proton, Filen) or encrypted USB drives stored in safe locations.
4.  [ ] **Scrub Metadata:** Run photos through Scrambled Exif or MAT2 before posting to social media.
5.  [ ] **Shred, Don't Delete:** Use BleachBit to permanently remove sensitive files.
6.  [ ] **Power Off:** Fully shut down devices before crossing checkpoints to maximize encryption strength.
