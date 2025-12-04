```yaml
---
title: "Encrypted Private Email Recommendations"
tags: [email, encryption, privacy, security, proton-mail, tuta, mailbox]
category: "Email Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Security Professionals]
topics: ["Email Privacy", "End-to-End Encryption", "Secure Communication", "Digital Security"]
summary: "Comprehensive guide to privacy-focused email providers with zero-access encryption, OpenPGP support, and detailed selection criteria."
source: "Privacy Guides"
content_type: "Reference Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic email usage", "Understanding of encryption concepts"]
estimated_read_time: "15 minutes"
---
```

# Encrypted Private Email Services

Email is practically a necessity for using any online service. However, it is not recommended for person-to-person conversations due to inherent security limitations. For direct communication, consider using an [instant messaging service](https://www.privacyguides.org/en/real-time-communication/) that supports forward secrecy.

For other email needs, this guide recommends providers based on sustainable business models and built-in security and privacy features.

---

## Recommended Providers Overview

| Provider | OpenPGP / WKD | IMAP / SMTP | Zero-Access Encryption | Anonymous Payment |
|----------|---------------|-------------|------------------------|-------------------|
| [Proton Mail](#proton-mail) | ✓ | Paid plans only | ✓ | Cash |
| [Mailbox Mail](#mailbox-mail) | ✓ | ✓ | Mail only | Cash |
| [Tuta](#tuta) | ✗ | ✗ | ✓ | Monero, Cash (via third party) |

> **Tip:** Consider pairing an email provider with a dedicated [email aliasing service](https://www.privacyguides.org/en/email-aliasing/) to protect your real inbox from spam, prevent marketers from correlating your accounts, and encrypt incoming messages with PGP.

---

## OpenPGP Compatible Services

These providers natively support OpenPGP encryption/decryption and the [Web Key Directory (WKD) standard](https://www.privacyguides.org/en/basics/email-security/#what-is-the-web-key-directory-standard), enabling provider-agnostic end-to-end encrypted emails.

> **Warning:** When using E2EE technology like OpenPGP, some metadata (including subject lines) remains unencrypted in the email header. Additionally, OpenPGP does not support forward secrecy—if a private key is compromised, all previous messages encrypted with it become exposed. Learn more about [protecting private keys](https://www.privacyguides.org/en/basics/email-security/#how-do-i-protect-my-private-keys).

### Proton Mail

**Proton Mail** is an email service focused on privacy, encryption, security, and ease of use. Operating since 2013, Proton AG is based in Geneva, Switzerland.

- **Free Plan:** 500 MB storage (expandable to 1 GB)
- **Links:** [Homepage](https://proton.me/mail) | [Onion Service](https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion/) | [Privacy Policy](https://proton.me/mail/privacy-policy) | [Source Code](https://github.com/ProtonMail)
- **Apps:** Web, iOS, Android, Windows, macOS, Linux (via Bridge)

#### Key Features

| Feature | Details |
|---------|---------|
| **Custom Domains** | Supported on paid plans with [catch-all](https://proton.me/support/catch-all) and [sub-addressing](https://proton.me/support/creating-aliases) |
| **Payment Methods** | Credit/debit, Bitcoin, PayPal, **cash by mail** |
| **Two-Factor Auth** | TOTP and hardware security keys (FIDO2/U2F) |
| **Zero-Access Encryption** | Emails and calendars encrypted at rest |
| **OpenPGP Integration** | Built-in encryption with automatic WKD key discovery |

#### Limitations

- Free accounts cannot search body text or use [Proton Mail Bridge](https://proton.me/mail/bridge) (required for desktop email clients)
- Internal crash reports enabled by default (can be disabled in settings)

#### Account Policies

- **Unpaid bills:** Account restricted after 14 days, delinquent after 30 days
- **Inactive free accounts:** Deleted after one year
- **Email reuse:** Deactivated email addresses cannot be reused

#### Security Audit

A [letter of attestation](https://proton.me/blog/security-audit-all-proton-apps) was provided for Proton Mail's apps on November 9, 2021 by [Securitum](https://research.securitum.com/).

---

### Mailbox Mail

**Mailbox Mail** is a secure, ad-free email service powered by 100% eco-friendly energy. Operating since 2014, it is based in Berlin, Germany.

- **Starting Storage:** Up to 2 GB (upgradable)
- **Links:** [Homepage](https://mailbox.org/) | [Privacy Policy](https://mailbox.org/en/data-protection-privacy-policy) | [Documentation](https://kb.mailbox.org/en/private)
- **Apps:** Web only

#### Key Features

| Feature | Details |
|---------|---------|
| **Custom Domains** | Supported with [catch-all](https://kb.mailbox.org/en/private/custom-domains/how-to-set-up-a-catch-all-alias-with-a-custom-domain-name) and [sub-addressing](https://kb.mailbox.org/en/private/account-article/what-is-an-alias-and-how-do-i-use-it) |
| **Two-Factor Auth** | TOTP or YubiKey (webmail only; WebAuthn not yet supported) |
| **Encrypted Mailbox** | Incoming mail encrypted with your public key |
| **OpenPGP Integration** | [Built-in encryption](https://kb.mailbox.org/en/private/e-mail-article/send-encrypted-e-mails-with-guard) with WKD support |
| **IMAP/SMTP Access** | Full support, including via [.onion service](https://kb.mailbox.org/en/private/faq-article/the-tor-exit-node-of-mailbox-org) |

#### Limitations

- Address book and calendar encryption not supported (Open-Xchange platform limitation)
- Webmail not accessible via .onion service

#### Additional Features

- **Encrypted cloud storage** included with all accounts
- **[@secure.mailbox.org](https://kb.mailbox.org/en/private/e-mail-article/ensuring-e-mails-are-sent-securely)** alias enforces TLS encryption between mail servers
- **Digital legacy feature** for designating data inheritance
- **Exchange ActiveSync** support

#### Account Termination

Accounts become restricted when contracts end and are irrevocably deleted after [30 days](https://kb.mailbox.org/en/private/payment-article/what-happens-at-the-end-of-my-contract).

---

## Zero-Knowledge Providers (Non-OpenPGP)

These providers use zero-knowledge encryption for stored emails but don't support interoperable E2EE standards for cross-provider communication.

### Tuta

**Tuta** (formerly Tutanota) focuses on security and privacy through encryption. Operating since 2011, it is based in Hanover, Germany.

- **Free Plan:** 1 GB storage
- **Links:** [Homepage](https://tuta.com/) | [Privacy Policy](https://tuta.com/privacy) | [Source Code](https://github.com/tutao/tutanota)
- **Apps:** Web, iOS, Android, Windows, macOS, Linux

#### Key Features

| Feature | Details |
|---------|---------|
| **Custom Domains** | Supported on paid plans with [catch-all](https://tuta.com/support#settings-global) |
| **Aliases** | 15-30 depending on plan; unlimited on custom domains |
| **Payment Methods** | Credit card, PayPal, **cryptocurrency via [ProxyStore](https://tuta.com/support/#cryptocurrency)** |
| **Two-Factor Auth** | TOTP and U2F |
| **Zero-Access Encryption** | Emails, contacts, and calendars |

#### Limitations

- **No IMAP support** or third-party email clients
- **No external email accounts** can be added
- **No OpenPGP support**—uses proprietary encryption
- Email import not currently supported (planned feature)
- [Sub-addressing not supported](https://tuta.com/support#plus)

#### Cross-Provider Encryption

Tuta accounts can only receive encrypted emails from non-Tuta accounts via a [temporary Tuta mailbox](https://tuta.com/support/#encrypted-email-external).

#### Account Policies

- **Inactive free accounts:** Deleted after six months (can be reactivated with payment)
- **Non-profit pricing:** [Discounted or free](https://tuta.com/blog/secure-email-for-non-profit) for qualifying organizations

---

## Selection Criteria

### Technology Requirements

**Minimum:**
- Zero-access encryption at rest
- Email export capability (Mbox or .EML with RFC5322)
- Custom domain support
- Self-operated infrastructure

**Best Case:**
- Full account data encryption (contacts, calendars)
- Integrated webmail E2EE/PGP
- WKD support for OpenPGP key discovery
- Temporary mailbox for external recipients
- Sub-addressing support
- Standard protocols (IMAP, SMTP, JMAP)
- Onion service availability

### Privacy Requirements

**Minimum:**
- Sender IP protection (filtered from headers)
- No PII required beyond username/password
- GDPR-compliant privacy policy

**Best Case:**
- Anonymous payment options
- Jurisdiction with strong email privacy laws

### Security Requirements

**Minimum:**
- 2FA for webmail (TOTP)
- Zero-access encryption
- DNSSEC support
- No TLS vulnerabilities
- Valid MTA-STS, TLS-RPT, DANE, SPF, DKIM, DMARC records
- TLS 1.2+ with forward secrecy
- SMTPS submission
- Message header viewing capability

**Best Case:**
- Hardware authentication (U2F/WebAuthn)
- DNS CAA records
- ARC implementation
- Third-party security audits
- Bug bounty program

### Trust & Transparency

**Minimum:**
- Public-facing leadership or ownership

**Best Case:**
- Frequent transparency reports

### Marketing Standards

**Minimum:**
- Self-hosted analytics (no Google Analytics, etc.)
- No irresponsible marketing practices (fingerprinting, tracking without consent)

**Best Case:**
- Clear documentation for 2FA setup, email clients, OpenPGP configuration

---

## Summary

| Provider | Best For | Key Advantage | Main Limitation |
|----------|----------|---------------|-----------------|
| **Proton Mail** | General privacy users | Comprehensive ecosystem, OpenPGP | Free tier limitations |
| **Mailbox Mail** | Technical users | Full IMAP/SMTP, eco-friendly | No calendar/contact encryption |
| **Tuta** | Maximum simplicity | Full zero-access encryption | No standard protocols or OpenPGP |