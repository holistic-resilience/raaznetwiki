---
title: "Protect Your Sensitive Information"
tags: [encryption, data-protection, file-security, privacy, digital-security, veracrypt]
category: "Data Protection"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Encryption", "File Storage", "Device Security", "Data Privacy"]
summary: "Comprehensive guide to protecting sensitive data through encryption, secure storage practices, and device security measures."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file management"]
estimated_read_time: "15 minutes"
---

# Protect Your Sensitive Information

Intruders may be able to read or modify your data if they manage to get hold of your device. It is always best to have several layers of defence against this possibility. Encrypting your entire devices as well as individual files is one important form of protection.

Encryption is a way for software to scramble your information using advanced mathematics, leaving you and only you with the key to unscramble it (in the form of a password, passphrase, or encryption key). Think of it like keeping your information in a locked safe with a combination that only you know.

---

## Consider Deleting Old Data Instead of Storing It

Storing confidential data can be a risk for you and for the people you work with. Encryption reduces this risk but does not eliminate it. The first step to protecting sensitive information is to reduce how much of it you keep around. Unless you have a good reason to store a particular file, or a particular category of information within a file, you should simply delete it securely.

**Learn more:** [How to destroy sensitive information](https://securityinabox.org/en/files/destroy-sensitive-information)

---

## Consider Whether Encryption Is Legal in Your Jurisdiction

Encryption is illegal in some countries. If it is illegal in your country, downloading, installing, or using encryption software might be considered a crime. Police, military, or intelligence services might take your use of encryption software as a pretext to investigate your activities or persecute your organization.

Regardless of what is actually inside your encrypted volumes, and regardless of whether or not this information is legal in your area, the usage of encryption might cast suspicion on you.

**Before proceeding:**
- Investigate how law enforcement has treated encryption in your country
- Think carefully about whether encryption tools are appropriate for your situation
- Research the legal status of encryption in your country: [Global Partners Digital World Map of Encryption Laws](https://www.gp-digital.org/world-map-of-encryption)

If encryption is not illegal in your country or in the countries you're travelling to, skip to [Consider Encrypting Your Whole Device](#consider-encrypting-your-whole-device).

### Alternatives If Encryption Is Illegal

**Store only non-sensitive information**
- Delete data you don't need
- Learn to [destroy sensitive information](https://securityinabox.org/en/files/destroy-sensitive-information) securely

**Store to an encrypted cloud account**
- Consider whether using an encrypted cloud service is wise given your threat model
- Be aware that adversaries with server access will have more time to attempt breaking your encryption

**Use a system of code words**
- Store files normally but use code words for sensitive names, locations, and activities

**Store to an encrypted removable drive**
- Keep sensitive information off your computer on an encrypted USB or portable hard drive
- Be aware that external devices are more vulnerable to loss and confiscation
- Use a strong password that is harder to guess or crack

---

## Consider Encrypting Your Whole Device

Full-disk encryption (FDE) protects your files and communications if your device is lost, stolen, or seized.

> **Important:** Full-disk encryption only works fully if your device is powered completely off, not in sleep mode (suspend/hibernate). If your device is not switched off, someone with physical access may still be able to read or modify your files.

### Android

Most devices with Android 10 and higher use file-based encryption by default.

**To verify encryption is enabled:**
Navigate to **Settings** > **Security** > **Encryption & credentials** and look for **Encryption** or **Encrypt phone**. (Menu options may vary by device.)

### iOS

iOS devices are encrypted by default when you [set a passcode](https://support.apple.com/en-us/HT204060).

### Linux

Full-disk encryption can only be activated during Linux installation. You will need to reinstall if FDE is not already enabled.

**Resources:**
- [Ubuntu installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop)
- Create a bootable USB stick: [Windows](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows) | [macOS](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos) | [Ubuntu](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-ubuntu)

### macOS

[Turn FileVault on](https://support.apple.com/en-us/HT204837) to encrypt your computer's disk.

### Windows

Use BitLocker, available on Windows 10 or 11 Pro, Enterprise, or Education editions.

- [Official Windows encryption documentation](https://support.microsoft.com/en-us/windows/device-encryption-in-windows-ad5dcf4b-dbe0-2331-228f-7925c2a3012d)

**For older devices without TPM:**
1. Press Start, type `gpedit.msc`, and press Enter
2. Double-click **Operating System Drives**
3. Select **Enabled** and ensure **Allow BitLocker without a compatible TPM** is enabled
4. Click OK and close the Local Group Policy Editor
5. [Turn on device encryption](https://support.microsoft.com/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)

### Alternative: VeraCrypt

If your computer does not support full-disk encryption or you prefer a free, open-source tool, use [VeraCrypt](https://veracrypt.io/) to [encrypt your whole device](https://veracrypt.io/en/System%20Encryption.html).

---

## Consider Encrypting Your External Storage Devices

Storing sensitive information on an encrypted external device (USB stick or portable hard drive) can protect your most important data from adversaries who search your computer.

> **Warning:** External devices are usually more vulnerable to loss and confiscation than computers. Always use a strong password.

### Cross-Platform: VeraCrypt

Works on Linux, macOS, and Windows. You can create an encrypted volume within your device or encrypt the entire storage device.

- [Download VeraCrypt](https://veracrypt.io/en/Downloads.html)
- [Beginner's Tutorial](https://veracrypt.io/en/Beginner%27s%20Tutorial.html)
- [How to encrypt a flash drive](https://www.lifewire.com/how-to-encrypt-a-flash-drive-4628341)
- Consider using [portable mode](https://veracrypt.io/en/Portable%20Mode.html) to hide that you're using VeraCrypt

### macOS: Disk Utility

Use the built-in Disk Utility to encrypt external storage devices. Note: encrypted devices will only be accessible on macOS systems.

- [Encrypt and protect a storage device with a password](https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac)

### Windows: BitLocker

Available on Windows 10 and 11 Pro, Enterprise, or Education. Note: encrypted devices will only be accessible on Windows systems.

- [How to encrypt an external storage device with BitLocker](https://www.microsoft.com/en-us/microsoft-365-life-hacks/privacy-and-safety/how-and-why-to-encrypt-usb-flash-drive)

### Tails

Tails is an operating system that runs from a USB drive, routes all internet connections through Tor, and erases your history on shutdown. You can create an encrypted persistent storage volume for sensitive information.

- [About Tails](https://tails.net/about/index.en.html)
- [Tails persistent storage](https://tails.net/doc/persistent_storage/index.en.html)

---

## Consider Encrypting Just Some Sensitive Files

You might want to leave non-sensitive files unencrypted so your device doesn't look suspicious if searched. In this case, encrypt only specific files.

### Cross-Platform: Cryptomator

Works on Windows, macOS, Linux, Android, and iOS. Originally created for protecting cloud-stored files, but also works for local encryption.

- [Cryptomator](https://cryptomator.org/)
- [Documentation](https://docs.cryptomator.org/en/latest/)
- [Getting Started guide](https://docs.cryptomator.org/en/latest/desktop/getting-started/)

### Windows

- [Encrypt a file in Windows 10](https://support.microsoft.com/en-us/windows/how-to-encrypt-a-file-1131805c-47b8-2e3e-a705-807e13c10da7)
- [Encrypt a file in Windows 11](https://www.microsoft.com/en-us/windows/learning-center/how-to-encrypt-file)

### macOS

Protect individual files by storing them in [a secure disk image](https://support.apple.com/et-ee/guide/disk-utility/dskutl11888/mac#dsku7bb3d28c) created through Disk Utility.

### VeraCrypt (Linux, macOS, Windows)

Protect individual files by storing them within an encrypted file container.

- [Download VeraCrypt](https://veracrypt.io/en/Downloads.html)
- [Beginner's Tutorial](https://veracrypt.io/en/Beginner's%20Tutorial.html)

### Hidden Volumes

When you encrypt information, someone might still see that encrypted data exists and that you've taken steps to protect it. They might try to coerce you into unlocking it.

[VeraCrypt hidden volumes](https://veracrypt.io/en/Hidden%20Volume.html) address this by allowing you to create a concealed encrypted space within your regular encrypted volume. To access the hidden volume, you enter a different password than for the standard volume.

**How it works:**
- VeraCrypt disguises encrypted information as less sensitive data (like music files)
- It is generally impossible to detect whether a hidden volume exists
- If coerced, you can provide the standard volume password, revealing only "decoy" material

**Caveats:**
- Your adversary may know VeraCrypt can hide information this way
- Don't accidentally reveal your hidden volume by leaving it open
- Prevent applications from creating shortcuts to files in the hidden volume

---

## Protect Your Encrypted Folder or Volume

### Unmount and Disconnect Properly

When your encrypted folder or volume is mounted (accessible), your data may be vulnerable. Keep it unmounted when not actively reading or modifying files.

**For external encrypted drives:**
1. Close all files being accessed from the volume
2. Unmount the volume
3. Eject the drive from your operating system
4. Physically disconnect the device

Simply disconnecting without unmounting may corrupt files. Practice this workflow until you can do it quickly in an emergency.

**Unmount your encrypted volumes:**
- Before walking away from your device for any length of time
- Before putting your computer to sleep (suspend/hibernate)
- Before allowing someone else to handle your computer
- Before going through security checkpoints or border crossings (shut down completely)
- Before inserting untrusted USB devices, including those from friends or colleagues

### Protect Your Device Against Malware

Encryption only protects your files if nobody can spy on you when entering your password. Malicious software can reduce the effectiveness of your encryption.

**Learn more:** [Security in a Box guide on malware protection](https://securityinabox.org/en/phones-and-computers/malware/)

### Don't Access Encrypted Volumes on Untrusted Devices

An adversary may have installed malware on devices not in your control (like shared computers at internet cafes) to steal your passwords and access your encrypted data.

---

## Use Trusted Dealers and Repair Shops

**When buying devices:**
- For pre-owned devices, have someone you trust wipe them clean and check for malware
- If you might be targeted, carefully consider how to find a trustworthy dealer
- When possible, buy new devices

**When repairing devices:**
- Only use repair shops or people you trust
- Repair shops have been known to spy on devices or copy and sell data
- If you're a public figure, consider having someone else interact with repair providers to avoid raising curiosity about your device's contents

---

*Updated 13 March 2024*

*Source: [Security in a Box](https://securityinabox.org/en/files/secure-file-storage/)*