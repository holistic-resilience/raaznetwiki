---
title: "Manage Your Passwords Safely"
tags: [password-management, security, encryption, authentication, privacy]
category: "Authentication"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["Digital Security", "Password Management", "Privacy Protection"]
summary: "Guide to using password managers for generating and storing strong, unique passwords securely."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "6 minutes"
---

# Manage Your Passwords Safely

No human brain is powerful enough to develop and remember passwords that are sufficiently long, random, and unique to keep all devices and accounts secure. A password manager generates and stores these passwords for you, protecting them with encryption.

## Why Use an Offline Password Manager?

Password managers store passwords either on your computer or on remote servers ("in the cloud"). Even though most cloud-based password managers are end-to-end encrypted, they can be exposed to hacking attempts without you noticing.

**We strongly recommend using an offline password manager** installed on your computer. If you still think an online password manager is the best choice for you, read our recommendations [at the end of this guide](#if-you-decide-to-use-an-online-password-manager) to minimize potential risks.

### A Note on Browser Password Storage

Some browsers, email clients, or built-in applications like iCloud Keychain will offer to store your passwords. This is generally less secure than using a dedicated password manager. Any solution that uses the same password for unlocking both your account and your password manager (like iCloud Keychain) should not be considered secure enough.

---

## Use a Password Manager Installed on Your Device

### Recommended Tools

| Platform | Recommended App |
|----------|-----------------|
| Linux, macOS, Windows | [KeePassXC](https://keepassxc.org/) |
| Android | [KeePassDX](https://keepassdx.com/) |
| iOS, macOS | [Strongbox](https://strongboxsafe.com/) |

### Getting Started

1. Install one of the recommended password managers for your device
2. Let the password manager generate and save a long, random, unique password for each of your accounts
3. Use the password manager's browser extension for convenient auto-fill

### Why These Tools?

We recommend KeePassXC, KeePassDX, and Strongbox because they are:
- **Free to use**
- **Verified as secure** by community experts
- **Continuously updated**
- **Offline by default** — you control where your data is stored and how it is managed

---

## Back Up Your Password Database

Losing access to your password manager could cause anything from a minor inconvenience to catastrophic loss of communication with contacts or access to finances. **Practice backing up your database regularly.**

### Backup Guides

- [How to back up KeePassXC](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_backing_up_a_database_file)
- [How to back up KeePassDX](https://github.com/Kunzisoft/KeePassDX/wiki/Backup)
- [How to back up Strongbox](https://strongboxsafe.com/support/#reamaze#0#/kb/migration-and-import-slash-export/does-strongbox-store-backups-how-can-i-export-them)

---

## Storing Passwords Outside Your Password Manager

Some passwords or backup codes may need to be stored separately (such as the password to unlock your password manager itself).

### Best Practices for Physical Storage

- **Write passwords on paper** and store them in a secure, locked place like a safe or desk drawer
- **Destroy paper copies** thoroughly when no longer needed
- **Consider keeping backup passwords on a separate device**
- **Hide passwords** among other notes without labels or descriptions

---

## If You Decide to Use an Online Password Manager

If you choose to use a cloud-based password manager despite the additional risks:

1. **Avoid storing highly sensitive information** (financial accounts, recovery account logins) in the online database
2. **Enable 2-factor authentication** to protect access to your online database
3. **Use a reputable service** — we recommend [Bitwarden](https://bitwarden.com/) as an online password manager

### Understanding the Risk

Online password managers that automatically synchronize between devices can be easier to use. However, they present the additional risk that an attacker could decrypt your database and access your passwords without your knowledge.

---

## If You Decide to Store Passwords in Your Browser

If you find it convenient to store some passwords in your browser, minimize risks by following these guidelines:

### Recommended Browsers

Only store passwords in **Firefox** or **Thunderbird**, which offer better security controls.

### Security Measures

1. **Avoid storing highly sensitive account information** (financial accounts, recovery accounts)
2. **Set a strong, unique primary password** for the browser's password manager
3. **Close your browser** whenever you aren't using it
4. **Do not sync passwords** to devices you do not trust

---

## Summary

| Approach | Security Level | Convenience |
|----------|---------------|-------------|
| Offline password manager (KeePassXC, etc.) | Highest | Moderate |
| Online password manager (Bitwarden) | Moderate | High |
| Browser password storage | Lower | High |
| Memory alone | Lowest | Low |

**The best choice for most users is an offline password manager** with regular backups. This provides the strongest security while still making it practical to use unique, complex passwords for every account.