---
title: "Private Notes and Media Management"
tags:
  [
    notes,
    photo-management,
    calendar,
    encryption,
    e2ee,
    iran-privacy,
    digital-security,
    cryptee,
    standard-notes,
    ente,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, General Public]
topics:
  [
    "Secure Note-Taking",
    "Photo Privacy",
    "Metadata Protection",
    "Plausible Deniability",
  ]
summary: "A guide to managing personal digital lives—notes, photos, and calendars—using end-to-end encryption to protect against surveillance and physical device seizure in Iran."
source: "Raaznet Wiki (Aggregated)"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of cloud sync",
    "Use of a reliable VPN/Circumvention tool",
  ]
estimated_read_time: "10 minutes"
last_updated: "2026-02-15"
---

# Private Notes and Media Management

The management of private notes, photos, and daily schedules is not just a matter of organization—it is a critical safety issue. Domestic surveillance apparatuses and aggressive physical device seizures mean that data stored in standard apps (like Google Photos, Apple Notes, or unencrypted calendars) can be easily accessed by authorities if a device is confiscated or if cloud credentials are compromised.

This guide focuses on **End-to-End Encrypted (E2EE)** alternatives for managing your personal digital footprint. In an E2EE model, the service provider cannot read your data; only you possess the keys to decrypt it.

## The Risks of "Big Tech" Clouds

Services like Google Drive, iCloud, and standard note-taking apps store encryption keys on their servers. This creates two major risks for Iranian users:

1.  **Server-Side Access:** If the company is compelled by a legal request (international or domestic), they can decrypt and hand over data.
2.  **Account Compromise:** If an adversary intercepts your SMS 2FA (a common tactic in Iran) or phishes your password, they gain access to your entire history of photos and notes.

## Secure Note-Taking Applications

Notes often contain sensitive thoughts, contacts, draft posts, or meeting minutes. We recommend switching to apps that encrypt data _before_ it leaves your device.

### 1. Standard Notes (Recommended)

Now part of the Proton ecosystem, Standard Notes is a robust, cross-platform app designed for longevity and privacy.

- **Security Model:** Client-side AES-256 encryption. The server (Proton) sees only gibberish.
- **Iran Context:** Offers a "Locked" notes feature, requiring an additional password to open specific notes. This provides a layer of defense if your phone is unlocked under duress.
- **Availability:** Windows, macOS, Linux, iOS, Android, Web.
- **Sync:** Works well, but may require a VPN/circumvention tool if Proton domains are blocked.

### 2. Cryptee (Best for Plausible Deniability)

Cryptee is a web-based (Progressive Web App) tool for notes and photos. It is unique because it is designed specifically for high-risk threat models.

- **Key Feature: Ghost Folders.** You can hide folders inside the app. They do not appear unless you type a specific "Ghost" password.
- **Why use it in Iran:** If forced to unlock your device or log into your account, you can provide your "safe" password. The sensitive "Ghost" data remains invisible and cryptographically inaccessible.
- **Format:** Web-based. This leaves less forensic footprint on the device than a native app but requires an internet connection to load initially.

### 3. Notesnook

A fully open-source, E2EE alternative that focuses on ease of use and migration from Evernote.

- **Features:** "Monograph" encryption allows you to share secure, encrypted notes via a public link (password protected).
- **Offline Access:** Good local caching, useful during internet throttle periods.

### 4. Joplin

A free, open-source app that allows you to choose _where_ you store your data (e.g., Dropbox, Nextcloud, AWS).

- **Warning:** You **must** enable End-to-End Encryption in the settings manually. It is not always on by default.
- **Use Case:** Best for users who want to sync via a self-hosted Nextcloud server or Syncthing (avoiding central clouds entirely).

---

## Private Photo Management

Photos contain rich metadata (location, time, device model) and facial data. Standard galleries scan this data to build profiles.

### Ente Photos (Top Recommendation)

Ente is an open-source, E2EE alternative to Google Photos and Apple iCloud.

- **How it works:** Photos are encrypted on your phone before upload. Ente cannot see your photos or AI-analyze your faces.
- **Features:**
  - Automatic backup for Android/iOS.
  - "Hide" feature to remove photos from the main timeline.
  - 3-click data export (no lock-in).
- **Audit:** Audited by Cure53 (2023).

### Metadata Scrubbing

Before sharing photos publicly or storing them in less secure locations, strip the metadata.

- **Android:** Use _Scrambled Exif_.
- **Desktop:** Use _ExifCleaner_.
- **Why:** A photo taken at a protest can reveal the exact GPS coordinates of your location to authorities.

---

## Secure Calendars

Your calendar reveals your network, your movements, and your routine.

### Proton Calendar & Tuta

Both Proton and Tuta (formerly Tutanota) offer encrypted calendars integrated with their email services.

- **Encryption:** Event title, description, location, and participants are encrypted. The provider knows _that_ you have an event, but not _what_ it is.
- **Reminder:** These services function best when all participants use the same platform. When inviting a Gmail user, the invite email sent to them is readable by Google.

---

## Ephemeral Text Sharing (Pastebins)

Sometimes you need to share a block of text (code, a statement, a list of URLs) without creating a permanent file or sending it via a messenger app.

### PrivateBin

PrivateBin is a "Zero-Knowledge" pastebin. The server has no knowledge of the data being pasted.

- **Mechanism:** The decryption key is part of the URL anchor (the part after the `#`). The server never receives this part of the URL.
- **Burn After Reading:** Configure the paste to delete itself after 1 view or 5 minutes.
- **Usage:** Send the link via Signal. Once clicked, the information destroys itself on the server, leaving no trail for future forensic analysis.

---

## Operational Security for Iranian Users

### 1. The "Clean Device" Approach

In high-risk situations (border crossings, protests), assume your device will be seized.

- **Web-Based is Better:** Use Cryptee or the web versions of Proton/Tuta via a browser (like Brave or Tor Browser) in "Private Mode." When you close the tab, the local data is cleared.
- **App Hiding:** On Android, use separate user profiles or "Second Space" features to keep your private apps (Signal, Ente, Standard Notes) separate from your "public" profile.

### 2. Network Censorship

Most privacy-focused services (Proton, Tuta, Ente) are frequent targets of the Great Firewall (Filternet).

- **Requirement:** Ensure you have a robust circumvention strategy (e.g., V2Ray/Xray, Psiphon, or Tor with Bridges) configured _before_ attempting to sync these apps.
- **Offline Mode:** Apps like Standard Notes and Notesnook allow you to write offline. Syncing happens only when you successfully connect to a VPN.

### 3. Plausible Deniability

Do not keep an empty phone; it looks suspicious.

- Keep "dummy" photos and "dummy" notes in the standard gallery/notes app.
- Use hidden volumes (like in Cryptee) for sensitive material.

## Summary of Tools

| Tool                | Category     | Key Benefit                        | Platform       |
| :------------------ | :----------- | :--------------------------------- | :------------- |
| **Standard Notes**  | Notes        | Proven reliability, "Locked" notes | All            |
| **Cryptee**         | Notes/Photos | **Ghost Folders** (Deniability)    | Web (PWA)      |
| **Ente Photos**     | Photos       | E2EE Google Photos replacement     | Mobile/Desktop |
| **Proton Calendar** | Calendar     | Integrated with Proton Mail        | Mobile/Web     |
| **PrivateBin**      | Sharing      | "Burn after reading" text          | Web            |
