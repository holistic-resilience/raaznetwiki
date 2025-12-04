---
title: "Manage Your Passwords Safely"
tags: [password-management, security, authentication, encryption, privacy]
category: "Authentication"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["Password Security", "Digital Security", "Privacy Protection"]
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

**We strongly recommend using an offline password manager** installed on your computer. If you still think an online password manager is the best choice for you, read the recommendations at the end of this guide to minimize potential risks.

> [!warning] Browser Password Storage
> Some browsers, email clients, or built-in applications like iCloud Keychain offer to store your passwords. This is generally less secure than using a dedicated password manager. Any solution that uses the same password for unlocking both your account and your password manager should not be considered secure enough.

## Use a Password Manager Installed on Your Device

### Recommended Tools

| Platform | Recommended App |
|----------|-----------------|
| Linux, macOS, Windows | [KeePassXC](https://keepassxc.org/) |
| Android | [KeePassDX](https://keepassdx.com/) |
| iOS, macOS | [Strongbox](https://strongboxsafe.com/) |

### Getting Started

1. Install one of the recommended password managers for your platform
2. Let the password manager generate and save a long, random, unique password for each of your accounts
3. Learn how to use your chosen tool effectively through its documentation

### Why These Tools?

These password managers are:
- **Free to use**
- **Verified as secure** by community experts
- **Actively maintained** with regular updates
- **Offline-based** — you control where your data is stored and how it's managed

## Back Up Your Password Database

Losing access to your password manager could mean losing access to all your accounts. Regular backups are essential.

### Backup Resources

- [How to back up KeePassXC](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_backing_up_a_database_file)
- [How to back up KeePassDX](https://github.com/Kunzisoft/KeePassDX/wiki/Backup)
- [How to back up Strongbox](https://strongboxsafe.com/support/#reamaze#0#/kb/migration-and-import-slash-export/does-strongbox-store-backups-how-can-i-export-them)

> [!tip]
> Practice backing up your database regularly. Losing many passwords at once could cause anything from a minor inconvenience to catastrophic loss of access to communications or finances.

## Storing Passwords Outside Your Password Manager

Some passwords can't be stored in your password manager—like the one that unlocks your device or the master password itself.

### Best Practices for Physical Storage

- **Write passwords on paper** only when necessary
- **Store written passwords** in a secure, locked place like a safe or desk drawer
- **Destroy paper copies** thoroughly when no longer needed
- **Consider hiding passwords** among other notes without labels or descriptions
- **Use a separate device** as an alternative storage method

## If You Choose an Online Password Manager

If convenience outweighs the additional risks for your situation:

### Recommendations

- Use [Bitwarden](https://bitwarden.com/) as your online password manager
- **Enable 2-factor authentication** to protect access to your online database
- **Avoid storing highly sensitive information** (financial accounts, recovery account logins) in the online database

### Understanding the Risks

Online password managers that sync between devices are easier to use, but they store your encrypted password database on servers. This presents an additional risk: an attacker could potentially decrypt your database and access your passwords without your knowledge.

## If You Store Passwords in Your Browser

If you find it convenient to store some passwords in your browser, minimize risks by following these guidelines:

### Browser Storage Guidelines

1. **Use only Firefox or Thunderbird** for password storage
2. **Avoid storing sensitive accounts** (financial, recovery accounts)
3. **Set a strong, unique primary password** for the browser's password manager
4. **Close your browser** when not in use
5. **Never sync passwords** to devices you don't fully trust

---

*Updated 28 March 2024*