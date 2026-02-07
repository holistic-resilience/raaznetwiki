---
title: "Email Encryption and OpenPGP"
tags:
  [
    email-security,
    encryption,
    openpgp,
    privacy,
    proton,
    tuta,
    thunderbird,
    digital-security,
    iran,
  ]
category: "Cryptography and Encryption"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public, Privacy-Conscious Users]
topics:
  [
    "End-to-End Encryption",
    "OpenPGP",
    "Secure Email Providers",
    "Email Clients",
  ]
summary: "A comprehensive guide to securing email communications in high-risk environments. Covers the limitations of standard email, the implementation of OpenPGP, and recommended providers and tools for Iranian users."
source: "Raaznet Wiki"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of email",
    "Familiarity with public/private key concepts",
  ]
estimated_read_time: "12 minutes"
---

# Email Encryption and OpenPGP

In the context of the Iranian internet landscape, standard email is one of the most vulnerable forms of communication. Traditional email functions like a postcard: it travels through multiple servers (ISPs, backbone providers, and email hosts), and at any point, the content can be read by administrators or surveillance systems.

For Iranian users, relying on domestic email providers or unencrypted international services poses a significant risk. This guide focuses on **End-to-End Encryption (E2EE)** and **OpenPGP** as the standards for securing email content against interception by the Islamic Republic's surveillance apparatus.

## The Threat Model: Why Standard Email is Unsafe

When you send a standard email (e.g., via basic Gmail or Yahoo without additional tools), the security is typically limited to **TLS (Transport Layer Security)**. TLS encrypts the connection between your device and the server, preventing a hacker in a coffee shop from sniffing your password.

However, TLS **does not** protect your data from:

1.  **The Service Provider:** Google, Yahoo, or any provider can read your emails. They may be compelled to hand this data over to governments.
2.  **Server Compromise:** If the email server is hacked, your stored emails are vulnerable ("Data at Rest").
3.  **Domestic Surveillance:** If you use an Iranian email provider (e.g., `chmail.ir` or ISP-provided email), the data is directly accessible to local intelligence services.

**The Solution:** End-to-End Encryption (E2EE) ensures that data is encrypted on your device _before_ it leaves. Only the intended recipient has the key to decrypt it. The service provider sees only scrambled code.

---

## Recommended Encrypted Email Providers

For most users, the easiest way to achieve E2EE is to use a provider that builds encryption into their web interface and apps.

> **⚠️ Warning for Iranian Users:**
>
> - **Access:** Most secure providers are blocked in Iran. You must use a trusted VPN or Tor Browser to access them.
> - **Verification:** Avoid using your real Iranian phone number for account verification. If a number is required, use a virtual number or a foreign SIM if available.
> - **Subject Lines:** Even with E2EE, **subject lines are NOT encrypted**. Never put sensitive information (names, locations, meeting times) in the subject line.

### 1. Proton Mail

Based in Switzerland, Proton is the industry leader for secure email.

- **Encryption:** Uses OpenPGP standard. Emails between Proton users are automatically encrypted.
- **Privacy:** Zero-access encryption means Proton cannot read your emails.
- **Anonymity:** No personal information required to sign up. Accepts Bitcoin and Cash for paid plans.
- **Censorship Circumvention:** Proton maintains an **Onion site** for Tor users, which is crucial when the main domain is filtered.
- **Platform:** Web, Android, iOS, Windows, macOS, Linux.

### 2. Tuta (formerly Tutanota)

Based in Germany, Tuta focuses on usability and strict privacy.

- **Encryption:** Uses a hybrid encryption protocol (not OpenPGP) that also encrypts the subject line and calendar, which Proton/OpenPGP does not do by default.
- **Pros:** Very easy to use; encrypts more metadata than competitors.
- **Cons:** Because it does not use OpenPGP, it is not compatible with external PGP tools (like Thunderbird) directly. You must use the Tuta app/client.
- **Platform:** Web, Android, iOS, Desktop clients.

### 3. Mailbox.org

Based in Germany, suitable for users willing to pay a small fee for high reliability.

- **Features:** Standard OpenPGP support, integrates well with third-party clients.
- **Privacy:** Strong legal protections in Germany; supports anonymous payment.

---

## OpenPGP: The Gold Standard for Encryption

**OpenPGP** (Pretty Good Privacy) is the open standard for email encryption. It relies on a pair of cryptographic keys:

1.  **Public Key:** You share this with the world. Anyone uses it to encrypt a message _to_ you.
2.  **Private Key:** You keep this secret. Only this key can decrypt messages sent to you.

### When to Use Manual OpenPGP?

While providers like Proton handle this automatically, you may need to use OpenPGP manually if:

- You use a standard provider (like Gmail) but need to send a secure message.
- You require absolute control over your private keys without trusting a web browser.
- You are communicating with a journalist or organization that only accepts PGP-encrypted mail.

### Recommended Software Tools

#### 1. Thunderbird (Desktop)

Mozilla Thunderbird is the recommended email client for desktop users.

- **Native PGP:** It has built-in OpenPGP support (formerly required the Enigmail add-on).
- **Key Management:** Allows you to generate, import, and manage keys easily.
- **Security:** Keeps your private keys on your local machine, not on a server.
- **Configuration:** Set up your account via POP3 (to remove mail from the server) or IMAP, then generate a key pair in the "End-to-End Encryption" settings.

#### 2. K-9 Mail / Thunderbird for Android (Mobile)

For Android users, K-9 Mail is the standard open-source client (currently rebranding to Thunderbird for Android).

- **Integration:** Works with **OpenKeychain**, a separate app that manages your PGP keys on Android.
- **Setup:** Install both K-9 Mail and OpenKeychain. Create your keys in OpenKeychain, then link it in K-9 settings.

#### 3. GPG4win / GPG Suite (Advanced)

For users who need to encrypt files outside of email or manage keys at a system level:

- **Windows:** **GPG4win** (includes Kleopatra key manager).
- **macOS:** **GPG Suite**.
- These tools allow you to encrypt text or files to the clipboard, which can then be pasted into any messaging platform or email.

---

## Email Aliasing: Protecting Your Identity

Encryption protects the _content_, but not the _metadata_ (who is talking to whom). To protect your identity and prevent cross-site tracking, use Email Aliasing.

**What is it?** A service that creates a random address (e.g., `pizza.cat88@simplelogin.com`) that forwards emails to your real inbox. You give this alias to websites or untrusted contacts.

**Recommended Services:**

- **SimpleLogin:** Open source, owned by Proton.
- **AnonAddy:** Open source, highly configurable.

**Use Case:** If you are signing up for a localized Iranian service that might be breached or monitored, use an alias. If the government seizes the database, they find a useless alias, not your primary secure email.

---

## Security Checklist for Iranian Users

1.  **Strong Passwords:** Use a Diceware passphrase (4+ random words) managed by a password manager like **KeepassXC**.
2.  **Two-Factor Authentication (2FA):**
    - **NEVER use SMS 2FA** in Iran. Telecommunication companies (MCI, Irancell) are state-monitored and SMS interception is trivial.
    - Use **TOTP apps** (Raivo OTP on iOS, Aegis on Android) or hardware keys (YubiKey).
3.  **Disable HTML Images:** In your email settings (Proton/Thunderbird), disable "Load remote content." This prevents trackers from logging your IP address and location when you open an email.
4.  **VPN/Tor:** Always access your email provider through a secure VPN or Tor. If the internet is cut (National Information Network), these services will be inaccessible; keep offline backups of critical data.
5.  **Headers:** Be aware that email headers (sender IP, server path) are usually visible. Use a VPN to mask your origin IP even when using a secure client.

## Summary Comparison

| Feature                    | Proton Mail              | Tuta                     | Standard Email + PGP (Thunderbird) |
| :------------------------- | :----------------------- | :----------------------- | :--------------------------------- |
| **Ease of Use**            | High                     | High                     | Medium/Hard                        |
| **Encryption Type**        | OpenPGP                  | Proprietary (AES/RSA)    | OpenPGP                            |
| **Metadata Protection**    | Subject visible          | Subject Encrypted        | Subject visible                    |
| **External Compatibility** | Good (Web Key Directory) | Low (Tuta-to-Tuta best)  | Excellent                          |
| **Best For**               | General Secure Use       | Maximum Metadata Privacy | Power Users / OpSec                |
