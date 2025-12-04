---
title: "Destroy Sensitive Information"
tags: [data-destruction, secure-deletion, privacy, digital-security, device-disposal]
category: "Data Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Secure Data Deletion", "Device Disposal", "Privacy Protection"]
summary: "Comprehensive guide on securely erasing files, wiping devices, and safely disposing of computers and phones to prevent data recovery."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file systems"]
estimated_read_time: "10 minutes"
---

# Destroy Sensitive Information

When you drag a file to the Trash and empty it, your device doesn't actually delete that file. It simply marks that space as available for new data. Until your device saves something else in that space, the original file can still be recovered by someone with access to your device and the right tools.

Secure deletion tools do more than just remove files—they overwrite the data multiple times with random information, ensuring no trace of the original file remains. Security experts agree that "wiping" unused space this way effectively prevents intruders from reading your erased files.

> [!warning] SSD Limitation
> **Solid-state drives (SSDs), USB sticks, and SD cards may not fully erase their contents** due to a technique called "wear leveling." To protect data on SSD drives, [encrypt these drives](https://securityinabox.org/en/files/secure-file-storage#consider-encrypting-your-external-storage-devices) as soon as possible—especially before disposal or re-use. Learn more in the [EFF guide on deleting data securely](https://ssd.eff.org/en/module/how-delete-your-data-securely-macos#SSDs).

---

## Clean Traces of Your Work

Set a regular schedule to wipe your device's unused memory. This ensures sensitive files don't remain on hard drives, USB sticks, SD cards, or any device storing sensitive information.

### By Platform

#### Android
1. Use [CCleaner for Android](https://www.ccleaner.com/ccleaner-android) to remove temporary files, application cache, browser history, clipboard content, and old call logs. See [their setup guide](https://support.ccleaner.com/s/article/running-ccleaner-for-android-for-the-first-time).
2. Use [Extirpater](https://f-droid.org/packages/us.spotco.extirpater/) to wipe free space. Install via [F-Droid](https://f-droid.org/) (not available on Google Play).

> [!caution]
> Use Extirpater sparingly—frequent use can damage your device's memory.

#### iOS
- Use [CCleaner for iOS](https://www.ccleaner.com/ccleaner-ios) to remove temporary and hidden files.

#### Linux and Windows
- Use [BleachBit](https://www.bleachbit.org/) to remove temporary and hidden files. See [their documentation](https://docs.bleachbit.org/).

#### macOS
- Use [CCleaner for Mac](https://www.ccleaner.com/ccleaner-mac) with the ["Custom files and folders" option](https://support.ccleaner.com/s/article/how-do-i-include-custom-files-for-cleaning) enabled.

### Why Clean Traces?

Your devices store more than you realize:
- **Browser data**: Text, images, cookies, account information, browsing history, and form data
- **Temporary files**: Auto-saved versions of documents you're working on
- **Clipboard history**: Everything you've copied
- **App caches**: Shortcuts and data stored by applications

These files are difficult to find and remove safely without specialized tools. Regular cleaning also helps combat malware and improves device performance.

---

## Wipe a Whole Device

> [!important] Before You Begin
> Create an encrypted backup of important files. See [Backup and recover from information loss](https://securityinabox.org/en/files/backup).

### Preparation (All Devices)
1. Close all apps you're not using
2. Disconnect from the internet (turn off WiFi or unplug cable)
3. [Clear your browser's temporary files](https://securityinabox.org/en/internet-connection/safer-browsing/#delete-your-browsing-history)

### Mobile Devices

#### Android
1. Ensure [full-disk encryption is enabled](https://securityinabox.org/en/files/secure-file-storage#consider-encrypting-your-whole-device)
2. [Reset to factory settings](https://support.google.com/android/answer/6088915)

#### iOS
Follow Apple's instructions on [what to do before you sell, give away, or trade in your iPhone or iPad](https://support.apple.com/HT201351).

### Computers

A device cannot thoroughly erase itself—you must start from an external drive.

#### General Process for HDDs
1. Remove the internal drive ([search iFixit](https://www.ifixit.com/Search?query=remove+hard+drive) for your device model)
2. Place the drive in an external USB enclosure
3. Use [ShredOS](https://github.com/PartialVolume/shredos.x86_64) to wipe the drive (download, write to USB stick, boot from USB)
4. Enable full-disk encryption when reinstalling the operating system

> [!note]
> SSDs are harder to fully erase. Follow the platform-specific instructions below.

#### macOS
- Follow the [official documentation](https://support.apple.com/en-us/102664) to erase and reset to factory settings
- **For SSDs**: Secure erase isn't available in Disk Utility. Instead, [enable FileVault encryption](https://support.apple.com/HT204837) before erasing
- **For older Intel Macs**: Use [Disk Utility](https://support.apple.com/en-us/102639) or [Erase Assistant](https://support.apple.com/guide/mac-help/mchl7676b710/mac)

#### Windows
1. Remove the internal drive ([search iFixit](https://www.ifixit.com/Search?query=remove+hard+drive) for your model)
2. Place in an external USB enclosure
3. Connect to a computer with [Eraser](https://securityinabox.org/en/files/tools#eraser) installed
4. Delete all files on the drive
5. Use Eraser to wipe all unallocated space (may need to run overnight)

---

## Before Selling, Giving Away, or Disposing of a Device

### General Checklist
- [ ] If selling a computer, consider keeping the hard drive; if you must include it, [wipe it completely](#wipe-a-whole-device)
- [ ] Remove USB drives, SD cards, SIM cards, and dongles
- [ ] For disposal: physically destroy the drive (hammer nails through it or use a drill)
  - **Do not** burn, pour acid on, or microwave drives
- [ ] Alternatively, keep wiped drives in good condition for re-use

### Platform-Specific Steps

| Platform | Account Removal Guide | Additional Steps |
|----------|----------------------|------------------|
| **Android** | [Secure Google accounts](https://securityinabox.org/en/phones-and-computers/android/#secure-the-google-accounts-connected-with-your-device) | — |
| **iOS** | [Secure connected accounts](https://securityinabox.org/en/phones-and-computers/ios#secure-the-accounts-connected-with-your-device) | [Apple disposal guide](https://support.apple.com/HT201351) |
| **Linux** | [Remove device accounts](https://securityinabox.org/en/phones-and-computers/linux#remove-unneeded-accounts-associated-with-your-device) | — |
| **macOS** | [Secure connected accounts](https://securityinabox.org/en/phones-and-computers/mac#secure-the-accounts-connected-with-your-device) | [Apple disposal guide](https://support.apple.com/HT201065) |
| **Windows** | [Secure connected accounts](https://securityinabox.org/en/phones-and-computers/windows/#secure-the-accounts-connected-with-your-device) | [Microsoft disposal guide](https://support.microsoft.com/account-billing/before-you-sell-or-gift-your-windows-10-device-or-xbox-one-78ee8071-c8ab-40c4-1d89-f708582062e4) |

### Why This Matters

Wiping a drive takes time, and negotiating to keep a hard drive when giving away a computer can be difficult. However, these precautions are essential to ensure you don't accidentally give someone access to your sensitive files.

---

## Quick Reference

| Task | Tools |
|------|-------|
| Clean temporary files (Android) | CCleaner, Extirpater |
| Clean temporary files (iOS) | CCleaner |
| Clean temporary files (Windows/Linux) | BleachBit |
| Clean temporary files (macOS) | CCleaner |
| Wipe HDD | ShredOS, Eraser |
| Protect SSD data | Full-disk encryption |