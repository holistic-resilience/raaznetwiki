---
title: "Email Security: Providers and Client Configuration"
tags:
  [email-security, privacy, encryption, openpgp, clients, surveillance, iran]
category: "Communication Platforms"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, General Public]
topics:
  [
    "Secure Email Providers",
    "Client Configuration",
    "Encryption",
    "Phishing Defense",
  ]
summary: "Comprehensive guide to selecting secure email providers, configuring desktop and mobile clients for privacy, and hardening email practices against surveillance and censorship in Iran."
source: "RaazNet Wiki"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of email", "Access to a VPN or Tor Browser"]
estimated_read_time: "20 minutes"
---

# Email Security: Providers and Client Configuration

**Email is inherently insecure.** Designed in the 1970s, the standard email protocol was built for reliability, not privacy. By default, emails are sent like postcards: anyone handling the message (internet service providers, server administrators, surveillance agencies) can read the content.

For high-risk users in Iran, email should primarily be used for registering accounts and receiving notifications. **Sensitive conversations should be moved to end-to-end encrypted messengers like Signal.**

However, since email is unavoidable, this guide explains how to choose a secure provider, configure email clients for maximum privacy, and protect your identity against state-sponsored surveillance and phishing.

---

## 1. The Threat Landscape for Iranian Users

When using email in Iran, you face specific threats:

1.  **Surveillance & Interception:** The Telecommunication Company of Iran (TCI) and other ISPs monitor unencrypted traffic. Standard emails (HTTP/SMTP without TLS) can be read in transit.
2.  **Metadata Analysis:** Even if the _content_ is encrypted, the _metadata_ (who you email, when, and the subject line) is visible to the email provider and often the ISP. This data is used to map social networks and identify activists.
3.  **Account Compromise:** State actors frequently use spear-phishing (fake login pages or malicious attachments) to hijack accounts.
4.  **Phone Number Association:** Registering an email with an Iranian phone number (+98) links your digital identity directly to your real-world identity, as SIM cards are registered with the government.

---

## 2. Choosing a Secure Email Provider

Avoid Iranian email providers (e.g., Chapar, Iran Mail) as they are legally required to comply with state surveillance. Avoid mainstream providers like Yahoo or Microsoft Outlook for sensitive work due to their jurisdictional cooperation with governments and data mining practices.

### Recommended Encrypted Providers

These providers offer **Zero-Access Encryption** (they cannot read your stored emails) and support **End-to-End Encryption (E2EE)**.

#### **Proton Mail (Switzerland)**

- **Why it's recommended:** Open-source, rigorous Swiss privacy laws, and proven track record.
- **Censorship Circumvention:** Proton provides an **Onion site** accessible via Tor Browser if the main site is blocked in Iran.
- **Privacy:** Does not require a phone number for registration (though sometimes requested for anti-abuse; solvable with a foreign number or captcha).
- **Features:** Integrated OpenPGP, supports hardware security keys (YubiKey), and offers **Proton Sentinel** (advanced account protection for high-risk users).
- **Tor Address:** `protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion`

#### **Tuta (Germany)**

- **Why it's recommended:** Does not use OpenPGP (uses its own encryption standard which also encrypts the _subject line_, unlike PGP).
- **Privacy:** No phone number required. Logs minimal metadata (IP addresses are stripped from emails sent).
- **Platform:** Excellent mobile app, but does not support standard email clients (IMAP/POP) in the free tier.

#### **Mailbox.org (Germany)**

- **Why it's recommended:** Solid privacy track record, supports standard clients via IMAP/SMTP, 100% green energy.
- **Cost:** Paid service only (very low cost), which deters spammers and keeps the service clean.
- **Anonymity:** Accepts cash by mail or cryptocurrency.

### The "Gmail" Compromise

Google's Gmail is not private (Google scans data for ads/AI), but it has world-class security against hackers. If you _must_ use Gmail:

1.  Enroll in the **Advanced Protection Program** (requires physical security keys).
2.  Use a dedicated browser for Google services only.
3.  Never use it for sensitive internal communications.
4.  **Crucial:** Do not link an Iranian recovery phone number. Use a virtual number or only a recovery email.

---

## 3. Email Client Configuration

Accessing email via a web browser (Webmail) is convenient but exposes you to browser-based attacks and tracking. Using a dedicated **Email Client** is more secure and allows for offline access and better encryption management.

### Recommended Desktop Client: **Mozilla Thunderbird**

Thunderbird is free, open-source, and supports advanced privacy configurations.

#### **Hardening Thunderbird for Privacy**

1.  **Disable Remote Content:**
    - _Settings → Privacy & Security → Web Content._
    - Uncheck "Allow remote content in messages."
    - **Why:** This blocks "tracking pixels" that tell the sender (or government) when you opened an email, your IP address, and your device type.
2.  **Disable Telemetry:**
    - _Settings → Privacy & Security → Data Collection._
    - Uncheck "Allow Thunderbird to send technical... data to Mozilla."
3.  **Global Search & Indexing:**
    - If you are on a shared computer, disable "Global Search and Indexer" to prevent creating a searchable database of your emails on the hard drive (unless the drive is fully encrypted).
4.  **Enforce Encryption:**
    - Use the **OpenPGP Key Manager** (built-in) to generate keys and encrypt emails to other PGP users.

### Recommended Mobile Clients (Android)

#### **K-9 Mail (Becoming Thunderbird for Android)**

- **Features:** Open-source, supports multiple accounts, supports OpenPGP via the **OpenKeychain** app.
- **Security:** Does not track you.
- **Configuration:** Set to "Fetch" emails rather than "Push" to save battery and reduce constant connection metadata.

#### **FairEmail**

- **Features:** extremely privacy-oriented, open-source.
- **Security:** Automatically attempts to block tracking images and scripts. Shows a "safety" indicator for every email (validating SPF/DKIM/DMARC) to help identify phishing.

---

## 4. Encryption Standards (OpenPGP)

### What OpenPGP Protects

If you use PGP encryption (available in Proton, Mailbox, Thunderbird, K-9):

- **Protected:** The body of the message and attachments.
- **NOT Protected:** The "Subject" line, the sender/recipient address, and the timestamp.

> **Warning for Iranian Activists:** Even with PGP, an ISP monitoring traffic can see _that_ you are emailing a specific foreign journalist or human rights organization, and _when_ you did it. They just cannot read the text. **Use a VPN or Tor to hide the metadata connection to the server.**

### Forward Secrecy Warning

Email encryption does **not** provide Forward Secrecy. If your private key is stolen (e.g., your laptop is seized and decrypted), **all past emails** encrypted with that key can be read.

- **Recommendation:** For high-risk conversations that require forward secrecy, move to **Signal**.

---

## 5. Advanced: Email Aliasing & Anonymity

Using your main email address for every signup creates a detailed profile of your online activity. If one site is breached, your email is exposed.

### Use Email Aliases

Services like **SimpleLogin** (owned by Proton) or **Addy.io** allow you to create unique email addresses for every account (e.g., `twitter@alias.com`, `bank@alias.com`) that forward to your main inbox.

- **Benefit:** If an account is compromised, you can just delete that alias. It prevents cross-site tracking.
- **Reverse Aliasing:** You can reply to emails without revealing your real address.

### Disposable Emails

For one-time verifications (e.g., accessing a news site), use disposable services like **Guerrilla Mail** or **Temp Mail**. Never use these for accounts you need to keep (like social media profiles), as you will lose access to the inbox.

---

## 6. Security Checklist for Iranian Users

| Action                         | Impact                                                                         |
| :----------------------------- | :----------------------------------------------------------------------------- |
| **Use a VPN/Tor**              | Hides that you are connecting to an email provider from your ISP.              |
| **Disable HTML/Remote Images** | Prevents tracking pixels from revealing your IP and location.                  |
| **No Phone Numbers**           | Never link a +98 number to a secure email account.                             |
| **Use Strong Passwords**       | Use a unique passphrase generated by a Password Manager (KeepassXC/Bitwarden). |
| **Enable 2FA**                 | Use an Authenticator App (Raivo, Aegis) or Hardware Key. **Avoid SMS 2FA.**    |
| **Verify Headers**             | Learn to read email headers to spot state-sponsored phishing attempts.         |
| **Periodic Deletion**          | Delete old emails regularly. If the data isn't there, it can't be seized.      |

---

## 7. What to Do if Compromised

If you suspect your email account has been accessed:

1.  **Immediate Password Change:** Do this from a secure, clean device.
2.  **Revoke Sessions:** Go to account settings and "Log out all other sessions."
3.  **Check Forwarding Rules:** Hackers often set up auto-forwarding rules to send a copy of all your emails to them. Check _Settings → Forwarding_ and delete any unknown rules.
4.  **Check Recovery Info:** Ensure the recovery email/phone hasn't been changed to the attacker's.
5.  **Migrate:** If the account is critical, consider abandoning it and moving to a new, clean account, informing your trusted contacts via Signal.
