---
title: "Create and Maintain Strong Passwords"
tags: [passwords, security, authentication, password-managers, two-factor-authentication]
category: "Authentication"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["Digital Security", "Password Management", "Account Protection"]
summary: "Comprehensive guide to creating, managing, and protecting strong passwords using best practices and security tools."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "12 minutes"
---

# Create and Maintain Strong Passwords

Passwords are important tools for keeping your data and identity secure. Unfortunately, attackers know this, and they have many tricks they can use to figure out your passwords. But you can defend against those tricks by applying a few important tools and tactics.

## Protect Your Passwords

- **Use a secure device**: Always use a secure, updated, protected and trusted device to access your accounts and manage your sensitive information, including passwords.
- **Use a password manager**: No human brain is powerful enough to develop and remember passwords that are sufficiently long, random and unique to keep all of their devices and accounts secure. A password manager generates and stores these passwords for you, protecting them with encryption.
- **Use two-factor authentication (2FA)**: Two-factor authentication adds a second factor to your login system. By using 2FA, you can make sure that even if someone manages to guess your password, they cannot log in because they still need a second factor which is harder to get.

## Create a Stronger Password

We recommend creating all passwords with an offline password manager and memorizing only a few longer passphrases for unlocking your device and password manager database.

### Password Requirements

- **Minimum length**: 12 characters (14 is even better)
- **Character variety**: Use letters, numbers, and symbols
- **Uniqueness**: Never reuse passwords across accounts

### What to Avoid

The following strategies alone **don't** make your passwords safe:

- Single dictionary words
- Common phrases, famous quotations, or song lyrics
- Words or numbers related to you or people around you (names, birthdays, addresses, pet names)

## Remember a Few Secure Passwords

Even with a password manager, you'll need to memorize a few secure passwords for your device and password manager database.

### The Diceware Method

1. Get a [list of numbered words](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) and 5 dice
2. Roll the 5 dice to get a five-digit number (e.g., 6,2,5,1,1)
3. Use the word in the list with the corresponding number
4. Repeat six times to create a six-word passphrase
5. Create a mental image using the words in order to help remember
6. Practice entering the password daily at first, then weekly

> **Note**: You can also [generate passphrases with KeePassXC](https://keepassxc.org/docs/KeePassXC_UserGuide#_generating_passphrases) if you don't have dice.

### The Book Method (Alternative)

1. Take a random book unrelated to your main activity
2. Open to a random page
3. With eyes closed, point to choose a random word
4. Repeat six times for a six-word passphrase

> **Note**: This method is less secure than diceware, especially if using a book from your office, as it creates less random passphrases.

## Sharing Passwords

**Avoid sharing passwords whenever possible.** If you must share:

- Create separate user accounts on computers and tablets instead of sharing login credentials
- For collaborative password sharing, use [KeePassXC's KeeShare feature](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_database_sharing_with_keeshare)

## Check If Your Passwords Have Been Compromised

- Search [Have I Been Pwned](https://haveibeenpwned.com/) to see if your accounts appear in known data breaches
- Even if no accounts appear, follow security best practices—many breaches go unreported

Attackers use lists of previously breached passwords to attempt access to accounts. Reusing passwords makes you particularly vulnerable.

## How Attackers Guess Passwords

### Guessing Techniques

- Using your personal information (dates, names, favorite quotes)
- Using dictionary attacks
- Slightly modifying your previously used passwords
- Brute-force software trying all possible combinations

### Observation Methods

- Finding written passwords (notes around your desk)
- Watching you type your password
- Using previously breached passwords available online

### Deception Tactics

- Installing malware to record passwords
- Phishing attacks with fake login pages
- Social engineering (pretending to be support staff or someone you know)

### Technical Attacks

- Hacking websites where your password is stored
- Stealing passwords saved in browsers
- Extracting passwords from phone apps

## Recognize Phishing Attempts

**Never give your password when someone emails, calls, or messages you.**

- Verify requests by going directly to the service's app or website
- Contact known senders through a different channel to verify requests
- Be suspicious of messages that create urgency, fear, curiosity, or pressure you to act quickly

## When to Change Your Password

**Change your password immediately if:**

- Your account, devices, or contacts appear to have been breached
- You entered your password on an untrusted, shared, or public device
- You suspect someone watched you type your password

**When responding to breach alerts:**

- Look for news reports about data breaches
- Verify alerts by checking the service provider's official website—never click links in emails or messages
- Warn others who may have been affected

> **Research note**: Frequent password changes don't necessarily improve security. People tend to make only small changes rather than creating entirely new passwords. It's more important to change passwords after confirmed breaches.

## Physical Security

### Protect Against Shoulder Surfing

- Be mindful of observers when typing passwords in public
- Check for people watching your keyboard or phone screen
- Use a privacy screen protector

Adversaries can monitor and record password entry. Authorities have studied CCTV footage to capture passwords being typed on confiscated devices.

## Avoid Biometric Unlock

Change your device settings to use password unlock instead of fingerprint or face recognition.

### Why Passwords Are Safer Than Biometrics

- You cannot change your fingerprint like you can a password
- Biometric data may be collected at airports, government offices, etc.
- Physical coercion makes biometric unlock easier to bypass than passwords

## Passkeys: When to Consider Them

Some platforms offer [passkeys](https://www.eff.org/deeplinks/2023/10/what-passkey) as an alternative to passwords.

### Passkey Advantages

- Stronger protection against phishing attacks

### Passkey Concerns

- Often rely on biometrics and cloud sharing
- Not recommended for sensitive accounts if using biometrics or cloud storage

### Passkey Options

- **Hardware security keys**: Most secure option
- **High-security chip in your device**: Good security
- **KeePassXC with browser integration**: Convenient but more exposed to browser-based attacks

## Set Safer Recovery Questions

Recovery questions help verify your identity but can be security vulnerabilities.

**Best practices:**

- Provide fake, unrelated answers
- Use random codes generated by your password manager
- Save your fake answers in your password manager

Answers to questions like "What town were you born in?" are often easy to find online. Fake answers make account hijacking harder.

## Further Reading

- EFF Surveillance Self-Defense: [Creating Strong Passwords](https://ssd.eff.org/en/module/creating-strong-passwords)
- [10,000 most common passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt) to avoid
- Wikipedia: [Passwords](https://en.wikipedia.org/wiki/Password), [Password Strength](https://en.wikipedia.org/wiki/Password_strength), [Password Cracking](https://en.wikipedia.org/wiki/Password_cracking)