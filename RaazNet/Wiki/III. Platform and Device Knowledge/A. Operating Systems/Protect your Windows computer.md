```yaml
---
title: "Protect Your Windows Computer"
tags: [windows-security, privacy, malware-protection, device-hardening, digital-security]
category: "Device Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Remote Workers]
topics: ["Windows Security", "Privacy Protection", "Malware Prevention", "Device Hardening"]
summary: "Comprehensive security checklist for Windows computers covering OS updates, app permissions, account protection, connectivity settings, and advanced threat prevention."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Windows navigation", "Administrator access to device"]
estimated_read_time: "25 minutes"
---
```

# Protect Your Windows Computer

Microsoft Windows is the world's most used operating system for desktop computers and laptops, but also the most common target for malicious software (malware). Follow this checklist to secure your Windows device.

---

## Operating System and Software Updates

### Use the Latest Version of Windows

When updating software, do it from a trusted location and internet connection, like your home or office—not at an internet café or coffee shop. Updating may require multiple downloads and restarts, so set aside time when you don't need to work on your device.

**Steps to update:**
1. [Check which version of Windows is running](https://learn.microsoft.com/en-us/windows/client-management/client-tools/windows-version-search)
2. Verify your version is still supported on the [Microsoft Product Lifecycle page](https://learn.microsoft.com/en-us/lifecycle/products/)
3. [Update your operating system](https://support.microsoft.com/en-us/windows/update-windows-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a)
4. Always restart when prompted after updates
5. Check again for additional updates until none remain

> [!info] Why this matters
> New vulnerabilities are discovered daily. Developers release patches to fix these security holes, which is why using the latest version and installing updates promptly is critical for protection.

### Regularly Update All Installed Apps

[Enable automatic app updates in the Microsoft Store](https://support.microsoft.com/en-us/windows/turn-on-automatic-app-updates-70634d32-4657-dc76-632b-66048978e51b) to ensure all applications stay current with security patches.

---

## Application Management

### Use Programs from Trusted Sources

- [Check what apps are installed](https://support.microsoft.com/en-us/windows/see-all-your-apps-in-windows-fde6f576-0fc0-0813-6b0d-d3ec1d244c50)
- Search the [Microsoft Store](https://www.microsoft.com/store/apps/) to verify app legitimacy
- [Verify Microsoft software licensing](https://www.microsoft.com/en-us/howtotell/Whattolookfor.aspx)

> [!warning] Important
> Windows offers fewer protections than other platforms for evaluating software trustworthiness. Only install apps from the Microsoft Store or official developer websites. Avoid "mirror" download sites unless you trust the provider.

### Remove Unused Apps

[Uninstall apps and programs](https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-10-4b55f974-2cc6-2d2b-d092-5905080eaf98) you don't need. If you can't uninstall an app, try disabling it instead.

Removing unused apps reduces your attack surface and prevents unnecessary data transmission about your activities and location.

### Use Privacy-Friendly Alternatives

Replace default Windows applications with more privacy-respecting alternatives:

| Purpose | Recommended App |
|---------|-----------------|
| Web browsing | [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox) |
| Email | [Thunderbird](https://www.thunderbird.net/) |
| Other needs | [Open source alternatives](https://github.com/0PandaDEV/awesome-windows) |

After installing privacy-friendly apps, [uninstall or disable](https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-10-4b55f974-2cc6-2d2b-d092-5905080eaf98) the default apps you won't use.

---

## App Permissions

Review [app permissions](https://support.microsoft.com/en-us/windows/app-permissions-aea98a7c-b61a-1930-6ed0-47f0ed2ee15c) and restrict access for apps that don't need specific capabilities.

**High-risk permissions to audit:**
- Camera and microphone
- Location
- Screen recording
- Voice/speech recognition
- Pictures, videos, and media libraries
- Fingerprint reader and facial recognition
- Near field communications (NFC)
- Any setting with "disk access," "files," "folders," or "system"
- Any setting with "install"

**Additional permissions to review:**
- Account Info
- Allow elevation
- Modifiable app
- Packaged services
- Package write redirect compatibility shim
- Unvirtualized resources

> [!tip] Why this matters
> Apps with access to sensitive services can leak information or be exploited by attackers. Disable permissions for any service an app doesn't genuinely need.

---

## Location Privacy

### Turn Off Location Services

Disable location services when not needed, both device-wide and for individual apps.

- [Manage Windows location services](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088)
- Regularly clear location history
- If using Google Maps, manage your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

> [!warning] Privacy risk
> Location records can be used to track your movements, prove you were at certain places, or identify people you've been near. This data can be exploited if your device is compromised or seized.

---

## User Account Management

### Create Separate User Accounts

**Recommended approach:**
- Use a [local account](https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32) instead of a Microsoft account to reduce data sharing
- Create separate accounts: one with admin privileges, others with standard privileges
- Use a standard account for daily work
- [Install Windows without a Microsoft account](https://gravesoft.dev/clean_install_windows#bypass-windows-11-internet-and-microsoft-account-requirements) if possible

> [!note]
> Using a local account means you won't be able to sync data across devices, but it significantly reduces what Microsoft knows about your activities.

### Remove Unneeded Accounts

[Remove user accounts](https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32) you don't use. Each unused account is an additional potential entry point for attackers.

### Secure Connected Accounts

- [Secure your Microsoft account](https://support.microsoft.com/en-us/account-billing/how-to-help-keep-your-microsoft-account-secure-628538c2-7006-33bb-5ef4-c917657362b9)
- [Review recent account activity](https://support.microsoft.com/en-us/account-billing/what-is-the-recent-activity-page-23cf5556-4dbe-70da-82c8-bb3a8d8f8016)
- Check [social media accounts](https://securityinabox.org/en/communication/social-media) connected to your device
- Screenshot any suspicious activity (unrecognized devices, locations, or access times)

---

## Authentication and Screen Security

### Use a Strong Passphrase

- Use a [long passphrase](https://securityinabox.org/en/passwords/passwords) (16+ characters), not a short password or PIN
- [Configure sign-in options](https://support.microsoft.com/windows/windows-10-sign-in-options-and-account-protection-7b34d4cf-794f-f6bd-ddcc-e73cdf1a6fbf)
- [Disable Windows Hello](https://support.microsoft.com/en-us/windows/configure-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0) biometric authentication
- Set Windows to require sign-in when PC wakes from sleep: **Settings > Accounts > Sign-in Options > Additional Settings**

> [!danger] Avoid biometric authentication
> Fingerprint, face, and voice unlock can be forced from you during detention or arrest. Short passwords and PINs can be guessed with software. Fingerprints can be faked from surfaces you've touched. A long passphrase is the safest option.

### Configure Screen Lock

- [Set screen to lock after 5 minutes of inactivity](https://support.microsoft.com/en-us/windows/how-to-adjust-power-and-sleep-settings-in-windows-26f623b5-4fcc-4194-863d-b824e5ea7679)
- Use **Windows Key + L** to manually lock when stepping away
- [Disable lock screen notifications](https://support.microsoft.com/en-us/windows/customize-the-lock-screen-in-windows-81dab9b0-35cf-887c-84a0-6de8ef72bea0) to prevent information leakage

---

## Voice and Visual Privacy

### Disable Voice Controls

- [Disable Voice Access](https://support.microsoft.com/en-us/topic/get-started-with-voice-access-bd2aa2dc-46c2-486c-93ae-3d75f7d053a4#ID0EDDBJ)
- [Disable Copilot](https://www.tomsguide.com/computing/software/how-disable-copilot-in-windows-11)
- Review [speech and voice privacy settings](https://support.microsoft.com/en-us/windows/speech-voice-activation-inking-typing-and-privacy-149e0e60-7c93-dedd-a0d8-5731b71a4fef)

> [!warning]
> Voice-activated features keep your device constantly listening, creating opportunities for eavesdropping through malicious code. Only enable if you have a disability requiring voice controls.

### Physical Privacy Measures

**Privacy filter:**
Use a [privacy filter screen](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent "shoulder surfing"—someone viewing your screen from nearby or via security cameras.

**Camera cover:**
- Locate all cameras on your device (built-in and external)
- Use a small adhesive bandage (the non-sticky center won't damage the lens) or purchase a sliding webcam cover
- Consider disabling cameras entirely if you have administrator access

---

## Network and Connectivity

### Turn Off Unused Connectivity

- Power off devices completely at night
- Keep WiFi, Bluetooth, and network sharing off when not in use
- Use [Airplane mode](https://support.microsoft.com/en-au/windows/turn-airplane-mode-on-or-off-f2c2e0a1-706f-ff26-c4b2-4a37f9796df1) as a quick way to disable all wireless connections
- [Turn off Bluetooth](https://support.microsoft.com/windows/turn-bluetooth-on-or-off-9e92fddd-4e12-e32b-9132-5e36bdb2f75a)
- [Disable mobile hotspot](https://support.microsoft.com/en-us/windows/use-your-pc-as-a-mobile-hotspot-c89b0fad-72d5-41e8-f7ea-406ad9036b85)
- Turn off WiFi: **Settings > Network & internet > WiFi**

**Network trust levels:**
- Set trusted networks (home, office) to "private"
- Set public networks (cafés, co-working spaces) to "public"
- Learn more about [public and private network settings](https://support.microsoft.com/windows/make-a-wi-fi-network-public-or-private-in-windows-10-0460117d-8d3e-a7ac-f003-7a0da607448d)

> [!info] Why this matters
> Active wireless connections broadcast information about your device and previously connected networks. This creates a unique fingerprint attackers can use to identify and target your device.

### Clear Saved WiFi Networks

- Store network names and passwords in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of on your device
- Regularly clear saved networks to prevent your device from broadcasting connection history

### Turn Off Sharing Features

Disable sharing when not actively using it:
- [Stop sharing files on OneDrive](https://support.microsoft.com/office/stop-sharing-onedrive-or-sharepoint-files-or-folders-or-change-permissions-0a36470f-d7fe-40a0-bd74-0ac6c1e13323)
- [Stop sharing files over local networks](https://support.microsoft.com/windows/file-sharing-over-a-network-in-windows-10-b58704b2-f53a-4b82-7bc1-80f9994725bf)
- [Stop sharing with nearby devices](https://support.microsoft.com/windows/share-things-with-nearby-devices-in-windows-10-0efbfe40-e3e2-581b-13f4-1a0e9936c2d9)

---

## System Security Settings

### Turn Off AutoPlay

**Settings > Bluetooth & Devices > AutoPlay** → Turn off

AutoPlay can automatically execute malicious code from inserted drives.

### Disable Advertising and Telemetry

**Settings > Privacy & security > General** → Turn off at least the first 3 options

Limiting data sharing reduces your exposure and the information available about you.

### Enable Windows Security

Use the built-in Microsoft Defender rather than third-party antivirus:
- [Review Windows Security features](https://support.microsoft.com/en-us/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963)
- Enable [SmartScreen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/) for protection against phishing, malware, and malicious downloads

### Enable Firewall

[Turn on Microsoft Defender Firewall](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f)

A firewall acts as a security guard, inspecting and controlling incoming and outgoing network traffic. The default configuration provides adequate protection for most users.

---

## Advanced Security

### Stop Malicious Code from Running

[Install and run Hardentools](https://github.com/securitywithoutborders/hardentools#readme) to disable Windows features commonly exploited by malware.

### Basic Forensics

If you suspect unauthorized access to your device:

1. Review [programs launching at startup](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/autoruns.md)
2. Check [network connections](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/network.md)
3. Examine [running processes](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/windows/processes.md)
4. Follow the [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/topics/device-acting-suspiciously/#windows-intro) for suspicious device behavior

---