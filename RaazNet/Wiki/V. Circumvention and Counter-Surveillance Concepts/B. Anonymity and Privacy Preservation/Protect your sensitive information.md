---
title: "Protect Your Sensitive Information"
tags: [encryption, data-protection, file-security, privacy, device-security]
category: "Data Protection"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Encryption", "Secure File Storage", "Device Security"]
summary: "Comprehensive guide to protecting sensitive data through encryption, secure storage practices, and device protection strategies."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file management"]
estimated_read_time: "15 minutes"
---

# Protect Your Sensitive Information

Intruders may be able to read or modify your data if they manage to get hold of your device. It is always best to have several layers of defence against this possibility. Encrypting your entire devices as well as individual files is one important form of protection.

Encryption is a way for software to scramble your information using advanced mathematics, leaving you and only you with the key to unscramble it (in the form of a password, passphrase, or encryption key). Think of encrypting your device like keeping your information in a locked safe with a combination that only you know.

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
- Research the legal status of encryption: [Global Partners Digital World Map of Encryption Laws](https://www.gp-digital.org/world-map-of-encryption)

If encryption is legal in your country, skip to [Consider Encrypting Your Whole Device](#consider-encrypting-your-whole-device).

### Alternatives If Encryption Is Illegal

**Store only non-sensitive information**
Delete data you don't need using secure deletion methods.

**Use an encrypted cloud account**
Consider whether an encrypted cloud service would be wise given your threat model. While these services protect your data, if adversaries gain access to those servers, they will have more time to attempt to break into your data without you detecting the intrusion.

**Use a system of code words**
Store files normally but use code words to label sensitive names, locations, and activities.

**Store to an encrypted removable drive**
Keep sensitive information off your computer by storing it on an encrypted USB memory stick or portable hard drive. Be aware that external devices are typically even more vulnerable to loss and confiscation than computers.

---

## Consider Encrypting Your Whole Device

Full-disk encryption (FDE) protects your files and communications if your device is lost, stolen, or seized.

> **Important:** Full-disk encryption only works fully if your device is powered completely off, not in sleep mode (also known as "suspend" or "hibernate"). If your device is not switched off, someone with physical access may be able to read or modify your files.

### Android

Most devices with Android 10 and higher use file-based encryption by default.

**To verify encryption is enabled:**
Navigate to **Settings** > **Security** > **Encryption & credentials** and look for **Encryption** or **Encrypt phone**. Menu options may vary by device.

### iOS

iOS devices are encrypted by default when you [set a passcode to access them](https://support.apple.com/en-us/HT204060).

### Linux

Full-disk encryption can only be activated during Linux installation. You will need to reinstall if FDE is not currently enabled.

**Resources:**
- [Ubuntu installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop)
- Create a bootable USB stick: [Windows](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows) | [macOS](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos) | [Ubuntu](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-ubuntu)

### macOS

[Turn FileVault on to encrypt your disk](https://support.apple.com/en-us/HT204837).

### Windows

Use BitLocker, available on Windows 10 or 11 Pro, Enterprise, or Education editions.

- [Official Windows encryption documentation](https://support.microsoft.com/en-us/windows/device-encryption-in-windows-ad5dcf4b-dbe0-2331-228f-7925c2a3012d)

**For older devices without TPM:**
1. Press Start, type `gpedit.msc`, and press Enter
2. Double-click **Operating System Drives**
3. Select **Enabled** and ensure **Allow BitLocker without a compatible TPM** is enabled
4. Click OK and close the Local Group Policy Editor
5. [Turn on device encryption](https://support.microsoft.com/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)

**Alternative:** If your computer doesn't support full-disk encryption or you prefer open-source tools, use [VeraCrypt](https://veracrypt.io/) to [encrypt your whole device](https://veracrypt.io/en/System%20Encryption.html).

---

## Consider Encrypting Your External Storage Devices

Storing sensitive information in an encrypted storage device like a USB stick or portable hard drive may protect your most important data from adversaries who search your computer.

> **Note:** External devices are usually more vulnerable than computers to loss and confiscation. Always use a strong password. See [Create and maintain strong passwords](https://securityinabox.org/en/passwords/passwords).

### Cross-Platform: VeraCrypt

Use [VeraCrypt](https://veracrypt.io/) to protect sensitive files on any operating system. You can create an encrypted volume within your external device or encrypt the entire storage device.

- [Download VeraCrypt](https://veracrypt.io/en/Downloads.html)
- [Beginner's Tutorial](https://veracrypt.io/en/Beginner%27s%20Tutorial.html)
- [How to encrypt a flash drive](https://www.lifewire.com/how-to-encrypt-a-flash-drive-4628341)
- Consider using [portable mode](https://veracrypt.io/en/Portable%20Mode.html) to hide that you're using VeraCrypt

### macOS: Disk Utility

Use the built-in Disk Utility to encrypt external storage devices. Note: encrypted devices will only be accessible on macOS systems.

- [Encrypt and protect a storage device with a password](https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac)

### Windows: BitLocker

Use BitLocker (Windows 10/11 Pro, Enterprise, or Education) to encrypt external storage devices. Note: encrypted devices will only be accessible on Windows systems.

- [How to encrypt an external storage device with BitLocker](https://www.microsoft.com/en-us/microsoft-365-life-hacks/privacy-and-safety/how-and-why-to-encrypt-usb-flash-drive)

### Tails

[Tails](https://tails.net/about/index.en.html) is an operating system that runs from a USB drive, protects all internet connections using Tor, and erases your history when shut down. You can create an encrypted [persistent storage](https://tails.net/doc/persistent_storage/index.en.html) volume for sensitive information.

---

## Consider Encrypting Just Some Sensitive Files

You might find it useful to leave non-sensitive files un-encrypted so that if your device is searched, it contains ordinary, everyday files and communications rather than appearing suspicious.

### Cross-Platform: Cryptomator

[Cryptomator](https://cryptomator.org/) is a free, open-source application that works on Windows, macOS, Linux, Android, and iOS. Originally designed for cloud storage protection, it can also encrypt local files.

- [Cryptomator Documentation](https://docs.cryptomator.org/en/latest/)
- [Getting Started Guide](https://docs.cryptomator.org/en/latest/desktop/getting-started/)

### Windows

- [How to encrypt a file in Windows 10](https://support.microsoft.com/en-us/windows/how-to-encrypt-a-file-1131805c-47b8-2e3e-a705-807e13c10da7)
- [How to encrypt a file in Windows 11](https://www.microsoft.com/en-us/windows/learning-center/how-to-encrypt-file)

### macOS

Protect individual files by storing them in [a secure disk image created through Disk Utility](https://support.apple.com/et-ee/guide/disk-utility/dskutl11888/mac#dsku7bb3d28c).

### VeraCrypt (Linux, macOS, Windows)

Protect individual files by storing them within an encrypted file container.

- [Download VeraCrypt](https://veracrypt.io/en/Downloads.html)
- [How to use VeraCrypt](https://veracrypt.io/en/Beginner's%20Tutorial.html)

### Consider Hidden Volumes

When you encrypt your information, nobody else can read it, but someone might still see that encrypted data exists and that you have taken steps to protect it. An adversary might try to intimidate, blackmail, interrogate, or torture you to unlock that encryption.

[VeraCrypt](https://veracrypt.io/) allows you to create a ["hidden volume"](https://veracrypt.io/en/Hidden%20Volume.html). To open a hidden volume, you enter a different password from your standard volume. If an intruder becomes suspicious about your encrypted files, they cannot prove hidden ones exist.

VeraCrypt disguises your encrypted information as other, less sensitive data (like music files or ordinary documents). It is generally considered impossible to determine whether an encrypted volume contains a hidden volume.

**Cautions:**
- Your adversary might know that VeraCrypt can hide information this way
- Do not accidentally reveal your hidden volume by leaving it open
- Prevent other applications from creating shortcuts to files in the hidden volume

---

## Protect Your Encrypted Folder or Volume

### Unmount When Not in Use

When your encrypted folder or volume is mounted (accessible), your data may be vulnerable. Keep it unmounted when you are not actively reading or modifying files.

**Always unmount before:**
- Walking away from your device for any length of time
- Putting your computer to sleep, suspend, or hibernate
- Allowing someone else to handle your computer
- Going through security checkpoints or border crossings
- Inserting an untrusted USB memory stick or external storage device

**For external drives:**
Simply disconnecting may corrupt files. Always unmount the volume first, then eject the drive from your operating system before physically disconnecting. All accessed files must be closed before unmounting.

### Protect Against Malware

Encryption only protects your files if nobody can spy on you when you enter your password. Malicious software can reduce the effectiveness of your protective measures.

**Learn more:** [Security in a Box guide on malware protection](https://securityinabox.org/en/phones-and-computers/malware/)

### Don't Access Encrypted Files on Untrusted Devices

An adversary may have installed malware on devices not in your control, like shared computers at internet cafes. They could steal your passwords and gain access to your encrypted data.

---

## Use Trusted Dealers and Repair Shops

- **Pre-owned devices:** Have someone you trust wipe the device clean and check for malware
- **New purchases:** If you believe someone might target you by pre-installing malware, carefully consider how to find a trustworthy dealer
- **Repairs:** Ensure you trust the repair shop or person before handing over your device

Repair shops have sometimes been known to spy on devices or copy and sell data. If you are a well-known public figure, consider having someone you trust interact with repair providers on your behalf.

---

## Additional Resources

- [How to destroy sensitive information](https://securityinabox.org/en/files/destroy-sensitive-information)
- [Create and maintain strong passwords](https://securityinabox.org/en/passwords/passwords)
- [VeraCrypt](https://veracrypt.io/)
- [Cryptomator](https://cryptomator.org/)
- [Tails](https://tails.net/)
- [Global Partners Digital - Encryption Laws Map](https://www.gp-digital.org/world-map-of-encryption)