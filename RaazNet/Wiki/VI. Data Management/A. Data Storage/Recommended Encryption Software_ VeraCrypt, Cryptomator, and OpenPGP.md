---
title: "Recommended Encryption Software: VeraCrypt, Cryptomator, and OpenPGP"
tags: [encryption, privacy, security, veracrypt, cryptomator, openpgp, disk-encryption, file-encryption]
category: "Encryption Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Practitioners, General Public]
topics: ["File Encryption", "Disk Encryption", "Cloud Security", "OpenPGP"]
summary: "Comprehensive guide to recommended encryption software including Cryptomator for cloud storage, VeraCrypt for disk encryption, and OpenPGP tools for email and file signing."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "12 minutes"
---

# Encryption Software

**Encryption** is the only secure way to control who can access your data. If you are currently not using encryption software for your hard disk, emails, or files, you should pick an option from this guide.

## Multi-Platform Tools

These options are available on multiple platforms and are excellent for creating encrypted backups of your data.

### Cryptomator (Cloud Storage)

**Cryptomator** is an encryption solution designed for privately saving files to any cloud service provider, eliminating the need to trust that they won't access your files. It creates vaults stored on a virtual drive, with contents encrypted and synced with your cloud storage provider.

**Key Features:**
- Uses AES-256 encryption for both files and filenames
- Available on Windows, macOS, Linux, iOS, and Android
- Free on desktop platforms; iOS offers read-only mode for free
- Android version can be purchased anonymously via ProxyStore

**Limitations:**
- Cannot encrypt metadata (access, modification, creation timestamps)
- Cannot hide the number and size of files and folders

**Security Audits:**
Cryptomator's cryptographic libraries have been [audited by Cure53](https://community.cryptomator.org/t/has-there-been-a-security-review-audit-of-cryptomator/44), covering cryptolib, cryptofs, siv-mode, and cryptomator-objc-cryptor. The iOS library (cryptolib-swift) was not included in the audit.

**Resources:**
- [Homepage](https://cryptomator.org/)
- [Documentation](https://docs.cryptomator.org/)
- [Source Code](https://github.com/cryptomator)

---

### VeraCrypt (Disk Encryption)

**VeraCrypt** is a source-available freeware utility for on-the-fly encryption. It can create virtual encrypted disks within files, encrypt partitions, or encrypt entire storage devices with pre-boot authentication.

**Key Features:**
- Fork of the discontinued TrueCrypt project with security improvements
- Supports virtual encrypted disks, partition encryption, and full disk encryption
- Available on Windows, macOS, and Linux

**Recommended Settings:**
- Use **SHA-512** as the hash function
- Use **AES** as the block cipher

**Security Audits:**
TrueCrypt was [audited multiple times](https://en.wikipedia.org/wiki/TrueCrypt#Security_audits), and VeraCrypt has been [audited separately](https://en.wikipedia.org/wiki/VeraCrypt#VeraCrypt_audit). Issues from the original TrueCrypt audit have been addressed.

**Resources:**
- [Homepage](https://veracrypt.fr/)
- [Documentation](https://veracrypt.fr/en/Documentation.html)
- [Source Code](https://veracrypt.fr/code)

---

## Operating System Encryption

Built-in OS encryption solutions typically leverage hardware security features such as a secure cryptoprocessor. We recommend using your operating system's built-in encryption for primary disk protection, supplemented by cross-platform tools for flexibility.

### BitLocker (Windows)

**BitLocker** is Microsoft Windows' full volume encryption solution that uses the Trusted Platform Module (TPM) for hardware-based security.

**Availability:**
- Officially supported on Pro, Enterprise, and Education editions
- Can be enabled on Home editions with specific prerequisites

**Enabling BitLocker on Windows Home:**

Requirements:
- GUID Partition Table formatted partitions
- Dedicated TPM module (v1.2 or 2.0+)

Steps:
1. Disable non-BitLocker "Device encryption" if enabled (this sends recovery keys to Microsoft)
2. Verify disk format: `Get-Disk` (PowerShell)
3. Verify TPM: `Get-WmiObject -Namespace "root/cimv2/security/microsofttpm" -Class WIN32_tpm`
4. Access Advanced Startup Options (F8 before Windows starts)
5. Enable BitLocker via command prompt in recovery mode

> **Important:** Back up your `BitLocker-Recovery-Key.txt` to a separate storage device. Loss of this recovery code may result in permanent data loss.

---

### FileVault (macOS)

**FileVault** is macOS's on-the-fly volume encryption solution, leveraging hardware security capabilities of Apple Silicon SoC or T2 Security Chip.

**Recommendation:** Store a local recovery key on a separate storage device rather than using iCloud account recovery.

**Resources:**
- [Apple Documentation](https://support.apple.com/guide/mac-help/encrypt-mac-data-with-filevault-mh11785/mac)

---

### LUKS (Linux)

**Linux Unified Key Setup (LUKS)** is the default full disk encryption method for Linux. It can encrypt full volumes, partitions, or create encrypted containers.

**Creating Encrypted Containers:**
```bash
dd if=/dev/urandom of=/path-to-file bs=1M count=1024 status=progress
sudo cryptsetup luksFormat /path-to-file
```

**Opening Encrypted Containers:**
```bash
udisksctl loop-setup -f /path-to-file
udisksctl unlock -b /dev/loop0
```

> **Important:** Always back up LUKS headers in case of partial drive failure:
> ```bash
> cryptsetup luksHeaderBackup /dev/device --header-backup-file /mnt/backup/file.img
> ```

**Resources:**
- [Documentation](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/home)
- [Source Code](https://gitlab.com/cryptsetup/cryptsetup)

---

## Command-Line Tools

Command-line encryption tools are useful for integrating with shell scripts and automation.

### Kryptor

**Kryptor** is a free, open-source file encryption and signing tool using modern cryptographic algorithms. It aims to be a simpler alternative to GPG.

**Resources:**
- [Homepage](https://kryptor.co.uk/)
- [Documentation](https://kryptor.co.uk/tutorial)
- Available on Windows, macOS, and Linux

### Tomb

**Tomb** is a command-line shell wrapper for LUKS with support for steganography via third-party tools.

**Resources:**
- [Homepage](https://dyne.org/software/tomb)
- [Documentation](https://github.com/dyne/Tomb/wiki)

---

## OpenPGP

OpenPGP is used for specific tasks such as digitally signing and encrypting email. While PGP is powerful, it is [complex](https://latacora.micro.blog/2019/07/16/the-pgp-problem.html) due to its long history. For simple file encryption, consider the tools above.

**Recommended Key Generation:**
Use the `future-default` option for modern cryptography (Curve25519 and Ed25519):
```bash
gpg --quick-gen-key alice@example.com future-default
```

### GNU Privacy Guard (GnuPG)

**GnuPG** is a GPL-licensed alternative to PGP, compliant with RFC 4880 (current OpenPGP specification). It has received significant funding from the German government.

**Resources:**
- [Homepage](https://gnupg.org/)
- [Documentation](https://gnupg.org/documentation/index.html)

### Platform-Specific OpenPGP Tools

| Tool | Platform | Description |
|------|----------|-------------|
| **GPG4win** | Windows | Package including various GPG utilities; funded by Germany's Federal Office for Information Security |
| **GPG Suite** | macOS | Provides OpenPGP support for Apple Mail and other email clients |
| **OpenKeychain** | Android | GnuPG implementation commonly used with Thunderbird and FairEmail |

> **Note:** GPG Suite does not yet have a stable release for macOS Sonoma and later.

OpenKeychain completed a [security audit by Cure53](https://openkeychain.org/openkeychain-3-6) in October 2015.

---

## Selection Criteria

### Minimum Requirements
- Cross-platform encryption apps must be open source
- File encryption apps must support decryption on Linux, macOS, and Windows
- External disk encryption apps must support decryption on all major platforms
- Internal (OS) disk encryption apps must be cross-platform or built into the OS natively

### Ideal Features
- OS encryption apps should utilize hardware security (TPM or Secure Enclave)
- File encryption apps should have mobile platform support

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/encryption/)*