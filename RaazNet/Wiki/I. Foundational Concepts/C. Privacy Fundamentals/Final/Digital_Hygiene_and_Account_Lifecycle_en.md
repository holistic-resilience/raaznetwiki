---
title: "Digital Hygiene and Account Lifecycle"
tags:
  [
    digital-hygiene,
    account-security,
    privacy,
    opsec,
    iran-security,
    metadata,
    doxxing,
  ]
category: "Privacy Fundamentals"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, At-Risk Individuals]
topics:
  [
    "Account Management",
    "Data Minimization",
    "Threat Response",
    "Digital Footprint",
  ]
summary: "A comprehensive guide to managing your digital footprint in the Iranian context, from secure account creation and daily hygiene to anti-doxxing measures and safe account deletion."
source: "Consolidated from Privacy Guides, Tactical Tech, and Certfa"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of account settings", "Password Manager installed"]
estimated_read_time: "15 minutes"
---

# Digital Hygiene and Account Lifecycle

"Digital hygiene" is not just about avoiding spam; it is a critical component of operational security (OpSec). The Islamic Republic's surveillance apparatus relies heavily on correlating data points—linking a phone number to a Telegram ID, or an IP address to a physical location.

This guide covers the entire lifecycle of your digital presence, ensuring you minimize your footprint, compartmentalize your identity, and safely dispose of data when it is no longer needed.

---

## Phase 1: Secure Account Creation

The most effective way to protect your privacy is to limit the data you provide from the very beginning.

### 1. Identity Compartmentalization

Never use your legal identity (Real Name, National ID/Code Melli) unless absolutely required by law (e.g., banking).

- **Activist vs. Personal:** Keep your political activity completely separate from your personal life. Use different browsers, different accounts, and ideally, different devices.
- **Pseudonyms:** Use consistent pseudonyms for specific activities, but never link them to your real name.

### 2. Email Aliasing

Avoid giving your primary email address to every service. If one service is breached, your main email—and potentially your identity—is exposed.

- **Use Aliases:** Services like **SimpleLogin** (owned by Proton) or **Addy.io** allow you to create unique email addresses for every account (e.g., `shop.ir@alias.com`). These forward emails to your real inbox.
- **Benefit:** If an alias receives spam or phishing, you can disable it instantly. You also hide your real email provider from the service.

### 3. Phone Numbers and SMS Verification

In Iran, SIM cards are tied to your National ID. Using a +98 number for sensitive accounts (Telegram, Twitter/X, Signal) is a significant risk.

- **Avoid SMS 2FA:** Never use SMS for Two-Factor Authentication if an alternative (Authenticator App, Hardware Key) exists. SMS is unencrypted and easily intercepted by mobile operators (MCI, Irancell) under state pressure.
- **Virtual Numbers:** If possible, use virtual numbers (e.g., Google Voice, though difficult to obtain) or anonymous number services for account verification.
- **Signal:** Enable "Registration Lock" so your account cannot be hijacked even if your SIM is compromised.

### 4. Strong Authentication

- **Passwords:** Use a Password Manager (Bitwarden, KeePassXC, 1Password) to generate unique, complex passwords for every site.
- **2FA/MFA:** Enable Two-Factor Authentication everywhere. Prioritize TOTP apps (Aegis on Android, Raivo/Ente on iOS) over SMS.

---

## Phase 2: Routine Hygiene & Data Minimization

Digital hygiene requires regular maintenance. Set a reminder (e.g., every 3 months) to review these settings.

### 1. Google Account Hardening

If you use Android or Google services, your account holds a wealth of data.

- **Privacy Checkup:** Run Google's [Privacy Checkup](https://myaccount.google.com/privacycheckup) regularly.
- **Location History (Timeline):** Google is transitioning "Timeline" data to be stored **on-device** rather than in the cloud.
  - _Action:_ Ensure your Maps app is updated. Configure auto-delete settings (e.g., delete data older than 3 months).
  - _Risk:_ While on-device storage prevents cloud subpoenas, if your phone is seized by FATA (Cyber Police), the data is physically accessible. **Disable Location History entirely** for sensitive devices.
- **Web & App Activity:** Set this to auto-delete every 3 or 18 months.

### 2. Social Media Audits

- **Facebook Link History:** Meta recently introduced "Link History," which tracks websites you visit via the Facebook browser.
  - _Disable:_ Settings & Privacy → Settings → Browser → Turn off **Link History**.
- **Twitter/X:** Regularly delete old tweets using services like Redact.dev or Semiphemeral. Old posts can be mined for location data or sentiment analysis.
- **Telegram:**
  - Check **Active Sessions** regularly and terminate unknown devices.
  - Set **Account Self-Destruct** to the minimum period (1 month or 3 months).
  - Ensure **Phone Number** visibility is set to "Nobody".

### 3. Browser Hygiene

- **Extensions:** Minimize extensions to reduce fingerprinting and attack surface.
- **Essential Extensions:**
  - **uBlock Origin:** Essential for blocking trackers, malicious ads, and some censorship scripts.
  - **Privacy Badger:** Blocks invisible trackers.
- **Clear Data:** Configure your browser to clear cookies and site data upon exit.

---

## Phase 3: Media & Metadata Redaction

Photos and documents contain hidden data (Metadata/EXIF) that can reveal your location, device model, and time of capture. This is dangerous for protesters or journalists.

### 1. Removing Metadata

Before sharing _any_ file on a public channel:

- **Android:** Use **Scrambled Exif** (F-Droid) or **ExifEraser**. Share the photo to this app first to strip data before sending.
- **Desktop:** Use **MAT2** (Metadata Anonymisation Toolkit). It supports images, audio, and documents.
- **iOS:** Use a shortcut or an app like **Metapho** or **ViewExif** to strip location data.

### 2. Face Blurring (Anonymizing Visuals)

Simple pixelation is often reversible. Use proper redaction tools.

- **Signal:** The safest and easiest tool. Open Signal, select a photo, use the **Blur** tool to automatically hide faces. Save the photo without sending it.
- **ObscuraCam:** An older tool, but still functional for some.
- **Putmask (Android):** Effective for blurring faces in videos.

> **Warning:** Never rely on social media stickers (like an Instagram emoji over a face) for redaction. The original image data might still exist or be recoverable by the platform.

---

## Phase 4: Anti-Doxxing & Threat Response

**Doxxing** is the malicious publication of private information. In Iran, pro-regime cyber groups often doxx activists to intimidate them.

### 1. Doxxing Prevention

- **Search Yourself:** Regularly search your real name, username, and phone number on Google and DuckDuckGo to see what is public.
- **Social Lockdowns:** Set Instagram and Facebook profiles to Private. Audit your follower lists and remove unknown accounts.
- **Google Calendar Spam:** Attackers can send spam invites to your calendar to verify your email.
  - _Fix:_ Google Calendar Settings → Event Settings → "Add invitations to my calendar" → Select **"Only if the sender is known"**.

### 2. Defense Against SIM Swapping

SIM swapping occurs when an attacker (or the state) convinces the mobile carrier to transfer your number to a new SIM card, intercepting your calls and SMS codes.

- **Defense:** This is why **avoiding SMS 2FA** is critical. If your SIM is swapped but your accounts are secured with a YubiKey or TOTP app, the attacker cannot access your accounts.

---

## Phase 5: Account Disposal (End of Lifecycle)

Unused accounts are security liabilities. They contain old data and often have weak passwords.

### 1. Finding Old Accounts

- Search your email inbox for keywords like "Welcome," "Verify," "Confirm," or "Subscription."
- Check your Password Manager for old entries.

### 2. Deleting Accounts

- **JustDeleteMe:** Use [JustDeleteMe](https://justdeleteme.xyz/) to find direct deletion links for popular services.
- **Impossible Deletions:** If a service does not allow deletion (common with some forums or old sites):
  1.  Change all personal info to fake data (name, address).
  2.  Change the email to a temporary alias or throwaway address.
  3.  Change the password to a random 64-character string and discard it.

### 3. Data retention laws

Be aware that even after "deletion," companies (especially domestic Iranian platforms like Aparat, Digikala, Snapp) may be legally required to retain user logs for at least 6 months to a year for law enforcement access. Always assume data generated on domestic platforms is permanent.

---

## Checklist: Quick Digital Hygiene Audit

- [ ] **Review Active Sessions:** Check Telegram, WhatsApp, and Google for unknown devices.
- [ ] **Update Software:** Ensure OS and Browsers are on the latest versions.
- [ ] **Metadata Check:** Are you stripping location data from protest photos?
- [ ] **2FA Audit:** Are you still using SMS for critical accounts? Switch to an App.
- [ ] **Google Timeline:** Is it configured to auto-delete or disabled?
