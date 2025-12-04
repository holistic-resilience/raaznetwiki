```yaml
---
title: "Protect Your Android Device"
tags: [android, mobile-security, privacy, device-hardening, google, app-permissions]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Android Security", "Device Hardening", "Privacy Protection", "App Management"]
summary: "Comprehensive guide to securing Android devices through OS updates, app management, privacy settings, and advanced hardening techniques."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Android device familiarity", "Access to device settings"]
estimated_read_time: "25 minutes"
---
```

# Protect Your Android Device

Security starts with setting up your device to protect your information. Follow the steps in this guide to make your Android device more secure. Android devices differ by manufacturer, so you may need to look in a few places to find the settings you are looking for.

---

## Operating System and App Updates

### Use the Latest Version of Your Device's Operating System

- Update from a trusted location and internet connection (home or office), not public wifi
- Set aside time for updates—they may require multiple downloads and restarts
- After updating, check again for additional updates until none remain
- Always restart your device when prompted after downloading updates

**Check your Android version:**
- [Find the most updated version available](https://developer.android.com/about/versions)
- [Compare and update your operating system](https://support.google.com/android/answer/7680439)
- [Check your "Android security update" date](https://support.google.com/android/answer/7680439?hl=en)—security updates release monthly

**Device-specific update information:**
- **Google Pixel**: [Security update timeline](https://support.google.com/pixelphone/answer/4457705)
- **Samsung**: [Security updates page](https://security.samsungmobile.com/workScope.smsb)
- **Fairphone**: [End of life dates](https://endoflife.date/fairphone)
- **Motorola**: [Security updates support](https://en-us.support.motorola.com/app/software-security-update)
- **Nokia**: [Security and Maintenance Release Summary](https://www.hmd.com/en_int/security-updates)
- **Other manufacturers**: [Android Authority update policies overview](https://www.androidauthority.com/phone-update-policies-1658633/)

If your Android version is unmaintained, consider buying a new device. Check [Android version history](https://en.wikipedia.org/wiki/Android_version_history) or [end of life dates](https://endoflife.date/android).

> **Why this matters:** New vulnerabilities are discovered daily. Developers release patches to fix them, making updates essential for security.

### Regularly Update All Installed Apps

- [Update the Google Play Store app](https://support.google.com/googleplay/answer/113412#update_google_play_store)
- [Enable automatic app updates](https://support.google.com/googleplay/answer/113412#auto)

---

## App Management

### Use Apps from Trusted Sources

- **Do not root your device**—it increases vulnerability to malware
- Install apps from the [Google Play Store](https://play.google.com/store)
- [Enable Google Play Protect](https://support.google.com/accounts/answer/2812853) and disable installation from unknown sources
- If apps aren't available in your country, [change your Google Play country](https://support.google.com/googleplay/answer/7431675) (may require a [VPN](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service))

**Trusted alternative sources:**
- [F-Droid](https://f-droid.org/) (free and open-source apps)
- [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) (anonymous access to Play Store apps)

> **Why this matters:** The Google Play Store provides centralized monitoring for security violations. Third-party sources carry higher risks.

### Remove Unnecessary Apps

- [Delete apps you don't use](https://support.google.com/googleplay/answer/13627402)
- [Disable or remove manufacturer bloatware](https://www.howtogeek.com/115533/how-to-disable-or-uninstall-android-bloatware/)

> **Why this matters:** Unused apps can contain vulnerabilities and may transmit your data without your knowledge.

### Avoid Social Media Apps When Possible

Access social media through your secure browser (like [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)) instead of dedicated apps. Apps collect more data including your phone ID, phone number, and connected wifi networks.

### Use Privacy-Friendly Alternatives

| Purpose | Recommended App |
|---------|-----------------|
| Web browsing | [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox) |
| Email | [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) |
| App store | [F-Droid](https://f-droid.org/en/) or [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) |

### Check App Permissions

Review and restrict permissions for sensitive access:
- Microphone and camera
- Location
- Contacts and call logs
- Files and storage
- Screen recording
- Fingerprint and facial recognition
- NFC and Bluetooth
- Physical activity and Health Connect
- Ability to install other apps

[Manage app permissions on Android](https://support.google.com/android/answer/9431959?hl=en)

> **Why this matters:** Apps with unnecessary permissions can leak sensitive information or be exploited by attackers.

---

## Location and Privacy Settings

### Turn Off Location and Clear History

- [Disable location services](https://support.google.com/android/answer/3467281) when not needed
- [Manage location for individual apps](https://support.google.com/android/answer/6179507)
- Regularly clear location history:
  - [Google Maps Timeline](https://support.google.com/accounts/answer/3118687?#delete)
  - [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location records can prove where you've been and who you've been near.

### Control Lock Screen Visibility

- [Hide all notifications on lock screen](https://support.google.com/android/answer/9079661#zippy=%2Coption-dont-show-any-notifications)
- Disable "Add users from lock screen" in [guest and user settings](https://support.google.com/pixelphone/answer/2865944?hl=en#zippy=%2Clet-users-add-other-users-from-the-lock-screen)

### Disable Voice Controls

- Disable Google Assistant in Settings > Google
- [Google Assistant privacy settings](https://support.google.com/assistant/thread/226517535?hl=en&msgid=226543054)
- Consider [disabling microphone access entirely](https://support.google.com/android/answer/13532937?hl=en)

> **Why this matters:** Voice-controlled devices can be exploited to capture audio without your knowledge.

---

## Device Security

### Set Strong Screen Lock

- Use a **long passphrase** (minimum 10 characters)
- **Remove** fingerprint and face unlock:
  - [Remove fingerprint](https://support.google.com/googlepixeltablet/answer/13554937#zippy=%2Cremove-a-fingerprint)
  - [Delete Face Unlock](https://support.google.com/pixelphone/answer/9517039?hl=en#zippy=%2Cdisable-or-delete-face-unlock)
- **Avoid** pattern locks (easily guessed) and swipe-to-unlock
- Disable "make password visible"
- Set screen timeout to 1-5 minutes

> **Why this matters:** Biometrics can be compelled or faked. A strong passphrase provides the best protection against physical access.

### Create Separate User Accounts

- Create an admin account and standard accounts for daily use
- [Add users on Android](https://support.google.com/android/answer/2865483#zippy=%2Cadd-user)
- [Remove unnecessary users](https://support.google.com/android/answer/2865483#zippy=%2Cdelete-user)

### Secure Connected Google Accounts

- [Check which devices use your account](https://support.google.com/accounts/answer/3067630)
- Complete the [Google security checkup](https://myaccount.google.com/security-checkup)
- Consider [Google's Advanced Protection program](https://landing.google.com/advancedprotection/)
- Screenshot any suspicious activity for documentation

---

## Connectivity and Sharing

### Turn Off Unused Connectivity

- Power off devices at night
- Keep wifi, Bluetooth, and hotspot off when not in use
- Use Airplane mode for quick disconnection
- [Disable "Turn on Wi-Fi automatically" and "Notify for public networks"](https://support.google.com/pixelphone/answer/9655181?hl=en#zippy=%2Cchange-more-wi-fi-settings)

> **Why this matters:** Wireless connections broadcast identifying information that can be used to track or target your device.

### Clear Saved Wifi Networks

- Store network credentials in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassdx)
- [Remove saved networks](https://support.google.com/android/answer/9075847#zippy=%2Cremove-a-saved-network) you no longer use

### Turn Off Unused Sharing Features

- Disable or remove connected devices in Settings
- [Turn off Quick Share/Nearby Share](https://support.google.com/android/answer/9286773)

---

## Physical Security

### Use a Privacy Screen Filter

A privacy filter limits screen visibility from side angles, protecting against "shoulder surfing." See [Security Planner's guide](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen).

### Use a Camera Cover

- Locate all cameras on your device
- Use a small adhesive bandage (non-sticky center) or sliding webcam cover
- Consider [disabling camera access entirely](https://support.google.com/android/answer/13532937?hl=en)

---

## Keyboard Privacy

- Check installed keyboards: Settings > System > Keyboard > On-screen keyboard
- Remove unused keyboard apps
- **For Gboard users**, disable in Gboard settings:
  - Auto-correction
  - Smart compose
  - Smart replies

**Privacy-focused alternatives:**
- [HeliBoard](https://github.com/Helium314/HeliBoard)
- [Simple Keyboard](https://github.com/rkkr/simple-keyboard)

> **Why this matters:** Keyboard apps can transmit everything you type to their developers.

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

Remove or skip Google account setup to prevent Google tracking:
- [Remove Google account](https://support.google.com/android/answer/7664951#remove_account)
- Use [F-Droid](https://f-droid.org/) and [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) for apps
- **Important:** Manually update apps regularly—automatic updates may not work

### Install Alternative Operating Systems

For maximum privacy, consider:
- [GrapheneOS](https://grapheneos.org/) (security-focused)
- [CalyxOS](https://calyxos.org/) (privacy-focused)

> **Warning:** This is advanced. Verify device compatibility and follow instructions carefully to avoid bricking your device.

---

## Additional Resources

- [Security in a Box Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Google Security Tips](https://safety.google/security/security-tips/)