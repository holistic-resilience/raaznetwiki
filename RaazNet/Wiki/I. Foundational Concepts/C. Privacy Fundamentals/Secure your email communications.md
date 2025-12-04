---
title: "Secure Your Email Communications"
tags: [email-security, privacy, encryption, phishing-protection, digital-security, openpgp]
category: "Communication Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Human Rights Workers, IT Administrators]
topics: ["Email Security", "Encryption", "Privacy Protection", "Phishing Prevention"]
summary: "Comprehensive guide to securing email communications, from choosing providers to implementing end-to-end encryption with OpenPGP."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts", "Familiarity with email clients"]
estimated_read_time: "15 minutes"
---

# Secure Your Email Communications

Email remains essential for creating online accounts and organizing work, despite the rise of encrypted chat apps. By default, email is not the most secure communication method—it lacks encryption, carries extensive metadata, persists on servers, and exposes users to phishing and malware. However, with proper precautions, you can significantly improve its security.

## Table of Contents

- [Choose an Email Provider](#choose-an-email-provider)
- [Secure Your Email Account](#secure-your-email-account)
- [Disposable and Alias Email Addresses](#disposable-and-alias-email-addresses)
- [Create an Anonymous Email](#create-an-anonymous-email)
- [Choose How to Access Your Mailbox](#choose-how-to-access-your-mailbox)
- [Manage Email Storage on Servers](#manage-email-storage-on-servers)
- [Organize and Back Up Your Mailbox](#organize-and-back-up-your-mailbox)
- [Protect Against Phishing and Malware](#protect-against-phishing-and-malware)
- [End-to-End Encryption with OpenPGP](#end-to-end-encryption-with-openpgp)
- [Understanding Email Headers](#understanding-email-headers)

---

## Choose an Email Provider

When selecting an email provider, evaluate these critical factors:

### Trust and Transparency
- Is the platform mature, actively maintained, and widely used?
- Where is the provider based, and where are the servers located?
- Will they comply with requests from authorities in your country?
- Do they publish transparency reports or canary statements?
- Have they been independently audited?

### Technical Security
- Do they use free and open-source software?
- Do they encrypt email in transit with TLS? (Verify at [checktls.com](https://www.checktls.com/TestReceiver))
- Are individual mailboxes encrypted on the server?
- Do they offer 2-factor authentication?
- Do they support end-to-end encryption between users?

### Additional Considerations
- Do they offer OpenPGP-based encryption?
- What additional services are included (calendar, file storage, VPN)?
- What is their business model if the service is free?

> **Note:** In some situations, using a mainstream provider like Gmail may be preferable to avoid an uncommon domain name associated with activists. If so, consider encrypting your email and review guides on using Gmail more securely.

### Why This Matters

Email was developed in the 1970s without security in mind. Today, most providers protect messages with TLS encryption during transit, but messages remain unencrypted when stored on servers and devices. Anyone with access to these can read your email.

---

## Secure Your Email Account

When creating a new account:

1. **Set a strong password** immediately
2. **Enable 2-factor authentication** if available
3. **Use fake answers for recovery questions** to prevent social engineering attacks

See guides on [strong passwords](https://securityinabox.org/en/passwords/passwords/) and [2-factor authentication](https://securityinabox.org/en/passwords/2fa/) for detailed instructions.

---

## Disposable and Alias Email Addresses

### Disposable Email
For one-time use (receiving only), create temporary mailboxes at:
- [Guerrilla Mail](https://www.guerrillamail.com/)
- [anonbox](https://anonbox.net/index.en.html)

This protects your main mailbox from spam and exposure when activating services.

### Email Aliases
Create alternative addresses connected to your primary mailbox to:
- Prevent spam
- Compartmentalize communications
- Track which services share your information

---

## Create an Anonymous Email

To create an email account not connected to your official identity, follow the instructions in the [anonymity guide](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails) for creating and using email anonymously.

---

## Choose How to Access Your Mailbox

### Recommended Mail Clients

| Platform | Recommended Client |
|----------|-------------------|
| Computer | [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) |
| Android | [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) or Thunderbird |

### Benefits of Using a Mail Client
- Organize multiple email accounts in one place
- Choose whether to download mail locally or keep it on the server
- Better control over security settings
- Enhanced encryption options

Read more: [Why Use a Mail Client vs Webmail](https://blog.thunderbird.net/2024/09/why-use-a-mail-client-vs-webmail/)

---

## Manage Email Storage on Servers

### POP3 vs IMAP

| Protocol | Use Case | Server Storage |
|----------|----------|----------------|
| **POP3** | Single device access, maximum privacy | Downloads and deletes from server |
| **IMAP** | Multiple device access | Keeps mail on server |

### Recommendations
- Use **POP3** if you can access email from one secure device only
- Use **IMAP** if you need access from multiple devices
- Mobile devices are less secure than computers—they're easily lost and harder to protect
- If downloading locally, ensure your device is [secure, updated](https://securityinabox.org/en/phones-and-computers/), and [backed up](https://securityinabox.org/en/files/backup/)

---

## Organize and Back Up Your Mailbox

### Organization Tips
- Use Thunderbird's folder and filter features
- Consider [Cory Doctorow's inbox-zero strategies](https://www.theguardian.com/technology/2008/apr/29/email.filter)

### Backup Strategy
1. Back up email from server to a secure device using Thunderbird with POP3
2. Optionally leave copies on server for multi-device access
3. [Back up your Thunderbird profile](https://support.mozilla.org/en-US/kb/thunderbird-export) (accounts, messages, address books, settings)
4. [Learn to restore backups](https://support.mozilla.org/en-US/kb/thunderbird-import) using the import tool

---

## Protect Against Phishing and Malware

### Warning Signs
Watch for emails that:
- Pressure you to act quickly
- Appeal to strong emotions (fear, curiosity, urgency)
- Request login credentials
- Contain unexpected attachments or links

### Why This Matters

Security experts consider human emotions and habits the most vulnerable part of digital security. The stresses of human rights work make people especially vulnerable to social engineering attacks. Even those convinced they can't be tricked should pause and verify before acting on suspicious messages.

---

## End-to-End Encryption with OpenPGP

### What Encryption Does
- Scrambles message content using complex mathematics
- Only recipients with the correct "key" can decrypt
- Protects email body and attachments
- Sometimes protects subject line

### What Encryption Doesn't Hide
- Sender and recipient addresses
- When the message was sent
- Other header metadata

### Implementation Options

**Using Mail Clients:**
- [K-9 Mail OpenPGP Guide](https://docs.k9mail.app/en/6.400/security/pgp/)
- Thunderbird (built-in OpenPGP support)

**Encrypted Email Services:**

| Service | Notes |
|---------|-------|
| **Proton Mail** | Automatic encryption only between Proton users. For others, [set a password](https://proton.me/support/password-protected-emails) or [exchange PGP keys](https://proton.me/support/how-to-use-pgp) |
| **Mailfence** | Automatic encryption only between Mailfence users. For others, use [symmetric encryption](https://kb.mailfence.com/kb/how-to-use-symmetric-encryption/) or [exchange PGP keys](https://kb.mailfence.com/kb/how-to-send-an-openpgp-encrypted-and-signed-email/) |

---

## Understanding Email Headers

Email headers contain metadata beyond the message body:
- Time and date sent/received
- Sender's name, email address, and IP address
- Recipient information
- Subject line
- Route information through mail servers
- Authentication information

### Why Read Headers?
- Verify if an email was sent from an authorized system
- Detect spoofed sender addresses
- Identify spam
- Investigate suspicious messages

### Resources
- [CIRCL Guide: Viewing and Extracting Raw Messages](https://circl.lu/pub/tr-34/)
- [Internews Field Guide: Email Header Analysis](https://internews.org/wp-content/uploads/2023/11/Field-Guide-to-Threat-Labs.pdf) (p. 60)

---

*Last updated: 10 October 2024*

*Source: [Security in a Box](https://securityinabox.org/en/communication/secure-email/)*