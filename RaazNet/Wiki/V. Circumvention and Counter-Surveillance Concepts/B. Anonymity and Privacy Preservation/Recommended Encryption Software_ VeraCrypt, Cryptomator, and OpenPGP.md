```yaml
---
title: "Recommended Encryption Software: VeraCrypt, Cryptomator, and OpenPGP"
tags: [encryption, privacy, security, file-encryption, disk-encryption, openpgp]
category: "Encryption Software"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Practitioners, General Public]
topics: ["File Encryption", "Disk Encryption", "OpenPGP", "Cloud Security"]
summary: "Comprehensive guide to recommended encryption software including Cryptomator for cloud storage, VeraCrypt for disk encryption, and OpenPGP tools for secure communication."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "12 minutes"
---
```

# Encryption Software

**Encryption** is the only secure way to control who can access your data. If you are currently not using encryption software for your hard disk, emails, or files, you should pick an option from this guide.

## Multi-Platform Tools

The options listed here are available on multiple platforms and great for creating encrypted backups of your data.

### Cryptomator (Cloud Storage Encryption)

**Threat Model:** Protects against passive attacks and untrusted service providers

![Cryptomator logo](https://www.privacyguides.org/en/assets/img/encryption-software/cryptomator.svg)

**Cryptomator** is an encryption solution designed for privately saving files to any cloud service provider, eliminating the need to trust that they won't access your files. It creates vaults stored on a virtual drive, with contents encrypted and synced with your cloud storage provider.

**Key Features:**
- Uses AES-256 encryption for both files and filenames
- Cannot encrypt metadata (access, modification, creation timestamps, file/folder counts and sizes)
- Free on desktop platforms; iOS has read-only free mode
- Android version available for anonymous purchase via ProxyStore

**Security Audits:**
Cure53 has audited several Cryptomator cryptographic libraries including cryptolib, cryptofs, siv-mode, and cryptomator-objc-cryptor. Note: cryptolib-swift (iOS library) was not included in the audit.

**Resources:**
- [Homepage](https://cryptomator.org/)
- [Documentation](https://docs.cryptomator.org/)
- [Source Code](https://github.com/cryptomator)

**Downloads:** Available on Google Play, App Store, Windows, macOS, Linux, and Flathub

---

### VeraCrypt (Disk Encryption)

**Threat Model:** Protects against targeted attacks

![VeraCrypt logo](https://www.privacyguides.org/en/assets/img/encryption-software/veracrypt.svg)

**VeraCrypt** is a source-available freeware utility for on-the-fly encryption. It can create virtual encrypted disks within files, encrypt partitions, or encrypt entire storage devices with pre-boot authentication.

**Key Information:**
- Fork of the discontinued TrueCrypt project with security improvements
- Issues from initial TrueCrypt code audit have been addressed
- **Recommended settings:** Use SHA-512 hash function and AES block cipher only

**Security Audits:**
Both TrueCrypt and VeraCrypt have undergone multiple security audits.

**Resources:**
- [Homepage](https://veracrypt.fr/)
- [Documentation](https://veracrypt.fr/en/Documentation.html)
- [Source Code](https://veracrypt.fr/code)

**Downloads:** Available on Windows, macOS, and Linux

---

## Operating System Encryption

Built-in OS encryption solutions generally leverage hardware security features such as a secure cryptoprocessor. We recommend using built-in encryption for your operating system, supplemented by cross-platform tools for additional flexibility.

### BitLocker (Windows)

**Threat Model:** Protects against targeted attacks

![BitLocker logo](https://www.privacyguides.org/en/assets/img/encryption-software/bitlocker.png)

**BitLocker** is the full volume encryption solution bundled with Microsoft Windows, using the Trusted Platform Module (TPM) for hardware-based security.

**Availability:**
- Officially supported on Pro, Enterprise, and Education editions
- Can be enabled on Home editions with specific prerequisites

#### Enabling BitLocker on Windows Home

**Prerequisites:**
- Partitions formatted with GUID Partition Table
- Dedicated TPM module (v1.2 or 2.0+)
- Disable non-BitLocker "Device encryption" if enabled (this inferior option sends recovery keys to Microsoft)

**Steps:**
1. Verify GUID partition table:
   ```powershell
   Get-Disk
   ```

2. Verify TPM module:
   ```powershell
   Get-WmiObject -Namespace "root/cimv2/security/microsofttpm" -Class WIN32_tpm
   ```

3. Access Advanced Startup Options (reboot while pressing F8 before Windows starts)

4. Navigate to **Troubleshoot** → **Advanced Options** → **Command Prompt**

5. Enable BitLocker via command prompt, then continue booting to regular Windows

> **Important:** Backup `BitLocker-Recovery-Key.txt` to a separate storage device. Loss of this recovery code may result in loss of data.

---

### FileVault (macOS)

**Threat Model:** Protects against targeted attacks

![FileVault logo](https://www.privacyguides.org/en/assets/img/encryption-software/filevault.png)

**FileVault** is the on-the-fly volume encryption solution built into macOS, leveraging hardware security capabilities of Apple Silicon SoC or T2 Security Chip.

**Recommendation:** Store a local recovery key on a separate storage device rather than using iCloud account recovery.

**Resources:** [Apple Documentation](https://support.apple.com/guide/mac-help/encrypt-mac-data-with-filevault-mh11785/mac)

---

### LUKS (Linux)

**Threat Model:** Protects against targeted attacks

![LUKS logo](https://www.privacyguides.org/en/assets/img/encryption-software/luks.png)

**LUKS** (Linux Unified Key Setup) is the default full disk encryption method for Linux. It can encrypt full volumes, partitions, or create encrypted containers.

#### Creating Encrypted Containers

```bash
dd if=/dev/urandom of=/path-to-file bs=1M count=1024 status=progress
sudo cryptsetup luksFormat /path-to-file
```

#### Opening Encrypted Containers

Use `udisksctl` for opening containers (uses Polkit for security). Tools like [udiskie](https://github.com/coldfix/udiskie) provide helpful system tray interfaces.

```bash
udisksctl loop-setup -f /path-to-file
udisksctl unlock -b /dev/loop0
```

#### Backup Volume Headers

Always back up LUKS headers in case of partial drive failure:

```bash
cryptsetup luksHeaderBackup /dev/device --header-backup-file /mnt/backup/file.img
```

**Resources:**
- [Repository](https://gitlab.com/cryptsetup/cryptsetup)
- [Documentation](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/home)

---

## Command-Line Tools

Command-line tools are useful for integrating with shell scripts and automation.

### Kryptor

![Kryptor logo](https://www.privacyguides.org/en/assets/img/encryption-software/kryptor.png)

**Kryptor** is a free, open-source file encryption and signing tool using modern cryptographic algorithms. It aims to be a simpler alternative to GPG, improving upon [age](https://github.com/FiloSottile/age) and [Minisign](https://jedisct1.github.io/minisign).

**Resources:**
- [Homepage](https://kryptor.co.uk/)
- [Documentation](https://kryptor.co.uk/tutorial)
- [Source Code](https://github.com/samuel-lucas6/Kryptor)

**Downloads:** Available on Windows, macOS, and Linux

---

### Tomb

![Tomb logo](https://www.privacyguides.org/en/assets/img/encryption-software/tomb.png)

**Tomb** is a command-line shell wrapper for LUKS with support for steganography via third-party tools.

**Resources:**
- [Homepage](https://dyne.org/software/tomb)
- [Documentation](https://github.com/dyne/Tomb/wiki)
- [Source Code](https://github.com/dyne/Tomb)

---

## OpenPGP Tools

**Threat Model:** Protects against targeted attacks, passive attacks, and untrusted service providers

OpenPGP is needed for specific tasks such as digitally signing and encrypting email. PGP is [complex](https://latacora.micro.blog/2019/07/16/the-pgp-problem.html) due to its long history. For simple file signing or encryption, consider the tools listed above instead.

**Configuration:** Stay with standard options in the [GnuPG user FAQ](https://gnupg.org/faq/gnupg-faq.html#new_user_gpg_conf).

**Key Generation Best Practice:**
Use the `future-default` command to generate keys with modern cryptography (Curve25519 and Ed25519):

```bash
gpg --quick-gen-key alice@example.com future-default
```

### GNU Privacy Guard (GnuPG)

![GnuPG logo](https://www.privacyguides.org/en/assets/img/encryption-software/gnupg.svg)

**GnuPG** is a GPL-licensed alternative to the PGP suite, compliant with RFC 4880 (current OpenPGP specification). Part of the Free Software Foundation's GNU project, it has received major funding from the German government.

**Resources:**
- [Homepage](https://gnupg.org/)
- [Documentation](https://gnupg.org/documentation/index.html)
- [Source Code](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gnupg.git)

**Downloads:** Available on Google Play, Windows, macOS, and Linux

---

### GPG4win (Windows)

![GPG4win logo](https://www.privacyguides.org/en/assets/img/encryption-software/gpg4win.svg)

**GPG4win** is a Windows package from Intevation and g10 Code, originally funded by Germany's Federal Office for Information Security (BSI) in 2005.

**Resources:**
- [Homepage](https://gpg4win.org/)
- [Documentation](https://gpg4win.org/documentation.html)

**Downloads:** [Windows](https://gpg4win.org/download.html)

---

### GPG Suite (macOS)

![GPG Suite logo](https://www.privacyguides.org/en/assets/img/encryption-software/gpgsuite.png)

**GPG Suite** provides OpenPGP support for Apple Mail and other email clients on macOS.

> **Note:** GPG Suite does not yet have a stable release for macOS Sonoma and later.

**Resources:**
- [Homepage](https://gpgtools.org/)
- [First Steps Guide](https://gpgtools.tenderapp.com/kb/how-to/first-steps-where-do-i-start-where-do-i-begin-setup-gpgtools-create-a-new-key-your-first-encrypted-email)
- [Knowledge Base](https://gpgtools.tenderapp.com/kb)

**Downloads:** [macOS](https://gpgtools.org/)

---

### OpenKeychain (Android)

![OpenKeychain logo](https://www.privacyguides.org/en/assets/img/encryption-software/openkeychain.svg)

**OpenKeychain** is a GnuPG implementation for Android, commonly required by mail clients such as Thunderbird and FairEmail for encryption support.

**Security Audit:** Cure53 completed a security audit of OpenKeychain 3.6 in October 2015.

**Resources:**
- [Homepage](https://openkeychain.org/)
- [Documentation](https://openkeychain.org/faq)
- [Security Audit Details](https://github.com/open-keychain/open-keychain/wiki/cure53-Security-Audit-2015)

**Downloads:** [Google Play](https://play.google.com/store/apps/details?id=org.sufficientlysecure.keychain)

---

## Selection Criteria

Privacy Guides is not affiliated with any recommended projects. Their selection criteria includes:

### Minimum Qualifications
- Cross-platform encryption apps must be open source
- File encryption apps must support decryption on Linux, macOS, and Windows
- External disk encryption apps must support decryption on Linux, macOS, and Windows
- Internal (OS) disk encryption apps must be cross-platform or built into the OS natively

### Best-Case Criteria
- OS encryption apps should utilize hardware security (TPM or Secure Enclave)
- File encryption apps should have mobile platform support