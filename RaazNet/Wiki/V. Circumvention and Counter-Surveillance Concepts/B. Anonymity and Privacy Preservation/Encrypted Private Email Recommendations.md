```yaml
---
title: "Encrypted Private Email Provider Recommendations"
tags: [email, privacy, encryption, security, openpgp, zero-knowledge]
category: "Email Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Professionals, General Public]
topics: ["Email Privacy", "End-to-End Encryption", "Digital Security"]
summary: "Comprehensive guide to privacy-focused email providers with encryption, security features, and selection criteria."
source: "Privacy Guides"
content_type: "Reference Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic email usage", "Understanding of encryption concepts"]
estimated_read_time: "15 minutes"
---
```

# Encrypted Private Email Provider Recommendations

Email is practically a necessity for using any online service, however it is not recommended for person-to-person conversations due to inherent metadata exposure. For private communications, consider using an [instant messaging medium](https://www.privacyguides.org/en/real-time-communication/) that supports forward secrecy.

For general email needs, this guide recommends privacy-focused providers based on sustainable business models and built-in security and privacy features.

## Recommended Providers Overview

| Provider | OpenPGP / WKD | IMAP / SMTP | Zero-Access Encryption | Anonymous Payment |
| --- | --- | --- | --- | --- |
| [Proton Mail](#proton-mail) | ✓ | Paid plans only | ✓ | Cash |
| [Mailbox Mail](#mailbox-mail) | ✓ | ✓ | Mail only | Cash |
| [Tuta](#tuta) | ✗ | ✗ | ✓ | Monero, Cash (via third party) |

> **Tip:** Consider using a dedicated [email aliasing service](https://www.privacyguides.org/en/email-aliasing/) to protect your real inbox from spam, prevent marketers from correlating your accounts, and encrypt incoming messages with PGP.

---

## OpenPGP Compatible Services

These providers natively support OpenPGP encryption/decryption and the [Web Key Directory (WKD) standard](https://www.privacyguides.org/en/basics/email-security/#what-is-the-web-key-directory-standard), enabling provider-agnostic end-to-end encrypted emails.

> **Warning:** When using E2EE technology like OpenPGP, email metadata (including subject lines) remains unencrypted. OpenPGP also does not support forward secrecy—if a private key is compromised, all previous messages encrypted with it become exposed.

### Proton Mail

**Proton Mail** is an email service focused on privacy, encryption, security, and ease of use. Operating since 2013, Proton AG is based in Geneva, Switzerland.

- **Free Plan:** 500 MB storage (upgradeable to 1 GB)
- **Security Audit:** Letter of attestation provided November 9, 2021 by [Securitum](https://research.securitum.com/)

**Links:** [Homepage](https://proton.me/mail) | [Onion Service](https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion/) | [Privacy Policy](https://proton.me/mail/privacy-policy) | [Source Code](https://github.com/ProtonMail)

#### Key Features

| Feature | Details |
| --- | --- |
| **Custom Domains** | Supported with paid plans; includes catch-all and sub-addressing |
| **Payment Methods** | Credit/debit, Bitcoin, PayPal, **cash by mail** |
| **2FA Support** | TOTP and hardware security keys (FIDO2/U2F) |
| **Zero-Access Encryption** | Emails and calendars encrypted at rest |
| **OpenPGP Integration** | Built-in webmail encryption with automatic WKD key discovery |

#### Limitations

- Free accounts cannot search body text or use Proton Mail Bridge (required for desktop email clients)
- Internal crash reports enabled by default (can be disabled in settings)

#### Account Policies

- **Unpaid bills:** Account restricted after 14 days, delinquent after 30 days
- **Inactive free accounts:** Deleted after one year
- **Email reuse:** Deactivated account addresses cannot be reused

---

### Mailbox Mail

**Mailbox Mail** is a secure, ad-free email service powered by 100% eco-friendly energy. Operating since 2014, based in Berlin, Germany.

- **Starting Storage:** Up to 2 GB (upgradeable)

**Links:** [Homepage](https://mailbox.org/) | [Privacy Policy](https://mailbox.org/en/data-protection-privacy-policy) | [Documentation](https://kb.mailbox.org/en/private)

#### Key Features

| Feature | Details |
| --- | --- |
| **Custom Domains** | Supported with catch-all and sub-addressing |
| **Payment Methods** | Standard methods plus **cash** |
| **2FA Support** | TOTP and YubiKey (via YubiCloud); WebAuthn not yet supported |
| **Encrypted Mailbox** | Incoming mail encrypted with your public key |
| **OpenPGP Integration** | Built-in Guard encryption with WKD support |

#### Additional Features

- **.onion service** for IMAP/SMTP access (webmail not available via Tor)
- **Encrypted cloud storage** included with all accounts
- **@secure.mailbox.org alias** enforces TLS encryption between mail servers
- **Digital legacy feature** for data inheritance
- **Exchange ActiveSync** support

#### Limitations

- Address book and calendar encryption not supported (Open-Xchange platform limitation)
- TLS certificate errors may occur with .onion service

#### Account Policies

- **Contract end:** Account set to restricted status, irrevocably deleted after 30 days

---

## Zero-Knowledge Encryption Providers

These providers store emails with zero-knowledge encryption but don't support interoperable E2EE standards (like OpenPGP) for cross-provider communications.

### Tuta

**Tuta** (formerly Tutanota) is an email service focused on security and privacy through encryption. Operating since 2011, based in Hanover, Germany.

- **Free Plan:** 1 GB storage

**Links:** [Homepage](https://tuta.com/) | [Privacy Policy](https://tuta.com/privacy) | [Source Code](https://github.com/tutao/tutanota)

#### Key Features

| Feature | Details |
| --- | --- |
| **Custom Domains** | Supported; 15-30 aliases depending on plan |
| **Payment Methods** | Credit cards, PayPal; **cryptocurrency via ProxyStore gift cards** |
| **2FA Support** | TOTP and U2F |
| **Zero-Access Encryption** | Emails, contacts, and calendars encrypted at rest |
| **External Encryption** | Temporary encrypted mailbox for non-Tuta recipients |

#### Limitations

- **No IMAP support** or third-party email clients
- **No OpenPGP support**
- No sub-addressing (plus addresses)
- Email import not currently supported
- Bulk export can be inconvenient with many folders

#### Account Policies

- **Inactive free accounts:** Deleted after six months (can be reactivated with payment)

#### Additional

- **Non-profit discount:** Business version available free or heavily discounted for non-profits

---

## Selection Criteria

### Technology Requirements

**Minimum Requirements:**
- Zero-access encryption at rest for email data
- Email export capability (Mbox or .EML with RFC5322)
- Custom domain support
- Self-owned infrastructure (not built on third-party providers)

**Best Case:**
- Zero-access encryption for all account data (contacts, calendars)
- Integrated webmail E2EE/PGP encryption
- WKD support for OpenPGP key discovery
- Temporary mailbox for external encrypted emails
- Sub-addressing support
- Standard protocols (IMAP, SMTP, JMAP)
- Onion service availability

### Privacy Requirements

**Minimum Requirements:**
- Sender IP protection (filtered from `Received` header)
- No PII required beyond username and password
- GDPR-compliant privacy policy

**Best Case:**
- Anonymous payment options (cryptocurrency, cash, gift cards)
- Hosted in jurisdiction with strong email privacy laws

### Security Requirements

**Minimum Requirements:**
- 2FA protection (TOTP) for webmail
- Zero-access encryption
- DNSSEC support
- No TLS errors or vulnerabilities
- Strong cipher suites with forward secrecy
- Valid MTA-STS, TLS-RPT, DANE, SPF, DKIM records
- Proper DMARC policy (reject or quarantine)
- TLS 1.2+ with RFC8996 compliance plan
- SMTPS submission
- Message header viewing capability

**Best Case:**
- Hardware authentication (U2F, WebAuthn)
- DNS CAA Resource Record
- Authenticated Received Chain (ARC) implementation
- Third-party security audits
- Bug bounty program

### Trust & Transparency

**Minimum Requirements:**
- Public-facing leadership or ownership

**Best Case:**
- Frequent transparency reports

### Marketing Standards

**Minimum Requirements:**
- Self-hosted analytics (no Google Analytics, Adobe Analytics)
- No irresponsible marketing practices (fingerprinting, unauthorized data reuse)

**Best Case:**
- Clear documentation for 2FA setup, email clients, OpenPGP configuration

---

## Additional Resources

- [Email Aliasing Services](https://www.privacyguides.org/en/email-aliasing/)
- [Email Security Basics](https://www.privacyguides.org/en/basics/email-security/)
- [Recommended Email Clients](https://www.privacyguides.org/en/email-clients/)
- [Multi-Factor Authentication Guide](https://www.privacyguides.org/en/basics/multi-factor-authentication/)