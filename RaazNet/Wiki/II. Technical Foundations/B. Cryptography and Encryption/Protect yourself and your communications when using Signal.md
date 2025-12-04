---
title: "Protect Yourself and Your Communications When Using Signal"
tags: [signal, encryption, secure-messaging, privacy, digital-security, mobile-security]
category: "Secure Communication"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, General Public]
topics: ["End-to-End Encryption", "Messaging Security", "Account Protection", "Privacy Settings"]
summary: "Comprehensive guide to securing your Signal account and communications, including privacy settings, identity verification, and group protection."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic smartphone usage", "Signal app installed", "Understanding of basic privacy concepts"]
estimated_read_time: "15 minutes"
---

# Protect Yourself and Your Communications When Using Signal

**Last Updated:** 23 September 2025

**Signal** is a free and open-source messaging app that protects your communications using end-to-end encryption. Developed by [the Signal Foundation](https://signalfoundation.org/), it's available for all major operating systems, though account creation requires a smartphone.

This guide covers how to use Signal more safely and secure your account. For broader context, see the companion guide on [using messaging apps more securely](https://securityinabox.org/en/communication/secure-chat).

---

## Table of Contents

- [Pros and Cons of Using Signal](#pros-and-cons-of-using-signal)
- [Before You Start](#before-you-start)
- [Installation and Setup](#installation-and-setup)
- [Account Protection](#account-protection)
- [Privacy Settings](#privacy-settings)
- [Securing Your Communications](#securing-your-communications)
- [Group Protection](#group-protection)
- [Monitoring for Suspicious Access](#monitoring-for-suspicious-access)
- [Alternative: Molly Client](#alternative-molly-client)
- [Resources](#resources)

---

## Pros and Cons of Using Signal

### Advantages

- **Open source** — Code is [publicly available](https://github.com/signalapp) for independent security review
- **Strong encryption** — Protects messages, voice calls, and video calls with [well-documented end-to-end encryption](https://github.com/signalapp/libsignal)
- **Identity verification** — Allows you to verify contacts' identities through safety numbers
- **Forward secrecy** — Past conversations remain protected even if current encryption keys are compromised
- **Asynchronous messaging** — Messages sent while offline are delivered when you reconnect

### Limitations

- **Signal-to-Signal only** — Encryption only works between Signal users
- **Metadata visibility** — Signal doesn't hide that you're using encrypted communications
- **Phone number required** — Registration requires receiving SMS or a call from a US number
- **Push notification services** — Relies on Google Firebase (Android) and Apple Push Notification Service (iOS), though notifications contain no sensitive content
- **Legal considerations** — Encryption tools may be illegal or attract attention in some jurisdictions. Check the [Global Partners Digital encryption laws map](https://www.gp-digital.org/world-map-of-encryption)
- **Blocked in some countries** — [Certain countries block Signal](https://en.wikipedia.org/wiki/Signal_(software)#Blocking); use a proxy to circumvent

---

## Before You Start

1. **Create a communication plan** based on recommendations in the guide on [protecting online communication privacy](https://securityinabox.org/en/assess-plan/private-communication/)
2. **Secure your device** — Review security recommendations for [Android](https://securityinabox.org/en/phones-and-computers/android) or [iOS](https://securityinabox.org/en/phones-and-computers/ios)

---

## Installation and Setup

### Install Signal

Follow [Signal's installation instructions](https://support.signal.org/hc/en-us/articles/360008216551-Installing-Signal) for your mobile device. After phone installation, you can link desktop or iPad apps.

### Using a Proxy (If Signal Is Blocked)

If Signal is blocked in your country:

- [Find a proxy address](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#proxy_find)
- [Configure proxy on Android](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61MK3AQHE51VWFYGTC)
- [Configure proxy on iOS](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61PANY8JE6N8XXWQKM)
- Consider [running a proxy server](https://github.com/signalapp/Signal-TLS-Proxy) to help others

### Create Your Account

Register following [Signal's phone number registration guide](https://support.signal.org/hc/en-us/articles/360007318691-Register-a-phone-number).

**Consider using an alternative phone number** — Your phone number may be linked to your official identity. For sensitive activities, [get a different phone number](https://securityinabox.org/en/assess-plan/multiple-identities/#get-a-different-phone-number) and [keep it private in your profile](#keep-your-phone-number-private).

---

## Account Protection

### Set a Registration Lock PIN

1. Go to **Settings > Account**
2. Enable **Registration Lock**
3. Select a PIN and store it in a password manager (Signal cannot reset it for you)

Learn more in [Signal's PIN documentation](https://support.signal.org/hc/en-us/articles/360007059792-Signal-PIN).

> **Why this matters:** A registration lock prevents others from registering a Signal account with your phone number without knowing your PIN.

---

## Privacy Settings

### Keep Your Phone Number Private

1. Go to **Settings > Privacy > Phone Number > Who can see my number**
2. Select **Nobody**

Learn more about [Signal's phone number privacy](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive).

### Connect Without Sharing Your Phone Number

1. **Create a username** — Must be unique with at least 2 digits appended
2. Go to **Settings > Privacy > Phone Number > Who can find me by number**
3. Select **Nobody**

This ensures only people with your username can find you on Signal.

### Back Up Your Messages

Signal only stores encrypted backups locally on your device. [Learn how to back up and restore conversations](https://support.signal.org/hc/en-us/articles/360007059752-Backup-and-Restore-Messages).

### Device Linking Precautions

- [Link Signal Desktop or iPad](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices) only when necessary
- Minimize linked devices to reduce attack surface
- Never link to shared or public devices

### iOS-Specific Settings

Disable these integrations to keep Signal activities private:

- **Settings > Chats** — Disable **Share Contacts with iOS**
- **Settings > Privacy > Calling > Show Calls in Recents** — Disable this option

### Android-Specific Settings

- Go to **Settings > Privacy**
- Enable **Incognito Keyboard**

Learn more in [Signal's Incognito Keyboard documentation](https://support.signal.org/hc/en-us/articles/360055276112-Incognito-Keyboard).

---

## Securing Your Communications

### Verify Contacts' Identities

Verify safety numbers to confirm you're communicating with the right person:

- [View a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#view)
- [Verify a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#verify)
- Mark verified contacts using the **Mark as Verified** button

> **Why this matters:** Safety numbers uniquely identify accounts and encryption keys. Verification protects against impersonation—if someone tries to impersonate a verified contact, you'll see a safety number change alert.

### Use Disappearing Messages

- Enable disappearing messages for sensitive conversations
- Alternatively, [manually delete messages, chats, or all chat history](https://support.signal.org/hc/en-us/articles/360007320491-Delete-messages-alerts-or-chats)

### Enable Screen Security

- **Android:** Settings > Privacy > Screen Security
- **iOS:** Settings > Privacy > Hide Screen in App Switcher

This blocks screenshots and prevents message previews in the app switcher. For notification privacy, see device-specific guides for [Android](https://securityinabox.org/en/phones-and-computers/android/#control-what-can-be-seen-when-your-device-is-locked), [iOS](https://securityinabox.org/en/phones-and-computers/ios/#control-what-can-be-seen-when-your-device-is-locked), [Mac](https://securityinabox.org/en/phones-and-computers/mac/#control-what-can-be-seen-when-your-device-is-locked), [Linux](https://securityinabox.org/en/phones-and-computers/linux/#control-what-can-be-seen-when-your-device-is-locked), or [Windows](https://securityinabox.org/en/phones-and-computers/windows/#control-what-can-be-seen-when-your-device-is-locked).

### Protect Your IP Address on Calls

Go to **Settings > Privacy > Advanced** and enable **Always relay calls**.

> **Note:** All calls are end-to-end encrypted regardless of this setting. Group calls always route through Signal's servers, protecting your IP automatically.

### Disable Link Previews

Go to **Settings > Chats** and disable **Generate link previews**.

> **Why this matters:** Link previews can leak information to linked websites. Both you and your contacts need to disable this for full protection.

---

## Group Protection

Signal supports groups up to 1,000 members and group calls with up to 50 participants.

### Membership Control

- Enable **Approve new members** (Android) or **Require admin approval** (iOS) when creating groups
- [Add members carefully](https://support.signal.org/hc/en-us/articles/360050427692-Manage-a-group#add)
- Consider restricting member additions to admins only

### Admin Management

- Assign admin rights to trusted members: tap member name > **Make admin**
- Multiple admins ensure continuity if one becomes unavailable
- Distribute moderation responsibilities

### Permission Settings

In the group's **Permissions** section, restrict to admins:
- Adding members
- Editing group info
- Sending messages (for announcement-style groups)

### Moderation

- Remove members who violate community standards: tap name > **Remove from group**
- Enable disappearing messages for sensitive groups

---

## Monitoring for Suspicious Access

### Check Linked Devices Regularly

- [View linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01JPNF3R6PAJQSQEFGVMMZ75TA)
- [Unlink unrecognized devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01K0YRHGSACMHVM8JYNSPNX157)

### If Your Device Is Lost or Stolen

Follow [Signal's guidance for lost or stolen phones](https://support.signal.org/hc/en-us/articles/360007062452-What-do-I-do-if-my-phone-is-lost-or-stolen).

---

## Alternative: Molly Client

[Molly](https://molly.im/) is an Android-only Signal client with additional security features:

- **Passphrase encryption** for stored messages
- **Multi-device support** for the same account on multiple phones
- **Enhanced backup options** with configurable frequency and retention
- **Google-independent notifications** (Molly-FOSS only)

See the [full feature list](https://github.com/mollyim/mollyim-android?tab=readme-ov-file#features) and [Techlore's Molly overview](https://www.youtube.com/watch?v=P-2z2c3XBkQ).

---

## Resources

- [EFF Surveillance Self-Defense: How to Use Signal](https://ssd.eff.org/module/how-to-use-signal) — Updated March 26, 2025
- [Techlore: Lock Down Signal Messenger Ultimate Hardening Guide](https://www.youtube.com/watch?v=DPjg3651oJM) — Published August 9, 2024
- [Signal Support Documentation](https://support.signal.org/)
- [Security in a Box: Secure Chat Guide](https://securityinabox.org/en/communication/secure-chat)