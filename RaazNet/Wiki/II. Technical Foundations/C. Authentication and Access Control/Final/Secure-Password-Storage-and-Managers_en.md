---
title: "Secure Password Storage and Managers"
tags:
  [
    password-manager,
    keepass,
    bitwarden,
    encryption,
    offline-security,
    iran-privacy,
    censorship-circumvention,
  ]
category: "Authentication"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists]
topics: ["Digital Security", "Password Management", "Data Protection"]
summary: "A comprehensive guide to securely storing credentials using password managers, tailored for the Iranian context of internet shutdowns and device seizure risks."
source: "Raaznet Wiki"
content_type: "Technical Guide"
security_level: "High"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of password strength"]
estimated_read_time: "10 minutes"
---

# Secure Password Storage and Managers

Relying on memory or browser-based storage for passwords is a significant security vulnerability. With threats ranging from extensive surveillance and phishing campaigns to physical device seizures and internet blackouts, the method used to store credentials is as critical as the strength of the passwords themselves.

This guide details the transition from insecure storage methods to robust, encrypted Password Managers (PMs), with a specific focus on tools that remain functional during internet shutdowns (National Information Network restrictions).

## Why Password Managers are Essential

The average user has dozens of accounts. Reusing passwords creates a "single point of failure"—if one service is breached, attackers (including state-sponsored actors) use **Credential Stuffing** to access all your other accounts.

A Password Manager solves this by:

1.  **Generating High-Entropy Passwords:** Creating long, random strings (e.g., `Xy9#mP2$Lq!zR5`) that are mathematically impossible to guess.
2.  **Encrypted Storage:** Storing all credentials in a "Vault" protected by modern encryption standards (AES-256 or ChaCha20).
3.  **Phishing Protection:** Auto-fill features only work on the legitimate URL, protecting you if you accidentally click a fake link (e.g., a fake Gmail login page sent via SMS).

## The Iranian Context: Cloud vs. Local Storage

When selecting a password manager in Iran, you must consider two specific threat vectors: **Internet Shutdowns** and **Physical Access**.

### 1. Offline (Local) Password Managers (Recommended)

These applications store your encrypted database file (`.kdbx`) directly on your device. No data is sent to a cloud server.

- **Pros:**
  - **Censorship Resistant:** Works perfectly during "filternet" disruptions or total internet blackouts.
  - **Privacy:** You possess the only copy of your data. No third-party server can leak it.
  - **Sanctions Proof:** No account creation required; no risk of service banning Iranian IP addresses.
- **Cons:**
  - **Backup Responsibility:** You must manually back up the database file to other devices. If you lose the device and have no backup, the data is gone forever.
  - **Sync Convenience:** Syncing between phone and laptop requires manually moving the file (via USB or Syncthing).

### 2. Cloud-Based Password Managers

These services store an encrypted copy of your vault on their servers, syncing changes across devices instantly.

- **Pros:**
  - **Convenience:** Passwords act seamlessly across all devices.
  - **Automatic Backups:** The provider handles data redundancy.
- **Cons:**
  - **Connection Dependency:** While they cache data locally, initial setup or syncing changes requires a VPN if the service is blocked.
  - **Traffic Analysis:** ISPs can see you are connecting to a password manager service (though they cannot read the content).

> [!tip] Recommendation for High-Risk Users
> For activists and journalists in Iran, **Offline Password Managers** (KeePass family) are recommended to mitigate the risk of server blocking and reduce the digital footprint.

## Recommended Tools

We recommend **Open Source** software. Open source code allows security researchers to verify that the encryption is implemented correctly and that there are no backdoors.

### Best for Desktop (Windows, Linux, macOS): KeePassXC

**KeePassXC** is the community standard for offline password management. It is free, open-source, and highly secure.

- **Encryption:** Uses AES-256 or Twofish with Argon2id key derivation (highly resistant to brute force).
- **Features:** detailed password generator, Diceware support, and SSH agent integration.
- **Setup:**
  1.  Download from the official site (verify the GPG signature if possible).
  2.  Create a new database.
  3.  Set the **Key Derivation Function** to `Argon2id` in Database Settings for maximum security.

### Best for Android: KeePassDX

**KeePassDX** is a file-compatible android client for KeePass databases.

- **Security:** Fully offline; does not require internet permissions.
- **Keyboard:** Includes a "Magikeyboard" to auto-fill passwords without using the clipboard (which other apps can read).
- **Biometrics:** Supports fingerprint unlock, but use with caution (see "Border Crossings" below).

### Best for iOS: Strongbox or KeePassium

Both are excellent, open-source friendly apps that support KeePass database files.

- **Strongbox:** Highly configurable, supports hardware keys (YubiKey).
- **KeePassium:** Clean interface, robust file handling.

### Best Cloud Option: Bitwarden

If you require cloud sync, **Bitwarden** is the safest choice. Unlike proprietary competitors, it is open-source and has undergone third-party audits.

- **Self-Hosting:** Advanced users can self-host a Bitwarden instance (Vaultwarden) on a private VPS, giving you cloud convenience without relying on central servers that might be blocked.
- **Free Tier:** The free version is fully functional and does not require payment methods (avoiding banking sanction issues).

## Security Configuration & Best Practices

### 1. The Master Password (Diceware)

Your Master Password is the key to the kingdom. It must be memorable but unbreakable. Do not use personal details. Use the **Diceware** method:

- Select 5 to 7 random words.
- Example: `correct-horse-battery-staple-spider` (Do not use this example).
- This creates a passphrase with high entropy that is easier to type than random characters.

### 2. Keyfiles (Two-Factor for Databases)

For offline managers like KeePassXC, you can use a **Keyfile** in addition to a password. This is a file (e.g., an image or a random text file) that must be present to open the database.

- **Strategy:** Keep the database on your laptop, but store the Keyfile on a USB drive or your phone. An attacker stealing the laptop cannot open the vault without the USB drive.

### 3. Browser Integration Risks

Most Password Managers offer browser extensions. While convenient, they increase the attack surface.

- **Safe Approach:** If using KeePassXC, use the official `KeePassXC-Browser` extension which communicates securely with the desktop app.
- **Unsafe Approach:** Never save passwords directly in the browser (Chrome/Edge/Firefox built-in managers). Malware known as "Info Stealers" (common in pirated software in Iran) specifically targets browser storage.

### 4. Database Backups

**The 3-2-1 Rule:**

- **3** copies of your database.
- **2** different media types (e.g., Laptop SSD + USB Drive).
- **1** offsite location (e.g., a trusted cloud storage with a separate encryption key, or a physical drive at a trusted relative's house).

> [!warning] Cloud Backups
> If you back up a KeePass database to a cloud service (Google Drive, Dropbox), ensure the Master Password is extremely strong. While the file is encrypted, putting it on a cloud server exposes it to potential download by adversaries if the cloud account is compromised.

## Operational Security for Iran

### Preventing Forced Unlocks

If you are detained or stopped at a checkpoint, security forces may force you to unlock your phone.

1.  **Biometrics:** Disable FaceID/Fingerprint for your Password Manager app. Require the Master Password or a PIN to open it.
2.  **Duress/Hidden Features:**
    - Some apps allow you to hide the icon or rename the application.
    - **KeePassDX** allows creating a separate "Panic" database. If forced to open the app, you can open a dummy database containing non-sensitive passwords, while the real database remains hidden.

### Detecting Compromise

- **Clipboard Clearing:** Configure your manager to clear the clipboard after 30 seconds. This prevents other apps from reading a copied password.
- **Check for Breaches:** Periodically check your email against [Have I Been Pwned](https://haveibeenpwned.com) (accessible via VPN). If your Master Password has ever been used elsewhere, change it immediately.

## Migration Guide

If you currently use Google Chrome or a notebook to store passwords:

1.  **Export:** In Chrome, go to `Settings > Autofill > Password Manager > Settings > Export Passwords`. This will create a `.csv` file.
    - _Warning:_ This file is unencrypted text. Anyone who sees it has all your passwords.
2.  **Import:** Open KeePassXC or Bitwarden and choose `Import from CSV`. Select the file generated by Chrome.
3.  **Secure Delete:** Immediately delete the `.csv` file. On Windows, use a shredding tool (like BleachBit); on macOS, use "Delete Immediately."
4.  **Purge:** Go back to Chrome and delete all saved passwords to ensure no unencrypted copies remain.

## Summary Comparison

| Feature                   | KeePassXC (Local)         | Bitwarden (Cloud)    | Browser Built-in          |
| :------------------------ | :------------------------ | :------------------- | :------------------------ |
| **Security**              | High (User controlled)    | High (Audited)       | Low (Targeted by malware) |
| **Censorship Resistance** | Excellent (Works offline) | Moderate (Needs VPN) | High                      |
| **Sync Convenience**      | Low (Manual)              | High (Automatic)     | High                      |
| **Cost**                  | Free (Open Source)        | Free (Open Source)   | Free                      |
| **Recommended For**       | **High-Risk Profiles**    | **General Use**      | **Do Not Use**            |
