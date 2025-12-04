```yaml
---
title: "Recommended Encryption Software: VeraCrypt, Cryptomator, and OpenPGP"
tags: [encryption, privacy, security, veracrypt, cryptomator, openpgp, disk-encryption, file-encryption]
category: "Encryption Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Practitioners, General Public]
topics: ["File Encryption", "Disk Encryption", "OpenPGP", "Cloud Security"]
summary: "Comprehensive guide to recommended encryption software including Cryptomator for cloud storage, VeraCrypt for disk encryption, and OpenPGP tools for secure communication."
source: "Privacy Guides"
content_type: "Reference Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "12 minutes"
---
```

# Encryption Software

**Encryption** is the only secure way to control who can access your data. If you are currently not using encryption software for your hard disk, emails, or files, you should pick an option from this guide.

---

## Multi-Platform Tools

These options work across multiple operating systems and are ideal for creating encrypted backups of your data.

### Cryptomator (Cloud Storage Encryption)

**Threat Model:** Passive Attacks, Privacy from Service Providers

Cryptomator is an encryption solution designed for privately saving files to any cloud service provider, eliminating the need to trust that they won't access your files. It creates vaults stored on a virtual drive, with contents encrypted and synced with your cloud storage provider.

**Technical Details:**
- Uses AES-256 encryption for both files and filenames
- Cannot encrypt metadata (access, modification, creation timestamps, file/folder counts and sizes)
- Free on desktop platforms; iOS offers "read only" mode for free
- Paid apps available for full iOS and Android functionality
- Android version available anonymously via ProxyStore

**Security Audits:**
Cure53 has audited several Cryptomator cryptographic libraries including cryptolib, cryptofs, siv-mode, and cryptomator-objc-cryptor. Note: cryptolib-swift (iOS library) was not included in the audit.

**Resources:**
- [Homepage](https://cryptomator.org/)
- [Documentation](https://docs.cryptomator.org/)
- [Source Code](https://github.com/cryptomator)

**Available on:** Windows, macOS, Linux, Android, iOS, Flathub

---

### VeraCrypt (Disk Encryption)

**Threat Model:** Targeted Attacks

VeraCrypt is a source-available freeware utility for on-the-fly encryption. It can create virtual encrypted disks within files, encrypt partitions, or encrypt entire storage devices with pre-boot authentication.

**Background:**
VeraCrypt is a fork of the discontinued TrueCrypt project. Security improvements have been implemented and issues from the initial TrueCrypt code audit have been addressed.

**Recommended Settings:**
- Hash function: **SHA-512 only**
- Block cipher: **AES**

**Security Audits:**
Both TrueCrypt and VeraCrypt have undergone multiple security audits.

**Resources:**
- [Homepage](https://veracrypt.fr/)
- [Documentation](https://veracrypt.fr/en/Documentation.html)
- [Source Code](https://veracrypt.fr/code)

**Available on:** Windows, macOS, Linux

---

## Operating System Encryption

**Threat Model:** Targeted Attacks

Built-in OS encryption solutions typically leverage hardware security features such as secure cryptoprocessors. We recommend using your operating system's built-in encryption. For cross-platform needs, use the multi-platform tools above to avoid vendor lock-in.

### BitLocker (Windows)

BitLocker is Microsoft Windows' full volume encryption solution that uses the Trusted Platform Module (TPM) for hardware-based security.

**Availability:** Officially supported on Pro, Enterprise, and Education editions. Can be enabled on Home editions with specific prerequisites.

**Enabling BitLocker on Windows Home:**

Requirements:
- GUID Partition Table formatted partitions
- Dedicated TPM module (v1.2 or 2.0+)
- Disable non-BitLocker "Device encryption" if enabled (this inferior option sends recovery keys to Microsoft)

**Steps:**
1. Check partition format:
   ```powershell
   Get-Disk
   ```

2. Check TPM status:
   ```powershell
   Get-WmiObject -Namespace "root/cimv2/security/microsofttpm" -Class WIN32_tpm
   ```

3. Access Advanced Startup Options (reboot with F8 before Windows starts)
4. Navigate to **Troubleshoot** → **Advanced Options** → **Command Prompt**
5. Enable BitLocker via command prompt
6. Continue booting to regular Windows

> **Important:** Backup `BitLocker-Recovery-Key.txt` to a separate storage device. Loss of this recovery code may result in permanent data loss.

---

### FileVault (macOS)

FileVault is macOS's on-the-fly volume encryption solution that leverages hardware security capabilities present on Apple Silicon SoC or T2 Security Chip.

**Recommendation:** Use a local recovery key stored on a separate device rather than iCloud account recovery.

**Resources:**
- [Apple Documentation](https://support.apple.com/guide/mac-help/encrypt-mac-data-with-filevault-mh11785/mac)

---

### LUKS (Linux)

Linux Unified Key Setup (LUKS) is the default full disk encryption method for Linux. It can encrypt full volumes, partitions, or create encrypted containers.

**Creating Encrypted Containers:**
```bash
dd if=/dev/urandom of=/path-to-file bs=1M count=1024 status=progress
sudo cryptsetup luksFormat /path-to-file
```

**Opening Encrypted Containers:**

Use `udisksctl` for Polkit integration (works with most file managers):
```bash
udisksctl loop-setup -f /path-to-file
udisksctl unlock -b /dev/loop0
```

> **Critical:** Always back up your LUKS headers in case of partial drive failure:
> ```bash
> cryptsetup luksHeaderBackup /dev/device --header-backup-file /mnt/backup/file.img
> ```

**Resources:**
- [Repository](https://gitlab.com/cryptsetup/cryptsetup)
- [Documentation](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/home)

---

## Command-Line Tools

**Threat Model:** Targeted Attacks

Command-line tools are useful for shell script integration and automation.

### Kryptor

Kryptor is a free and open-source file encryption and signing tool using modern cryptographic algorithms. It aims to be a simpler alternative to GPG, improving on age and Minisign.

**Resources:**
- [Homepage](https://kryptor.co.uk/)
- [Documentation](https://kryptor.co.uk/tutorial)
- [Source Code](https://github.com/samuel-lucas6/Kryptor)

**Available on:** Windows, macOS, Linux

---

### Tomb

Tomb is a command-line shell wrapper for LUKS that supports steganography via third-party tools.

**Resources:**
- [Homepage](https://dyne.org/software/tomb)
- [Documentation](https://github.com/dyne/Tomb/wiki)
- [Source Code](https://github.com/dyne/Tomb)

---

## OpenPGP

**Threat Model:** Targeted Attacks, Passive Attacks, Privacy from Service Providers

OpenPGP is used for specific tasks like digitally signing and encrypting email. Note that PGP is [complex](https://latacora.micro.blog/2019/07/16/the-pgp-problem.html) due to its long history. For simple file signing or encryption, consider the tools above instead.

**Configuration:**
Stick with standard options from the [GnuPG user FAQ](https://gnupg.org/faq/gnupg-faq.html#new_user_gpg_conf).

**Generating Keys with Modern Cryptography:**
```bash
gpg --quick-gen-key alice@example.com future-default
```
This uses modern algorithms like Curve25519 and Ed25519.

---

### GNU Privacy Guard (GnuPG)

GnuPG is the GPL-licensed alternative to PGP, compliant with RFC 4880 (current OpenPGP specification). It has received major funding from the German government.

**Resources:**
- [Homepage](https://gnupg.org/)
- [Documentation](https://gnupg.org/documentation/index.html)

**Available on:** Windows, macOS, Linux, Android (via OpenKeychain)

---

### GPG4win (Windows)

A Windows package from Intevation and g10 Code, originally funded by Germany's Federal Office for Information Security (BSI) in 2005.

**Resources:**
- [Homepage](https://gpg4win.org/)
- [Documentation](https://gpg4win.org/documentation.html)

---

### GPG Suite (macOS)

Provides OpenPGP support for Apple Mail and other macOS email clients.

> **Note:** Currently does not have a stable release for macOS Sonoma and later.

**Resources:**
- [Homepage](https://gpgtools.org/)
- [First Steps Guide](https://gpgtools.tenderapp.com/kb/how-to/first-steps-where-do-i-start-where-do-i-begin-setup-gpgtools-create-a-new-key-your-first-encrypted-email)

---

### OpenKeychain (Android)

An Android implementation of GnuPG, commonly required by mail clients like Thunderbird and FairEmail for encryption support.

**Security Audit:** Cure53 completed a security audit of OpenKeychain 3.6 in October 2015.

**Resources:**
- [Homepage](https://openkeychain.org/)
- [Documentation](https://openkeychain.org/faq)
- [Source Code](https://github.com/open-keychain/open-keychain)

**Available on:** Google Play

---

## Selection Criteria

Privacy Guides uses the following criteria for encryption software recommendations:

### Minimum Requirements
- Cross-platform encryption apps must be open source
- File encryption apps must support decryption on Linux, macOS, and Windows
- External disk encryption apps must support decryption on Linux, macOS, and Windows
- Internal (OS) disk encryption apps must be cross-platform or built into the OS natively

### Best-Case Criteria
- OS encryption apps should utilize hardware security (TPM or Secure Enclave)
- File encryption apps should have mobile platform support

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/encryption/)*