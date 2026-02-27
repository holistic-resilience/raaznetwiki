---
title: "Device Security Fundamentals and Hardware"
tags:
  [
    hardware-security,
    device-integrity,
    encryption,
    firmware,
    supply-chain,
    physical-security,
    iran-security,
  ]
category: "Platform and Device Knowledge"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, High-Risk Users]
topics:
  [
    "Hardware Selection",
    "Physical Security",
    "Device Encryption",
    "Supply Chain Safety",
  ]
summary: "A comprehensive guide to selecting secure hardware, understanding physical security states (BFU/AFU), and protecting devices against physical seizure and supply chain attacks in the Iranian context."
source: "Raaznet Aggregation"
content_type: "Educational Guide"
security_level: "Essential"
language: "English"
prerequisites:
  [
    "Basic understanding of computer components",
    "Awareness of physical security risks",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-18"
---

# Device Security Fundamentals and Hardware

In the hierarchy of digital security, **hardware is the foundation**. If your physical device is compromised—whether by a hardware implant, a supply chain interdiction, or physical seizure by authorities—no amount of software encryption or Tor browsing can fully protect you.

For users in Iran, hardware security presents unique challenges due to international sanctions, reliance on "grey market" imports, and the high risk of physical device confiscation at checkpoints or protests. This guide covers how to select secure hardware, protect it physically, and understand the critical states of device encryption.

---

## 1. The Supply Chain Risk in Iran

Unlike users in other regions who can order directly from manufacturers, Iranian users often rely on third-party importers, bazaars, and informal markets. This increases the risk of **interdiction** (tampering with the device before you receive it).

### Mitigating Supply Chain Risks

- **Verify Packaging:** When purchasing a new phone or laptop (e.g., from markets like Charsoo or Aladdin), ensure the factory seals are intact. Look for signs of re-gluing or tampering.
- **Check Serial Numbers:** Before opening the box, check the serial number (IMEI for phones) on the manufacturer’s website (via VPN if necessary) to ensure the device specs match the box.
- **Wipe Immediately:** Never trust the pre-installed operating system on a laptop or "setup" services offered by sellers. Always perform a factory reset or, preferably, wipe the drive and reinstall the operating system yourself immediately after purchase.
- **Avoid Pre-configured Devices:** Reject devices that have already been "set up" or "activated" by the seller to install apps or VPNs. These may contain rootkits or spyware.

---

## 2. Selecting Secure Hardware

Not all devices are created equal. Some manufacturers implement hardware-based security features that make forensic extraction significantly harder.

### Mobile Devices

- **Google Pixel (Recommended):** Pixel devices (Series 6 and newer) include the **Titan M2** security chip. They allow for **Verified Boot** with custom operating systems (like GrapheneOS), making them the gold standard for high-risk users.
- **iPhone (Apple Silicon):** iPhones have robust hardware security (Secure Enclave). However, the closed ecosystem makes it impossible to inspect the code or move away from Apple's proprietary cloud services.
- **Android Ready SE:** Look for devices compliant with "Android Ready SE" standards, which ensure the device has tamper-resistant storage for encryption keys.

### Computers (Laptops/Desktops)

- **Apple Silicon (M1/M2/M3):** These devices have built-in Secure Enclaves similar to iPhones. They utilize hardware-based microphone disconnects when the lid is closed.
- **Windows "Secured-core" PCs:** These meet specific Microsoft security benchmarks, including protection against DMA (Direct Memory Access) attacks.
- **Old Hardware (ThinkPads/Latitudes):** Older enterprise laptops are popular in Iran. While cheap and repairable, ensure they have **TPM 2.0** chips if you intend to use modern Windows security features or full-disk encryption on Linux.

> **Warning regarding Firmware Updates:**
> Due to sanctions, many manufacturers (like Intel, Lenovo, or Apple) block Iranian IP addresses from downloading firmware/BIOS updates. **Always use a trusted VPN** when checking for and applying these updates. Running outdated firmware leaves hardware vulnerabilities (like Spectre/Meltdown) unpatched.

---

## 3. Device Encryption States: BFU vs. AFU

Understanding the difference between **Before First Unlock (BFU)** and **After First Unlock (AFU)** is critical for anyone facing the risk of arrest or device seizure.

### BFU (Before First Unlock)

This is the state of your device when it is completely powered off or immediately after a reboot, _before_ you have entered your PIN/Password.

- **Security Level:** **High**.
- **Why:** Encryption keys are stored in the hardware security chip and are not loaded into the device's memory (RAM). Forensic tools (like Cellebrite, often used by law enforcement) find it extremely difficult to extract data in this state.

### AFU (After First Unlock)

This is the state after you have unlocked your device once. Even if you lock the screen again, the device is in AFU.

- **Security Level:** **Lower**.
- **Why:** Encryption keys are loaded into memory to allow background apps (notifications, calls) to function. Advanced forensic tools can potentially extract these keys from RAM to bypass the lock screen.

### Practical Advice for Activists

If you are approaching a checkpoint, a protest zone, or border control:

1.  **Power off your device completely.** Do not just turn off the screen.
2.  If you cannot power off, trigger a **force reboot**.
    - _iPhone:_ Hold Power + Volume Down (or click Power 5 times) to enter SOS mode/BFU.
    - _Android:_ Restart the device via the power menu.

---

## 4. Biometrics vs. Passphrases

Biometrics (Fingerprint, Face ID) offer convenience, but they weaken security in high-risk physical scenarios.

### The Risk of Forced Entry

Authorities can physically force your finger onto a sensor or hold your phone up to your face to unlock it. They cannot force you to think of a password inside your mind (though they can use coercion/threats).

### Recommendations

- **Primary Protection:** Use a strong, alphanumeric passphrase (random words + numbers), not a 4 or 6-digit PIN.
- **Disable Biometrics in High Risk:** If you use biometrics for daily convenience, know the "panic button" to disable them instantly (see _BFU_ section above).
- **Class 3 Biometrics:** If you must use biometrics on Android, ensure your device supports "Class 3" (strong) biometrics. Avoid using 2D face unlock (common on cheaper Samsung/Xiaomi phones), which can be spoofed with a photo.

---

## 5. Peripheral and Physical Security

### Camera and Microphone

Malware or RATs (Remote Access Trojans) can activate cameras and microphones without the user's knowledge.

- **Camera:** Use a physical sticker or sliding cover. Ensure it does not damage the screen (especially on MacBooks).
- **Microphone:** Hardware disconnects are rare.
  - _MacBooks/iPads (2020+):_ Physically disconnect the mic when the lid is closed.
  - _DIY:_ You can plug a "dummy" headphone jack (a jack with the mic circuit cut) into the audio port to trick the device into using the external (dead) mic input.

### Privacy Screens

"Shoulder surfing" (people looking at your screen) is a threat in crowded spaces like the Tehran Metro or internet cafes. A privacy screen filter limits the viewing angle so only the person directly in front of the screen can see the content.

### Trusted Platform Module (TPM)

Ensure your computer has a TPM enabled. This chip stores encryption keys (like BitLocker or LUKS headers). If an attacker removes your hard drive to copy it, they cannot decrypt it without the TPM chip and your passphrase.

### Hardware Security Keys (2FA)

Devices like **YubiKey** or **Nitrokey** provide the strongest protection against phishing.

- **How it works:** You must physically plug in the key or tap it (NFC) to log in.
- **Iranian Context:** These are difficult to import and expensive. If you can obtain one, they are highly recommended for securing email and cloud accounts. Avoid buying these second-hand.

---

## 6. Network Hardware: Routers

Your router is the gateway to your home network. ISP-provided modems (from providers like MCI, Irancell, or TCI) are often outdated, possess unpatched vulnerabilities, or may have ISP-accessible backdoors.

### Router Hardening

1.  **Replace the ISP Unit:** If possible, put the ISP modem into "Bridge Mode" and connect it to your own high-quality router.
2.  **Update Firmware:** Check for router updates monthly.
3.  **Open Source Firmware:** For advanced users, replacing stock firmware with **OpenWrt** is recommended. OpenWrt is open-source, receives frequent security updates, and allows for advanced features like running a VPN client directly on the router to bypass censorship for the entire home.

---

## 7. Device Integrity Checks

How do you know if your device has been tampered with?

### Reboot Hygiene

Sophisticated spyware (like Pegasus) often relies on "non-persistent" exploits, meaning they live in the device's memory. **Rebooting your phone daily** clears the memory and can disrupt these infections.

### Verification Tools

- **Auditor (Android):** If you use GrapheneOS, the [Auditor app](https://attestation.app/) uses the hardware security chip to cryptographically verify that the operating system has not been tampered with or downgraded.
- **MVT (Mobile Verification Toolkit):** A forensic tool by Amnesty International to scan for signs of spyware. _Note: This requires technical expertise and is reactive, not preventative._

---

## Summary Checklist

| Component       | Recommendation                                                          |
| :-------------- | :---------------------------------------------------------------------- |
| **Purchase**    | Check seals, verify serials, wipe immediately. Avoid pre-setup devices. |
| **Mobile**      | Google Pixel (w/ GrapheneOS) or iPhone (Lockdown Mode).                 |
| **Laptop**      | Apple Silicon or Windows Secured-core. Wiped and reinstalled OS.        |
| **Encryption**  | Always ON. Power off (BFU state) when traveling through checkpoints.    |
| **Access**      | Strong alphanumeric passphrase. Biometrics disabled in high-risk zones. |
| **Maintenance** | Update firmware/OS immediately (use VPN). Reboot daily.                 |
