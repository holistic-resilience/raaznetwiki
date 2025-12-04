```yaml
---
title: "Protect Your Windows Computer"
tags: [windows-security, privacy, malware-protection, device-hardening, digital-security]
category: "Device Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Windows Security", "Privacy Protection", "Device Hardening", "Malware Prevention"]
summary: "Comprehensive guide to securing Windows computers covering system updates, app permissions, privacy settings, and advanced security measures."
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

## System Updates

### Use the Latest Version of Your Operating System

When updating software, do it from a trusted location and internet connection, like your home or office—not at an internet cafe or coffee shop.

**Steps to update:**
1. [Check which version of Windows is running](https://learn.microsoft.com/en-us/windows/client-management/client-tools/windows-version-search)
2. Verify your version is still supported on the [Microsoft Product Lifecycle page](https://learn.microsoft.com/en-us/lifecycle/products/)
3. [See the most updated versions available](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions)
4. [Update your operating system](https://support.microsoft.com/en-us/windows/update-windows-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a)

> **Tip:** Set aside time for updates—they may require multiple downloads and restarts. Always restart your computer when prompted after updates complete.

**Why this matters:** New vulnerabilities in code are discovered daily. Developers cannot predict where they will be found due to code complexity. Malicious attackers exploit these vulnerabilities to access your devices. Software developers regularly release fixes, making updates essential for security.

### Regularly Update All Installed Apps

[Enable automatic app updates in the Microsoft Store](https://support.microsoft.com/en-us/windows/turn-on-automatic-app-updates-70634d32-4657-dc76-632b-66048978e51b).

---

## Application Management

### Use Programs from Trusted Sources

- [Check what apps are installed on your computer](https://support.microsoft.com/en-us/windows/see-all-your-apps-in-windows-fde6f576-0fc0-0813-6b0d-d3ec1d244c50)
- Search the [Microsoft Store](https://www.microsoft.com/store/apps/) to verify app legitimacy
- [Verify your Microsoft software is licensed](https://www.microsoft.com/en-us/howtotell/Whattolookfor.aspx)

> **Warning:** Windows does not offer as many protections as other platforms. Carefully evaluate whether it is safe to install a given program. Only install apps from the Microsoft Store or official developer websites—avoid "mirror" download sites unless you trust the provider.

### Remove Unused Apps

[Uninstall or remove apps and programs](https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-10-4b55f974-2cc6-2d2b-d092-5905080eaf98) you don't need. If you cannot uninstall an app, try disabling it instead.

**Why this matters:** Removing unused apps limits potential vulnerabilities and prevents apps from transmitting information you may not want to share.

### Use Privacy-Friendly Apps

Consider these alternatives to default Windows software:

| Purpose | Recommended App |
|---------|-----------------|
| Web browsing | [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox) |
| Email | [Thunderbird](https://www.thunderbird.net/) |
| Other needs | [Free and open source alternatives](https://github.com/0PandaDEV/awesome-windows) |

**Why this matters:** Default Windows software like Microsoft Edge and Microsoft Office have documented [privacy](https://www.theverge.com/2023/4/25/23697532/microsoft-edge-browser-url-leak-bing-privacy) and [security issues](https://www.techtarget.com/searchsecurity/news/366549116/Vendors-criticize-Microsoft-for-repeated-security-failings).

---

## Permissions and Privacy

### Check App Permissions

Review permissions in [Windows app permissions settings](https://support.microsoft.com/en-us/windows/app-permissions-aea98a7c-b61a-1930-6ed0-47f0ed2ee15c). Be especially careful with these sensitive permissions:

**High-risk permissions:**
- Camera and microphone
- Location
- Screen recording
- Voice/speech recognition
- Fingerprint reader and facial recognition
- Pictures and videos libraries
- Disk access, files, folders, or system access
- Installation permissions

**Why this matters:** Apps with access to sensitive services can leak information or be exploited by attackers. Disable permissions for apps that don't need them.

### Turn Off Location and Clear History

- Turn off location services when not in use—both system-wide and for individual apps
- [Learn how location services work and how to disable them](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088)
- If using Google Maps, clear your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

**Why this matters:** Location records can be used to track your movements, prove you were in certain places, or associate you with specific people.

### Turn Off Advertising and Privacy Options

Go to **Settings > Privacy & security > General** and disable at least the first three options.

---

## User Account Security

### Create Separate User Accounts

**Recommended approach:**
1. Use a [local account](https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32) instead of a Microsoft account to reduce data sharing
2. Create separate admin and standard accounts
3. Use a standard account for daily work
4. [Learn to install Windows without a Microsoft account](https://gravesoft.dev/clean_install_windows#bypass-windows-11-internet-and-microsoft-account-requirements)

**Why this matters:** Separate accounts protect sensitive information when sharing devices and limit potential damage from compromised accounts.

### Remove Unneeded Accounts

[Remove unused user accounts](https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32) to reduce your attack surface. Check for accounts that may have been added without your knowledge.

### Secure Connected Accounts

- [Secure your Microsoft account](https://support.microsoft.com/en-us/account-billing/how-to-help-keep-your-microsoft-account-secure-628538c2-7006-33bb-5ef4-c917657362b9)
- [Review recent account activity](https://support.microsoft.com/en-us/account-billing/what-is-the-recent-activity-page-23cf5556-4dbe-70da-82c8-bb3a8d8f8016) for suspicious access
- Screenshot any suspicious activity showing unrecognized devices

---

## Screen and Physical Security

### Use a Strong Passphrase

- Use a passphrase longer than 16 characters—not a short password or PIN
- [Change your passphrase in sign-in options](https://support.microsoft.com/windows/windows-10-sign-in-options-and-account-protection-7b34d4cf-794f-f6bd-ddcc-e73cdf1a6fbf)
- **Disable [Windows Hello](https://support.microsoft.com/en-us/windows/configure-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0)** (fingerprint, face, eye, or voice unlock)
- Set Windows to require sign-in when PC wakes: **Settings > Accounts > Sign-in Options > Additional Settings**

**Why this matters:** Biometric authentication can be forced—you can be compelled to unlock with your face or fingerprint. Short passwords and PINs can be guessed by software. A long passphrase is the safest protection.

### Set Screen to Lock Automatically

- [Set screen to lock after 5 minutes of inactivity](https://support.microsoft.com/en-us/windows/how-to-adjust-power-and-sleep-settings-in-windows-26f623b5-4fcc-4194-863d-b824e5ea7679)
- Use **Windows Logo Key + L** to lock manually when stepping away

### Control Lock Screen Visibility

[Disable notifications on lock screen](https://support.microsoft.com/en-us/windows/customize-the-lock-screen-in-windows-81dab9b0-35cf-887c-84a0-6de8ef72bea0) to prevent information leaks from visible messages.

### Disable Voice Controls

- [Disable Voice Access](https://support.microsoft.com/en-us/topic/get-started-with-voice-access-bd2aa2dc-46c2-486c-93ae-3d75f7d053a4#ID0EDDBJ)
- [Disable Copilot](https://www.tomsguide.com/computing/software/how-disable-copilot-in-windows-11)
- [Review speech and voice privacy settings](https://support.microsoft.com/en-us/windows/speech-voice-activation-inking-typing-and-privacy-149e0e60-7c93-dedd-a0d8-5731b71a4fef)

**Why this matters:** Voice-activated features constantly listen, and malicious code could capture what your device hears.

### Physical Privacy Measures

- **Privacy filter:** Use a [screen privacy filter](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent shoulder surfing
- **Camera cover:** Use a sliding webcam cover or small adhesive bandage (bandage center has no adhesive, preventing lens stickiness)

---

## Network and Connectivity

### Turn Off Unused Connectivity

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use [Airplane mode](https://support.microsoft.com/en-au/windows/turn-airplane-mode-on-or-off-f2c2e0a1-706f-ff26-c4b2-4a37f9796df1) to quickly disable all wireless connections
- [Disable Bluetooth](https://support.microsoft.com/windows/turn-bluetooth-on-or-off-9e92fddd-4e12-e32b-9132-5e36bdb2f75a)
- [Disable mobile hotspot](https://support.microsoft.com/en-us/windows/use-your-pc-as-a-mobile-hotspot-c89b0fad-72d5-41e8-f7ea-406ad9036b85)

**Network types:**
- Set trusted networks (home/office) to "private"
- Set public networks (cafes, co-working spaces) to "public"
- [Learn about public vs private networks](https://support.microsoft.com/windows/make-a-wi-fi-network-public-or-private-in-windows-10-0460117d-8d3e-a7ac-f003-7a0da607448d)

**Why this matters:** Wireless connections can be exploited by nearby attackers. Your device broadcasts names of saved networks, creating a unique fingerprint that can identify you.

### Clear Saved WiFi Networks

Save network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of your device. This prevents your device from broadcasting your network history while keeping credentials accessible.

### Turn Off File Sharing

- [Stop sharing files on OneDrive](https://support.microsoft.com/office/stop-sharing-onedrive-or-sharepoint-files-or-folders-or-change-permissions-0a36470f-d7fe-40a0-bd74-0ac6c1e13323)
- [Stop sharing files over local networks](https://support.microsoft.com/windows/file-sharing-over-a-network-in-windows-10-b58704b2-f53a-4b82-7bc1-80f9994725bf)
- [Stop sharing with nearby devices](https://support.microsoft.com/windows/share-things-with-nearby-devices-in-windows-10-0efbfe40-e3e2-581b-13f4-1a0e9936c2d9)

### Turn Off Autoplay

Go to **Settings > Bluetooth & Devices > Autoplay** and disable the Autoplay switch.

**Why this matters:** Autoplay may automatically run malicious code from inserted drives.

---

## Security Software

### Use Windows Security

Windows Security includes Microsoft Defender Antivirus. Use it instead of third-party antivirus software.

- [Get familiar with Windows Security features](https://support.microsoft.com/en-us/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963)
- Enable [SmartScreen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/) for protection against phishing and malware

### Enable the Firewall

[Turn on Microsoft Defender Firewall](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f).

**Why this matters:** Firewalls act as security guards, inspecting and controlling communications to and from your device. Default settings provide adequate protection for most users.

---

## Advanced Security

### Stop Malicious Code from Running

[Install and run Hardentools](https://github.com/securitywithoutborders/hardentools#readme) to prevent malicious code execution.

### Basic Forensics: Detect Unauthorized Access

If you suspect your device may be compromised:

1. Review [programs launching at startup](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/autoruns.md)
2. Check [network connections](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/network.md)
3. Examine [running processes](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/processes.md)
4. Follow the [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/topics/device-acting-suspiciously/#windows-intro)

---

*Last updated: 30 September 2024*