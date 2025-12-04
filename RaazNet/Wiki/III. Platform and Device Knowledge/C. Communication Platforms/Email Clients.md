```yaml
---
title: "Email Clients"
tags: [email, privacy, encryption, openpgp, security, open-source]
category: "Email Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, General Public, Security Enthusiasts]
topics: ["Email Privacy", "Encryption", "Secure Communication"]
summary: "Guide to privacy-focused email clients supporting OpenPGP encryption and strong authentication across multiple platforms."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic email usage", "Understanding of encryption concepts"]
estimated_read_time: "8 minutes"
---
```

# Email Clients

The **email clients** recommended here support both [OpenPGP](https://www.privacyguides.org/en/encryption/#openpgp) and strong authentication such as [Open Authorization (OAuth)](https://www.privacyguides.org/en/basics/account-creation/#sign-in-with-oauth). OAuth allows you to use [Multi-Factor Authentication](https://www.privacyguides.org/en/basics/multi-factor-authentication/) to prevent account theft.

> [!warning] Email Does Not Provide Forward Secrecy
> When using end-to-end encryption (E2EE) technology like OpenPGP, email will still have [some metadata](https://www.privacyguides.org/en/basics/email-security/#email-metadata-overview) that is not encrypted in the header of the email.
> 
> OpenPGP also does not support [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy), which means if either your or the recipient's private key is ever stolen, all previous messages encrypted with it will be exposed. Consider using a medium that provides forward secrecy for sensitive communications, such as [real-time communication tools](https://www.privacyguides.org/en/real-time-communication/).

---

## Cross-Platform

### Thunderbird

**Thunderbird** is a free, open-source, cross-platform email, newsgroup, news feed, and chat (XMPP, IRC, Matrix) client developed by the Thunderbird community.

- **Homepage:** [thunderbird.net](https://thunderbird.net/)
- **Source Code:** [hg.mozilla.org/comm-central](https://hg.mozilla.org/comm-central)
- **Available on:** Windows, macOS, Linux, Android (Google Play, GitHub)

> [!note] Mobile Reply Warning
> When replying to someone on a mailing list in Thunderbird Mobile, the "reply" option may also include the mailing list. See [thunderbird-android #3738](https://github.com/thunderbird/thunderbird-android/issues/3738) for details.

#### Recommended Configuration

To enhance privacy in Thunderbird Desktop, navigate to **Settings → Privacy & Security**:

**Web Content:**
- Uncheck "Remember websites and links I've visited"
- Uncheck "Accept cookies from sites"

**Telemetry:**
- Uncheck "Allow Thunderbird to send technical and interaction data to Mozilla"

#### Advanced: thunderbird-user.js

[`thunderbird-user.js`](https://github.com/HorlogeSkynet/thunderbird-user.js) is a configuration set that disables web-browsing features within Thunderbird Desktop to reduce attack surface and maintain privacy. Some changes are backported from the [Arkenfox project](https://www.privacyguides.org/en/desktop-browsers/#arkenfox-advanced).

---

## Platform-Specific Clients

### Apple Mail (macOS/iOS)

**Apple Mail** is included in macOS and can be extended with [GPG Suite](https://www.privacyguides.org/en/encryption/#gpg-suite) for OpenPGP support.

- **Homepage:** [Apple Mail Guide](https://support.apple.com/guide/mail/welcome/mac)

**Privacy Features:**
- Load remote content in the background or block it entirely
- Hide your IP address from senders on [macOS](https://support.apple.com/guide/mail/mlhl03be2866/mac) and [iOS](https://support.apple.com/guide/iphone/iphf084865c7/ios)

> [!note] macOS Sonoma Users
> GPG Suite does [not yet](https://gpgtools.com/sonoma) have a stable release for macOS Sonoma.

### FairEmail (Android)

**FairEmail** is a minimal, open-source email app using open standards (IMAP, SMTP, OpenPGP) with minimal data and battery usage.

- **Homepage:** [email.faircode.eu](https://email.faircode.eu/)
- **Source Code:** [GitHub](https://github.com/M66B/FairEmail)
- **Available on:** Google Play, GitHub

### GNOME Evolution (Linux - GNOME)

**Evolution** is a personal information management application providing integrated mail, calendaring, and address book functionality.

- **Homepage:** [GNOME Evolution](https://wiki.gnome.org/Apps/Evolution)
- **Source Code:** [GitLab](https://gitlab.gnome.org/GNOME/evolution)
- **Available on:** Flathub

### Kontact (Linux - KDE)

**Kontact** is a personal information manager from the [KDE](https://kde.org/) project, providing a mail client, address book, RSS client, and organizer.

- **Homepage:** [kontact.kde.org](https://kontact.kde.org/)
- **Source Code:** [KDE Invent](https://invent.kde.org/pim/kmail)
- **Available on:** Native Linux packages, Flathub

### Mailvelope (Browser Extension)

**Mailvelope** is a browser extension enabling encrypted email exchange following the OpenPGP standard, useful for webmail users.

- **Homepage:** [mailvelope.com](https://mailvelope.com/)
- **Source Code:** [GitHub](https://github.com/mailvelope/mailvelope)
- **Available on:** Firefox, Chrome, Edge

### NeoMutt (CLI)

**NeoMutt** is an open-source command-line email reader for Linux and BSD, forked from [Mutt](https://en.wikipedia.org/wiki/Mutt_(email_client)) with added features.

- **Homepage:** [neomutt.org](https://neomutt.org/)
- **Source Code:** [GitHub](https://github.com/neomutt/neomutt)
- **Available on:** macOS, Linux

> [!note]
> NeoMutt is a text-based client with a steep learning curve but is highly customizable.

---

## Selection Criteria

### Minimum Qualifications

- Apps for open-source operating systems must be open source
- Must not collect telemetry, or provide an easy way to disable all telemetry
- Must support OpenPGP message encryption

### Best-Case Criteria

- Should be open source
- Should be cross-platform
- Should not collect any telemetry by default
- Should support OpenPGP natively (without extensions)
- Should support storing OpenPGP encrypted emails locally