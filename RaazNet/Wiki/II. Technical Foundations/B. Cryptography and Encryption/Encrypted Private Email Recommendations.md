```yaml
---
title: "Encrypted Private Email Recommendations"
tags: [email, encryption, privacy, security, protonmail, tuta, mailbox]
category: "Email Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Security Professionals]
topics: ["Email Encryption", "Privacy Protection", "Secure Communication"]
summary: "Comprehensive guide to privacy-focused email providers with end-to-end encryption, comparing Proton Mail, Mailbox Mail, and Tuta."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of email", "Familiarity with encryption concepts"]
estimated_read_time: "15 minutes"
---
```

# Encrypted Private Email Services

Email is practically a necessity for using any online service, however it is not recommended for person-to-person conversations. For direct communication with others, consider using an instant messaging medium that supports forward secrecy.

## Recommended Providers Overview

The following email providers are recommended based on sustainable business models and built-in security and privacy features.

| Provider | OpenPGP / WKD | IMAP / SMTP | Zero-Access Encryption | Anonymous Payment |
| --- | --- | --- | --- | --- |
| Proton Mail | ✓ | Paid plans only | ✓ | Cash |
| Mailbox Mail | ✓ | ✓ | Mail only | Cash |
| Tuta | ✗ | ✗ | ✓ | Monero, Cash (via third party) |

Consider also using a dedicated [email aliasing service](https://www.privacyguides.org/en/email-aliasing/) to protect your privacy. These services help protect your real inbox from spam, prevent marketers from correlating your accounts, and can encrypt all incoming messages with PGP.

---

## OpenPGP Compatible Services

These providers natively support OpenPGP encryption/decryption and the Web Key Directory (WKD) standard, enabling provider-agnostic end-to-end encrypted emails.

> **Warning:** When using E2EE technology like OpenPGP, your email will still have some metadata that is not encrypted in the header, generally including the subject line. OpenPGP also does not support forward secrecy—if the private key of either sender or recipient is ever stolen, all previous messages encrypted with it will be exposed.

### Proton Mail

**Proton Mail** is an email service focused on privacy, encryption, security, and ease of use. Operating since 2013, Proton AG is based in Geneva, Switzerland.

- **Free Plan**: 500 MB storage (upgradeable to 1 GB free)
- **Website**: [proton.me/mail](https://proton.me/mail)
- **Onion Service**: Available
- **Apps**: Android, iOS, Windows, macOS, Linux, Web

#### Key Features

**Custom Domains and Aliases**
- Paid subscribers can use their own domain with catch-all addresses
- Supports sub-addressing for alias creation without purchasing a domain

**Private Payment Methods**
- Accepts cash by mail, credit/debit cards, Bitcoin, and PayPal

**Account Security**
- TOTP two-factor authentication
- Hardware security keys (FIDO2/U2F) supported (requires TOTP setup first)

**Data Security**
- Zero-access encryption at rest for emails and calendars
- Contact fields with zero-access encryption indicated by padlock icon

**Email Encryption**
- Integrated OpenPGP encryption in webmail
- Automatic encryption to other Proton Mail accounts
- WKD support for automatic external key discovery
- Password-protected emails for non-Proton recipients without OpenPGP

**Limitations**
- Free accounts cannot search body text
- Proton Mail Bridge (for desktop clients) requires paid plan
- Internal crash reports enabled by default (can be disabled in settings)

**Account Termination**
- Unpaid bills: data inaccessible after 14 days, delinquent after 30 days
- Inactive free accounts deleted after one year
- Deactivated email addresses cannot be reused

---

### Mailbox Mail

**Mailbox Mail** is a secure, ad-free email service powered by 100% eco-friendly energy. Operating since 2014, based in Berlin, Germany.

- **Starting Storage**: Up to 2 GB (upgradeable)
- **Website**: [mailbox.org](https://mailbox.org/)
- **Apps**: Web only

#### Key Features

**Custom Domains and Aliases**
- Supports custom domains with catch-all addresses
- Sub-addressing available

**Account Security**
- Two-factor authentication for webmail (TOTP or YubiKey via YubiCloud)
- WebAuthn not yet supported

**Data Security**
- Encrypted mailbox for incoming mail using your public key
- Note: Address book and calendar encryption not supported by underlying Open-Xchange platform

**Email Encryption**
- Integrated encryption in webmail for OpenPGP messages
- Remote recipients can decrypt emails on Mailbox servers
- WKD support for public key discovery

**Additional Features**
- IMAP/SMTP access via .onion service
- Encrypted cloud storage included
- @secure.mailbox.org alias enforces TLS encryption between mail servers
- Exchange ActiveSync support
- Digital legacy feature for all plans

**Account Termination**
- Account becomes restricted when contract ends
- Irrevocably deleted after 30 days

---

## Zero-Knowledge Encryption Providers

These providers store emails with zero-knowledge encryption but don't support interoperable encryption standards for E2EE communications between different providers.

### Tuta

**Tuta** (formerly Tutanota) is an email service focused on security and privacy through encryption. Operating since 2011, based in Hanover, Germany.

- **Free Plan**: 1 GB storage
- **Website**: [tuta.com](https://tuta.com/)
- **Apps**: Android, iOS, Windows, macOS, Linux, Web

#### Key Features

**Custom Domains and Aliases**
- 15-30 aliases depending on plan, unlimited on custom domains
- Catch-all supported with custom domains
- Sub-addressing (plus addresses) not supported

**Private Payment Methods**
- Credit cards and PayPal directly
- Cryptocurrency via gift cards through ProxyStore partnership

**Account Security**
- Two-factor authentication with TOTP or U2F

**Data Security**
- Zero-access encryption at rest for emails, address book contacts, and calendars

**Email Encryption**
- Does not use OpenPGP
- Encrypted emails from non-Tuta accounts only via temporary Tuta mailbox

**Limitations**
- No IMAP protocol support
- No third-party email client support
- Cannot add external email accounts
- Email import not currently supported
- Bulk email export may be inconvenient with many folders

**Account Termination**
- Inactive free accounts deleted after six months
- Deactivated free accounts can be reused if you pay

**Additional Features**
- Business version available free or discounted for non-profit organizations

---

## Selection Criteria

### Technology Requirements

**Minimum Requirements:**
- Zero-access encryption for email account data at rest
- Email export capability (Mbox or individual .EML with RFC5322 standard)
- Custom domain name support
- Operated on owned infrastructure (not third-party email service providers)

**Best Case:**
- Zero-access encryption for all account data (contacts, calendars, etc.)
- Integrated webmail E2EE/PGP encryption
- WKD support for OpenPGP key discovery
- Temporary mailbox support for external users
- Sub-addressing support
- Catch-all or alias functionality for custom domains
- Standard email access protocols (IMAP, SMTP, or JMAP)
- Onion service availability

### Privacy Requirements

**Minimum Requirements:**
- Sender IP address protection (filtered from `Received` header)
- No PII required beyond username and password
- GDPR-compliant privacy policy

**Best Case:**
- Anonymous payment options (cryptocurrency, cash, gift cards)
- Hosted in jurisdiction with strong email privacy protection laws

### Security Requirements

**Minimum Requirements:**
- Webmail protected with 2FA (TOTP)
- Zero-access encryption
- DNSSEC support
- No TLS errors or vulnerabilities
- Strong cipher suites with forward secrecy and authenticated encryption
- Valid MTA-STS and TLS-RPT policy
- Valid DANE records
- Valid SPF and DKIM records
- Proper DMARC record (policy set to `reject` or `quarantine`)
- TLS 1.2 or later with RFC8996 compliance plan
- SMTPS submission
- Message header viewing capability

**Best Case:**
- Hardware authentication (U2F, WebAuthn)
- DNS CAA Resource Record with DANE support
- Authenticated Received Chain (ARC) implementation
- Published third-party security audits
- Bug-bounty program or coordinated vulnerability disclosure

### Trust Requirements

**Minimum Requirements:**
- Public-facing leadership or ownership

**Best Case:**
- Frequent transparency reports

### Marketing Requirements

**Minimum Requirements:**
- Self-hosted analytics (no Google Analytics, Adobe Analytics, etc.)
- No irresponsible marketing practices (no reuse of personal information accessed without anonymity software, no browser fingerprinting)

**Best Case:**
- Clear documentation for 2FA setup, email clients, OpenPGP configuration