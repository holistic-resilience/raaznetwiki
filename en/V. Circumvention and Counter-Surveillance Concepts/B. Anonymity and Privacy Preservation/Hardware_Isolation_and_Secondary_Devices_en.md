---
title: "Hardware Isolation and Secondary Devices"
tags:
  [
    hardware-security,
    isolation,
    burner-phones,
    qubes-os,
    tails,
    air-gap,
    faraday-bags,
    iran-security,
    compartmentalization,
  ]
category: "Device Security"
difficulty: "Advanced"
audience: [Activists, Journalists, High-Risk Individuals, Protesters]
topics:
  [
    "Device Isolation",
    "Secondary Phones",
    "Secure Operating Systems",
    "Physical Security",
  ]
summary: "A comprehensive guide to using hardware isolation and secondary devices to protect sensitive data. Covers strategies for secondary phones in the Iranian context, air-gapped systems, and secure operating systems like Tails and Qubes."
source: "Raaznet Wiki"
content_type: "Operational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Understanding of basic threat modeling",
    "Familiarity with operating systems installation",
    "Basic knowledge of mobile networks",
  ]
estimated_read_time: "15 minutes"
---

# Hardware Isolation and Secondary Devices

In high-risk environments—such as attending protests, crossing borders, or conducting sensitive investigations—software security alone may not be enough. If an adversary gains physical access to your device, or if your operating system is compromised by malware, software encryption can be bypassed.

**Hardware isolation** involves using separate physical devices for different activities to prevent data leaks and cross-contamination. This guide explores how to implement hardware isolation strategies effectively, tailored to the specific constraints and threats within Iran.

## The Principle of Compartmentalization

Compartmentalization is the practice of separating sensitive information from your everyday digital life. By using different hardware for different tasks, you ensure that if one device is seized, hacked, or monitored, your other identities and data remain secure.

**Levels of Isolation:**

1.  **Virtualization:** Running separate virtual machines (VMs) on one physical computer.
2.  **Live Systems:** Booting a temporary, amnesic operating system (like Tails) from a USB stick.
3.  **Physical Separation:** Using completely different devices (secondary phones, air-gapped laptops) for specific tasks.

---

## Secondary Smartphones ("Protest Phones")

For activists and protesters in Iran, carrying a primary smartphone—containing personal photos, chats, and contacts—is extremely dangerous. A secondary phone (often called a "burner phone," though true anonymity is difficult) minimizes the data available to authorities if the device is confiscated.

### The Challenge of Anonymity in Iran (Hamta Registry)

In many countries, you can buy a "burner" phone and a prepaid SIM with cash for complete anonymity. **In Iran, this is nearly impossible due to the Hamta registry scheme.**

- Mobile phones must be registered with the network using a National ID or Passport.
- SIM cards require valid identification to activate.
- Therefore, **assume the device and SIM can be linked to your legal identity.**

**The Goal:** Since anonymity of _ownership_ is difficult, focus on **minimizing data**. If the phone is seized, it should contain nothing incriminating and no links to your main social circles.

### Checklist for a Secondary Phone

#### 1. Hardware Selection

- **Use an older device:** A spare phone you already own or a cheap second-hand smartphone.
- **Factory Reset:** Wipe the device completely before configuring it for sensitive use.
- **No Biometrics:** Do not set up Face ID or Fingerprint unlock. You can be physically forced to unlock these. Use a strong, alphanumeric PIN or passphrase (at least 8-10 digits).

#### 2. Clean Setup (Data Minimization)

- **No Personal Accounts:** Do not sign in with your primary Google (Gmail) or Apple (iCloud) account. Create a fresh, dedicated account for this device if necessary, or use it without an account (e.g., using F-Droid on Android).
- **Minimal Apps:** Install only what is strictly necessary (e.g., Signal, a VPN, a secure camera app).
- **No Contact Syncing:** Do not import your contact list. Manually save only essential numbers (lawyer, emergency contact) using pseudonyms or memorize them.

#### 3. Secure Communications

- **Signal Only:** Use Signal with a [username](https://signal.org/blog/phone-number-privacy-usernames/) and hide your phone number. Set "Disappearing Messages" to a short timer by default.
- **VPN/Tor:** Install a robust, obfuscated VPN (e.g., Mullvad, IVPN, or a private Outline server) or use Tor Browser for Android.
- **Offline Maps:** Use Organic Maps or OsmAnd with downloaded maps of your city (Tehran, Mashhad, etc.) so you don't need data to navigate.

#### 4. During High-Risk Events

- **Leave it off:** Keep the phone powered off until absolutely necessary.
- **Faraday Bag:** Store the phone in a Faraday bag (RF shielding pouch) to block all signals (Cellular, Wi-Fi, Bluetooth, GPS) preventing location tracking while moving.
- **Emergency Wipe:** Know how to factory reset the device quickly. On some Android ROMs (like GrapheneOS), you can set a "duress PIN" that wipes the device when entered.

---

## Secure Operating Systems and Live USBs

If you cannot afford separate physical computers, you can turn a single laptop into an isolated secure station using specialized operating systems.

### Tails (The Amnesic Incognito Live System)

**Best for:** Extreme anonymity, whistleblowing, and temporary use on untrusted computers.

[Tails](https://tails.net/) is a portable operating system that runs from a USB stick.

- **Amnesic:** It forgets everything after you shut it down. No trace is left on the computer's hard drive.
- **Tor-Enforced:** All internet traffic is forced through the Tor network. Unsafe connections are blocked.
- **Encryption:** Includes tools like LUKS (for encrypted persistent storage), VeraCrypt, and GnuPG out of the box.

**Usage Scenario:** An activist needs to edit a sensitive document and email it securely. They boot Tails from a USB on their family laptop, do the work, and shut down. The family laptop retains no record of the activity.

### Qubes OS

**Best for:** High-risk users needing persistent, compartmentalized workspaces.

[Qubes OS](https://www.qubes-os.org/) is a desktop operating system that implements "Security by Compartmentalization." It uses the Xen hypervisor to isolate different activities into separate Virtual Machines (called "qubes").

- **Isolation:** If you open a malicious PDF in your "Untrusted" qube, the malware cannot escape to infect your "Personal" or "Vault" qubes.
- **Whonix Integration:** Qubes allows you to run Whonix (a Tor gateway) easily, ensuring specific qubes are always routed through Tor.
- **Hardware Requirements:** Requires a reasonably powerful computer (16GB+ RAM recommended) and specific CPU features (VT-x/VT-d).

---

## Air-Gapped Machines

An **air-gapped** computer is one that is physically isolated from unsecured networks—it has no Wi-Fi, Bluetooth, or Ethernet connection to the internet.

**Use Cases:**

- Generating and storing PGP private keys.
- Storing cryptocurrency cold wallets.
- Editing leaked documents that must never be exfiltrated.

**How to maintain an Air-Gap:**

1.  **Physical Removal:** Physically remove the Wi-Fi and Bluetooth cards from the laptop/desktop. Glue USB ports shut or use USB data blockers if strictly necessary.
2.  **Data Transfer:** Data should only enter/exit via one-way methods (like QR codes scanned by a camera) or carefully sanitized USB drives (though USBs present a risk of bridging the gap via malware like Stuxnet).
3.  **Physical Security:** Store the machine in a safe or hidden location.

---

## Physical Isolation Accessories

### Faraday Bags

These pouches are lined with conductive metal mesh that blocks all radio signals.

- **Purpose:** Prevents a phone from connecting to cell towers (stopping location tracking) and prevents remote access/wiping by authorities.
- **Usage:** Place your phone inside before traveling to a sensitive location. Only remove it when you need to use it.

### USB Data Blockers ("Connectors")

Small adapters that place between your USB cable and a charging port. They physically disconnect the data pins, allowing only power to pass through.

- **Purpose:** Protects against "Juice Jacking"—malware installation via public charging stations (e.g., at airports or cafes).

### Hardware Security Keys (YubiKey / Nitrokey)

Physical tokens used for Two-Factor Authentication (2FA).

- **Why Isolation?** The cryptographic secret is stored on the separate hardware chip, not on your computer or phone. Even if your computer is infected with malware, the attacker cannot steal the physical key required to log in.

---

## Summary of Recommendations for Iranian Context

| Threat Scenario             | Recommended Hardware Strategy                                                                                |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **Daily Use / Low Risk**    | Primary smartphone with strong passphrase + VPN.                                                             |
| **Protest / Gathering**     | **Secondary Phone:** Cheap/Old device, no SIM (Wi-Fi only) or pre-registered SIM, minimal data, Faraday bag. |
| **Sensitive Communication** | **Tails OS:** Booted from USB on a laptop. Do not use Windows/macOS for leaking documents.                   |
| **Key Storage / Archives**  | **Air-Gapped Device:** An old laptop with networking hardware removed, encrypted with VeraCrypt/LUKS.        |

### Final Warning

Hardware isolation increases security, but it also increases complexity. **Complexity is the enemy of security.** Ensure you practice using your secondary devices, Tails USBs, or Faraday bags _before_ you are in a high-stress situation. A locked burner phone you cannot unlock or a Tails USB that won't boot is useless in an emergency.
