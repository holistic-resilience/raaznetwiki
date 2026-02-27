---
title: "Device Integrity and Advanced Spyware Defense"
tags:
  - device-integrity
  - spyware
  - pegasus
  - forensics
  - mobile-security
  - iran-surveillance
  - digital-forensics
category: "Surveillance Technologies"
difficulty: "Advanced"
audience:
  [
    Journalists,
    Human Rights Defenders,
    High-Risk Activists,
    Political Dissidents,
  ]
topics:
  ["Mobile Security", "Spyware Detection", "Device Hardening", "Forensics"]
summary: "Comprehensive guide on maintaining mobile device integrity, detecting advanced mercenary spyware (Pegasus/Predator), and defending against physical and remote extraction tactics used by Iranian security agencies."
source: "Raaznet Aggregated Resources"
content_type: "Educational Guide"
security_level: "Critical"
language: "English"
prerequisites:
  [
    "Understanding of mobile operating systems",
    "Basic command-line familiarity (for MVT)",
    "High threat model awareness",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-17"
---

# Device Integrity and Advanced Spyware Defense

"Device Integrity" refers to ensuring that your mobile device has not been tampered with by state actors, either remotely via mercenary spyware (like Pegasus) or physically during detention.

The Islamic Republic employs a two-tiered surveillance strategy:

1.  **Mass Surveillance:** Using domestic apps (e.g., Rubika, Eitaa, malicious VPNs) and commodity malware to track the general population.
2.  **Targeted Espionage:** Utilizing advanced, "zero-click" mercenary spyware and physical extraction tools (like Cellebrite/GrayKey) against high-value targets such as journalists, activists, and protest leaders.

This guide focuses on defending against **Targeted Espionage**.

---

## I. Understanding the Threat Landscape

### 1. Mercenary Spyware (Remote)

Advanced spyware tools like **Pegasus** (NSO Group) and **Predator** (Intellexa) allow attackers to gain total control over a device without the user clicking a link ("zero-click exploits").

- **Capabilities:** Access encrypted messages (Signal/WhatsApp), turn on cameras/microphones, track GPS, and steal passwords.
- **Iranian Context:** While the IRGC primarily relies on domestic malware, evidence suggests the acquisition of foreign surveillance tech. High-profile Iranian dissidents are routinely targeted.

### 2. Physical Extraction (Forensic)

When a device is seized at a checkpoint or during arrest, Iranian security forces use forensic devices (often acquired via grey markets) to extract data.

- **Threat:** Even if a device is locked, tools can exploit older OS vulnerabilities to bypass passcodes or dump data.
- **Defense:** The only defense against physical extraction is a strong alphanumeric passphrase and a modern, updated Operating System (OS) with Secure Boot.

### 3. Domestic "Rat"ware

The most common vector in Iran is **social engineering**. Users are tricked into installing "Anti-Filter" apps, "Gold Telegram" clones, or government service apps that break device integrity and grant persistent access to the MOIS (Ministry of Intelligence).

---

## II. Preventative Hardening: The "Shield"

Prevention is significantly more effective than detection. Once a device is compromised by kernel-level spyware, it cannot be "cleaned"—it must be destroyed or factory reset (with caveats).

### 1. OS Updates & Support

- **Crucial Rule:** Never delay updates. State-sponsored spyware relies on "n-day" vulnerabilities (bugs that have a fix released, but the user hasn't installed yet).
- **End-of-Life:** If your phone no longer receives security updates from Apple or Google, **it is not safe for activism**.

### 2. Apple iOS: Lockdown Mode

For iPhone users in Iran, **Lockdown Mode** is the single most effective defense against zero-click exploits.

- **How it works:** It drastically reduces the "attack surface" by blocking complex web technologies, specific message attachments, and incoming invitations from unknown Apple IDs.
- **To Enable:** `Settings` → `Privacy & Security` → `Lockdown Mode`.
- **Trade-off:** Some websites may load slower, and some images in iMessage may not preview. This is a necessary trade-off for safety.

### 3. Android: Advanced Protection & GrapheneOS

- **Stock Android:** Enable **Google Advanced Protection Program**. This enforces strict checks on app installations and requires a physical security key or passkey for account access.
- **GrapheneOS (Pixel Devices):** For the highest security profile, Raaznet recommends replacing the stock Android OS with **GrapheneOS**. It provides:
  - Hardened memory allocation (making exploits harder).
  - Sandboxed Google Play Services.
  - **Auditor App:** Uses hardware-backed attestation to verify the OS hasn't been tampered with.

### 4. Daily Reboots

Many modern spyware strains are "non-persistent," meaning they live in the device's RAM to avoid leaving forensic trails on the hard drive.

- **Action:** Reboot your phone **every morning**. This kicks out non-persistent malware, forcing the attacker to re-infect the device (which increases their risk of detection).

---

## III. Verifying Integrity: The "Scan"

> [!DANGER] **Warning on Antivirus**
> Standard antivirus apps (Avast, AVG, etc.) **cannot** detect military-grade spyware like Pegasus. Do not rely on them. They often harvest user data themselves.

### 1. Mobile Verification Toolkit (MVT)

Developed by Amnesty International's Security Lab, MVT is the gold standard for forensic analysis. It scans backup files for "Indicators of Compromise" (IOCs).

- **For iOS:** MVT analyzes iTunes backups for suspicious process names and interaction records.
- **For Android:** MVT checks installed APKs and SMS records, though Android diagnosis is harder due to system restrictions.
- **Usage:** MVT is a command-line tool. If you are not technical, seek help from digital security helpdesks (see Section V).

### 2. iMazing (iOS Spyware Analyzer)

iMazing includes a user-friendly implementation of MVT.

- **Function:** It scans your iPhone against a database of known malicious indicators (Pegasus, Predator, KingsPawn).
- **Limitation:** A "clean" scan does not guarantee safety. It only means _known_ indicators were not found.

### 3. Android "Auditor" App

The **Auditor** app (available for GrapheneOS and stock Android 10+) uses the device's hardware security chip to verify the operating system's signing keys.

- **Why use it:** It detects if a malicious actor has physically tampered with your phone to install a rootkit or a modified OS version.
- **Method:** It requires two devices to pair and verify each other.

---

## IV. Defense Against Physical Seizure

In Iran, the risk of arrest is higher than the risk of remote zero-click hacking.

### 1. The Panic Button / Lockdown

- **iPhone:** Rapidly press the Power button 5 times (or hold Power + Volume Up). This disables FaceID/TouchID and forces a passcode entry.
- **Android:** Enable "Lockdown" in power menu settings. This disables biometrics.
- **Why:** Iranian interrogators can force your finger onto a sensor or hold the phone to your face. They cannot legally or easily force you to reveal a complex alphanumeric code in the initial moments of seizure.

### 2. Secondary "Burner" Devices

For protests or high-risk meetings, do not carry your primary device.

- **The Strategy:** Use a cheap, clean phone with only the necessary apps (e.g., Signal).
- **Setup:** Use a prepaid SIM purchased with cash (if possible) or a data-only eSIM. Do not log into your primary Google/Apple ID.
- **Disposal:** If you are chased or cornered, this device can be discarded or wiped without losing your digital life.

### 3. Remote Wipe Preparations

- Ensure **Find My (iOS)** or **Find My Device (Android)** is enabled.
- If your device is confiscated, attempt to issue a "Remote Erase" command from a secure computer immediately.
- **Note:** If the authorities place the device in a Faraday bag (signal blocking), the wipe command will execute the moment it reconnects to a network.

---

## V. What to Do If Compromised

If MVT confirms an infection, or if your device behaves erratically (rapid battery drain, overheating, unknown apps appearing) after a detention:

1.  **Stop Communication:** Immediately disconnect from WiFi and Cellular data (Airplane Mode is not enough; turn the device OFF).
2.  **Faraday Bag:** Place the device in a Faraday bag (or a microwave/fridge temporarily) to block remote signals.
3.  **Do Not Backup:** Do not restore a new phone from the backup of an infected phone. You will likely reinstall the spyware.
4.  **Hardware Replacement:** The only 100% safe removal method for kernel-level spyware is to physically destroy the device and replace it.
5.  **Seek Help:** Contact trusted organizations for forensic assistance:
    - **Amnesty Tech:** For human rights defenders.
    - **Access Now Helpline:** For activists and journalists.
    - **Citizen Lab:** For high-level investigation.

---

## VI. Summary Checklist for High-Risk Iranian Users

| Action              | Frequency | Notes                                            |
| :------------------ | :-------- | :----------------------------------------------- |
| **Reboot Device**   | Daily     | Removes non-persistent implants.                 |
| **OS Update**       | Immediate | Patch vulnerabilities used by NSO/Intellexa.     |
| **Lockdown Mode**   | Always On | Crucial for iOS users.                           |
| **MVT Scan**        | Monthly   | Or after any suspicious event/detention.         |
| **Review App List** | Weekly    | Remove _any_ Iranian app not strictly necessary. |
| **Passcode**        | Permanent | Use 8+ digit alphanumeric code, not 4-6 digits.  |

---

**Related Topics:**

- [[Operational_Security_for_High_Risk_Scenarios]]
- [[Commercial_Platform_Hardening_and_Data_Minimization]]
