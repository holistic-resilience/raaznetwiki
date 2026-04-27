---
title: "Strong Password Fundamentals"
tags:
  [
    passwords,
    authentication,
    security,
    privacy,
    diceware,
    entropy,
    iran-security,
  ]
category: "Authentication & Access Control"
difficulty: "Beginner"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "Digital Security",
    "Password Management",
    "Account Protection",
    "Threat Mitigation",
  ]
summary: "A comprehensive guide to understanding, creating, and maintaining strong passwords, tailored to the Iranian digital security context."
source: "Raaznet Aggregated Resources"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "10 minutes"
---

# Strong Password Fundamentals

Passwords are the first line of defense in digital security. They act as the "keys" to your digital identity, protecting everything from private conversations and photos to financial assets and sensitive operational data. In the context of Iran, where users face targeted surveillance, state-sponsored phishing, and device seizures, the strength of your passwords is critical.

This guide explains the mechanics of strong passwords, how attackers attempt to crack them, and the most secure methods for creating credentials you can actually remember.

## The Core Principles of Password Strength

For years, users were told to use "complex" passwords like `P@ssw0rd1!`. Modern security standards (such as NIST 2025 guidelines) have shifted. Today, **length** and **uniqueness** are far more important than complexity.

### 1. Length vs. Complexity

Mathematical entropy (randomness) increases significantly with length. A short password with symbols is easier for a computer to crack than a long phrase of random words.

- **Weak:** `Tr0ub4dor&3` (Hard for humans to remember, easy for computers to guess).
- **Strong:** `correct horse battery staple` (Easy for humans to remember, hard for computers to guess).

**Recommendation:** Your passwords should be at least **12-16 characters** long. For critical encryption keys (like your BitLocker or VeraCrypt password), aim for 20+ characters.

### 2. Uniqueness

You must use a **unique** password for every single account.

- **The Risk:** If you use the same password for Instagram and a small online shop, and the shop gets hacked, attackers will immediately try that password on your Instagram, Gmail, and Twitter. This is called **Credential Stuffing**.
- **The Solution:** Never reuse passwords.

### 3. Entropy (Randomness)

A password must be unpredictable. Humans are terrible at being random; we predictably capitalize the first letter, use the year (e.g., `2024`) at the end, or use simple patterns like `qwerty`. Secure passwords rely on true randomness.

---

## How to Create Strong Passwords

We recommend two different strategies depending on whether you need to memorize the password or not.

### Strategy A: Machine-Generated Passwords (For 99% of Accounts)

For almost all your accounts (Twitter, Email, Digikala, Snapp), you should **not** know your password. You should use a **Password Manager** to generate and store a random string of characters.

- **Example:** `X7f!m9#L2$pQz@v4`
- **How to use:** Copy and paste this using your password manager.
- **Why:** It is mathematically impossible to guess and protects you from dictionary attacks.

> [!INFO]
> See our guide on [Secure-Password-Storage-and-Managers](secure-password-storage-and-managers) to choose the right tool for this.

### Strategy B: Diceware Passphrases (For Master Passwords)

You still need to memorize a few passwords: your **Password Manager Master Password**, your **Phone/Laptop Lock Screen**, and your **Disk Encryption Key**. For these, use the **Diceware** method.

**What is Diceware?**
Diceware creates a "passphrase" by selecting random words from a numbered list.

1.  **Roll a die:** Roll a standard 6-sided die five times to get a 5-digit number (e.g., `4-1-2-5-3`).
2.  **Lookup:** Find the word corresponding to `41253` in a standardized word list (e.g., the EFF Wordlist).
3.  **Repeat:** Do this 6 or 7 times.

**Result Example:** `viewable fastness reluctant squishy seventeen shown pencil`

**Why it works:**

- **High Entropy:** A 7-word phrase from a 7,776-word list has ~90 bits of entropy, making it resistant to brute-force attacks by even powerful state actors.
- **Memorability:** It is easier to remember a story involving these words than a complex string like `G7*b9!x`.

---

## Context-Specific Security: What to Avoid in Iran

Attackers in Iran often use localized dictionaries and social engineering data to crack passwords. Avoid the following specifically:

### 1. Avoid "Finglish"

Many Iranian users create passwords by typing Persian words using English letters (Finglish) or mapping Persian keyboard characters to English keys (e.g., typing `sibzamini` or key-walking based on Persian layout).

- **Risk:** Iranian hackers and state-sponsored groups use specialized "Finglish" wordlists in their brute-force tools. These are cracked as easily as standard English words.

### 2. Avoid Personal Identity Information

Do not use any part of your:

- **National ID (Code Melli)**
- **Birth Certificate Number (Shenasnameh)**
- **Mobile Number**
- **Birth Year (1360, 1375, etc.)**

Iranian databases containing this information are frequently leaked or accessible to state actors. A password containing `1370` or the last 4 digits of a mobile number is insecure.

### 3. Avoid Common Iranian Patterns

- Names of Iranian football teams (Persepolis/Esteghlal).
- Common names (Ali, Maryam, Mohamad) followed by `123`.
- Religious terms or famous poetry verses.

---

## Understanding Attack Methods

To defend yourself, you must understand how adversaries attempt to break in.

### 1. Brute Force & Dictionary Attacks

Attackers use software to try millions of combinations per second.

- **Dictionary Attack:** Tries every word in the dictionary (English and Persian/Finglish).
- **Brute Force:** Tries every possible character combination (`aaaa`, `aaab`, etc.).
- **Defense:** Length is the best defense. Each added word or character exponentially increases the time required to crack the password.

### 2. Credential Stuffing / Password Spraying

- **Stuffing:** Attackers take a leaked database (e.g., from a hacked forum) and try those exact email/password pairs on Telegram or Google.
- **Spraying:** Attackers try one common password (like `Tehran1403`) against thousands of different user accounts to avoid lockouts.
- **Defense:** Unique passwords for every site.

### 3. Phishing (Social Engineering)

Attackers send fake SMS (e.g., fake "Sana" judicial notices) or emails tricking you into typing your password on a fake page.

- **Defense:** Password Managers help here—they will not auto-fill your password if the website URL is not an exact match (e.g., `g00gle.com` instead of `google.com`).

### 4. Keylogging & Physical Observation

- **Keyloggers:** Malware recording your keystrokes.
- **Surveillance:** In Iran, be cautious of CCTV cameras in cafes or public spaces that could record you typing your password.
- **Defense:** Keep devices malware-free and shield your keyboard when typing in public.

---

## Password Maintenance

### Do Not Rotate Arbitrarily

Old advice suggested changing passwords every 90 days. **This is now considered bad practice** (NIST 2025). Frequent forced changes cause users to choose weaker passwords (changing `Tehran1` to `Tehran2`).

- **When to change:** Only change a password if you suspect the account was compromised or if a service announces a data breach.

### Check for Breaches

Regularly check if your email or phone number has been part of a data breach.

- **Tool:** [Have I Been Pwned](https://haveibeenpwned.com/)
- **Action:** If your email appears in a breach, immediately change the password for that specific site.

### Recovery Questions

"Security Questions" (e.g., "What is your father's name?") are a security weakness. The answers are often public record or easy to guess.

- **Best Practice:** Treat the answer like a password. Generate a random string using your password manager and store it there.
  - _Question:_ "What is your mother's maiden name?"
  - _Answer:_ `X7f!m9#L2$pQz`

---

## Summary Checklist

1.  [ ] **Use a Password Manager** for all accounts except the few you must memorize.[cite](#tm-cite:0%7Cdefense.gov)
2.  [ ] **Create a unique password** for every single service.
3.  [ ] **Use Diceware (Passphrases)** for your Master Password and Device Encryption (minimum 6-7 random words).
4.  [ ] **Avoid Finglish** and personal data (Code Melli, mobile number).
5.  [ ] **Do not rotate** passwords unless a breach occurs.
6.  [ ] **Enable Multi-Factor Authentication (MFA)** wherever possible to add a layer beyond the password.

> **Next Step:** Now that you understand the fundamentals, you need a secure way to store these unique credentials. Proceed to [Secure-Password-Storage-and-Managers](secure-password-storage-and-managers).
