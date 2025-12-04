---
title: "Protect Your Android Device"
tags: [android, mobile-security, privacy, device-hardening, google]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Android Security", "Device Hardening", "Privacy Protection", "Mobile Privacy"]
summary: "Comprehensive guide to securing Android devices through system updates, app management, privacy settings, and advanced protection techniques."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic smartphone literacy", "Access to Android device settings"]
estimated_read_time: "25 minutes"
---

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
- **Nokia**: [Security and Maintenance Summary](https://www.hmd.com/en_int/security-updates)
- **Other manufacturers**: [Android Authority update policies guide](https://www.androidauthority.com/phone-update-policies-1658633/)

If your Android version is unmaintained, consider buying a new device. Check maintenance status at [Android version history](https://en.wikipedia.org/wiki/Android_version_history) or [Android end of life dates](https://endoflife.date/android).

> **Why this matters:** Vulnerabilities in device code are discovered daily. Developers cannot predict where they will be found due to code complexity. Attackers exploit these vulnerabilities to access your devices. Regular updates fix these security holes.

### Regularly Update All Installed Apps

- [Update the Google Play Store app](https://support.google.com/googleplay/answer/113412#update_google_play_store)
- [Enable automatic app updates](https://support.google.com/googleplay/answer/113412#auto)

---

## App Management

### Use Apps from Trusted Sources

- **Do not root your device**—it increases malware infection risk
- Install apps from the [Google Play Store](https://play.google.com/store)
- [Enable Google Play Protect](https://support.google.com/accounts/answer/2812853) to verify apps and disable unknown source installation
- If apps are unavailable in your country, consider [changing your Google Play country](https://support.google.com/googleplay/answer/7431675) (may require a [VPN](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service))

**Trusted alternative app stores:**
- [F-Droid](https://f-droid.org/) (free and open-source apps)
- [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) (anonymous Google Play access)

> **Why this matters:** The Google Play Store is the official Android app store, making it easier for Google to monitor apps for security violations. Some governments demand app bans, leading people to "root" devices for third-party stores—this is unnecessary if you use [censorship circumvention techniques](https://securityinabox.org/en/internet-connection/anonymity-and-circumvention/).

### Remove Unnecessary Apps

- [Delete apps you don't use](https://support.google.com/googleplay/answer/13627402)
- [Disable or remove manufacturer bloatware](https://www.howtogeek.com/115533/how-to-disable-or-uninstall-android-bloatware/)

> **Why this matters:** Unused apps can contain vulnerabilities and may transmit information about you (like location) without your knowledge. Reducing installed apps limits your attack surface.

### Avoid Social Media Apps When Possible

Access social media through your secure browser (like [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)) instead of dedicated apps.

> **Why this matters:** Social media apps (Facebook, Instagram, etc.) collect extensive data including your phone ID, phone number, and wifi connections. Browser access provides better privacy protection.

### Use Privacy-Friendly Apps

- **Web browsing**: [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)
- **Email**: [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail)
- **App stores**: [F-Droid](https://f-droid.org/en/) or [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore)

After installing privacy-friendly alternatives, [uninstall or disable](https://securityinabox.org/en/phones-and-computers/android/#remove-apps-that-you-do-not-need-and-do-not-use) the default apps you won't use.

### Check Your App Permissions

Review and restrict permissions for sensitive access:
- Voice/speech recognition
- Camera and screen recording
- Call logs and history
- Fingerprint reader and facial recognition
- Near field communications (NFC)
- Disk access, files, folders, system settings
- Installation permissions
- Physical activity and Health Connect

[Manage app permissions on Android](https://support.google.com/android/answer/9431959?hl=en) to change permissions, understand their implications, and disable camera/microphone access device-wide.

> **Why this matters:** Apps accessing sensitive services can leak information or be exploited by attackers. Disable permissions you don't actively need.

---

## Location and Privacy Settings

### Turn Off Location and Wipe History

- [Turn off location services](https://support.google.com/android/answer/3467281) overall and [for individual apps](https://support.google.com/android/answer/6179507)
- Regularly delete location history:
  - [Google Maps Timeline](https://support.google.com/accounts/answer/3118687?#delete)
  - [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Devices track location via GPS, cell towers, and wifi. This record can be used to find you or prove your presence at specific locations and associations with specific people.

### Control Lock Screen Visibility

- [Hide all notifications on lock screen](https://support.google.com/android/answer/9079661#zippy=%2Coption-dont-show-any-notifications)
- Disable "Add users from lock screen" in [guest and user settings](https://support.google.com/pixelphone/answer/2865944?hl=en#zippy=%2Clet-users-add-other-users-from-the-lock-screen)

> **Why this matters:** A strong screen lock is useless if notifications display sensitive information to anyone who picks up your device.

---

## Screen Lock and Physical Security

### Set Your Screen to Sleep and Lock

**Recommended lock settings:**
- Use a **long passphrase** (minimum 10 characters)—not a short PIN or password
- Remove fingerprints and face data from your device:
  - [Remove fingerprint](https://support.google.com/googlepixeltablet/answer/13554937#zippy=%2Cremove-a-fingerprint)
  - [Delete Face Unlock](https://support.google.com/pixelphone/answer/9517039?hl=en#zippy=%2Cdisable-or-delete-face-unlock)
- **Do not use** pattern locks (easily guessed)
- **Do not use** simple swipe-to-unlock
- Disable "make password visible"
- Set screen timeout to 1-5 minutes under [Display settings](https://support.google.com/pixelphone/answer/6111557?hl=en)

> **Why this matters:** If arrested, detained, or searched, you can be forced to unlock with biometrics. Short PINs can be guessed with software. Pattern locks leave visible finger tracks. A long passphrase is the safest option.

### Disable Voice Controls

- Disable Google Assistant and voice control (Settings > Google)
- Review [Google Assistant privacy settings](https://support.google.com/assistant/thread/226517535?hl=en&msgid=226543054)
- Consider [disabling microphone access device-wide](https://support.google.com/android/answer/13532937?hl=en)

> **Why this matters:** Voice-controlled devices can be exploited to capture audio. If you need voice controls for accessibility, follow [Security Planner's safer setup instructions](https://securityplanner.consumerreports.org/tool/secure-your-smart-speaker).

### Use Physical Privacy Protections

**Privacy screen filter:**
- Prevents shoulder surfing attacks
- [Security Planner guide on privacy filters](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen)

**Camera cover:**
- Use a small adhesive bandage (non-sticky center protects lens)
- Or search for "webcam privacy cover thin slide" for your device model
- Consider [disabling camera access device-wide](https://support.google.com/android/answer/13532937?hl=en)

> **Why this matters:** Some attacks are low-tech—people looking over your shoulder or malicious software activating your camera to spy on you.

---

## Connectivity and Network Security

### Turn Off Unused Connectivity

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use Airplane mode for quick connectivity shutdown (selectively enable wifi/Bluetooth as needed)
- In [advanced network settings](https://support.google.com/pixelphone/answer/9655181?hl=en#zippy=%2Cchange-more-wi-fi-settings), disable:
  - "Turn on Wi-Fi automatically"
  - "Notify for public networks"
- Turn off hotspot when not in use

> **Why this matters:** Wireless connections can be exploited by nearby attackers. When enabled, your device broadcasts names of previously connected networks—a unique fingerprint that can identify and target your device.

### Clear Saved Wifi Networks

- Save network credentials in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassdx) instead
- Regularly [remove saved networks](https://support.google.com/android/answer/9075847#zippy=%2Cremove-a-saved-network) you no longer use
- Disable automatic wifi connection and public network notifications

### Turn Off Unused Sharing Features

- In Settings, find "connected devices" or "device connections" and remove all devices
- [Disable Quick Share/Nearby Share](https://support.google.com/android/answer/9286773)—enable only when sharing with trusted devices

> **Why this matters:** File sharing features left enabled can be exploited by malicious actors to access your files.

---

## Keyboard Privacy

### Ensure Your Keyboard Respects Privacy

**Check your keyboard:**
1. Go to Settings > System > Keyboard > On-screen keyboard
2. Disable and delete unused keyboard apps
3. Verify custom keyboards are trustworthy

**If using Gboard (Google's default keyboard):**
1. [Open Gboard settings](https://support.google.com/gboard/answer/6380730?co=GENIE.Platform%3DAndroid&oco=0#zippy=%2Cchange-your-settings)
2. Tap Text correction or Corrections & suggestions
3. Disable: Auto-correction, Smart compose, Smart replies

**Privacy-friendly alternatives:**
- [HeliBoard](https://github.com/Helium314/HeliBoard)
- [Simple Keyboard](https://github.com/rkkr/simple-keyboard?tab=readme-ov-file)

> **Why this matters:** Keyboard apps can send typing data to their developers. Gboard's advanced features share voice and text data with Google.

---

## Account and User Management

### Create Separate User Accounts

- Create multiple user accounts with one "admin" and others "standard"
- Use a standard user for day-to-day work
- [Add users on Android](https://support.google.com/android/answer/2865483#zippy=%2Cadd-user)

### Remove Unneeded Users

- [Delete unused user accounts](https://support.google.com/android/answer/2865483#zippy=%2Cdelete-user)

> **Why this matters:** Separate accounts protect sensitive information when sharing devices. Removing unused accounts reduces your attack surface and may reveal unauthorized accounts.

### Secure Connected Google Accounts

1. Log in to each Google account associated with your device
2. [Check which devices use your account](https://support.google.com/accounts/answer/3067630)
3. Follow [account protection steps](https://securityinabox.org/en/tools/google/#account-protection)
4. Review [social media accounts](https://securityinabox.org/en/communication/social-media) connected to your device
5. Screenshot suspicious activity (unrecognized devices, disposed devices)
6. Check for [suspicious access](https://securityinabox.org/en/tools/google/#look-for-suspicious-access)
7. Complete the [security checkup](https://myaccount.google.com/security-checkup)
8. Consider [Google's Advanced Protection program](https://landing.google.com/advancedprotection/)

---

## Advanced Security Measures

### Detect Unauthorized Device Access (Basic Forensics)

- [Check devices linked to chat applications](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/smartphones/linkeddevices.md)
- [Review installed applications](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/applications.md)
- [Check if phone is rooted](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/root.md)
- [Check for stalkerware](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/stalkerware.md)
- If compromised: [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/topics/device-acting-suspiciously/#android-intro)

### Use Android Without a Google Account

Remove Google tracking by removing your Google account or skipping sign-in during initial setup.

**Alternative app installation:**
1. [Download F-Droid APK](https://f-droid.org/) from the official website
2. Temporarily [allow installing unknown apps](https://www.androidauthority.com/how-to-install-apks-31494/#1)
3. Install F-Droid, then revoke installation permissions
4. [Install Aurora Store from F-Droid](https://f-droid.org/en/packages/com.aurora.store/)
5. Manually check for updates regularly—automatic updates may not work

### Change Your Android Operating System

For maximum privacy, install alternative operating systems:
- [GrapheneOS](https://grapheneos.org/) (security and privacy focused)
- [CalyxOS](https://calyxos.org/) (privacy focused)

> **Warning:** This is an advanced solution. Verify device compatibility and follow instructions carefully—incorrect installation can make your device unusable.

---

## Additional Resources

- [Security in a Box malware guide](https