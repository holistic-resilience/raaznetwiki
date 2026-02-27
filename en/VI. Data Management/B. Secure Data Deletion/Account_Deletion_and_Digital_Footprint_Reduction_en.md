---
title: "Account Deletion and Digital Footprint Reduction"
tags:
  [
    privacy,
    digital-footprint,
    account-deletion,
    opsec,
    iran-security,
    osint-countermeasures,
    social-media-hygiene,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [Activists, Journalists, General Public, High-Risk Users]
topics:
  [
    "Account Management",
    "Privacy Protection",
    "Data Security",
    "Anti-Forensics",
  ]
summary: "A comprehensive guide for Iranian users on reducing their digital footprint, securely deleting online accounts (foreign and domestic), and managing social media history to minimize surveillance risks."
source: "Raaznet Aggregated Resources"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites:
  [
    "Basic internet navigation",
    "Access to current email/phone numbers",
    "Password manager (optional)",
  ]
estimated_read_time: "12 minutes"
---

# Account Deletion and Digital Footprint Reduction

A "digital footprint" is not just a privacy concern—it is potential evidence. The Islamic Republic’s security agencies actively profile citizens by aggregating data from old social media accounts, leaked databases, and domestic applications.

This guide focuses on **minimizing your online presence**. It covers how to find old accounts, the correct strategy for deleting them (especially on Iranian platforms), and how to scrub your history from active social media profiles.

## Phase 1: Assessment (OSINT Yourself)

Before you can delete your footprint, you must find it. Use the same "Open Source Intelligence" (OSINT) techniques that investigators might use against you.

### 1. Breach Checks

Check if your email or phone number has appeared in data leaks. This often reveals old accounts you forgot about.

- **Have I Been Pwned:** [haveibeenpwned.com](https://haveibeenpwned.com/)
- **Firefox Monitor:** [monitor.firefox.com](https://monitor.firefox.com/)

### 2. Search Engine "Dorking"

Search for your own name, username, and phone numbers using specific operators in Google or DuckDuckGo:

- `"Your Name"` (Exact match)
- `"YourUsername" -site:instagram.com` (Find your username on sites _other_ than Instagram)
- `site:twitter.com "Your Name"` (Find mentions of you on specific platforms)

### 3. Email Excavation

Search your own email inboxes (Gmail, Yahoo, etc.) for these keywords to find old sign-ups:

- "Welcome to"
- "Verify your email"
- "Confirm account"
- "Registration"

---

## Phase 2: The "Poison then Delete" Strategy

For high-risk users, simply clicking "Delete Account" is insufficient. Many services—especially domestic Iranian apps—retain data in their backups or archives even after an account is marked as "deleted."

**The Golden Rule:** Always overwrite data with false information before deletion.

### Step-by-Step Procedure:

1.  **Log In:** Access the account you wish to destroy.
2.  **Scrub Content:** Manually delete messages, photos, and addresses.
3.  **Poison the Profile:**
    - Change the **Name** to a generic one (e.g., "User 123456").
    - Change the **Email** to a disposable/burner address (e.g., use a temporary email service).
    - Change the **Phone Number** (if the service allows) to a virtual number or remove it.
    - Change the **Profile Picture** to a blank image.
4.  **Delete the Account:** Only _after_ poisoning the data should you proceed with the official deletion process.

---

## Phase 3: Deleting Foreign Accounts

For international services (Google, Meta, X, etc.), the deletion process is usually reliable but often hidden.

### Tools to Assist Deletion

- **JustDeleteMe (.xyz):** A directory of direct links to delete pages for thousands of services. It color-codes sites by difficulty (Green = Easy, Black = Impossible).
  - _URL:_ [justdeleteme.xyz](https://justdeleteme.xyz/)
- **Redact.dev:** A powerful application that runs _locally_ on your computer. It allows you to bulk-delete old posts, likes, and DMs from services like Twitter (X), Discord, and Reddit without sending your credentials to a third-party server.
  - _Recommendation:_ Essential for cleaning up active accounts without deleting them entirely.

### Specific Platforms

#### Google

Google stores a vast amount of activity.

1.  Go to [myactivity.google.com](https://myactivity.google.com/).
2.  Set **Web & App Activity** to "Auto-delete (3 months)."
3.  To delete the account entirely: Google Account > Data & Privacy > Delete your Google Account.

#### Telegram (Crucial for Iran)

Telegram is a primary target for device seizures.

1.  **Auto-Delete:** Settings > Privacy and Security > If Away For > Set to **1 Month**.
2.  **Immediate Deletion:** Visit [my.telegram.org](https://my.telegram.org/) (requires VPN), enter your number, and select "Delete Account."
3.  **Cache:** On your phone, go to Settings > Data and Storage > Storage Usage > Clear Telegram Cache. This removes images/files from the _device_ but keeps them in the cloud.

#### Signal

Signal stores very little metadata.

1.  **Disappearing Messages:** Enable this by default for _all_ new chats (Settings > Privacy > Default timer for new chats).
2.  **Registration Lock:** Enable this to prevent SIM swapping attacks (Settings > Account > Registration Lock).

---

## Phase 4: Managing Iranian Domestic Apps (High Risk)

**Warning:** Domestic apps (Rubika, Eitaa, Soroush, Snapp, etc.) operate under Iranian jurisdiction. You must assume that **deletion does not equal data removal** from Intelligence (Vaja/Sepah) databases.

### 1. Rubika & Soroush

- **Risk:** Highly monitored.
- **Deletion:** Newer versions include a delete option in `Settings > Privacy & Security > Delete My Account`.
- **Precaution:** You usually must wait a few days (often 7-10) without logging in for the deletion to finalize. **Do not log back in** during this window.
- **Action:** Delete all chats and change your name/bio to random characters _before_ requesting deletion.

### 2. Eitaa (Iranian Telegram Clone)

- **Method:** You cannot delete the account from inside the app.
- **Process:** You must visit `https://my.eitaa.com/deleteAccount` (using an Iranian IP or with VPN off may be required).
- **Verification:** They will send a code to your _Eitaa app_ (not SMS). Enter the code on the site to delete.

### 3. Snapp / Digikala / Tapsi

- **Difficulty:** Impossible to self-delete.
- **Strategy:** These apps act as tracking devices. If you are going to a protest or sensitive meeting:
  1.  Log out.
  2.  **Uninstall the application.**
  3.  If possible, use the web version (PWA) instead of the installed app to reduce permission access (contacts, exact GPS history).

---

## Phase 5: Social Media Hygiene (Active Accounts)

If you must keep an account (e.g., Twitter/X for activism), you should regularly scrub its history to prevent "archaeology" by regime agents who look for old tweets to incriminate you.

### Automated Scrubbing

Use tools to automatically delete posts older than X months.

- **TweetDelete / TweetDeleter:** For X (Twitter).
- **Redact.dev:** For Discord, Facebook, Reddit, and X.

### Sanitizing Media

Before uploading photos or videos to any platform:

1.  **Remove EXIF Metadata:** Use tools like _ObscuraCam_ or _ExifTool_ to strip GPS and device data.
2.  **Blur Faces:** Never upload raw footage of protests. Blur faces to protect fellow citizens.
3.  **Audio:** Strip audio if it contains identifiable names or voices.

## Summary Checklist

| Platform Type                | Primary Strategy                                   | Tools                      |
| :--------------------------- | :------------------------------------------------- | :------------------------- |
| **Foreign (Google/Meta)**    | Download data (optional), then "Poison & Delete"   | JustDeleteMe, Redact.dev   |
| **Messaging (Telegram)**     | Set Auto-Destruct to 1 month; Clear Cache          | my.telegram.org            |
| **Messaging (Signal)**       | Enable Disappearing Messages                       | In-app settings            |
| **Iranian (Eitaa/Rubika)**   | **Obfuscate identity first**, then use web portals | my.eitaa.com               |
| **Iranian (Snapp/Services)** | Uninstall app; use Web/PWA versions                | None (Deletion impossible) |

> [!danger] **Final Warning for Iranian Users**
> If you are detained, interrogators may force you to restore deleted accounts.
>
> - **Telegram:** If you delete your account and re-register with the _same_ phone number, your "User ID" changes, proving the account was wiped.
> - **2FA:** Use a cloud password (2FA) on Telegram. Interrogators cannot restore the account without this password, even if they have your SIM card.
