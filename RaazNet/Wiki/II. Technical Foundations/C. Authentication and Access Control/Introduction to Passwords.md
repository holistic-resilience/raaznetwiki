---
title: "Introduction to Passwords"
tags: [security, privacy, authentication, passwords, password-managers, diceware]
category: "Authentication"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users]
topics: ["Digital Security", "Password Management", "Authentication"]
summary: "Comprehensive guide to creating, managing, and storing strong passwords using best practices and password managers."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "8 minutes"
---

# Introduction to Passwords

Passwords are an essential part of our everyday digital lives. We use them to protect our accounts, our devices, and our secrets. Despite often being the only thing between us and an adversary who's after our private information, not a lot of thought is put into them, which often leads to people using passwords that can be easily guessed or brute-forced.

## Best Practices

### Use Unique Passwords for Every Service

**Credential stuffing** is one of the most common ways that accounts are compromised by bad actors. This attack occurs when criminals obtain username/password combinations from one data breach and automatically try them on thousands of other websites.

To protect yourself, **never re-use your passwords** across different services.

### Use Randomly Generated Passwords

You should **never** rely on yourself to come up with a good password. Human-created passwords tend to follow predictable patterns that attackers can exploit.

Instead, use:
- **Randomly generated passwords** for accounts stored in your password manager
- **Diceware passphrases** for passwords you need to memorize

All recommended password managers include built-in password generators.

### Rotating Passwords

**Passwords you must remember** (like your password manager's master password):
- Avoid changing too frequently unless you suspect compromise
- Changing too often increases the risk of forgetting

**Passwords stored in your password manager**:
- Consider changing important account passwords every few months
- Prioritize accounts without multifactor authentication
- Use your password manager's expiry date feature to track rotation

> [!tip] Checking for Data Breaches
> If your password manager supports checking for compromised passwords, use this feature regularly. Promptly change any password exposed in a data breach. You can also monitor [Have I Been Pwned's Latest Breaches feed](https://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches) using a news aggregator.

## Creating Strong Passwords

### Generated Passwords

Many services impose criteria for passwords, including minimum/maximum length and allowed special characters. Use your password manager's built-in generator to create passwords that are:

- As long as the service allows
- Include uppercase and lowercase letters
- Include numbers and special characters

For passwords you need to memorize, use a diceware passphrase instead.

### Diceware Passphrases

Diceware is a method for creating passphrases that are **easy to remember but hard to guess**. They're ideal for:

- Password manager master passwords
- Device encryption passwords
- Any credential you must memorize or manually input

**Example passphrase:** `viewable fastness reluctant squishy seventeen shown pencil`

#### How to Generate a Diceware Passphrase

These instructions use the [EFF's large word list](https://eff.org/files/2016/07/18/eff_large_wordlist.txt), which requires five dice rolls per word.

1. Roll a six-sided die five times, noting each number
2. Look up the five-digit number in the EFF word list (e.g., `25266` = `encrypt`)
3. Write down the corresponding word
4. Repeat until you have at least 6-7 words
5. Separate words with spaces

> [!warning] Important
> **Do not re-roll words** to get combinations that appeal to you. The process must be completely random to maintain security.

**Alternative method:** Use your password manager's built-in diceware generator with a minimum of 6 words.

#### Why Diceware Works

The EFF's large word list contains 7,776 unique words. A seven-word passphrase provides approximately **90.47 bits of entropy** (log₂(7776⁷)), resulting in roughly 1.7 septillion possible combinations.

This remains secure even when an adversary knows:
- You used the diceware method
- Which word list you used
- How many words your passphrase contains

Word lists are available in [multiple languages](https://theworld.com/~reinhold/diceware.html#Diceware%20in%20Other%20Languages|outline) if you prefer a non-English passphrase.

## Storing Passwords

### Password Managers

Password managers store your passwords in an encrypted file or cloud service, protected by a single master password. This approach means you only need to remember one strong password to access all others.

**Recommendations:**
- Choose a reputable password manager (cloud-based or local)
- Secure it with a diceware passphrase of at least seven words
- Use it to generate and store strong, unique passwords for all accounts

> [!warning] Separate Your TOTP Tokens
> When using TOTP codes for multifactor authentication, store them in a **separate app** from your password manager. Keeping passwords and TOTP codes together reduces security to a single factor if your password manager is compromised.

> [!tip] Recovery Codes
> Store single-use recovery codes separately from your password manager—ideally in an encrypted container on an offline storage device.

### Backups

Store an **encrypted backup** of your passwords on:
- Multiple storage devices
- A cloud storage provider

This ensures access to your passwords if something happens to your primary device or service.