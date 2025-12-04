```yaml
---
title: "Security Keys"
tags: [security-keys, fido2, hardware-authentication, multi-factor-authentication, yubikey, nitrokey]
category: "Authentication"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Security Professionals]
topics: ["Hardware Security", "Multi-Factor Authentication", "FIDO2", "Physical Security"]
summary: "Guide to hardware security keys including Yubico and Nitrokey options for phishing-resistant authentication."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic understanding of online accounts", "Familiarity with multi-factor authentication concepts"]
estimated_read_time: "6 minutes"
---
```

# Security Keys

A physical **security key** adds a very strong layer of protection to your online accounts. Compared to authenticator apps, the FIDO2 security key protocol is immune to phishing and cannot be compromised without physical possession of the key itself. Many services support FIDO2/WebAuthn as a multifactor authentication option, and some services allow you to use a security key as a strong single-factor authenticator with passwordless authentication.

## Yubico Security Key

The **Yubico Security Key** series is the most cost-effective hardware security key with FIDO Level 2 certification. It supports FIDO2/WebAuthn and FIDO Universal 2nd Factor (U2F), working out of the box with most services that support security keys as a second factor, including many password managers.

**Key Features:**
- Available in USB-C and USB-A variants
- Both options support NFC for mobile device use
- FIDO Level 2 certified

**Limitations:**
- Does not include Yubico Authenticator app support
- No CCID Smart Card support (PIV-compatible)

If you need those additional features, consider the higher-end YubiKey series instead.

> [!warning]
> The firmware of Yubico's Security Keys is not updatable. If you want features in newer firmware versions, or if there is a vulnerability in the firmware version you are using, you would need to purchase a new key.

**Resources:** [Homepage](https://yubico.com/products/security-key) | [Privacy Policy](https://yubico.com/support/terms-conditions/privacy-notice) | [Documentation](https://docs.yubico.com/)

---

## YubiKey

The **YubiKey** series from Yubico are among the most popular security keys with FIDO Level 2 Certification. The **YubiKey 5 Series** offers a comprehensive feature set:

- FIDO2/WebAuthn and FIDO U2F
- TOTP and HOTP authentication
- Personal Identity Verification (PIV)
- OpenPGP support

**Selecting the Right YubiKey:**
- Use Yubico's [comparison table](https://yubico.com/store/compare) to compare models
- Take their [quiz](https://yubico.com/quiz) to find the right key for your needs
- One key can typically handle all expected hardware security key functions

**Configuration Tools:**
- [YubiKey Manager](https://yubico.com/support/download/yubikey-manager) - General programming
- [YubiKey Personalization Tools](https://yubico.com/support/download/yubikey-personalization-tools) - Advanced configuration
- [Yubico Authenticator](https://yubico.com/products/yubico-authenticator) - TOTP code management

All of Yubico's clients are open source.

**Security Model for TOTP/HOTP:**
For models supporting HOTP and TOTP, secrets are stored encrypted on the key and never exposed to connected devices. Once a seed is provided to the Yubico Authenticator, it only outputs six-digit codes—never the seed itself. This limits what an attacker can do if they compromise a device running the Yubico Authenticator and makes the YubiKey resistant to physical attacks.

> [!warning]
> The firmware of YubiKey is not updatable. If you want features in newer firmware versions, or if there is a vulnerability in the firmware version you are using, you would need to purchase a new key.

**Resources:** [Homepage](https://yubico.com/products/yubikey-5-overview) | [Privacy Policy](https://yubico.com/support/terms-conditions/privacy-notice) | [Documentation](https://docs.yubico.com/)

---

## Nitrokey

**Nitrokey** offers several security key options:

| Model | Features | Certification |
|-------|----------|---------------|
| **Nitrokey Passkey** | FIDO2/WebAuthn, FIDO U2F | Cost-effective option |
| **Nitrokey 3** | PIV, OpenPGP, TOTP/HOTP | Full-featured |
| **Nitrokey 3A Mini** | Full features | FIDO Level 1 Certified |

Use Nitrokey's [comparison table](https://nitrokey.com/products/nitrokeys) to compare models and their [documentation](https://docs.nitrokey.com/nitrokeys/features) for detailed feature information.

**Configuration:** Use the [Nitrokey app](https://nitrokey.com/download) to configure your device.

> [!warning]
> Excluding the Nitrokey 3, Nitrokeys which support HOTP and TOTP do not have encrypted storage, making them vulnerable to physical attacks.

**Resources:** [Homepage](https://nitrokey.com/) | [Privacy Policy](https://nitrokey.com/data-privacy-policy) | [Documentation](https://docs.nitrokey.com/)

---

## Selection Criteria

### Minimum Requirements

- High-quality, tamper-resistant hardware security modules
- Support for the latest FIDO2 specification
- Private key extraction must not be possible
- Devices costing over $35 must support OpenPGP and S/MIME

### Best-Case Features

- USB-C form factor
- NFC capability
- TOTP secret storage
- Secure firmware updates

---

## Additional Notes

**FIDO Level 2 Certification:** Some governments or organizations may require Level 2 certification, but most users do not need to worry about this distinction.