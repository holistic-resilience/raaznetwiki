```yaml
---
title: "Protect Your Mac Computer"
tags: [macos, device-security, privacy, apple, digital-hygiene]
category: "Device Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["macOS Security", "Privacy Protection", "Device Hardening"]
summary: "Comprehensive guide to securing your Mac computer, covering OS updates, privacy settings, app permissions, and advanced protection measures."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Access to a Mac computer"]
estimated_read_time: "20 minutes"
---
```

# Protect Your Mac Computer

If you use a Mac, you may have heard the myth that Mac computers are more secure. This is not necessarily true. Security depends on a combination of how we use our devices and their software, which can have vulnerabilities discovered at any time. Follow the steps in this guide to make your device more secure, and get in the habit of checking these settings regularly to ensure nothing has changed.

---

## Table of Contents

1. [Keep Your Operating System Updated](#keep-your-operating-system-updated)
2. [Enable Lockdown Mode](#enable-lockdown-mode)
3. [Manage Apps Securely](#manage-apps-securely)
4. [Control App Permissions](#control-app-permissions)
5. [Manage Location Services](#manage-location-services)
6. [Secure User Accounts](#secure-user-accounts)
7. [Protect Your Login Credentials](#protect-your-login-credentials)
8. [Configure Lock Screen Security](#configure-lock-screen-security)
9. [Disable Voice Controls](#disable-voice-controls)
10. [Physical Security Measures](#physical-security-measures)
11. [Manage Network Connectivity](#manage-network-connectivity)
12. [Configure Firewall and Sharing](#configure-firewall-and-sharing)
13. [Additional Protection Recommendations](#additional-protection-recommendations)
14. [Basic Forensics: Detecting Unauthorized Access](#basic-forensics-detecting-unauthorized-access)

---

## Keep Your Operating System Updated

New vulnerabilities in device and app code are discovered daily. Developers cannot predict where these weaknesses will appear, but malicious attackers can exploit them to access your devices. Software developers regularly release updates that fix these vulnerabilities, making it essential to install updates and use the latest operating system version.

### Best Practices

- **Update from trusted locations** like your home or office—not internet cafes or coffee shops
- **Set aside dedicated time** for updates, as they may require multiple downloads and restarts
- **Check for additional updates** after each installation until no new updates appear
- **Always restart your device** when prompted to fully install updates
- **Consider upgrading your hardware** if the latest macOS won't run on your computer

### Resources

- [What to do if your computer doesn't have enough storage space](https://support.apple.com/en-us/102624)
- [Updating old versions of macOS](https://support.apple.com/en-us/102662)

---

## Enable Lockdown Mode

We strongly recommend [turning Lockdown Mode on](https://support.apple.com/en-us/105120) for your Mac. Most users won't notice significant differences in daily use, but you'll gain substantially better protection against sophisticated attacks.

### Why This Matters

Lockdown Mode limits infection strategies used by sophisticated spyware like [Pegasus](https://securityinabox.org/en/blog/pegasus-project-questions-and-answers/). These protective features should be standard for everyone and represent essential security measures.

---

## Manage Apps Securely

### Install Apps from Trusted Sources

- [Install apps from the App Store](https://support.apple.com/en-us/111105)
- [Only allow apps downloaded from the App Store](https://support.apple.com/en-us/102445#changesettings) unless you have specific expertise
- **Advanced users**: Learn to [temporarily override security settings for trusted apps](https://support.apple.com/en-us/102445#openanyway)

The [Apple App Store](https://www.apple.com/app-store/) provides centralized app distribution, making it easier for Apple to monitor apps for security violations. If you install apps from developer websites, take additional precautions and consider keeping sensitive information off that device.

### Remove Unnecessary Apps

[Uninstall apps](https://support.apple.com/en-us/102610) you don't need or use. Removing unused apps limits potential vulnerabilities and prevents apps from transmitting information about you (like your location) without your knowledge.

> **Note**: Uninstalling default apps like Safari or iTunes is difficult and risky.

### Use Privacy-Friendly Alternatives

Mac computers come with built-in software that has a history of [privacy](https://www.theregister.com/2024/04/30/apple_safari_europe_tracking/) and [security issues](https://www.techradar.com/news/apple-itunes-has-a-serious-security-flaw-you-really-should-know-about). Consider these alternatives:

- **Web browsing**: [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)
- **Email**: [Thunderbird](https://www.thunderbird.net/)
- **General use**: [Open source Mac applications](https://github.com/serhii-londar/open-source-mac-os-apps)

---

## Control App Permissions

Apps that access sensitive information—like your location, microphone, camera, or device settings—can leak that data or be exploited by attackers.

### Review These Permissions Carefully

The following permissions are frequently abused by malicious applications:
- Location
- Photos
- Contacts
- Calendar
- Microphone
- Camera
- Usage logs

Review the [macOS guide on controlling personal information shared with apps](https://support.apple.com/en-gw/guide/mac-help/mh35847/mac#mchlpa3b92d9) and disable permissions for apps that don't need them.

---

## Manage Location Services

Many devices track your location using GPS, cell towers, and wifi networks. This record could help someone find you or prove you were in certain places at specific times.

### Recommended Actions

- Turn off location services overall or when not in use
- [Manage location services for your device and individual apps](https://support.apple.com/en-gw/guide/maps/mpsa33caac1f/mac)
- Regularly clear your location history
- If using Google Maps, manage your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

---

## Secure User Accounts

### Create Separate User Accounts

Create multiple user accounts on your device—one with administrative privileges and others with standard (non-admin) privileges. Consider using a standard account for daily work to protect administrative permissions and sensitive files.

- [How to add a user on Mac](https://support.apple.com/en-gw/guide/mac-help/mchl3e281fc9/mac)

### Remove Unnecessary Accounts

[Delete unneeded accounts](https://support.apple.com/en-gw/guide/mac-help/mchlp1557/mac) to reduce your attack surface. Also check for accounts that may have been created without your knowledge.

### Secure Your Apple ID

- Review [Apple's checklist to protect your Apple ID](https://support.apple.com/en-us/102614)
- Set a [strong password](https://securityinabox.org/en/passwords/passwords/)
- [Enable 2-factor authentication](https://support.apple.com/en-us/102660)
- Never share your Apple ID account
- [Check your device list](https://support.apple.com/en-us/102649) for connected devices
- Take screenshots of suspicious activity (devices you don't recognize or no longer control)
- Follow [Apple's steps if your Apple ID has been compromised](https://support.apple.com/en-us/102560)
- Consider enabling [Advanced Data Protection for iCloud](https://support.apple.com/en-us/108756) for end-to-end encryption

---

## Protect Your Login Credentials

### Use a Strong Passphrase

- Use a [long passphrase](https://securityinabox.org/en/passwords/passwords) (16+ characters), not a short password
- [Disable automatic login](https://support.apple.com/en-us/102316)
- [Change your login password](https://support.apple.com/en-vn/guide/mac-help/mchlp1550/14.0/mac/14.0)
- Ensure [FileVault is enabled](https://support.apple.com/en-vn/guide/mac-help/mh11785/mac)

### Avoid Biometric Login

**Do not use TouchID** to log in unless you have a disability that makes typing impossible. Biometric login can be used against you by force—someone could compel you to unlock your device with your fingerprint, or create a fake version of your finger from dusted prints.

---

## Configure Lock Screen Security

### Screen Lock Settings

- [Set your screen to lock](https://support.apple.com/en-in/guide/mac-help/mh11784/mac) after 5 minutes of inactivity
- [Require a password](https://support.apple.com/en-in/guide/mac-help/mchlp2270/mac) when waking from sleep or screensaver

### Control Lock Screen Notifications

A strong screen lock provides limited protection if notifications display sensitive information. Configure your device to hide notification content:

- [Pause notifications when sleeping or locked](https://support.apple.com/en-in/guide/mac-help/mh40583/mac)
- [Use Focus modes like Do Not Disturb](https://support.apple.com/en-in/guide/mac-help/mchl999b7c1a/14.0/mac/14.0)
- [Turn off notifications for specific apps](https://support.apple.com/en-in/guide/mac-help/mchl39cc046c/mac)

---

## Disable Voice Controls

If you set up voice control, someone could install code on your device to capture what it's listening to.

### Recommended Actions

- [Turn off Siri](https://support.apple.com/en-in/guide/mac-help/mchl6b029310/mac#mchl9bf44710)
- [Delete Siri and dictation history](https://support.apple.com/en-gb/guide/mac-help/mchlf55961c0/mac)

> **Accessibility Note**: If you have a disability requiring voice control, follow the [Security Planner instructions for safer setup](https://securityplanner.consumerreports.org/tool/secure-your-smart-speaker).

---

## Physical Security Measures

### Privacy Screen Filter

"Shoulder surfing"—someone looking at your screen—is a real threat. Human rights defenders have had information stolen this way. A [privacy filter](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) makes this attack less likely to succeed.

### Camera Cover

Malicious software can turn on your camera to spy on you without your knowledge.

**Options**:
- Apply a small adhesive bandage (the middle part won't leave residue on your lens)
- Purchase a sliding webcam cover designed for your model
- [Disable camera access for specific apps](https://support.apple.com/en-ie/guide/mac-help/mchlf6d108da/mac)
- Disable the camera entirely: **Settings > Screen Time > Content & Privacy > App Restrictions > Turn off Allow Camera** ([detailed instructions](https://support.apple.com/en-ie/guide/mac-help/mchl3a19a9e7/14.0/mac/14.0))

---

## Manage Network Connectivity

### Turn Off Unused Connections

All wireless communication (wifi, NFC, Bluetooth) can be exploited by nearby attackers. When these connections are enabled, your device broadcasts the names of networks and devices it has previously connected to, creating a unique fingerprint that can identify your device.

**Best Practices**:
- Power off your computer completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- [Understand wifi menu icons](https://support.apple.com/guide/mac-help/wi-fi-menu-icons-on-mac-mchlcedc581e/mac)
- [Disable Internet Sharing](https://support.apple.com/guide/mac-help/share-internet-connection-mac-network-users-mchlp1540/14.0/mac/14.0)

### Clear Saved Wifi Networks

- Save network credentials in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of your device
- Regularly remove saved networks you no longer use

---

## Configure Firewall and Sharing

### Enable the Firewall

Firewalls act as security guards, deciding which communications can enter and leave your device.

- [Block connections with a firewall](https://support.apple.com/guide/mac-help/block-connections-to-your-mac-with-a-firewall-mh34041/mac)
- Enable [stealth mode](https://support.apple.com/en-jo/guide/mac-help/mh17133/mac) for enhanced security

### Disable Unused Sharing Features

Sharing features are useful but can be exploited if left enabled unnecessarily.

- [Turn off AirDrop](https://support.apple.com/guide/mac-help/airdrop-mac-send-files-devices-mh35868/mac#mchl3aad4788)
- [Review and disable unused sharing services](https://support.apple.com/guide/mac-help/change-sharing-settings-mchl26e04309/mac)

---

## Additional Protection Recommendations

### Spotlight Privacy Settings

In **System Preferences > Spotlight > Search Results**, uncheck:
- Contacts
- Events & Reminders
- Mail & Messages
- Siri Suggestions

In **System Preferences > Spotlight > Privacy**, add sensitive folders you don't want communicated to Apple.

### Further Reading

- [Comprehensive macOS Security and Privacy Guide](https://github.com/drduh/macOS-Security-and-Privacy-Guide)

---

## Basic Forensics: Detecting Unauthorized Access

If you suspect your device has been compromised, these steps can help identify tampering.

### Review System Activity

- [Running processes](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/mac/processes.md)
- [Startup programs](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/mac/autoruns.md)
- [Network connections](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/mac/network.md)
- [Kernel extensions](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/mac/kernel.md)

### Recommended Security Tools

Install [Objective-See security tools](https://objective-see.com/products.html):
- **OverSight**: Monitors microphone and webcam
- **BlockBlock**: Alerts on persistent installations
- **KnockKnock**: Reveals persistently installed software

### Verify Secure Boot

- **Mac with T2 Security Chip**: Check [Startup Security Utility](https://support.apple.com/HT208198) and ensure Secure Boot is set to Full Security
- **Mac with Apple Silicon**: [Verify Security Policy is set to Full Security](https://support.apple.com/guide/mac-help/change-security-settings-startup-disk-a-mac-mchl768f7291/mac)

### If You Suspect Compromise

Follow the Digital First Aid Kit troubleshooter: [My device is acting suspiciously](https://digitalfirstaid.org/topics/device-acting-suspiciously/#mac-intro)

---

*Last updated: 25 June 2024*