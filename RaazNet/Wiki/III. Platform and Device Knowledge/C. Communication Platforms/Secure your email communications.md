---
title: "Secure Your Email Communications"
tags: [email-security, privacy, encryption, phishing-protection, digital-security, openpgp]
category: "Digital Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Email Security", "Privacy Protection", "Encryption", "Account Security"]
summary: "Comprehensive guide to securing email communications, covering provider selection, account protection, encryption, and phishing defense."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "15 minutes"
---

# Secure Your Email Communications

*Updated 10 October 2024*

An email is a text message (which can include file attachments) that you send through a browser or mail client app like [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail). When you click Send, your message reaches your email provider's servers, where it is stored and may be backed up. Your provider then forwards it to your recipient's provider, where it is stored again. Finally, the email is delivered to your recipients, who can keep it stored online or download it to their devices.

While many people now prefer [encrypted chat apps](https://securityinabox.org/en/communication/secure-chat) or [video calls](https://securityinabox.org/en/communication/video-conference) for everyday communications, email remains essential for creating online accounts and organizing work conversations.

**Important:** By default, email is not the most secure communication method—it is not encrypted, carries extensive metadata, persists on provider servers, and exposes you to phishing and [malware attacks](https://securityinabox.org/en/phones-and-computers/malware/). However, there are ways to make it more secure.

---

## Choose an Email Provider

When selecting an email provider, consider these questions:

**Reliability and Trust:**
- Is it a mature, actively maintained platform with a large user base?
- What is the provider's history and mission?
- Do they publish transparency reports or canary statements?
- Have they been independently audited?

**Jurisdiction and Privacy:**
- Where is the provider based, and where are the servers located?
- Would they comply with requests from authorities in your country?
- Does the country enforce human rights and consumer protection?

**Technical Security:**
- Do they use free and open-source software?
- Do they encrypt email in transit with TLS? (Test at [checktls.com](https://www.checktls.com/TestReceiver))
- Are individual mailboxes encrypted on the server?
- Do they offer 2-factor authentication?
- Do they offer end-to-end encryption between users?
- Is encryption based on mature software like OpenPGP?

**Additional Considerations:**
- Do they offer additional services (calendar, file storage, VPN)?
- Is it paid? If free, what's the business model?

See [our list of email providers](https://securityinabox.org/en/communication/tools/#more-secure-email-providers) to make your choice.

> **Note:** In some situations, you may choose a mainstream provider like Gmail to avoid using an uncommon domain that identifies you as an activist. If so, consider the risk that commercial providers may hand over data to authorities, and [use Gmail more securely](https://securityinabox.org/en/tools/google).

### Why This Matters

Email was developed in the 1970s for a limited number of users without security focus. Today, most providers protect messages with TLS encryption in transit—from your device through your ISP to the email servers. However, messages remain unencrypted when stored on servers and devices. Anyone with access to these can read your email, which is why [encrypting your messages](https://securityinabox.org/en/communication/secure-email/#advanced-protect-your-email-messages-with-end-to-end-encryption) is strongly recommended for sensitive content.

---

## Secure Your Email Account

When creating a new email account:

1. **Set a [strong password](https://securityinabox.org/en/passwords/passwords/)** immediately
2. **Enable [2-factor authentication](https://securityinabox.org/en/passwords/2fa/)** if available
3. **Use fake answers for recovery questions**—[learn strategies in our password guide](https://securityinabox.org/en/passwords/passwords/#set-safer-recovery-questions)

---

## Use Disposable and Alias Email Addresses

### Disposable Email Accounts

For one-time situations (like activating a service), use a disposable mailbox:
- [Guerrilla Mail](https://www.guerrillamail.com/)
- [anonbox](https://anonbox.net/index.en.html)

This protects your main mailbox from spam and other risks. Note that disposable emails can receive but not send messages.

### Email Aliases

Create alternative addresses connected to your mailbox to prevent spam and compartmentalize your communications.

### Anonymous Email

To create an email account not connected to your identity, follow [the instructions in our anonymity guide](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails).

---

## Choose How to Access Your Mailbox

**Recommended mail clients:**
- **Computer:** [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird)
- **Android:** [Thunderbird](https://play.google.com/store/apps/dev?id=8696262544613553264) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail)

### Why Use a Mail Client?

Mail clients let you:
- Organize all your email accounts in one place
- Choose whether to download mail to a secure device or keep it on the server
- Access mail from different devices when needed

Read more: [Why Use a Mail Client vs Webmail](https://blog.thunderbird.net/2024/09/why-use-a-mail-client-vs-webmail/)

---

## Manage Mail Storage on Servers

**POP3 vs IMAP:**
- **POP3:** Downloads email to your device and can delete it from the server—better for security
- **IMAP:** Keeps email on the server for access from multiple devices—more convenient but less secure

See [Thunderbird's documentation on POP3 vs IMAP](https://support.mozilla.org/en-US/kb/difference-between-imap-and-pop3).

**Security considerations:**
- Mobile devices are less secure than computers (easier to lose, harder to protect)
- If downloading all email to a device, ensure it is [secure, updated](https://securityinabox.org/en/phones-and-computers/), and [backed up](https://securityinabox.org/en/files/backup/)

---

## Organize and Back Up Your Mailbox

### Organization
- Use Thunderbird's built-in organization features
- Read [Cory Doctorow's tips on keeping your inbox empty](https://www.theguardian.com/technology/2008/apr/29/email.filter)

### Backup
1. Back up email from your server using [Thunderbird with POP3](https://securityinabox.org/en/communication/secure-email/#consider-regularly-deleting-mail-stored-on-the-server)
2. [Back up your Thunderbird profile](https://support.mozilla.org/en-US/kb/thunderbird-export) (accounts, messages, address books, settings)
3. [Restore backups using the import tool](https://support.mozilla.org/en-US/kb/thunderbird-import)

---

## Protect Yourself from Phishing and Malware

[Recognize when emails pressure you to act quickly or appeal to your emotions](https://securityinabox.org/en/phones-and-computers/malware/#be-aware-that-malicious-actors-may-try-to-pressure-you-to-act-quickly-or-appeal-to-your-emotions)—these may be attempts to make you:
- Open malicious links
- Download infected attachments
- Enter credentials on phishing pages

### Why This Matters

Security experts consider human emotions and habits the most vulnerable part of digital security. When pressured to act quickly, curious, or threatened, people often comply without thinking. Human rights workers face particular stress that increases vulnerability. Taking a moment to think twice can prevent malware installation and surveillance.

---

## [Advanced] End-to-End Encryption with OpenPGP

### Using Mail Clients

Encrypt and sign messages with OpenPGP using:
- **Thunderbird:** Built-in OpenPGP support
- **K-9 Mail:** [OpenPGP guide](https://docs.k9mail.app/en/6.400/security/pgp/)

### Encrypted Email Services

**Proton Mail:**
- Does not automatically encrypt mail to non-Proton addresses
- Options: [Set a password for recipients](https://proton.me/support/password-protected-emails) or [exchange public keys](https://proton.me/support/how-to-use-pgp)

**Mailfence:**
- Does not automatically encrypt mail to non-Mailfence addresses
- Options: [Set a password](https://kb.mailfence.com/kb/how-to-use-symmetric-encryption/) or [exchange public keys](https://kb.mailfence.com/kb/how-to-send-an-openpgp-encrypted-and-signed-email/)

### Why Encryption Matters

Email encryption uses complex mathematics to scramble content so only someone with the decryption key can read it. OpenPGP is trusted because no one has successfully broken it without the key.

**What encryption protects:**
- Email body
- Attachments
- Sometimes the subject line

**What encryption does NOT protect:**
- Sender and recipient addresses
- When the message was sent
- Other header metadata

An attacker could still demonstrate that people are communicating, even without knowing the content.

---

## [Advanced] Understanding Email Headers

Email headers contain information beyond the message body:
- Time and date sent/received
- Sender's name, email address, and IP address
- Recipient's name and email address
- Subject line
- Route information between sender and recipient
- Authentication status (helps identify spam or spoofed emails)

### Resources

- [CIRCL guide on viewing raw messages](https://circl.lu/pub/tr-34/)
- [Internews Field Guide to Incident Response (2023, p. 60)](https://internews.org/wp-content/uploads/2023/11/Field-Guide-to-Threat-Labs.pdf)

Being able to read headers helps you verify whether an email is legitimate or if the sender's address has been spoofed.