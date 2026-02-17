---
title: "Digital Identity Management and Pseudonymity"
tags:
  [
    identity-management,
    pseudonymity,
    anonymity,
    opsec,
    iran,
    anti-surveillance,
    compartmentalization,
  ]
category: "Circumvention and Counter-Surveillance Concepts"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public, At-Risk Individuals]
topics:
  [
    "Identity Separation",
    "Online Personas",
    "Account Creation",
    "Mobile Security",
  ]
summary: "A comprehensive guide to creating, maintaining, and protecting separate digital identities to mitigate surveillance risks in Iran."
source: "Raaznet Aggregated Resources"
content_type: "Guide"
security_level: "High"
language: "English"
last_updated: "2026-02-17"
---

# Digital Identity Management and Pseudonymity

In an environment of extensive state surveillance, such as Iran, your digital identity—the composite of your online accounts, metadata, and behavior—is the primary vector for tracking and persecution. The Islamic Republic's surveillance apparatus relies heavily on linking online activity to real-world identities through SIM card registration, National IDs, and ISP logs.

**Digital Identity Management** is the practice of controlling what information exists about you online. **Pseudonymity** is the use of a consistent, non-real name (handle) for online activities, while **Anonymity** aims to make actions untraceable to any specific person.

This guide provides strategies to separate your sensitive activities from your real-world identity to prevent cross-correlation and "doxing."

---

## 1. The Strategy: Compartmentalization

The core principle of identity management is **compartmentalization**. This means creating distinct "silos" for different aspects of your life so that a compromise in one area does not expose the others.

### The Three Identity Levels

1.  **Real Identity (The "Clean" Identity):**
    - **Usage:** Banking, university portals, government services (e-Government), contacting family.
    - **Risk:** High visibility; assumed to be fully monitored by the state.
    - **Behavior:** Never use this identity for activism or accessing banned content without strong protection.

2.  **Persistent Pseudonymity (The "Avatar"):**
    - **Usage:** Social media (X/Twitter, Mastodon), forums, community organizing.
    - **Goal:** To build a reputation and trust within a community without revealing your legal name or location.
    - **Risk:** If linked to your real identity (e.g., by accidentally forgetting a VPN), the history of this persona is exposed.

3.  **Anonymity (The "Ghost"):**
    - **Usage:** Whistleblowing, high-risk reporting, accessing highly sensitive information.
    - **Goal:** One-time use or short-term use with no history.
    - **Behavior:** Destroyed after use. No consistent history.

---

## 2. Creating a Secure Pseudonymous Identity

To create an identity that cannot be traced back to you, you must break the link between your device, your connection, and your account.

### Step 1: Secure the Connection

Before creating any account, you must hide your IP address. Iranian ISPs log connection data that can correlate the time an account was created with your home IP.

- **Tools:** Use [Tor Browser](https://www.torproject.org/) (recommended) or a trusted, obfuscated VPN.
- **Rule:** Never log into a pseudonymous account without this protection active.

### Step 2: The Phone Number Problem (Iran Context)

Iranian SIM cards are biometric-linked to your National ID. **Never use a personal Iranian SIM (+98) to register accounts for sensitive activities.**

- **Virtual Numbers:** Use services like **Google Voice** (requires US verification) or **MySudo** (paid).
- **Crypto-Numbers:** Services like **Fragment** allow buying anonymous numbers (specifically for Telegram) using TON cryptocurrency.
- **Receive-SMS Services:** For one-time verification, use services like **SMSPool** or **5sim** (paid via crypto) to rent temporary foreign numbers. Avoid free public SMS sites, as they allow others to hijack the account later.
- **No-Number Platforms:** Prioritize platforms that do not require phone numbers, such as **SimpleX Chat**, **Session**, or **Threema**.

### Step 3: Secure Email Creation

Do not use Gmail for sensitive identities, as it requires phone verification and logs extensive data.

- **Providers:** Use [Proton Mail](https://proton.me) or [Tuta](https://tuta.com). Neither requires a phone number for free accounts (usually).
- **Email Aliasing:** Use services like **SimpleLogin** or **Addy.io**. These create a "mask" email (e.g., `random.word@aleeas.com`) that forwards to your inbox. If one alias is compromised, you can delete it without losing your main account.

---

## 3. Hardware and Software Isolation

Separating identities purely through "careful behavior" usually fails due to human error. Enforce separation with software or hardware.

### Hardware Isolation (Secondary Devices)

For high-risk activists, a dedicated "clean" device is the safest option.

- **The "Burner" or "Action" Phone:** A cheap smartphone used _only_ for sensitive work.
  - Keep it powered off and in a Faraday bag when not in use.
  - Never insert a SIM card registered to your name. Use data-only modes or Wi-Fi.
  - Never bring it to your home or workplace if it has been turned on at a protest site (to avoid location correlation).

### Software Isolation (Virtual Environments)

If you must use one computer, separate identities using virtualization.

- **Qubes OS:** The gold standard. Runs every app in a separate, isolated virtual machine (e.g., a "Whistleblower" VM and a "Personal" VM).
- **Whonix:** A virtual machine that forces all connections through Tor.
- **Browser Profiles:** On Firefox or Brave, create distinct profiles (e.g., "Work," "Activism"). Each profile has separate cookies and history. Use **Firefox Multi-Account Containers** to prevent cross-site tracking (e.g., Facebook cannot see what you do in your "News" tab).

---

## 4. Account Hygiene and Anti-Doxing

"Doxing" is the gathering and publishing of private information. In Iran, state-sponsored doxing is a prelude to arrest.

### Scrubbing Your Footprint

1.  **Search Yourself:** Perform a "self-dox." Search your real name, username, and phone numbers in Google, DuckDuckGo, and Iranian people-search databases.
2.  **Audit Old Accounts:** Delete old forums, blogs, or social media accounts that might link your pseudonym to your real life (e.g., an old Instagram post where you tagged your location).
3.  **Metadata Management:** Before uploading photos or videos (especially of protests), strip the metadata (EXIF).
    - **Tools:** [ObscuraCam](https://guardianproject.info/apps/obscuracam/) (Android), [Scrambled Exif](https://f-droid.org/packages/com.cannibal_vox.scrambled_exif/) (Android), or **ExifCleaner** (Desktop).
    - **Warning:** Most social media platforms strip metadata automatically _upon upload_, but the file might still be intercepted during upload or seized from your device.

### Securing the Accounts

- **2FA:** Enable Two-Factor Authentication on _every_ account. Use **TOTP apps** (Raivo, Aegis, Ente Auth) or **Hardware Keys** (YubiKey). **Do not use SMS 2FA** on Iranian networks, as operators can intercept codes.
- **Password Managers:** Use **Bitwarden** or **KeePassXC** to generate unique, complex passwords for every single identity. Never reuse passwords.

---

## 5. Iranian Context: Specific Risks

### Domestic Applications (The "Super-App" Trap)

Platforms like **Rubika**, **Eitaa**, **Soroush**, and **Bale** are effectively surveillance tools.

- **Risk:** They have root-level access to device data, contacts, and location. They log all chats and can be accessed by intelligence services without a warrant.
- **Mitigation:**
  - Never install domestic apps on a device used for activism.
  - If mandatory (for banking/university), install them on a separate, quarantined device or within a "Work Profile" using apps like **Shelter** or **Insular** on Android.

### IMEI Tracking and Registry

Iran's mobile registry scheme means every phone's IMEI is linked to a specific person's passport or ID.

- **Risk:** Even if you change SIM cards, the network sees the IMEI of the phone.
- **Mitigation:** Swapping SIMs into a registered phone does _not_ provide anonymity. For true anonymity, the device itself (IMEI) must not be registered to you (e.g., an older unregistered phone or a device that has never had a registered SIM inserted).

### The "Pattern of Life" Analysis

Intelligence agencies analyze patterns.

- _Example:_ If your "Anonymous" Twitter account always posts at the exact times your "Real" phone connects to home Wi-Fi, correlation is possible.
- _Mitigation:_ Vary your posting times. Use the "Schedule Post" features. Use Tor to mask traffic timing and origin.

---

## 6. Communication Tools for Pseudonymity

- **Signal:** Now supports **Usernames**. You can hide your phone number entirely from contacts. Ensure "Who can find me by number" is set to "Nobody" in settings.
- **SimpleX Chat:** Requires no phone number or email. Uses a decentralized network. Highly recommended for high-risk identity separation.
- **Briar:** P2P messenger that works over Tor and Bluetooth/Wi-Fi (offline). Ideal for protests but leaves no cloud backup.
- **Session:** No phone number required. Routes messages through an onion-routing network.

## Summary Checklist

- [ ] **Create identities over Tor/VPN** (never raw ISP connection).
- [ ] **Never use an Iranian phone number** (+98) for secure accounts.
- [ ] **Use a password manager** with unique passwords for every account.
- [ ] **Enable TOTP 2FA** (No SMS).
- [ ] **Separate devices** or use virtualization for high-risk identities.
- [ ] **Isolate domestic apps** (Rubika/Eitaa) from secure apps.
- [ ] **Scrub metadata** from media before sharing.
