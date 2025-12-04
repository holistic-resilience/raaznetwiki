---
title: "Secure Your Email Communications"
tags: [email-security, encryption, privacy, digital-security, phishing-protection, openpgp]
category: "Communication Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Email Security", "Encryption", "Privacy Protection", "Digital Communication"]
summary: "Comprehensive guide to securing email communications, from choosing providers to implementing end-to-end encryption with OpenPGP."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "15 minutes"
---

# Secure Your Email Communications

Email remains essential for creating online accounts and organizing work, despite the rise of encrypted chat apps and video calls. While not inherently secure, email can be significantly hardened with proper practices.

**Key challenges with email security:**
- Not encrypted by default
- Carries extensive metadata
- Messages persist on provider servers
- Vulnerable to phishing and malware attacks

This guide covers strategies to make your email communications more secure.

---

## Table of Contents

1. [Choose an Email Provider](#choose-an-email-provider)
2. [Secure Your Email Account](#secure-your-email-account)
3. [Disposable and Alias Email Accounts](#disposable-and-alias-email-accounts)
4. [Create an Anonymous Email](#create-an-anonymous-email)
5. [Accessing Your Mailbox](#accessing-your-mailbox)
6. [Managing Server-Stored Mail](#managing-server-stored-mail)
7. [Organize and Back Up Your Mailbox](#organize-and-back-up-your-mailbox)
8. [Protect Against Phishing and Malware](#protect-against-phishing-and-malware)
9. [End-to-End Encryption with OpenPGP](#end-to-end-encryption-with-openpgp)
10. [Understanding Email Headers](#understanding-email-headers)

---

## Choose an Email Provider

When selecting an email provider, evaluate these criteria:

### Platform Maturity and Trust
- Is it actively maintained with a large user base?
- What is the provider's history, mission, and track record?
- Do they publish transparency reports or canary statements?
- Have they been independently audited?

### Jurisdiction and Privacy
- Where is the provider based and where are the servers located?
- Would they comply with requests from authorities in your country?
- Does the country enforce human rights and consumer protection?
- How have they responded to past government information requests?

### Technical Security Features
- Do they use free and open-source software?
- Do they encrypt email in transit with TLS? (Test at [checktls.com](https://www.checktls.com/TestReceiver))
- Are individual mailboxes encrypted on the server?
- Do they offer 2-factor authentication?
- Do they offer end-to-end encryption between users?
- Is encryption based on mature standards like OpenPGP?

### Additional Considerations
- Do they offer calendar, file storage, or VPN services?
- What is their business model if the service is free?

> **Note:** In some situations, using a mainstream provider like Gmail may be preferable to avoid an uncommon domain that identifies you as an activist. If choosing a commercial provider, consider the risk of data disclosure to authorities and implement email encryption.

### Why This Matters

Email was developed in the 1970s without security focus. Today, most providers protect messages with TLS encryption during transit—from your device through your ISP to the email servers. However, messages remain **unencrypted when stored** on devices and servers. Anyone with server or device access can read your email, making [end-to-end encryption](#end-to-end-encryption-with-openpgp) essential for sensitive content.

---

## Secure Your Email Account

When creating a new email account:

1. **Set a strong password** immediately using [password best practices](https://securityinabox.org/en/passwords/passwords/)
2. **Enable 2-factor authentication** if available
3. **Use fake answers for recovery questions** to prevent social engineering attacks

---

## Disposable and Alias Email Accounts

### Disposable Email

For one-time email needs (like service activation), use disposable mailboxes:
- [Guerrilla Mail](https://www.guerrillamail.com/)
- [anonbox](https://anonbox.net/index.en.html)

> **Limitation:** Disposable emails can receive but not send messages. For untraceable sending, see [Create an Anonymous Email](#create-an-anonymous-email).

### Email Aliases

Create alternative addresses connected to your main mailbox to:
- Prevent spam on your primary address
- Compartmentalize different activities
- Track which services share your information

---

## Create an Anonymous Email

To create an email account disconnected from your official identity, follow [the anonymity guide instructions](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails) for creating and using email anonymously.

---

## Accessing Your Mailbox

### Recommended Mail Clients

| Platform | Recommended Client |
|----------|-------------------|
| Computer | [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) |
| Android | [Thunderbird](https://play.google.com/store/apps/dev?id=8696262544613553264) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) |

### Benefits of Mail Clients

- **Centralized management** of multiple email accounts
- **Choice of storage location**—download to secure device or keep on server
- **Better security controls** than web interfaces
- **Offline access** to downloaded messages

> **Further reading:** [Why Use a Mail Client vs Webmail](https://blog.thunderbird.net/2024/09/why-use-a-mail-client-vs-webmail/) (Thunderbird Blog)

---

## Managing Server-Stored Mail

### POP3 vs IMAP

| Protocol | Use Case | Server Storage |
|----------|----------|----------------|
| **POP3** | Single device, maximum privacy | Downloads and can delete from server |
| **IMAP** | Multiple devices | Keeps messages on server |

### Recommendations

- Use **POP3** with Thunderbird to download email to a secure device and delete from server
- Use **IMAP** if you need access from multiple devices
- **Mobile devices are less secure** than computers—easier to lose and harder to protect
- Ensure your download device is [secure, updated](https://securityinabox.org/en/phones-and-computers/), and [backed up](https://securityinabox.org/en/files/backup/)

---

## Organize and Back Up Your Mailbox

### Organization Tips

- Use Thunderbird's folder and filter features
- Implement [inbox zero strategies](https://www.theguardian.com/technology/2008/apr/29/email.filter)

### Backup Procedures

1. **Back up email from server** using Thunderbird with POP3 (optionally leave copies on server)
2. **Export your Thunderbird profile** including accounts, messages, address books, and settings ([guide](https://support.mozilla.org/en-US/kb/thunderbird-export))
3. **Restore backups** using the [import tool](https://support.mozilla.org/en-US/kb/thunderbird-import)

---

## Protect Against Phishing and Malware

### Warning Signs

Be alert when emails:
- **Pressure you to act quickly**
- **Appeal to strong emotions** (fear, curiosity, urgency)
- Request clicking links or downloading attachments
- Ask for login credentials

### Why Attackers Target Emotions

Security experts identify human emotions and habits as the most vulnerable aspect of digital security. The stresses of activism and human rights work increase vulnerability to social engineering attacks.

> **Key defense:** Always pause and think twice before acting on urgent requests, even if you believe you could never be tricked.

---

## End-to-End Encryption with OpenPGP

### Implementation Options

**Mail Clients with OpenPGP:**
- **Thunderbird** (desktop): Built-in OpenPGP support
- **K-9 Mail** (Android): See [K-9 Mail PGP guide](https://docs.k9mail.app/en/6.400/security/pgp/)

**Encrypted Email Services:**
- **Proton Mail**: Automatic encryption between Proton users; external recipients require [password-protected messages](https://proton.me/support/password-protected-emails) or [public key exchange](https://proton.me/support/how-to-use-pgp)
- **Mailfence**: Similar to Proton—use [symmetric encryption](https://kb.mailfence.com/kb/how-to-use-symmetric-encryption/) or [OpenPGP key exchange](https://kb.mailfence.com/kb/how-to-send-an-openpgp-encrypted-and-signed-email/) for external recipients

### What Encryption Protects

| Protected | Not Protected |
|-----------|---------------|
| Message body | Sender/recipient addresses |
| Attachments | Timestamps |
| Subject line (sometimes) | Routing information |

### Why Encryption Matters

OpenPGP uses complex mathematics to scramble content so only the key holder can decrypt it. No one has successfully broken OpenPGP encryption without the key.

**Without encryption:** Your email is stored unencrypted on:
- Your email provider's servers
- Your recipient's provider's servers
- Multiple devices (phones, computers)

Anyone with server or device access can read unencrypted messages.

> **Important limitation:** Encryption doesn't hide metadata. An attacker can still determine who is communicating with whom and when, even without reading message content.

---

## Understanding Email Headers

Email headers contain routing and authentication information beyond the message body:

### Header Information Includes
- Date and time sent/received
- Sender's name, email address, and IP address
- Recipient's name and email address
- Subject line
- Routing path through intermediate servers
- Authentication status (SPF, DKIM, DMARC)

### Why Analyze Headers

- **Verify sender authenticity**—detect spoofed emails
- **Identify spam** and phishing attempts
- **Investigate suspicious messages**

### Resources for Header Analysis

- [CIRCL guide on viewing raw messages](https://circl.lu/pub/tr-34/) in common email clients
- [Internews Field Guide](https://internews.org/wp-content/uploads/2023/11/Field-Guide-to-Threat-Labs.pdf) (p. 60) for email header analysis

---

## Quick Reference: Email Security Checklist

- [ ] Choose a privacy-respecting email provider
- [ ] Use a strong, unique password
- [ ] Enable 2-factor authentication
- [ ] Use disposable emails for one-time signups
- [ ] Consider email aliases for compartmentalization
- [ ] Use a mail client (Thunderbird/K-9 Mail) instead of webmail
- [ ] Regularly back up your mailbox
- [ ] Learn to recognize phishing attempts
- [ ] Implement OpenPGP encryption for sensitive communications
- [ ] Understand how to read email headers when investigating suspicious messages