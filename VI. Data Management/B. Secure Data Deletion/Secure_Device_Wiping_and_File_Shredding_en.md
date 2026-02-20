---
title: "Secure Device Wiping and File Shredding"
tags:
  [
    data-destruction,
    secure-deletion,
    digital-security,
    device-disposal,
    privacy,
    anti-forensics,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public, High-Risk Users]
topics:
  [
    "Secure Data Deletion",
    "Device Sanitization",
    "Anti-Forensics",
    "Crypto-Shredding",
  ]
summary: "A comprehensive guide on securely erasing files and wiping entire devices to prevent data recovery by state authorities or forensic tools. Covers modern methods for SSDs, HDDs, and mobile devices."
source: "Raaznet Aggregation"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of file systems",
    "Full Disk Encryption enabled (recommended)",
  ]
estimated_read_time: "12 minutes"
---

# Secure Device Wiping and File Shredding

Simply "deleting" a file or "formatting" a drive is not enough. When you delete a file, the operating system merely removes the reference to that data, marking the space as "available." The actual data remains physically on the drive until it is overwritten.

For Iranian activists, journalists, and citizens facing the threat of device seizure by security forces (e.g., at protests, border crossings, or home raids), this distinction is critical. Forensic tools used by authorities (such as Cellebrite or Oxygen Forensics) can easily recover "deleted" files.

This guide details how to **permanently** destroy data—whether it's a single incriminating file or an entire device—ensuring it cannot be recovered.

---

## The Core Concept: Overwriting vs. Crypto-Shredding

### 1. Traditional Overwriting (HDD)

On older mechanical Hard Disk Drives (HDDs), secure deletion works by writing random data (0s and 1s) over the original file multiple times. Tools like **ShredOS** or **BleachBit** use this method.

### 2. Modern Crypto-Shredding (SSD & Mobile)

Modern devices (Android, iPhones, and laptops with SSDs) use flash storage. Traditional overwriting is ineffective and harmful here due to "Wear Leveling" (a mechanism that distributes data across the drive to extend its life).

- **The Solution:** If your device is encrypted, you don't need to overwrite every sector. You only need to destroy the **decryption key**. Without the key, the data is indistinguishable from random noise and is mathematically impossible to recover.
- **Rule of Thumb:** **Always use Full Disk Encryption.** When you factory reset an encrypted device, you are effectively "shredding" the key.

---

## Section 1: Shredding Individual Files

_Use this when you need to delete specific sensitive documents but keep the operating system intact._

> [!WARNING] limitation for SSDs and USB Drives
> "Shredding" individual files on **Solid State Drives (SSDs)**, **USB sticks**, and **SD cards** is unreliable. due to wear leveling, the original data might remain in a different physical sector.
>
> **Best Practice:** For highly sensitive data on SSDs/USBs, use an encrypted container (like **VeraCrypt**) and delete the entire container volume when necessary.

### Desktop Tools (Windows, Linux, macOS)

#### **BleachBit** (Recommended)

An open-source, privacy-focused alternative to CCleaner.

- **Function:** Cleans temporary files, cache, and securely "shreds" individual files.
- **Platform:** Windows, Linux. (macOS via command line/Homebrew).
- **Usage:**
  1.  Install [BleachBit](https://www.bleachbit.org/).
  2.  Go to **File** > **Shred Files**.
  3.  Select the files you want to destroy.
  4.  BleachBit will overwrite the file content before deleting it.
- **Wiping Free Space:** Use the "Wipe Free Space" option to overwrite remnants of files you previously deleted normally.

#### **Eraser** (Windows Only)

A dedicated secure deletion tool for Windows.

- **Features:** Integrates into the right-click context menu. Allows you to schedule automated wiping of specific folders.
- **Download:** [Eraser (Heidi)](https://eraser.heidi.ie/)

#### **Command Line (Linux/macOS)**

- **Linux:** Use the `shred` command.
  ```bash
  shred -u -z -n 3 filename.txt
  # -u: remove file after overwriting
  # -z: add a final overwrite with zeros to hide shredding
  # -n 3: overwrite 3 times
  ```
- **macOS:** The `rm -P` command exists but is **not recommended** for SSDs (which all modern Macs use). Rely on **FileVault** encryption and emptying the Trash, or use a specific tool like BleachBit if available.

---

## Section 2: Wiping Entire Devices (Sanitization)

_Use this before selling a device, crossing a border, or if you believe seizure is imminent._

### Mobile Devices (Android & iOS)

On mobile devices, "shredding" individual files is nearly impossible due to app sandboxing. You must wipe the whole device.

#### **Android**

1.  **Encrypt First:** Ensure your phone is encrypted. (Settings > Security > Encryption). Most modern Androids (Android 10+) are encrypted by default.
2.  **Factory Reset:** Go to **Settings > System > Reset Options > Erase all data (factory reset)**.
3.  **The Result:** This destroys the encryption key. The data remains on the chip but is encrypted and inaccessible.
4.  **Extra Paranoia (Optional):** After resetting, you can set up the phone as "new" (without logging in), fill the storage with large video files until full, and factory reset again. This overwrites the old encrypted data with new data.
5.  **Free Space Wiping (Rooted/Older Devices):** Use apps like **Extirpater** (available on F-Droid) to wipe free space, but use with caution as it wears out memory.

#### **iOS (iPhone/iPad)**

1.  **iOS encryption:** iPhones are hardware-encrypted by default.
2.  **Reset:** Go to **Settings > General > Transfer or Reset iPhone > Erase All Content and Settings**.
3.  **Result:** The encryption key is discarded. Data is unrecoverable.

### Computers (Laptops & Desktops)

#### **1. Modern Method (SSDs / NVMe)**

If you have an SSD (most laptops post-2015), do **not** use tools like DBAN/ShredOS immediately.

- **BIOS/UEFI Secure Erase:** Many modern motherboards (Lenovo, ASUS, HP) have a built-in "Secure Erase" tool in the BIOS setup. This sends a voltage spike to the SSD controller to reset all blocks. This is the fastest and most secure method.
- **Parted Magic / Manufacturer Tools:** If your BIOS lacks this, use the SSD manufacturer’s software (e.g., Samsung Magician) or a bootable tool like **Parted Magic** (paid) which can issue the ATA Secure Erase command.

#### **2. Traditional Method (HDDs)**

For older spinning hard drives, you must overwrite the platters.

- **Tool:** **ShredOS** (The modern successor to DBAN).
- **Download:** [ShredOS on GitHub](https://github.com/PartialVolume/shredos.x86_64).
- **Usage:**
  1.  Download the `.img` file and flash it to a USB drive (using Etcher or Rufus).
  2.  Boot your computer from the USB drive.
  3.  The tool `nwipe` will launch automatically. Select the drives you want to wipe.
  4.  Choose the **DoD Short** (3 passes) or **PRNG Stream** method.
  5.  Let it run (this can take hours).

---

## Section 3: Physical Destruction

_The only 100% guarantee. Recommended for high-risk users holding highly sensitive data who cannot risk any forensic recovery._

If you are in a situation where you cannot safely wipe the device (e.g., a raid is in progress) or the hardware is damaged, physical destruction is necessary.

1.  **HDDs (Spinning Drives):**
    - Drill 4-5 holes through the metal casing, ensuring you penetrate the platters inside.
    - Disassemble the drive and sand/scratch the mirror-like surface of the platters.

2.  **SSDs and Mobile Phones:**
    - The data is stored on small black **NAND flash chips** on the circuit board.
    - Simply snapping a phone in half might miss the chip.
    - **Method:** Drill directly through the memory chips or shatter them with a hammer. On a phone, the motherboard is usually located in the top half of the device.

---

## Iran-Specific Context & Risks

### The "Bazaar" Risk

It is common in Iran to sell used phones or laptops at local bazaars (e.g., Alaeddin or Charsou in Tehran). **Do not sell devices that have stored sensitive political or activist materials.** Even with a factory reset, there is a non-zero risk of recovery if encryption was not implemented correctly.

- **Advice:** If you have used a device for sensitive work, destroy it physically rather than selling it. The small financial gain is not worth the security risk.

### Checkpoints and "Hiding"

At checkpoints (Ist-e Bazrasi), agents often look for gallery photos and Telegram/Instagram apps. Wiping specific files might leave "thumbnails" or cache traces that specialized software can find.

- **Strategy:** If you are heading into a high-risk zone (protest area), use a "burner" phone with no sensitive data. If you must carry your main device, consider **Hidden Volumes** (using Veracrypt) or rely on **Signal's Disappearing Messages** for communication, rather than manually deleting files later.

### "Clean" Rooms

Iranian cyber police (FATA) and intelligence services (Sepah) have access to commercially available forensic tools. They can recover data from:

- Unencrypted devices.
- "Deleted" files in the Recycle Bin/Trash.
- Temp folders and browser caches.

**Regularly using BleachBit** to clean your system traces is a good "digital hygiene" habit that reduces your footprint even if you aren't wiping the whole device.

---

## Quick Reference Summary

| Storage Type              | Recommended Method     | Tools                                         |
| :------------------------ | :--------------------- | :-------------------------------------------- |
| **Individual File (HDD)** | Overwrite              | BleachBit, Eraser, `shred`                    |
| **Individual File (SSD)** | **Avoid** (Unreliable) | Use Encrypted Containers (VeraCrypt)          |
| **Whole Android**         | Crypto-Shred           | Encrypt + Factory Reset                       |
| **Whole iPhone**          | Crypto-Shred           | "Erase All Content and Settings"              |
| **Whole SSD (Laptop)**    | ATA Secure Erase       | BIOS Tool, Parted Magic                       |
| **Whole HDD (Legacy)**    | Overwrite (Nuke)       | ShredOS (nwipe)                               |
| **Free Space**            | Wipe Clean             | BleachBit, Extirpater (Android - use caution) |
