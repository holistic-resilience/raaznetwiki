---
title: "Quick Security Recommendations for Your Devices"
tags: [security, privacy, device-security, passwords, two-factor-authentication, operating-systems]
category: "Digital Security"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["Device Security", "Privacy Protection", "Account Security"]
summary: "Essential first steps for protecting your devices across Android, iOS, Windows, macOS, and Linux platforms."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Access to your devices"]
estimated_read_time: "8 minutes"
---

# Quick Security Recommendations for Your Devices

People often ask where they can start and what minimum steps they should consider taking to better protect their devices. This guide shares the first, often most effective, and most important security measures.

## General Recommendations

1. **Use unique, strong passwords** for each account, storing them safely with a [password manager](https://securityinabox.org/en/passwords/password-managers/).

2. **Enable two-factor authentication (2FA)** on [supported accounts](https://2fa.directory/):
   - **First choice**: Hardware security keys (see recommendations below)
   - **Alternative**: TOTP apps that generate time-based one-time passwords
   - **Avoid**: SMS-based 2FA when possible

3. **Avoid biometric authentication** (Face ID, fingerprint) as your primary method. [Learn why in the password guide](https://securityinabox.org/en/passwords/passwords/#avoid-fingerprint-or-face-unlock-biometrics).

4. **Delete unnecessary files** including old documents, pictures, screenshots, and chat history. [Back up](https://securityinabox.org/en/files/backup/) important data before removal.

5. **Restart your device frequently** to ensure updates are applied and reduce risks from non-persistent malware.

### 2FA Hardware Token Recommendations
- YubiKey
- SoloKeys
- Nitrokey

### 2FA TOTP App Recommendations
- Aegis Authenticator (Android)
- Raivo OTP (iOS)
- KeePassXC (Desktop)

### Further Reading
- [Creating Strong Passwords](https://ssd.eff.org/module/creating-strong-passwords) - EFF
- [Threat Modeling](https://www.privacyguides.org/en/basics/threat-modeling/) - Privacy Guides
- [Security Planner](https://securityplanner.consumerreports.org/recommendations) - Consumer Reports
- [Digital Security Guidance](https://openbriefing.gitbook.io/defenders-protocol/digital) - Open Briefing
- [Your Security Plan](https://ssd.eff.org/module/your-security-plan) - EFF

---

## Android

1. **Verify your Android is up to date** and that both your [Android version](https://endoflife.date/android) and device are still supported. Check manufacturer support pages: [Samsung](https://security.samsungmobile.com/workScope.smsb) | [Google Pixel](https://support.google.com/pixelphone/answer/4457705) | [Nokia](https://www.hmd.com/en_int/security-updates) | [Motorola](https://en-us.support.motorola.com/app/software-security-update) | [Other manufacturers](https://www.androidauthority.com/phone-update-policies-1658633/)

2. **Enable automatic app updates** via [Google Play](https://support.google.com/googleplay/answer/113412).

3. **Enable [Play Protect](https://support.google.com/googleplay/answer/2812853)** for malware scanning.

4. **[Review app permissions](https://support.google.com/android/answer/9431959)** and revoke unnecessary access.

5. **[Review installed apps](https://securityinabox.org/en/phones-and-computers/android/#remove-apps-that-you-do-not-need-and-do-not-use)** and uninstall unneeded or unknown applications.

6. **Restrict app installations** to [trusted sources](https://securityinabox.org/en/phones-and-computers/android/#use-apps-from-trusted-sources) only.

7. **Set a strong password** (not a PIN or pattern) to [protect device access](https://support.google.com/android/answer/9079129).

8. **Consider [Google's Advanced Protection program](https://support.google.com/android/answer/16339980)** for enhanced security.

**Further reading**: [Protect your Android device](https://securityinabox.org/en/phones-and-computers/android/)

---

## iOS/iPhone

1. **Verify your [iOS version](https://endoflife.date/ios) and [device](https://endoflife.date/iphone) are supported** and [up-to-date](https://support.apple.com/en-gb/guide/iphone/iph3e504502/ios).

2. **Enable [automatic app updates](https://support.apple.com/en-gb/102629)**.

3. **[Review app permissions](https://support.apple.com/en-ie/guide/iphone/iph251e92810/ios)** and revoke unnecessary access.

4. **Review installed apps** and [uninstall unneeded ones](https://support.apple.com/en-gb/guide/iphone/iph248b543ca/ios).

5. **Enable [Lockdown Mode](https://support.apple.com/en-us/105120)** for enhanced protection against sophisticated attacks.

6. **Set a long [passcode](https://support.apple.com/en-us/119586)** to protect device access.

**Further reading**: [Protect your iOS device](https://securityinabox.org/en/phones-and-computers/ios/)

---

## Windows

1. **Use a [supported Windows version](https://endoflife.date/windows)** with [automatic updates enabled](https://support.microsoft.com/en-au/topic/how-to-change-your-automatic-updates-settings-by-using-windows-security-center-804009cd-7931-fc07-5ada-6b157a854201).

2. **Enable [automatic updates for Microsoft Store apps](https://support.microsoft.com/en-us/windows/turn-on-automatic-app-updates-70634d32-4657-dc76-632b-66048978e51b)**.

3. **[Enable Windows Defender](https://support.microsoft.com/en-us/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963)** rather than third-party antivirus software.

4. **Consider [Hardentools](https://github.com/securitywithoutborders/hardentools#readme)** to disable commonly abused Windows features.

5. **Consider [Simplewall](https://github.com/henrypp/simplewall)** to monitor network connections.

6. **Enable [BitLocker or Device Encryption](https://support.microsoft.com/en-us/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)**.

7. **Set a [strong login password](https://support.microsoft.com/en-us/windows/change-or-reset-your-windows-password-8271d17c-9f9e-443f-835a-8318c8f68b9c)**.

8. **[Review installed programs](https://support.microsoft.com/en-us/windows/how-to-check-if-an-app-or-program-is-installed-in-windows-10-5af73cea-f875-dfa0-4cd1-72a06aa06436)** and [remove unneeded ones](https://securityinabox.org/en/phones-and-computers/windows/#remove-apps-that-you-do-not-need-and-do-not-use).

**Further reading**: [Protect your Windows computer](https://securityinabox.org/en/phones-and-computers/windows/) | [Manage updates in Windows](https://support.microsoft.com/en-us/windows/manage-updates-in-windows-643e9ea7-3cf6-7da6-a25c-95d4f7f099fe)

---

## macOS

1. **Use a [supported macOS version](https://endoflife.date/macos)** with [automatic updates enabled](https://support.apple.com/guide/mac-help/keep-your-mac-up-to-date-mchlpx1065/mac).

2. **Consider [LuLu](https://objective-see.org/products/lulu.html)** to monitor network connections.

3. **[Enable FileVault](https://support.apple.com/en-vn/guide/mac-help/mh11785/mac)** for disk encryption.

4. **Set a [strong login password](https://support.apple.com/en-vn/guide/mac-help/mchlp1550/14.0/mac/14.0)**.

5. **Review installed programs** and [uninstall unneeded ones](https://securityinabox.org/en/phones-and-computers/mac/#remove-apps-that-you-do-not-need-and-do-not-use).

**Further reading**: [Protect your Mac computer](https://securityinabox.org/en/phones-and-computers/mac/) | [Background updates in macOS](https://support.apple.com/en-us/101591) | [Set up your Mac to be secure](https://support.apple.com/en-ie/guide/mac-help/flvlt003/mac)

---

## Ubuntu Linux

1. **Use a [supported Ubuntu version](https://endoflife.date/ubuntu)** and keep [software up-to-date](https://wiki.ubuntu.com/SoftwareUpdates).

2. **Enable the [Firewall](https://help.ubuntu.com/community/Gufw)** or use [OpenSnitch](https://github.com/evilsocket/opensnitch/wiki/Installation) to monitor network connections.

3. **[Enable LUKS encryption](https://www.tecmint.com/encrypt-ubuntu-24-04-installation/)** during installation.

4. **Disable automatic login** and set a [strong account password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html).

**Further reading**: [Protect your Linux Device](https://securityinabox.org/en/phones-and-computers/linux/)