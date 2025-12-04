---
title: "Android Overview"
tags: [android, mobile-security, privacy, google, operating-systems, encryption]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Android Users, Security Researchers]
topics: ["Android Security", "Mobile Privacy", "Operating Systems"]
summary: "Comprehensive guide to Android's security model, privacy features, and Google services configuration for enhanced privacy."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic Android familiarity", "Understanding of mobile security concepts"]
estimated_read_time: "15 minutes"
---

# Android Overview

The **Android Open Source Project (AOSP)** is a secure mobile operating system featuring strong [app sandboxing](https://source.android.com/security/app-sandbox), [Verified Boot](https://source.android.com/security/verifiedboot) (AVB), and a robust [permission](https://developer.android.com/guide/topics/permissions/overview) control system.

## Security Protections

Key components of the Android security model include verified boot, firmware updates, and a robust permission system. These security features form the baseline criteria for evaluating mobile phones and custom Android OS distributions.

### Verified Boot

**Verified Boot** is an essential part of the Android security model, providing protection against:
- [Evil maid attacks](https://en.wikipedia.org/wiki/Evil_maid_attack)
- Malware persistence
- Security update downgrades via [rollback protection](https://source.android.com/security/verifiedboot/verified-boot#rollback-protection)

Android 10 and above uses [file-based encryption](https://source.android.com/security/encryption/file-based) instead of full-disk encryption. Your data is encrypted using unique encryption keys while operating system files remain unencrypted. Verified Boot ensures the integrity of these OS files, preventing adversaries with physical access from tampering with or installing malware on the device.

#### Important Considerations

- Only a few OEMs (such as Google) support custom AVB key enrollment
- AOSP derivatives like LineageOS or /e/ OS often do not support Verified Boot
- Some OEMs have broken Verified Boot implementations—for example, the Fairphone 3 and 4 stock bootloader trusts the public AVB signing key, which undermines security

> **Recommendation:** Verify Verified Boot support before purchasing a new device. AOSP derivatives without Verified Boot support are not recommended.

### Firmware Updates

Firmware updates are critical for maintaining security. OEMs have support agreements with partners to provide closed-source component updates for limited periods, detailed in monthly [Android Security Bulletins](https://source.android.com/security/bulletin).

**Support Periods by Manufacturer:**
| Manufacturer | Support Period |
|--------------|----------------|
| Qualcomm | 4 years |
| Samsung | 4 years |
| Google Pixel 6 | 5 years minimum |
| Google Pixel 8+ | 7 years |

> **Warning:** End-of-life (EOL) devices cannot receive firmware updates from OEM vendors or aftermarket Android distributors. Security issues on these devices will remain unfixed.

**Example:** Fairphone markets 6 years of support for the Fairphone 4, but the Qualcomm Snapdragon 750G SoC has an EOL date of September 2023, meaning firmware security updates end regardless of Fairphone's software updates.

### Android Permissions

[Permissions on Android](https://developer.android.com/guide/topics/permissions/overview) control what apps can access. All installed apps are strictly [sandboxed](https://source.android.com/security/app-sandbox), eliminating the need for antivirus apps.

> A smartphone with the latest Android version is always more secure than an old smartphone with paid antivirus software.

#### Permission Improvements by Android Version

**Android 10:**
- **Scoped Storage:** Greater control over files and external storage access
- **Background Location:** New `ACCESS_BACKGROUND_LOCATION` permission prevents silent location tracking

**Android 11:**
- One-time permissions
- Auto-reset permissions for unused apps
- Granular phone number access permissions

**Android 12:**
- Approximate location permission option
- Auto-reset of hibernated apps
- Data access auditing

**Android 13:**
- Nearby Wi-Fi access permission (prevents location tracking via MAC addresses)
- Granular media permissions (images, videos, or audio separately)
- Background sensor use requires `BODY_SENSORS` permission

#### Evaluating App Permissions

[Exodus Privacy](https://exodus-privacy.eu.org/) helps compare apps with similar purposes. Warning signs include:
- Excessive permissions beyond app functionality
- High numbers of advertising and analytics trackers

> **Note:** Evaluate trackers individually rather than counting totals. Privacy-friendly apps like [Bitwarden](https://reports.exodus-privacy.eu.org/en/reports/com.x8bit.bitwarden/latest) may include Google Firebase Analytics for push notification functionality, not analytics.

> **Warning:** Apps may track users server-side even without client-side trackers. Facebook shows "no trackers" in Exodus but tracks user behavior extensively through their servers.

## Privacy Features

### User Profiles

Multiple user profiles provide the simplest isolation method in Android.

**Location:** Settings → System → Users

### Work Profile

[Work Profiles](https://support.google.com/work/android/answer/6191949) isolate individual apps and may be more convenient than separate user profiles.

**Requirements:**
- A device controller app such as [Shelter](https://www.privacyguides.org/en/android/general-apps/#shelter) to create a Work Profile without enterprise MDM
- Or a custom Android OS with built-in work profile management

**Limitations:**
- Features like File Shuttle and contact search blocking depend on the device controller
- The device controller has full access to work profile data
- Generally less secure than a secondary user profile

### Private Space (Android 15+)

Private Space is a native Android 15 feature for isolating apps within the owner profile.

**Setup:** Settings → Security & privacy → Private space

**Characteristics:**
- Encrypted with its own encryption key
- Supports different unlock method than main profile
- Apps distinguished by key-within-shield icon
- No third-party app required (unlike work profiles)
- Can be used alongside work profiles

> **Recommendation:** Private Space is generally preferred over work profiles due to native implementation.

### VPN Kill Switch

Android 7+ includes a built-in VPN kill switch to prevent leaks when VPN disconnects.

**Location:** Settings → Network & internet → VPN → ⚙ → Block connections without VPN

### Global Toggles

Android 12 introduced camera and microphone toggles alongside existing Bluetooth and location toggles.

> **Recommendation:** Disable these features when not in use. Apps cannot use disabled features even with granted permissions.

## Google Services Configuration

For devices with Google services (stock OS or sandboxed Google Play like GrapheneOS), additional privacy improvements are possible.

### Advanced Protection Program

The [Advanced Protection Program](https://landing.google.com/advancedprotection) is free for anyone with two or more hardware security keys with [FIDO](https://www.privacyguides.org/en/basics/multi-factor-authentication/#fido-fast-identity-online) support or [passkeys](https://fidoalliance.org/passkeys).

**Benefits:**
- Stricter 2FA requirements (FIDO required; SMS OTP, TOTP, and OAuth disallowed)
- Only Google and verified third-party apps can access account data
- Enhanced Gmail phishing detection
- Stricter Chrome safe browsing
- Stricter account recovery process

**Additional benefits for non-sandboxed Google Play:**
- App installation restricted to Google Play Store, OS vendor store, or `adb`
- Mandatory Play Protect scanning
- Warnings about unverified applications

### Google Play System Updates

Android 10+ allows Google to push security updates for some system components via Play Services. For EOL devices running Android 10+ where recommended operating systems aren't available, stock OEM Android may be preferable to unsecured alternatives like LineageOS, as it still receives some Google security fixes.

### Advertising ID

All devices with Google Play Services generate an [advertising ID](https://support.google.com/googleplay/android-developer/answer/6048248) for targeted advertising.

**To disable on sandboxed Google Play (GrapheneOS):**
Settings → Apps → Sandboxed Google Play → Google Settings → All services → Ads → **Delete advertising ID**

**To disable on stock Android:**
- Settings → Google → Ads, or
- Settings → Privacy → Ads

Select "Delete advertising ID" if available; otherwise, opt out and reset the advertising ID.

### SafetyNet and Play Integrity API

These APIs are commonly used by banking apps. GrapheneOS with sandboxed Play services passes the `basicIntegrity` check but not `ctsProfileMatch`. Devices with Android 8+ have hardware attestation that cannot be bypassed without leaked keys or serious vulnerabilities.

> **Note:** Google Wallet is not recommended due to their [privacy policy](https://payments.google.com/payments/apis-secure/get_legal_document?ldo=0&ldt=privacynotice&ldl=en), which shares credit rating and personal information with affiliate marketing services unless you opt out.