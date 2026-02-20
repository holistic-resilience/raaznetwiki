---
title: "Anti-Doxing and Social Footprint Reduction"
tags:
  [
    doxing,
    privacy,
    osint,
    social-engineering,
    operational-security,
    identity-management,
    metadata,
    iran-security,
  ]
category: "Anonymity and Privacy"
difficulty: "Intermediate"
audience: [Activists, Journalists, Political Dissidents, General Iranian Public]
topics:
  [
    "Digital Footprint Analysis",
    "Identity Separation",
    "Social Media Hardening",
    "Metadata Removal",
    "Crisis Response",
  ]
summary: "A comprehensive guide to reducing your digital footprint and protecting against doxing attacks, specifically tailored for the Iranian threat landscape."
content_type: "Guide"
security_level: "High"
last_updated: "2026-02-17"
---

# Anti-Doxing and Social Footprint Reduction

**Doxing** (dropping documents) is the act of researching and publicly broadcasting private or identifying information (PII) about an individual or organization.

In the context of Iran, doxing is not just harassment; it is often a precursor to state repression. Information gathered by state-affiliated actors (cyber armies, Basij) or vigilantes can lead to interrogation, arrest, forced confessions, and physical harm. Reducing your social footprint is a critical preventative measure to break the link between your online activity and your physical identity.

## I. Understanding the Threat Landscape

### What Information is Targeted?

Adversaries typically seek to link an anonymous activist profile to a real-world identity using:

- **Phone Numbers:** In Iran, SIM cards are strictly tied to National IDs (_Code Melli_). A leaked phone number is a direct path to your home address.
- **Photos/Videos:** Facial recognition and background landmarks (shops, street signs) in photos.
- **Metadata:** Hidden GPS coordinates in images or device identifiers in files.
- **Social Graphs:** Who you interact with publicly on Instagram or X (Twitter).
- **Username Reuse:** Using the same handle for a political account and a gaming or hobby account.

---

## II. Self-Doxing: Auditing Your Footprint

Before you can hide, you must know what is visible. "Self-doxing" involves searching for yourself as an attacker would.

### 1. Search Engine Reconnaissance (Google Dorks)

Perform these searches using a privacy-focused browser (like Tor or Brave) and a VPN. Do not be logged into your own Google account.

- `"Your Real Name"` (in Persian and English)
- `"Your Username"`
- `"0912..."` (Your phone number in various formats: +98, 0098, with/without dashes)
- `"Your Name" site:instagram.com`
- `"Your Name" site:twitter.com`
- `"Your Name" filetype:pdf` (Checks for public documents/resumes)

### 2. Reverse Image Search

If you use a static profile picture across multiple accounts, an attacker can link them.

- Use **Google Images**, **Yandex Images** (very strong for facial recognition), or **PimEyes** (facial search) to see where your photos appear.
- If your face appears on a university website or old blog linked to your name, and that same photo is on your anonymous Twitter, the link is established.

### 3. Compromised Database Check

Iran has suffered massive data breaches (banks, ride-sharing apps, food delivery services). Check if your email or phone number has been exposed in known breaches using:

- [Have I Been Pwned](https://haveibeenpwned.com/)

---

## III. Reducing Your Footprint

### 1. Compartmentalization and Pseudonymity

The most effective defense is separating your identities.

- **The Air-Gap Strategy:** Never mix your "Personal/Family" identity with your "Activist" identity.
  - Use different browsers (e.g., Firefox for personal, Tor/Mullvad Browser for activism).
  - Use different email addresses (e.g., Gmail for banking, Proton/Tuta for activism).
  - **Crucial:** Never use your personal Iranian SIM card for 2FA on activist accounts. Use a virtual number (Google Voice) or a dedicated foreign SIM if available.

### 2. Metadata Management & File Sanitization

Files carry invisible data (EXIF) that can reveal your location, camera model, and time.

- **Photos:** Before posting images (especially of protests), remove metadata.
  - **Android:** Use [Scrambled Exif](https://f-droid.org/packages/com.cannibal_tux.scrambled/).
  - **Desktop:** Use [MAT2](https://0xacab.org/jvoisin/mat2) or [ExifCleaner](https://exifcleaner.com/).
  - **Manual:** Take a screenshot of the photo and post the screenshot. Screenshots usually generate new metadata without the original GPS tags.
- **Visual Sanitization:**
  - Blur faces, tattoos, and unique street landmarks using tools like **ObscuraCam** or the blur tool in **Signal**.
  - _Warning:_ Do not use simple "swirl" or transparent marker tools; these can sometimes be reversed. Use solid blocks or emojis to cover sensitive details.

### 3. Phone Number Hygiene

In Iran, your phone number is your digital national ID.

- **Telegram:** Go to Settings > Privacy and Security > Phone Number. Set "Who can see my phone number" to **Nobody** and "Who can find me by my number" to **My Contacts** (or Nobody if available).
- **Signal:** Enable **Registration Lock** (PIN) so your number cannot be hijacked via SIM swapping. Set phone number visibility to **Nobody**.
- **WhatsApp:** Avoid for high-risk activism if possible, as hiding your number is harder in groups. If used, set all privacy settings to "My Contacts" or "Nobody."

---

## IV. Hardening Social Media (Iranian Context)

### Instagram

Instagram is widely used in Iran and heavily monitored.

- **Private Account:** Keep personal accounts private. Remove followers you do not know.
- **Tagging:** Go to Settings > Privacy > Tags. Select "Manually approve tags." This prevents others from identifying you in their photos without your consent.
- **Location History:** Never use the "Add Location" feature on posts from your home or secret workspaces.
- **Bio:** Do not list your university, workplace, or city in your bio.

### X (Twitter)

- **Protect your Tweets:** If your account is personal, lock it.
- **Old Tweet Scrub:** Use services like `Redact.dev` or `TweetDelete` to wipe old posts that might contain identifying info (like birthdays or location check-ins) from years ago.
- **Two-Factor Authentication (2FA):** Switch from SMS 2FA (vulnerable to state interception) to an Authenticator App (Aegis, Raivo, Google Auth) or a Security Key.

### Telegram

- **People Nearby:** Ensure "People Nearby" is **OFF**. This feature can triangulate your exact location.
- **P2P Calls:** Go to Settings > Privacy > Calls > Peer-to-Peer. Set to **Nobody**. P2P calls expose your IP address to the caller.
- **Forwarded Messages:** Set "Who can add a link to my account when forwarding my messages" to **Nobody**. This prevents people from clicking your name in a forwarded message to find your profile.

---

## V. Response Strategy: What to do if Doxed

If your personal information is published by regime-affiliated accounts (e.g., Adl Ali, Gerdab):

1.  **Lock Down Immediately:** Switch all social accounts to private. Temporarily deactivate accounts if the heat is intense.
2.  **Change Credentials:** Change passwords and ensure 2FA is active (App-based, not SMS).
3.  **Do Not Engage:** Do not reply to the doxer. This increases visibility and confirms they have the right target.
4.  **Document Evidence:** Take screenshots of the doxing posts, but do so safely. This serves as evidence for international human rights organizations or asylum claims later.
5.  **Alert Trusted Contacts:** Inform family and close friends that you have been targeted so they do not accidentally reveal more info about you (e.g., "I saw your address online, are you okay?").
6.  **Physical Safety:** If your home address is leaked, stay with a friend or relative for a few days if possible. Vary your routine.
7.  **Do Not Contact Local Police (FATA):** In the context of political doxing in Iran, the cyber police are often part of the apparatus targeting you. Seek help from trusted digital security helplines (e.g., Access Now, Filterwatch) instead.

---

## VI. Recommended Tools Summary

| Category      | Tool                           | Function                                           |
| :------------ | :----------------------------- | :------------------------------------------------- |
| **Browser**   | **Tor Browser**                | Anonymous browsing for self-auditing.              |
| **Metadata**  | **MAT2** / **ExifCleaner**     | Removes GPS/Device data from files.                |
| **Redaction** | **ObscuraCam** / **Signal**    | Blurs faces and identifying features securely.     |
| **Search**    | **Yandex Images**              | Powerful reverse image search to find your photos. |
| **Cleanup**   | **Redact.dev**                 | Automates deleting old social media history.       |
| **Identity**  | **SimpleLogin** / **AnonAddy** | Creates email aliases to protect your real email.  |

---

_This guide is part of the Raaznet Wiki. Always access this information through a secure connection (VPN/Tor)._
