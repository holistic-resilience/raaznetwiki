---
title: "Secure Whistleblowing and Data Submission"
tags:
  [
    whistleblowing,
    securedrop,
    anonymity,
    metadata,
    tor,
    iran,
    opsec,
    signal,
    briar,
  ]
category: "Communication Platform"
difficulty: "Advanced"
audience: [Whistleblowers, Activists, Journalists, High-Risk Users]
topics:
  [
    "Anonymous Submission",
    "Source Protection",
    "Data Sanitization",
    "Secure Communication",
  ]
summary: "Comprehensive guide for Iranian users on how to anonymously submit sensitive data and whistleblow to journalists or organizations while minimizing the risk of identification."
source: "Raaznet Aggregated Knowledge"
content_type: "Operational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Proficiency with Tor Browser",
    "Understanding of metadata",
    "Basic encryption knowledge",
  ]
estimated_read_time: "15 minutes"
---

# Secure Whistleblowing and Data Submission

For Iranian citizens, activists, and insiders wishing to expose corruption, human rights violations, or state surveillance, the act of "whistleblowing" carries extreme risk. The Islamic Republic’s security apparatus (FATA and IRGC Intelligence) actively monitors domestic networks for unauthorized leaks.

This guide outlines the operational security (OpSec) required to submit information anonymously. **It is designed for high-threat scenarios.**

> [!DANGER] **Critical Warning for Iranian Users**
>
> - **Never** use your personal internet connection (home Wi-Fi, mobile data) without rigorous obfuscation (Tor with Bridges).
> - **Never** use domestic Iranian platforms (Rubika, Eitaa, Soroush) or SMS for whistleblowing.
> - **Avoid** sending sensitive material to domestic news agencies (Fars, Tasnim, IRNA), as they are state-controlled. Submit only to trusted international organizations or exiled independent media.
> - **Whistleblowing is not leaking:** Leaking is often casual; whistleblowing is a calculated, ethical act requiring maximum anonymity to protect your life and liberty.

---

## Phase 1: The Golden Rule of Anonymity

Your safety depends on **compartmentalization**. You must separate your "Whistleblower Identity" from your "Personal Identity."

### 1. The Environment

- **Physical Location:** Do not submit data from your home or workplace. Avoid cafes with CCTV cameras or requirements to show ID for Wi-Fi. Ideally, use a location unconnected to you.
- **The Device:** Do not use your primary smartphone or work laptop. If possible, buy a cheap, second-hand laptop for cash and destroy it (or the hard drive) afterwards.
- **Operating System:** For high-risk submissions, **do not use Windows or macOS.** Use **Tails OS** (The Amnesic Incognito Live System). Tails runs from a USB stick, routes everything through Tor, and leaves no trace on the computer after shutdown.

### 2. The Network (Tor & Bridges)

Direct access to anonymity networks like Tor is often blocked in Iran. You must use **Tor Bridges** to disguise your traffic.

- **Snowflake:** Makes your traffic look like a video call. Effective in Iran.
- **OBFS4:** Obfuscates Tor traffic to look like random noise.

---

## Phase 2: Sanitizing Your Data (Metadata Removal)

Before you send _anything_, you must clean it. Every digital file (photo, video, PDF, Word doc) contains hidden "metadata" that can identify you.

### What is Metadata?

- **Photos:** GPS coordinates of where the photo was taken, camera model, unique serial number, date/time.
- **Documents:** Author name, computer hostname, editing history, software version.

### Tools for Removal

#### On Android (Mobile)

- **ExifEraser:** A permissionless, open-source app that strips metadata from JPEGs and PNGs.
- **Scrambled Exif:** An open-source tool (available on F-Droid) that removes metadata before you share the file.
- **Usage:** "Share" the photo to the Scrambled Exif app first; it will sanitize the file and then prompt you to share the clean version to your destination.

#### On Desktop (Linux/Tails)

- **MAT2 (Metadata Anonymisation Toolkit):** The gold standard. Included in Tails OS. It removes metadata from images, audio, and documents (PDF, office files) without compromising the file content.
- **Usage (Terminal):** `mat2 --inplace yourfile.jpg`

> [!TIP] **Visual Scrubbing**
> Metadata tools do not remove visual identifiers. If a photo shows your reflection, a unique landmark outside your window, or a distinct tattoo, crop or blur it. **Do not** use the simple "markup" tool in iPhones/Androids to cover sensitive text; it can often be reversed. Use a dedicated tool or physically block the info before taking the photo.

---

## Phase 3: Choosing a Submission Channel

Select the method that matches your threat model.

### Tier 1: Maximum Security (SecureDrop)

**SecureDrop** is an open-source submission system used by major news organizations (e.g., _The Guardian_, _The Washington Post_, _ProPublica_) and NGOs. It is the safest way to transfer documents.

- **How it works:**
  1.  You download **Tor Browser** and use the organization's unique `.onion` address.
  2.  You upload files to a server that is physically air-gapped (not connected to the internet) and encrypted.
  3.  The organization receives the documents but _does not record your IP address, browser info, or location._
  4.  You receive a random codename to check back for replies later.
- **Iran Strategy:** Look for SecureDrop addresses of reputable _international_ human rights organizations or trusted diaspora media outlets.

### Tier 2: High Anonymity Messengers (Briar, SimpleX)

If you cannot use SecureDrop, use a decentralized messenger that does not require a phone number.

- **SimpleX Chat:**
  - **Pros:** No phone numbers, no user IDs, no central servers. Routing is onion-like (multi-hop).
  - **Cons:** Requires the recipient to share a QR code or link first.
- **Briar:**
  - **Pros:** Routes entirely over Tor. Can work via Bluetooth/Wi-Fi in local mesh networks (useful during internet blackouts).
  - **Cons:** Both parties must be online to exchange messages (no cloud storage).

### Tier 3: Standard Encrypted Messaging (Signal)

**Signal** is excellent for privacy but requires caution for whistleblowing because it is linked to a phone number.

- **Risk:** In Iran, SIM cards are registered to your ID. If your Signal account is compromised or mapped, it traces back to you.
- **Mitigation:**
  1.  **Hide Phone Number:** Settings > Privacy > Phone Number > Who can see my number: **Nobody**.
  2.  **Username:** Create a username and share that, not your number.
  3.  **Registration Lock:** Enable this PIN to prevent SIM swapping attacks.
  4.  **Disappearing Messages:** Set a short timer (e.g., 5 minutes) for sensitive chats.
  5.  **VPN:** Always access Signal via a VPN or its built-in Proxy feature to hide usage from the ISP.

### Tier 4: Anonymous Email (Proton / Tuta)

Email is inherently less secure due to metadata (headers). Use only if necessary.

- **Provider:** Use **Proton Mail** or **Tuta** (formerly Tutanota).
- **Access:** Access via their **Tor Onion service** (e.g., Proton's `.onion` site) rather than the standard web or app.
- **Creation:** Create the account while on Tor. Do not link a recovery phone number or external email.

---

## Phase 4: After Submission

1.  **Digital Cleanup:**
    - If using Tails OS, simply shut down. The RAM is wiped.
    - If using a standard OS, use **BleachBit** to securely wipe the files. Deleting them to the "Trash" is insufficient; forensic tools can recover them.
2.  **Silence:** Do not tell colleagues, friends, or family that you submitted the data.
3.  **Monitoring:** Do not obsessively check the news organization's website from your personal device to see if they published your story. This creates a "pattern of life" correlation.

## Summary Checklist

| Action           | Tool/Method                                |
| :--------------- | :----------------------------------------- |
| **OS**           | Tails OS (booted from USB)                 |
| **Network**      | Tor Browser (with Snowflake/Obfs4 bridges) |
| **Sanitization** | MAT2 (Tails/Linux) or ExifEraser (Android) |
| **Submission**   | SecureDrop (.onion) or SimpleX Chat        |
| **Cleanup**      | Secure Wipe / Physical Destruction         |

**Disclaimer:** No system is 100% secure. This guide reduces risk but cannot eliminate it entirely. Assess your specific situation before acting.
