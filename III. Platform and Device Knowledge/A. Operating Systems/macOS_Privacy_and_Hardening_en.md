---
title: "macOS Privacy and Hardening"
tags:
  [
    macos,
    apple,
    privacy,
    security,
    hardening,
    encryption,
    filevault,
    lockdown-mode,
    iran-restrictions,
  ]
category: "Operating Systems"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "macOS Security",
    "Privacy Configuration",
    "System Hardening",
    "Apple Silicon",
    "Iranian Context",
  ]
summary: "Comprehensive guide to securing macOS for Iranian users, addressing local restrictions, Apple ID limitations, and advanced hardening techniques."
source: "Raaznet"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites: ["Administrator access to Mac", "Apple Silicon Mac recommended"]
estimated_read_time: "20 minutes"
last_updated: "2026-02-18"
---

# macOS Privacy and Hardening

macOS is a robust operating system, but its default settings prioritize convenience and cloud integration over strict privacy. For Iranian users, this presents unique challenges: Apple's strict adherence to US sanctions means no official presence in Iran, blocked IP addresses, and significant hurdles in creating secure accounts.

This guide focuses on hardening macOS against surveillance while navigating the specific constraints of the Iranian internet landscape.

> **Warning:** Older Intel-based Macs lack the advanced hardware security features of Apple Silicon (M1/M2/M3 chips). If possible, use an Apple Silicon Mac for high-risk work.

---

## 1. The Iranian Context: Apple ID & Connectivity

Before hardening the system, Iranian users must address the fundamental barriers to using Apple services.

### The Apple ID Challenge

Apple requires Two-Factor Authentication (2FA) for all new Apple IDs, but **does not support Iranian (+98) phone numbers**.

- **Risk:** Using temporary "virtual numbers" (free online services) creates a high risk of permanent account lockout.
- **Solution:** Use a permanent foreign phone number (friend/family abroad) or a paid, reputable VoIP service (like Google Voice) that you can maintain long-term.
- **Region:** Set your Apple ID region to a country that does not require residency proof for free apps (e.g., United States), but be aware you cannot use Iranian payment methods.

### Connectivity & Updates

Apple frequently blocks traffic from Iranian IPs.

- **VPN Requirement:** You will likely need a trusted VPN or circumvention tool to access the App Store, activate macOS, and download Security Updates.
- **Traffic Leaks:** Even with a VPN, macOS may send some traffic outside the tunnel. Use a "Kill Switch" feature in your VPN or a firewall like **LuLu** to prevent leaks.

---

## 2. Initial Setup & User Accounts

### Clean Installation

If you bought your Mac used or from a third-party seller in Iran, **do not trust the pre-installed OS**. Perform a "Erase All Content and Settings" or a fresh install from a bootable USB drive to ensure no spyware is pre-loaded.

### Device Name

Your computer's name is broadcasted on local networks (Wi-Fi). Change it to something generic to avoid identifying yourself.

- **Settings > General > About > Name**: Change to "MacBook" or "Mac".

### User Accounts

Do not use an Administrator account for daily tasks. Malware running on an Admin account can do significantly more damage.

1.  **Settings > Users & Groups > Add Account**.
2.  **Type:** Standard.
3.  Use this **Standard** account for daily work. Log into the **Administrator** account only when necessary for system changes.

---

## 3. System Hardening & Settings

### FileVault (Full Disk Encryption)

This is mandatory. Without FileVault, anyone with physical access to your Mac can read your files.

- **Settings > Privacy & Security > FileVault**: Turn **On**.
- **Recovery Key:** Store your recovery key offline (on paper). Do _not_ store it in iCloud if you cannot use Advanced Data Protection.

### Lockdown Mode (Crucial for Activists)

Introduced in macOS Ventura, Lockdown Mode drastically reduces the attack surface (e.g., blocks JIT in browsers, blocks message attachments). It is the best defense against sophisticated spyware like Pegasus.

- **Settings > Privacy & Security > Lockdown Mode**: Turn **On**.
- _Note:_ Some websites and features may look different or load slower.

### Firewall & Network Security

- **Settings > Network > Firewall**: Turn **On**.
- **Options:** Enable "Block all incoming connections" to prevent remote access services (SSH, Screen Sharing) from being reachable.
- **Wi-Fi MAC Randomization:**
  - **Settings > Network > Wi-Fi > Details > Private Wi-Fi Address**: Set to **Rotating** or **Fixed** to prevent tracking across networks.

### Disable Siri & Spotlight Telemetry

Prevent your search queries and voice data from being sent to Apple.

1.  **Settings > Siri & Spotlight**: Turn **Ask Siri** OFF.
2.  **Spotlight Privacy:** Click "Spotlight Privacy..." and drag your hard drive into the list to prevent local indexing if you want extreme privacy (disables local search).
3.  **Disable "Help Apple Improve Search"**: Uncheck this option to stop sending search metadata to Apple.

### Privacy & Security Settings

- **Location Services:** Turn OFF entirely if possible. If needed, enable only for specific apps (e.g., Maps) and ensure "System Services" location sharing is minimized.
- **Analytics & Improvements:** Turn OFF "Share Mac Analytics" and "Share with App Developers".
- **Apple Advertising:** Turn OFF "Personalized Ads".
- **Microphone/Camera:** Review which apps have access. Revoke access for any app that doesn't strictly need it.

---

## 4. iCloud & Data Privacy

iCloud is convenient but dangerous if Apple holds the encryption keys, as they can be compelled to hand over data.

### Advanced Data Protection (ADP)

If you successfully created an Apple ID with 2FA, **enable Advanced Data Protection**.

- **Settings > [Your Name] > iCloud > Advanced Data Protection**.
- This ensures **End-to-End Encryption (E2EE)** for backups, Photos, Drive, and Notes. Apple cannot decrypt this data.

### If ADP is NOT an option (No 2FA / Iranian Restrictions):

**Do not use iCloud for sensitive data.**

- **Disable iCloud Photos, Drive, and Backup.**
- Sync your data manually via cable to a local encrypted drive.
- Use E2EE alternatives:
  - **Cloud Storage:** Proton Drive, Tresorit, or self-hosted Nextcloud.
  - **Notes:** Standard Notes or Obsidian (with local encryption).
  - **Photos:** Ente Photos (E2EE alternative).

---

## 5. Application Security

### Gatekeeper

Never disable Gatekeeper. It ensures only signed, trusted code runs on your Mac.

- **Settings > Privacy & Security > Security**: Ensure "Allow applications downloaded from" is set to **App Store and known developers**.

### Outbound Firewall (LuLu)

macOS has a built-in inbound firewall, but malware can still "phone home".

- **Recommendation:** Install **LuLu** (free, open-source by Objective-See). It alerts you whenever an app tries to connect to the internet.
- _Usage:_ Block any Adobe/Microsoft/Unknown background processes that don't need internet access.

### Browser Choice

Do not use Safari for sensitive browsing, as its traffic can be correlated with your iCloud account.

- **General Privacy:** **Mullvad Browser** or **Brave** (Hardened).
- **Anonymity:** **Tor Browser** (Essential for circumvention).
- _Reference:_ See `Privacy_Focused_Browsers_and_Applications.md`.

---

## 6. Physical Security & Forensics

### "Before First Unlock" (BFU)

When your Mac is fully powered off (or restarted) and you haven't logged in yet, it is in **BFU** state. The encryption keys are not in memory.

- **Practice:** If you are crossing a checkpoint or expect device seizure, **shut down** your Mac completely. Do not just put it to sleep.

### Secure Boot & Recovery

- **Apple Silicon:** Ensure "Full Security" is enabled in Recovery Mode (Startup Security Utility).
- **USB Accessories:** **Settings > Privacy & Security > Allow accessories to connect**: Set to **Ask for New Accessories** or **Always Ask** (available on laptops with Apple Silicon). This blocks tools like GrayKey from connecting via USB port when locked.[cite]

### Webcam & Mic

- **Hardware:** Apple Silicon Macs physically disconnect the microphone when the lid is closed.
- **Visual Indicator:** Monitor the green/orange dots in the menu bar.
- **Physical Cover:** Use a sticker or sliding cover for the webcam.

---

## 7. Connectivity Hygiene (AirDrop & Bluetooth)

AirDrop broadcasts your device hash to everyone nearby. This can identify you in a crowd.

- **AirDrop:** Set to **Receiving Off**. Only enable it momentarily when needed.
- **Bluetooth:** Turn OFF when not in use.
- **AirPlay Receiver:** Disable in **Settings > General > AirPlay & Handoff**.

---

## Checklist for Iranian Users

1.  [ ] **Apple ID:** Secured with a stable foreign number + 2FA enabled.
2.  [ ] **Encryption:** FileVault enabled with offline recovery key.
3.  [ ] **iCloud:** Advanced Data Protection enabled OR iCloud fully disabled.
4.  [ ] **Lockdown:** Lockdown Mode enabled (for high-risk profiles).
5.  [ ] **Firewall:** System Firewall ON + LuLu installed.
6.  [ ] **VPN:** Trusted VPN with Kill Switch configured.
7.  [ ] **Browser:** Mullvad Browser or Tor Browser installed for sensitive work.
8.  [ ] **Maintenance:** Auto-updates enabled (check weekly via VPN).
