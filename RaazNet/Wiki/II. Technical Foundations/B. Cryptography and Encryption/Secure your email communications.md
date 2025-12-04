---
title: "Secure Your Email Communications"
tags: [email-security, encryption, privacy, phishing-protection, digital-security, openpgp]
category: "Communication Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Human Rights Workers, General Public]
topics: ["Email Security", "Encryption", "Privacy Protection", "Phishing Prevention"]
summary: "Comprehensive guide to securing email communications, from choosing providers to implementing end-to-end encryption with OpenPGP."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "15 minutes"
---

# Secure Your Email Communications

When you send an email, your message travels through multiple servers before reaching its destination. It's stored on your provider's servers, forwarded to your recipient's provider, and stored again—potentially backed up at each step. Understanding this journey is essential for protecting your communications.

While many people now prefer [encrypted chat apps](https://securityinabox.org/en/communication/secure-chat) or [video calls](https://securityinabox.org/en/communication/video-conference) for daily communication, email remains essential for creating online accounts and organizing work. By default, email isn't the most secure method—it carries significant metadata, persists on servers, and exposes you to phishing and malware. However, there are effective ways to make it more secure.

---

## Choose an Email Provider

When selecting an email provider, evaluate these key factors:

**Trust and Transparency**
- Is it a mature, actively maintained platform with a large user base?
- Where is the provider based, and where are the servers located?
- Do they publish transparency reports or canary statements?
- Have they been independently audited?
- How have they responded to government data requests?

**Technical Security**
- Do they use free and open-source software?
- Do they encrypt email in transit with TLS? (Verify at [checktls.com](https://www.checktls.com/TestReceiver))
- Are individual mailboxes encrypted on the server?
- Do they offer 2-factor authentication?
- Do they support end-to-end encryption between users?
- Do they offer OpenPGP-based encryption?

**Practical Considerations**
- Do they offer additional services (calendar, file storage, VPN)?
- Is it a paid service? If free, what's their business model?

See the [Security in a Box list of email providers](https://securityinabox.org/en/communication/tools/#more-secure-email-providers) for recommendations.

> **Note:** In some situations, using a mainstream provider like Gmail may be strategic—for example, to avoid an uncommon domain that identifies you as an activist. If so, consider the risks and [use Gmail more securely](https://securityinabox.org/en/tools/google).

### Why This Matters

Email was developed in the 1970s without security in mind. Today, most providers protect messages in transit using TLS encryption, preventing eavesdropping between your device and the servers. However, messages remain unencrypted when stored on devices and servers. Anyone with server or device access can potentially read your email—which is why [end-to-end encryption](#protect-your-email-messages-with-end-to-end-encryption) is crucial for sensitive content.

---

## Secure Your Email Account

When creating a new email account:

1. **Set a [strong password](https://securityinabox.org/en/passwords/passwords/)** immediately
2. **Enable [2-factor authentication](https://securityinabox.org/en/passwords/2fa/)** if available
3. **Use fake answers for recovery questions**—learn strategies in the [safe passwords guide](https://securityinabox.org/en/passwords/passwords/#set-safer-recovery-questions)

---

## Use Disposable and Alias Email Addresses

### Disposable Email
For one-time situations (like activating a service), use a disposable mailbox:
- [Guerrilla Mail](https://www.guerrillamail.com/)
- [anonbox](https://anonbox.net/index.en.html)

> **Note:** Disposable emails can receive but not send messages. For untraceable sending, see [creating an anonymous email](#create-an-anonymous-email).

### Email Aliases
Create alternative addresses connected to your main mailbox to prevent spam and organize incoming mail by purpose.

---

## Create an Anonymous Email

To create an email account that cannot be traced to your identity, follow the [instructions in the anonymity guide](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails).

---

## Choose How to Access Your Mailbox

**Recommended Mail Clients:**
- **Computer:** [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird)
- **Android:** [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) or [Thunderbird for Android](https://play.google.com/store/apps/dev?id=8696262544613553264)

Using a dedicated mail client offers several advantages:
- Organize multiple email accounts in one place
- Choose whether to download mail locally or keep it on the server
- Better control over security settings

Read more: [Why Use a Mail Client vs Webmail](https://blog.thunderbird.net/2024/09/why-use-a-mail-client-vs-webmail/)

---

## Manage Server-Stored Email

**Protocol Options:**
- **POP3:** Downloads email to your device and can delete it from the server—better for privacy
- **IMAP:** Keeps email on the server for multi-device access

See the [Thunderbird documentation](https://support.mozilla.org/en-US/kb/difference-between-imap-and-pop3) for detailed explanations.

**Important Considerations:**
- Mobile devices are less secure than computers (easier to lose, harder to protect)
- If downloading all email locally, ensure your device is [secure, updated](https://securityinabox.org/en/phones-and-computers/), and [backed up](https://securityinabox.org/en/files/backup/)

---

## Organize and Back Up Your Mailbox

### Organization Tips
- Use Thunderbird's folder and filter features
- Read [Cory Doctorow's tips for inbox zero](https://www.theguardian.com/technology/2008/apr/29/email.filter)

### Backup Strategy
1. Back up email from server to a secure device using [Thunderbird with POP3](https://support.mozilla.org/en-US/questions/1128358#answer-890862)
2. [Export your Thunderbird profile](https://support.mozilla.org/en-US/kb/thunderbird-export) (accounts, messages, address books, settings)
3. [Restore backups using the import tool](https://support.mozilla.org/en-US/kb/thunderbird-import)

---

## Protect Yourself from Phishing and Malware

[Develop habits to recognize manipulation attempts](https://securityinabox.org/en/phones-and-computers/malware/#be-aware-that-malicious-actors-may-try-to-pressure-you-to-act-quickly-or-appeal-to-your-emotions):

**Warning Signs:**
- Pressure to act quickly
- Appeals to emotion (fear, curiosity, urgency)
- Requests to click links or download attachments
- Prompts to enter login credentials

### Why This Matters

Security experts identify human emotions and habits as the most vulnerable part of digital security. The stresses of human rights work can increase vulnerability to these attacks. Even those convinced they can't be tricked should pause and think twice—it can prevent malware installation and surveillance.

---

## Protect Your Email with End-to-End Encryption

### Using OpenPGP

Encrypt and sign your messages using:
- **Thunderbird:** Built-in OpenPGP support
- **K-9 Mail:** Follow the [K-9 Mail encryption guide](https://docs.k9mail.app/en/6.400/security/pgp/)

### Encrypted Email Services

**Proton Mail**
- Does not automatically encrypt to non-Proton addresses
- Options: [Set a password for recipients](https://proton.me/support/password-protected-emails) or [exchange PGP keys](https://proton.me/support/how-to-use-pgp)

**Mailfence**
- Does not automatically encrypt to non-Mailfence addresses
- Options: [Use symmetric encryption with password](https://kb.mailfence.com/kb/how-to-use-symmetric-encryption/) or [exchange OpenPGP keys](https://kb.mailfence.com/kb/how-to-send-an-openpgp-encrypted-and-signed-email/)

### Why This Matters

Email encryption uses complex mathematics to scramble content so only someone with the decryption key can read it. OpenPGP encryption is trusted by experts because no one has successfully decrypted it without the proper key.

**What Encryption Protects:**
- Email body
- Attachments
- Sometimes the subject line

**What Encryption Does NOT Hide:**
- Sender and recipient addresses
- Timestamps
- Other header metadata

An attacker could still determine that people are communicating, even without knowing the content.

---

## Learn to Read Email Headers

Email headers contain crucial metadata beyond the message body:
- Time and date sent/received
- Sender's name, email, and IP address
- Recipient information
- Routing information through servers
- Authentication data (helps identify spoofing)

### Resources
- [CIRCL guide on viewing raw email messages](https://circl.lu/pub/tr-34/)
- [Internews Field Guide to Incident Response](https://internews.org/wp-content/uploads/2023/11/Field-Guide-to-Threat-Labs.pdf) (p. 60, email header analysis)

### Why This Matters

Reading headers helps you:
- Verify if an email came from an authorized system
- Identify spam or spoofed sender addresses
- Provide evidence to security experts for analysis when suspicious emails arrive