---
title: "Secure Your Email Communications"
tags: [email-security, privacy, encryption, phishing-protection, digital-security, openpgp]
category: "Communication Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Email Security", "Privacy Protection", "Encryption", "Account Security"]
summary: "Comprehensive guide to securing email communications, from choosing providers to implementing end-to-end encryption."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "15 minutes"
---

# Secure Your Email Communications

*Updated 10 October 2024*

An email is a text message (which can include file attachments) sent through a browser or mail client app like [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail). When you send an email, your message travels through multiple servers where it can be stored and backed up before reaching your recipient.

While many people now prefer [encrypted chat apps](https://securityinabox.org/en/communication/secure-chat) or [video calls](https://securityinabox.org/en/communication/video-conference) for everyday communication, email remains essential for creating online accounts and organizing work communications.

> **Important:** By default, email is not the most secure communication method—it's unencrypted, carries extensive metadata, persists on servers, and exposes you to phishing and [malware](https://securityinabox.org/en/phones-and-computers/malware/). However, there are ways to make it more secure.

---

## Choose an Email Provider

When evaluating email providers, consider these key questions:

### Platform Reliability
- Is it a mature, actively maintained platform with a large user base?

### Jurisdiction and Privacy
- Where is the provider based? Where are the servers located?
- Would they comply with requests from authorities in your country?
- Does the country enforce human rights and consumer protection?

### Trust and Transparency
- What's their history and mission?
- Do they publish transparency reports or canary statements?
- Have they been independently audited?
- How have they responded to government information requests?

### Technical Security
- Do they use free and open-source software?
- Do they encrypt email in transit with TLS? (Check with [checktls.com](https://www.checktls.com/TestReceiver))
- Are individual mailboxes encrypted on the server?
- Do they offer 2-factor authentication?
- Do they offer end-to-end encryption between users?
- Is encryption based on mature software like OpenPGP?

### Additional Considerations
- Do they offer additional services (calendar, file storage, VPN)?
- Is it paid? If free, what's their business model?

See [the Security in a Box list of email providers](https://securityinabox.org/en/communication/tools/#more-secure-email-providers) to help choose a provider.

> **Note:** In some situations, you may choose a mainstream provider like Gmail to avoid using an uncommon domain that identifies you as an activist. If so, consider the risk that commercial providers may hand over data to authorities. Read the [guide on using Gmail more securely](https://securityinabox.org/en/tools/google).

### Why This Matters

Email was developed in the 1970s for a limited number of users without security focus. Today, most providers protect messages with TLS encryption in transit—from your device through your ISP to the email servers. This prevents eavesdropping on your network.

However, messages remain **unencrypted when stored** on your device, your provider's servers, and your recipient's devices and servers. Anyone with server or device access can read your email. Consider [encrypting sensitive messages](#advanced-protect-your-email-messages-with-end-to-end-encryption).

---

## Secure Your Email Account

When creating a new email account:

1. **Set a [strong password](https://securityinabox.org/en/passwords/passwords/)** immediately
2. **Enable [2-factor authentication](https://securityinabox.org/en/passwords/2fa/)** if available
3. **Use fake answers for recovery questions** — [learn strategies for safer recovery questions](https://securityinabox.org/en/passwords/passwords/#set-safer-recovery-questions)

---

## Consider Using a Disposable Mail Account

For one-time situations (like activating a service), use a disposable mailbox:
- [Guerrilla Mail](https://www.guerrillamail.com/)
- [anonbox](https://anonbox.net/index.en.html)

This protects your main mailbox from spam and other risks.

> **Note:** Disposable emails can only **receive** messages, not send them. To send untraceable messages, see [creating an anonymous email](#optional-create-an-anonymous-email).

---

## Consider Using Email Aliases

Create alternative addresses connected to your mailbox to prevent spam and organize incoming mail.

---

## [Optional] Create an Anonymous Email

To create an email account not connected to your official identity, follow the [instructions on exchanging anonymous emails](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails).

---

## Decide How to Access Your Mailbox

### Recommended Mail Clients

| Platform | Recommended Client |
|----------|-------------------|
| Computer | [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) |
| Android | [Thunderbird](https://play.google.com/store/apps/dev?id=8696262544613553264) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) |

### Benefits of Mail Clients

- Organize multiple email accounts in one application
- Choose whether to download mail to a secure device or keep it on the server
- Access mail from different devices when needed

Read more: [Why Use a Mail Client vs Webmail](https://blog.thunderbird.net/2024/09/why-use-a-mail-client-vs-webmail/)

---

## Consider Regularly Deleting Mail from the Server

### Protocol Options

| Protocol | Use Case |
|----------|----------|
| **POP3** | Download email to a secure device and delete from server |
| **IMAP** | Keep mail on server to access from multiple devices |

See [Thunderbird's documentation on POP3 vs IMAP](https://support.mozilla.org/en-US/kb/difference-between-imap-and-pop3).

> **Security Note:** Accessing email through mobile devices is less secure than through computers—mobile devices are easily lost and harder to protect.

If downloading all email to a device, ensure it is [secure, regularly updated](https://securityinabox.org/en/phones-and-computers/) and [backed up](https://securityinabox.org/en/files/backup/).

---

## Organize Your Mailbox

- Learn to organize email in Thunderbird
- Read [Cory Doctorow's tips on keeping your inbox empty](https://www.theguardian.com/technology/2008/apr/29/email.filter)

---

## Back Up Your Mailbox

1. **Back up email from server** using [Thunderbird with POP3](https://support.mozilla.org/en-US/questions/1128358#answer-890862) (optionally leave mail on server)
2. **[Export your Thunderbird profile](https://support.mozilla.org/en-US/kb/thunderbird-export)** including accounts, messages, address books, and settings
3. **[Restore backups using the import tool](https://support.mozilla.org/en-US/kb/thunderbird-import)**

---

## Protect Yourself from Phishing and Malware

[Recognize warning signs](https://securityinabox.org/en/phones-and-computers/malware/#be-aware-that-malicious-actors-may-try-to-pressure-you-to-act-quickly-or-appeal-to-your-emotions) when an email:
- Pressures you to act quickly
- Appeals to your emotions
- Asks you to open links or download attachments
- Requests login credentials

### Why This Matters

Security experts consider human emotions and habits the most vulnerable aspect of digital security. When pressured, curious, or threatened, we tend to comply with instructions without thinking.

The stresses of human rights work make activists especially vulnerable. Many believe they can't be tricked, but **pausing to think twice** can prevent malware installation and surveillance.

---

## [Advanced] Protect Your Email with End-to-End Encryption

### Encryption Tools

**For K-9 Mail:**
- Follow [K-9 Mail's OpenPGP guide](https://docs.k9mail.app/en/6.400/security/pgp/)

### Email Services with Built-in Encryption

**Proton Mail:**
- Does not automatically encrypt mail to non-Proton addresses
- Options: [Set a password for recipients](https://proton.me/support/password-protected-emails) or [exchange PGP public keys](https://proton.me/support/how-to-use-pgp)

**Mailfence:**
- Does not automatically encrypt mail to non-Mailfence addresses
- Options: [Use symmetric encryption with password](https://kb.mailfence.com/kb/how-to-use-symmetric-encryption/) or [exchange OpenPGP keys](https://kb.mailfence.com/kb/how-to-send-an-openpgp-encrypted-and-signed-email/)

### Why Encryption Matters

Email encryption uses complex mathematics to scramble content so only someone with the decryption "key" can read it. OpenPGP encryption is trusted because no one has successfully decrypted it without the proper key.

By default, email is stored unencrypted on multiple servers and devices. Anyone with access to these locations could read your messages. Encryption makes the content appear as nonsense to attackers.

> **Limitation:** Encryption does not hide metadata—where the message comes from, who it's addressed to, when it was sent, and sometimes the subject line. An attacker could still demonstrate that people are communicating, even without knowing the content.

---

## [Advanced] Learn to Read Email Headers

Email headers contain information beyond the message body:
- Time and date sent/received
- Sender's name, email address, and IP address
- Recipient's name and email address
- Subject line
- Routing information between sender and recipient

### Why This Matters

Headers help verify whether an email was sent from an authorized system, helping identify spam or spoofed sender addresses. When you suspect a sender isn't who they claim to be, analyzing the header (or sending it to experts) can reveal the truth.

### Resources

- [CIRCL guide on viewing and extracting raw messages](https://circl.lu/pub/tr-34/)
- [Internews Field Guide to Incident Response](https://internews.org/wp-content/uploads/2023/11/Field-Guide-to-Threat-Labs.pdf) (email headers section, p. 60)