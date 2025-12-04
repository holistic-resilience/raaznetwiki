```yaml
---
title: "Protect Your Android Device"
tags: [android, mobile-security, privacy, google, app-permissions, device-hardening]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Android Security", "Mobile Privacy", "Device Hardening", "App Management"]
summary: "Comprehensive guide to securing Android devices through OS updates, app management, privacy settings, and advanced security configurations."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic smartphone literacy", "Access to Android device settings"]
estimated_read_time: "25 minutes"
---
```

# Protect Your Android Device

Security starts with setting up your device to protect your information. Follow the steps in this guide to make your Android device more secure. Android devices differ by manufacturer, so you may need to look in a few places to find the settings you are looking for.

---

## Operating System & App Updates

### Use the Latest Version of Your Device's Operating System

- Update from a trusted location and internet connection (home or office), not public wifi
- Set aside time for updates—they may require multiple downloads and restarts
- After updating, check again for additional updates until none remain
- Always restart your device when prompted after downloading updates
- Check your "Android security update" date—security updates are released monthly

**Check your device's support status:**
- [Wikipedia Android version history](https://en.wikipedia.org/wiki/Android_version_history)
- [Android end of life dates](https://endoflife.date/android)
- [Google Pixel support timeline](https://support.google.com/pixelphone/answer/4457705)
- [Samsung security updates](https://security.samsungmobile.com/workScope.smsb)
- [Fairphone updates](https://endoflife.date/fairphone)
- [Motorola security updates](https://en-us.support.motorola.com/app/software-security-update)
- [Nokia security updates](https://www.hmd.com/en_int/security-updates)

> **Why this matters:** New vulnerabilities are discovered daily. Developers release patches to fix them, making updates essential for protection against malicious attackers.

### Regularly Update All Installed Apps

- [Update the Google Play Store app](https://support.google.com/googleplay/answer/113412#update_google_play_store)
- [Enable automatic app updates](https://support.google.com/googleplay/answer/113412#auto)

---

## App Management

### Use Apps from Trusted Sources

- **Avoid rooting your device**—it increases infection risk
- Install apps primarily from the [Google Play Store](https://play.google.com/store)
- [Enable Google Play Protect](https://support.google.com/accounts/answer/2812853) to verify app sources
- If apps are unavailable in your country, consider [changing your Google Play country](https://support.google.com/googleplay/answer/7431675) using a VPN

**Alternative trusted sources:**
- [F-Droid](https://f-droid.org/) for free and open-source apps
- [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) for anonymous Google Play access

> **Why this matters:** The Google Play Store provides centralized monitoring for security violations. Third-party sources increase risk of malicious software.

### Remove Unused Apps

- [Delete apps you don't use](https://support.google.com/googleplay/answer/13627402)
- [Disable or remove pre-installed bloatware](https://www.howtogeek.com/115533/how-to-disable-or-uninstall-android-bloatware/)

> **Why this matters:** Every app is a potential vulnerability. Unused apps may also transmit your data without your knowledge.

### Avoid Social Media Apps When Possible

Access social media through your browser (like [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)) instead of dedicated apps.

> **Why this matters:** Social media apps collect extensive data including your phone ID, phone number, and wifi connections. Browser access limits this data collection.

### Use Privacy-Friendly Alternatives

| Purpose | Recommended App |
|---------|-----------------|
| Web browsing | [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox) |
| Email | [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) |
| App store | [F-Droid](https://f-droid.org/) or [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) |

### Check App Permissions

Review and restrict access to sensitive permissions:
- Camera and microphone
- Location
- Contacts and call logs
- Files and storage
- Screen recording
- Fingerprint reader and facial recognition
- Physical activity and Health Connect

[Manage app permissions on Android](https://support.google.com/android/answer/9431959)

> **Why this matters:** Apps with unnecessary permissions can leak sensitive information or be exploited by attackers.

---

## Location & Privacy Settings

### Turn Off Location and Clear History

- [Turn off location services](https://support.google.com/android/answer/3467281) when not needed
- [Manage location for individual apps](https://support.google.com/android/answer/6179507)
- Regularly [delete your location history](https://support.google.com/accounts/answer/3118687#delete)
- Clear [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location records can be used to track your movements, prove your presence at locations, or identify your associations with others.

---

## User Account Management

### Create Separate User Accounts

- Set up one account with admin privileges and others with standard privileges
- Use a standard user account for daily work
- [Add users on Android](https://support.google.com/android/answer/2865483)

### Remove Unneeded Users

- [Delete unused user accounts](https://support.google.com/android/answer/2865483#zippy=%2Cdelete-user)
- Check for accounts created without your knowledge

### Secure Connected Google Accounts

- [Review which devices use your account](https://support.google.com/accounts/answer/3067630)
- Complete the [Google security checkup](https://myaccount.google.com/security-checkup)
- Consider [Google's Advanced Protection program](https://landing.google.com/advancedprotection/)
- Screenshot any suspicious activity for documentation

---

## Screen Lock & Display Security

### Set Strong Screen Lock

**Recommended:** Long passphrase (minimum 10 characters)

**Avoid:**
- Short PINs or passwords
- Fingerprint or face unlock (can be compelled)
- Pattern locks (easily guessed from finger tracks)
- Swipe to unlock

**Additional settings:**
- Disable "make password visible"
- Set screen timeout to 1-5 minutes
- [Configure display settings](https://support.google.com/pixelphone/answer/6111557)

> **Why this matters:** If arrested or detained, you can be forced to unlock with biometrics. A passphrase provides stronger legal protection.

### Control Lock Screen Visibility

- [Hide all notifications on lock screen](https://support.google.com/android/answer/9079661#zippy=%2Coption-dont-show-any-notifications)
- Disable "Add users from lock screen"

### Disable Voice Controls

- Turn off Google Assistant in Settings > Google
- [Disable microphone access](https://support.google.com/android/answer/13532937) when not needed

> **Why this matters:** Voice-activated devices can be exploited to capture audio without your knowledge.

### Physical Privacy Measures

- Use a [privacy filter screen](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent shoulder surfing
- Cover cameras with a small adhesive bandage or sliding cover
- [Disable camera access](https://support.google.com/android/answer/13532937) when not in use

---

## Connectivity & Network Security

### Turn Off Unused Connectivity

- Power off devices at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use Airplane mode for quick disconnection
- [Disable "Turn on Wi-Fi automatically" and "Notify for public networks"](https://support.google.com/pixelphone/answer/9655181)
- Turn off hotspot when not in use

> **Why this matters:** Active wireless connections can be exploited by nearby attackers. Your device broadcasts known network names, creating a unique fingerprint.

### Clear Saved Wifi Networks

- Store network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassdx) instead
- Regularly [remove saved networks](https://support.google.com/android/answer/9075847#zippy=%2Cremove-a-saved-network)

### Turn Off Unused Sharing Features

- Disable or remove connected devices in Settings
- [Turn off Quick Share/Nearby Share](https://support.google.com/android/answer/9286773)

---

## Keyboard Privacy

### Secure Your Keyboard

1. Check installed keyboards: Settings > System > Keyboard > On-screen keyboard
2. Remove unused keyboard apps
3. For Gboard, disable:
   - Auto-correction
   - Smart compose
   - Smart replies

**Privacy-friendly alternatives:**
- [HeliBoard](https://github.com/Helium314/HeliBoard)
- [Simple Keyboard](https://github.com/rkkr/simple-keyboard)

> **Why this matters:** Keyboard apps can transmit everything you type back to their developers.

---

## Advanced Security

### Basic Device Forensics

If you suspect unauthorized access:
- [Check devices linked to chat apps](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/smartphones/linkeddevices.md)
- [Review installed applications](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/applications.md)
- [Check if phone is rooted](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/root.md)
- [Check for stalkerware](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/stalkerware.md)
- Use the [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/topics/device-acting-suspiciously/#android-intro)

### Use Android Without a Google Account

- Skip the "Sign in" screen during initial setup, or [remove your Google account](https://support.google.com/android/answer/7664951#remove_account)
- Use [F-Droid](https://f-droid.org/) and [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) for apps
- **Important:** Manually check for app updates regularly

### Alternative Operating Systems

For maximum privacy, consider installing:
- [GrapheneOS](https://grapheneos.org/)
- [CalyxOS](https://calyxos.org/)

> **Warning:** This is advanced—verify device compatibility and follow instructions carefully to avoid bricking your device.

---

## See Also

- [Security in a Box Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Google Security Tips](https://safety.google/security/security-tips/)