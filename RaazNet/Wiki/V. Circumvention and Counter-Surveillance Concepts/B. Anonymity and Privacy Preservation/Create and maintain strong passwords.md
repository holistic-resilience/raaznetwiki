```yaml
---
title: "Create and Maintain Strong Passwords"
tags: [passwords, security, authentication, privacy, password-managers, two-factor-authentication]
category: "Password Security"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Digital Security", "Password Management", "Account Protection"]
summary: "Comprehensive guide on creating strong passwords, using password managers, and protecting accounts from common attacks."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "12 minutes"
---
```

# Create and Maintain Strong Passwords

Passwords are important tools for keeping your data and identity secure. Unfortunately, attackers know this, and they have many tricks they can use to figure out your passwords. But you can defend against those tricks by applying a few important tools and tactics.

## Protect Your Passwords

- **Use secure devices**: Always use a secure, updated, protected and trusted device to access your accounts and manage your sensitive information, including passwords.
- **Use a password manager**: No human brain is powerful enough to develop and remember passwords that are sufficiently long, random and unique to keep all devices and accounts secure. A password manager generates and stores these passwords for you, protecting them with encryption.
- **Enable two-factor authentication (2FA)**: Two-factor authentication adds a second factor to your login system. Even if someone manages to guess your password, they cannot log in because they still need a second factor which is harder to obtain.

## Create a Stronger Password

We recommend creating all passwords with an offline password manager and memorizing only a few longer passphrases for unlocking your device and password manager database.

**Password requirements:**
- Create a long password—12 characters minimum, 14 is better
- Use letters, numbers, and symbols
- Never use a single dictionary word
- Avoid common phrases, famous quotations, or song lyrics
- Don't use words or numbers related to you or people around you

**What to avoid:**
- Names of people, pets, or organizations
- Birthdays, anniversaries, or other significant dates
- Phone numbers or addresses
- Anything someone could discover through social media

## Remember a Few Secure Passwords

Even with a password manager, you'll need to memorize a few secure passwords to unlock your device and the password manager database.

### The Diceware Method

1. Get a [numbered word list](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) and 5 dice
2. Roll the 5 dice to get a five-digit number (e.g., 6,2,5,1,1)
3. Find the word in the list with the corresponding number
4. Repeat six times to create a six-word passphrase
5. Create a mental image using the words in order to help remember
6. Practice entering the password daily at first, then weekly

**Alternative methods:**
- Generate passphrases with [KeePassXC](https://keepassxc.org/docs/KeePassXC_UserGuide#_generating_passphrases)
- Use the "book method": Open a random book, close your eyes, point to select words, and repeat six times

## Sharing Passwords Safely

- Avoid sharing passwords whenever possible
- If you need shared access to a device, create separate accounts with individual passwords
- For necessary password sharing, use KeePassXC's collaborative features with [KeeShare](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_database_sharing_with_keeshare)

## Check If Your Passwords Have Been Compromised

- Search [Have I Been Pwned](https://haveibeenpwned.com/) to see if your accounts appear in known data breaches
- Even if your accounts don't appear, follow security best practices as many breaches go unreported
- Attackers use lists of breached passwords to attempt access to accounts, making password reuse particularly risky

## How Attackers Guess Passwords

**Guessing strategies:**
- Using your personal information (dates, names, favorite quotes)
- Dictionary attacks
- Modifying passwords you've used before
- Software that tries all possible combinations

**Observation methods:**
- Finding written passwords (notes around your desk)
- Watching you type your password
- Using previously breached passwords available online

**Deception techniques:**
- Installing malware to record keystrokes
- Phishing with fake login pages
- Social engineering (pretending to be support staff or someone you know)

**Technical attacks:**
- Hacking websites to steal stored passwords
- Stealing passwords saved in browsers
- Extracting passwords from phone apps

## Recognize and Avoid Phishing

**Never give your password when someone contacts you unexpectedly:**
- Go directly to the app or website to verify any requests
- Contact the supposed sender through a different channel to verify
- Be suspicious of messages that create urgency, fear, or curiosity—these are common manipulation tactics

## When to Change Your Password

**Change your password immediately if:**
- Your account, devices, or contacts have been victims of a data breach
- You entered your password on an untrusted, shared, or public device
- You suspect someone watched you type your password

**Verification steps:**
- Check news reports about data breaches
- Verify alerts by going directly to the service provider's website—never click links in suspicious emails or messages

**Note:** Research shows frequent password changes don't necessarily improve security. People tend to make small modifications rather than creating entirely new passwords. It's more important to change passwords after confirmed breaches.

## Physical Security Awareness

- In public spaces, be aware of who might see or record your screen
- Check for observers before typing passwords
- Consider using a privacy screen protector

## Avoid Biometric Unlock (Fingerprint/Face)

Change your device settings to use password unlock instead of biometrics.

**Why passwords are safer than biometrics:**
- You cannot change your fingerprint if it's compromised
- Biometric data may be collected at airports, government offices, etc.
- Adversaries can more easily force biometric unlock than extract a password from your memory

## Using Passkeys

Some platforms offer passkeys as an alternative to passwords. Passkeys provide stronger phishing protection but typically rely on biometrics or cloud sharing.

**Passkey options:**
- Password manager with passkey support
- Hardware security key
- Device's built-in security chip
- [KeePassXC with browser integration](https://keepassxc.org/docs/KeePassXC_UserGuide#_passkeys) (note: browser-based solutions may be more vulnerable)

Consider passkeys if you face advanced phishing threats, but be aware of the trade-offs with biometrics and cloud storage.

## Set Safer Recovery Questions

- Provide fake, unrelated answers to security questions
- Consider using random codes generated by your password manager
- Save your fake answers in your password manager to avoid lockouts

Answers to questions like "What town were you born in?" are often discoverable online. Fake answers make it harder for attackers to hijack your account.

## Further Reading

- EFF Surveillance Self-Defense: [Creating Strong Passwords](https://ssd.eff.org/en/module/creating-strong-passwords)
- [10,000 Most Common Passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt) (avoid these)
- Wikipedia: [Password Strength Guidelines](https://en.wikipedia.org/wiki/Password_strength)