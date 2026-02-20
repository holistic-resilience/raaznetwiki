---
title: "Doxxing Prevention and Response"
tags:
  [
    doxxing,
    privacy,
    digital-security,
    online-harassment,
    social-media,
    iran,
    personal-safety,
  ]
category: "Privacy Fundamentals"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public, Privacy-Conscious Users]
topics:
  [
    "Doxxing Defense",
    "Online Harassment",
    "Identity Protection",
    "Crisis Response",
  ]
summary: "A comprehensive guide on preventing doxxing through digital hygiene and identity compartmentalization, with actionable steps for responding to harassment campaigns in the Iranian context."
source: "Raaznet Aggregated Resources"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of social media settings",
    "Familiarity with privacy concepts",
  ]
estimated_read_time: "15 minutes"
---

# Doxxing Prevention and Response

**Doxxing** (dropping documents) is the act of researching and publicly broadcasting private or identifying information (PII) about an individual or organization. In the context of Iranian digital security, doxxing is frequently weaponized by state-sponsored actors, vigilante groups, and cybercriminals to intimidate activists, journalists, and dissenters. The goal is often to incite harassment, silence opposition, or facilitate physical arrest.

This guide outlines proactive measures to minimize your digital footprint and reactive strategies to mitigate harm if you are targeted.

---

## Part 1: Prevention and Hardening

The most effective defense against doxxing is **prevention**—making it difficult for adversaries to link your online activities to your physical identity.

### 1. Self-Doxxing (Audit Your Footprint)

To defend yourself, you must think like an attacker. Regularly search for your own information to see what is publicly available.

- **Search Engines:** Use Google, Bing, and DuckDuckGo. Search for:
  - Your full legal name (in Persian and English).
  - Your usernames/handles.
  - Your email addresses and phone numbers.
  - Your home address (if previously shared).
  - _Tip:_ Use quotation marks (e.g., `"Name Surname"`) for exact matches.
- **Reverse Image Search:** Use Google Images, TinEye, or Yandex to see if your profile photos appear elsewhere or link to real-name accounts.
- **Leaked Database Check:** Iranian users are frequently exposed in massive data breaches (e.g., ride-sharing apps, banks, food delivery services). Check if your email or phone number has been compromised using tools like [Have I Been Pwned](https://haveibeenpwned.com/). While you cannot remove data from a leaked database, knowing it exists helps you assess your risk.

### 2. Social Media Lockdown

Social media is the primary source of data for doxxers.

- **Instagram (Critical in Iran):**
  - Set your account to **Private**.
  - Remove location tags from old posts.
  - Audit your followers: Remove accounts you do not know or trust.
  - Disable "Activity Status" to hide when you are online.
  - Avoid sharing photos of landmarks near your home or workplace.
- **X (formerly Twitter):**
  - If using an anonymous account for activism, ensure it is not linked to your real phone number or email address accessible by contacts.
  - Disable "Let others find you by your email" and "Let others find you by your phone" in _Settings and privacy > Privacy and safety > Discoverability and contacts_.
  - Periodically delete old tweets using tools like Redact or TweetDelete.
- **Telegram:**
  - **Hide Your Phone Number:** This is vital. Go to _Settings > Privacy and Security > Phone Number_. Set "Who can see my phone number" to **Nobody** and "Who can find me by my number" to **My Contacts**.
  - Disable "Forwarded Messages" attribution to prevent people from clicking your name in forwarded posts to find your profile.
  - Use a generic profile photo (not your face) if you are in public channels.
  - **2FA:** Enable Two-Step Verification (Cloud Password) to prevent account hijacking via SMS interception.

### 3. Identity Compartmentalization

Separate your online identities to prevent cross-contamination.

- **Pseudonymity:** Use a pseudonym for activism that is distinct from your legal name. Do not mix the two.
- **Separate Accounts:** Use different email addresses and profile photos for your professional life, personal life, and activism.
- **Burner Numbers:** Avoid using your primary Iranian SIM card for sensitive social media registration if possible. If you must use a phone number, consider virtual numbers (e.g., Google Voice) if you can secure one safely, or ensure your privacy settings hide the number completely.

### 4. Metadata Scrubbing

Files contain invisible data called **metadata** (EXIF data) that can reveal your location, device model, and time of creation.

- **Photos & Videos:** Before posting media anonymously, remove metadata.
  - **Tools:** Use **Scrambled Exif** (Android), **Metapho** (iOS), or **MAT2** (Desktop).
  - _Note:_ Most major social platforms (Instagram, Twitter, Telegram) strip metadata upon upload, but sending files as "Documents" or via email retains it.
- **Screenshots:** Be careful when posting screenshots. They often contain status bar icons, time, or other UI elements that can fingerprint your device or reveal your location/time zone. Crop heavily or use a scrubbing tool.

### 5. Account Security

Doxxing often starts with a hacked account.

- **Strong Passwords:** Use a password manager (e.g., Bitwarden, KeePassXC) to generate unique, complex passwords for every site.
- **2FA:** Enable Two-Factor Authentication (2FA) on everything. Prefer **Authenticator Apps** (Raaz, Google Authenticator, Aegis) over SMS, as SMS interception is a common threat in Iran.

---

## Part 2: Response Strategy (If You Are Doxxed)

If your personal information is published, immediate action is crucial to minimize harm.

### 1. Immediate Triage (First 24 Hours)

- **Do Not Panic:** Fear is the attacker's goal. Take a deep breath.
- **Lock Down Everything:** Immediately change your social media accounts to private. Temporarily deactivate accounts if the harassment is overwhelming.
- **Change Passwords:** If the doxxing includes account credentials, change passwords immediately and enable 2FA.
- **Alert Trusted Contacts:** Inform family, close friends, or colleagues that you are being targeted so they do not accidentally share more information or click malicious links sent by imposters.

### 2. Documentation

You need evidence for reporting and potential legal protection.

- **Screenshots:** Capture everything. Include the URL, the date/time, and the profile of the attacker.
- **Save URLs:** Copy the direct links to the posts or profiles. Use archiving services (like Archive.today) if you can do so safely without linking it to your IP (use Tor/VPN), but be aware this makes the harassment permanently public. _Caution is advised._

### 3. Reporting and Takedowns

- **Social Media Platforms:** Report the specific posts for violating "Terms of Service" regarding "Private Information" or "Harassment."
  - _Twitter/X:_ Report for "Posting private information."
  - _Instagram:_ Report for "Bullying or Harassment."
  - _Telegram:_ Report channels or users engaging in coordinated harassment.
- **Google Search:** If sensitive personal data (like national ID numbers, bank details, or handwritten signatures) appears in search results, you can file a [removal request with Google](https://support.google.com/websearch/answer/9673730).

### 4. Physical Safety Assessment (Iranian Context)

In Iran, doxxing can lead to state attention.

- **Assess the Source:** Is this a personal dispute, or is it politically motivated (e.g., "Arzeshi" cyber-armies)?
- **State Threats:** If the doxxing reveals your location and you are an activist, consider relocating temporarily. Do not stay at the address published.
- **Law Enforcement:** Be extremely cautious about contacting Iranian police (FATA) if the harassment is political, as this may expose you to further interrogation. If the harassment is non-political (e.g., a stalker), FATA may be able to assist, but proceed with caution and consult a trusted lawyer first.

### 5. Psychological Support

Online harassment is traumatic.

- **Disengage:** Do not reply to harassers. It fuels the fire and increases visibility.
- **Seek Support:** Connect with trusted networks or mental health professionals who understand digital trauma.

---

## Part 3: Advanced Considerations

### WHOIS Protection

If you run a website or blog (e.g., WordPress), ensure **WHOIS Privacy Protection** is enabled. Without it, your full name, address, and phone number are visible to anyone who looks up your domain.

### Data Brokers and "People Search" Sites

While vast commercial "people search" engines (like Whitepages) are primarily a US phenomenon, Iranian data often circulates on Telegram channels and dark web forums ("Leak Markets").

- You cannot "opt-out" of a criminal leak channel. Your defense is **changing the compromised credential** (e.g., changing passwords, getting a new SIM card if harassment is severe).
- For those in the diaspora: Use services like **EasyOptOuts** or **Optery** to scrub your data from Western data brokers that might be used by transnational repression agents to locate you.

### Biometric Hygiene

Avoid posting high-resolution photos where your fingerprints are visible (e.g., peace signs close to the camera) or photos of your iris/retina. While advanced, biometric harvesting is an emerging threat.

## Recommended Tools

| Tool             | Purpose                                                        | Platform              |
| :--------------- | :------------------------------------------------------------- | :-------------------- |
| **Bitwarden**    | Password Manager (Securely store unique passwords)             | All                   |
| **Signal**       | Encrypted Messenger (Use face blur tool before sending photos) | Android, iOS, Desktop |
| **ObscuraCam**   | Photo obfuscation (Blur faces/metadata)                        | Android               |
| **MAT2**         | Metadata Anonymisation Toolkit                                 | Linux, Web            |
| **Aegis / Raaz** | 2FA Authenticator (Avoid SMS)                                  | Android               |
| **Tor Browser**  | Anonymous browsing for self-doxing checks                      | Desktop, Android      |

---

**Disclaimer:** This guide provides educational information on digital security. In high-risk situations involving state actors, no tool can guarantee 100% safety. Always assess your specific threat model.
