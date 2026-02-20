---
title: "Physical Security and Crisis Preparedness"
tags:
  [
    physical-security,
    crisis-response,
    raids,
    irgc,
    basij,
    emergency-planning,
    device-seizure,
  ]
category: "Surveillance Technologies (Iranian Context)"
difficulty: "Intermediate"
audience:
  [Activists, Journalists, Human Rights Defenders, General Public in Iran]
topics:
  [
    "Home Security",
    "Raid Response",
    "Device Encryption",
    "Emergency Evacuation",
    "Duress Planning",
  ]
summary: "Comprehensive guide on securing physical spaces, protecting devices from seizure, and preparing for raids or emergencies in the Iranian context."
source: "Raaznet Aggregated Data (EFF, Security in a Box, Community Reports)"
content_type: "Operational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of digital security",
    "Familiarity with local threat landscape",
  ]
estimated_read_time: "20 minutes"
---

# Physical Security and Crisis Preparedness

Digital security cannot be separated from physical security. The Islamic Republic's security forces (including the IRGC, Ministry of Intelligence, and Basij) frequently utilize physical raids, device confiscation, and arbitrary detention as primary tactics to suppress dissent. A strong password is useless if an agent physically forces you to unlock your phone at gunpoint or if your unencrypted laptop is seized during a home raid.

This guide focuses on securing your physical environment, preparing for the possibility of arrest or raids, and mitigating the damage if your devices fall into hostile hands.

## 1. Securing Your Physical Space (Home and Office)

Your home is your primary base of operations, but it is also a common target for raids. While you cannot turn your home into a fortress against state security forces, you can implement measures that **buy you time**—seconds that are crucial for locking or wiping devices.

### A. Perimeter and Access Control

- **Reinforce Entry Points:** Install high-quality deadbolts and reinforcement plates on doors. While security forces will eventually breach a door, a stronger door provides vital seconds to execute emergency data destruction plans.
- **Window Visibility:** Use heavy curtains or blackout shades. Visual surveillance from street level or adjacent rooftops is common. Ensure screens cannot be seen from windows.
- **Surveillance Awareness:** Be aware of CCTV cameras installed by the municipality or neighbors that cover your entrance. Assume building managers or neighbors may be pressured to share footage or access logs.

### B. Clean Desk Policy

- **Zero Evidence:** Never leave sensitive documents, flash drives, or hardware tokens (like 2FA keys) on desks or in plain sight.
- **Visual Privacy:** When working, position screens away from windows and doors.
- **Paper Shredding:** Do not throw sensitive documents in the trash. Burn them or use a cross-cut shredder. Trash bags left outside are easily retrieved by surveillance teams.

### C. Hiding Places and Decoys

- **The Decoy Strategy:** If raided, security forces expect to find devices. Maintaining a "clean" decoy laptop or phone that you surrender immediately can sometimes satisfy a superficial search, diverting attention from well-hidden secure devices.
- **Deep Concealment:** Secure devices should be stored in non-obvious locations (e.g., inside hollowed-out furniture, false bottoms in drawers, or vents) when not in use.

---

## 2. Protecting Devices Against Physical Seizure

In Iran, the most common threat to digital data is the physical seizure of the device while it is unlocked or the coercion of the user to unlock it.

### A. Full Disk Encryption (FDE)

Encryption is the baseline defense. Without it, physical seizure guarantees data compromise.

- **Computers:** Use **BitLocker** (Windows), **FileVault** (macOS), or **LUKS** (Linux). Ensure the computer is **fully powered off** (not just sleeping) when transporting it or leaving the house.
- **Mobile Devices:** Modern Android and iOS devices are encrypted by default _if_ a passcode is set.

### B. Disable Biometrics (FaceID / Fingerprint)

**CRITICAL FOR IRAN:** Security forces can and will physically force your finger onto a scanner or hold your phone up to your face to unlock it.

- **Disable Biometric Unlock:** Use a strong, alphanumeric passphrase instead.
- **Emergency Lockdown:** Learn the panic gesture for your phone.
  - _iPhone:_ Hold the Power button and either Volume button for 5 seconds (until the slider appears). This disables FaceID and requires the passcode for the next unlock.
  - _Android:_ use the "Lockdown" option if enabled in settings, which disables biometrics and notifications on the lock screen.

### C. "Panic" and "Wipe" Protocols

- **Auto-Wipe:** Configure your device to factory reset after a set number of incorrect password attempts (e.g., 10 attempts).
- **Remote Wipe:** Enable "Find My" (iOS) or "Find My Device" (Android). If you are arrested but your device is left behind (or if a trusted contact has access to your account), the device can be wiped remotely. **Note:** This requires the device to be connected to the internet.
- **Duress Passwords:** Some advanced tools (like VeraCrypt for PCs or custom Android ROMs) allow for "hidden volumes" or "duress passwords" that, when entered, either show a fake environment or silently wipe the encryption keys.

---

## 3. Preparing for Raids ("The Knock at the Door")

Raids in Iran often occur late at night or early in the morning (e.g., between 2:00 AM and 6:00 AM) to maximize psychological shock.

### A. Immediate Response Plan

If security forces are at your door:

1.  **Do Not Open Immediately:** If they do not have a battering ram, do not voluntarily open the door. Use the delay to execute your emergency plan.
2.  **Lock/Wipe Devices:**
    - **Power Off:** Immediately power off all phones and laptops. This places encryption keys in a "cold" state, making forensic recovery much harder.
    - **Destroy SIM Cards:** If safe to do so, break your SIM card. This prevents them from easily intercepting SMS 2FA codes or using your number to impersonate you.
3.  **Silence:** Do not speak to agents more than necessary. Do not answer questions about passwords.
4.  **Non-Resistance:** Once they gain entry, physical resistance can lead to severe injury or death. Adopt a non-confrontational physical posture while maintaining mental resolve to protect your digital information.

### B. Household Protocol

- **Brief Housemates:** Ensure everyone in your home knows the drill. If they hear a specific phrase or noise, they should immediately power off their own devices and stay clear of the entrance.
- **Guest Policy:** Do not allow unknown devices (smartphones of guests you don't fully trust) into sensitive work areas.

---

## 4. Crisis Preparedness and Evacuation

You may need to flee your home with little to no notice due to a credible threat or imminent arrest.

### A. The "Go Bag"

Prepare a bag that is kept ready near the exit. It should contain:

- **Cash:** Physical currency (Rials and stable foreign currency like USD or EUR if possible). Cards may be tracked or frozen.
- **Documents:** Copies of identification (Shenasnameh, National ID card), passport, and deeds/leases. _Store these on an encrypted USB drive as well._
- **Medications:** A supply of essential prescription medications.
- **Communication:** A pre-paid "burner" phone or SIM card that is not linked to your identity.
- **Paper List:** A physical list of emergency contact numbers (lawyers, family, trusted network). Do not rely on your phone's contact list, which may be seized.

### B. Emergency Contacts and "Safe Person"

- **Primary Safe Person:** Designate one trusted individual (ideally outside the country or in a very low-risk position) who holds your backup information.
- **Check-in System:** Establish a routine check-in (e.g., a message every day at 10 AM). If you miss a check-in, they initiate a safety protocol (e.g., locking down your accounts, notifying lawyers).
- **Code Words:** Agree on innocuous phrases that signal danger.
  - _Example:_ "I am going to visit my aunt in Mashhad" might actually mean "I am compromised and destroying my devices."

### C. Safe Houses

- Identify a location where you can stay for 24-48 hours if your home is unsafe. This should be a place not legally linked to you or your immediate family.
- Avoid taking your primary mobile phone to a safe house, as cell tower triangulation will reveal your location. Remove the battery (if possible) or leave the device behind.

---

## 5. Post-Incident Recovery

If your devices have been seized or you have been detained and released:

- **Assume Compromise:** Never trust a device that has been in the possession of security forces. It likely contains spyware or hardware implants.
- **Revoke Access:** Immediately change all passwords and revoke active sessions (e.g., "Log out of all other sessions" in Telegram/Google) from a secure computer.
- **Warn Network:** Notify your contacts immediately that your old accounts/devices are compromised so they do not respond to messages impersonating you.

## Summary Checklist

| Category    | Action Item                                                        | Status |
| :---------- | :----------------------------------------------------------------- | :----- |
| **Devices** | Full Disk Encryption enabled on all laptops/phones                 | ☐      |
| **Access**  | Biometric unlock (Face/Finger) DISABLED                            | ☐      |
| **Access**  | Strong, alphanumeric passcodes set (10+ chars)                     | ☐      |
| **Home**    | "Go Bag" packed and accessible                                     | ☐      |
| **Home**    | Sensitive documents digitized (encrypted) and physically destroyed | ☐      |
| **Network** | Emergency "Safe Person" designated and briefed                     | ☐      |
| **Drill**   | Practice the "Power Off" drill for raids                           | ☐      |

**Disclaimer:** This guide provides best practices for physical security. However, no measure guarantees safety against a determined state actor. Always weigh these recommendations against your specific personal risk profile in Iran.
