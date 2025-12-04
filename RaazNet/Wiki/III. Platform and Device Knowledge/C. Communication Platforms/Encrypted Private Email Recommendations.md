```yaml
---
title: "Encrypted Private Email Recommendations"
tags: [email, privacy, encryption, security, proton-mail, tuta, mailbox]
category: "Email Services"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Professionals, General Public]
topics: ["Email Security", "Privacy Protection", "Encryption", "Digital Communication"]
summary: "Comprehensive guide to privacy-focused email providers featuring zero-access encryption, OpenPGP support, and anonymous payment options."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic email concepts", "Understanding of encryption basics"]
estimated_read_time: "12 minutes"
---
```

# Encrypted Private Email Services

Email is practically a necessity for using any online service, however it is not recommended for person-to-person conversations. Rather than using email to contact other people, consider using an instant messaging medium that supports forward secrecy.

## Recommended Providers Overview

The following email providers are recommended based on sustainable business models and built-in security and privacy features.

| Provider | OpenPGP / WKD | IMAP / SMTP | Zero-Access Encryption | Anonymous Payment |
| --- | --- | --- | --- | --- |
| Proton Mail | ✓ | Paid plans only | ✓ | Cash |
| Mailbox Mail | ✓ | ✓ | Mail only | Cash |
| Tuta | ✗ | ✗ | ✓ | Monero, Cash via third party |

Consider also using a dedicated [email aliasing service](https://www.privacyguides.org/en/email-aliasing/) to protect your privacy. These services help protect your real inbox from spam, prevent marketers from correlating your accounts, and can encrypt all incoming messages with PGP.

---

## OpenPGP Compatible Services

These providers natively support OpenPGP encryption/decryption and the Web Key Directory (WKD) standard, allowing for provider-agnostic end-to-end encrypted emails.

> **Warning:** When using E2EE technology like OpenPGP, your email will still have some metadata that is not encrypted in the header, generally including the subject line. OpenPGP also does not support forward secrecy—if the private key of either you or the recipient is ever stolen, all previous messages encrypted with it will be exposed.

### Proton Mail

**Proton Mail** is an email service with a focus on privacy, encryption, security, and ease of use. Operating since 2013, Proton AG is based in Geneva, Switzerland.

- **Free plan:** 500 MB storage (upgradable to 1 GB free)
- **Website:** [proton.me/mail](https://proton.me/mail)
- **Onion Service:** Available
- **Platforms:** Web, Android, iOS, Windows, macOS, Linux

#### Key Features

**Custom Domains and Aliases**
- Paid subscribers can use their own domain with catch-all address support
- Sub-addressing supported for users without custom domains

**Private Payment Methods**
- Accepts cash by mail, credit/debit cards, Bitcoin, and PayPal

**Account Security**
- TOTP two-factor authentication
- Hardware security keys (FIDO2/U2F) — requires TOTP setup first

**Data Security**
- Zero-access encryption at rest for emails and calendars
- Some Proton Contacts fields (display names, email addresses) are not zero-access encrypted
- Fields supporting zero-access encryption are indicated with a padlock icon

**Email Encryption**
- Integrated OpenPGP encryption in webmail
- Automatic encryption to other Proton Mail accounts
- Automatic external key discovery with WKD
- Password-protected emails for non-Proton recipients without OpenPGP
- Public keys published via HTTP from WKD (for `@proton.me` domains)

**Account Termination**
- Unpaid bills after 14 days: cannot access data
- After 30 days: account becomes delinquent, no incoming mail
- Inactive free accounts deleted after one year
- Deactivated email addresses cannot be reused

**Additional Features**
- Unlimited plan includes access to other Proton services
- Multiple custom domains, unlimited hide-my-email aliases, 500 GB storage
- SimpleLogin Premium included with Proton Unlimited or multi-user plans
- Security audit attestation provided November 9, 2021 by Securitum
- Internal crash reports (can be disabled in settings)

---

### Mailbox Mail

**Mailbox Mail** is an email service focused on security, ad-free experience, and 100% eco-friendly energy. Operating since 2014, based in Berlin, Germany.

- **Starting storage:** Up to 2 GB (upgradable)
- **Website:** [mailbox.org](https://mailbox.org/)
- **Platforms:** Web

#### Key Features

**Custom Domains and Aliases**
- Custom domain support with catch-all addresses
- Sub-addressing supported

**Account Security**
- Two-factor authentication for webmail only (TOTP or YubiKey via YubiCloud)
- WebAuthn not yet supported

**Data Security**
- Encrypted mailbox for incoming mail using your public key
- Address book and calendar encryption not supported (Open-Xchange platform limitation)

**Email Encryption**
- Integrated encryption in webmail for OpenPGP messages
- Remote recipients can decrypt emails on Mailbox Mail servers
- Public key discovery via HTTP from WKD (for `@mailbox.org` domains)

**Account Termination**
- Account set to restricted status when contract ends
- Irrevocably deleted after 30 days

**Additional Features**
- IMAP/SMTP access via .onion service (webmail not available via .onion)
- Limited cloud storage with encryption option
- `@secure.mailbox.org` alias enforces TLS encryption between mail servers
- Exchange ActiveSync support
- Digital legacy feature for all plans

---

## Zero-Knowledge Encryption Providers

These providers store emails with zero-knowledge encryption but don't support interoperable encryption standards for E2EE communications between different providers.

### Tuta

**Tuta** (formerly Tutanota) is an email service focused on security and privacy through encryption. Operating since 2011, based in Hanover, Germany.

- **Free plan:** 1 GB storage
- **Website:** [tuta.com](https://tuta.com/)
- **Platforms:** Web, Android, iOS, Windows, macOS, Linux
- **Source Code:** Open source on GitHub

#### Limitations

- No IMAP protocol support
- No third-party email client support
- Cannot add external email accounts
- Email import not currently supported (planned feature)
- Emails must be exported individually or by bulk selection per folder

#### Key Features

**Custom Domains and Aliases**
- 15 or 30 aliases depending on plan
- Unlimited aliases on custom domains
- Catch-all supported with custom domain
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

**Account Termination**
- Inactive free accounts deleted after six months
- Deactivated free accounts can be reused if you pay

**Additional Features**
- Business version available free or heavily discounted for non-profit organizations

---

## Selection Criteria

### Technology Requirements

**Minimum Requirements:**
- Zero-access encryption for email account data at rest
- Export capability as Mbox or individual .EML (RFC5322 standard)
- Custom domain name support
- Operated on owned infrastructure (not third-party providers)

**Best Case:**
- Zero-access encryption for all account data (contacts, calendars)
- Integrated webmail E2EE/PGP encryption
- WKD support for OpenPGP key discovery
- Temporary mailbox support for external users
- Sub-addressing support
- Catch-all or alias functionality
- Standard email access protocols (IMAP, SMTP, JMAP)
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
- 2FA protection for webmail (TOTP)
- Zero-access encryption
- DNSSEC support
- No TLS errors or vulnerabilities
- Strong cipher suites with forward secrecy and authenticated encryption
- Valid MTA-STS and TLS-RPT policy
- Valid DANE records
- Valid SPF and DKIM records
- Proper DMARC record (policy: `reject` or `quarantine`) or ARC
- TLS 1.2 or later with RFC8996 compliance plan
- SMTPS submission
- Message header viewing capability

**Best Case:**
- Hardware authentication (U2F, WebAuthn)
- DNS CAA Resource Record with DANE support
- Authenticated Received Chain (ARC) implementation
- Published third-party security audits
- Bug-bounty programs or coordinated vulnerability disclosure

### Trust Requirements

**Minimum Requirements:**
- Public-facing leadership or ownership

**Best Case:**
- Frequent transparency reports

### Marketing Requirements

**Minimum Requirements:**
- Self-hosted analytics (no Google Analytics, Adobe Analytics)
- No irresponsible marketing practices

**Best Case:**
- Clear documentation for 2FA setup, email clients, OpenPGP configuration