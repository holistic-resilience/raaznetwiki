---
title: "Windows Privacy and Hardening"
tags:
  [
    windows-security,
    privacy,
    device-hardening,
    telemetry,
    group-policy,
    bitlocker,
    digital-security,
  ]
category: "Operating Systems"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics:
  [
    "Windows Configuration",
    "System Hardening",
    "Data Privacy",
    "Surveillance Protection",
  ]
summary: "Comprehensive guide to securing Microsoft Windows, minimizing telemetry, and hardening the system against surveillance and forensic analysis."
source: "Raaznet Aggregated"
content_type: "Educational Guide"
security_level: "Intermediate"
language: "English"
prerequisites:
  ["Administrator access to Windows", "Basic familiarity with System Settings"]
estimated_read_time: "25 minutes"
---

# Windows Privacy and Hardening

Microsoft Windows is the most widely used desktop operating system globally, making it a frequent target for malware and surveillance. Out of the box, Windows is configured to collect significant amounts of usage data (telemetry) and relies heavily on cloud integration. For Iranian users facing state surveillance and censorship, hardening Windows is essential to reduce the "attack surface" and minimize the digital footprint.

This guide covers selecting the right edition, performing a clean installation, configuring privacy settings, and using advanced tools to secure the operating system.

---

## 1. Choosing the Right Version and Edition

### Windows 10 vs. Windows 11

Microsoft has announced that **Windows 10 will reach its End of Life (EOL) on October 14, 2025**. After this date, it will no longer receive security updates, leaving it vulnerable to new attacks.

- **Recommendation:** If your hardware supports it, upgrade to **Windows 11**.
- **Hardware Limitations:** If your device cannot run Windows 11 securely, consider switching to a Linux distribution (e.g., Ubuntu, Fedora) before the 2025 deadline.

### Windows Editions: Home vs. Pro vs. Enterprise

Privacy and security features vary significantly by edition.

- **Windows Home:** **Not recommended.** It lacks BitLocker (full disk encryption), Group Policy Editor, and Sandbox features. It also makes it difficult to set up a local (offline) account.
- **Windows Pro:** The recommended retail version. Includes BitLocker and Group Policy Editor (`gpedit.msc`), which is crucial for advanced privacy configuration.
- **Windows Enterprise / Education:** The gold standard for privacy, allowing the highest level of telemetry restriction. While not typically available for retail purchase, Education licenses may be available to university students.

> [!warning] Avoid "Modified" or "Cracked" Windows
> In Iran, pirated or pre-activated versions of Windows are common. **Avoid these.**
>
> - **Modified ISOs (e.g., "Tiny10", "Windows AME"):** Often lack critical security updates and may have broken defense mechanisms.
> - **Activators/Cracks:** Often contain backdoors or malware.
>
> **Best Practice:** Download the official ISO directly from Microsoft. If you cannot afford a license, running an unactivated official version is safer than running a cracked version.

---

## 2. Installation and Setup

### Clean Installation

Always perform a "clean install" (wiping the drive) rather than using the pre-installed Windows that comes with a new laptop. Manufacturer installations often contain "bloatware" and third-party trials that degrade privacy.

### Use a Local Account

By default, Windows 11 forces you to sign in with a Microsoft Account, linking your activity to your online identity.

- **Privacy Goal:** Use a **Local Account** (offline account) to keep data on the device.
- **How to bypass (Windows 11):** During setup, if forced to connect to Wi-Fi, you can often bypass this by disconnecting the internet or using specific command-line bypasses (e.g., `OOBE\BYPASSNRO` in the command prompt accessed via `Shift + F10`).

---

## 3. Basic System Hardening

### Operating System Updates

New vulnerabilities are discovered daily.

- **Action:** Go to **Settings > Windows Update** and ensure you are up to date.
- **Iranian Context:** While bandwidth may be expensive or throttled, security updates are non-negotiable. Do not disable Windows Update.

### Full Disk Encryption (BitLocker)

Encryption protects your data if your laptop is seized or stolen.

- **Requirement:** Windows Pro, Enterprise, or Education.
- **Action:** Enable **BitLocker** on your OS drive.
- **Best Practice:** Set a pre-boot PIN. This requires you to enter a code _before_ Windows even loads, protecting against cold-boot attacks.
  - _Group Policy:_ **Computer Configuration > Administrative Templates > Windows Components > BitLocker Drive Encryption > Operating System Drives > Require additional authentication at startup.**

### Windows Security (Defender)

Third-party antivirus software often increases your attack surface (adding more code that runs with high privileges) and may collect its own data.

- **Recommendation:** Stick to the built-in **Microsoft Defender**.
- **Configuration:**
  - Enable **Real-time protection**.
  - Enable **Tamper Protection**.
  - Enable **Potentially Unwanted App (PUA) blocking** in **App & browser control**.

### Firewall Configuration

The Windows Firewall is robust but needs to be enabled.

- **Action:** Ensure **Microsoft Defender Firewall** is On for Public, Private, and Domain networks.
- **Advanced Tool:** Consider using **[Simplewall](https://github.com/henrypp/simplewall)**. It is an open-source tool that helps you configure the Windows Filtering Platform (WFP) to block all traffic by default and only allow specific apps. This is excellent for preventing unauthorized apps from "phoning home."

---

## 4. Privacy Configuration (Settings App)

Navigate through the **Settings > Privacy & security** menu and configure the following:

### General Privacy

- **Advertising ID:** **Off**. Prevents apps from tracking you for ads.
- **Suggested content:** **Off**.
- **Activity History:** Uncheck "Store my activity history on this device" and "Send my activity history to Microsoft."

### App Permissions

Review permissions carefully. Block access for any app that does not strictly need it.

- **Location:** **Off** globally if possible. If needed, grant only to specific apps (e.g., Maps) "While using".
- **Camera & Microphone:** Deny access to all apps except those you trust (e.g., Signal, Firefox).
- **Voice Activation:** **Off**. Prevents the device from constantly listening for keywords.

### Diagnostics & Feedback

- **Diagnostic Data:** Set to **Required data only** (formerly "Basic").
- **Feedback frequency:** Set to **Never**.

---

## 5. Advanced Hardening (Group Policy)

For users with **Windows Pro/Enterprise**, the **Group Policy Editor** (`gpedit.msc`) allows for deeper configuration not available in the Settings app.

**Navigate to:** `Computer Configuration > Administrative Templates`

| Path                                     | Setting                          | Action                             | Reason                                                                                         |
| :--------------------------------------- | :------------------------------- | :--------------------------------- | :--------------------------------------------------------------------------------------------- |
| **Windows Components > AutoPlay**        | Turn off AutoPlay                | **Enabled**                        | Prevents malware from running automatically when USBs are inserted.                            |
| **Windows Components > Data Collection** | Allow Diagnostic Data            | **Disabled** (or Limit to minimum) | Reduces telemetry sent to Microsoft.                                                           |
| **Windows Components > Search**          | Allow Cortana                    | **Disabled**                       | Removes voice assistant data collection.                                                       |
| **Windows Components > Search**          | Don't search the web...          | **Enabled**                        | Prevents local searches (e.g., searching for a file) from being sent to Bing.                  |
| **Windows Components > OneDrive**        | Prevent the usage of OneDrive... | **Enabled**                        | Stops files from syncing to the cloud automatically.                                           |
| **Windows Components > Windows AI**      | Turn off Recall                  | **Enabled**                        | **CRITICAL:** Disables the AI feature that takes screenshots of your screen every few seconds. |

> [!danger] Disable "Recall" Immediately
> The **Recall** feature (part of Copilot+) periodically takes screenshots of everything you see on your screen to create a searchable timeline. This creates a massive forensic database of your activity (encrypted, but accessible if you are logged in).
>
> - **Action:** Ensure Recall is disabled in Settings or via Group Policy.

---

## 6. Network and Connectivity

### DNS Security

ISPs in Iran heavily monitor DNS requests to block sites and track users.

- **Action:** Enable **DNS over HTTPS (DoH)** in Windows.
- **Navigate to:** **Settings > Network & internet > Wi-Fi (or Ethernet) > Hardware properties > DNS server assignment > Edit**.
- **Setting:** Choose "Encrypted only (DNS over HTTPS)" and use a trusted provider (e.g., Cloudflare, Quad9, or a private server).

### Wi-Fi Privacy

- **Random Hardware Addresses:** Enable this in **Settings > Network & internet > Wi-Fi**. It randomizes your MAC address to prevent tracking across different Wi-Fi networks.
- **Public Networks:** Set your home network to **Private** and all other networks (cafes, public Wi-Fi) to **Public**.

---

## 7. Additional Tools and Practices

### Hardentools

For high-risk users, **[Hardentools](https://github.com/securitywithoutborders/hardentools)** (by Security Without Borders) automatically disables risky Windows features (like PowerShell, cmd.exe, and Office macros) that are rarely used by average people but frequently exploited by malware.

- _Note:_ This may break some advanced workflows. Use with caution.

### Privacy-Focused Browsers

Do not use Microsoft Edge or Google Chrome.

- **Recommendation:** Use **Firefox** or **Brave**. Configure them to delete cookies on exit and use strict tracking protection.

### Physical Security

- **Camera Cover:** Physically cover your webcam. Software switches can be bypassed by malware.
- **BIOS/UEFI Password:** Set a password in your BIOS to prevent an attacker from booting from a USB drive to bypass your OS security.
- **Secure Boot:** Ensure Secure Boot is enabled in BIOS to prevent "Evil Maid" attacks (tampering with the bootloader).

### Forensic Awareness

If you suspect your device has been compromised:

- Check **Task Manager > Startup apps** for unknown programs.
- Use tools like Sysinternals **Autoruns** to see exactly what runs when the system starts.
- Check **Settings > Accounts > Access work or school** to ensure no rogue organization management profiles have been added.
