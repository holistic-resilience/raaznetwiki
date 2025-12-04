```yaml
---
title: "Protect Your Windows Computer"
tags: [windows-security, privacy, device-hardening, malware-protection, digital-security]
category: "Device Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists, IT Administrators]
topics: ["Windows Security", "Privacy Protection", "Device Hardening", "Malware Prevention"]
summary: "Comprehensive security checklist for hardening Windows computers against malware, surveillance, and unauthorized access."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Windows computer literacy", "Administrator access to your device"]
estimated_read_time: "25 minutes"
---
```

# Protect Your Windows Computer

Microsoft Windows is the world's most used operating system for desktop computers and laptops, but also the most common target for malicious software (malware). Follow this checklist to secure your Windows device.

---

## Operating System and Software Updates

### Use the Latest Version of Your Operating System

When updating software, do it from a trusted location and internet connection, like your home or office—not at an internet cafe or coffee shop. Updating may require downloading software and restarting multiple times, so set aside time when you don't need to work on your device.

**Steps:**
1. [Check which version of Windows is running](https://learn.microsoft.com/en-us/windows/client-management/client-tools/windows-version-search)
2. Verify your version is still supported on the [Microsoft Product Lifecycle page](https://learn.microsoft.com/en-us/lifecycle/products/)
3. [See the most updated versions available](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions)
4. [Update your operating system](https://support.microsoft.com/en-us/windows/update-windows-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a)
5. Always restart when prompted after updates
6. Check again for additional updates until none remain

> **Why this matters:** Vulnerabilities in code are discovered daily. Developers release patches to fix them, so using the latest version and enabling automatic updates is essential protection against exploitation.

### Regularly Update All Installed Apps

[Enable automatic app updates in the Microsoft Store](https://support.microsoft.com/en-us/windows/turn-on-automatic-app-updates-70634d32-4657-dc76-632b-66048978e51b) to ensure all applications stay current.

---

## Application Management

### Use Programs and Apps from Trusted Sources

1. [Check what apps are installed](https://support.microsoft.com/en-us/windows/see-all-your-apps-in-windows-fde6f576-0fc0-0813-6b0d-d3ec1d244c50)
2. Search the [Microsoft Store](https://www.microsoft.com/store/apps/) to verify app legitimacy
3. [Verify Microsoft software is properly licensed](https://www.microsoft.com/en-us/howtotell/Whattolookfor.aspx)

> **Note:** Windows offers fewer protections than other platforms when evaluating software trustworthiness. Only install apps from the Microsoft Store or directly from developer websites. Carefully evaluate any software before installation.

### Remove Unused Apps

[Uninstall apps and programs you don't need](https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-10-4b55f974-2cc6-2d2b-d092-5905080eaf98). If you can't uninstall an app, try disabling it instead.

> **Why this matters:** Unused apps can contain vulnerabilities and may transmit information about you without your knowledge. Reducing installed apps limits your attack surface.

### Use Privacy-Friendly Apps

Replace default Windows applications with privacy-respecting alternatives:

- **Web Browser:** [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)
- **Email Client:** [Thunderbird](https://www.thunderbird.net/)
- **General Software:** [Free and open source alternatives for Windows](https://github.com/0PandaDEV/awesome-windows)

> **Why this matters:** Built-in software like Microsoft Edge and Office have documented [privacy](https://www.theverge.com/2023/4/25/23697532/microsoft-edge-browser-url-leak-bing-privacy) and [security issues](https://www.techtarget.com/searchsecurity/news/366549116/Vendors-criticize-Microsoft-for-repeated-security-failings).

---

## App Permissions

### Review and Restrict App Permissions

Check [app permissions in Windows](https://support.microsoft.com/en-us/windows/app-permissions-aea98a7c-b61a-1930-6ed0-47f0ed2ee15c) and restrict access for apps that don't need these capabilities:

**High-Risk Permissions:**
- Location
- Microphone
- Camera/Webcam
- Contacts and Calendar
- Email and Messaging
- Voice/Speech recognition
- Screen recording
- Fingerprint reader
- Any setting with "disk access," "files," "folders," or "system"
- Any setting with "install" in it
- Facial recognition

**Sensitive System Permissions:**
- Account Info
- Allow elevation
- Modifiable app
- Packaged services
- Package write redirect compatibility shim
- Unvirtualized resources

> **Why this matters:** Apps with access to sensitive services can leak information or be exploited by attackers. Only grant permissions that apps actually need.

---

## Location Privacy

### Turn Off Location and Clear History

1. [Disable location services](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088) when not needed
2. Regularly clear your location history
3. If using Google Maps, clear your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location records can be used to track your movements, prove you were in certain places, or associate you with specific people based on shared locations.

---

## User Account Security

### Create Separate User Accounts

1. [Use a local account](https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32) instead of a Microsoft account to reduce data sharing
2. [Install Windows without a Microsoft account](https://gravesoft.dev/clean_install_windows#bypass-windows-11-internet-and-microsoft-account-requirements) if possible
3. Create separate accounts with one "admin" and others "standard" privileges
4. Use a standard account for daily work

> **Why this matters:** Separate accounts protect sensitive information and administrative privileges from other users and reduce risk if one account is compromised.

### Remove Unneeded Accounts

[Remove unused user accounts](https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32) to reduce your attack surface. Additional accounts are additional "doors" into your device.

### Secure Connected Accounts

1. [Secure Microsoft accounts connected to your device](https://support.microsoft.com/en-us/account-billing/how-to-help-keep-your-microsoft-account-secure-628538c2-7006-33bb-5ef4-c917657362b9)
2. [Check recent account activity](https://support.microsoft.com/en-us/account-billing/what-is-the-recent-activity-page-23cf5556-4dbe-70da-82c8-bb3a8d8f8016) for suspicious logins
3. Take screenshots of any suspicious activity (devices you don't recognize)
4. Review [social media accounts](https://securityinabox.org/en/communication/social-media) connected to your device

---

## Authentication and Screen Lock

### Use a Strong Passphrase

1. Use a [long passphrase](https://securityinabox.org/en/passwords/passwords) (16+ characters), not a short password or PIN
2. [Configure sign-in options](https://support.microsoft.com/windows/windows-10-sign-in-options-and-account-protection-7b34d4cf-794f-f6bd-ddcc-e73cdf1a6fbf)
3. [Disable Windows Hello](https://support.microsoft.com/en-us/windows/configure-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0) (fingerprint, face, eyes, voice unlock)
4. Set Windows to require sign-in when PC wakes from sleep: **Settings > Accounts > Sign-in Options > Additional Settings**

> **Why this matters:** Biometric authentication (fingerprint, face) can be forced upon you if detained. Short passwords and PINs can be guessed. A long passphrase is the safest option.

### Configure Screen Lock

1. [Set screen to lock after 5 minutes of inactivity](https://support.microsoft.com/en-us/windows/how-to-adjust-power-and-sleep-settings-in-windows-26f623b5-4fcc-4194-863d-b824e5ea7679)
2. Use **Windows Key + L** to manually lock when stepping away
3. [Disable notifications on lock screen](https://support.microsoft.com/en-us/windows/customize-the-lock-screen-in-windows-81dab9b0-35cf-887c-84a0-6de8ef72bea0)

---

## Voice Controls and Privacy

### Disable Voice Controls

1. [Disable Voice Access](https://support.microsoft.com/en-us/topic/get-started-with-voice-access-bd2aa2dc-46c2-486c-93ae-3d75f7d053a4#ID0EDDBJ)
2. [Disable Copilot](https://www.tomsguide.com/computing/software/how-disable-copilot-in-windows-11)
3. Review [speech and voice activation privacy settings](https://support.microsoft.com/en-us/windows/speech-voice-activation-inking-typing-and-privacy-149e0e60-7c93-dedd-a0d8-5731b71a4fef)

> **Why this matters:** Voice-activated features constantly listen while enabled and could be exploited to capture audio. Only use if you have a disability requiring voice controls.

---

## Physical Security

### Use a Privacy Screen Filter

Install a [privacy filter](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent "shoulder surfing"—someone viewing your screen over your shoulder or via security cameras.

### Use a Camera Cover

1. Identify all cameras on your device (built-in and external)
2. Apply a small adhesive bandage (the non-sticky center won't damage the lens)
3. Or purchase a sliding webcam cover for your device model
4. Consider disabling cameras entirely if you have admin access

> **Why this matters:** Malware can activate your camera without your knowledge to spy on you and your surroundings.

---

## Network and Connectivity

### Turn Off Unused Connectivity

1. Power off devices completely at night
2. Keep wifi, Bluetooth, and network sharing disabled when not in use
3. [Enable Airplane mode](https://support.microsoft.com/en-au/windows/turn-airplane-mode-on-or-off-f2c2e0a1-706f-ff26-c4b2-4a37f9796df1) to quickly disable all wireless connections
4. Set trusted networks (home/office) to "private" and public networks to "public" in [network settings](https://support.microsoft.com/windows/make-a-wi-fi-network-public-or-private-in-windows-10-0460117d-8d3e-a7ac-f003-7a0da607448d)
5. [Turn off Bluetooth](https://support.microsoft.com/windows/turn-bluetooth-on-or-off-9e92fddd-4e12-e32b-9132-5e36bdb2f75a)
6. [Disable mobile hotspot](https://support.microsoft.com/en-us/windows/use-your-pc-as-a-mobile-hotspot-c89b0fad-72d5-41e8-f7ea-406ad9036b85)

> **Why this matters:** Wireless connections can be exploited by nearby attackers. When enabled, your device broadcasts the names of previously connected networks, creating a unique fingerprint that can identify and target your device.

### Clear Saved WiFi Networks

Save network credentials in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of your device. If you must save networks on your device, periodically clear networks you no longer use.

---

## Sharing and Autoplay

### Turn Off Unused Sharing

1. [Stop sharing files on OneDrive](https://support.microsoft.com/office/stop-sharing-onedrive-or-sharepoint-files-or-folders-or-change-permissions-0a36470f-d7fe-40a0-bd74-0ac6c1e13323)
2. [Stop sharing over local networks](https://support.microsoft.com/windows/file-sharing-over-a-network-in-windows-10-b58704b2-f53a-4b82-7bc1-80f9994725bf)
3. [Stop nearby device sharing](https://support.microsoft.com/windows/share-things-with-nearby-devices-in-windows-10-0efbfe40-e3e2-581b-13f4-1a0e9936c2d9)

### Disable Autoplay

Go to **Settings > Bluetooth & Devices > Autoplay** and turn off the Autoplay switch.

> **Why this matters:** Autoplay can automatically execute malicious code from inserted drives.

---

## Privacy Settings

### Turn Off Advertising and Tracking

Go to **Settings > Privacy & security > General** and disable at least the first three options to limit data sharing and tracking.

---

## Security Software

### Enable Windows Security

Windows Security includes Microsoft Defender Antivirus. Use the built-in protection rather than third-party antivirus software.

1. [Familiarize yourself with Windows Security features](https://support.microsoft.com/en-us/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963)
2. Enable [SmartScreen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/) for phishing and malware protection

### Enable the Firewall

[Turn on Microsoft Defender Firewall](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f) to block unwanted connections. Default settings provide adequate protection for most users.

---

## Advanced Security

### Stop Malicious Code from Running

[Install and run Hardentools](https://github.com/securitywithoutborders/hardentools#readme) to prevent common malware execution techniques.

### Basic Forensics: Detect Unauthorized Access

If you suspect compromise, review:
- [Programs launching at startup](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/autoruns.md)
- [Network connections](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/network.md)
- [Running processes](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/processes.md)

For suspected compromise, follow the [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/topics/device-acting-susp