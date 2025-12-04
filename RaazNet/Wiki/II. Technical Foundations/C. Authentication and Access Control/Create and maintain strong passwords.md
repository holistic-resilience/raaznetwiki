---
title: "Create and Maintain Strong Passwords"
tags: [passwords, security, authentication, password-managers, two-factor-authentication]
category: "Authentication"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["Digital Security", "Password Management", "Account Protection"]
summary: "Comprehensive guide to creating, managing, and protecting strong passwords using best practices and tools."
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
- **Use a password manager**: No human brain is powerful enough to develop and remember passwords that are sufficiently long, random and unique to keep all devices and accounts secure. A password manager generates and stores these passwords for you, protecting them with encryption.
- **Use two-factor authentication (2FA/MFA)**: Two-factor authentication adds a second factor to your login system. Even if someone manages to guess your password, they cannot log in because they still need a second factor which is harder to get.

## Create a Stronger Password

We recommend creating all passwords with an offline password manager and memorizing only a few longer passphrases for unlocking your device and password manager database.

**Password requirements:**
- Minimum 12 characters (14 is better)
- Use letters, numbers, and symbols
- Make it unique for each account

**What to avoid:**
- Single dictionary words
- Common phrases, famous quotations, or song lyrics
- Words or numbers related to you or people around you (names, birthdays, addresses)

## Remember a Few Secure Passwords

Even with a password manager, you'll need to memorize a few secure passwords for your device and password manager database.

### The Diceware Method

1. Get [a numbered word list](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) and 5 dice
2. Roll the 5 dice to get a five-digit number (e.g., 6,2,5,1,1)
3. Find the corresponding word in the list
4. Repeat six times to create a six-word passphrase
5. Create a mental image using the words to help remember the phrase
6. Practice entering the password daily at first, then weekly

**Alternative methods:**
- Generate a passphrase with [KeePassXC](https://keepassxc.org/docs/KeePassXC_UserGuide#_generating_passphrases)
- Use the "book method": Open a random book to random pages and blindly select 6 words (less secure but works without software)

## Sharing Passwords

Avoid sharing passwords whenever possible. If you must share:
- On iOS devices, password sharing is only available on iPads via Shared iPad
- Use KeePassXC's collaborative features via [KeeShare](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_database_sharing_with_keeshare)

## Check If Your Passwords Have Been Compromised

- Search [Have I Been Pwned](https://haveibeenpwned.com/) to see if your accounts appear in known data breaches
- Even if your accounts don't appear, follow password best practices since many breaches go unreported

Attackers use lists of breached passwords to attempt access to accounts. Reusing passwords makes this attack particularly effective.

## How Attackers Guess Passwords

**Guessing techniques:**
- Using your personal information (dates, names, favorite quotes)
- Dictionary attacks
- Modifying passwords you've used before
- Brute force software trying all possible combinations

**Observation methods:**
- Finding written passwords (notes around your desk)
- Watching you type your password
- Using previously breached passwords

**Deception tactics:**
- Installing malware to record passwords
- Phishing attacks with fake login pages
- Social engineering (pretending to be support staff)

**Technical attacks:**
- Hacking websites to steal stored passwords
- Stealing passwords from browsers
- Extracting passwords from phone apps

## Recognize Phishing Attempts

If someone emails, calls, or messages you requesting your password:

- Go directly to the app or website to verify the request
- Contact the person through a different channel to confirm
- Be suspicious of messages creating urgency, fear, or excitement—these are common phishing tactics

Never click links in emails, SMS, or chat messages asking for your password.

## When to Change Your Password

**Change immediately if:**
- Your account, device, or colleagues appear to have been breached
- You entered your password on an untrusted, shared, or public device
- You suspect someone watched you type your password

**Verify breach alerts:**
- Check news reports about data breaches
- Verify alerts by going directly to the service provider's website

**Note:** Research shows frequent password changes don't improve security—people tend to make only small modifications. Change passwords when there's a specific reason, or periodically every few months to a year for important online services.

## Physical Security

When typing passwords in public:
- Check if anyone can see your keyboard or screen
- Be aware of cameras that might record your typing
- Use a privacy screen protector

Adversaries may study CCTV footage to capture passwords being typed.

## Avoid Biometric Unlock

Change your device settings to use password unlock instead of fingerprint or face recognition.

**Why biometrics are risky:**
- You cannot change your fingerprint or face like a password
- Biometric data may be collected at airports or government offices
- Someone can physically force you to unlock with biometrics more easily than extracting a password

## Passkeys

Some platforms offer passkeys as an alternative to passwords. Passkeys provide stronger phishing protection but often rely on biometrics and cloud sharing.

**If you choose to use passkeys:**
- Use a password manager with passkey support, a security key, or your device's security chip
- You can store passkeys with [KeePassXC browser integration](https://keepassxc.org/docs/KeePassXC_UserGuide#_passkeys), though browser-based solutions have additional attack surface

## Set Safer Recovery Questions

Recovery questions help verify your identity but can be security weaknesses.

**Best practices:**
- Provide fake, unrelated answers
- Use random codes generated by your password manager
- Save your responses in your password manager to avoid lockouts

Answers to questions like "What town were you born in?" are often easy to find online.

## Further Reading

- EFF Surveillance Self-Defense: [Creating Strong Passwords](https://ssd.eff.org/en/module/creating-strong-passwords)
- [10,000 Most Common Passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt) - avoid using anything on this list
- Wikipedia: [Passwords](https://en.wikipedia.org/wiki/Password), [Password Strength](https://en.wikipedia.org/wiki/Password_strength), [Password Cracking](https://en.wikipedia.org/wiki/Password_cracking)