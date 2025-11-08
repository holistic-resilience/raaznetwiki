---
title: "Encryption Software"
tags: [encryption, cryptomator, veracrypt, openpgp, luks]
category: "Tool Recommendations"
difficulty: "Intermediate"
audience: "General Users"
topics: [disk-encryption, file-encryption, backups, pgp]
summary: "Recommended encryption tools for securing disks, files, backups, and communications across platforms."
source: "https://www.privacyguides.org/en/encryption/"
content_type: "guide"
security_level: "Standard"
language: "en"
prerequisites: []
estimated_read_time: 18
---

[Skip to content](https://www.privacyguides.org/en/encryption/#multi-platform)

![](https://www.privacyguides.org/en/assets/img/cover/encryption.webp)

# Encryption Software

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/encryption.md?plain=1 "Edit this page")

**Encryption** is the only secure way to control who can access your data. If you are currently not using encryption software for your hard disk, emails, or files, you should pick an option here.

## Multi-platform

The options listed here are available on multiple platforms and great for creating encrypted backups of your data.

### Cryptomator (Cloud)

Protects against the following threat(s):

- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)

![Cryptomator logo](https://www.privacyguides.org/en/assets/img/encryption-software/cryptomator.svg)

**Cryptomator** is an encryption solution designed for privately saving files to any cloud [Service Provider](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers).

### VeraCrypt (Disk)

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

![VeraCrypt logo](https://www.privacyguides.org/en/assets/img/encryption-software/veracrypt.svg#only-light)![VeraCrypt logo](https://www.privacyguides.org/en/assets/img/encryption-software/veracrypt-dark.svg#only-dark)

**VeraCrypt** is a source-available freeware utility used for on-the-fly encryption.

## Operating System Encryption

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

Built-in OS encryption solutions generally leverage hardware security features.

### BitLocker

**BitLocker** is the full volume encryption solution bundled with Microsoft Windows.

### FileVault

**FileVault** is the on-the-fly volume encryption solution built into macOS.

### Linux Unified Key Setup

**LUKS** is the default FDE method for Linux.

## Command-line

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

### Kryptor

**Kryptor** is a free and open-source file encryption and signing tool.

### Tomb

**Tomb** is a command-line shell wrapper for LUKS.

## OpenPGP

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)
- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)
- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)

OpenPGP is sometimes needed for specific tasks such as digitally signing and encrypting email.

### GNU Privacy Guard

**GnuPG** is a GPL-licensed alternative to the PGP suite of cryptographic software.

### GPG4win

**GPG4win** is a package for Windows from Intevation and g10 Code.

### GPG Suite

**GPG Suite** provides OpenPGP support for Apple Mail and other email clients on macOS.

### OpenKeychain

**OpenKeychain** is an implementation of GnuPG for Android.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.**

### Minimum Qualifications

- Cross-platform encryption apps must be open source.
- File encryption apps must support decryption on Linux, macOS, and Windows.
- External disk encryption apps must support decryption on Linux, macOS, and Windows.
- Internal (OS) disk encryption apps must be cross-platform or built in to the operating system natively.

### Best-Case

- Operating System (FDE) encryption apps should utilize hardware security such as a TPM or Secure Enclave.
- File encryption apps should have first- or third-party support for mobile platforms.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
