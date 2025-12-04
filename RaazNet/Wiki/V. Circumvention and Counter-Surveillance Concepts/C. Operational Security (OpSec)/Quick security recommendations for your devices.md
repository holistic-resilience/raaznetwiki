---
title: "Quick Security Recommendations for Your Devices"
tags: [security, privacy, device-hardening, passwords, two-factor-authentication, encryption]
category: "Device Security"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Digital Security", "Device Protection", "Privacy"]
summary: "Essential first steps for securing Android, iOS, Windows, macOS, and Linux devices with practical, actionable recommendations."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Access to device settings"]
estimated_read_time: "8 minutes"
---

# Quick Security Recommendations for Your Devices

People often ask us where they can start, what are minimum steps they should consider taking in an effort to better protect their devices. In this post we share what we are recommending as the first, often most effective and most important items.

## General Recommendations

1. Use [unique and strong passwords](https://securityinabox.org/en/passwords/passwords) for each account, using a [password manager](https://securityinabox.org/en/passwords/password-managers/) to safely store them.

2. Use [two-factor authentication (2FA)](https://securityinabox.org/en/passwords/2fa) on [supported accounts](https://2fa.directory/). As a first choice, consider using hardware security keys. Otherwise, use apps that generate time-based one-time passwords (TOTP). Avoid using SMS for 2FA if you can.

3. Avoid using biometrics (face ID, fingerprint scan) as an authentication method. [We explain why in the guide on passwords](https://securityinabox.org/en/passwords/passwords/#avoid-fingerprint-or-face-unlock-biometrics).

4. Delete old files, documents, pictures, screenshots and chat history that you do not need on your device. Securely [back up](https://securityinabox.org/en/files/backup/) as necessary before removal.

5. Restart your device frequently. This ensures updates are applied properly and reduces the risk for cases of non-persistent malware.

### Further Reading

- [Creating Strong Passwords](https://ssd.eff.org/module/creating-strong-passwords)
- [Privacy Guides - Threat modeling article](https://www.privacyguides.org/en/basics/threat-modeling/)
- [Security Planner recommendations](https://securityplanner.consumerreports.org/recommendations)
- [Open Briefing - Digital security guidance](https://openbriefing.gitbook.io/defenders-protocol/digital)
- [Surveillance Self-defense - Security plan](https://ssd.eff.org/module/your-security-plan)

---

## Android

1. Check that your [Android is up to date](https://support.google.com/android/answer/7680439) and that both your [version of Android](https://endoflife.date/android) and your device are still supported (check [Samsung](https://security.samsungmobile.com/workScope.smsb), [Google Pixel](https://support.google.com/pixelphone/answer/4457705), [Nokia](https://www.hmd.com/en_int/security-updates) or [Motorola](https://en-us.support.motorola.com/app/software-security-update). For other models, see [Android Authority's phone update policies article](https://www.androidauthority.com/phone-update-policies-1658633/)).

2. Automatically [update your apps](https://support.google.com/googleplay/answer/113412).

3. Enable [Play Protect](https://support.google.com/googleplay/answer/2812853).

4. [Review the permissions](https://support.google.com/android/answer/9431959) your apps have access to.

5. Review [installed apps](https://securityinabox.org/en/phones-and-computers/android/#remove-apps-that-you-do-not-need-and-do-not-use) and uninstall any unneeded or unknown ones.

6. Ensure apps can only be installed from [trusted sources](https://securityinabox.org/en/phones-and-computers/android/#use-apps-from-trusted-sources).

7. Set a longer password (not a PIN or a pattern) to [protect access to your device](https://support.google.com/android/answer/9079129#zippy=%2Cstandard-locks).

8. Consider enrolling in [Google's Advanced Protection program](https://support.google.com/android/answer/16339980).

**Further reading:** [Protect your Android device](https://securityinabox.org/en/phones-and-computers/android/)

---

## iOS/iPhone

1. Check that your [iOS version](https://endoflife.date/ios) and [device](https://endoflife.date/iphone) are still supported and [up-to-date](https://support.apple.com/en-gb/guide/iphone/iph3e504502/ios).

2. Automatically [update your apps](https://support.apple.com/en-gb/102629).

3. Review the [permissions your apps have access to](https://support.apple.com/en-ie/guide/iphone/iph251e92810/ios).

4. Review installed apps and [uninstall any unneeded ones](https://support.apple.com/en-gb/guide/iphone/iph248b543ca/ios).

5. Switch on [Lockdown Mode](https://support.apple.com/en-us/105120), which makes it harder to compromise your device.

6. Set a long [passcode](https://support.apple.com/en-us/119586) to protect access to your device.

**Further reading:** [Protect your iOS device](https://securityinabox.org/en/phones-and-computers/ios/)

---

## Windows

1. Ensure you are using a [supported version of Windows](https://endoflife.date/windows) with [automatic updates enabled](https://support.microsoft.com/en-au/topic/how-to-change-your-automatic-updates-settings-by-using-windows-security-center-804009cd-7931-fc07-5ada-6b157a854201).

2. Make sure that any software installed via the [Microsoft Store is set to automatically update](https://support.microsoft.com/en-us/windows/turn-on-automatic-app-updates-70634d32-4657-dc76-632b-66048978e51b).

3. Ensure [Windows Defender is turned on](https://support.microsoft.com/en-us/windows/stay-protected-with-windows-security-2ae0363d-0ada-c064-8b56-6a39afb6a963). Use Microsoft Defender rather than third-party antivirus.

4. Consider using [Hardentools](https://github.com/securitywithoutborders/hardentools#readme) to disable often-abused features.

5. Consider using [Simplewall](https://github.com/henrypp/simplewall) to monitor where your computer is connecting to.

6. Ensure [BitLocker or Device Encryption is turned on](https://support.microsoft.com/en-us/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838).

7. Ensure your computer [requires a strong password](https://support.microsoft.com/en-us/windows/change-or-reset-your-windows-password-8271d17c-9f9e-443f-835a-8318c8f68b9c) to log in.

8. [Review installed programs](https://support.microsoft.com/en-us/windows/how-to-check-if-an-app-or-program-is-installed-in-windows-10-5af73cea-f875-dfa0-4cd1-72a02aa06436) and [remove any that are no longer needed](https://securityinabox.org/en/phones-and-computers/windows/#remove-apps-that-you-do-not-need-and-do-not-use).

**Further reading:** [Protect your Windows computer](https://securityinabox.org/en/phones-and-computers/windows/) | [Manage updates in Windows](https://support.microsoft.com/en-us/windows/manage-updates-in-windows-643e9ea7-3cf6-7da6-a25c-95d4f7f099fe)

---

## macOS

1. Ensure macOS [automatic updates are enabled](https://support.apple.com/guide/mac-help/keep-your-mac-up-to-date-mchlpx1065/mac#aria-mchlpa64b4a7) and that you use a [supported version of macOS](https://endoflife.date/macos).

2. Consider using [LuLu](https://objective-see.org/products/lulu.html) to monitor where your computer is connecting to.

3. Make sure [FileVault is enabled](https://support.apple.com/en-vn/guide/mac-help/mh11785/mac).

4. Ensure your computer [requires a strong password](https://support.apple.com/en-vn/guide/mac-help/mchlp1550/14.0/mac/14.0) to log in.

5. Review installed programs and [uninstall any that are not needed](https://securityinabox.org/en/phones-and-computers/mac/#remove-apps-that-you-do-not-need-and-do-not-use).

**Further reading:** [Protect your Mac computer](https://securityinabox.org/en/phones-and-computers/mac/) | [About background updates in macOS](https://support.apple.com/en-us/101591) | [Set up your Mac to be secure](https://support.apple.com/en-ie/guide/mac-help/flvlt003/mac)

---

## Ubuntu Linux

1. Ensure that your version of Ubuntu is [still supported](https://endoflife.date/ubuntu) and that you are keeping it and the [installed software up-to-date](https://wiki.ubuntu.com/SoftwareUpdates).

2. Enable the [Firewall](https://help.ubuntu.com/community/Gufw) or consider using [OpenSnitch](https://github.com/evilsocket/opensnitch/wiki/Installation) to monitor where your computer is connecting to.

3. Ensure [LUKS encryption is enabled](https://www.tecmint.com/encrypt-ubuntu-24-04-installation/) when you install the operating system.

4. Ensure automatic login is disabled and [your account is set up with a strong password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html).

**Further reading:** [Protect your Linux Device](https://securityinabox.org/en/phones-and-computers/linux/)