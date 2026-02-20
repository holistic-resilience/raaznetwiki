---
title: "Secure Reporting and Whistleblowing"
tags:
  [
    whistleblowing,
    journalism,
    evidence-gathering,
    iran,
    opsec,
    digital-security,
    tor,
    securedrop,
    signal,
  ]
category: "Operational Security"
difficulty: "Advanced"
audience: [Activists, Whistleblowers, Journalists, Human Rights Defenders]
topics:
  [
    "Secure Communication",
    "Evidence Documentation",
    "Source Protection",
    "Anonymity",
  ]
summary: "A comprehensive guide for Iranian users on how to securely document human rights violations, scrub metadata, and submit information to media outlets or human rights organizations while minimizing the risk of identification."
source: "Raaznet Consolidated Wiki"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites:
  [
    "Proficiency with Tor Browser",
    "Understanding of metadata",
    "Basic encryption knowledge",
  ]
estimated_read_time: "15 minutes"
---

# Secure Reporting and Whistleblowing in Iran

For Iranian citizens, activists, and whistleblowers, reporting human rights violations or leaking sensitive documents is a high-stakes activity. The Islamic Republic’s surveillance apparatus (including FATA and IRGC intelligence) actively monitors telecommunications and internet traffic for dissent.

This guide outlines the operational security (OpSec) protocols necessary to document evidence and transmit it to international media or human rights organizations while minimizing the risk of identification, arrest, or retaliation against family members.

> ⚠️ **Critical Warning:** No technology can guarantee 100% safety. Your behavior and physical security are just as important as the tools you use. If you are under active surveillance, assume your devices are already compromised.

---

## 1. The Golden Rules of Reporting

Before taking any action, adhere to these fundamental principles:

1.  **Do Not Use Your Primary SIM:** Mobile networks (MCI, Irancell, Rightel) track your location and identity. Use a dedicated "burner" device if possible, or a device with no SIM card connected only to trusted Wi-Fi (via VPN/Tor).
2.  **Sanitize the Environment:** Never discuss sensitive submissions over standard phone lines or SMS.
3.  **Separate Identities:** Your whistleblowing activity must be compartmentalized from your personal digital life. Do not use the same username, email, or browser for both.
4.  **Assume Network Monitoring:** Assume all ISPs in Iran perform Deep Packet Inspection (DPI). Always use encryption (VPN + Tor) to mask the content and destination of your traffic.

---

## 2. Secure Evidence Gathering

When recording protests, violence, or sensitive documents, the file itself contains hidden data that can identify you.

### A. Metadata Management

Every photo and video taken on a smartphone contains **EXIF metadata**. This includes:

- **GPS Coordinates:** The exact location where the photo was taken.
- **Device Model:** The specific make and model of your phone.
- **Timestamp:** The exact second the file was created.
- **Unique Identifiers:** Sometimes even the serial number of the camera lens.

**How to Scrub Metadata:**

- **Android:** Use **Scrambled Exif** (available on F-Droid). Share the photo _to_ this app, and it will save a clean copy.
- **Desktop (Linux/Windows/macOS):** Use **MAT2** (Metadata Anonymisation Toolkit). It is the gold standard for cleaning files without compromising quality.
- **Built-in Options:** Android and iOS have "Remove Location" features in the gallery, but these are often insufficient for high-threat scenarios as they may leave device identifiers.

### B. Visual Anonymity (Blurring Faces)

In the context of Iranian protests, revealing the faces of other protesters puts them at risk of identification by facial recognition systems.

- **Tella:** A documentation app designed for activists. It allows you to record encrypted video, blur faces automatically, and hide the app itself (Calculator mode).
- **ProofMode:** Developed by the Guardian Project, this app adds cryptographic "proof" to your photos (timestamps, location) to verify they are real, without revealing your identity _if configured correctly_. It creates a "Chain of Custody" for legal evidence.
- **Signal Blur Tool:** If using Signal to take photos, use the built-in blur tool to obscure faces before sending.

### C. Audio Forensics

Be aware that your voice can be voice-printed.

- **Silence:** Try not to speak while recording.
- **Stripping Audio:** Remove the audio track from videos if the sound isn't essential evidence.

---

## 3. Secure Communication Channels

Once evidence is gathered and scrubbed, it must be transmitted. Choose the channel based on the sensitivity of the data.

### Level 1: High Security (Whistleblowing & Leaks)

For submitting sensitive documents to major news organizations (e.g., BBC Persian, Radio Farda, 1500tasvir, or human rights groups).

#### **SecureDrop**

SecureDrop is the industry standard for anonymous submissions. It uses the Tor network to hide the source's identity.

1.  **Download Tor Browser:** [Get Tor Browser](https://www.torproject.org/). If blocked, use the `Get Bridges` feature (Snowflake or obfs4).
2.  **Find the .onion Address:** Go to the _official_ website of the organization (e.g., The Guardian, Washington Post) and look for "SecureDrop" or "Tip Us" in the footer.
    - _Note:_ Never trust .onion addresses sent to you via chat; verify them on the official site.
3.  **Submit:** Open the .onion address in Tor Browser. You will receive a unique codename. Save this codename securely (offline)—it is the only way to log back in to check for replies.
4.  **Wipe:** After submission, securely delete the files from your device.

### Level 2: Medium Security (Direct Contact)

For rapid communication with trusted journalists.

#### **Signal**

Signal is the most secure instant messenger, but it requires careful configuration in Iran.

- **Registration Lock:** Enable this (Settings > Account) to prevent the regime from hijacking your account via SMS interception.
- **Screen Lock:** Enable the screen lock within the app.
- **Disappearing Messages:** Set a short timer (e.g., 1 hour) for sensitive chats.
- **Sender Secrecy:** Signal minimizes metadata, but the service still knows _when_ you communicate.
- **Circumvention:** If Signal is blocked, use a **Signal Proxy**.

### Level 3: Offline/Shutdown Scenarios (Nahoft)

During internet shutdowns (Aban 98 style), real-time communication may be impossible.

- **Nahoft:** An app designed specifically for the Iranian context. It encrypts text into a jumble of random Persian words or hides it inside an image file (steganography).
  - You can send these "nonsense" texts via SMS or even read them over a voice call. The recipient uses Nahoft to decrypt the message.

### ⚠️ The Danger of Telegram

Telegram is widely used in Iran but is **NOT secure by default**.

- **Risk:** "Cloud Chats" are stored on Telegram's servers. If your account is compromised or if Telegram is coerced, that data is accessible.
- **Mitigation:** If you _must_ use Telegram:
  1.  Use **Secret Chats** (End-to-End Encrypted) for _every_ sensitive conversation.
  2.  Hide your Phone Number (Settings > Privacy and Security > Phone Number > Nobody).
  3.  Enable Two-Step Verification (Cloud Password).
  4.  Never use "unofficial" Telegram clients (like Telegram Talaeii or Hotgram), which are often regime-controlled spyware.

---

## 4. Submitting to Specific Outlets

When submitting to Persian-language media or human rights groups, follow their specific security guidelines.

| Organization Type                    | Recommended Method        | Notes                                                                                                            |
| :----------------------------------- | :------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| **Major Media** (BBC, Radio Farda)   | **SecureDrop**            | Look for the "Send Us Your Story" page on their official website for the .onion link.                            |
| **Citizen Journalism** (1500tasvir)  | **Signal / Telegram Bot** | verify the bot or number on their official Twitter/X account. Do not trust random numbers circulating on groups. |
| **Human Rights orgs** (Amnesty, HRW) | **SecureDrop / Signal**   | Use their official contact pages to find the dedicated SecureDrop address.                                       |

---

## 5. Post-Submission Hygiene

After sending the material, you must eliminate traces from your device.

### Secure Deletion

Simply "deleting" a file does not remove it; it just marks the space as available. Forensic tools can recover it.

- **Android:** Use apps like **Shredder** (iShredder) to overwrite the free space.
- **PC:** Use **BleachBit** to securely wipe files and clean free disk space.

### Clear Recent Activity

- Clear clipboard history.
- Clear browser cache and history (or use Tor Browser which does this automatically).
- Delete the "sent" message from your messenger app (ensure "delete for me" is selected if "delete for everyone" is not desired/safe).

### The "Panic" Button

If you are at risk of imminent arrest:

- **Ripple:** An app by Guardian Project. If you press the "panic" button, it can broadcast a distress message to trusted contacts and structurally delete sensitive apps/data.
- **Factory Reset:** This is a last resort. While it clears user data, sophisticated forensics _might_ still recover some data if the device was not encrypted. Ensure **Full Disk Encryption** is always enabled on your phone.

---

## Summary Checklist for Iranian Whistleblowers

1.  [ ] **Environment:** Safe location, away from CCTV and eavesdroppers.
2.  [ ] **Network:** VPN + Tor Browser (or Tor Bridges).
3.  [ ] **File:** Metadata scrubbed (Scrambled Exif/MAT2).
4.  [ ] **Content:** Faces blurred, audio stripped if necessary.
5.  [ ] **Transmission:** SecureDrop (preferred) or Signal (Disappearing messages).
6.  [ ] **Cleanup:** Securely delete original files and clear app caches.
