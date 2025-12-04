```yaml
---
title: "Protect Yourself and Your Communications When Using Signal"
tags: [signal, encryption, secure-messaging, privacy, digital-security, mobile-security]
category: "Secure Communication"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, General Public]
topics: ["End-to-End Encryption", "Secure Messaging", "Account Security", "Privacy Protection"]
summary: "Comprehensive guide to securing your Signal account, protecting communications, and using advanced privacy features effectively."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic smartphone usage", "Signal app installed", "Understanding of basic privacy concepts"]
estimated_read_time: "15 minutes"
---
```

# Protect Yourself and Your Communications When Using Signal

*Updated 23 September 2025*

**Signal** is a free and open-source messaging app that protects your communications using end-to-end encryption. Developed by [the Signal Foundation](https://signalfoundation.org/), it's available for all major operating systems, though account creation requires installation on a smartphone.

This guide covers how to use Signal more safely and secure your account. For broader context, see the companion guide on [using messaging apps more securely](https://securityinabox.org/en/communication/secure-chat).

---

## Table of Contents

- [The Pros and Cons of Using Signal](#the-pros-and-cons-of-using-signal)
- [Before You Start Using Signal](#before-you-start-using-signal)
- [Install Signal](#install-signal)
- [Use a Proxy if Signal is Blocked](#use-a-proxy-if-signal-is-blocked-in-your-country)
- [Create a New Account](#create-a-new-account)
- [Protect Your Account](#protect-your-account)
- [Use Signal More Safely](#use-signal-more-safely)
- [Secure Your Signal Communications](#secure-your-signal-communications)
- [Protect Your Groups](#protect-your-groups)
- [Check Suspicious Access](#check-suspicious-access)
- [Consider Using Molly as an Alternative Client](#consider-using-molly-as-an-alternative-client-for-signal)
- [Resources](#resources)

---

## The Pros and Cons of Using Signal

### Advantages

- **Open-source software** — Code is [publicly available](https://github.com/signalapp) for independent security review
- **Strong encryption by default** — Protects 1:1 messages, group chats, voice calls, and video calls using [well-documented end-to-end encryption](https://github.com/signalapp/libsignal)
- **Identity verification** — Allows you to [verify contact identities](#verify-your-contacts-identities) through safety numbers
- **Forward secrecy** — Past conversations remain protected even if an encryption key is later compromised
- **Asynchronous messaging** — Messages sent while you're offline wait for you when you reconnect

### Limitations

- **Signal-to-Signal only** — Encryption only works when communicating with other Signal users
- **Metadata visibility** — While message content is protected, the fact that you're using encrypted communications may be observable
- **Phone number requirement** — Registration requires a phone capable of receiving SMS or calls from a US number
- **Push notification infrastructure** — Relies on Google Firebase (Android) and Apple Push Notification Service (iOS), though notifications contain no sensitive data and are processed entirely on your device
- **Legal considerations** — Encryption tools may attract attention or violate laws in some jurisdictions. Research your local situation using the [Global Partners Digital World map of encryption laws](https://www.gp-digital.org/world-map-of-encryption)
- **Regional blocking** — [Some countries](https://en.wikipedia.org/wiki/Signal_(software)#Blocking) block Signal entirely, though [proxies can help](#use-a-proxy-if-signal-is-blocked-in-your-country)

---

## Before You Start Using Signal

1. **Create a communication plan** based on recommendations in the guide on [protecting the privacy of your online communications](https://securityinabox.org/en/assess-plan/private-communication/)
2. **Read general advice** on [using messaging apps more securely](https://securityinabox.org/en/communication/secure-chat/)
3. **Secure your device** — Review recommendations for [Android](https://securityinabox.org/en/phones-and-computers/android) or [iOS](https://securityinabox.org/en/phones-and-computers/ios) security

---

## Install Signal

1. Follow [Signal's official installation instructions](https://support.signal.org/hc/en-us/articles/360008216551-Installing-Signal) for your mobile device
2. After phone installation, you can optionally connect to a desktop app or iPad app

---

## Use a Proxy if Signal is Blocked in Your Country

If Signal is [blocked in your region](https://en.wikipedia.org/wiki/Signal_(software)#Blocking), you can still create an account or continue using it through a proxy:

- [How to find a proxy address](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#proxy_find)
- [Using a proxy on Android](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61MK3AQHE51VWFYGTC)
- [Using a proxy on iOS](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61PANY8JE6N8XXWQKM)
- [Running your own proxy server](https://github.com/signalapp/Signal-TLS-Proxy) to support circumvention efforts

---

## Create a New Account

Learn how to register in [Signal's phone number registration guide](https://support.signal.org/hc/en-us/articles/360007318691-Register-a-phone-number).

### Consider Registering with an Alternative Phone Number

Your phone number may be linked to your official identity. For sensitive activities that shouldn't be traced back to you:

1. [Get a different phone number](https://securityinabox.org/en/assess-plan/multiple-identities/#get-a-different-phone-number) than your primary one
2. [Keep your phone number private in your profile](#keep-your-phone-number-private)

---

## Protect Your Account

### Set a Registration Lock PIN

A registration lock prevents others from registering a Signal account with your phone number without knowing your PIN.

**To enable:**
1. Go to **Settings > Account**
2. Turn on **Registration Lock**
3. Select a PIN and store it in a password manager (Signal cannot reset this for you)

Learn more in [Signal's PIN documentation](https://support.signal.org/hc/en-us/articles/360007059792-Signal-PIN).

---

## Use Signal More Safely

### Keep Your Phone Number Private

Since phone numbers often connect to official identities, keep yours hidden for sensitive communications:

1. Go to **Settings > Privacy > Phone Number > Who can see my number**
2. Select **Nobody**

Learn more about [Signal's phone number privacy](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive).

### Connect with Others Without Sharing Your Phone Number

1. **Create a username** — Must be unique, consisting of a name plus at least 2 digits
2. Go to **Settings > Privacy > Phone Number > Who can find me by number**
3. Select **Nobody** — This ensures only people with your username can find you

Learn more about [Signal usernames](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive#usernames).

### Back Up Your Messages

Signal doesn't back up chats by default. Backups are stored encrypted on your device only.

[Learn how to back up and restore Signal conversations](https://support.signal.org/hc/en-us/articles/360007059752-Backup-and-Restore-Messages).

### Precautions When Linking Devices

- [Link Signal Desktop or iPad to your phone](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices)
- **Minimize linked devices** — Each additional device increases your attack surface
- **Avoid shared devices** — Never link to public computers or others' devices

### iOS-Specific: Disable Contact and Call Sharing

Prevent iOS from syncing Signal data with system apps:

1. **Settings > Chats** — Disable **Share Contacts with iOS**
2. **Settings > Privacy > Calling > Show Calls in Recents** — Disable this option

### Android-Specific: Enable Incognito Keyboard

1. Go to **Settings > Privacy**
2. Enable **Incognito Keyboard**

This requests your keyboard app to disable learning and prediction for Signal. [Learn more](https://support.signal.org/hc/en-us/articles/360055276112-Incognito-Keyboard).

---

## Secure Your Signal Communications

### Verify Your Contacts' Identities

Safety numbers uniquely identify accounts and their encryption keys, helping you avoid impersonation:

1. [View a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#view)
2. [Verify a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#verify) (compare in person or via trusted channel)
3. Tap **Mark as Verified** once confirmed

If someone tries to impersonate a verified contact, Signal will alert you to the safety number change.

### Use Disappearing Messages

Limit stored information by setting messages to auto-delete:

- Enable for all conversations or specific sensitive ones
- If not using auto-deletion, [manually delete chat history](https://support.signal.org/hc/en-us/articles/360007320491-Delete-messages-alerts-or-chats) regularly

### Enable Screen Security

Blocks screenshots and app switcher previews:

- **Android:** Settings > Privacy > Screen Security
- **iOS:** Settings > Privacy > Hide Screen in App Switcher

> **Note:** This doesn't affect notification previews. Configure those in your device settings for [Android](https://securityinabox.org/en/phones-and-computers/android/#control-what-can-be-seen-when-your-device-is-locked), [iOS](https://securityinabox.org/en/phones-and-computers/ios/#control-what-can-be-seen-when-your-device-is-locked), [Mac](https://securityinabox.org/en/phones-and-computers/mac/#control-what-can-be-seen-when-your-device-is-locked), [Linux](https://securityinabox.org/en/phones-and-computers/linux/#control-what-can-be-seen-when-your-device-is-locked), or [Windows](https://securityinabox.org/en/phones-and-computers/windows/#control-what-can-be-seen-when-your-device-is-locked).

### Protect Your IP Address on Calls

For 1:1 calls, hide your IP address by routing through Signal's servers:

1. Go to **Settings > Privacy > Advanced**
2. Enable **Always relay calls**

> **Note:** Group calls automatically route through Signal's servers, so your IP is always protected in group calls.

### Disable Link Previews

Prevent linked websites from obtaining information about you:

1. Go to **Settings > Chats**
2. Disable **Generate link previews**

> **Note:** Both you and your contacts need this disabled for full protection. [Learn more](https://support.signal.org/hc/en-us/articles/360022474332-Link-Previews).

---

## Protect Your Groups

Signal supports groups of up to 1,000 members and group calls with up to 50 participants.

- [Starting a group chat](https://support.signal.org/hc/en-us/articles/360007319331-Group-chats)
- [Group voice and video calls](https://support.signal.org/hc/en-us/articles/360052977792-Group-Calling-Voice-or-Video)
- [Tips on using group chats safely](https://securityinabox.org/en/communication/secure-chat/#use-group-chats-more-safely)

### Invite Only People You Know and Trust

1. When creating a group, enable admin approval:
   - **Android:** Approve new members
   - **iOS:** Require admin approval
2. [Add members carefully](https://support.signal.org/hc/en-us/articles/360050427692-Manage-a-group#add)
3. For sensitive groups, restrict member addition to admins only
4. Never share invite links publicly

### Select a Few Trusted Admins

Multiple admins create resilience and share moderation burden:

1. Go to the group members list
2. Tap the person's name
3. Select **Make admin**

### Assign Privileges to Admins Only

In the **Permissions** section, you can restrict to admins:
- Adding members
- Editing group info
- Sending messages

### Moderate the Conversation

- For announcement-style groups, allow only admins to send messages
- Remove members who violate community standards: tap their name > **Remove from group**

### Set Messages to Disappear

Enable disappearing messages for groups, especially sensitive ones, to limit stored information.

---

## Check Suspicious Access

### Check Your Linked Devices

Regularly verify no unauthorized devices have access:

1. [View linked devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01JPNF3R6PAJQSQEFGVMMZ75TA)
2. [Unlink unrecognized devices](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01K0YRHGSACMHVM8JYNSPNX157)

### If Your Device is Lost or Stolen

Follow [Signal's guidance for lost or stolen phones](https://support.signal.org/hc/en-us/articles/360007062452-What-do-I-do-if-my-phone-is-lost-or-stolen).

---

## Consider Using Molly as an Alternative Client for Signal

[Molly](https://molly.im/) (or Molly-FOSS) is an Android-only alternative client offering additional features:

- **Passphrase encryption** for stored messages
- **Multi-device support** — Same Signal account on multiple mobile devices
- **Flexible backups** — Control backup frequency and retention
- **Google-independent notifications** — Molly-FOSS can notify without Google services

Molly is a secure, free, and open-source client with all Signal features plus security improvements.

**Learn more:**
- [Full feature list on Molly's GitHub](https://github.com/mollyim/mollyim-android?tab=readme-ov-file#features)
- [Techlore's video on Molly](https://www.youtube.com/watch?v=P-2z2c3XBkQ) (YouTube)

---

## Resources

- [EFF Surveillance Self-Defense: How to Use Signal](https://ssd.eff.org/module/how-to-use-signal) — *Last updated: March 26, 2025*
- [Techlore: Lock Down Signal Messenger - Ultimate Hardening Guide](https://www.youtube.com/watch?v=DPjg3651oJM) (YouTube) — *Published: August 9, 2024*
- [Signal Official Website](https://signal.org/)