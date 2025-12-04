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

**Cryptomator** is an encryption solution designed for privately saving files to any cloud [Service Provider](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers), eliminating the need to trust that they won't access your files. It allows you to create vaults that are stored on a virtual drive, the contents of which are encrypted and synced with your cloud storage provider.

[Homepage](https://cryptomator.org/) [Privacy Policy](https://cryptomator.org/privacy "Privacy Policy") [Documentation](https://docs.cryptomator.org/ "Documentation") [Source Code](https://github.com/cryptomator "Source Code") [Contribute](https://cryptomator.org/donate "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=org.cryptomator)
- [App Store](https://apps.apple.com/app/id1560822163)
- [Android](https://cryptomator.org/android)
- [Windows](https://cryptomator.org/downloads)
- [macOS](https://cryptomator.org/downloads)
- [Linux](https://cryptomator.org/downloads)
- [Flathub](https://flathub.org/apps/details/org.cryptomator.Cryptomator)

Cryptomator uses AES-256 encryption to encrypt both files and filenames. Cryptomator cannot encrypt metadata such as access, modification, and creation timestamps, nor the number and size of files and folders.

Cryptomator is free to use on all desktop platforms, as well as on iOS in "read only" mode. Cryptomator offers [paid](https://cryptomator.org/pricing) apps with full functionality on iOS and Android. The Android version can be purchased anonymously via [ProxyStore](https://cryptomator.org/coop/proxystore).

Some Cryptomator cryptographic libraries have been [audited](https://community.cryptomator.org/t/has-there-been-a-security-review-audit-of-cryptomator/44) by Cure53. The scope of the audited libraries includes: [cryptolib](https://github.com/cryptomator/cryptolib), [cryptofs](https://github.com/cryptomator/cryptofs), [siv-mode](https://github.com/cryptomator/siv-mode) and [cryptomator-objc-cryptor](https://github.com/cryptomator/cryptomator-objc-cryptor). The audit did not extend to [cryptolib-swift](https://github.com/cryptomator/cryptolib-swift), which is a library used by Cryptomator for iOS.

Cryptomator's documentation details its intended [security target](https://docs.cryptomator.org/en/latest/security/security-target), [security architecture](https://docs.cryptomator.org/en/latest/security/architecture), and [best practices](https://docs.cryptomator.org/en/latest/security/best-practices) for use in further detail.

### VeraCrypt (Disk)

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

![VeraCrypt logo](https://www.privacyguides.org/en/assets/img/encryption-software/veracrypt.svg#only-light)![VeraCrypt logo](https://www.privacyguides.org/en/assets/img/encryption-software/veracrypt-dark.svg#only-dark)

**VeraCrypt** is a source-available freeware utility used for on-the-fly encryption. It can create a virtual encrypted disk within a file, encrypt a partition, or encrypt the entire storage device with pre-boot authentication.

[Homepage](https://veracrypt.fr/) [Documentation](https://veracrypt.fr/en/Documentation.html "Documentation") [Source Code](https://veracrypt.fr/code "Source Code") [Contribute](https://veracrypt.fr/en/Donation.html "Contribute")

Downloads

- [Windows](https://veracrypt.fr/en/Downloads.html)
- [macOS](https://veracrypt.fr/en/Downloads.html)
- [Linux](https://veracrypt.fr/en/Downloads.html)

VeraCrypt is a fork of the discontinued TrueCrypt project. According to its developers, security improvements have been implemented and issues raised by the initial TrueCrypt code audit have been addressed.

When encrypting with VeraCrypt, you have the option to select from different [hash functions](https://en.wikipedia.org/wiki/VeraCrypt#Encryption_scheme). We suggest you **only** select [SHA-512](https://en.wikipedia.org/wiki/SHA-512) and stick to the [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) block cipher.

TrueCrypt has been [audited a number of times](https://en.wikipedia.org/wiki/TrueCrypt#Security_audits), and VeraCrypt has also been [audited separately](https://en.wikipedia.org/wiki/VeraCrypt#VeraCrypt_audit).

## Operating System Encryption

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

Built-in OS encryption solutions generally leverage hardware security features such as a [secure cryptoprocessor](https://www.privacyguides.org/en/basics/hardware/#tpmsecure-cryptoprocessor). Therefore, we recommend using the built-in encryption solutions for your operating system. For cross-platform encryption, we still recommend [cross-platform tools](https://www.privacyguides.org/en/encryption/#multi-platform) for additional flexibility and to avoid vendor lock-in.

### BitLocker

![BitLocker logo](https://www.privacyguides.org/en/assets/img/encryption-software/bitlocker.png)

**BitLocker** is the full volume encryption solution bundled with Microsoft Windows that uses the Trusted Platform Module ( [TPM](https://learn.microsoft.com/windows/security/information-protection/tpm/how-windows-uses-the-tpm)) for hardware-based security.

[Documentation](https://learn.microsoft.com/windows/security/information-protection/BitLocker/BitLocker-overview "Documentation")

BitLocker is [officially supported](https://support.microsoft.com/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838) on the Pro, Enterprise, and Education editions of Windows. It can be enabled on Home editions provided that they meet the following prerequisites.

Enabling BitLocker on Windows Home

To enable BitLocker on "Home" editions of Windows, you must have partitions formatted with a [GUID Partition Table](https://en.wikipedia.org/wiki/GUID_Partition_Table) and have a dedicated TPM (v1.2, 2.0+) module. You may need to [disable the non-Bitlocker "Device encryption" functionality](https://discuss.privacyguides.net/t/enabling-bitlocker-on-the-windows-11-home-edition/13303/5) (which is inferior because it sends your recovery key to Microsoft's servers) if it is enabled on your device already before following this guide.

1. Open a command prompt and check your drive's partition table format with the following command. You should see " **GPT**" listed under "Partition Style":



```
powershell Get-Disk
```

2. Run this command (in an admin command prompt) to check your TPM version. You should see `2.0` or `1.2` listed next to `SpecVersion`:



```
powershell Get-WmiObject -Namespace "root/cimv2/security/microsofttpm" -Class WIN32_tpm
```

3. Access [Advanced Startup Options](https://support.microsoft.com/windows/advanced-startup-options-including-safe-mode-b90e7808-80b5-a291-d4b8-1a1af602b617). You need to reboot while pressing the F8 key before Windows starts and go into the _command prompt_ in **Troubleshoot** → **Advanced Options** → **Command Prompt**.

4. Login with your admin account and type this in the command prompt to start encryption:



```
manage-bde -on c: -used
```

5. Close the command prompt and continue booting to regular Windows.

6. Open an admin command prompt and run the following commands:



```
manage-bde c: -protectors -add -rp -tpm
manage-bde -protectors -enable c:
manage-bde -protectors -get c: > %UserProfile%\Desktop\BitLocker-Recovery-Key.txt
```


Tip

Backup `BitLocker-Recovery-Key.txt` on your Desktop to a separate storage device. Loss of this recovery code may result in loss of data.

### FileVault

![FileVault logo](https://www.privacyguides.org/en/assets/img/encryption-software/filevault.png)

**FileVault** is the on-the-fly volume encryption solution built into macOS. FileVault takes advantage of the [hardware security capabilities](https://www.privacyguides.org/en/os/macos-overview/#hardware-security) present on an Apple Silicon SoC or T2 Security Chip.

[Documentation](https://support.apple.com/guide/mac-help/encrypt-mac-data-with-filevault-mh11785/mac "Documentation")

We advise against using your iCloud account for recovery; instead, you should securely store a local recovery key on a separate storage device.

### Linux Unified Key Setup

![LUKS logo](https://www.privacyguides.org/en/assets/img/encryption-software/luks.png)

**LUKS** is the default FDE method for Linux. It can be used to encrypt full volumes, partitions, or create encrypted containers.

[Repository](https://gitlab.com/cryptsetup/cryptsetup#what-the-) [Documentation](https://gitlab.com/cryptsetup/cryptsetup/-/wikis/home "Documentation") [Source Code](https://gitlab.com/cryptsetup/cryptsetup "Source Code")

Creating and opening encrypted containers

```
dd if=/dev/urandom of=/path-to-file bs=1M count=1024 status=progress
sudo cryptsetup luksFormat /path-to-file
```

#### Opening encrypted containers

We recommend opening containers and volumes with `udisksctl` as this uses [Polkit](https://en.wikipedia.org/wiki/Polkit). Most file managers, such as those included with popular desktop environments, can unlock encrypted files. Tools like [udiskie](https://github.com/coldfix/udiskie) can run in the system tray and provide a helpful user interface.

```
udisksctl loop-setup -f /path-to-file
udisksctl unlock -b /dev/loop0
```

Remember to back up volume headers

We recommend you always [back up your LUKS headers](https://wiki.archlinux.org/title/Dm-crypt/Device_encryption#Backup_and_restore) in case of partial drive failure. This can be done with:

```
cryptsetup luksHeaderBackup /dev/device --header-backup-file /mnt/backup/file.img
```

## Command-line

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

Tools with command-line interfaces are useful for integrating [shell scripts](https://en.wikipedia.org/wiki/Shell_script).

### Kryptor

![Kryptor logo](https://www.privacyguides.org/en/assets/img/encryption-software/kryptor.png)

**Kryptor** is a free and open-source file encryption and signing tool that makes use of modern and secure cryptographic algorithms. It aims to be a better version of [age](https://github.com/FiloSottile/age) and [Minisign](https://jedisct1.github.io/minisign) to provide a simple, easier alternative to GPG.

[Homepage](https://kryptor.co.uk/) [Privacy Policy](https://kryptor.co.uk/features#privacy "Privacy Policy") [Documentation](https://kryptor.co.uk/tutorial "Documentation") [Source Code](https://github.com/samuel-lucas6/Kryptor "Source Code") [Contribute](https://kryptor.co.uk/#donate "Contribute")

Downloads

- [Windows](https://kryptor.co.uk/)
- [macOS](https://kryptor.co.uk/)
- [Linux](https://kryptor.co.uk/)

### Tomb

![Tomb logo](https://www.privacyguides.org/en/assets/img/encryption-software/tomb.png)

**Tomb** is a command-line shell wrapper for LUKS. It supports steganography via [third-party tools](https://dyne.org/software/tomb/#advanced-usage).

[Homepage](https://dyne.org/software/tomb) [Documentation](https://github.com/dyne/Tomb/wiki "Documentation") [Source Code](https://github.com/dyne/Tomb "Source Code") [Contribute](https://dyne.org/donate "Contribute")

## OpenPGP

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)
- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)
- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)

OpenPGP is sometimes needed for specific tasks such as digitally signing and encrypting email. PGP has many features and is [complex](https://latacora.micro.blog/2019/07/16/the-pgp-problem.html) as it has been around a long time. For tasks such as signing or encrypting files, we suggest the above options.

When encrypting with PGP, you have the option to configure different options in your `gpg.conf` file. We recommend staying with the standard options specified in the [GnuPG user FAQ](https://gnupg.org/faq/gnupg-faq.html#new_user_gpg_conf).

Use future defaults when generating a key

When [generating keys](https://gnupg.org/gph/en/manual/c14.html) we suggest using the `future-default` command as this will instruct GnuPG use modern cryptography such as [Curve25519](https://en.wikipedia.org/wiki/Curve25519#History) and [Ed25519](https://ed25519.cr.yp.to/):

```
gpg --quick-gen-key alice@example.com future-default
```

### GNU Privacy Guard

![GNU Privacy Guard logo](https://www.privacyguides.org/en/assets/img/encryption-software/gnupg.svg)

**GnuPG** is a GPL-licensed alternative to the PGP suite of cryptographic software. GnuPG is compliant with [RFC 4880](https://tools.ietf.org/html/rfc4880), which is the current IETF specification of OpenPGP. The GnuPG project has been working on an [updated draft](https://datatracker.ietf.org/doc/draft-ietf-openpgp-crypto-refresh) in an attempt to modernize OpenPGP. GnuPG is a part of the Free Software Foundation's GNU software project and has received major [funding](https://gnupg.org/blog/20220102-a-new-future-for-gnupg.html) from the German government.

[Homepage](https://gnupg.org/) [Privacy Policy](https://gnupg.org/privacy-policy.html "Privacy Policy") [Documentation](https://gnupg.org/documentation/index.html "Documentation") [Source Code](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gnupg.git "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=org.sufficientlysecure.keychain)
- [Windows](https://gpg4win.org/download.html)
- [macOS](https://gpgtools.org/)
- [Linux](https://gnupg.org/download/index.html#binary)

### GPG4win

![GPG4win logo](https://www.privacyguides.org/en/assets/img/encryption-software/gpg4win.svg)

**GPG4win** is a package for Windows from [Intevation and g10 Code](https://gpg4win.org/impressum.html). It includes [various tools](https://gpg4win.org/about.html) that can assist you in using GPG on Microsoft Windows. The project was initiated and originally [funded by](https://web.archive.org/web/20190425125223/https://joinup.ec.europa.eu/news/government-used-cryptography) Germany's Federal Office for Information Security (BSI) in 2005.

[Homepage](https://gpg4win.org/) [Privacy Policy](https://gpg4win.org/privacy-policy.html "Privacy Policy") [Documentation](https://gpg4win.org/documentation.html "Documentation") [Source Code](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpg4win.git;a=summary "Source Code") [Contribute](https://gpg4win.org/donate.html "Contribute")

Downloads

- [Windows](https://gpg4win.org/download.html)

### GPG Suite

![GPG Suite logo](https://www.privacyguides.org/en/assets/img/encryption-software/gpgsuite.png)

**GPG Suite** provides OpenPGP support for [Apple Mail](https://www.privacyguides.org/en/email-clients/#apple-mail-macos) and other email clients on macOS.

We recommend taking a look at their [First steps](https://gpgtools.tenderapp.com/kb/how-to/first-steps-where-do-i-start-where-do-i-begin-setup-gpgtools-create-a-new-key-your-first-encrypted-email) and [Knowledge Base](https://gpgtools.tenderapp.com/kb) for support.

[Homepage](https://gpgtools.org/) [Privacy Policy](https://gpgtools.org/privacy "Privacy Policy") [Documentation](https://gpgtools.tenderapp.com/kb "Documentation") [Source Code](https://github.com/GPGTools "Source Code")

Downloads

- [macOS](https://gpgtools.org/)

Currently, GPG Suite does [not yet](https://gpgtools.com/sequoia) have a stable release for macOS Sonoma and later.

### OpenKeychain

![OpenKeychain logo](https://www.privacyguides.org/en/assets/img/encryption-software/openkeychain.svg)

**OpenKeychain** is an implementation of GnuPG for Android. It's commonly required by mail clients such as [Thunderbird](https://www.privacyguides.org/en/email-clients/#thunderbird), [FairEmail](https://www.privacyguides.org/en/email-clients/#fairemail-android), and other Android apps to provide encryption support.

[Homepage](https://openkeychain.org/) [Privacy Policy](https://openkeychain.org/help/privacy-policy "Privacy Policy") [Documentation](https://openkeychain.org/faq "Documentation") [Source Code](https://github.com/open-keychain/open-keychain "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=org.sufficientlysecure.keychain)

Cure53 completed a [security audit](https://openkeychain.org/openkeychain-3-6) of OpenKeychain 3.6 in October 2015. The published audit and OpenKeychain's solutions to the issues raised in the audit can be found [here](https://github.com/open-keychain/open-keychain/wiki/cure53-Security-Audit-2015).

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

### Minimum Qualifications

- Cross-platform encryption apps must be open source.
- File encryption apps must support decryption on Linux, macOS, and Windows.
- External disk encryption apps must support decryption on Linux, macOS, and Windows.
- Internal (OS) disk encryption apps must be cross-platform or built in to the operating system natively.

### Best-Case

Our best-case criteria represents what we would like to see from the perfect project in this category. Our recommendations may not include any or all of this functionality, but those which do may rank higher than others on this page.

- Operating System (FDE) encryption apps should utilize hardware security such as a TPM or Secure Enclave.
- File encryption apps should have first- or third-party support for mobile platforms.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).