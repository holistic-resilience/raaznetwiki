---
title: "Android Privacy Guide"
tags: [android, mobile-security, privacy, google-alternatives, custom-rom, digital-security]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Android Users]
topics: ["Android Security", "Mobile Privacy", "Custom ROMs", "Google Alternatives"]
summary: "Guide to improving privacy on Android devices by replacing Google services, installing custom distributions, and following security best practices."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic smartphone literacy", "Understanding of app permissions"]
estimated_read_time: "8 minutes"
---

# Android Privacy Guide

![Android logo](https://www.privacyguides.org/en/assets/img/android/android.svg)

The **Android Open Source Project** (AOSP) is an open-source mobile operating system led by Google that powers the majority of the world's mobile devices. Most phones sold with Android are modified to include invasive integrations and apps such as Google Play Services, so you can significantly improve your privacy on your mobile device by replacing your phone's default installation with a version of Android without these invasive features.

## Key Recommendations

### Replace Google Services

There are many private alternatives to the apps that come pre-installed on your phone, such as the camera app. You can obtain applications from privacy-respecting sources and replace system utilities with alternatives that don't require Google Play Services.

### Install a Custom Distribution

When you buy an Android phone, the default operating system comes bundled with apps and functionality that are not part of the Android Open Source Project. Many of these apps—even apps like the dialer which provide basic system functionality—require invasive integrations with Google Play Services, which in turn asks for privileges to access your files, contacts storage, call logs, SMS messages, location, camera, microphone, and numerous other things on your device.

Frameworks like Google Play Services increase the attack surface of your device and are the source of various privacy concerns with Android.

**The solution:** Use an alternative Android distribution, commonly known as a *custom ROM*, that does not come with such invasive integration.

#### Choosing a Secure Custom ROM

Unfortunately, many custom Android distributions violate the Android security model by not supporting critical security features such as:

- AVB (Android Verified Boot)
- Rollback protection
- Firmware updates
- Proper SELinux enforcement

Some distributions ship `userdebug` builds which expose root via ADB and require more permissive SELinux policies to accommodate debugging features, resulting in increased attack surface and weakened security.

**When choosing a custom Android distribution, ensure it has:**

- Production builds (not userdebug)
- Support for AVB
- Rollback protection
- Timely firmware and operating system updates
- SELinux in enforcing mode

### Avoid Rooting Your Device

Rooting Android phones can significantly decrease security as it weakens the complete Android security model. This can decrease privacy should there be an exploit assisted by the decreased security.

**Problems with rooting:**

- **Compromises Verified Boot:** Common rooting methods involve directly tampering with the boot partition, making it impossible to perform successful Verified Boot
- **Modifies system partition:** Apps that require root modify the system partition, meaning Verified Boot must remain disabled
- **Increases attack surface:** Having root exposed directly in the user interface may assist in privilege escalation vulnerabilities and SELinux policy bypasses

#### Root-Based Apps to Avoid

Content blockers which modify the hosts file (like AdAway) and firewalls which require root access persistently (like AFWall+) are dangerous and should not be used.

**Better alternatives:**

- For content blocking: Use encrypted DNS or content blocking functionality provided by a VPN
- Note: TrackerControl and AdAway in non-root mode use the VPN slot (via local loopback VPN), preventing you from using privacy-enhancing services such as Orbot or a real VPN provider
- AFWall+ works based on packet filtering and may be bypassable in some situations

**The security sacrifices made by rooting a phone are not worth the questionable privacy benefits of those apps.**

### Install Updates Regularly

It's important to not use an end-of-life version of Android. Newer versions receive not only security updates but also important privacy-enhancing updates.

**Example:** Prior to Android 10, any app with the `READ_PHONE_STATE` permission could access sensitive and unique serial numbers of your phone such as IMEI, MEID, or your SIM card's IMSI. Now only system apps can access this information.

### Use Built-in Sharing Features

You can avoid giving many apps permission to access your media with Android's built-in sharing features.

**Example:** If you want to post a picture to Discord, open your file manager or gallery and share that picture with the Discord app, instead of granting Discord full access to your media and photos.

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/android/)*