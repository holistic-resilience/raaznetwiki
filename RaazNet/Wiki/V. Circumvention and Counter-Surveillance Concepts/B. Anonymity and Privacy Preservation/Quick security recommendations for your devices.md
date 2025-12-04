---
title: "Quick Security Recommendations for Your Devices"
tags: [security, privacy, device-hardening, passwords, two-factor-authentication, encryption]
category: "Device Security"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Digital Security", "Device Protection", "Privacy Best Practices"]
summary: "Essential first steps for securing Android, iOS, Windows, macOS, and Linux devices with practical, actionable recommendations."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Access to device settings"]
estimated_read_time: "8 minutes"
---

# Quick Security Recommendations for Your Devices

People often ask where to start when protecting their devices. This guide covers the minimum, most effective steps you should consider taking to better protect your devices.

## General Recommendations

These practices apply across all devices and platforms:

1. **Use unique, strong passwords** for each account, storing them in a [password manager](https://securityinabox.org/en/passwords/password-managers/)
2. **Enable two-factor authentication (2FA)** on [supported accounts](https://2fa.directory/):
   - **Best option:** Hardware security keys (see recommendations below)
   - **Alternative:** TOTP apps that generate time-based codes
   - **Avoid:** SMS-based 2FA when possible
3. **Avoid biometric authentication** (Face ID, fingerprint) as your primary method — [learn why](https://securityinabox.org/en/passwords/passwords/#avoid-fingerprint-or-face-unlock-biometrics)
4. **Delete unnecessary files** — old documents, screenshots, and chat history. [Back up](https://securityinabox.org/en/files/backup/) important data before removal
5. **Restart your device frequently** — this applies updates and reduces risk from non-persistent malware

### Recommended 2FA Tools

**Hardware Tokens:**
- [YubiKey](https://www.yubico.com/)
- [Nitrokey](https://www.nitrokey.com/)
- [SoloKeys](https://solokeys.com/)

**TOTP Apps:**
- [Aegis Authenticator](https://getaegis.app/) (Android)
- [Raivo OTP](https://raivo-otp.com/) (iOS)
- [KeePassXC](https://keepassxc.org/) (Desktop)

### Further Reading
- [Creating Strong Passwords](https://ssd.eff.org/module/creating-strong-passwords) — EFF
- [Threat Modeling](https://www.privacyguides.org/en/basics/threat-modeling/) — Privacy Guides
- [Your Security Plan](https://ssd.eff.org/module/your-security-plan) — EFF Surveillance Self-Defense

---

## Android

1. **Verify your Android is up to date** — check that both your [Android version](https://endoflife.date/android) and device are still supported:
   - [Samsung](https://security.samsungmobile.com/workScope.smsb) | [Google Pixel](https://support.google.com/pixelphone/answer/4457705) | [Nokia](https://www.hmd.com/en_int/security-updates) | [Motorola](https://en-us.support.motorola.com/app/software-security-update)
   - See [Android Authority's update policy guide](https://www.androidauthority.com/phone-update-policies-1658633/) for other manufacturers
2. **Enable automatic app updates** via [Google Play settings](https://support.google.com/googleplay/answer/113412)
3. **Enable Play Protect** for [malware scanning](https://support.google.com/googleplay/answer/2812853)
4. **Review app permissions** — [audit what apps can access](https://support.google.com/android/answer/9431959)
5. **Remove unused apps** — [uninstall unknown or unnecessary applications](https://securityinabox.org/en/phones-and-computers/android/#remove-apps-that-you-do-not-need-and-do-not-use)
6. **Restrict app installation sources** — only allow [trusted sources](https://securityinabox.org/en/phones-and-computers/android/#use-apps-from-trusted-sources)
7. **Use a strong password** (not PIN or pattern) to [lock your device](https://support.google.com/android/answer/9079129)
8. **Consider Google's Advanced Protection** — [enroll for enhanced security](https://support.google.com/android/answer/16339980)

**Further reading:** [Protect your Android device](https://securityinabox.org/en/phones-and-computers/android/)

---

## iOS/iPhone

1. **Verify iOS and device support** — check [iOS version](https://endoflife.date/ios) and [device support status](https://endoflife.date/iphone), then [update](https://support.apple.com/en-gb/guide/iphone/iph3e504502/ios)
2. **Enable automatic app updates** in [App Store settings](https://support.apple.com/en-gb/102629)
3. **Review app permissions** — [audit privacy settings](https://support.apple.com/en-ie/guide/iphone/iph251e92810/ios)
4. **Remove unused apps** — [delete unnecessary applications](https://support.apple.com/en-gb/guide/iphone/iph248b543ca/ios)
5. **Enable Lockdown Mode** — [activate for enhanced protection](https://support.apple.com/en-us/105120) against sophisticated attacks
6. **Set a long passcode** — use an [alphanumeric passcode](https://support.apple.com/en-us/119586) rather than a short PIN

**Further reading:** [Protect your iOS device](https://securityinabox.org/en/phones-and-computers/ios/)

---

## Windows

1. **Use a supported Windows version** — verify on [endoflife.date](https://endoflife.date/windows) and [enable automatic updates](https://support.microsoft.com/en-au/topic/how-to-change-your-automatic-updates-settings-by-using-windows-security-center-804009cd-7931-fc07-5ada-6b157a854201)
2. **Enable automatic Microsoft Store updates** in [store settings](https://support.microsoft.com/en-us/windows/turn-on-automatic-app-updates-70634d32-4657-dc76-632b-66048978e51b)
3. **Enable Windows Defender** — use the [built-in security](https://support.microsoft.com/en-us/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963) rather than third-party antivirus
4. **Consider Hardentools** — [disable commonly abused features](https://github.com/securitywithoutborders/hardentools#readme)
5. **Monitor network connections** — use [Simplewall](https://github.com/henrypp/simplewall) to see where your computer connects
6. **Enable BitLocker** — turn on [device encryption](https://support.microsoft.com/en-us/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)
7. **Require a strong login password** — [configure account security](https://support.microsoft.com/en-us/windows/change-or-reset-your-windows-password-8271d17c-9f9e-443f-835a-8318c8f68b9c)
8. **Remove unused programs** — [review and uninstall](https://securityinabox.org/en/phones-and-computers/windows/#remove-apps-that-you-do-not-need-and-do-not-use) unnecessary software

**Further reading:** [Protect your Windows computer](https://securityinabox.org/en/phones-and-computers/windows/)

---

## macOS

1. **Use a supported macOS version** — verify on [endoflife.date](https://endoflife.date/macos) and [enable automatic updates](https://support.apple.com/guide/mac-help/keep-your-mac-up-to-date-mchlpx1065/mac)
2. **Monitor network connections** — use [LuLu](https://objective-see.org/products/lulu.html) to see outgoing connections
3. **Enable FileVault** — turn on [disk encryption](https://support.apple.com/en-vn/guide/mac-help/mh11785/mac)
4. **Require a strong login password** — [configure account security](https://support.apple.com/en-vn/guide/mac-help/mchlp1550/14.0/mac/14.0)
5. **Remove unused applications** — [uninstall unnecessary programs](https://securityinabox.org/en/phones-and-computers/mac/#remove-apps-that-you-do-not-need-and-do-not-use)

**Further reading:** [Protect your Mac computer](https://securityinabox.org/en/phones-and-computers/mac/) | [Set up your Mac to be secure](https://support.apple.com/en-ie/guide/mac-help/flvlt003/mac)

---

## Ubuntu Linux

1. **Use a supported Ubuntu version** — verify on [endoflife.date](https://endoflife.date/ubuntu) and [keep software updated](https://wiki.ubuntu.com/SoftwareUpdates)
2. **Enable firewall protection** — use [Gufw](https://help.ubuntu.com/community/Gufw) or [OpenSnitch](https://github.com/evilsocket/opensnitch/wiki/Installation) for connection monitoring
3. **Enable LUKS encryption** — [encrypt your disk during installation](https://www.tecmint.com/encrypt-ubuntu-24-04-installation/)
4. **Disable automatic login** — require a [strong password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html) for account access

**Further reading:** [Protect your Linux Device](https://securityinabox.org/en/phones-and-computers/linux/)