---
title: "High-Risk Operations: Protests and Travel Security"
tags:
  [
    opsec,
    protest-safety,
    travel-security,
    border-crossing,
    iran,
    physical-security,
    emergency-planning,
    digital-safety,
  ]
category: "Operational Security (OpSec)"
difficulty: "Advanced"
audience:
  [Activists, Journalists, Political Dissidents, High-Risk Individuals in Iran]
topics:
  [
    "Protest Security",
    "Border Crossings",
    "Arrest Protocols",
    "Device Hygiene",
    "Surveillance Detection",
  ]
summary: "A comprehensive guide for Iranian activists and high-risk individuals on maintaining digital and physical security during protests, direct actions, and travel. Includes strategies for device sanitization, border crossings, and emergency response."
source: "Consolidated from Security in a Box, Tactical Tech, and Freedom of the Press Foundation"
content_type: "Operational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Understanding of Threat Modeling",
    "Basic Encryption Knowledge",
    "Familiarity with Mobile Security",
  ]
estimated_read_time: "25 minutes"
---

# High-Risk Operations: Protests and Travel Security

"High-risk operations" encompass activities such as participating in street protests, organizing dissent, transporting sensitive information, and crossing borders (both domestic checkpoints and international). The Islamic Republic's surveillance apparatus uses a combination of advanced digital monitoring (IMSI catchers, traffic analysis) and physical intimidation (device seizure, forced unlocking).

This guide consolidates operational security (OpSec) protocols to mitigate risks during these critical moments. It assumes an adversarial environment where legal protections are minimal or non-existent.

---

## 1. Protest and Direct Action Security

Participating in protests in Iran carries the risk of arrest, physical violence, and long-term surveillance. Your digital footprint can be used not only to incriminate you but to map your entire social network.

### A. Device Preparation (The "Burner" Strategy)

The safest phone at a protest is **no phone**. However, communication and documentation are often necessary.

1.  **Use a Secondary Device:**
    - **The "Burner" Concept:** Do not bring your primary smartphone containing your life's data (personal photos, main accounts, contacts) to a protest. Use a cheap, secondary smartphone.
    - **Minimal Data:** This device should have _only_ the apps necessary for the specific action (e.g., Signal, a camera app).
    - **New/Clean Accounts:** Register accounts (Google, Signal) using a separate, anonymous email and, if possible, a burner SIM card or VoIP number not linked to your real identity.

2.  **Sanitize Your Primary Device (If you must bring it):**
    - **Back Up and Wipe:** If you cannot obtain a secondary phone, back up your primary phone to a secure, local location (encrypted computer or USB), then **factory reset** it before the protest. Restore only essential apps.
    - **Remove Sensitive Apps:** Uninstall banking apps, primary social media (Instagram, X/Twitter), and email clients.
    - **Log Out:** Log out of all browser sessions and cloud accounts.

### B. Hardening the Device

Whether using a secondary or primary device, apply these settings before leaving home:

- **Disable Biometrics:** Turn off Face Unlock and Fingerprint Unlock. Iranian security forces can physically force you to look at your phone or press your finger against the sensor.
- **Strong Passcode:** Use a random, 6-to-8 digit numeric PIN or a strong alphanumeric password. Do not use patterns (grease smudges reveal them).
- **Encryption:** Ensure device encryption is active (standard on modern Android/iOS).
- **Disable Location Services:** Turn off GPS/Location entirely in settings. Put the phone in **Airplane Mode** when not actively communicating to prevent tower triangulation (though this prevents receiving calls).
- **Disable Notifications:** Set notifications to show no content on the lock screen to prevent police from reading messages over your shoulder or on a confiscated device.

### C. Communications During Action

- **Signal:** Use Signal for all communications.
  - **Disappearing Messages:** Set a short timer (e.g., 1 hour or less) for all chats related to the protest.
  - **Registration Lock:** Enable this to prevent authorities from hijacking your account if they seize your SIM card.
  - **Hide Phone Number:** In Signal settings, set "Who can see my phone number" to "Nobody".
- **Avoid Regular SMS/Call:** These are unencrypted and easily intercepted by telecommunication providers (MCI, Irancell) monitoring for the state.

### D. Documentation (Filming and Photos)

Documenting human rights abuses is vital, but it carries high risks.

- **Metadata Removal:** Photos contain "EXIF" data (time, date, GPS coordinates, device model). Use apps that scrub this data automatically or remove it before sharing.
  - _Android Tools:_ **ObscuraCam** or **Scrambled Exif**.
  - _iOS Tools:_ **ViewExif** or use Signal's built-in blur tool before sending.
- **Blur Faces:** Always blur the faces of fellow protesters before publishing or sharing footage to protect them from facial recognition software utilized by Iranian authorities.
- **Quick Capture & Hide:** If you film police violence, immediately move the file to a hidden folder (e.g., Android's "Safe Folder" or "Private Space") or disguise the app icon (e.g., using **Tella** disguised as a calculator).

---

## 2. Travel and Border Crossing Security

Crossing borders (including airports like IKA and land borders) places you under the direct physical control of authorities who may seize and search devices without a warrant.

### A. The "Clean Crossing" Protocol

The only way to guarantee data safety at a border is to not carry the data across the border.

1.  **Cloud Sync & Wipe:**
    - Encrypt your sensitive data and upload it to a secure cloud storage provider (e.g., Proton Drive, Mega).
    - **Factory reset** your laptop and phone before the crossing.
    - Cross the border with "blank" devices.
    - Once in a safe location, download and decrypt your data.
    - _Note:_ This requires reliable internet access on the other side.

2.  **Hidden Volumes (Advanced):**
    - If you must carry data physically, use **VeraCrypt** to create a hidden volume. This creates a decoy encrypted container that looks like legitimate data, while the sensitive data is hidden within it. If forced to give up a password, you reveal the decoy password, not the sensitive one.

### B. Physical Inspections

- **Power Down:** Fully power off devices before approaching checkpoints. Cold boot attacks are harder than accessing a device in sleep mode. Encryption keys are cleared from RAM when powered off.
- **Tamper Evidence:** Place tamper-evident tape or unique glitter nail polish over screws and ports of laptops. Photograph it before travel. If the seal is broken upon arrival, assume the hardware has been compromised (bugged).
- **Leave Primary SIMs Behind:** Do not travel with your primary Iranian SIM card if fleeing or traveling for sensitive work. It links your location history to your passport identity.

### C. Digital Hygiene on the Move

- **Never Use Public WiFi:** Airport and hotel WiFi networks are notoriously insecure and often monitored. Use a mobile hotspot or a reputable VPN if you must connect.
- **VPN Strategy:** In Iran, use VPNs with obfuscation (like **Tor** with bridges or **v2ray**) to mask traffic. Ensure your "Kill Switch" is active so data doesn't leak if the VPN drops.

---

## 3. Operational Security (OpSec) & Affinity Groups

Security is collective. Organizing in small, trusted "affinity groups" (2-10 people) is safer than large, loose networks.

### A. Affinity Group Protocols

1.  **Vetting:** Only include people you know and trust personally. Do not vouch for strangers.
2.  **Roles:** Assign roles for protests (e.g., medic, legal observer, communication liaison).
3.  **The "Buddy System":** Never go to a protest alone. Arrive together, stay together, leave together. If a buddy is grabbed, the other documents the arrest and notifies the support network.
4.  **Need-to-Know:** Limit information sharing. Not everyone needs to know the full scope of a plan—only what is necessary for their role.

### B. Emergency Response Plan

Before any high-risk operation, establish a protocol for "When Things Go Wrong."

1.  **Proof of Life / Check-ins:** Establish strict check-in times with a trusted contact who is _not_ at the protest.
    - _Protocol:_ "If I do not message by 20:00, assume I am detained and execute Plan B."
2.  **Plan B (The Dead Man's Switch):**
    - If you are detained, your trusted contact should have instructions (and potentially access) to revoke your digital tokens, lock down social media accounts, or remote wipe devices if possible.
3.  **Legal Preparation:** Have the name and number of a human rights lawyer written on your arm or body (hidden under sleeves) in permanent marker. Paper can be confiscated; phones can be taken.

### C. Counter-Surveillance

- **Situational Awareness:** Constantly scan your environment. Look for individuals loitering, filming continuously, or wearing improper clothing for the setting (e.g., tactical boots with civilian clothes).
- **Route Variation:** Do not use the same route to leave a protest or return home. Use counter-surveillance driving/walking techniques (e.g., three consecutive turns, stopping abruptly) to detect if you are being followed.
- **Change Appearance:** Bring a change of clothes (jacket, hat, glasses) to alter your silhouette when leaving a high-risk zone.

---

## 4. Localized Context: Specific Iranian Threats

### "Gasht-e Ershad" and Plainclothes Forces

Basij and plainclothes officers often infiltrate crowds to identify leaders or violent instigators. They may photograph participants for later arrest.

- **Counter-measure:** Wear a mask (medical or otherwise) and sunglasses to defeat facial recognition. Cover distinctive tattoos or scars.

### Forced Unlocking

Iranian interrogators are known to use physical force to unlock phones.

- **Counter-measure:** This highlights the importance of **disabling biometrics**. It is physically harder to force someone to recall and type a complex alphanumeric password than to force a finger onto a sensor. If you are in imminent danger of arrest, power off the phone immediately to engage full disk encryption (BFU - Before First Unlock state).

### Digital Extraction (Cellebrite/GrayKey)

Iranian intelligence agencies possess forensic tools capable of extracting data from seized phones.

- **Counter-measure:** Auto-delete messages on Signal/Telegram. Use a 6+ digit PIN. If possible, use a device with a "Secure Element" (like Google Pixel's Titan chip or iPhone's Secure Enclave) which resists brute-force attacks better than older hardware.

---

## 5. Checklist Summary

### Before Deployment

- [ ] Device sanitized or secondary device procured.
- [ ] Biometrics disabled; strong alphanumeric passcode set.
- [ ] Location services and non-essential radios (Bluetooth/NFC) off.
- [ ] Emergency contacts written on body.
- [ ] Check-in protocol established with external ally.
- [ ] Sensitive apps hidden or protected by secondary PINs.
- [ ] Full device backup created and stored securely offline.

### During Operation

- [ ] Maintain visual contact with affinity group.
- [ ] Use encrypted comms (Signal) with disappearing messages.
- [ ] Blur faces before capturing any footage.
- [ ] Watch for surveillance indicators.

### Post-Operation

- [ ] Safe route home (check for tails).
- [ ] Debrief with affinity group (securely).
- [ ] Digital cleanup: Delete photos/videos from device once backed up safely.
- [ ] Leave sensitive Signal groups if they are no longer needed.
