---
title: "Mobile Security for High-Risk Scenarios"
tags:
  [
    mobile-security,
    iran,
    protests,
    burner-phone,
    activism,
    surveillance,
    arrest-protocol,
    forensics,
  ]
category: "Platform and Device Knowledge"
difficulty: "Advanced"
audience: [Activists, Journalists, Political Dissidents, High-Risk Individuals]
topics:
  ["High-Risk Security", "Device Hardening", "Protest Safety", "Anti-Forensics"]
summary: "Advanced protocols for mobile security in high-threat environments, focusing on protests, border crossings, and targeted surveillance within the Iranian context."
source: "Raaznet Aggregated Research"
content_type: "Operational Guide"
security_level: "Critical"
language: "English"
prerequisites:
  [
    "Basic Android/iOS hardening",
    "Understanding of encryption",
    "Risk assessment",
  ]
estimated_read_time: "20 minutes"
last_updated: "2026-02-18"
---

# Mobile Security for High-Risk Scenarios

"High Risk" refers to situations where the likelihood of device confiscation, physical coercion, or targeted state-sponsored cyberespionage is imminent. This includes attending protests, crossing borders, being summoned by intelligence agencies (such as the IRGC Intelligence Organization or FATA), or engaging in sensitive journalism and activism.

Unlike general security advice, high-risk protocols prioritize **data minimization**, **deniability**, and **physical security** over convenience.

> **Warning for Iranian Users:** In Iran, legal protections against device search are virtually non-existent. Security forces often use physical coercion to force users to unlock devices. Therefore, technical defenses (like encryption) must be paired with operational security (like not carrying the device at all).

---

## I. The "Clean Device" Strategy (Secondary Phones)

The most effective defense against device seizure is to ensure the device you carry contains no incriminating data. For high-risk activities (protests, sensitive meetings), do not bring your primary smartphone.

### 1. The "Burner" / Protest Phone

A secondary phone minimizes the "blast radius" if confiscated.

- **Hardware:** Acquire a mid-range Android (e.g., Samsung Galaxy A-series or a used Pixel) or an older iPhone (iPhone 8 or newer).
  - _Avoid:_ Obscure brands that may have pre-installed Chinese malware or lack security updates.
- **Acquisition (Iran Context):**
  - Buying a SIM card in Iran requires a National ID (Melli Code), making anonymity impossible at the carrier level.
  - _Mitigation:_ If possible, use a device that has never been associated with your primary SIM or home Wi-Fi.
  - If you must use a SIM, accept that your location is tracked. The goal of this phone is to protect _data_ (chats/contacts), not necessarily _location_ (which the network sees).
- **Setup Protocol:**
  - **Factory Reset:** Wipe the device immediately upon acquisition.
  - **Minimal Install:** Install **only** the apps necessary for the specific mission (e.g., Signal, a VPN, a map app).
  - **Accounts:** Do not sign in to your primary Google or iCloud account. Create a dedicated "throwaway" account for this device.
  - **No Biometrics:** Do not set up Face ID or Fingerprint unlock.

### 2. Data Sanitation

If you cannot use a secondary phone, you must sanitize your primary device before entering a high-risk zone.

- **Uninstall Sensitive Apps:** Remove Instagram, Telegram, X (Twitter), and photo galleries containing sensitive media.
- **Log Out:** Log out of all cloud accounts and browsers.
- **Clear History:** Wipe browser history, keyboard predictive text history, and clipboard history.

---

## II. Hardening Against Physical Seizure

If you are arrested or stopped at a checkpoint (Gasht-e Ershad or security block), the immediate threat is forensic extraction (Cellebrite, GrayKey) or forced unlocking.

### 1. Disable Biometrics (Crucial)

Iranian interrogators can forcibly hold your phone to your face or press your finger against the sensor.

- **Action:** Disable Face ID and Fingerprint unlock entirely.
- **Requirement:** Set a strong **alphanumeric passphrase** (minimum 8-10 characters, mixing numbers and letters). Do not use a 4 or 6-digit PIN or a Pattern lock (patterns can be guessed by smudge marks on the screen).

### 2. Panic Protocols (Emergency Lockdown)

Know how to disable biometrics instantly if you haven't already:

- **iPhone:** Hold the Power button and either Volume button for 3 seconds until the "Slide to Power Off" slider appears. This disables Face ID/Touch ID immediately and requires the passcode for the next unlock.
- **Android:** Android 9+ includes a "Lockdown" option (Show lockdown option in Power menu settings). Using this disables fingerprint/face unlock and hides notifications on the lock screen.

### 3. The "Before First Unlock" (BFU) State

Modern smartphones (iOS and Android) are most secure when they are **fully powered off**.

- **Encryption:** When a device is restarted and has not yet been unlocked with the passcode, it is in BFU state. The encryption keys are held in the hardware security module (Secure Enclave/Titan M) and are inaccessible to forensic tools.
- **Protocol:** If you anticipate imminent arrest, **power off the device completely**.

---

## III. Communication & App Security

### 1. Signal Configuration

Signal is preferred over Telegram for high-risk communication because it is End-to-End Encrypted (E2EE) by default and stores minimal metadata.

- **Disappearing Messages:** Set a default timer (e.g., 1 hour or 1 day) for all chats.
- **Registration Lock:** Enable this (Settings > Account) to prevent authorities from hijacking your account on another device using a stolen SMS code.
- **Screen Security:** Enable "Screen Security" to prevent screenshots and hide the app content in the recent apps switcher.
- **Notification Hiding:** Configure notifications to show "No Name or Content" on the lock screen.
- **Keyboard Privacy:** Use an open-source keyboard (like OpenBoard) or disable "Personalized Learning" in Gboard to prevent the keyboard from learning sensitive words you type.

### 2. Telegram (Iran Specifics)

Telegram is widely used but risky. If you must use it:

- **Two-Step Verification (2FA):** Mandatory. Set a strong cloud password and a recovery email that is also secured.
- **Secret Chats:** Standard Telegram chats are _not_ E2EE. Use "Secret Chats" for sensitive conversations.
- **Privacy Settings:** Set Phone Number visibility to "Nobody" and "Who can find me by my number" to "My Contacts" or "Nobody".
- **Local Passcode:** Set a passcode for the app itself (Settings > Privacy and Security > Passcode Lock).

### 3. VPN and Internet Censorship

- **Kill Switch:** Enable "Always-on VPN" and "Block connections without VPN" in Android/iOS settings to prevent IP leaks.
- **Obfuscation:** Use VPNs capable of bypassing Deep Packet Inspection (DPI) (e.g., protocols like VLESS, VMess, Trojan via apps like v2rayNG or Streisand). Avoid free, ad-supported VPNs as they often log data.

---

## IV. Surveillance Defense: IMSI Catchers & Location

Security forces in Iran utilize Cell-Site Simulators (IMSI Catchers/Stingrays) during protests to identify attendees and intercept SMS.

### 1. The Threat

- These devices mimic cell towers, forcing phones to connect to them.
- **Capabilities:** They can identify your IMSI (unique SIM ID), triangulate your location, and downgrade your connection to 2G to intercept SMS/Calls.
- **SIAM System:** Iran's localized cellular surveillance system allows operators to track users and throttle bandwidth based on location or identity.

### 2. Mitigation

- **Airplane Mode is Insufficient:** Malware or baseband exploits can sometimes bypass Airplane mode.
- **Faraday Bags:** The only sure way to block cellular tracking while keeping the device with you is a high-quality RF-shielding Faraday bag.
- **Wi-Fi Only:** If possible, remove the SIM card entirely and rely on Wi-Fi with a VPN.
- **3G/2G Disabling:** On Android, set "Preferred Network Type" to LTE/5G only to prevent downgrade attacks (though this may kill connectivity in areas with poor coverage).

---

## V. Advanced Threats: Spyware (Pegasus/Malware)

While mass surveillance is the primary threat, high-profile individuals may be targeted with mercenary spyware like Pegasus.

### 1. Indicators of Compromise

Spyware like Pegasus is designed to be invisible. However, watch for:

- Unexpected battery drain or overheating.
- The device rebooting randomly.
- Specific SMS/links containing lures (e.g., "urgent legal notice," "package delivery").

### 2. Lockdown Mode (iOS)

If you use an iPhone, enable **Lockdown Mode** (Settings > Privacy & Security > Lockdown Mode).

- This drastically reduces the attack surface by blocking message attachments, disabling complex web technologies, and blocking incoming invitations from strangers. It is highly effective against known Pegasus exploits.

### 3. Daily Reboots

Many mobile exploits are "non-persistent," meaning they do not survive a reboot.

- **Protocol:** Reboot your phone **every morning**. This clears non-persistent malware from memory.

---

## VI. Border Crossing & Checkpoints

Crossing Iranian borders (or domestic checkpoints in volatile regions like Kurdistan or Baluchistan) requires specific preparation.

1.  **Assume Inspection:** Border agents may demand to see your phone.
2.  **The "Decoy" Strategy:**
    - Carry a "clean" phone that looks lived-in (has some harmless photos, innocent chats, and standard apps like Snapp or Digikala).
    - Hide sensitive apps. On Android, use the **Private Space** (Android 15+) or **Secure Folder** (Samsung). On iOS, remove the app from the Home Screen (Keep in App Library) or delete it entirely and reinstall later.
3.  **Cloud Wipe:**
    - Before approaching a checkpoint, if you fear imminent search, you can remote wipe your device using "Find My" (iOS) or "Find My Device" (Android) via a trusted contact, _provided the device has internet access_.
4.  **Log Out:** Ensure you are logged out of the primary accounts. It is easier to claim you "forgot your password" than to explain the content of an open app.

---

## VII. Post-Incident Forensics

If your device was confiscated and returned, or if you suspect it was tampered with during detention:

1.  **Do Not Trust the Device:** It may have been cloned, or a rootkit/spyware may have been installed.
2.  **Factory Reset:** A factory reset _might_ clear software-level malware, but sophisticated firmware attacks can persist.
3.  **Replacement:** The safest course of action is to destroy the device and replace it.
4.  **Account Credential Rotation:** Assume all passwords saved on the device are compromised. Change all passwords and revoke active sessions (especially for Google, Telegram, and Apple ID) from a different, secure computer.

### Summary Checklist for High-Risk Events

- [ ] **Primary phone left at home.**
- [ ] **Secondary phone wiped and minimal apps installed.**
- [ ] **Biometrics disabled; Strong alphanumeric passcode set.**
- [ ] **Signal messages set to disappear.**
- [ ] **SIM card removed (if Wi-Fi is sufficient) or phone in Faraday bag until needed.**
- [ ] **Emergency contact written on physical paper/body (not stored in phone).**
