---
title: "Operational Security for High-Risk Scenarios"
tags:
  [
    opsec,
    iran,
    protests,
    interrogation,
    anti-forensics,
    burner-phone,
    signal,
    spyware,
  ]
category: "Surveillance Technologies"
difficulty: "Advanced"
audience: [Activists, Journalists, High-Risk Individuals, Protesters]
topics:
  [
    "Operational Security",
    "Interrogation Resistance",
    "Device Hardening",
    "Protest Safety",
  ]
summary: "Advanced operational security protocols for Iranian activists facing high-risk scenarios, including protests, targeted surveillance, and arrest.[cite](#tm-cite:0%7Cirantimes.com) Covers device sterilization, counter-forensics, and communication discipline."
source: "Raaznet Aggregation"
content_type: "Guide"
security_level: "Critical"
language: "English"
prerequisites:
  ["Basic digital security knowledge", "Familiarity with Signal and VPNs"]
estimated_read_time: "15 minutes"
---

# Operational Security for High-Risk Scenarios

**Warning:** This guide is intended for individuals in Iran facing **critical threats**, including arrest, interrogation, and targeted espionage by the Islamic Republic. The strategies below prioritize _harm reduction_ and _data denial_ over convenience. No system is 100% secure; these measures aim to increase the cost and difficulty of surveillance against you.

---

## I. The Threat Landscape

In high-risk scenarios (protests, organizing, journalism), you face three primary vectors of attack in Iran:

1.  **Network Surveillance (SIAM & IMSI Catchers):** The CRA (Communications Regulatory Authority) uses systems like **SIAM** to track location, throttle speeds to 2G (breaking encryption), and intercept SMS/calls. In protests, police deploy **IMSI Catchers** to log the identity of every phone in the vicinity.
2.  **Device Seizure & Forensics:** Upon arrest, devices are seized. Interrogators use forensic tools (like Cellebrite or Chinese equivalents) to extract data. You will likely be coerced or tortured to provide passwords.
3.  **Targeted Spyware:** High-value targets may be infected with mercenary spyware (like **Pegasus**) or domestic malware delivered via fake "Judiciary" (Sana) SMS links or fake VPN apps.

---

## II. Device Sterilization & Segregation

**The "One Phone" rule is dangerous.** Your daily driver phone contains your life history. For high-risk activities, you must segregate your digital life.

### A. The "Secondary Phone" Strategy

Do not take your primary phone to a protest or sensitive meeting. Obtain a secondary device.

- **Acquisition:** Buy a cheap, used Android (Pixel preferred for GrapheneOS) or an older iPhone (6s or newer). Buy with cash if possible.
- **The "Burner" SIM Problem:** Anonymous "White SIMs" are increasingly banned and tracked. Buying a SIM requires a National ID.
  - _Mitigation:_ If possible, use the device **Wi-Fi only** (no SIM). Rely on portable hotspots (kept separate) or trusted Wi-Fi networks.
  - _Risk:_ If you must use a SIM, understand it links to the ID holder. Do not use a SIM registered to your primary identity for sensitive work.
- **Sanitization:**
  - Factory reset the device immediately upon purchase.
  - Remove _all_ Iranian domestic apps (Snapp, Rubika, Eitaa, Divar). These apps have root certificates or permissions that can leak location and data to authorities.
  - Do not sign in with your primary Google or iCloud account. Create a fresh, anonymous account dedicated to this device.

### B. Device Hardening (The "Clean" State)

1.  **Encryption:** Ensure "Encrypt Phone" is enabled (default on modern Android/iOS).
2.  **Passcodes:**
    - **Disable Biometrics:** Turn off FaceID and Fingerprint unlock immediately. These can be forced physically during arrest.
    - **Length:** Use a random 8-10 digit PIN. Patterns are easily smeared or guessed.
3.  **Lockdown Mode (iOS):**
    - Go to `Settings > Privacy & Security > Lockdown Mode` and enable it. This blocks most "zero-click" spyware exploits (like Pegasus) used by state actors.
4.  **Auto-Wipe (iOS/Android):**
    - Enable the setting to factory reset the phone after 10-15 incorrect password attempts. This is a critical last line of defense if your device is seized.

---

## III. Protest & Field Protocols

If you are physically attending a protest or meeting:

### 1. The "Faraday" Protocol

Turning a phone "off" is often insufficient due to modern "Find My" networks and potential malware persistence.

- **Best:** Leave the phone at home.
- **Good:** Use a **Faraday Bag** (RF shielding bag). This blocks all signals (Cellular, GPS, Wi-Fi, Bluetooth) physically.
- **Alternative:** Wrap the phone in multiple layers of heavy-duty aluminum foil when moving between locations to prevent IMSI catcher tracking.

### 2. Visual Anonymity

- **Facial Recognition:** Iran uses street cameras with facial recognition. Wear a mask and sunglasses. Cover distinctive tattoos.
- **Digital Markers:** Disable Bluetooth and Wi-Fi scanning in settings. These broadcast unique identifiers (MAC addresses) that can be logged by stationary receivers.

### 3. Capture & Documentation

- **Never record faces.** Blur faces before sharing.
- **Metadata Removal:** Use apps like **ObscuraCam** or **Scrambled Exif** (Android) to strip GPS and device data from photos _before_ sending them.
- **Live Upload:** If internet is available, stream footage to a cloud account (not linked to your identity) rather than saving locally, then delete from the device immediately.

---

## IV. Communication Discipline

### 1. Signal (The Gold Standard)

Use **Signal** for all sensitive communication. Telegram is not end-to-end encrypted by default and is heavily monitored.

- **Registration:** Use a VoIP number or a foreign SIM if possible. If using an Iranian SIM, enable "Registration Lock" (PIN) immediately to prevent SIM swapping attacks.
- **Proxies:** Signal is blocked. You must use a **Signal Proxy**.
  - _Action:_ Find active proxies via Twitter/Telegram channels (search `#IRanASignalProxy`).
- **Disappearing Messages:** Set to **5 minutes** or less.
- **Notification Secrecy:** Go to `Settings > Notifications` and set "Show" to "No Name or Content".

### 2. VPNs and Censorship Circumvention

Standard VPNs (OpenVPN, WireGuard) are often blocked by the DPI (Deep Packet Inspection) firewall.

- **Obfuscation:** Use tools that disguise traffic as HTTPS web browsing.
  - **V2Ray / VLESS / VMess:** The current standard for bypassing Iranian filtration.
  - **Tor + Snowflake:** Use Tor Browser with the "Snowflake" bridge to bypass blocks.
- **Kill Switch:** Ensure your VPN "Kill Switch" is ON. If the VPN drops, your internet must cut to prevent leaking your real IP.

---

## V. Post-Arrest & Interrogation Strategy

If you are detained, assume your device is in enemy hands.

### 1. The "Duress" Situation

You will likely be forced to unlock your phone.

- **Plausible Deniability:** On Android, use **Multiple User Profiles**. Keep a "Main" profile that looks like a normal, boring phone (family photos, harmless apps). Keep sensitive data in a "Secondary" profile with a different password.
- **Hidden Volumes:** specialized apps (like Veracrypt on PC) allow hidden data containers.
- **The "Panic" Button:** If you have seconds before seizure:
  - _iPhone:_ Press the Power button 5 times rapidly. This disables Biometrics and requires a PIN to unlock.
  - _Android:_ Hold Power + Volume Down (force restart). A fresh boot requires a PIN to decrypt.

### 2. Cloud Cleaning

If a comrade is arrested:

- **Kick Them Out:** Immediately remove them from all Signal groups and chats.
- **Delete History:** Use "Delete for Everyone" on recent sensitive messages if the platform supports it.

---

## VI. Advanced Spyware Defense

Targeted activists face threats from malware like **Pegasus** (NSO Group) or **Predator**.

### 1. Infection Vectors

- **Fake SMS:** The most common vector in Iran is a fake SMS claiming to be from the **Judiciary (Sana)**, **Post Office**, or **Sejam**. It contains a link to a fake app. **NEVER CLICK SMS LINKS.**
- **Fake VPNs:** Avoid "Free VPN" apps sent via Telegram. They often contain keyloggers or spyware.

### 2. Remediation

- **Daily Reboots:** Many sophisticated spyware strains are "non-persistent" (they live in RAM). Rebooting your phone every morning clears these infections.
- **MVT (Mobile Verification Toolkit):** If you suspect infection, use Amnesty International's [MVT](https://mvt.re/) to scan backup files for Indicators of Compromise (IoC). _Note: This requires technical command-line skills._

---

## VII. Checklist: High-Risk Action Plan

1.  [ ] **Device:** Secondary phone acquired. Factory reset. Biometrics disabled.
2.  [ ] **Apps:** Signal installed (Proxy configured). Maps downloaded offline (Magic Earth/OSM). Domestic apps removed.
3.  [ ] **Network:** VPN (V2Ray/Obfuscated) tested and working.
4.  [ ] **Physical:** Faraday bag/foil ready. Face mask prepared.
5.  [ ] **Emergency:** Trusted contact memorized (write on arm in marker). Phone storage encrypted.
6.  [ ] **Protocol:** Agree with your team: "If I don't check in by [Time], assume I am arrested and remove me from groups."

_Last Updated: February 2026_
