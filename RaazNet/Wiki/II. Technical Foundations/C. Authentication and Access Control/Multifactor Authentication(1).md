---
title: "Multifactor Authentication"
tags: [mfa, authentication, security, hardware-security-keys, totp, fido2]
category: "Authentication Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, System Administrators]
topics: ["Digital Security", "Account Protection", "Authentication Methods"]
summary: "Comprehensive guide to multifactor authentication methods, comparing security levels from SMS to hardware keys."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of passwords and account security"]
estimated_read_time: "12 minutes"
---

# Multifactor Authentication

**Multifactor Authentication (MFA)** is a security mechanism that requires additional steps beyond entering your username and password. The most common method is time-limited codes received from SMS or an authenticator app.

If a hacker obtains your password, they would normally gain access to that account. An account with MFA forces the hacker to have both the password (something you *know*) and a device you own (something you *have*), like your phone.

MFA methods vary in security based on how difficult it is for an attacker to gain access to your MFA method. Methods range from weakest to strongest: SMS, Email codes, app push notifications, TOTP, Yubico OTP, and FIDO.

## MFA Method Comparison

### SMS or Email MFA

Receiving OTP codes via SMS or email is one of the weaker ways to secure accounts with MFA. These methods undermine the "something you *have*" principle because hackers can [take over your phone number](https://en.wikipedia.org/wiki/SIM_swap_scam) or gain access to your email without physical access to your devices.

If an unauthorized person gains access to your email, they can reset your password and receive the authentication code, giving them full account access.

### Push Notifications

Push notification MFA sends a message to an app on your phone asking you to confirm new account logins. This method is better than SMS or email since an attacker typically needs an already logged-in device first.

**Limitations:**
- Risk of accidentally accepting login attempts
- Notifications sent to all devices, widening MFA code availability
- Security depends on app quality, server component, and developer trust
- Apps may require invasive permissions
- Requires a specific app for each service

### Time-based One-time Password (TOTP)

TOTP is one of the most common MFA forms. Setup involves scanning a QR code that establishes a "[shared secret](https://en.wikipedia.org/wiki/Shared_secret)" with the service. The time-limited code derives from this shared secret and current time.

**Hardware TOTP Storage:** If you have a hardware security key with TOTP support (such as a YubiKey with [Yubico Authenticator](https://yubico.com/products/yubico-authenticator)), store your shared secrets on the hardware. A YubiKey makes the shared secret difficult to extract and isn't connected to the Internet.

**TOTP Limitations:**
- No protection against [phishing](https://en.wikipedia.org/wiki/Phishing) or reuse attacks
- Valid codes can be used multiple times until expiration (typically 60 seconds)
- Adversaries can create fake websites to capture credentials and TOTP codes

Despite limitations, TOTP is secure enough for most people and remains a good option when hardware security keys aren't supported.

### Hardware Security Keys

Hardware security keys like YubiKey store data on a tamper-resistant solid-state chip that is [impossible to access](https://security.stackexchange.com/a/245772) non-destructively without expensive forensic processes.

These keys are generally multi-function and provide several authentication methods.

#### Yubico OTP

Yubico OTP uses a public ID, private ID, and Secret Key uploaded to the Yubico OTP server. When logging into a website, physically touching the security key generates a one-time password that the service validates with Yubico's server.

A counter increments on both the key and validation server, preventing OTP reuse. See Yubico's [detailed documentation](https://developers.yubico.com/OTP/OTPs_Explained.html) for more information.

**Considerations:**
- Requires trust in Yubico's cloud-based validation server
- Public ID is reused across websites, potentially enabling third-party profiling
- Does not provide phishing resistance
- If your threat model requires different identities across websites, **do not** use Yubico OTP with the same hardware security key

#### FIDO (Fast IDentity Online)

[FIDO](https://en.wikipedia.org/wiki/FIDO_Alliance) includes several standards: [U2F](https://en.wikipedia.org/wiki/Universal_2nd_Factor), [FIDO2](https://en.wikipedia.org/wiki/FIDO2_Project), and [WebAuthn](https://en.wikipedia.org/wiki/WebAuthn).

WebAuthn is the most secure and private form of second-factor authentication. Instead of printing one-time passwords, it uses [public key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography) for authentication.

**How it works:**
1. When creating an account, the public key is sent to the service
2. When logging in, the service requires you to "sign" data with your private key
3. No password data is stored by the service—nothing for adversaries to steal

**WebAuthn Advantages:**
- Uses public key authentication (more secure than shared secrets)
- Includes origin name (domain) during authentication
- Provides attestation to protect against phishing
- No public ID used—key isn't identifiable across websites
- No third-party cloud server required
- Uses a counter to prevent session reuse and cloned keys

**If a website supports WebAuthn, it is highly recommended over any other MFA form.**

## General Recommendations

### Which Method Should I Use?

Your MFA is only as secure as your weakest authentication method. Use only the best MFA method available:

- If using TOTP, disable email and SMS MFA
- If using FIDO2/WebAuthn, don't use Yubico OTP or TOTP on the same account

### Backups

Always have backups for your MFA method. Hardware security keys can get lost, stolen, or stop working. Keep a pair of hardware security keys with the same account access.

For TOTP with an authenticator app:
- Back up recovery keys or the app itself
- Copy shared secrets to another app instance on a different phone
- Store in an encrypted container (e.g., [VeraCrypt](https://www.privacyguides.org/en/encryption/#veracrypt-disk))

### Initial Set Up

When buying a security key:
- Change default credentials
- Set up password protection
- Enable touch confirmation if supported
- Configure protection for each interface (products like YubiKey have multiple interfaces with separate credentials)

### Email and SMS

If you must use email for MFA, ensure the email account itself is secured with a proper MFA method.

For SMS MFA:
- Use a carrier that won't switch your phone number to a new SIM without account access
- Consider a dedicated VoIP number from a provider with similar security to avoid [SIM swap attacks](https://en.wikipedia.org/wiki/SIM_swap_scam)

## More Places to Set Up MFA

Beyond website logins, MFA can secure local logins, SSH keys, and password databases.

### macOS

macOS has [native support](https://support.apple.com/guide/deployment/intro-to-smart-card-integration-depd0b888248/web) for authentication with smart cards (PIV). Follow your hardware security vendor's documentation to set up second-factor authentication.

Yubico provides a guide: [Using Your YubiKey as a Smart Card in macOS](https://support.yubico.com/hc/articles/360016649059)

To prevent adversaries from bypassing MFA when the computer boots:

```bash
sudo defaults write /Library/Preferences/com.apple.loginwindow DisableFDEAutoLogin -bool YES
```

### Linux

> **Warning:** If your system's hostname changes (such as due to DHCP), you would be unable to login. Set up a proper hostname before following this guide.

The `pam_u2f` module provides two-factor authentication for logging in on most popular Linux distributions. Yubico's [Ubuntu Linux Login Guide - U2F](https://support.yubico.com/hc/articles/360016649099-Ubuntu-Linux-Login-Guide-U2F) works on most distributions (package manager commands and package names may differ).

**Note:** This guide does not apply to Qubes OS.

### Qubes OS

Qubes OS supports Challenge-Response authentication with YubiKeys. See the [Qubes OS YubiKey documentation](https://qubes-os.org/doc/yubikey) for setup instructions.

### SSH

#### Hardware Security Keys

SSH MFA can be set up using hardware security keys. See Yubico's [SSH documentation](https://developers.yubico.com/SSH) for setup instructions.

#### TOTP

SSH MFA can also use TOTP. DigitalOcean provides a tutorial: [How To Set Up Multi-Factor Authentication for SSH on Ubuntu 20.04](https://digitalocean.com/community/tutorials/how-to-set-up-multi-factor-authentication-for-ssh-on-ubuntu-20-04). Steps are similar across distributions, though package manager commands may differ.

### KeePass and KeePassXC

KeePass and KeePassXC databases can be secured using HOTP or Challenge-Response as a second factor. See:
- Yubico: [Using Your YubiKey with KeePass](https://support.yubico.com/hc/articles/360013779759-Using-Your-YubiKey-with-KeePass)
- [KeePassXC YubiKey FAQ](https://keepassxc.org/docs/#faq-yubikey-2fa)