---
title: "Self-Hosting Email Servers"
tags: [self-hosting, email, privacy, security, mail-server]
category: "Self-Hosting"
difficulty: "Advanced"
audience: [System Administrators, Privacy-Conscious Users, Technical Users]
topics: ["Email Infrastructure", "Self-Hosting", "Privacy", "Server Administration"]
summary: "Guide to self-hosting email servers with recommendations for Stalwart, Mailcow, and Mail-in-a-Box solutions."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Linux administration experience", "Basic networking knowledge", "Domain ownership", "Server access"]
estimated_read_time: "4 minutes"
---

# Email Servers

Self-hosting your own email server gives you complete control over your email data and privacy. This guide covers recommended mail server solutions for various experience levels.

## Additional Resources

- [Setting up a mail server with OpenSMTPD, Dovecot and Rspamd](https://poolp.org/posts/2019-09-14/setting-up-a-mail-server-with-opensmtpd-dovecot-and-rspamd) (2019)
- [How To Run Your Own Mail Server](https://www.c0ffee.net/blog/mail-server-guide) (August 2017)

---

## Stalwart

**Stalwart** is a modern mail server written in Rust that supports JMAP in addition to standard IMAP, POP3, and SMTP protocols. It combines extensive configuration options with sensible security defaults, making it accessible for immediate use.

### Key Features

- Web-based administration with TOTP 2FA support
- Public PGP key integration to encrypt **all** incoming messages
- Zero-knowledge message storage capability
- Web Key Directory (WKD) support for seamless E2EE with Proton Mail users

### Considerations

- **No integrated webmail** — requires a dedicated email client or self-hosted webmail solution (e.g., Nextcloud Mail)
- Used by Privacy Guides for internal email

### Links

- [Homepage](https://stalw.art/)
- [Documentation](https://stalw.art/docs/get-started)
- [Source Code](https://github.com/stalwartlabs)
- [PGP Implementation Details](https://stalw.art/docs/encryption/overview)

---

## Mailcow

**Mailcow** is a comprehensive mail server solution ideal for users with Linux experience. It deploys as a Docker container with an integrated feature set.

### Key Features

- DKIM support
- Antivirus and spam monitoring
- Webmail and ActiveSync via SOGo
- Web-based administration with 2FA support

### Links

- [Homepage](https://mailcow.email/)
- [Documentation](https://docs.mailcow.email/)
- [Source Code](https://github.com/mailcow/mailcow-dockerized)

---

## Mail-in-a-Box

**Mail-in-a-Box** is an automated setup script designed to simplify mail server deployment on Ubuntu. It's the most accessible option for those new to self-hosting email.

### Key Features

- Automated deployment script
- Simplified setup process
- Ubuntu-based installation

### Links

- [Homepage](https://mailinabox.email/)
- [Documentation](https://mailinabox.email/guide.html)
- [Source Code](https://github.com/mail-in-a-box/mailinabox)

---

## Comparison Summary

| Solution | Best For | Complexity | Webmail |
|----------|----------|------------|---------|
| Stalwart | Privacy-focused users, PGP encryption | Moderate | No |
| Mailcow | Full-featured deployment | Advanced | Yes (SOGo) |
| Mail-in-a-Box | Beginners to self-hosting | Beginner | Yes |