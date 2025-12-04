Looking at this document, I need to:

1. Clean up the front matter with accurate metadata
2. Remove redundant content (like the orphaned list items at the top and duplicate table of contents)
3. Improve organization and formatting
4. Ensure consistent structure throughout

Let me process this comprehensively:

```markdown
---
title: "Protect Your Android Device"
tags: [android, mobile-security, privacy, device-hardening, google, app-permissions]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Android Security", "Mobile Privacy", "Device Hardening", "App Management"]
summary: "Comprehensive guide to securing Android devices through OS updates, app management, permission controls, and privacy settings."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic smartphone usage", "Access to device settings"]
estimated_read_time: "25 minutes"
related_guides: ["malware-protection", "password-management", "google-account-security"]
last_updated: "2025-09-17"
---

# Protect Your Android Device

Security starts with setting up your device to protect your information. Follow the steps in this guide to make your Android device more secure. Android devices differ by manufacturer, so you may need to look in a few places to find the settings you are looking for.

---

## Operating System & App Updates

### Use the Latest Version of Your Device's Operating System

**Why this matters:** New vulnerabilities in device and app code are discovered daily. Developers cannot predict where security flaws will be found due to code complexity. Malicious attackers exploit these vulnerabilities to access your devices. Regular updates fix these security holes, making it essential to install updates and use the latest OS version.

**Best practices:**
- Update from a trusted location and internet connection (home or office), not public wifi
- Set aside time for updates—they may require multiple downloads and restarts
- After updating, check again for additional updates until none remain
- Always restart your device when prompted after downloading updates

**Check your Android version:**
- [Find the most updated version available](https://developer.android.com/about/versions)
- [Compare and update your operating system](https://support.google.com/android/answer/7680439)
- [Check your "Android security update" date](https://support.google.com/android/answer/7680439?hl=en)—security updates are released at least monthly

**Device-specific update information:**
- **Google Pixel:** [Security update schedule](https://support.google.com/pixelphone/answer/4457705)
- **Samsung:** [Security updates page](https://security.samsungmobile.com/workScope.smsb)
- **Fairphone:** [End of life dates](https://endoflife.date/fairphone)
- **Motorola:** [Security update support](https://en-us.support.motorola.com/app/software-security-update)
- **Nokia:** [Security and maintenance releases](https://www.hmd.com/en_int/security-updates)
- **Other manufacturers:** [Android Authority's update policy guide](https://www.androidauthority.com/phone-update-policies-1658633/)

> **Important:** If your Android version is no longer maintained, consider purchasing a new device. Check maintenance status at [Wikipedia Android version history](https://en.wikipedia.org/wiki/Android_version_history) or [Android end of life dates](https://endoflife.date/android).

### Regularly Update All Installed Apps

- [Update the Google Play Store app](https://support.google.com/googleplay/answer/113412#update_google_play_store)
- [Enable automatic app updates](https://support.google.com/googleplay/answer/113412#auto)

---

## App Management

### Use Apps from Trusted Sources

**Why this matters:** The Google Play Store is the official Android app store, making it easier to find apps while allowing Google to monitor for major security violations. Centralized distribution provides better oversight of app safety.

**Recommendations:**
- Install apps primarily from the [Google Play Store](https://play.google.com/store)
- [Enable Google Play Protect](https://support.google.com/accounts/answer/2812853) to verify app sources and disable unknown source installation
- **Avoid "rooting" your device**—it increases risk of malicious code infection
- If apps are unavailable in your country, consider [changing your Google Play country](https://support.google.com/googleplay/answer/7431675) (may require a [VPN](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service))

**Trusted alternative app stores:**
- [F-Droid](https://f-droid.org/) — Free and open-source apps only
- [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore) — Anonymous access to Play Store apps

> **Note:** Some governments demand tech companies ban certain apps. If contacts encourage you to "root" your device for banned apps, use [censorship circumvention techniques](https://securityinabox.org/en/internet-connection/anonymity-and-circumvention/) instead—rooting is unnecessary and risky.

### Remove Unnecessary Apps

**Why this matters:** Removing unused apps limits the number of potentially vulnerable applications on your device. Unused apps may also transmit information about you (like location) without your knowledge. Fewer apps means reduced attack surface.

**Steps:**
- [Delete unused apps](https://support.google.com/googleplay/answer/13627402)
- [Disable or remove manufacturer bloatware](https://www.howtogeek.com/115533/how-to-disable-or-uninstall-android-bloatware/) (pre-installed apps that can't be fully uninstalled)

### Avoid Social Media Apps When Possible

**Why this matters:** Social media apps like Facebook and Instagram often collect excessive data, including your phone ID, phone number, and wifi connections. Using these services through a secure browser provides better privacy protection.

**Recommendation:** Access social media through your browser (like [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)) instead of dedicated apps.

### Use Privacy-Friendly Apps

**Why this matters:** Android devices come with built-in apps that require Google account login (Chrome, Gmail). Privacy-friendly alternatives reduce data collection.

**Recommended alternatives:**
- **Web browser:** [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)
- **Email:** [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail)
- **App stores:** [F-Droid](https://f-droid.org/en/) or [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore)

After installing privacy-friendly alternatives, [disable or uninstall](https://securityinabox.org/en/phones-and-computers/android/#remove-apps-that-you-do-not-need-and-do-not-use) the default apps you won't use.

### Check Your App Permissions

**Why this matters:** Apps with access to sensitive services (location, microphone, camera, device settings) can leak information or be exploited by attackers. Disable permissions that apps don't need for their core functions.

**Sensitive permissions to review:**
- Voice/speech recognition
- Camera and screen recording
- Microphone
- Call logs and history
- Location
- Files, folders, and disk access
- Fingerprint reader and facial recognition
- Near field communications (NFC)
- Physical activity and Health Connect
- Permission to install other apps

**How to manage:** See [Google's guide on changing app permissions](https://support.google.com/android/answer/9431959?hl=en), including how to disable camera or microphone access device-wide.

---

## Location Privacy

### Turn Off Location and Clear History

**Why this matters:** Your device tracks your physical location using GPS, cell towers, and wifi networks. This record could allow someone to find you, prove your presence at certain locations, or establish your associations with specific people.

**Steps:**
- [Turn off location services overall](https://support.google.com/android/answer/3467281) or when not in use
- [Manage location for individual apps](https://support.google.com/android/answer/6179507)
- Regularly clear location history:
  - [Google Maps Timeline](https://support.google.com/accounts/answer/3118687?#delete)
  - [Maps activity](https://support.google.com/maps/answer/3137804)

> **Note:** Location settings may be in Settings > Privacy, Settings > Security, or Google account preferences depending on your device.

---

## User Account Management

### Create Separate User Accounts

**Why this matters:** If you must share your device with others, separate user accounts protect your administrative permissions and sensitive files from other users.

**Recommendations:**
- Create one account with admin privileges and others with standard (non-admin) privileges
- Use a standard user account for day-to-day work
- [Add users on Android](https://support.google.com/android/answer/2865483#zippy=%2Cadd-user)

> **Best practice:** Avoid sharing devices used for sensitive work with anyone else.

### Remove Unneeded Users

**Why this matters:** Extra user accounts create additional access points ("doors") to your device. Checking existing users may also reveal accounts created without your knowledge.

**Steps:** [Delete unwanted users](https://support.google.com/android/answer/2865483#zippy=%2Cdelete-user)

### Secure Connected Google Accounts

**Why this matters:** Most devices have associated accounts (Google accounts for Android phones, Chromebooks, Google TV). Multiple devices may be logged into your Google account. Unauthorized access to your account affects all connected devices.

**Security checklist:**
1. Log in to each Google account associated with your device
2. [Check which devices use your account](https://support.google.com/accounts/answer/3067630)
3. Follow [account protection steps](https://securityinabox.org/en/tools/google/#account-protection)
4. Review [social media accounts](https://securityinabox.org/en/communication/social-media) connected to your device
5. Screenshot any suspicious activity (unrecognized devices, disposed devices)
6. Check [suspicious access indicators](https://securityinabox.org/en/tools/google/#look-for-suspicious-access)
7. Complete the [Google security checkup](https://myaccount.google.com/security-checkup)
8. Consider enrolling in [Google's Advanced Protection program](https://landing.google.com/advancedprotection/)

---

## Screen Lock & Display Security

### Set Your Screen to Sleep and Lock

**Why this matters:** Your device may be confiscated or stolen, allowing someone to break into it. A strong passphrase prevents unauthorized access. Technical attacks aside, physical access is a common threat.

**Security recommendations:**
- **Use a long passphrase** (minimum 10 characters)—not a short PIN or password
- **Remove biometric authentication** (fingerprints, face unlock):
  - [Remove fingerprints](https://support.google.com/googlepixeltablet/answer/13554937#zippy=%2Cremove-a-fingerprint)
  - [Delete Face Unlock](https://support.google.com/pixelphone/answer/9517039?hl=en#zippy=%2Cdisable-or-delete-face-unlock)
- **Avoid pattern locks**—they can be guessed from finger tracks on the screen
- **Disable "swipe to unlock"**—this provides no security
- **Disable "make password visible"**
- **Set short screen timeout** (1-5 minutes): Look for "Screen timeout" under [Display](https://support.google.com/pixelphone/answer/6111557?hl=en), System, or Security settings

> **Why avoid biometrics?** If arrested, detained, or searched, you could be forced to unlock with your face, voice, eyes, or fingerprint. Fingerprints can be duplicated, and face unlock has been defeated by similar hacks. A passphrase is the safest option.

### Control Lock Screen Visibility

**Why this matters:** A strong screen lock is undermined if notifications display sensitive information when your device is locked.

**Steps:**
- [Disable all lock screen notifications](https://support.google.com/android/answer/9079661#zippy=%2Coption-dont-show-any-notifications)
- If using multiple users, disable "Add users from lock screen" in [guest and user settings](https://support.google.com/pixelphone/answer/2865944?hl=en#zippy=%2Clet-users-add-other-users-from-the-lock-screen)

### Disable Voice Controls

**Why this matters:** Voice-controlled devices can be exploited—someone could install code to capture what your device hears. Unless you require voice controls for accessibility reasons, disable them.

**Steps:**
- Disable Google Assistant and voice control (Settings > Google, location varies by device)
- Review [Google Assistant privacy settings](https://support.google.com/assistant/thread/226517535?hl=en&msgid=226543054)
- Consider [disabling microphone access device-wide](https://support.google.com/android/answer/13532937?hl=en)

> **For accessibility needs:** If voice controls are necessary, follow [Security Planner's smart speaker guide](https://securityplanner.consumerreports.org/tool/secure-your-smart-speaker) and review [Google Assistant privacy information](https://developers.google.com/assistant/how-assistant-works/privacy).

### Use a Privacy Screen Filter

**Why this matters:** "Shoulder surfing"—someone viewing your screen over your shoulder or via security cameras—has compromised human rights defenders. A privacy filter makes your screen visible only from directly in front.

**More information:** [Security Planner guide on privacy filters](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen)

### Use a Camera Cover

**Why this matters:** Malicious software can activate your camera to spy on you and your surroundings without your knowledge.

**Options:**
- **Low-tech:** Apply a small adhesive bandage over the camera (the non-adhesive center won't make your lens sticky)
- **Commercial:** Search for your device model + "webcam privacy cover thin slide"
- **Software:** [Disable camera access device-wide](https://support.google.com/android/answer/13532937?hl=en)

> **Note:** Your smartphone likely has multiple cameras—check front and back.

---

## Connectivity & Network Security

### Turn Off Unused Connectivity

**Why this matters:** Wireless communications (wifi, NFC, Bluetooth) can be exploited by nearby attackers. When Bluetooth or wifi is enabled, your device broadcasts the names of previously connected networks and devices—this unique "fingerprint" can identify and target your device.

**Best practices:**
- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use Airplane mode for quick connectivity shutdown (you can selectively re-enable wifi or Bluetooth)
- [Disable "Turn on Wi-Fi automatically" and "Notify for public networks"](https://support.google.com/pixelphone/answer/9655181?hl=en#zippy=%2Cchange-more-wi-fi-settings)
- Turn off mobile hotspot when not in use

### Clear Saved Wifi Networks

**Why this matters:** Your saved network list can identify you. Erasing networks you no longer use and preventing constant network scanning protects against this identification.

**Steps:**
- Save network credentials in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassdx) instead of on your device
- Regularly [remove saved networks](https://support.google.com/android/answer/9075847#zippy=%2Cremove-a-saved-network) you no longer use
- [Disable automatic wifi connection and public network notifications](https://support.google.com/android/answer/9654714?#zippy=%2Cchange-more-wi-fi-settings)

### Turn Off Unused Sharing Features

**Why this matters:** File and service sharing features, while convenient, can be exploited by malicious actors if left enabled when not in use.

**Steps:**
- Check Settings for "connected devices" or "device connections" and turn off/remove all devices
- [Disable Quick Share/Nearby Share](https://support.google.com/android/answer/9286773)—only enable when sharing with trusted nearby devices