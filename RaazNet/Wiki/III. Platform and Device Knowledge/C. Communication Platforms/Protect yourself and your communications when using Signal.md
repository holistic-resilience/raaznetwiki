```yaml
---
title: "Protect Yourself and Your Communications When Using Signal"
tags: [signal, encrypted-messaging, privacy, digital-security, mobile-security, end-to-end-encryption]
category: "Secure Communication"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, General Public]
topics: ["Encrypted Messaging", "Account Security", "Privacy Protection", "Group Security"]
summary: "Comprehensive guide to securing your Signal account, protecting communications, and using advanced privacy features effectively."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic smartphone proficiency", "Signal app installed", "Understanding of basic encryption concepts"]
estimated_read_time: "15 minutes"
---
```

# Protect Yourself and Your Communications When Using Signal

**Last Updated:** 23 September 2025

**Signal** is a free and open-source messaging app that protects your communications using end-to-end encryption. Developed by [the Signal Foundation](https://signalfoundation.org/), it's available for all major operating systems, though an account can only be created by installing it on a smartphone.

This guide covers how to use Signal more safely and secure your account. For broader context, see the companion guide on [using messaging apps more securely](https://securityinabox.org/en/communication/secure-chat).

---

## Table of Contents

1. [Pros and Cons of Using Signal](#pros-and-cons-of-using-signal)
2. [Before You Start](#before-you-start)
3. [Installation and Setup](#installation-and-setup)
4. [Account Protection](#account-protection)
5. [Using Signal Safely](#using-signal-safely)
6. [Securing Your Communications](#securing-your-communications)
7. [Protecting Your Groups](#protecting-your-groups)
8. [Checking for Suspicious Access](#checking-for-suspicious-access)
9. [Alternative: Molly Client](#alternative-molly-client)
10. [Additional Resources](#additional-resources)

---

## Pros and Cons of Using Signal

### Advantages

- **Open-source software** — Code is [publicly available](https://github.com/signalapp) for independent security review
- **Strong encryption by default** — All 1:1 and group messages, voice, and video calls use [well-documented end-to-end encryption](https://github.com/signalapp/libsignal)
- **Identity verification** — Verify contacts' identities through safety numbers
- **Forward secrecy** — Past conversations remain safe even if encryption keys are compromised
- **Asynchronous messaging** — Messages sent while offline are delivered when you reconnect

### Limitations

- **Signal-to-Signal only** — Encryption only works between Signal users
- **Metadata visibility** — Signal doesn't hide that you're sending encrypted messages or making encrypted calls
- **Phone number required** — Registration requires a phone capable of receiving SMS or calls from a US number
- **Push notification dependencies** — Relies on Google Firebase (Android) and Apple Push Notification Service (iOS), though notifications contain no sensitive data and are processed entirely on your device
- **Legal considerations** — Encryption tools may attract attention or violate laws in some jurisdictions. Check the [Global Partners Digital World map of encryption laws](https://www.gp-digital.org/world-map-of-encryption)
- **Regional blocking** — [Some countries block Signal](https://en.wikipedia.org/wiki/Signal_(software)#Blocking); proxy connections may be required

---

## Before You Start

1. **Create a communication plan** based on recommendations in the guide on [protecting online communication privacy](https://securityinabox.org/en/assess-plan/private-communication/)
2. **Read general advice** on [using messaging apps securely](https://securityinabox.org/en/communication/secure-chat/)
3. **Secure your device** — Review security recommendations for [Android](https://securityinabox.org/en/phones-and-computers/android) or [iOS](https://securityinabox.org/en/phones-and-computers/ios)

---

## Installation and Setup

### Installing Signal

Follow [Signal's official installation instructions](https://support.signal.org/hc/en-us/articles/360008216551-Installing-Signal) for your mobile device. After phone installation, you can connect desktop or iPad apps.

### Using a Proxy (If Signal Is Blocked)

If Signal is blocked in your country:

- [Find a proxy address](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#proxy_find)
- [Configure proxy on Android](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61MK3AQHE51VWFYGTC)
- [Configure proxy on iOS](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61PANY8JE6N8XXWQKM)
- [Set up your own proxy server](https://github.com/signalapp/Signal-TLS-Proxy) to help circumvention efforts

### Creating an Account

See Signal's [phone number registration guide](https://support.signal.org/hc/en-us/articles/360007318691-Register-a-phone-number).

#### Consider Using an Alternative Phone Number

Your phone number may be connected to your official identity. For sensitive activities:

- [Get a different phone number](https://securityinabox.org/en/assess-plan/multiple-identities/#get-a-different-phone-number)
- [Keep your phone number private in your profile](#keep-your-phone-number-private)

---

## Account Protection

### Set a Registration Lock PIN

A registration lock prevents others from registering a Signal account with your phone number.

**To enable:**
1. Go to **Settings > Account**
2. Turn on **Registration Lock**
3. Select a PIN and store it in a password manager (Signal cannot reset it for you)

Learn more in [Signal's PIN support page](https://support.signal.org/hc/en-us/articles/360007059792-Signal-PIN).

---

## Using Signal Safely

### Keep Your Phone Number Private

Since phone numbers are often connected to official identities, keep yours hidden:

1. Go to **Settings > Privacy > Phone Number > Who can see my number**
2. Select **Nobody**

Learn more about [Signal's phone number privacy](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive).

### Connect Without Sharing Your Phone Number

Use a username instead:

1. **Create a username** (must be unique: name + at least 2 digits)
2. Go to **Settings > Privacy > Phone Number > Who can find me by number**
3. Select **Nobody**

This ensures only people with your username can find you on Signal.

### Back Up Your Messages

Signal doesn't back up chats by default. Backups are stored encrypted on your device only.

- [Learn to back up and restore conversations](https://support.signal.org/hc/en-us/articles/360007059752-Backup-and-Restore-Messages)

### Linking Devices Safely

- [Link Signal Desktop or iPad to your phone](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices)
- **Minimize linked devices** — Each additional device increases your attack surface
- **Never link to shared devices** — Avoid public computers or others' devices

### iOS-Specific Settings

Disable iOS integrations to keep Signal activities private:

1. **Settings > Chats** — Disable **Share Contacts with iOS**
2. **Settings > Privacy > Calling** — Disable **Show Calls in Recents**

This prevents contact and call history synchronization with iCloud.

### Android-Specific Settings

Enable Incognito Keyboard to prevent your keyboard from learning what you type:

1. Go to **Settings > Privacy**
2. Enable **Incognito Keyboard**

Learn more in [Signal's Incognito Keyboard guide](https://support.signal.org/hc/en-us/articles/360055276112-Incognito-Keyboard).

---

## Securing Your Communications

### Verify Contacts' Identities

Safety numbers uniquely identify accounts and encryption keys, helping you avoid impersonation.

- [View a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#view)
- [Verify a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#verify)

After verification, tap **Mark as Verified**. If someone impersonates a verified contact, Signal will alert you to the safety number change.

### Use Disappearing Messages

Limit stored information by setting messages to auto-delete:

- Enable for all conversations or specific sensitive ones
- Manually [delete messages, single chats, or all chats](https://support.signal.org/hc/en-us/articles/360007320491-Delete-messages-alerts-or-chats) regularly

### Enable Screen Security

Prevent screenshots and app switcher previews:

- **Android:** Settings > Privacy > Screen Security
- **iOS:** Settings > Privacy > Hide Screen in App Switcher

> **Note:** This doesn't affect notification previews. Configure those in your device settings for [Android](https://securityinabox.org/en/phones-and-computers/android/#control-what-can-be-seen-when-your-device-is-locked), [iOS](https://securityinabox.org/en/phones-and-computers/ios/#control-what-can-be-seen-when-your-device-is-locked), [Mac](https://securityinabox.org/en/phones-and-computers/mac/#control-what-can-be-seen-when-your-device-is-locked), [Linux](https://securityinabox.org/en/phones-and-computers/linux/#control-what-can-be-seen-when-your-device-is-locked), or [Windows](https://securityinabox.org/en/phones-and-computers/windows/#control-what-can-be-seen-when-your-device-is-locked).

### Protect Your IP Address on Calls

Route calls through Signal's servers to hide your IP:

1. Go to **Settings > Privacy > Advanced**
2. Enable **Always relay calls**

> **Note:** Calls remain end-to-end encrypted. Group calls always route through Signal's servers automatically.

### Disable Link Previews

Prevent linked websites from obtaining information about you:

1. Go to **Settings > Chats**
2. Disable **Generate link previews**

> **Note:** This only affects links you send. Others must disable previews on their end too.

---

## Protecting Your Groups

Signal supports groups of up to 1,000 members and group calls with up to 50 participants.

- [Start a group chat](https://support.signal.org/hc/en-us/articles/360007319331-Group-chats)
- [Group voice and video calls](https://support.signal.org/hc/en-us/articles/360052977792-Group-Calling-Voice-or-Video)
- [Tips for safer group chats](https://securityinabox.org/en/communication/secure-chat/#use-group-chats-more-safely)

### Control Group Membership

- Enable **Approve new members** (Android) or **Require admin approval** (iOS) when creating groups
- [Add members to a group](https://support.signal.org/hc/en-us/articles/360050427692-Manage-a-group#add)
- Consider restricting member additions to admins only

> **Tip:** Don't share invite links publicly. For sensitive groups, require admin approval for all new members.

### Manage Admins Effectively

- Give admin rights: Go to group members list > tap member name > **Make admin**
- Select a few trusted admins to share moderation responsibilities
- Multiple admins ensure continuity if one becomes unavailable

### Configure Permissions

In the group's **Permissions** section, restrict to admins:
- Adding members
- Editing group info
- Sending messages (for announcement-style groups)

### Moderate Conversations

- For update-focused groups, allow only admins to send messages
- Remove members violating community standards: tap their name > **Remove from group**

### Enable Disappearing Messages for Groups

Set messages to disappear in all groups, especially sensitive ones.

---

## Checking for Suspicious Access

### Review Linked Devices

Adversaries may access your account from unauthorized devices.

- [View linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01JPNF3R6PAJQSQEFGVMMZ75TA)
- [Unlink unrecognized devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01K0YRHGSACMHVM8JYNSPNX157)

### If Your Device Is Lost or Stolen

Follow [Signal's guide for lost or stolen phones](https://support.signal.org/hc/en-us/articles/360007062452-What-do-I-do-if-my-phone-is-lost-or-stolen).

---

## Alternative: Molly Client

[Molly](https://molly.im/) (or Molly-FOSS) is an Android alternative client offering additional features:

- **Passphrase encryption** for stored messages
- **Multi-device support** for the same Signal account on multiple phones
- **Flexible backup options** — choose frequency and retention
- **Google-independent notifications** (Molly-FOSS only)

Molly includes all Signal features plus security improvements. See the [full feature list](https://github.com/mollyim/mollyim-android?tab=readme-ov-file#features) or watch [Techlore's Molly overview](https://www.youtube.com/watch?v=P-2z2c3XBkQ).

---

## Additional Resources

- [EFF Surveillance Self-Defense: How to Use Signal](https://ssd.eff.org/module/how-to-use-signal) — Updated March 26, 2025
- [Techlore: Lock Down Signal Messenger Ultimate Hardening Guide](https://www.youtube.com/watch?v=DPjg3651oJM) — August 9, 2024