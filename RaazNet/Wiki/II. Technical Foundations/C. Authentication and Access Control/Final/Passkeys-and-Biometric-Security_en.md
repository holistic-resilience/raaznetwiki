---
title: "Passkeys and Biometric Security"
tags:
  [
    passkeys,
    biometrics,
    fido2,
    webauthn,
    authentication,
    anti-surveillance,
    iran-security,
    keepassxc,
    yubikey,
  ]
category: "Authentication and Access Control"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, High-Risk Users]
topics:
  [
    "Digital Security",
    "Account Protection",
    "Anti-Censorship",
    "Physical Security",
  ]
summary: "A guide to understanding Passkeys and Biometrics in the Iranian context, focusing on phishing resistance, the risks of forced biometric unlock, and secure implementation strategies."
source: "Raaznet"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Understanding of Basic Authentication", "Password Manager Basics"]
estimated_read_time: "8 minutes"
last_updated: "2026-02-15"
---

# Passkeys and Biometric Security

As surveillance technologies in Iran become more sophisticated—shifting from simple brute-force attacks to algorithmic control and state-sponsored phishing—our authentication methods must evolve. **Passkeys** and **Biometrics** represent the modern standard for securing accounts, moving us away from "something you know" (passwords) to "something you have" (a device/key) and "something you are" (biometrics).

However, in the context of the Islamic Republic, these technologies act as a double-edged sword. While they offer superior protection against remote hackers and phishing, they introduce specific physical risks during detention or interrogation. This guide explains how to use them safely.

## The Iranian Context: Biometrics and Coercion

Before enabling biometric features, every Iranian user must understand the distinction between **Local Authentication** and **Centralized Surveillance**.

### 1. Centralized Biometric Databases

The Iranian government, through the National Organization for Civil Registration and Law Enforcement Command (FARAJA), maintains extensive biometric databases (iris scans, fingerprints, facial images) linked to National ID cards. This data is used for mass surveillance, including enforcing hijab laws via traffic and street cameras.

- **Risk:** You cannot hide your identity from the state if you are in a public space monitored by these cameras.

### 2. Device Biometrics (The "Forced Unlock" Threat)

Modern phones allow unlocking via FaceID or Fingerprint. While convenient, this poses a severe risk for activists, journalists, or anyone detained by security forces.

- **The Threat:** Legally and physically, it is much easier for an interrogator to force your finger onto a sensor or hold your phone up to your face than it is to coerce a complex alphanumeric password out of your mind.
- **Raaznet Recommendation:** **Disable biometric screen unlock** on your primary mobile device if you are attending protests, crossing borders, or entering high-risk zones. Rely on a strong, 6+ digit PIN or alphanumeric passphrase.

## Passkeys: The End of Phishing

**Passkeys** (based on FIDO2/WebAuthn standards) are the most significant upgrade to account security in the last decade. They effectively neutralize **phishing attacks** and **credential stuffing**—two common tactics used by state-sponsored actors to hijack Telegram, Instagram, and Email accounts.

### How Passkeys Work

Unlike a password (which is a shared secret you send to a server), a passkey consists of a cryptographic key pair:

1.  **Public Key:** Stored on the service's server (e.g., Google, GitHub). It is useless on its own.
2.  **Private Key:** Stored securely on your device (Phone, Computer, or Hardware Key). It never leaves your device.

When you log in, the server sends a challenge. Your device signs this challenge with the Private Key to prove your identity.

- **Why it stops phishing:** The protocol verifies the website's domain. If a hacker sends you a fake login link (e.g., `g00gle.com`), your device will refuse to sign the challenge because the domain doesn't match the original key.

## Types of Passkeys & Selection for Iranian Users

### 1. Hardware Security Keys (Gold Standard)

Physical USB/NFC devices like **YubiKeys** or **Nitrokeys**.

- **Security:** Highest. The key is air-gapped; it cannot be extracted by malware.
- **Iranian Context:** Extremely difficult to procure due to sanctions and customs restrictions. If you can obtain one (e.g., via a trusted traveler), it is the best protection for your primary email and admin accounts.
- **Risk:** If confiscated, you lose access unless you have a backup.

### 2. Password Manager Passkeys (Recommended)

Modern password managers like **Bitwarden**, **KeePassXC**, and **1Password** can store passkeys alongside your passwords.

- **Security:** High. Synced across devices (except KeePassXC/Local).
- **Iranian Context:**
  - **KeePassXC (Best for Privacy):** Fully offline, open-source, and stores passkeys in your local encrypted database. No concern about US cloud sanctions or data leaks.
  - **Bitwarden:** Excellent cloud option with strong encryption. Accessible in Iran (usually requires VPN).

### 3. Platform Passkeys (Convenient)

Google (Android) and Apple (iOS) store passkeys in their respective cloud keychains.

- **Security:** Good, but ties you to a single ecosystem.
- **Iranian Context:** syncing relies on Google/Apple servers, which may be blocked or require stable VPN connections.

## Implementation Strategy

### Step 1: Secure the Device

Before setting up passkeys, secure the "Vault" that holds them (your phone or computer).

- **Android:** Enable "Advanced Protection" if available (Android 16+). Set a strong screen lock PIN.
- **iOS:** Enable "Lockdown Mode" if you are a high-risk target.

### Step 2: Choose Your Storage

For most Iranian users, we recommend **KeePassXC** (Desktop) or **KeepassDX** (Android) for offline security, or **Bitwarden** for convenience.

- _Note:_ Avoid storing passkeys in the browser (Chrome/Edge) directly if you share your computer or use internet cafes.

### Step 3: Create the Passkey

1.  Log in to the service (e.g., Google Account Settings).
2.  Find "Passkeys" or "Security Keys".
3.  Select "Create a Passkey".
4.  When prompted, choose your authenticator (e.g., your YubiKey or your Bitwarden extension).

### Step 4: Create Backups (Crucial)

Unlike passwords, you cannot simply "memorize" a passkey. If you lose the device holding the private key, you are locked out.

- **Strategy:** Always register **at least two** passkeys for critical accounts.
  - Primary: Your phone or main Password Manager.
  - Backup: A secondary device (tablet), a file backup of your KeePassXC database (stored on a USB drive), or a printed set of **Recovery Codes**.

## Anti-Surveillance & Emergency Protocols

### The "SOS" Reboot

If you are in imminent danger of arrest or device seizure:

1.  **Turn off your phone immediately.**
2.  Modern phones (iOS and Android) enter "Before First Unlock" (BFU) mode upon reboot. In this state, biometric unlock is completely disabled, and the encryption keys are wiped from memory until the correct PIN is entered.
3.  This prevents authorities from using your face or fingerprint to unlock the device and access your passkeys.

### Moving Away from SMS 2FA

Iranian mobile operators (MCI, Irancell, RighTel) are legally required to cooperate with security services. **SMS 2FA is not secure.**

- **Action:** Wherever possible, replace SMS 2FA with **Passkeys** first, or **TOTP** (Authenticator Apps) second.
- **Defense:** If a service _forces_ SMS 2FA, use a Google Voice number or a foreign virtual number, never your registered Iranian SIM.

## Summary: Risk Profile Assessment

| User Profile             | Recommended Setup                                                       | Biometric Advice                                                                     |
| :----------------------- | :---------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **General Public**       | **Bitwarden** or **Google/Apple Passkeys**.                             | Biometric unlock enabled for convenience.                                            |
| **Privacy Conscious**    | **Bitwarden** with strong master password. SMS 2FA disabled everywhere. | Biometric unlock disabled on phone; enabled only for app access.                     |
| **High-Risk (Activist)** | **KeePassXC** (Offline) + **Hardware Key** (if possible).               | **Strictly NO biometrics.** Alphanumeric PINs only. "SOS" reboot protocol practiced. |

---

_Created by Raaznet Digital Security Team. Last verified: February 2026._
