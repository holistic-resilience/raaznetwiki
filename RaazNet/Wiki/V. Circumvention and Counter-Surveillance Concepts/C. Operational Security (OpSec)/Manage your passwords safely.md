---
title: "Manage Your Passwords Safely"
tags: [passwords, password-manager, security, encryption, digital-security]
category: "Password Security"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["Password Management", "Digital Security", "Data Protection"]
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

**We strongly recommend using an offline password manager** installed on your computer. If you still think an online password manager is the best choice for you, read our recommendations at the end of this guide to minimize potential risks.

> **Note on Browser Password Storage:** Some browsers, email clients, or built-in applications like iCloud Keychain will offer to store your passwords. This is generally less secure than using a dedicated password manager. Any solution that uses the same password for unlocking both your account and your password manager should not be considered secure enough.

## Use a Password Manager Installed on Your Device

### Recommended Tools

| Platform | Recommended Tool |
|----------|------------------|
| Linux, macOS, Windows | [KeePassXC](https://keepassxc.org/) |
| Android | [KeePassDX](https://keepassdx.com/) |
| iOS, macOS | [Strongbox](https://strongboxsafe.com/) |

### Getting Started

1. Install one of the recommended password managers for your platform
2. Let the password manager generate and save a long, random, unique password for each of your accounts
3. Protect your password database with a strong master password

### Why These Tools?

We recommend KeePassXC, KeePassDX, and Strongbox because they:
- Are free to use
- Have been verified as secure by community experts
- Continue to be actively updated
- Store passwords in an offline database, giving you control over where data is stored and how it is managed

## Back Up Your Password Database

Losing access to your password manager could cause anything from a minor inconvenience to catastrophic loss of communication with contacts or access to finances.

**Practice backing up your database regularly:**

- [How to back up KeePassXC](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_backing_up_a_database_file)
- [How to back up KeePassDX](https://github.com/Kunzisoft/KeePassDX/wiki/Backup)
- [How to back up Strongbox](https://strongboxsafe.com/support/#reamaze#0#/kb/migration-and-import-slash-export/does-strongbox-store-backups-how-can-i-export-them)

## Storing Passwords Outside Your Password Manager

For passwords you cannot save in your password manager (like device unlock codes), consider these options:

- **Write on paper** and store in a secure, locked place like a safe or desk drawer
- **Destroy paper copies** thoroughly as soon as you no longer need them
- **Store on a separate device** as an alternative
- **Hide among other notes** without explanation or description

## If You Choose an Online Password Manager

If you decide an online password manager better suits your needs:

1. **Avoid storing highly sensitive information** (financial accounts, recovery account logins) in the online database
2. **Enable 2-factor authentication** to protect access to your online database
3. **Use a reputable service** — we recommend [Bitwarden](https://bitwarden.com/) as an online option

### Understanding the Risks

Online password managers that automatically sync between devices can be easier to use. However, they store your encrypted password database on servers, presenting the additional risk that an attacker could potentially decrypt your database and access your passwords without your knowledge.

## If You Store Passwords in Your Browser or Email Client

If you find it convenient to store some passwords in your browser or email client, minimize risks by following these guidelines:

- **Use only Firefox or Thunderbird** for this purpose
- **Avoid storing highly sensitive accounts** (financial, recovery accounts)
- **Set a strong, unique primary password** for the browser's password storage
- **Close your browser** whenever you aren't using it
- **Do not sync passwords** to devices you do not fully trust

---

*Last updated: 28 March 2024*