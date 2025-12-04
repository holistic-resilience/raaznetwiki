```yaml
---
title: "Protect Your Android Device"
tags: [android, mobile-security, privacy, google, app-permissions, device-hardening]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Android Security", "Privacy Protection", "Device Hardening", "App Management"]
summary: "Comprehensive guide to securing Android devices through OS updates, app management, privacy settings, and advanced configurations."
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

## Keep Your System Updated

### Use the Latest Operating System Version

- Update from a trusted location and internet connection (home or office), not public wifi
- Set aside time for updates—they may require multiple downloads and restarts
- After updating, check again for additional updates until none remain
- Always restart your device when prompted after downloading updates

**Check your versions:**
- Find the [most updated Android version available](https://developer.android.com/about/versions)
- [Compare and update your operating system](https://support.google.com/android/answer/7680439)
- Check your "Android security update" date—security updates release monthly

**Device-specific update information:**
- [Google Pixel](https://support.google.com/pixelphone/answer/4457705)
- [Samsung](https://security.samsungmobile.com/workScope.smsb)
- [Fairphone](https://endoflife.date/fairphone)
- [Motorola](https://en-us.support.motorola.com/app/software-security-update)
- [Nokia](https://www.hmd.com/en_int/security-updates)
- [Other manufacturers](https://www.androidauthority.com/phone-update-policies-1658633/)

If your Android version is unmaintained, consider buying a new device. Check [Android version history](https://en.wikipedia.org/wiki/Android_version_history) or [end of life dates](https://endoflife.date/android).

> **Why this matters:** Vulnerabilities are discovered daily. Developers release patches to fix them, making updates essential protection against attackers exploiting these weaknesses.

### Regularly Update All Installed Apps

- [Update the Google Play Store app](https://support.google.com/googleplay/answer/113412#update_google_play_store)
- [Enable automatic app updates](https://support.google.com/googleplay/answer/113412#auto)

---

## Manage Your Apps Securely

### Use Apps from Trusted Sources

- **Do not root your device**—it increases malware risk
- Install apps from the [Google Play Store](https://play.google.com/store)
- [Enable Google Play Protect](https://support.google.com/accounts/answer/2812853) to verify apps and disable unknown sources
- If apps aren't available in your country, consider [changing your Play Store country](https://support.google.com/googleplay/answer/7431675) using a [VPN](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service)

**Trusted alternative sources:**
- [F-Droid](https://f-droid.org/) (free and open-source apps)
- [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) (anonymous Google Play access)

> **Why this matters:** Centralized app stores enable security monitoring. Third-party sources and rooting increase exposure to malicious code.

### Remove Unnecessary Apps

- [Delete apps you don't use](https://support.google.com/googleplay/answer/13627402)
- [Disable or remove pre-installed bloatware](https://www.howtogeek.com/115533/how-to-disable-or-uninstall-android-bloatware/)

> **Why this matters:** Each app is a potential vulnerability. Unused apps may also transmit data about you, including location.

### Avoid Social Media Apps When Possible

Access social media through your browser (like [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)) instead of dedicated apps, which collect more data including phone ID, phone number, and wifi connections.

### Use Privacy-Friendly Alternatives

- **Browser:** [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)
- **Email:** [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail)
- **App stores:** [F-Droid](https://f-droid.org/en/) or [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore)

Once configured, [uninstall or disable](https://securityinabox.org/en/phones-and-computers/android/#remove-apps-that-you-do-not-need-and-do-not-use) default apps you won't use.

---

## Control App Permissions

Review and restrict permissions for sensitive access:

- Voice/speech recognition
- Camera and screen recording
- Call logs and history
- Fingerprint reader and facial recognition
- Near field communications (NFC)
- Disk/file/folder access
- Installation permissions
- Physical activity and Health Connect

[Manage permissions through Google's guide](https://support.google.com/android/answer/9431959?hl=en), including how to disable camera or microphone access device-wide.

> **Why this matters:** Apps accessing sensitive services can leak information or be exploited. Disable permissions you don't actively need.

---

## Protect Your Location Data

- [Turn off location services](https://support.google.com/android/answer/3467281) when not needed—both device-wide and [per app](https://support.google.com/android/answer/6179507)
- Regularly clear location history:
  - [Google Maps Timeline](https://support.google.com/accounts/answer/3118687#delete)
  - [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location records can prove where you've been and who you've associated with, creating significant privacy and safety risks.

---

## Secure Device Access

### Set Your Screen to Sleep and Lock

- Use a **passphrase** (minimum 10 characters)—not a PIN, pattern, or biometric
- Remove fingerprints and face data if previously enrolled:
  - [Remove fingerprint](https://support.google.com/googlepixeltablet/answer/13554937#zippy=%2Cremove-a-fingerprint)
  - [Delete Face Unlock](https://support.google.com/pixelphone/answer/9517039?hl=en#zippy=%2Cdisable-or-delete-face-unlock)
- Disable "make password visible"
- Set screen timeout to 1-5 minutes (Settings > Display or Security)

> **Why this matters:** Biometrics can be compelled or faked. Short PINs and patterns are easily guessed or observed. A long passphrase provides the strongest protection.

### Control Lock Screen Information

- [Hide all notifications on lock screen](https://support.google.com/android/answer/9079661#zippy=%2Coption-dont-show-any-notifications)
- Disable "Add users from lock screen" ([Google's guide](https://support.google.com/pixelphone/answer/2865944?hl=en#zippy=%2Clet-users-add-other-users-from-the-lock-screen))

### Disable Voice Controls

- Turn off Google Assistant (Settings > Google)
- [Follow Google Assistant disabling instructions](https://support.google.com/assistant/thread/226517535?hl=en&msgid=226543054)
- Consider [disabling microphone access entirely](https://support.google.com/android/answer/13532937?hl=en)

> **Why this matters:** Voice-controlled devices can be exploited to capture audio. Disable unless needed for accessibility.

---

## Manage User Accounts

### Create Separate User Accounts

- Create an admin account and standard accounts for daily use
- [Add users](https://support.google.com/android/answer/2865483#zippy=%2Cadd-user)

### Remove Unneeded Users

- [Delete unused accounts](https://support.google.com/android/answer/2865483#zippy=%2Cdelete-user)

> **Why this matters:** Separate accounts protect sensitive data when sharing devices. Unused accounts are unnecessary attack surfaces.

### Secure Connected Google Accounts

- [Review which devices use your account](https://support.google.com/accounts/answer/3067630)
- Screenshot any suspicious activity
- Complete the [security checkup](https://myaccount.google.com/security-checkup)
- Consider [Google's Advanced Protection program](https://landing.google.com/advancedprotection/)

---

## Physical Security Measures

### Use a Privacy Screen Filter

A [privacy filter](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) prevents "shoulder surfing"—someone viewing your screen from an angle.

### Use a Camera Cover

- Identify all cameras on your device
- Apply a small adhesive bandage (non-sticky center protects lens) or purchase a sliding cover
- Consider [disabling camera access entirely](https://support.google.com/android/answer/13532937?hl=en)

> **Why this matters:** Malicious software can activate cameras without your knowledge.

---

## Secure Connectivity

### Turn Off Unused Connections

- Power off devices at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use Airplane mode for quick disconnection (selectively re-enable wifi/Bluetooth as needed)
- Disable ["Turn on Wi-Fi automatically" and "Notify for public networks"](https://support.google.com/pixelphone/answer/9655181?hl=en#zippy=%2Cchange-more-wi-fi-settings)
- Turn off hotspot when not in use

> **Why this matters:** Wireless connections can be exploited by nearby attackers. Your device broadcasts known network names, creating a unique fingerprint that can identify you.

### Clear Saved Wifi Networks

- Store network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassdx) instead
- [Regularly remove saved networks](https://support.google.com/android/answer/9075847#zippy=%2Cremove-a-saved-network)

### Turn Off Unused Sharing Features

- Look for "connected devices" or "device connections" in Settings
- [Disable Quick Share/Nearby Share](https://support.google.com/android/answer/9286773) unless actively needed

---

## Keyboard Privacy

- Check installed keyboards: Settings > System > Keyboard > On-screen keyboard
- Remove any keyboards you don't use
- Verify custom keyboards are trustworthy

**For Gboard users:**
1. [Open Gboard settings](https://support.google.com/gboard/answer/6380730?co=GENIE.Platform%3DAndroid&oco=0#zippy=%2Cchange-your-settings)
2. Disable Auto-correction, Smart compose, and Smart replies

**Privacy-focused alternatives:**
- [HeliBoard](https://github.com/Helium314/HeliBoard)
- [Simple Keyboard](https://github.com/rkkr/simple-keyboard)

> **Why this matters:** Keyboard apps can transmit everything you type. Even Gboard shares usage data with Google.

---

## Advanced: Detect Unauthorized Access

If you suspect compromise:
- [Check devices linked to chat apps](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/smartphones/linkeddevices.md)
- [Review installed applications](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/applications.md)
- [Check if phone is rooted](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/root.md)
- [Check for stalkerware](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/android/stalkerware.md)
- Follow [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/topics/device-acting-suspiciously/#android-intro)

---

## Advanced: Use Android Without Google

To remove Google tracking:
- [Remove your Google account](https://support.google.com/android/answer/7664951#remove_account) or skip sign-in during initial setup
- Use alternative app stores:
  - **F-Droid:** [Download APK](https://f-droid.org/) (temporarily allow unknown apps, then revoke)
  - **Aurora Store:** [Install from F-Droid](https://f-droid.org/en/packages/com.aurora.store/)
- Manually check for app updates regularly—automatic updates may not work

---

## Advanced: Install Alternative Operating Systems

For maximum privacy, consider replacing Android with:
- [GrapheneOS](https://grapheneos.org/) (security-focused)
- [CalyxOS](https://calyxos.org/) (privacy-focused)

**Warning:** Verify device compatibility before attempting. Incorrect installation can render your device unusable.

---

## See Also

- [Security in a Box: Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Google Security Tips](https://safety.google/security/security-tips/)