```yaml
---
title: "Private Instant Messengers Guide"
tags: [privacy, security, encryption, messaging, signal, simplex, briar]
category: "Digital Privacy"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Encrypted Messaging", "Real-Time Communication", "Digital Security"]
summary: "Comprehensive guide to encrypted instant messengers including Signal, SimpleX Chat, and Briar with security features and selection criteria."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic smartphone usage", "Understanding of privacy concepts"]
estimated_read_time: "8 minutes"
---
```

# Private Instant Messengers

These recommendations for encrypted **real-time communication** are designed to secure your sensitive communications. These instant messengers protect against passive attacks, service provider surveillance, mass surveillance programs, and surveillance capitalism.

> **Important**: It's time to stop using SMS for sensitive communications. Standard text messages lack encryption and expose your conversations to interception.

---

## Signal

**Signal** is a mobile app developed by Signal Messenger LLC that provides instant messaging and calls secured with the Signal protocol—an extremely secure encryption protocol supporting:

- **Forward secrecy**: Keys rotate frequently, so compromising the current key doesn't expose past messages
- **Post-compromise security**: Attackers cannot decrypt future messages after compromising a private key

### Key Privacy Features

- **Encrypted contact lists**: Protected using your Signal PIN; servers cannot access them
- **Encrypted personal profiles**: Only shared with contacts you chat with
- **Private groups**: Server has no record of group memberships, titles, avatars, or attributes
- **Sealed Sender**: Encrypts sender address along with message body; only recipient address visible to server

### Recommended Configuration

1. Open app settings → tap your account profile
2. Tap **Username** → choose **Continue** on setup screen
3. Enter a username (paired with unique digits, e.g., `@john.35`)
4. Go to **Privacy** → **Phone Number**
5. Set **Who Can See My Number** to **Nobody**
6. (Optional) Set **Who Can Find Me By Number** to **Nobody**

### Security Verification

The Signal protocol was independently [audited in 2016](https://eprint.iacr.org/2016/1013.pdf), with full specification available in their documentation.

**Available on**: Android (Google Play, F-Droid, APK), iOS, Windows, macOS, Linux

---

## Molly (Android Alternative)

**Molly** is an alternative Signal client for Android recommended for users with higher threat models requiring protection against targeted attacks.

### Additional Security Features

- **Local database encryption**: Encrypt with passphrase at rest
- **Secure RAM shredding**: Unused RAM data securely wiped
- **Tor routing**: Route connections through Tor network
- **Automatic locking**: Enhanced device security
- **Scheduled backups**: Automated backup management

### Important Considerations

- Updates every two weeks (security patches applied immediately)
- Requires trusting both Signal and Molly development teams
- **Molly-FOSS**: Version without proprietary Google services (requires UnifiedPush for notifications)

**Available on**: F-Droid, Accrescent, GitHub

---

## SimpleX Chat

**SimpleX Chat** is an instant messenger that **doesn't require any unique identifiers**—no phone numbers or usernames needed. Its decentralized network makes it effective against censorship.

### Key Features

- **No identifiers**: Connect without phone numbers or usernames
- **SimpleX Messaging Protocol**: Double ratchet encryption with quantum resistance
- **Metadata protection**: Uses unidirectional "simplex queues" for message delivery
- **Out-of-band verification**: Scan QR codes or click invite links to verify contacts
- **Data portability**: Export and import data between devices; no central backup servers

### Security Verification

Independently audited in [July 2024](https://simplex.chat/blog/20241014-simplex-network-v6-1-security-review-better-calls-user-experience.html) and [October 2022](https://simplex.chat/blog/20221108-simplex-chat-v4.2-security-audit-new-website).

**Available on**: Android, iOS, Windows, macOS, Linux, Flathub

---

## Briar

**Briar** is an encrypted instant messenger that connects via the **Tor network**, making it effective for circumventing censorship. It can also connect via Wi-Fi or Bluetooth for local proximity communication.

### Unique Features

- **Tor-based connections**: All communications routed through Tor
- **Local mesh mode**: Functions when internet is unavailable (Wi-Fi/Bluetooth)
- **Bramble protocols**: Handshake and Transport protocols provide forward secrecy
- **Published specification**: Fully open protocol documentation

### Security Verification

Client software independently audited; Tor network routing also audited.

**Available on**: Android (Google Play), Windows, Linux, Flathub

---

## Selection Criteria

### Minimum Requirements

| Requirement | Description |
|-------------|-------------|
| Open-source clients | Source code publicly available |
| No personal identifiers | No phone numbers or emails required for contacts |
| Default E2EE | End-to-end encryption for private messages by default |
| Universal E2EE | E2EE support for all messages |
| Forward secrecy | Key rotation to protect past messages |
| Independent audit | Published security audit from reputable third party |

### Best-Case Features

- Post-compromise security (future secrecy)
- Open-source servers
- Decentralized network (federated or P2P)
- E2EE for all messages by default
- Cross-platform support (Linux, macOS, Windows, Android, iOS)

---

## Quick Comparison

| Feature | Signal | Molly | SimpleX | Briar |
|---------|--------|-------|---------|-------|
| Phone number required | Optional | Optional | No | No |
| Decentralized | No | No | Yes | Yes (P2P) |
| Tor support | No | Yes | No | Yes |
| Offline messaging | No | No | No | Yes |
| Desktop support | Yes | No | Yes | Limited |
| Forward secrecy | Yes | Yes | Yes | Yes |

---

## Glossary

**Forward Secrecy**: Keys rotate frequently so that if the current encryption key is compromised, it does not expose past messages.

**Post-Compromise Security (Future Secrecy)**: Prevents attackers from decrypting future messages after compromising a private key, unless they compromise additional session keys. Forces attackers to intercept all communication continuously.