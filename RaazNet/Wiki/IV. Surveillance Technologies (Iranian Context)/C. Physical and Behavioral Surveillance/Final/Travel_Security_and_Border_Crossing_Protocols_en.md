---
title: "Travel Security and Border Crossing Protocols"
tags:
  [
    travel-security,
    border-control,
    iran-border,
    digital-sanitization,
    burner-phones,
    interrogation,
    dual-nationals,
    physical-security,
  ]
category: "Surveillance Technologies (Iranian Context)"
difficulty: "Advanced"
audience: [Activists, Journalists, Dual Nationals, General Public]
topics:
  [
    "Border Security",
    "Device Confiscation",
    "Interrogation Techniques",
    "Digital Hygiene",
    "Physical Surveillance",
  ]
summary: "Comprehensive guide for Iranian citizens and dual nationals on securing digital devices and physical safety when crossing borders (air, land, or sea), specifically tailored to mitigate risks posed by Iranian intelligence and security forces (IRGC, Ministry of Intelligence)."
source: "Raaznet Aggregated Resources"
content_type: "Operational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Understanding of Digital Surveillance",
    "Basic Encryption Knowledge",
    "Risk Assessment",
  ]
estimated_read_time: "20 minutes"
---

# Travel Security and Border Crossing Protocols

## Overview

For Iranian citizens, activists, and dual nationals, crossing international borders is one of the most vulnerable moments in any operational security model. Iranian borders—particularly Imam Khomeini International Airport (IKA) and land crossings with Turkey and Iraq—are heavily monitored by the **Islamic Revolutionary Guard Corps (IRGC)**, the **Ministry of Intelligence (VAJA)**, and **NAJA (Law Enforcement Command)**.

Unlike in democratic jurisdictions where legal frameworks like the Fourth Amendment (US) or GDPR (EU) may offer some protection against warrantless searches, Iranian border control operates with broad extrajudicial powers. Security agents can and do confiscate devices, demand passwords, and detain individuals without immediate legal recourse.

This guide consolidates protocols for minimizing data exposure, handling physical surveillance, and preparing for potential detention during travel.

---

## I. Pre-Travel Risk Assessment

Before traveling, you must assess your "threat profile."

1.  **Exit Ban Check (_Mamnoo-ol-khorooj_):**
    - In Iran, activists, journalists, and even ordinary citizens involved in financial disputes or protests may be placed on a "no-fly" list without notification.
    - **Action:** Check your exit status electronically via the "Police My" (Police-e Man) app or the official exit status portal before heading to the airport. However, be aware that high-level security bans (by IRGC Intelligence) often do not appear on public databases and strictly manifest at the passport control counter.
2.  **Dual National Risk:**
    - Dual nationals are frequent targets for "hostage diplomacy." If you hold a passport from a Western nation (specifically US, UK, Canada, EU, Australia), assume you are a high-value target.
    - **Protocol:** Never travel with your foreign passport as your primary identification within Iran. Ensure your Iranian documents are flawless.

---

## II. Digital Device Hygiene (The "Clean Travel" Rule)

The most effective defense against a digital strip search is to have nothing to find. **Do not rely on encryption or "rights" to refuse unlocking your device.** Refusal to unlock a device in Iran can lead to indefinite detention or torture.

### A. The "Burner" Device Strategy

The safest protocol is to **leave your primary devices at home**.

- **Acquire a Travel Device:** Buy a cheap, used, or separate smartphone/laptop specifically for travel.
- **Sanitization:** This device should contain _no_ sensitive data, no history of protest activity, and no contacts related to activism.
- **Setup:** Populate the device with "mundane" data (family photos, generic music, standard apps like Snapp or Digikala) to avoid the suspicion that comes with a factory-reset "empty" phone.

### B. Sanitizing Your Primary Device (If You Must Bring It)

If you cannot use a burner device, you must ruthlessly sanitize your current one _before_ arriving at the airport/border.

1.  **Cloud Migration & Wipe:**
    - Back up sensitive data to a secure cloud service (e.g., Proton Drive, cryptomator-encrypted cloud).
    - **Factory Reset:** This is the only way to ensure deleted files are not recoverable by forensic tools (like Cellebrite, often used by Iranian authorities).
    - _Warning:_ Forensic tools can detect a recent factory reset. If asked, have a plausible cover story (e.g., "The phone was glitching/slow").
2.  **Social Media & Messaging:**
    - **Log Out & Uninstall:** Remove Telegram, WhatsApp, Signal, Instagram, and Twitter (X).
    - **Browser Hygiene:** Clear all history, cookies, and saved passwords.
    - **Gallery Check:** Manually audit your photo gallery. Remove screenshots of tweets, photos of unveiled women (if strict enforcement is active), or protest imagery. Check the "Recently Deleted" folder and empty it.
3.  **VPNs and Circumvention Tools:**
    - While most Iranians use VPNs, having specific "activist-grade" tools (e.g., Tor, Orbot, specific private bridges) visible can flag you for secondary screening.
    - **Strategy:** Uninstall VPN apps before the border. Memorize a download link or carry an installer on a hidden partition of a USB drive for re-installation _after_ you clear customs.

---

## III. Physical Security & Anti-Tampering

Iranian security services may attempt to physically tamper with devices left unattended (e.g., in hotel rooms or checked luggage) or during confiscation at the border.

### A. Laptop & Hardware Security

1.  **Full Disk Encryption (FDE):** Ensure BitLocker (Windows), FileVault (macOS), or LUKS (Linux) is enabled. While you may be forced to unlock it, FDE prevents data access if the device is stolen or seized without your presence.
2.  **Tamper Detection (Glitter/Nail Polish Method):**
    - Apply a unique pattern of glitter nail polish over the screws of your laptop case. Take a high-resolution photo of it.
    - Upon return, compare the screws to the photo. If the pattern is broken, the device has been physically opened and likely implanted with a hardware keylogger or beacon.
3.  **Power Off:** Fully power down devices before approaching checkpoints. This clears RAM (removing encryption keys from memory) and forces a "Cold Boot" attack, which is much harder than attacking a device in Sleep mode.

### B. Biometrics (FaceID / Fingerprint)

- **Disable Biometrics:** Turn off FaceID and TouchID before approaching the border. Set a strong alphanumeric passcode (8+ digits).
- **Why:** An agent can physically force your finger onto a sensor or hold the phone to your face to unlock it instantly. They cannot force your mind to recall a password as easily without crossing into physical coercion (which takes time and specific authorization).

---

## IV. At the Checkpoint: Behavioral Protocols

### A. Interactions with Agents

- **Minimize Speech:** Answer only what is asked. Do not volunteer information.
- **Body Language:** Nervousness is a primary indicator for behavioral detection officers. Maintain a calm, bored demeanor.
- **The "Grey Rock" Method:** Be uninteresting. If questioned about your work or travel, provide simple, verifiable, and boring answers.

### B. Secondary Screening

If you are pulled aside for secondary screening ("Otagh-e Amniat"):

1.  **Compliance:** In the Iranian context, aggressive assertion of rights usually escalates the situation. Comply with instructions to unlock devices if you have prepared them (i.e., they are clean).
2.  **Duress Passwords:** If your device supports it (e.g., certain custom Android ROMs), use a "duress password" that unlocks a dummy user profile or wipes the device. _Warning: Use this only if you are certain the agent is not tech-savvy; triggering a wipe can be seen as destruction of evidence._

### C. Forced Password Disclosure

If you are forced to hand over passwords:

- **Write it down:** If possible, write the password down rather than speaking it aloud.
- **2FA Traps:** If you have 2FA enabled (which you should), ensure your 2FA method (e.g., YubiKey or Authenticator app) is not on the same device you are unlocking, or be prepared to hand over the 2FA code if under extreme duress.
- **Post-Event Protocol:** As soon as you are released and have internet access, assume all accounts accessed on that device are compromised. Revoke sessions and change passwords immediately from a secure device.

---

## V. Special Considerations: Aerial & Visual Surveillance

While crossing land borders or moving through airports, you are subject to advanced visual surveillance.

1.  **Facial Recognition:** Iran's national ID database (_Kart-e Melli_) is linked to CCTV networks. Cameras at IKA airport and major terminals are capable of matching faces to the national registry.
    - _Countermeasure:_ Wear a standard medical mask (COVID-style) if permitted. While modern algorithms can detect faces with masks, it increases the error rate.
2.  **Smart Hijab Cameras:** Automated systems identify women violating mandatory hijab laws. This can trigger an immediate travel ban or summons.
    - _Protocol:_ Strictly adhere to dress codes within the airport and border zones to avoid flagging by automated behavioral systems.
3.  **Location Tracking:** Be aware that Iranian SIM cards (MCI, Irancell, RighTel) are fully accessible to security services. Your location is triangulated the moment you turn on your phone.
    - _Protocol:_ Keep your phone in "Airplane Mode" with WiFi/Bluetooth off until absolutely necessary, or use a Faraday bag to block signals completely until you are clear of the sensitive zone.

---

## VI. Emergency Plan & Support Network

Before you travel, establish a **Proof of Life** protocol.

1.  **Trusted Contact:** Designate one person (outside Iran, if possible) who knows your exact itinerary.
2.  **Dead Man's Switch:** If you do not check in by a certain time (e.g., "I will message you 1 hour after landing"), they should execute a pre-planned response (e.g., contacting lawyers, locking down your social media accounts, notifying family).
3.  **Go Bag:** If you are an activist fearing imminent arrest at your home, keep a "Go Bag" packed with cash (USD/Euro), a change of clothes, and a paper list of emergency numbers (lawyers, family). Do not keep digital devices in this bag.

---

### Summary Checklist

- [ ] **Check Exit Ban Status** (Mikhak/Police+10).
- [ ] **Sanitize Devices:** Factory reset or bring a burner phone.
- [ ] **Cloud Backup:** Upload sensitive data; delete local copies.
- [ ] **Social Media:** Log out and uninstall apps.
- [ ] **Biometrics:** Disable FaceID/Fingerprint unlock.
- [ ] **Encryption:** Enable Full Disk Encryption; power off device fully.
- [ ] **Communication:** Set up a check-in protocol with a trusted contact.
