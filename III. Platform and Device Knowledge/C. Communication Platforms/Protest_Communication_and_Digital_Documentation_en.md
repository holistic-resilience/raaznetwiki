---
title: "Protest Communication and Digital Documentation"
tags:
  [
    protest-security,
    signal,
    briar,
    offline-communication,
    documentation,
    iran,
    evidence-collection,
    internet-shutdown,
  ]
category: "Operational Security"
difficulty: "Advanced"
audience: [Activists, Protesters, Citizen Journalists, Human Rights Defenders]
topics:
  [
    "Secure Communication",
    "Mesh Networks",
    "Digital Evidence",
    "Anti-Censorship",
  ]
summary: "Comprehensive guide for Iranian activists on communicating securely during protests (online and offline) and documenting human rights violations safely."
source: "Consolidated from Security in a Box, Tactical Tech, and Certfa"
content_type: "Operational Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic smartphone usage", "Signal installed", "Briar installed (optional)"]
estimated_read_time: "15 minutes"
---

# Protest Communication and Digital Documentation

Digital security is synonymous with physical safety. The Islamic Republic’s security apparatus utilizes sophisticated surveillance, including IMSI catchers, facial recognition, and internet blackouts. This guide outlines how to maintain communication during unrest and how to document events without endangering yourself or others.

## I. Pre-Protest Preparation: Digital Hygiene

Before attending a protest, assume your device may be lost, seized, or broken.

### 1. Device Strategy

- **The "Burner" Option:** Ideally, leave your primary smartphone at home. Use a secondary, inexpensive Android device with a fresh SIM card (not registered to your name if possible) and minimal data.
- **Sanitize Your Main Device:** If you must bring your primary phone:
  - **Remove Biometrics:** Disable Face ID and Fingerprint unlock. Use a strong, 6+ digit PIN or alphanumeric passphrase. Biometrics can be forced by security forces; a PIN cannot be easily coerced physically without cooperation.
  - **Uninstall Sensitive Apps:** Remove apps that reveal your network (Instagram, X/Twitter, main Telegram account) or log you into accounts automatically.
  - **Log Out:** Sign out of all cloud accounts (Google, iCloud) to prevent remote data access if the device is seized.
  - **Enable Full Disk Encryption:** Ensure your phone is encrypted (standard on modern iOS and Android).

### 2. Emergency Contacts & Planning

- **The "Proof of Life" Contact:** Designate a trusted person _not_ at the protest who knows your location and expected return time. Agree on a check-in schedule.
- **Memorize Numbers:** Write critical phone numbers (legal aid, family) on your body using a permanent marker or memorize them. Do not rely on your phone's contact list.

---

## II. Secure Communication Channels

During protests, mobile networks may be throttled or shut down. Your communication tools must be resilient.

### 1. Online Communication (When Internet is Available)

Use **Signal** for all protest coordination. It minimizes metadata and offers features specifically for high-risk environments.

- **Disappearing Messages:** Enable this _by default_ for all chats. Set the timer to **1 hour or less** during active protests.
  - _Settings > Privacy > Disappearing Messages_
- **Registration Lock:** Prevent the regime from hijacking your number on Signal if they seize your SIM card.
  - _Settings > Account > Registration Lock_
- **Hide Mobile Number:** Ensure only your username is visible.
  - _Settings > Privacy > Phone Number > Who can see my number: Nobody_
- **Avoid SMS & Phone Calls:** These are unencrypted and tracked by mobile operators (MCI, Irancell), providing location data and call logs to security agencies.

### 2. Offline Communication (During Internet Shutdowns)

When the government implements a blackout (SHOMA/National Information Network), centralized apps like Telegram and WhatsApp will fail without a specialized bridge/proxy.

- **Briar (Recommended):** An open-source mesh messenger that works without the internet. It syncs messages via **Bluetooth** and **Wi-Fi** between nearby devices.
  - _Use Case:_ Coordinating with a group within a crowd or nearby streets.
  - _Setup:_ Install and pair devices _before_ the internet is cut.
  - _Security Note:_ While Briar hides content, using Bluetooth/Wi-Fi makes you radio-visible. Use only when necessary.
- **Silence (Android):** If data is cut but SMS (GSM) is still working, Silence encrypts SMS messages. _Note: Both parties must have the app._

---

## III. Documenting Human Rights Violations

Recording evidence is vital, but _publishing_ it incorrectly can lead to arrests. You must distinguish between **Evidence Collection** (for courts/NGOs) and **Public Awareness** (social media).

### 1. Recording for Evidence (Private)

If you are witnessing a crime and want to submit footage to human rights organizations (e.g., Amnesty, UN Fact-Finding Mission), you need to preserve **metadata** (location, time, device info) to prove authenticity.

- **Tools:**
  - **eyeWitness to Atrocities:** Captures verifiable footage with embedded metadata. It stores footage in a secure, hidden gallery and allows strictly secure upload to legal experts.
  - **ProofMode:** A lighter alternative that creates cryptographic "proof" data for your photos/videos without modifying the original file.
- **Action:** Do **NOT** post these raw files on social media. The metadata reveals your exact location and identity. Send them directly to trusted organizations via secure channels (e.g., SecureDrop or Signal).

### 2. Recording for Public Awareness (Social Media)

If you intend to share footage publicly (Instagram, Twitter/X) to raise awareness, you must **scrub** the data to protect yourself and others.

- **Anonymize Faces:**
  - **Signal Blur Tool:** The easiest method. Open Signal, select the photo/video, use the "Checkerboard" icon to automatically blur all faces. Save the result _before_ sending or posting.
  - **Scrambled Exif (Android):** An app that strips metadata (location, device model) from photos before you share them.
- **Remove Metadata:**
  - Social media platforms (Twitter, Instagram) usually strip metadata automatically, but **chat apps (Telegram 'Send as File', Email)** do not.
  - Always use a tool like **ExifEraser** or **Signal** (which strips metadata by default) to clean files before broad distribution.

### 3. Safe Filming Tactics

- **Filming Security Forces:** Keep a safe distance. Try to film from a concealed location (e.g., inside a building/vehicle) if possible.
- **Team Work:** If filming in a crowd, have a "spotter" watch your back for plainclothes officers (Basij) who often target those recording.
- **Lock Screen:** Start recording, then lock your screen if your camera app supports it (or use `Quick Video Recorder` apps that film with the screen off).

---

## IV. Post-Protest Protocols

### 1. Cleaning Up

- **Leave Groups:** Leave and delete temporary coordination groups on Signal/Telegram immediately after the event.
  - _Signal:_ Delete the chat thread to remove it from your local database.
- **Sanitize Gallery:** Transfer sensitive photos/videos to a hidden, encrypted volume (e.g., using **VeraCrypt** on a PC) and delete them from your phone.

### 2. If Detained

- **Factory Reset (Panic Button):** If you have a "panic button" app or feature (e.g., Wasted for Android) and can trigger it safely, do so.
- **Silence:** Do not provide PINs or passwords. Iranian law may force this, but delaying access gives you time.
- **Digital First Aid:** If you are released, assume your device is compromised. Do not use it for sensitive communication until it has been factory reset or replaced.

## V. Summary Checklist

| Action             | Tool/Method                          |
| :----------------- | :----------------------------------- |
| **Chat (Online)**  | Signal (Disappearing Msgs ON)        |
| **Chat (Offline)** | Briar (Bluetooth/Wi-Fi)              |
| **Evidence**       | eyeWitness / ProofMode               |
| **Public Video**   | Blur faces + Strip Metadata (Signal) |
| **Phone Security** | 6+ Digit PIN, No Biometrics          |
| **Emergency**      | Memorize lawyer/family numbers       |

> **Warning:** No tool is 100% secure. Your behavior (OpSec) is your primary defense. Assume you are being watched and act accordingly.
