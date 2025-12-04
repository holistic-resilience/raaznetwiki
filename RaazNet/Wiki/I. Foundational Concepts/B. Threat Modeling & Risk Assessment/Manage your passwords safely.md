---
title: "Manage Your Passwords Safely"
tags: [password-management, security, authentication, encryption, privacy, digital-security]
category: "Authentication"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["Password Management", "Digital Security", "Privacy Protection"]
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

Password managers store passwords on your computer or on remote servers ("in the cloud"). Even though most cloud-based password managers are end-to-end encrypted, they can be exposed to hacking attempts without you noticing. **We strongly recommend using an offline password manager installed on your computer** like the ones listed in this guide.

Some browsers, email clients, or built-in applications like iCloud Keychain will also offer to store your passwords. This is generally less secure than using a dedicated password manager. Any solution that uses the same password for unlocking both your account and your password manager should not be considered secure enough.

## Use a Password Manager Installed on Your Device

### Recommended Password Managers

| Platform | Recommended Tool |
|----------|------------------|
| Linux, macOS, Windows | [KeePassXC](https://keepassxc.org/) |
| Android | [KeePassDX](https://keepassdx.com/) |
| iOS, macOS | [Strongbox](https://strongboxsafe.com/) |

### Best Practices

- Let the password manager generate and save a long, random, unique password for each of your accounts
- Avoid using your browser or email client to generate or store passwords when possible

### Why These Tools?

KeePassXC, KeePassDX, and Strongbox are:
- Free to use
- Verified as secure by community experts
- Continuously updated
- Offline-based, giving you control over where data is stored and how it's managed

## Back Up Your Password Manager Database

Regular backups protect you from catastrophic loss of access to your accounts.

### Backup Guides by Tool

- [How to back up KeePassXC](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_backing_up_a_database_file)
- [How to back up KeePassDX](https://github.com/Kunzisoft/KeePassDX/wiki/Backup)
- [How to back up Strongbox](https://strongboxsafe.com/support/#reamaze#0#/kb/migration-and-import-slash-export/does-strongbox-store-backups-how-can-i-export-them)

Losing many passwords at once could cause anything from a minor nuisance to catastrophic loss of communication with contacts or access to finances. Practice backing up your database regularly.

## Storing Passwords Outside Your Password Manager

For passwords you cannot save in your password manager (like device unlock codes):

- **Paper storage**: Keep in a secure, locked place like a safe or desk drawer
- **Destruction**: Thoroughly destroy paper copies as soon as you no longer need them
- **Alternative devices**: Store on a separate, secure device
- **Obscurity**: Hide passwords among other notes without explanation or description

## If You Choose an Online Password Manager

If you decide an online password manager best fits your needs:

- **Avoid storing highly sensitive information** (financial accounts, recovery account logins) in the online database
- **Enable 2-factor authentication** to protect access to your online database
- **Recommended option**: [Bitwarden](https://bitwarden.com/)

### Risk Considerations

Online password managers that sync between devices can be easier to use, but they store your encrypted password database on servers. This presents the additional risk that an attacker could decrypt your database and access your passwords without your knowledge.

## If You Store Passwords in Your Browser or Email Client

If you find it convenient to store some passwords in your browser or email client, minimize risks by following these guidelines:

- **Use only Firefox and Thunderbird** for this purpose
- **Avoid storing highly sensitive information** (financial accounts, recovery accounts)
- **Set a strong, unique primary password**
- **Close your browser** whenever you aren't using it
- **Do not sync** on devices you do not trust

---

*Updated 28 March 2024*

*Source: [Security in a Box](https://securityinabox.org/en/passwords/password-managers/)*