---
title: "Advanced Mobile Threats and Countermeasures"
tags:
  [
    mobile-security,
    spyware,
    pegasus,
    imsi-catcher,
    sim-swapping,
    forensics,
    iran,
    digital-repression,
  ]
category: "Platform and Device Knowledge"
difficulty: "Advanced"
audience: [Journalists, Activists, High-Risk Individuals, Technical Users]
topics:
  [
    "Spyware Defense",
    "Network Surveillance",
    "Forensic Evasion",
    "Carrier Threats",
  ]
summary: "A comprehensive guide to defending against advanced mobile threats in Iran, including state-sponsored spyware (Pegasus), IMSI catchers, forensic extraction, and weaponized SIM deactivation."
source: "Raaznet Aggregated Wiki"
content_type: "Wiki"
security_level: "High"
language: "English"
prerequisites:
  ["Basic mobile security knowledge", "Familiarity with 2FA and encryption"]
estimated_read_time: "15 minutes"
last_updated: "2026-02-18"
---

# Advanced Mobile Threats and Countermeasures

Mobile devices are the primary targets for state surveillance. Unlike general cybercriminals, state actors like the Islamic Republic possess direct access to telecommunications infrastructure (MCI, Irancell, Rightel) and procure advanced surveillance weaponry (such as NSO Group's Pegasus or Cellebrite forensic tools).

This guide addresses high-level threats beyond basic malware, focusing on targeted espionage, network interception, and physical device compromise.

## 1. Advanced Spyware (Pegasus, Predator, and Equivalents)

State-sponsored "mercenary spyware" allows attackers to take full control of a device—accessing microphones, cameras, messages (even in Signal/WhatsApp), and location data—often without any user interaction ("zero-click" exploits).

### How It Works

- **Zero-Click Exploits:** Malicious code is sent via iMessage, WhatsApp, or other system processes. The user does not need to click a link; receiving the data packet is enough to infect the device.
- **Silent Operation:** These tools run in the background, masking their battery and data usage.
- **Capabilities:** Full exfiltration of files, real-time audio/video recording, and keylogging.

### Countermeasures & Hardening

#### A. Reboot Daily (Non-Persistence)

Many modern spyware payloads are non-persistent to avoid detection during forensic analysis. They reside in volatile memory (RAM).

- **Action:** Reboot your phone **at least once daily**. This forces the attacker to re-infect the device, increasing their cost and risk of detection.

#### B. Enable Lockdown Mode (iOS)

For iPhone users, **Lockdown Mode** is the most effective defense against zero-click exploits. It reduces the attack surface by blocking complex web technologies, message attachments, and unsolicited communication requests.

- **Enable:** `Settings` → `Privacy & Security` → `Lockdown Mode`.

#### C. Android Advanced Protections

- **GrapheneOS:** If possible, use a Google Pixel running [GrapheneOS](https://grapheneos.org/). Its hardened memory allocator and sandboxing make exploitation significantly harder.
- **Auto-Reboot:** Configure your device to auto-restart if not unlocked for a set period (e.g., 18 hours).

#### D. Detection (MVT)

The **Mobile Verification Toolkit (MVT)** by Amnesty International can scan backup files for "Indicators of Compromise" (IOCs).

- **Note:** This is a technical process. If you suspect infection, disconnect the device from the internet immediately and seek help from a digital forensics expert (e.g., Access Now, Amnesty Tech).

---

## 2. Network Surveillance: IMSI Catchers & Stingrays

IMSI Catchers (Stingrays) are fake cell towers used by security forces during protests or targeted operations to intercept traffic and track location.

### How It Works

- **Man-in-the-Middle (MitM):** The device mimics a legitimate cell tower (e.g., Hamrah-e Aval) but broadcasts a stronger signal, forcing nearby phones to connect to it.
- **Downgrade Attacks:** The device forces your phone to drop from secure 4G/5G to insecure 2G (GSM), where encryption is weak or nonexistent.
- **Capabilities:** Intercepting SMS/Calls, capturing IMSI (unique ID) for identity mapping, and precise location triangulation.

### Countermeasures

#### A. Disable 2G (Critical)

Prevent your phone from connecting to insecure 2G networks.

- **Android (Android 12+):** `Settings` → `Network & Internet` → `SIMs` → Toggle **OFF** "Allow 2G".
- **iOS:** Enabled automatically when **Lockdown Mode** is active.

#### B. Android 15+ Security Features

Use devices running Android 15 or later, which introduce specific anti-surveillance alerts:

- **Cellular Ciphering Transparency:** Warns if the network connection is unencrypted.
- **Identifier Disclosure Transparency:** Warns if the network requests your device's unique identifiers (IMSI/IMEI) unnecessarily.

#### C. Use Encrypted Data Only

- **Avoid SMS/Cellular Calls:** Traditional calls and SMS are easily intercepted by IMSI catchers.
- **Use Signal/Orbot:** Conduct all communication over end-to-end encrypted data channels (Signal, WhatsApp) via a VPN. Even if the "pipe" is intercepted, the content remains encrypted.

#### D. Faraday Bags

During high-risk transport or protests, place the device in a **Faraday bag** (RF shielding pouch) to physically block all signals. This prevents remote tracking or activation.

---

## 3. Carrier Threats: SIM Deactivation & Interception

In Iran, mobile carriers are state-controlled. The threat is not just "hackers" swapping your SIM, but the government itself manipulating the infrastructure.

### The Threat Landscape

- **State-Ordered Deactivation:** Security agencies (CRA/IRGC) can order the deactivation of SIM cards belonging to activists to deny them access to banking, social media, and services.
- **SMS Interception:** The state has direct API access to SMS gateways, allowing them to read 2FA codes or inject malicious links.

### Countermeasures

#### A. Decouple Accounts from Phone Numbers

Do not rely on your Iranian phone number for critical identity verification.

- **Signal:** Set up a **Username** and hide your phone number from everyone (`Settings` → `Privacy` → `Phone Number` → `Who can see my number: Nobody`).
- **Telegram:** Use a non-Iranian number if possible (e.g., virtual numbers), but be aware Telegram does not hide numbers as effectively as Signal.

#### B. Abandon SMS 2FA

Never use SMS for Two-Factor Authentication if an alternative exists.

- **Use TOTP:** Use authenticator apps like **Aegis** (Android) or **Raivo** (iOS).
- **Use FIDO/Passkeys:** Hardware keys (YubiKey) or on-device Passkeys are immune to SIM interception.

#### C. SIM PIN (Limited Utility)

Setting a SIM PIN prevents a thief from moving your SIM to another phone, but it **does not** stop the carrier/government from cloning your SIM or intercepting traffic at the network level.

---

## 4. Forensic Extraction (Physical Seizure)

If you are arrested, security forces will attempt to extract data using tools like **Cellebrite** or **GrayKey**.

### Understanding BFU vs. AFU

- **BFU (Before First Unlock):** The state of the phone after a reboot but _before_ you enter your passcode. Data is fully encrypted and hardest to extract.
- **AFU (After First Unlock):** The phone has been unlocked at least once since boot. Encryption keys are in memory, making extraction easier for forensic tools.

### Countermeasures

#### A. The "Panic" Reboot

If you anticipate arrest or seizure:

- **Turn the phone OFF immediately.** This puts it in BFU state.
- **Trigger Lockdown (iOS):** Press Power + Volume button for 3 seconds. This disables biometrics and requires a passcode.
- **Trigger Lockdown (Android):** Enable "Show Lockdown Option" in settings. Long-press power and tap "Lockdown" to disable fingerprint/face unlock.

#### B. Strong Alphanumeric Passphrases

Forensic tools rely on brute-forcing codes.

- **Avoid:** 4 or 6-digit PINs.
- **Use:** A strong alphanumeric passphrase (e.g., `Tr@ctor!Red77`). A 6-digit PIN can be cracked in minutes; a complex password can take decades.

#### C. Biometrics are a Liability

- **Disable FaceID/Fingerprint:** In Iran, you can be physically forced to unlock a device with your finger or face. You cannot be easily forced to reveal a complex code inside your mind without coercion.
- **Legal Note:** While Iranian law does not protect against self-incrimination effectively, a strong passcode buys time and creates a technical barrier that biometrics do not.

---

## 5. Location Tracking

Your location is tracked via three vectors: **GPS** (Satellite), **Cellular Triangulation** (Towers), and **Advertising IDs** (Data Brokers).

### Countermeasures

- **Airplane Mode is Insufficient:** "Soft" airplane mode may still allow GPS or background Bluetooth queries.
- **Leave it Behind:** The only way to be 100% untrackable is to not carry the device.
- **Burner Devices:** Use a secondary device for sensitive work. Purchase it with cash, never turn it on at your home address, and keep it powered off in a Faraday bag when not in use.
- **Disable Advertising ID:**
  - **Android:** `Settings` → `Privacy` → `Ads` → `Delete advertising ID`.
  - **iOS:** `Settings` → `Privacy & Security` → `Tracking` → Turn off "Allow Apps to Request to Track".

---

## Summary Checklist for High-Risk Scenarios

1.  **Transport/Protest:** Phone OFF (BFU state) or in a Faraday bag.
2.  **Daily Use:** Reboot every morning.
3.  **Network:** Disable 2G. Use VPN (Orbot/Mullvad/Proton) 100% of the time.
4.  **Authentication:** No SMS 2FA. Use TOTP apps.
5.  **Biometrics:** Disabled. Use a strong alphanumeric passphrase.
