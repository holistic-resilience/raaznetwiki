---
title: "Identity, Authentication, and Account Security"
tags:
  [
    identity-management,
    authentication,
    passwords,
    2fa,
    opsec,
    privacy,
    iran-security,
  ]
category: "Operational Security (OpSec)"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, At-Risk Iranian Users]
topics:
  [
    "Password Management",
    "Two-Factor Authentication",
    "Anonymity",
    "Account Recovery",
  ]
summary: "Comprehensive guide on securing digital identities for Iranian users, covering strong authentication, compartmentalization, and protection against state-sponsored account compromise."
source: "Raaznet Aggregated Resources"
content_type: "Wiki"
security_level: "High"
language: "English"
prerequisites:
  ["Basic digital literacy", "Access to circumvention tools (VPN/Tor)"]
estimated_read_time: "15 minutes"
last_updated: "2026-02-17"
---

# Identity, Authentication, and Account Security

Your online identity is often the primary target of state surveillance. The Islamic Republic utilizes extensive phishing campaigns, SMS interception, and coercion to compromise accounts. This guide outlines strategies to secure your digital identity, manage authentication robustly, and compartmentalize your online presence to minimize risk.

## 1. Authentication Fundamentals

The first line of defense against unauthorized access is how you prove who you are to a system.

### Password Management

Reusing passwords is a critical vulnerability. If one Iranian service is breached (a frequent occurrence), those credentials will be tested against your email, Telegram, and Instagram accounts.

#### The Strategy: Password Managers

Human memory cannot manage unique, complex passwords for every account. You must use a password manager.

- **Offline Managers (Highly Recommended):** Given the risk of internet blackouts (filmternet) and service blocking in Iran, offline managers are superior. They store your database locally on your device.
  - **Recommended Tools:** [KeePassXC](https://keepassxc.org/) (Desktop), [KeePassDX](https://www.keepassdx.com/) (Android), [Strongbox](https://strongboxsafe.com/) (iOS).
- **Cloud Managers:** If you require synchronization across devices, ensure you use a service with a "Zero-Knowledge" architecture and turn on strict 2FA. Be aware that you may need a VPN to access your vault.
  - **Options:** [Bitwarden](https://bitwarden.com/) or [1Password](https://1password.com/).

#### Creating Strong Passphrases

For your "Master Password" (the one that unlocks your manager) or full-disk encryption, use a **Diceware Passphrase**. This consists of 5-7 random words.

- _Weak:_ `Tehran1398!` (Predictable structure, widely used).
- _Strong:_ `battery-horse-staple-correct-painting` (Mathematically hard to guess, easier to type).

### Two-Factor Authentication (2FA)

Passwords alone are no longer sufficient. You must require a second form of verification.

#### ⚠️ The Danger of SMS 2FA in Iran

**Do not use SMS for Two-Factor Authentication if possible.**
Telecommunication providers in Iran (MCI, Irancell, Rightel) are legally required to cooperate with security services. State actors can easily intercept SMS verification codes or execute SIM-swap attacks to hijack your phone number.

#### Recommended 2FA Methods

1.  **Authenticator Apps (TOTP):** These generate codes offline on your device. Even if the internet is cut, you can still log in.
    - **Android:** [Aegis Authenticator](https://getaegis.app/) (Free, Open Source, Encrypted backups).
    - **iOS:** [Raivo OTP](https://raivo-otp.com/) or [Ente Auth](https://ente.io/auth/).
2.  **Hardware Security Keys:** Physical USB/NFC keys (like YubiKey) are the gold standard. They are immune to phishing. However, they can be difficult to purchase anonymously in Iran and may be confiscated during physical searches.
3.  **Passkeys:** A newer standard that replaces passwords entirely using cryptography stored on your device. Use this wherever supported (e.g., Google, GitHub).

---

## 2. Identity Management & Compartmentalization

Separating your "true" identity from your online activities is essential for safety.

### Strategies for Identity

1.  **Real Identity:** Use only for banking, official government services, and necessary family communications. Minimize political activity here.
2.  **Pseudonymity:** Using a consistent alias (e.g., specific handle on Twitter/X). This builds reputation but can be linked back to you over time through metadata.
3.  **Anonymity:** Using short-lived identities with no link to your real life. Use [Tor Browser](https://www.torproject.org/) and new accounts for high-risk whistleblowing.

### Compartmentalization

Never allow your identities to cross-contaminate.

- **Separate Browsers:** Use one browser (e.g., Firefox) for daily tasks and a hardened browser (e.g., Brave or Tor) for sensitive work.
- **Separate Accounts:** Do not use your "Real Name" email to sign up for an anonymous Twitter account.
- **Work Profiles:** On Android, use the "Work Profile" feature (via apps like _Shelter_ or _Island_) to isolate suspicious apps from your main data.

### Phone Number Security

Your phone number is a direct link to your national ID.

- **Hide Your Number:** In Telegram and Signal settings, set "Who can see my phone number" to **Nobody**.
- **Virtual Numbers:** For registering accounts (Twitter, Telegram), consider using foreign virtual numbers (like Google Voice, if obtained securely) or anonymous fragment numbers (for Telegram) to avoid linking the account to your SIM card.

---

## 3. Account Hygiene and Anti-Doxxing

Doxxing (publishing private info) is a tactic used by state-aligned actors to intimidate activists.

### Reducing Your Digital Footprint

- **Audit Old Accounts:** Delete accounts you no longer use. Breach data from old forums is frequently used to guess passwords for current accounts.
- **Social Media Lockdown:** Set friend lists to "Private." Do not display your birth date, location, or employer on public profiles.
- **Search Yourself:** Regularly search your name, handle, and phone number in Google and Iranian search engines to see what is public.

### Identifying Phishing

Iranian users are frequently targeted by fake "Judiciary" (Edalat) SMS messages or emails claiming unauthorized access to accounts.

- **Never click links in SMS.**
- **Check the URL:** Look for misspellings (e.g., `gmai1.com` instead of `gmail.com`).
- **Urgency is a Red Flag:** Any message demanding immediate action ("Your account will be deleted in 24 hours") is likely an attack.

---

## 4. Compromise Recovery

If you suspect an account has been accessed or you have been detained and forced to unlock devices:

1.  **Revoke Sessions:** Immediately go to the "Devices" or "Sessions" menu of the service (Telegram, Google, Instagram) and "Log out all other sessions."
2.  **Change Credentials:** Change your password and generate **new** backup codes.
3.  **Check Forwarding:** Attackers often set up email forwarding rules to keep spying on you after you change passwords. Check your email settings for unknown forwarding addresses.
4.  **Device Wipe:** If a device was in custody of security forces for _any_ amount of time, assume it is compromised with spyware. Factory reset is often insufficient; physical destruction or professional flashing is safer.

## 5. Summary Checklist

- [ ] **Manager:** Transferred all passwords to an offline password manager (e.g., KeePassXC).
- [ ] **2FA:** Enabled TOTP (Authenticator App) on all accounts. Removed SMS 2FA where possible.
- [ ] **Cleanup:** Deleted old accounts and removed phone numbers from public social media profiles.
- [ ] **Drill:** Saved "Backup Codes" for critical accounts (Google, Telegram) in a secure, offline location.
- [ ] **VPN:** Ensured reliable, obfuscated VPN access to log into accounts during filtering.
