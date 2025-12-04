---
title: "Protect Your Android Device"
tags: [android, mobile-security, privacy, google, app-permissions, device-hardening]
category: "Mobile Device Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Android Security", "Mobile Privacy", "Device Hardening", "App Management"]
summary: "Comprehensive guide to securing Android devices through OS updates, app management, permission controls, and privacy settings."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic smartphone literacy", "Access to an Android device"]
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
- **Google Pixel**: [Security update schedule](https://support.google.com/pixelphone/answer/4457705)
- **Samsung**: [Security updates page](https://security.samsungmobile.com/workScope.smsb)
- **Fairphone**: [End of life dates](https://endoflife.date/fairphone)
- **Motorola**: [Security update support](https://en-us.support.motorola.com/app/software-security-update)
- **Nokia**: [Security and Maintenance Release Summary](https://www.hmd.com/en_int/security-updates)
- **Other manufacturers**: [Android Authority update policies guide](https://www.androidauthority.com/phone-update-policies-1658633/)

If your Android version is unmaintained, consider buying a new device. Check [Android version history](https://en.wikipedia.org/wiki/Android_version_history) or [end of life dates](https://endoflife.date/android).

> **Why this matters:** Vulnerabilities in device code are discovered daily. Developers cannot predict where they will be found due to code complexity. Attackers exploit these vulnerabilities to access devices, but software updates fix them. Automatic updates reduce the tasks you need to remember.

### Regularly Update All Installed Apps

- [Update the Google Play Store app](https://support.google.com/googleplay/answer/113412#update_google_play_store)
- [Enable automatic app updates](https://support.google.com/googleplay/answer/113412#auto)

---

## App Management

### Use Apps from Trusted Sources

- **Do not "root" your device**—it increases malware risk
- Install apps from the [Google Play Store](https://play.google.com/store)
- [Enable Google Play Protect](https://support.google.com/accounts/answer/2812853) to verify apps and disable unknown sources
- If apps are unavailable in your country, consider [changing your Google Play country](https://support.google.com/googleplay/answer/7431675) (may require a [VPN](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service))

**Trusted alternative app stores:**
- [F-Droid](https://f-droid.org/) (free and open-source apps)
- [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) (anonymous access to Play Store apps)

> **Why this matters:** The Google Play Store is the official Android app store. Google monitors apps for security violations. Only install apps from trusted sources. "Mirror" download sites may be untrustworthy.

### Remove Unnecessary Apps

- [Delete unused apps](https://support.google.com/googleplay/answer/13627402)
- [Disable or remove pre-installed bloatware](https://www.howtogeek.com/115533/how-to-disable-or-uninstall-android-bloatware/)

> **Why this matters:** Unused apps can contain vulnerabilities and transmit information about you. Removing them limits your attack surface.

### Avoid Social Media Apps When Possible

Access social media through your browser instead of dedicated apps. Use a secure browser like [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox).

> **Why this matters:** Social media apps (Facebook, Instagram, etc.) collect extensive data including phone ID, phone number, and wifi connections. Browser access provides more privacy protection.

### Use Privacy-Friendly Apps

- **Web browsing**: [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)
- **Email**: [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail)
- **App stores**: [F-Droid](https://f-droid.org/en/) or [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore)

After installing privacy-friendly alternatives, [uninstall or disable](https://securityinabox.org/en/phones-and-computers/android/#remove-apps-that-you-do-not-need-and-do-not-use) default apps you won't use.

### Check Your App Permissions

Review and restrict permissions for sensitive access:
- Microphone and camera
- Location
- Contacts and call logs
- Files and storage
- Screen recording
- Fingerprint reader and facial recognition
- Physical activity and Health Connect
- Ability to download other apps

[Manage app permissions on Android](https://support.google.com/android/answer/9431959?hl=en) including how to disable camera or microphone access device-wide.

> **Why this matters:** Apps with access to sensitive services can leak information or be exploited by attackers. Disable permissions that apps don't need.

---

## Location and Privacy Settings

### Turn Off Location and Wipe History

- [Turn off location services overall](https://support.google.com/android/answer/3467281) when not in use
- [Manage location for individual apps](https://support.google.com/android/answer/6179507)
- Delete location history: [Google Maps Timeline](https://support.google.com/accounts/answer/3118687?#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Devices track location using GPS, cell towers, and wifi. This record can prove where you've been and who you've associated with.

### Control Lock Screen Visibility

- [Hide all notifications on lock screen](https://support.google.com/android/answer/9079661#zippy=%2Coption-dont-show-any-notifications)
- Disable "Add users from lock screen" in [guest and user settings](https://support.google.com/pixelphone/answer/2865944?hl=en#zippy=%2Clet-users-add-other-users-from-the-lock-screen)

> **Why this matters:** A strong screen lock is ineffective if notifications display sensitive information to anyone with physical access to your device.

### Disable Voice Controls

- Disable Google Assistant in Settings > Google
- Review [Google Assistant privacy settings](https://support.google.com/assistant/thread/226517535?hl=en&msgid=226543054)
- Consider [disabling microphone access device-wide](https://support.google.com/android/answer/13532937?hl=en)

If you need voice controls for accessibility, follow [Security Planner instructions](https://securityplanner.consumerreports.org/tool/secure-your-smart-speaker) and review [Google Assistant privacy guide](https://developers.google.com/assistant/how-assistant-works/privacy).

> **Why this matters:** Voice-controlled devices can be exploited to capture audio. Unless needed for accessibility, disable voice controls entirely.

---

## Screen Lock and Physical Security

### Set Your Screen to Sleep and Lock

**Recommended settings:**
- Use a **long passphrase** (minimum 10 characters)
- Remove fingerprints and face unlock: [remove fingerprint](https://support.google.com/googlepixeltablet/answer/13554937#zippy=%2Cremove-a-fingerprint), [delete Face Unlock](https://support.google.com/pixelphone/answer/9517039?hl=en#zippy=%2Cdisable-or-delete-face-unlock)
- Disable "make password visible"
- Set screen timeout to 1-5 minutes in [Display settings](https://support.google.com/pixelphone/answer/6111557?hl=en)

**Avoid:**
- Pattern locks (can be guessed from finger tracks)
- Simple swipe to unlock
- Short PINs or passwords

> **Why this matters:** If your device is confiscated or stolen, biometrics can be forced (face, fingerprint, voice). Short PINs can be guessed by software. Pattern locks leave visible traces. A long passphrase is the safest option.

### Use Physical Privacy Measures

**Privacy filter:**
- Apply a [privacy filter screen](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent shoulder surfing

**Camera cover:**
- Use a small adhesive bandage (non-sticky middle won't damage lens)
- Or search for "webcam privacy cover thin slide" for your device model
- Consider [disabling camera access device-wide](https://support.google.com/android/answer/13532937?hl=en)

> **Why this matters:** "Shoulder surfing" attacks are common. Malicious software can activate cameras without your knowledge.

---

## Connectivity and Network Security

### Turn Off Unused Connectivity

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use Airplane mode for quick disconnection (selectively re-enable wifi/Bluetooth as needed)
- [Disable "Turn on Wi-Fi automatically" and "Notify for public networks"](https://support.google.com/pixelphone/answer/9655181?hl=en#zippy=%2Cchange-more-wi-fi-settings)
- Turn off hotspot when not in use

> **Why this matters:** Wireless connections can be exploited by nearby attackers. When enabled, your device broadcasts names of previously connected networks, creating a unique fingerprint that can identify and target your device.

### Clear Saved Wifi Networks

- Save network credentials in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassdx) instead
- Regularly [remove saved networks](https://support.google.com/android/answer/9075847#zippy=%2Cremove-a-saved-network) you no longer use
- [Disable automatic wifi connection features](https://support.google.com/android/answer/9654714?#zippy=%2Cchange-more-wi-fi-settings)

### Turn Off Unused Sharing Features

- Look for "connected devices" or "device connections" in Settings and remove all devices
- [Disable Quick Share/Nearby Share](https://support.google.com/android/answer/9286773)—only enable when sharing with trusted nearby devices

---

## Keyboard Privacy

### Secure Your Keyboard App

1. Check your keyboard: Settings > System > Keyboard > On-screen keyboard
2. Disable and delete unused keyboard apps
3. Verify custom keyboards are trustworthy, or restore the default

**For Gboard (default on most Android devices):**
1. [Open Gboard settings](https://support.google.com/gboard/answer/6380730?co=GENIE.Platform%3DAndroid&oco=0#zippy=%2Cchange-your-settings)
2. Go to Text correction/Corrections & suggestions
3. Disable: Auto-correction, Smart compose, Smart replies

**Privacy-friendly alternatives:**
- [HeliBoard](https://github.com/Helium314/HeliBoard)
- [Simple Keyboard](https://github.com/rkkr/simple-keyboard?tab=readme-ov-file)

> **Why this matters:** Keyboard apps can transmit your typing activity to their developers. Gboard's advanced features send voice and text data to Google.

---

## User Account Management

### Create Separate User Accounts

- Create an admin account and standard (non-admin) accounts
- Use a standard user for daily work
- [Add users on Android](https://support.google.com/android/answer/2865483#zippy=%2Cadd-user)

> **Why this matters:** If you must share devices, separate user accounts protect administrative permissions and sensitive files from other users.

### Remove Unneeded Users

- [Delete unused user accounts](https://support.google.com/android/answer/2865483#zippy=%2Cdelete-user)
- Check for accounts created without your knowledge

### Secure Connected Google Accounts

1. Log in to each Google account on your device
2. [Check which devices use your account](https://support.google.com/accounts/answer/3067630)
3. Follow [Google account protection steps](https://securityinabox.org/en/tools/google/#account-protection)
4. Screenshot suspicious activity (unrecognized devices, disposed devices)
5. Check [suspicious access](https://securityinabox.org/en/tools/google/#look-for-suspicious-access)
6. Complete the [security checkup](https://myaccount.google.com/security-checkup)
7. Consider [Google's Advanced Protection program](https://landing.google.com/advancedprotection/)

> **Why this matters:** Multiple devices may be logged into your Google account. Unauthorized access to your account gives access to all connected devices.

---

## Advanced Security Measures

### Detect Unauthorized Access (Basic Forensics)

- [Check devices linked to chat applications](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/smartphones/linkeddevices.md)
- [Review installed applications](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/applications.md)
- [Check if phone is rooted](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/root.md)
- [Check for stalkerware](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/stalkerware.md)
- If compromised, follow [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/topics/device-acting-suspiciously/#android-intro)

### Use Android Without a Google Account

To remove Google tracking:
- [Remove your Google account](https://support.google.com/android/answer/7664951#remove_account) from your device
- Or skip "Sign in" during initial setup

**Without a Google account, use alternative app stores:**
- [Download F-Droid APK](https://f-droid.org/) from the official website
- [Install Aurora Store from F-Droid](https://f-droid.org/en/packages/com.aurora.store/)
- Manually check for updates regularly—automatic updates may not work

### Install an Alternative Operating System

For maximum privacy, consider security-focused Android alternatives:
- [GrapheneOS](https://grapheneos.org/)
- [CalyxOS](https://calyxos.org/)

> **Warning:** This is an advanced procedure. Verify device compatibility before attempting. Incorrect installation can make your device unusable.

---

## Additional Resources

- [Security in a Box malware guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Google's security tips](https://safety.google/security/security-tips/)