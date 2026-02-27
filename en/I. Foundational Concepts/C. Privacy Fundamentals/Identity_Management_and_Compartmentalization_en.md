---
title: "Identity Management and Compartmentalization"
tags:
  [
    privacy,
    opsec,
    identity-management,
    compartmentalization,
    anonymity,
    iran,
    digital-footprint,
    aliasing,
  ]
category: "Foundational Concepts"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public, At-Risk Individuals]
topics:
  [
    "Operational Security",
    "Identity Separation",
    "Digital Hygiene",
    "Anti-Surveillance",
  ]
summary: "A comprehensive guide on separating digital identities to minimize risk, specifically tailored for the Iranian threat landscape. Covers compartmentalization strategies, email aliasing, phone number management, and metadata removal."
source: "Raaznet Aggregated Resources"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Understanding Digital Surveillance", "Basic Account Management"]
estimated_read_time: "20 minutes"
---

# Identity Management and Compartmentalization

In the context of the Iranian digital landscape, where the state actively correlates online activities with physical identities to suppress dissent, **Identity Management** and **Compartmentalization** are not optional luxuries—they are survival skills.

The goal is not just "privacy" in the abstract, but the prevention of **correlation**. If one aspect of your digital life is compromised (e.g., a university email account), it should not lead authorities to your anonymous activist persona on Twitter or your private communications on Signal.

## The Core Concept: Compartmentalization

Compartmentalization is the practice of separating different aspects of your life into isolated "containers" or "compartments." Think of it like a submarine: if the hull is breached in one section, you seal the bulkheads so the water doesn't flood the entire ship.

### The Three Levels of Identity

To effectively compartmentalize, you must categorize your online activities into three distinct levels. **Never mix these levels.**

#### Level 1: The "Real" You (Attributed Identity)

This identity is linked to your legal name, National ID (Code Melli), and physical address.

- **Use cases:** Banking (Shaparak), Government services (My.Gov.ir), University portals, official employment.
- **Device:** Your primary smartphone or a specific browser profile.
- **Network:** Standard domestic internet (or domestic VPNs strictly for banking).
- **Risk:** This identity is already known to the state. The goal here is **Data Minimization**—give them nothing extra.

#### Level 2: The Pseudonym (Persistent Identity)

A consistent online persona that is _not_ linked to your legal name but builds a reputation over time.

- **Use cases:** Social media (Twitter/X, Instagram), forums, general internet browsing.
- **Device:** A separate browser (e.g., Brave or Firefox with strict settings), or a separate user profile on your phone.
- **Network:** Trusted VPN (e.g., Mullvad, Proton) or Tor.
- **Rule:** Never post photos of your face, your home, or recognizable local landmarks. Never use your real mobile number for 2FA.

#### Level 3: The Ghost (Anonymous Identity)

A temporary, single-use identity for high-risk activities.

- **Use cases:** Whistleblowing, organizing protests, contacting human rights organizations, accessing sensitive news.
- **Device:** **Tails OS** (live USB), **Whonix**, or a completely "clean" burner device.
- **Network:** **Tor Bridge** (Snowflake/Meek) exclusively.
- **Rule:** Used once or for a specific operation, then destroyed. No persistent history.

---

## Technical Separation Strategies

Separating identities requires technical barriers, not just mental ones.

### 1. Browser Compartmentalization

Do not use the same browser for all activities. Cookies, cache, and browser fingerprinting can link your activities.

- **Strategy A (Multiple Browsers):** Use **Firefox** for Level 2 (Pseudonym) and **Chrome/Edge** only for Level 1 (Real ID). Use **Tor Browser** for Level 3.
- **Strategy B (Profiles):** Use Firefox "Multi-Account Containers" or Chrome "Profiles" to separate "Work," "Personal," and "Activism." This prevents cross-site tracking (e.g., Facebook seeing what you do on other tabs).

### 2. Device Isolation (Advanced)

For high-risk users (journalists/organizers):

- **Qubes OS:** An operating system that runs everything in isolated virtual machines.
- **Tails OS:** A live operating system that runs from a USB stick and forgets everything after shutdown. Mandatory for Level 3 activities.
- **Physical Separation:** Use a separate, cheap smartphone ("Burner") for secure communications. Keep it powered off and in a Faraday bag when not in use. **Never insert a SIM card registered to your name in a burner phone.**

---

## Credential & Account Management

### Email Aliasing

Your email address is a unique identifier used to track you across the web. **Never use your primary Gmail/Yahoo for every sign-up.**

- **How it works:** You use a service to generate a unique address (e.g., `shop.pizza@alias.com`) that forwards to your real inbox. If that address receives spam or is compromised, you simply disable it.
- **Recommended Tools:**
  - **SimpleLogin:** Owned by Proton. Open-source. Allows creating aliases that forward to your ProtonMail.
  - **Addy.io:** Open-source, creates anonymous forwarding addresses.
- **Use Case:** If signing up for a Persian news letter or a tool that might be monitored, use an alias. If the regime seizes the server logs of that service, they see `random-alias@simplelogin.com`, not `Firstname.Lastname@gmail.com`.

### Phone Number Management (Critical for Iran)

In Iran, purchasing a SIM card requires a National ID, meaning **your phone number is a direct link to your physical identity.**

- **The Danger:** Using your +98 number for Telegram, Signal, Twitter, or Instagram allows the telecommunications infrastructure (MCI/Irancell/Rightel) to correlate your IP address and SMS verification codes.
- **Defensive Strategy:**
  - **Never** use your +98 number for accounts unrelated to banking/government.
  - **Virtual Numbers (VoIP):** Use services like **Google Voice** (requires US verification, difficult to get) or **MySudo** (iOS focused).
  - **SMS Verification Services:** For setting up accounts (like Telegram/Twitter) where you don't need the number for calls, use anonymous SMS receive services (e.g., SMSPool, 5sim) paid via crypto. **Warning:** You may lose access to these numbers, so only use them for accounts you can secure with an email backup or 2FA app.
  - **Fragment:** For Telegram specifically, purchase an anonymous number via Fragment (TON blockchain). This removes the SIM card vulnerability entirely.

### Signal Configuration

Signal is the gold standard for communication, but requires configuration:

1.  **Hide Phone Number:** Settings > Privacy > Phone Number > Who can see my number: **Nobody**.
2.  **Registration Lock:** Settings > Account > Registration Lock. (Prevents SIM swapping or state seizure of your number to hijack your account).
3.  **Usernames:** Set a username and share _that_, not your phone number.

---

## Digital Footprint & Metadata Scrubbing

Files you create contain hidden data called **Metadata** (EXIF data).

- **What it reveals:** GPS coordinates (exact location of a protest), camera model, date/time, and device serial number.
- **Risk:** Posting a photo of a protest on Twitter can lead security forces directly to your window.

### Tools for Removal

- **Android:** Use **Scrambled Exif** (F-Droid) or **ExifEraser**. Share the photo to this app _before_ uploading to social media.
- **Desktop:** Use **MAT2** (Metadata Anonymisation Toolkit). It cleans PDFs, images, and audio files.
- **Strategy:** Remove metadata _locally_ on your device before the file ever touches the internet. Do not rely on social media platforms to "scrub" this for you.

### Doxxing Defense & Self-Audit

"Doxxing" is the publishing of private info. In Iran, "Cyber Armies" use this to intimidate activists.

- **Self-Doxing:** Regularly search for your own username, real name, and phone number. See what information is public.
- **Username Re-use:** Do not use the same username (e.g., `AzadiLover123`) on a dating site, a gaming forum, and your political Twitter. Tools like `Sherlock` or `Namechk` can link these profiles instantly.

---

## Social Engineering & AI Threats

The Islamic Republic uses sophisticated social engineering and AI to compromise targets.

- **Deepfakes & Voice Cloning:** AI can now clone voices from a 3-second audio clip.
  - **Countermeasure:** Establish a **"Family Safe Word"** (code phrase). If a family member calls you in distress asking for money or passwords, ask for the safe word. If they don't know it, hang up and call them back on a secure line.
- **Phishing:** Be skeptical of emails/SMS claiming to be from "Google Support," "Telegram Security," or "Judiciary Notices" (Sana system).
  - **Rule:** Never click links in SMS. Go directly to the official website/app.

---

## Checklist: Compartmentalization Setup

1.  [ ] **Audit:** List all your accounts. Which ones have your real name? Which ones have your +98 number?
2.  [ ] **Isolate:** Move sensitive accounts (Twitter, Telegram, Signal) off your +98 number. Use virtual numbers.
3.  [ ] **Alias:** Set up SimpleLogin or Addy.io. Replace your email on non-essential services with aliases.
4.  [ ] **Clean:** Install **Scrambled Exif** or **MAT2**. Scrub metadata from all media before sharing.
5.  [ ] **Verify:** Ensure **2FA** is enabled on everything, using an app (Aegis, Raivo, Ente Auth) or a hardware key (YubiKey), **never SMS**.
6.  [ ] **Separate:** Create a separate browser profile or use a different browser entirely for political/activist browsing.
