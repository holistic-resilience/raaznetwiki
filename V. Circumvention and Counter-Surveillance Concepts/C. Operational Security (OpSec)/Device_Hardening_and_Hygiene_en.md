---
title: "Device Hardening and Hygiene"
tags:
  [
    device-hardening,
    physical-security,
    mobile-security,
    encryption,
    opsec,
    iran-security,
    malware-protection,
  ]
category: "Operational Security (OpSec)"
difficulty: "Intermediate"
audience:
  [General Public, Activists, Journalists, High-Risk Individuals in Iran]
topics:
  ["Device Security", "Physical Protection", "OS Hardening", "Anti-Forensics"]
summary: "Comprehensive guide to securing mobile and desktop devices against physical seizure, forensic extraction, and digital surveillance within the Iranian threat landscape."
source: "Raaznet Wiki Aggregation"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of operating systems", "Access to device settings"]
estimated_read_time: "20 minutes"
---

# Device Hardening and Hygiene

Digital security is not just about preventing hackers from stealing your data; it is about protecting your identity, your network, and your physical freedom from a state apparatus with extensive surveillance capabilities.

**Device Hardening** refers to the process of reducing the "attack surface" of your devices—closing doors that adversaries might use to enter. **Device Hygiene** refers to the daily habits that keep those protections effective.

This guide consolidates best practices for securing Android, iOS, Windows, macOS, and Linux devices against threats common in Iran, such as device confiscation at protests, checkpoints, and state-sponsored malware.

---

## 1. Physical Security: The First Line of Defense

In Iran, the physical seizure of devices (by the IRGC, Basij, or regular police) is a primary threat. If an adversary has physical access to your unlocked device, digital protections often fail.

### Full Disk Encryption (FDE)

Encryption scrambles your data so it is unreadable without a password.

- **Modern Smartphones:** Android and iOS are encrypted by default _if_ you set a passcode.
- **Desktops/Laptops:** You must enable this manually.
  - **Windows:** Enable **BitLocker** (Pro versions) or "Device Encryption".
  - **macOS:** Enable **FileVault** immediately (`System Settings > Privacy & Security`).
  - **Linux:** Enable **LUKS** encryption during installation.

### The "Golden State": Powered Off (BFU)

Devices have two states of encryption:

1.  **AFU (After First Unlock):** The device is on, and you have entered the password once. Encryption keys are in memory. Forensic tools (like Cellebrite, used by Iranian authorities) can often extract data in this state.
2.  **BFU (Before First Unlock):** The device is completely powered off. Encryption keys are cleared from memory. This is the most secure state.

> **[CRITICAL ADVICE]** If you are approaching a checkpoint, being detained, or entering a protest zone, **power off your phone completely**. Do not just lock the screen.

### Disable Biometrics (FaceID / Fingerprint)

In Iran, you can be physically forced to press your finger to a scanner or hold your phone to your face. You cannot be easily forced to reveal a complex code inside your mind.

- **Recommendation:** Disable FaceID and Fingerprint unlock in settings. Rely **only** on a strong alphanumeric passphrase.
- **Emergency Lockdown:**
  - **iOS:** Hold the Power button + Volume Up/Down until the slider appears. This disables biometrics immediately.
  - **Android:** Enable the "Lockdown" button in settings. Holding the power button and tapping "Lockdown" disables biometrics.

---

## 2. Authentication and Access Control

### Strong Passphrases

Simple PINs (4-6 digits) can be brute-forced by forensic hardware in minutes or days.

- **Switch to Alphanumeric:** Use a passphrase of 12+ characters (mixing letters and numbers) rather than a numeric PIN.
- **Diceware Method:** String together 5-6 random words (e.g., `correct-horse-battery-staple`). This is easier to type and remember but mathematically hard to crack.

### Two-Factor Authentication (2FA)

**Warning regarding SMS:** In Iran, telecommunication providers (MCI, Irancell, Rightel) are heavily monitored or state-owned. SMS 2FA codes can be intercepted.

- **Do NOT use SMS 2FA.**
- **Use Authenticator Apps:** Use apps like **Aegis** (Android/F-Droid), **Raivo** (iOS), or **Ente Auth**. These generate codes offline on your device.
- **Hardware Keys:** For high-risk users, use a hardware key (like YubiKey) for accounts. This prevents phishing completely.

---

## 3. Mobile Device Hardening

Mobile phones are the primary tracking devices used by the state.

### Android Hardening

- **Debloating:** Remove or disable apps you do not use. Each app is a potential security hole.
- **App Sources:**
  - **Avoid Iranian App Stores:** Stores like _Cafe Bazaar_ or _Myket_ may host modified apps with backdoors or comply with state data requests.
  - **Use F-Droid:** For open-source, tracker-free software.
  - **Google Play:** Safer than local stores, but requires a VPN.
  - **Aurora Store:** An anonymous frontend for Google Play.
- **Google Advanced Protection:** If you have a supported Pixel device (Android 16+), enable **Advanced Protection Mode**. It restricts USB data transfer and blocks unverified apps.
- **Alternative OS:** For maximum security, install **GrapheneOS** on a Google Pixel. It de-Googles the phone and hardens the kernel against exploits.

### iOS Hardening

- **Lockdown Mode:** Enable this in `Settings > Privacy & Security > Lockdown Mode`. It strictly limits web technologies and message attachments, blocking many "zero-click" exploits (like Pegasus) used by state actors.
- **iCloud Security:** Enable **Advanced Data Protection** for iCloud. This end-to-end encrypts your backups so even Apple cannot provide your data to authorities if subpoenaed.

### SIM Card Security

- **SIM PIN:** Set a PIN on your SIM card (`Settings > Cellular > SIM PIN`). This prevents a thief (or agent) from putting your SIM in another phone to receive your calls/SMS.
- **SIM Swapping:** Be aware that the Iranian state can clone SIMs without social engineering. Rely on apps (Signal) for communication, not regular calls/SMS.

---

## 4. Desktop Hardening

### Windows

- **Updates:** Windows is the most targeted OS. Enable automatic updates.
- **Windows Security:** Ensure Microsoft Defender is active. Enable "Ransomware Protection" (Controlled Folder Access).
- **Debloat:** Uninstall pre-loaded vendor software.
- **Firewall:** Use a tool like **Simplewall** to whitelist only the apps you want connecting to the internet.

### macOS

- **Firewall:** Enable the built-in firewall. Consider installing **LuLu** (open-source) to block unauthorized outgoing connections.
- **Gatekeeper:** Ensure "Allow apps downloaded from" is set to "App Store and identified developers."

### Linux (Ubuntu/Debian/Tails)

- **Tails OS:** For extremely high-risk activities (whistleblowing), run **Tails OS** from a USB stick. It routes everything through Tor and wipes memory on shutdown.
- **Qubes OS:** For advanced users, Qubes uses "compartmentalization," running every app in a separate virtual machine. If you open a malicious PDF, it cannot infect your password manager.

---

## 5. Network Hygiene & Anti-Surveillance

The Iranian Internet (SHOMA/Filternet) uses Deep Packet Inspection (DPI).

### Connection Discipline

- **Disable Unused Radios:** Turn off Wi-Fi, Bluetooth, and NFC when not explicitly using them. They broadcast unique identifiers (MAC addresses) that can track your movement in crowded areas (like protests).
- **Randomized MAC Addresses:** Ensure your phone is set to use a "Private Wi-Fi Address" or "Randomized MAC" when connecting to networks.
- **Vigilance with Public Wi-Fi:** Avoid public Wi-Fi in Iran. If necessary, _never_ connect without a trusted VPN (like Mullvad, IVPN, or a private Shadowsocks/V2Ray server).

### Location Tracking

- **GPS:** Revoke location permissions for all apps except maps.
- **Metadata:** Use tools like **Scrambled Exif** (Android) or **Metapho** (iOS) to remove GPS coordinates from photos before sharing them online.

---

## 6. Malware and App Hygiene

State-sponsored malware (often disguised as VPNs, "Gold" Telegram clients, or dating apps) is common.

### Warning Signs

- Apps asking for "Accessibility Services" permissions.
- Apps asking to "Install Unknown Apps."
- Battery draining faster than usual.

### Response

- **Factory Reset:** If you suspect infection, antivirus is rarely enough. A factory reset is the safest option.
- **Audit Permissions:** Regularly check which apps have access to Microphone, Camera, and Location. Revoke any that are not essential.

---

## 7. Travel and Border Crossings

Crossing borders (e.g., IKA Airport) carries a high risk of digital search.

- **Sanitize Devices:** Uninstall sensitive apps (Signal, Twitter, Instagram) before crossing. Log out of accounts.
- **The "Burner" Strategy:** If possible, travel with a "clean" secondary device that contains no sensitive data.
- **Cloud Travel:** Back up data to a secure, encrypted cloud (e.g., Proton Drive), wipe the device, cross the border, and restore data via VPN once safe.

---

## Summary Checklist for Iranian Users

1.  [ ] **Encryption:** Full disk encryption enabled on all devices.
2.  [ ] **State:** Power off devices (BFU state) when transporting them through checkpoints.
3.  [ ] **Lock:** Alphanumeric passphrase set (12+ chars). Biometrics disabled.
4.  [ ] **SIM:** SIM PIN enabled.
5.  [ ] **Apps:** Unused apps deleted. Permissions audited. Iranian app stores avoided.
6.  [ ] **Network:** VPN used 24/7 (Kill switch enabled). Bluetooth/Wi-Fi off when traveling.
7.  [ ] **Updates:** OS and apps updated to latest versions immediately.
8.  [ ] **2FA:** Authenticator app used; SMS 2FA disabled where possible.

> **Note:** Security is a process, not a product. No device is unhackable. These steps significantly raise the cost and effort required for the regime to compromise your digital life.
