```yaml
---
title: "Protect Your iOS Device"
tags: [ios-security, mobile-security, privacy, iphone, ipad, device-hardening]
category: "Mobile Device Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["iOS Security", "Mobile Privacy", "Device Hardening", "Digital Self-Defense"]
summary: "Comprehensive guide to securing iPhones and iPads through system settings, app management, and privacy controls."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic iOS device familiarity", "Access to device Settings app"]
estimated_read_time: "20 minutes"
---
```

# Protect Your iOS Device

If you use an iPhone or iPad, you may have heard the myth that they are more secure than other devices. This is not necessarily true. Security depends on a combination of how we use our devices and their software, which can be found to have vulnerabilities at any time. Follow the steps in this guide to make your device more secure, and get in the habit of checking these settings regularly to ensure nothing has changed.

---

## Table of Contents

- [Keep Your Operating System Updated](#keep-your-operating-system-updated)
- [Enable Lockdown Mode](#enable-lockdown-mode)
- [Manage Your Apps Securely](#manage-your-apps-securely)
- [Control App Permissions](#control-app-permissions)
- [Secure Your Accounts](#secure-your-accounts)
- [Lock Screen Security](#lock-screen-security)
- [Disable Voice Controls](#disable-voice-controls)
- [Manage Connectivity](#manage-connectivity)
- [Physical Security Measures](#physical-security-measures)
- [Advanced: Basic Forensics](#advanced-basic-forensics)
- [Additional Resources](#additional-resources)

---

## Keep Your Operating System Updated

**Why this matters:** New vulnerabilities in device software are discovered daily. Developers regularly release updates that fix these security holes. Running outdated software leaves you exposed to known attacks.

### How to Update

1. Update from a trusted location and internet connection (home or office, not public wifi)
2. Set aside time for updates—they may require multiple downloads and restarts
3. After updating, check again for additional updates until none remain
4. Always restart your device when prompted after downloading updates

### Important Considerations

- **Backup first:** Apple recommends backing up before updates. For better security, [back up to your own computer](https://support.apple.com/en-us/108796) rather than iCloud
- **Unsupported devices:** If your device no longer receives iOS updates, consider replacing it with a newer model

---

## Enable Lockdown Mode

**We strongly recommend enabling [Lockdown Mode](https://support.apple.com/en-us/105120) on all iOS devices.** Most users will notice little to no difference in daily use, but gain significantly improved protection.

### Why Enable It

Lockdown Mode reduces the attack surface for sophisticated spyware like [Pegasus](https://securityinabox.org/en/blog/pegasus-project-questions-and-answers/). The protections it provides should really be standard for everyone.

**How to enable:** Follow [Apple's Lockdown Mode guide](https://support.apple.com/en-gb/guide/iphone/iph049680987/ios)

---

## Manage Your Apps Securely

### Install Apps Safely

- **Do not jailbreak your device**—it significantly increases your risk from malicious code
- **Only install apps from the [App Store](https://support.apple.com/en-us/102590)**
- If needed apps aren't available in your country, consider [changing your Apple Account region](https://support.apple.com/en-us/118283) (you may need a [VPN](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service))

### Remove Unnecessary Apps

Uninstall apps you don't use. Each installed app is a potential vulnerability, and unused apps may still transmit your data.

**How to remove apps:** [Delete apps from iPhone](https://support.apple.com/en-gb/guide/iphone/iph248b543ca/ios)

### Choose Privacy-Friendly Alternatives

- **Web browser:** Use [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox) instead of Safari
- **General apps:** Consider [free and open source alternatives](https://github.com/dkhamsing/open-source-ios-apps)
- **Social media:** Access through your browser rather than dedicated apps—apps collect significantly more data (phone ID, phone number, wifi connections)

---

## Control App Permissions

Review and restrict app permissions regularly. Apps with access to sensitive features can leak information or be exploited by attackers.

### High-Risk Permissions to Review

- Location Services
- Camera and Microphone
- Contacts and Calendars
- Photos
- Bluetooth
- Local Network
- Files and Folders
- Motion & Fitness
- Speech Recognition

### How to Review Permissions

- [Privacy and location services guide](https://support.apple.com/en-us/102515)
- [Control access to information in apps](https://support.apple.com/guide/iphone/control-access-to-information-in-apps-iph251e92810/ios)
- [Security Planner: Review iPhone app permissions](https://securityplanner.consumerreports.org/tool/review-iphone-app-permissions)

### Location Data

- Turn off location services when not needed (both device-wide and per-app)
- Regularly clear your location history if you keep it enabled

---

## Secure Your Accounts

### Apple ID Security

1. [Review Apple's security checklist](https://support.apple.com/en-us/102614)
2. Set a [strong, unique password](https://securityinabox.org/en/passwords/passwords)
3. [Enable two-factor authentication](https://support.apple.com/en-us/102660)
4. Never share your Apple ID with anyone
5. [Review devices connected to your account](https://support.apple.com/en-us/102649)—screenshot any suspicious devices
6. Enable [Advanced Data Protection for iCloud](https://support.apple.com/en-us/108756) for end-to-end encryption

**If compromised:** Follow [Apple's recovery steps](https://support.apple.com/en-us/102560)

### Review Shared Access

Use Apple's Safety Check feature to audit who has access to your device and data:

- **iOS 15 or earlier:** Use [this checklist](https://support.apple.com/guide/personal-safety/see-who-has-access-to-your-iphone-or-ipad-ipsb8deced49/web)
- **iOS 16 or later:** Use [Safety Check](https://support.apple.com/guide/personal-safety/additional-considerations-safety-check-ipsce4cb8352/web)
- Review [built-in privacy protections](https://support.apple.com/guide/iphone/use-built-in-privacy-and-security-protections-iph6e7d349d1/ios)

---

## Lock Screen Security

### Set a Strong Passcode

- Use a **passphrase of at least 10 characters**, not a short PIN
- Set your screen to lock after **5 minutes or less** of inactivity
- **Avoid biometric unlocks** (fingerprint, face, voice)—these can be forced from you; a passphrase cannot

**How to set up:** [Apple's passcode guide](https://support.apple.com/en-us/119586)

### Why Avoid Biometrics

If arrested, detained, or searched, you can be physically forced to unlock with your face or fingerprint. Attackers can also:
- Duplicate fingerprints from surfaces you've touched
- Use photos or 3D models to bypass face unlock
- Crack short PINs with software

A long passphrase remains the most secure option.

### Control Lock Screen Information

1. Set notification previews to **"When Unlocked"** or **"Never"** in [notification settings](https://support.apple.com/guide/iphone/change-notification-settings-iph7c3d96bab/ios)
2. Go to **Settings > Face ID & Passcode** (or Touch ID & Passcode)
3. Under "Allow Access When Locked," disable:
   - Notification Center
   - Control Center
   - Accessories ([more info](https://support.apple.com/en-us/111806))
   - Any other features you don't need accessible while locked

---

## Disable Voice Controls

Voice-controlled devices can be exploited to capture audio without your knowledge.

### Turn Off Voice Features

1. [Disable classic voice control](https://support.apple.com/en-us/119836)
2. [Turn off Siri](https://support.apple.com/en-il/guide/iphone/iphc28624b81abc/ios), including "Allow Siri When Locked"
3. Disable Dictation: **Settings > General > Keyboard > Enable Dictation (off)**

Disabling both Siri and Dictation will delete Siri data associated with your account. Learn more: [Ask Siri, Dictation & Privacy](https://www.apple.com/legal/privacy/data/en/ask-siri-dictation)

**Note:** If you have a disability requiring voice control, see [Security Planner's guide to safer voice assistant use](https://securityplanner.consumerreports.org/tool/secure-your-smart-speaker).

---

## Manage Connectivity

### Turn Off Unused Connections

Keep wifi, Bluetooth, and Personal Hotspot disabled when not in use. **Important:** Use the Settings app, not Control Center—Control Center only disconnects from current networks without fully disabling the radios.

**Why this matters:** When enabled, your device broadcasts the names of previously connected networks and devices, creating a unique fingerprint that can identify and track you.

### Clear Saved Networks

- Store network passwords in your [password manager](https://securityinabox.org/en/passwords/tools/#strongbox) instead of your device
- Regularly delete saved networks you no longer use
- Turn off "Auto-Join" for networks
- [How to forget wifi networks](https://support.apple.com/en-us/102480)
- [Reset all network settings](https://support.apple.com/guide/iphone/reset-iphone-settings-iphea1c2fe48/ios)

### Disable AirDrop

[Turn off AirDrop](https://support.apple.com/en-us/119857#setoptions) by selecting "Receiving Off" when not actively sharing files.

### Power Down at Night

Completely powering off your device overnight limits the window for remote attacks.

---

## Physical Security Measures

### Privacy Screen Filter

A privacy filter prevents "shoulder surfing"—when someone views your screen from an angle. Find filters at electronics retailers by searching for your device model plus "privacy screen."

[Security Planner guide on privacy filters](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen)

### Camera Cover

Malware can activate your camera without your knowledge.

- Locate all cameras on your device (smartphones often have multiple)
- **Low-tech solution:** Use a small adhesive bandage—the non-sticky center pad won't leave residue on your lens
- **Commercial option:** Search for your device model plus "webcam privacy cover thin slide"

### Keyboard Security

Third-party keyboards can transmit everything you type to their developers.

**Check your keyboards:** Settings > General > Keyboard > Keyboards

Remove any keyboards you don't recognize or need, and delete associated keyboard apps.

---

## Advanced: Basic Forensics

If you suspect unauthorized access to your device:

### Checks to Perform

- [Review iCloud accounts](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/ios/icloud.md)
- [Check for Mobile Device Management profiles](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/ios/mdm.md)
- [Check for jailbreaks](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/ios/jailbreaks.md)
- [Review devices linked to chat applications](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/smartphones/linkeddevices.md)
- [Monitor network traffic](https://github.com/securitywithoutborders/guide-to-quick-forensics/blob/master/smartphones/network.md)

### If You Suspect Compromise

Follow the Digital First Aid Kit troubleshooter: [My device is acting suspiciously](https://digitalfirstaid.org/topics/device-acting-suspiciously/#ios-intro)

---

## Additional Resources

- [Security in a Box: Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Apple Personal Safety User Guide (PDF)](https://help.apple.com/pdf/personal-safety/en_US/personal-safety-user-guide.pdf)

---

*Last updated: 24 September 2025*