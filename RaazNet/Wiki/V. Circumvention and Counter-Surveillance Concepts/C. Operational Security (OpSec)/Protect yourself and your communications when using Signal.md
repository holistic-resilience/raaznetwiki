```yaml
---
title: "Protect Yourself and Your Communications When Using Signal"
tags: [signal, encryption, messaging, privacy, digital-security, mobile-security]
category: "Secure Communication"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, General Public]
topics: ["End-to-End Encryption", "Secure Messaging", "Account Security", "Privacy Protection"]
summary: "Comprehensive guide to securing your Signal messenger account, protecting communications, and using advanced privacy features effectively."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic smartphone usage", "Signal app installed", "Understanding of basic privacy concepts"]
estimated_read_time: "15 minutes"
---
```

# Protect Yourself and Your Communications When Using Signal

**Signal** is a free and open-source messaging app that protects your communications using end-to-end encryption. Developed by [the Signal Foundation](https://signalfoundation.org/), it's available for all major operating systems, though accounts can only be created via smartphone installation.

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
- [Alternative: Molly Client](#alternative-molly-client)
- [Resources](#resources)

---

## Pros and Cons of Using Signal

### Advantages

- **Open-source**: [Code is publicly available](https://github.com/signalapp) for independent security review
- **Strong encryption**: Protects 1:1 and group messages, voice, and video calls using [well-documented end-to-end encryption](https://github.com/signalapp/libsignal)
- **Identity verification**: Allows you to [verify contact identities](#verify-your-contacts-identities)
- **Forward secrecy**: Past conversations remain safe even if encryption keys are compromised
- **Asynchronous delivery**: Messages sent while offline are delivered when you reconnect

### Limitations

- Only encrypts messages between Signal users
- Doesn't hide that you're using encrypted communications
- Requires a phone number for registration (SMS or call from US number)
- Uses Google Firebase and Apple Push Notification services for notifications (though notifications contain no sensitive data—they simply wake the app)
- May attract attention or violate laws in some jurisdictions—check [Global Partners Digital's encryption laws map](https://www.gp-digital.org/world-map-of-encryption)
- [Blocked in certain countries](https://en.wikipedia.org/wiki/Signal_(software)#Blocking)—use a [proxy](#use-a-proxy-if-signal-is-blocked) to bypass restrictions

---

## Before You Start

1. **Create a communication plan** based on [protecting online communication privacy](https://securityinabox.org/en/assess-plan/private-communication/)
2. **Secure your device first**—review recommendations for [Android](https://securityinabox.org/en/phones-and-computers/android) or [iOS](https://securityinabox.org/en/phones-and-computers/ios)

---

## Installation and Setup

### Install Signal

Follow [Signal's official installation instructions](https://support.signal.org/hc/en-us/articles/360008216551-Installing-Signal) for your mobile device. After phone installation, you can link desktop or iPad apps.

### Use a Proxy if Signal is Blocked

If Signal is blocked in your country:

- [Find a proxy address](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#proxy_find)
- [Configure proxy on Android](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61MK3AQHE51VWFYGTC)
- [Configure proxy on iOS](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61PANY8JE6N8XXWQKM)
- Consider [running a proxy server](https://github.com/signalapp/Signal-TLS-Proxy) to help others

### Create Your Account

See [Signal's phone registration guide](https://support.signal.org/hc/en-us/articles/360007318691-Register-a-phone-number).

**Consider using an alternative phone number** if you want to separate your messaging identity from your official identity. Learn [how to get a different phone number](https://securityinabox.org/en/assess-plan/multiple-identities/#get-a-different-phone-number), then [keep it private](#keep-your-phone-number-private).

---

## Protect Your Account

### Set a Registration Lock PIN

1. Go to **Settings > Account**
2. Enable **Registration Lock**
3. Select a PIN and store it in a password manager

> **Why**: Prevents others from registering a Signal account with your phone number, even if they gain access to it.

Learn more in [Signal's PIN support page](https://support.signal.org/hc/en-us/articles/360007059792-Signal-PIN).

---

## Use Signal More Safely

### Keep Your Phone Number Private

1. Go to **Settings > Privacy > Phone Number > Who can see my number**
2. Select **Nobody**

Learn more about [Signal's phone number privacy](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive).

> **Why**: Phone numbers are often tied to official identity. Keeping yours private protects against unwanted identification.

### Connect Without Sharing Your Number

1. **Create a username**: Must be unique with at least 2 digits appended
2. Go to **Settings > Privacy > Phone Number > Who can find me by number**
3. Select **Nobody**

This ensures only people with your username can find you on Signal.

### Back Up Your Messages

Signal doesn't back up chats by default. Backups are stored encrypted on your device only.

- [Learn to back up and restore conversations](https://support.signal.org/hc/en-us/articles/360007059752-Backup-and-Restore-Messages)

### Link Devices Carefully

- [How to link Signal Desktop or iPad](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices)
- **Minimize linked devices** to reduce attack surface
- **Never link to shared or public devices**

### iOS-Specific Settings

Disable these integrations to keep Signal activities private:

1. **Settings > Chats** → Disable **Share Contacts with iOS**
2. **Settings > Privacy > Calling > Show Calls in Recents** → Disable

### Android-Specific Settings

Enable **Incognito Keyboard**:

1. Go to **Settings > Privacy**
2. Enable **Incognito Keyboard**

Learn more in [Signal's Incognito Keyboard guide](https://support.signal.org/hc/en-us/articles/360055276112-Incognito-Keyboard).

---

## Secure Your Communications

### Verify Contact Identities

Verify safety numbers to confirm you're communicating with the right person:

- [View a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#view)
- [Verify a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#verify)

After verification, tap **Mark as Verified**. Signal will alert you if a contact's safety number changes, helping detect impersonation attempts.

### Use Disappearing Messages

- Enable automatic deletion for sensitive conversations
- [Delete messages manually](https://support.signal.org/hc/en-us/articles/360007320491-Delete-messages-alerts-or-chats) if not using auto-deletion

> **Why**: Limits information stored on devices if they're compromised.

### Enable Screen Security

Go to **Settings > Privacy**:
- **Android**: Enable **Screen Security**
- **iOS**: Enable **Hide Screen in App Switcher**

> **Why**: Blocks screenshots and prevents message previews in app switcher.

For notification previews, see device-specific guides for [Android](https://securityinabox.org/en/phones-and-computers/android/#control-what-can-be-seen-when-your-device-is-locked), [iOS](https://securityinabox.org/en/phones-and-computers/ios/#control-what-can-be-seen-when-your-device-is-locked), [Mac](https://securityinabox.org/en/phones-and-computers/mac/#control-what-can-be-seen-when-your-device-is-locked), [Linux](https://securityinabox.org/en/phones-and-computers/linux/#control-what-can-be-seen-when-your-device-is-locked), or [Windows](https://securityinabox.org/en/phones-and-computers/windows/#control-what-can-be-seen-when-your-device-is-locked).

### Protect Your IP Address on Calls

Go to **Settings > Privacy > Advanced** and enable **Always relay calls**.

> **Why**: Routes calls through Signal servers to hide your IP address. Note: All group calls already use this protection, and calls remain end-to-end encrypted regardless.

### Disable Link Previews

Go to **Settings > Chats** and disable **Generate link previews**.

> **Why**: Prevents linked websites from obtaining information about you. Both you and your contacts need this disabled for full protection.

---

## Protect Your Groups

Signal supports groups up to 1,000 members and group calls with up to 50 participants.

- [Start a group chat](https://support.signal.org/hc/en-us/articles/360007319331-Group-chats)
- [Group voice and video calls](https://support.signal.org/hc/en-us/articles/360052977792-Group-Calling-Voice-or-Video)

### Invite Only Trusted People

- Enable **Approve new members** (Android) or **Require admin approval** (iOS) when creating groups
- [Add members to group chats](https://support.signal.org/hc/en-us/articles/360050427692-Manage-a-group#add)
- Consider restricting member additions to admins only
- Avoid sharing invite links publicly

### Manage Admins Wisely

- **Designate trusted admins**: Tap member name → **Make admin**
- Multiple admins ensure continuity if one becomes unavailable
- Reduces moderation burden on any single person

### Configure Permissions

In the **Permissions** section, restrict to admins only:
- Adding members
- Editing group info
- Sending messages (for announcement-only groups)

### Moderate Effectively

- For update-focused groups, allow only admins to send messages
- Remove members who violate community standards: Tap name → **Remove from group**
- Enable disappearing messages for sensitive groups

---

## Check for Suspicious Access

### Review Linked Devices

- [View linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01JPNF3R6PAJQSQEFGVMMZ75TA)
- [Unlink unrecognized devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01K0YRHGSACMHVM8JYNSPNX157)

> **Why**: Adversaries who gain account access may appear as linked devices.

### If Your Device is Lost or Stolen

Follow [Signal's guide for lost or stolen phones](https://support.signal.org/hc/en-us/articles/360007062452-What-do-I-do-if-my-phone-is-lost-or-stolen).

---

## Alternative: Molly Client

[Molly](https://molly.im/) (or Molly-FOSS) is an Android alternative offering additional features:

- **Passphrase encryption** for stored messages
- **Multiple mobile devices** with same account
- **Customizable backup** frequency and retention
- **Google-independent notifications** (Molly-FOSS only)

Molly is a secure, free, open-source client with all Signal features plus security improvements.

- [Full feature list](https://github.com/mollyim/mollyim-android?tab=readme-ov-file#features)
- [Techlore video on Molly](https://www.youtube.com/watch?v=P-2z2c3XBkQ)

---

## Resources

- [EFF Surveillance Self-Defense: How to Use Signal](https://ssd.eff.org/module/how-to-use-signal) — *Updated March 26, 2025*
- [Techlore: Lock Down Signal Messenger](https://www.youtube.com/watch?v=DPjg3651oJM) — *Published August 9, 2024*
- [Signal Official Support](https://support.signal.org/)
- [Security in a Box: Secure Chat Guide](https://securityinabox.org/en/communication/secure-chat)