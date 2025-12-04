```yaml
---
title: "Protect Yourself and Your Communications When Using Signal"
tags: [signal, encrypted-messaging, privacy, digital-security, mobile-security, communication]
category: "Secure Communication"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, General Public]
topics: ["End-to-End Encryption", "Messaging Security", "Account Protection", "Privacy Settings"]
summary: "Comprehensive guide to securing your Signal messenger account, protecting communications, and using advanced privacy features effectively."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic smartphone literacy", "Signal app installed or ready to install"]
estimated_read_time: "15 minutes"
---
```

# Protect Yourself and Your Communications When Using Signal

**Signal** is a free and open-source messaging app that protects your communications using end-to-end encryption. Developed by [the Signal Foundation](https://signalfoundation.org/), it's available for all major operating systems, though account creation requires a smartphone.

This guide covers how to use Signal more safely and secure your account. For broader context, see the companion guide on [using messaging apps more securely](https://securityinabox.org/en/communication/secure-chat).

---

## Table of Contents

- [Pros and Cons of Using Signal](#pros-and-cons-of-using-signal)
- [Before You Start](#before-you-start)
- [Installation and Setup](#installation-and-setup)
- [Protect Your Account](#protect-your-account)
- [Use Signal More Safely](#use-signal-more-safely)
- [Secure Your Communications](#secure-your-communications)
- [Protect Your Groups](#protect-your-groups)
- [Check for Suspicious Access](#check-for-suspicious-access)
- [Consider Molly as an Alternative Client](#consider-molly-as-an-alternative-client)
- [Resources](#resources)

---

## Pros and Cons of Using Signal

### Advantages

- **Open source**: [Code is publicly available](https://github.com/signalapp) for independent security review
- **Strong encryption**: Protects messages, voice, and video calls with [well-documented end-to-end encryption](https://github.com/signalapp/libsignal)
- **Identity verification**: Allows you to [verify contacts' identities](#verify-your-contacts-identities)
- **Forward secrecy**: Past conversations remain safe even if current encryption keys are compromised
- **Asynchronous delivery**: Messages sent while offline wait for you to reconnect

### Limitations

- **Signal-only encryption**: Only encrypts messages between Signal users
- **Metadata visibility**: Does not hide that you're using encrypted communications
- **Phone number required**: Registration requires SMS or phone call verification from a US number
- **Push notification dependencies**: Relies on Google Firebase (Android) and Apple Push Notification Service (iOS)—though notifications contain no sensitive data and are processed locally
- **Legal considerations**: Encryption tools may attract attention or violate laws in some jurisdictions. Check the [Global Partners Digital encryption laws map](https://www.gp-digital.org/world-map-of-encryption)
- **Regional blocking**: Some countries [block Signal access](https://en.wikipedia.org/wiki/Signal_(software)#Blocking)—see [proxy instructions](#use-a-proxy-if-signal-is-blocked) for workarounds

---

## Before You Start

1. **Create a communication plan** based on recommendations in the guide on [protecting online communication privacy](https://securityinabox.org/en/assess-plan/private-communication/)
2. **Secure your device first**—review security guides for [Android](https://securityinabox.org/en/phones-and-computers/android) or [iOS](https://securityinabox.org/en/phones-and-computers/ios)

---

## Installation and Setup

### Install Signal

Follow [Signal's official installation instructions](https://support.signal.org/hc/en-us/articles/360008216551-Installing-Signal) for your mobile device. After phone installation, you can link desktop or iPad apps.

### Use a Proxy if Signal is Blocked

If Signal is blocked in your country:

- [Find a proxy address](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#proxy_find)
- [Configure proxy on Android](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61MK3AQHE51VWFYGTC)
- [Configure proxy on iOS](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61PANY8JE6N8XXWQKM)
- [Set up your own proxy server](https://github.com/signalapp/Signal-TLS-Proxy) to help others

### Create Your Account

Register following [Signal's phone number registration guide](https://support.signal.org/hc/en-us/articles/360007318691-Register-a-phone-number).

**Consider using an alternative phone number** if you want to keep your official identity separate from your messaging activities. Learn [how to get a different phone number](https://securityinabox.org/en/assess-plan/multiple-identities/#get-a-different-phone-number), then [keep it private in your profile](#keep-your-phone-number-private).

---

## Protect Your Account

### Set a Registration Lock PIN

1. Go to **Settings > Account**
2. Enable **Registration Lock**
3. Select a PIN and store it in a password manager

> **Why this matters**: A registration lock prevents others from registering a Signal account with your phone number, even if they gain access to it.

Learn more in [Signal's PIN documentation](https://support.signal.org/hc/en-us/articles/360007059792-Signal-PIN).

---

## Use Signal More Safely

### Keep Your Phone Number Private

1. Go to **Settings > Privacy > Phone Number > Who can see my number**
2. Select **Nobody**

Learn more about [Signal's phone number privacy](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive).

> **Why this matters**: Phone numbers often link to official identities. Keeping yours private protects against unwanted identification, especially for sensitive activities.

### Connect Without Sharing Your Number

1. **Create a username**: Choose a unique name with at least 2 digits appended
2. Go to **Settings > Privacy > Phone Number > Who can find me by number**
3. Select **Nobody**

This ensures only people with your username can find you on Signal.

### Back Up Your Messages

Signal doesn't back up chats by default. Backups are stored encrypted on your device only.

- [Learn to back up and restore conversations](https://support.signal.org/hc/en-us/articles/360007059752-Backup-and-Restore-Messages)

### Link Devices Carefully

- [Learn how to link Signal Desktop or iPad](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices)
- **Minimize linked devices** to reduce attack surface
- **Never link to shared or public devices**

### iOS-Specific Settings

Disable these to keep Signal activities private:

- **Settings > Chats**: Disable **Share Contacts with iOS**
- **Settings > Privacy > Calling**: Disable **Show Calls in Recents**

> **Why this matters**: These settings prevent Signal contacts and call history from syncing with iCloud.

### Android-Specific Settings

- Go to **Settings > Privacy**
- Enable **Incognito Keyboard**

Learn more about [Incognito Keyboard](https://support.signal.org/hc/en-us/articles/360055276112-Incognito-Keyboard).

---

## Secure Your Communications

### Verify Contacts' Identities

Safety numbers uniquely identify accounts and encryption keys. Verification helps prevent impersonation.

1. [View a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#view)
2. [Verify the safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#verify)
3. Tap **Mark as Verified** once confirmed

> **Why this matters**: If someone impersonates a verified contact, Signal alerts you when the safety number changes.

### Use Disappearing Messages

- Enable for sensitive conversations or set a default timer for all chats
- [Delete specific messages, chats, or all history](https://support.signal.org/hc/en-us/articles/360007320491-Delete-messages-alerts-or-chats) if not using auto-deletion

> **Why this matters**: Limits stored information on your devices, reducing exposure if a device is compromised.

### Enable Screen Security

- **Android**: Settings > Privacy > Screen Security
- **iOS**: Settings > Privacy > Hide Screen in App Switcher

> **Why this matters**: Blocks screenshots and hides Signal previews in the app switcher. For notification privacy, see device-specific guides for [Android](https://securityinabox.org/en/phones-and-computers/android/#control-what-can-be-seen-when-your-device-is-locked), [iOS](https://securityinabox.org/en/phones-and-computers/ios/#control-what-can-be-seen-when-your-device-is-locked), [Mac](https://securityinabox.org/en/phones-and-computers/mac/#control-what-can-be-seen-when-your-device-is-locked), [Linux](https://securityinabox.org/en/phones-and-computers/linux/#control-what-can-be-seen-when-your-device-is-locked), or [Windows](https://securityinabox.org/en/phones-and-computers/windows/#control-what-can-be-seen-when-your-device-is-locked).

### Protect Your IP Address on Calls

- Go to **Settings > Privacy > Advanced**
- Enable **Always relay calls**

> **Why this matters**: Routes calls through Signal's servers instead of direct peer-to-peer connections, hiding your IP address. Note: All calls remain end-to-end encrypted, and group calls always use relays.

### Disable Link Previews

- Go to **Settings > Chats**
- Disable **Generate link previews**

Learn more about [Signal Link Previews](https://support.signal.org/hc/en-us/articles/360022474332-Link-Previews).

> **Why this matters**: Link previews can leak information to linked websites. Both sender and recipient must disable this for full protection.

---

## Protect Your Groups

Signal supports groups up to 1,000 members and group calls with up to 50 participants.

- [Learn about Signal groups](https://support.signal.org/hc/en-us/articles/360007319331-Group-chats)
- [Learn about group calls](https://support.signal.org/hc/en-us/articles/360052977792-Group-Calling-Voice-or-Video)

### Invite Only Trusted Members

- Enable **Approve new members** (Android) or **Require admin approval** (iOS) when creating groups
- Consider restricting member additions to admins only
- [Learn to add members](https://support.signal.org/hc/en-us/articles/360050427692-Manage-a-group#add)

> **Why this matters**: Prevents trolls and potential surveillance by controlling who joins sensitive groups.

### Manage Admins Wisely

- **Appoint trusted admins**: Tap a member's name > **Make admin**
- **Restrict privileges**: In group Permissions, limit who can add members, edit info, or send messages

> **Why this matters**: Multiple admins ensure continuity if one is unavailable, while restricted privileges prevent unauthorized changes.

### Moderate Effectively

- Restrict messaging to admins for announcement-style groups
- Remove members who violate community standards: tap their name > **Remove from group**

### Enable Disappearing Messages for Groups

Set messages to disappear, especially in sensitive groups, to limit stored information.

---

## Check for Suspicious Access

### Review Linked Devices

- [View linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01JPNF3R6PAJQSQEFGVMMZ75TA)
- [Unlink unrecognized devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01K0YRHGSACMHVM8JYNSPNX157)

> **Why this matters**: Attackers who gain account access may appear as linked devices you don't recognize.

### If Your Device is Lost or Stolen

Follow [Signal's guide for lost or stolen phones](https://support.signal.org/hc/en-us/articles/360007062452-What-do-I-do-if-my-phone-is-lost-or-stolen).

---

## Consider Molly as an Alternative Client

[Molly](https://molly.im/) (or Molly-FOSS) is an Android-only alternative Signal client offering additional features:

- **Passphrase encryption** for stored messages
- **Multi-device support** for the same account on multiple phones
- **Flexible backup options** with customizable frequency and retention
- **Google-independent notifications** (Molly-FOSS only)

Learn more:
- [Full feature list on GitHub](https://github.com/mollyim/mollyim-android?tab=readme-ov-file#features)
- [Techlore's Molly overview video](https://www.youtube.com/watch?v=P-2z2c3XBkQ)

---

## Resources

- [EFF Surveillance Self-Defense: How to Use Signal](https://ssd.eff.org/module/how-to-use-signal) — Updated March 26, 2025
- [Techlore: Lock Down Signal Messenger Ultimate Hardening Guide](https://www.youtube.com/watch?v=DPjg3651oJM) — Published August 9, 2024
- [Signal Official Support](https://support.signal.org/)