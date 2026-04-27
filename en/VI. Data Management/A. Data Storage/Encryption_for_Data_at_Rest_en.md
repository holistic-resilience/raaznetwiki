---
title: "Encryption for Data at Rest"
tags:
  [
    encryption,
    data-storage,
    veracrypt,
    cryptomator,
    mobile-security,
    plausible-deniability,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public, High-Risk Users]
topics:
  [
    "Full Disk Encryption",
    "Hidden Volumes",
    "Cloud Encryption",
    "Mobile Security",
  ]
summary: "Comprehensive guide to protecting stored data from physical seizure and unauthorized access using encryption tools like VeraCrypt, Cryptomator, and mobile lockdown features."
source: "Raaznet Aggregated"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file management"]
estimated_read_time: "15 minutes"
---

# Encryption for Data at Rest

**Data at Rest** refers to information stored on a digital medium—such as a hard drive, USB stick, or mobile phone—that is not currently moving through a network. In the Iranian context, protecting data at rest is critical. A primary threat vector for Iranian citizens is the physical seizure of devices at checkpoints, during protests, or via home raids.

If your device is seized, **encryption** is the only barrier between your private information and the authorities. Without encryption, a seized laptop or phone is an open book. With strong encryption, it is merely a brick.

## The Strategy: Defense in Depth

To effectively protect your stored data, you must apply encryption at multiple layers:

1.  **Full Disk Encryption (FDE):** Protects the entire operating system and all files.
2.  **Container Encryption:** Creates secure "vaults" for specific sensitive files (often with plausible deniability).
3.  **Cloud Encryption:** Protects files before they are uploaded to services like Google Drive.

---

## 1. Full Disk Encryption (FDE)

FDE encrypts everything on your storage drive. You must enter a password before the operating system even boots.

### Windows: VeraCrypt (Recommended) vs. BitLocker

While Windows Pro editions come with **BitLocker**, it is closed-source and relies on the TPM chip, which has known vulnerabilities requiring physical access to exploit. For high-risk users in Iran, we recommend **VeraCrypt** for System Encryption because it is open-source and audit-friendly.

- **VeraCrypt System Encryption:** Replaces the Windows bootloader. It requires a password immediately upon powering on the machine.
- **BitLocker Hardening:** If you must use BitLocker, do _not_ rely on the default "transparent" mode (where it unlocks automatically). You must enable a **Pre-Boot PIN** via Group Policy so the device cannot be unlocked solely by the TPM chip.

### macOS: FileVault

macOS users should enable **FileVault** immediately.

- **Go to:** `System Settings` > `Privacy & Security` > `FileVault`.
- **Recovery Key:** Do _not_ store your recovery key with Apple (i.e., do not use your iCloud account to unlock). Generate a local recovery key and write it down in a secure, physical location.

### Linux: LUKS

**LUKS (Linux Unified Key Setup)** is the standard for Linux encryption.

- Most distributions (Ubuntu, Debian, Fedora) offer to enable LUKS during installation. **You must select this option when installing the OS.**
- **Nuke Option (Advanced):** Users running Kali Linux or specialized distros can configure a "Nuke Password." If forced to enter a password, entering the "Nuke" variant destroys the encryption headers, making the data permanently unrecoverable.

---

## 2. Container Encryption & Plausible Deniability

In Iran, you may face "rubber-hose cryptanalysis"—where an adversary forces you to reveal your password through coercion or threats. **Plausible Deniability** is your defense against this.

### VeraCrypt Hidden Volumes

**VeraCrypt** allows you to create a "Hidden Volume" inside a standard encrypted volume.

1.  **Outer Volume (Decoy):** This volume contains "normal" sensitive data (e.g., personal photos, non-political documents). You reveal this password if forced.
2.  **Inner Volume (Hidden):** This resides in the "free space" of the outer volume. It contains your critical sensitive data (e.g., evidence of human rights abuses, protest coordination).

**How it works:**

- When you mount the file, you are asked for a password.
- If you enter the **Decoy Password**, the Outer Volume opens.
- If you enter the **Hidden Password**, the Hidden Volume opens.
- Mathematically, it is impossible to prove the Hidden Volume exists. To an adversary, the free space of the Outer Volume looks like random noise.

> **Warning:** To maintain plausible deniability, you must not accidentally overwrite the hidden data when using the Decoy volume. VeraCrypt has a "Protect Hidden Volume" option when mounting the outer volume for maintenance.

---

## 3. Cloud Encryption (Before Uploading)

Cloud storage providers (Google Drive, Dropbox) can see your files. In legal cases, they may comply with subpoenas, or their accounts can be compromised.

### Cryptomator

**Cryptomator** is the standard tool for encrypting files _before_ they sync to the cloud. Unlike VeraCrypt, which creates one giant file (difficult to sync), Cryptomator encrypts each file individually.

- **Usage:** Create a "Vault" inside your Google Drive or Dropbox folder.
- **Result:** You see unlocked files on your virtual drive. The cloud provider only sees encrypted nonsense names (e.g., `d83ks92.c9r`).
- **Mobile:** Cryptomator has excellent apps for Android and iOS, allowing you to access these encrypted cloud files on your phone.

---

## 4. Mobile Device Security

Smartphones are the most commonly seized devices in Iran.

### Disable Biometrics (Lockdown Mode)

Fingerprint and Face Unlock are convenient but dangerous. An agent can forcibly press your finger to the sensor or hold the phone to your face.

- **Android:** Enable "Show Lockdown Option" in settings. When approaching a checkpoint, hold the Power button and tap **Lockdown**. This disables biometrics and forces a PIN/Pattern entry.
- **iOS:** Hold the Power button + Volume Up for 2 seconds (until the slider appears), then cancel. This disables FaceID/TouchID until the next passcode entry.

### Android: Private Space / Secure Folder

Modern Android versions (Android 15+ "Private Space" or Samsung "Secure Folder") create an encrypted sandbox.

- Apps and data inside this space are separate from the main OS.
- You can set a **different PIN** for this space.
- **Raaznet Tip:** Store sensitive apps (Signal, VPNs) inside this space. In some implementations, you can "hide" the existence of the space entirely, requiring a special code in the dialer or search bar to reveal it.

---

## 5. Security Checklists

### Hardware Hygiene

- **Power Off:** When crossing borders or checkpoints, **power off your device completely**. Encryption keys are stored in RAM (memory) while the device is on. Powering off clears the RAM (Cold Boot defense).
- **Separate Accounts:** Use a separate user profile for sensitive work if you cannot use a separate device.

### Selection Criteria for Tools

We only recommend tools that meet these standards:

- **Open Source:** The code must be auditable (e.g., VeraCrypt, Cryptomator).
- **End-to-End Encryption (E2EE):** Keys must be on your device, not the server.
- **Audit History:** The software must have undergone independent security audits.

### Summary of Recommended Tools

| Purpose              | Tool            | Platform    | Notes                                                   |
| :------------------- | :-------------- | :---------- | :------------------------------------------------------ |
| **Disk Encryption**  | **VeraCrypt**   | Win/Linux   | Best for plausible deniability.                         |
| **Cloud Encryption** | **Cryptomator** | All         | Best for Google Drive/Dropbox.                          |
| **MacOS Disk**       | **FileVault**   | macOS       | Use a local recovery key.                               |
| **Mobile Backups**   | **Signal**      | Android/iOS | Enable "Chat Backups" with a 30-digit passphrase.       |
| **File Deletion**    | **BleachBit**   | Win/Linux   | Securely wipes free space (see "Secure Data Deletion"). |

---

**Related Topics:**

- [Backup_and_Recovery_Strategies](backup-and-recovery-strategies)
- [Secure_Cloud_Storage_and_Sharing](secure-cloud-storage-and-sharing)
- [Secure_Data_Deletion](../secure-data-deletion)
