---
title: "Self-Hosting Email Servers"
tags: [self-hosting, email, privacy, security, mail-server]
category: "Self-Hosting"
difficulty: "Advanced"
audience: [System Administrators, Privacy-Conscious Users, Technical Users]
topics: ["Email Infrastructure", "Self-Hosting", "Privacy"]
summary: "Guide to self-hosted email server solutions including Stalwart, Mailcow, and Mail-in-a-Box"
source: "Privacy Guides"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Linux administration", "DNS configuration", "Basic networking knowledge"]
estimated_read_time: "4 minutes"
---

# Email Servers

Self-hosting your own email server gives you complete control over your communications and eliminates reliance on third-party service providers. This guide covers three recommended solutions for running your own mail server.

## Additional Resources

- [Setting up a mail server with OpenSMTPD, Dovecot and Rspamd](https://poolp.org/posts/2019-09-14/setting-up-a-mail-server-with-opensmtpd-dovecot-and-rspamd) (2019)
- [How To Run Your Own Mail Server](https://www.c0ffee.net/blog/mail-server-guide) (August 2017)

---

## Stalwart

**Stalwart** is a modern mail server written in Rust that supports JMAP in addition to standard IMAP, POP3, and SMTP protocols. It features sensible security defaults and is easy to deploy immediately.

**Key Features:**
- Web-based administration with TOTP 2FA support
- PGP key integration to encrypt all incoming messages
- Wide variety of configuration options with secure defaults

**Links:** [Homepage](https://stalw.art/) | [Documentation](https://stalw.art/docs/get-started) | [Source Code](https://github.com/stalwartlabs)

### PGP Implementation

Stalwart's [PGP implementation](https://stalw.art/docs/encryption/overview) is unique among self-hosted solutions, enabling zero-knowledge message storage. When combined with Web Key Directory (WKD) configuration and a PGP-compatible email client like Thunderbird, this provides the easiest path to self-hosted E2EE compatibility with [Proton Mail](https://www.privacyguides.org/en/email/#proton-mail) users.

> **Note:** Stalwart does not include integrated webmail. You'll need a [dedicated email client](https://www.privacyguides.org/en/email-clients/) or self-hosted webmail solution like Nextcloud's Mail app.

---

## Mailcow

**Mailcow** is a comprehensive mail server solution ideal for users with Linux experience. It runs entirely in Docker containers.

**Included Components:**
- Mail server with DKIM support
- Antivirus and spam monitoring
- SOGo webmail with ActiveSync
- Web-based administration with 2FA support

**Links:** [Homepage](https://mailcow.email/) | [Documentation](https://docs.mailcow.email/) | [Source Code](https://github.com/mailcow/mailcow-dockerized)

---

## Mail-in-a-Box

**Mail-in-a-Box** is an automated setup script for deploying a mail server on Ubuntu. It's designed to simplify the process of setting up a personal mail server.

**Links:** [Homepage](https://mailinabox.email/) | [Documentation](https://mailinabox.email/guide.html) | [Source Code](https://github.com/mail-in-a-box/mailinabox)

---

## Comparison Summary

| Feature | Stalwart | Mailcow | Mail-in-a-Box |
|---------|----------|---------|---------------|
| **Complexity** | Moderate | Advanced | Beginner-friendly |
| **Webmail** | No (external required) | Yes (SOGo) | Yes |
| **PGP Encryption** | Built-in | No | No |
| **Deployment** | Various | Docker | Ubuntu script |
| **2FA Admin** | Yes (TOTP) | Yes | Limited |