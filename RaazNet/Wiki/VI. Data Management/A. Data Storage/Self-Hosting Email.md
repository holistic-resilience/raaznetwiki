---
title: "Self-Hosting Email Servers"
tags: [email, self-hosting, privacy, security, mail-server]
category: "Self-Hosting"
difficulty: "Advanced"
audience: [System Administrators, Privacy-Conscious Users, Technical Users]
topics: ["Email Infrastructure", "Self-Hosting", "Privacy"]
summary: "Guide to self-hosted email server solutions including Stalwart, Mailcow, and Mail-in-a-Box"
source: "Privacy Guides"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Linux system administration", "Basic networking knowledge", "Domain management"]
estimated_read_time: "4 minutes"
---

# Email Servers

Self-hosting your own email server gives you complete control over your email data and privacy. This guide covers three recommended solutions for running your own mail server.

## Additional Resources

- [Setting up a mail server with OpenSMTPD, Dovecot and Rspamd](https://poolp.org/posts/2019-09-14/setting-up-a-mail-server-with-opensmtpd-dovecot-and-rspamd) (2019)
- [How To Run Your Own Mail Server](https://www.c0ffee.net/blog/mail-server-guide) (August 2017)

---

## Stalwart

**Stalwart** is a modern mail server written in Rust that supports JMAP in addition to standard IMAP, POP3, and SMTP protocols. It offers reasonable security defaults out of the box, making it easy to deploy immediately.

### Key Features

- Web-based administration with TOTP 2FA support
- PGP key integration to encrypt **all** incoming messages
- Wide variety of configuration options
- Zero-knowledge message storage capability

### PGP Implementation

Stalwart's [PGP implementation](https://stalw.art/docs/encryption/overview) is unique among self-hosted solutions. When combined with Web Key Directory (WKD) configuration and a compatible email client (like Thunderbird), it provides the easiest path to self-hosted E2EE compatibility with [Proton Mail](https://www.privacyguides.org/en/email/#proton-mail) users.

### Limitations

Stalwart does **not** include integrated webmail. You'll need to use a [dedicated email client](https://www.privacyguides.org/en/email-clients/) or self-host a webmail solution like Nextcloud's Mail app.

> **Note:** Privacy Guides uses Stalwart for their internal email.

**Links:** [Homepage](https://stalw.art/) | [Documentation](https://stalw.art/docs/get-started) | [Source Code](https://github.com/stalwartlabs)

---

## Mailcow

**Mailcow** is an advanced mail server solution ideal for users with Linux experience. It provides a complete email infrastructure in a Docker container.

### Included Components

- Mail server with DKIM support
- Antivirus and spam monitoring
- Webmail and ActiveSync via SOGo
- Web-based administration with 2FA support

**Links:** [Homepage](https://mailcow.email/) | [Documentation](https://docs.mailcow.email/) | [Source Code](https://github.com/mailcow/mailcow-dockerized)

---

## Mail-in-a-Box

**Mail-in-a-Box** is an automated setup script for deploying a mail server on Ubuntu. Its primary goal is simplifying mail server deployment for users who want their own server without extensive manual configuration.

**Links:** [Homepage](https://mailinabox.email/) | [Documentation](https://mailinabox.email/guide.html) | [Source Code](https://github.com/mail-in-a-box/mailinabox)

---

## Comparison Summary

| Feature | Stalwart | Mailcow | Mail-in-a-Box |
|---------|----------|---------|---------------|
| Language/Platform | Rust | Docker | Ubuntu Script |
| Built-in Webmail | No | Yes (SOGo) | Yes |
| PGP Encryption | Yes | No | No |
| 2FA Admin | Yes | Yes | Limited |
| Ease of Setup | Moderate | Moderate | Easy |