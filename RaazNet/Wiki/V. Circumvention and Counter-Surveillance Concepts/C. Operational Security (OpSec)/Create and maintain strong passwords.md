---
title: "Create and Maintain Strong Passwords"
tags: [passwords, security, authentication, password-managers, two-factor-authentication]
category: "Password Security"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Digital Security", "Authentication", "Password Management"]
summary: "Comprehensive guide on creating strong passwords, using password managers, and protecting accounts from common attacks."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "12 minutes"
---

# Create and Maintain Strong Passwords

Passwords are important tools for keeping your data and identity secure. Unfortunately, attackers know this, and they have many tricks they can use to figure out your passwords. You can defend against those tricks by applying a few important tools and tactics.

## Protect Your Passwords

- **Use a secure device**: Always use a secure, updated, protected and trusted device to access your accounts and manage your sensitive information, including passwords.
- **Use a password manager**: No human brain is powerful enough to develop and remember passwords that are sufficiently long, random and unique to keep all devices and accounts secure. A password manager generates and stores these passwords for you, protecting them with encryption.
- **Use two-factor authentication (2FA)**: Two-factor authentication adds a second factor to your login system. Even if someone guesses your password, they cannot log in because they still need a second factor which is harder to obtain.

## Create a Stronger Password

We recommend creating all passwords with an offline password manager and memorizing only a few longer passphrases to unlock your device and password manager database.

**Password requirements:**
- Create a long password—12 characters minimum, 14 is better
- Use letters, numbers, and symbols
- Don't rely solely on these strategies to make passwords safe; add them to an already strong password

**Avoid these common mistakes:**
- Using a single dictionary word
- Using common phrases, famous quotations, or song lyrics
- Using words or numbers related to you or people around you (names, birthdays, addresses)

## Remember a Few Secure Passwords

Even with a password manager, you need to memorize passwords for unlocking your device and the password manager database.

### The Diceware Method

1. Get a [numbered word list](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt) and 5 dice
2. Roll the 5 dice to get a five-digit number (e.g., 6,2,5,1,1)
3. Find the corresponding word in the list
4. Repeat six times to create a six-word passphrase
5. Create a mental image using the words in order to help remember
6. Practice entering the password daily at first, then weekly

**Alternative: The Book Method**
1. Take a random book unrelated to your main activity
2. Open to a random page
3. With eyes closed, point to choose a random word
4. Repeat six times for a six-word passphrase

*Note: The book method is less secure than diceware, especially if using a book from your office, as it creates less random passphrases.*

## Sharing Passwords

- **Avoid sharing passwords whenever possible**
- If you must share, set up KeePassXC for collaborative use with KeeShare
- On iOS devices, password sharing options are limited (available only on iPad via Shared iPad)

## Check If Your Passwords Have Been Compromised

- Search [Have I Been Pwned](https://haveibeenpwned.com/) to see if your accounts appear in known data breaches
- Even if your accounts don't appear, follow security best practices—many breaches go unreported

Attackers use lists of previously breached passwords and try them against your accounts. Reusing passwords is particularly risky.

## How Attackers Guess Passwords

**Guessing methods:**
- Using your personal information (dates, names, favorite quotes, songs)
- Using dictionary attacks
- Modifying your previous passwords
- Brute-force software trying all possible combinations

**Observation methods:**
- Finding written passwords (notes around your desk)
- Watching you type
- Using previously breached passwords available online

**Deception methods:**
- Installing malware to record passwords
- Phishing attacks with fake login pages
- Social engineering (pretending to be support staff or someone you know)

**Technical methods:**
- Hacking websites where you have accounts
- Stealing passwords stored in browsers
- Extracting passwords from phone apps

## Never Give Your Password to Unsolicited Requests

If someone contacts you via email, call, or message requesting your password:

- Go directly to the app or website to verify the request
- Contact the person or organization through a different channel to confirm
- Be suspicious of messages creating urgency, fear, curiosity, or fear of missing out—these are common phishing tactics

Attackers often impersonate banks or technical support to obtain sensitive information.

## When to Change Your Password

**Change your password immediately if:**
- Your account, devices, or colleagues appear to have been breached
- You entered your password on an untrusted, shared, or public device
- You suspect someone watched you type your password

**Best practices:**
- Warn others who may have been affected
- Monitor news reports about data breaches
- Verify breach alerts by checking the service provider's official website—never click links in suspicious emails or messages

**Note on frequent changes:** Research shows that requiring frequent password changes doesn't improve security—people tend to make only small modifications. It's more important to change passwords after confirmed breaches. For online services, consider changing passwords every few months to a year, or immediately when compromise is suspected.

## Physical Security When Typing Passwords

- In public spaces, be aware of who can see or record you from behind
- Check for anyone watching your keyboard or phone screen
- Use a privacy screen protector to obscure your display

Adversaries can study CCTV footage to capture passwords being typed on unlocked devices.

## Avoid Biometric Authentication (Fingerprint/Face Unlock)

Change your device settings to use password unlock instead of biometrics.

**Why:**
- You cannot change your fingerprint like you can change a password
- Biometric data may be collected at airports, government offices, etc.
- Adversaries who physically restrain you can more easily unlock biometric-protected devices

## Passkeys: When to Consider Them

Some platforms offer passkeys as an alternative to passwords. Passkeys provide stronger phishing protection but typically rely on biometrics and cloud sharing.

**If you face advanced phishing threats**, passkeys may be worth considering. Use them without biometrics or cloud sharing for better security.

**Passkey storage options:**
- Password manager with passkey support
- Hardware security key
- High-security chip in your computer or phone
- KeePassXC with browser integration (note: browser-based solutions are more vulnerable to browser attacks)

## Set Safer Recovery Questions

- Provide fake, unrelated answers to security questions
- Consider using random codes generated by your password manager
- Save your fake answers in your password manager to avoid lockouts

Recovery questions like "What town were you born in?" or "What is your pet's name?" can often be discovered through social media or public records.

## Further Reading

- EFF Surveillance Self-Defense: [Creating Strong Passwords](https://ssd.eff.org/en/module/creating-strong-passwords)
- [The 10,000 Most Common Passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt) - avoid using anything on this list
- Wikipedia: [Passwords](https://en.wikipedia.org/wiki/Password), [Password Strength Guidelines](https://en.wikipedia.org/wiki/Password_strength), [Password Cracking](https://en.wikipedia.org/wiki/Password_cracking)