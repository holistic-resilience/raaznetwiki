---
title: "Protect Your Sensitive Information"
tags: [encryption, data-protection, file-security, privacy, digital-security]
category: "Data Protection"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Encryption", "File Storage Security", "Device Protection"]
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

> **Why this matters:** The less sensitive data you store, the less there is to protect—and the less that can be compromised.

---

## Consider Whether Encryption Is Legal in Your Jurisdiction

Encryption is illegal in some countries. If it is illegal in your country, downloading, installing, or using encryption software might be considered a crime. Police, military, or intelligence services might take your use of encryption software as a pretext to investigate your activities or persecute your organization.

Regardless of what is actually inside your encrypted volumes, and regardless of whether or not this information is legal in your area, the usage of encryption might cast suspicion on you.

**Before proceeding:**
- Investigate how law enforcement has treated encryption in your country
- Research the legal status using the [Global Partners Digital World Map of Encryption Laws and Policies](https://www.gp-digital.org/world-map-of-encryption)
- Think carefully about whether encryption tools are appropriate for your situation

If encryption is legal in your country and travel destinations, skip to [Consider Encrypting Your Whole Device](#consider-encrypting-your-whole-device).

### Alternatives If Encryption Is Illegal

**Store only non-sensitive information**
- Delete data you don't need using secure deletion methods

**Use encrypted cloud storage**
- Consider whether an encrypted cloud service makes sense given your threat model
- Be aware that if adversaries access those servers, they will have more time to attempt breaking into your data

**Use a system of code words**
- Store files normally but use code words to label sensitive names, locations, and activities

**Store on encrypted removable drives**
- Keep sensitive information off your computer by storing it on encrypted USB drives or portable hard drives
- Be aware that external devices are typically more vulnerable to loss and confiscation
- Use strong passwords that are harder to guess or crack

---

## Consider Encrypting Your Whole Device

Full-disk encryption (FDE) protects your files and communications if your device is lost, stolen, or seized. However, FDE only works fully if your device is **powered completely off**, not in sleep mode (suspend or hibernate). If your device is not switched off, someone with physical access may still be able to read or modify your files.

### By Operating System

**Android**
- Devices with Android 10+ are encrypted by default using file-based encryption
- Verify by navigating to **Settings** > **Security** > **Encryption & credentials** and look for **Encryption** or **Encrypt phone**

**iOS**
- iOS devices are encrypted by default when you [set a passcode](https://support.apple.com/en-us/HT204060)

**Linux**
- Full-disk encryption can only be activated during installation
- Follow the [Ubuntu installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop)
- You'll need to create a bootable USB stick ([Windows](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows) | [macOS](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos) | [Ubuntu](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-ubuntu))

**macOS**
- [Enable FileVault](https://support.apple.com/en-us/HT204837) to encrypt your disk

**Windows**
- Use BitLocker (available on Windows 10/11 Pro, Enterprise, or Education)
- See [Microsoft's device encryption documentation](https://support.microsoft.com/en-us/windows/device-encryption-in-windows-ad5dcf4b-dbe0-2331-228f-7925c2a3012d)
- For older devices without TPM:
  1. Press Start, type `gpedit.msc`, press Enter
  2. Double-click **Operating System Drives**
  3. Select **Enabled** and ensure "Allow BitLocker without a compatible TPM" is enabled
  4. Click OK and close the window
  5. [Turn on device encryption](https://support.microsoft.com/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)

**Alternative:** If your computer doesn't support FDE or you prefer open-source tools, use [VeraCrypt](https://veracrypt.io/) to [encrypt your whole device](https://veracrypt.io/en/System%20Encryption.html).

---

## Consider Encrypting Your External Storage Devices

Storing sensitive information on an encrypted external drive (USB stick or portable hard drive) may protect your most important data from adversaries who search your computer.

> **Warning:** External devices are usually more vulnerable to loss and confiscation than computers. Always use strong passwords.

### Cross-Platform Option: VeraCrypt

Use [VeraCrypt](https://veracrypt.io/) on Linux, macOS, or Windows to protect sensitive files. You can either create an encrypted volume within your device or encrypt the entire storage device.

- [Download VeraCrypt](https://veracrypt.io/en/Downloads.html)
- [Beginner's Tutorial](https://veracrypt.io/en/Beginner%27s%20Tutorial.html)
- [How to encrypt a flash drive](https://www.lifewire.com/how-to-encrypt-a-flash-drive-4628341)
- Consider using [portable mode](https://veracrypt.io/en/Portable%20Mode.html) to hide that you're using VeraCrypt

### Platform-Specific Options

**macOS:** Use the built-in Disk Utility to [encrypt storage devices with a password](https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac). Note: encrypted devices will only be accessible on macOS.

**Windows:** Use BitLocker to [encrypt external storage devices](https://www.microsoft.com/en-us/microsoft-365-life-hacks/privacy-and-safety/how-and-why-to-encrypt-usb-flash-drive). Note: encrypted devices will only be accessible on Windows.

### Tails Operating System

[Tails](https://tails.net/about/index.en.html) is an operating system that runs from a USB drive, routes all internet connections through Tor, and erases your history when shut down. You can create an encrypted [persistent storage](https://tails.net/doc/persistent_storage/index.en.html) volume inside the USB stick for sensitive information.

---

## Consider Encrypting Just Some Sensitive Files

You might want to leave non-sensitive files unencrypted so your device doesn't look suspicious if searched. In this case, encrypt only specific files.

### Cross-Platform Option: Cryptomator

[Cryptomator](https://cryptomator.org/) is a free, open-source application that works on Windows, macOS, Linux, Android, and iOS. Originally designed for cloud storage protection, it also works for local files.

- [Cryptomator Documentation](https://docs.cryptomator.org/en/latest/)
- [Getting Started Guide](https://docs.cryptomator.org/en/latest/desktop/getting-started/)

### Platform-Specific Options

**Windows:**
- [Encrypt files in Windows 10](https://support.microsoft.com/en-us/windows/how-to-encrypt-a-file-1131805c-47b8-2e3e-a705-807e13c10da7)
- [Encrypt files in Windows 11](https://www.microsoft.com/en-us/windows/learning-center/how-to-encrypt-file)

**macOS:** Store files in [secure disk images created through Disk Utility](https://support.apple.com/et-ee/guide/disk-utility/dskutl11888/mac#dsku7bb3d28c)

**VeraCrypt (Linux, macOS, Windows):** Store files within an encrypted file container

### Hidden Volumes

When you encrypt information, someone might still see that encrypted data exists and that you've taken steps to protect it. They might try to intimidate or coerce you into unlocking it.

[VeraCrypt's hidden volumes](https://veracrypt.io/en/Hidden%20Volume.html) address this by allowing you to enter a different password to reveal a "decoy" volume with ordinary files, while your truly sensitive data remains hidden.

**Important considerations:**
- Your adversary might know VeraCrypt can hide information this way
- Don't accidentally reveal your hidden volume by leaving it open
- Prevent applications from creating shortcuts to files in hidden volumes

---

## Protect Your Encrypted Folder or Volume

### Unmount When Not in Use

When your encrypted folder or volume is mounted (accessible), your data is vulnerable. Keep it unmounted when not actively reading or modifying files.

**Critical times to unmount:**
- Before walking away from your device
- Before putting your computer to sleep or hibernate
- Before allowing someone else to handle your computer
- Before going through security checkpoints or border crossings (disconnect and shut down completely)
- Before inserting untrusted USB devices

**Proper disconnection procedure:**
1. Close all files being accessed from the encrypted volume
2. Unmount the volume
3. Eject the drive from your operating system
4. Physically disconnect the device

> **Warning:** Simply disconnecting external storage without unmounting may corrupt files.

### Protect Against Malware

Encryption only protects your files if nobody can spy on you while entering your password. Malicious software can reduce the effectiveness of encryption by capturing your credentials.

### Never Access Encrypted Volumes on Untrusted Devices

An adversary may have installed malware on shared computers (like at internet cafes) to steal your passwords and access your encrypted data.

---

## Use Trusted Dealers and Repair Shops

**When buying devices:**
- Have pre-owned devices wiped clean and checked for malware by someone you trust
- If you might be targeted, carefully consider how to find a trustworthy dealer

**When repairing devices:**
- Only use repair shops or technicians you trust
- Repair shops have sometimes been known to spy on devices or copy and sell data
- If you're a public figure, consider having someone else interact with repair providers on your behalf

---

## Related Resources

- [How to Destroy Sensitive Information](https://securityinabox.org/en/files/destroy-sensitive-information)
- [Create and Maintain Strong Passwords](https://securityinabox.org/en/passwords/passwords)
- [Protect Against Malware](https://securityinabox.org/en/phones-and-computers/malware/)