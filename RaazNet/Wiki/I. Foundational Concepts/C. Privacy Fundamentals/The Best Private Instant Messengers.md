```yaml
---
title: "Private Instant Messengers: Signal, SimpleX, and Briar"
tags: [privacy, security, encryption, messaging, real-time-communication, e2ee]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Security Researchers, General Public]
topics: ["Encrypted Messaging", "Privacy Protection", "Secure Communication"]
summary: "Comprehensive guide to privacy-focused instant messengers with end-to-end encryption, covering Signal, Molly, SimpleX Chat, and Briar."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of encryption", "Smartphone or computer usage"]
estimated_read_time: "12 minutes"
---
```

# Private Real-Time Communication

These recommendations for encrypted **real-time communication** are designed to secure your sensitive communications. These instant messengers protect against passive attacks, service provider surveillance, mass surveillance programs, and surveillance capitalism.

> **Important:** It's time to stop using SMS for private communications. Standard text messaging lacks encryption and exposes your messages to carriers and potential interceptors.

---

## Signal

**Signal** is a mobile app developed by Signal Messenger LLC that provides instant messaging and calls secured with the Signal protocol—an extremely secure encryption protocol supporting:

- **Forward secrecy**: Keys rotate frequently, so if the current encryption key is compromised, past messages remain protected
- **Post-compromise security**: Prevents attackers from decrypting future messages after compromising a private key

### Key Features

- **Encrypted contact lists**: Protected using your Signal PIN; servers cannot access them
- **Encrypted personal profiles**: Only shared with contacts you chat with
- **Private groups**: Server has no record of group memberships, titles, avatars, or attributes
- **Sealed Sender**: Encrypts sender address along with message body; only recipient address visible to server

### Privacy Configuration

To maximize privacy on Signal:

1. Open app settings and tap your account profile
2. Tap **Username** and create one (paired with unique digits, e.g., `@john.35`)
3. Navigate to **Settings → Privacy → Phone Number**
4. Set **Who Can See My Number** to **Nobody**
5. Optionally set **Who Can Find Me By Number** to **Nobody**

### Security Verification

The Signal protocol was independently [audited in 2016](https://eprint.iacr.org/2016/1013.pdf), with full specification available in their [documentation](https://signal.org/docs).

**Availability**: Android (Google Play, APK), iOS, Windows, macOS, Linux

---

## Molly (Android Alternative)

**Molly** is an alternative Signal client for Android designed for users with higher threat models requiring protection against targeted attacks.

### Additional Security Features

- **Local database encryption**: Encrypt with passphrase at rest
- **Secure RAM shredding**: Unused data securely wiped
- **Tor routing**: Route connections through Tor network
- **Automatic locking**: Enhanced device security
- **Scheduled backups**: Automated data protection

### Important Considerations

- Updates every two weeks (security patches applied immediately)
- Requires trusting both Signal and Molly development teams
- Supports [reproducible builds](https://github.com/mollyim/mollyim-android/tree/main/reproducible-builds) for verification

### Molly-FOSS Version

Removes proprietary Google services code at the expense of some features. Push notifications available via [UnifiedPush](https://unifiedpush.org/) with a [MollySocket](https://github.com/mollyim/mollysocket) server.

**Availability**: F-Droid, Accrescent, GitHub

---

## SimpleX Chat

**SimpleX Chat** is unique among messengers because it **doesn't require any unique identifiers**—no phone numbers, usernames, or email addresses. Its decentralized network makes it effective against censorship.

### Technical Features

- **SimpleX Messaging Protocol**: Double ratchet encryption with quantum resistance
- **Metadata protection**: Uses unidirectional "simplex queues" for message delivery
- **Out-of-band verification**: QR code or invite link scanning protects against man-in-the-middle attacks
- **Data portability**: Export and import data between devices; no central server backups

### Communication Capabilities

- Direct messaging
- Group chats
- End-to-end encrypted calls

### Security Audits

- [July 2024](https://simplex.chat/blog/20241014-simplex-network-v6-1-security-review-better-calls-user-experience.html#simplex-cryptographic-design-review-by-trail-of-bits): Trail of Bits cryptographic design review
- [October 2022](https://simplex.chat/blog/20221108-simplex-chat-v4.2-security-audit-new-website): Security audit

**Availability**: Android (Google Play), iOS, Windows, macOS, Linux, Flathub

---

## Briar

**Briar** is an encrypted instant messenger that connects through the **Tor network**, making it highly effective for circumventing censorship. It can also connect via **Wi-Fi or Bluetooth** for local proximity communication.

### Unique Capabilities

- **Tor-based routing**: Anonymous network connectivity
- **Local mesh mode**: Functions when internet is unavailable
- **Peer-to-peer**: No central servers required
- **Published specification**: Fully transparent [protocol documentation](https://code.briarproject.org/briar/briar-spec)

### Security Features

- Forward secrecy via Bramble Handshake and Transport protocols
- Independently [audited client software](https://briarproject.org/news/2017-beta-released-security-audit)
- Audited Tor anonymous routing

**Availability**: Android (Google Play), Windows, Linux, Flathub

---

## Selection Criteria

### Minimum Requirements

All recommended messengers must:

- Have open-source clients
- Not require sharing personal identifiers (phone numbers/emails) with contacts
- Use E2EE for private messages by default
- Support E2EE for all messages
- Support forward secrecy
- Have published audits from reputable, independent third parties

### Best-Case Features

Ideal messengers should also:

- Support post-compromise security (future secrecy)
- Have open-source servers
- Use decentralized networks (federated or P2P)
- Use E2EE for all messages by default
- Support Linux, macOS, Windows, Android, and iOS

---

## Quick Comparison

| Feature | Signal | Molly | SimpleX | Briar |
|---------|--------|-------|---------|-------|
| No phone number required | ✓* | ✓* | ✓ | ✓ |
| Decentralized | ✗ | ✗ | ✓ | ✓ |
| Tor support | ✗ | ✓ | ✗ | ✓ |
| Offline/mesh mode | ✗ | ✗ | ✗ | ✓ |
| Desktop apps | ✓ | ✗ | ✓ | ✓ |
| iOS support | ✓ | ✗ | ✓ | ✗ |

*Signal/Molly require phone number for registration but can hide it from contacts

---

## Glossary

**Forward Secrecy**: Keys rotate frequently so that if the current encryption key is compromised, it does not expose past messages.

**Post-Compromise Security (Future Secrecy)**: Prevents attackers from decrypting future messages after compromising a private key, unless they compromise additional session keys. Forces attackers to intercept all communication continuously.