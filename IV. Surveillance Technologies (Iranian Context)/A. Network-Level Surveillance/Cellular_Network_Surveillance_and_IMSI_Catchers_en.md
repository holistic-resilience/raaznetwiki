---
title: "Cellular Network Surveillance and IMSI Catchers"
tags:
  [
    mobile-security,
    surveillance,
    imsi-catchers,
    siam-system,
    irgc,
    privacy,
    iran-protests,
    2g-downgrade,
  ]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Protesters, Journalists]
topics:
  [
    "Mobile Network Tracking",
    "SIAM System",
    "IMSI Catchers",
    "Location Tracking",
    "Counter-Surveillance",
  ]
summary: "A comprehensive guide to how the Iranian government tracks mobile phones via the SIAM system and local IMSI catchers, including detection methods and defense strategies."
source: "Raaznet Aggregated Research"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of mobile networks (2G/3G/4G)",
    "Smartphone settings knowledge",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-17"
---

# Cellular Network Surveillance and IMSI Catchers

In Iran, mobile phone surveillance operates on two distinct levels: **Network-Level Surveillance**, integrated directly into the infrastructure of mobile operators (MCI, Irancell, Ariantel) via systems like **SIAM**, and **Street-Level Surveillance**, conducted using tactical devices known as **IMSI Catchers** (or Stingrays).

For Iranian activists and citizens, understanding these mechanisms is critical. Your mobile phone is often the primary tracking device used by the Islamic Revolutionary Guard Corps (IRGC) and the Ministry of Intelligence (MOIS) to identify protesters, map social networks, and intercept communications.

---

## 1. Network-Level Surveillance: The SIAM System

While IMSI catchers are physical devices deployed in specific areas, **Network-Level Surveillance** covers the entire country. In Iran, this is largely orchestrated through a system known as **SIAM** (Integrated System to Query Telecom Customer Information).

### What is SIAM?

SIAM is a web-based API and backend system that sits between Iran's mobile network operators and the **Communications Regulatory Authority (CRA)**. It grants security agencies direct, remote access to user data without the need for a warrant or operator intervention.

### Capabilities of SIAM

Leaked documents and technical analyses have revealed that SIAM allows operators to perform the following actions on specific targets:

- **Speed Throttling:** Remotely reducing a user's data speed to make uploading videos or accessing heavy content impossible.
- **Force 2G Mode:** Downgrading a target's connection from 4G/LTE to 2G. This is a critical attack vector because **2G encryption is weak and easily broken**, allowing for real-time interception of calls and SMS.
- **Location Tracking:** identifying which cell tower a user is connected to, allowing for the triangulation of their location.
- **Bulk Queries:** Identifying all phone numbers present in a specific "geofence" (e.g., a protest square) at a specific time.
- **Contact Analysis:** Generating detailed summaries of who spoke to whom, creating a "social graph" of dissidents.

> **Warning:** During the 2022 protests, citizens received SMS warnings stating they were present in "illegal gatherings." This was a direct result of bulk location queries via systems like SIAM.

---

## 2. Street-Level Surveillance: IMSI Catchers (Stingrays)

**IMSI Catchers** (also known as Cell-Site Simulators or Stingrays) are tactical surveillance devices used by security forces on the ground. They are often mounted in unmarked vans, hidden in backpacks, or even deployed via drones.

### How They Work

Mobile phones are designed to connect to the cell tower with the strongest signal. An IMSI catcher masquerades as a legitimate cell tower, broadcasting a signal stronger than the real network.

1.  **The Trap:** Your phone disconnects from the real MCI or Irancell tower and connects to the IMSI catcher.
2.  **The ID Grab:** The device requests your phone's **IMSI** (International Mobile Subscriber Identity) and **IMEI** (device serial number).
3.  **The Attack:** Once connected, the device can:
    - Pinpoint your exact location (more precise than network triangulation).
    - Intercept unencrypted SMS and calls.
    - Deploy spyware or malicious configuration packets.
    - Block your service (Denial of Service).

### Usage in Iran

The IRGC and Basij forces use these devices heavily during protests to identify attendees. Because the device acts as a "Man-in-the-Middle," they can capture the identities of everyone in a crowd, even if the users are not making calls.

**Foreign Technology:** Reports indicate that Iran has acquired this technology from various sources, including Chinese vendors (ZTE, Huawei) and through sanctions-evasion networks involving European and Russian firms (e.g., Protei).

---

## 3. Indicators of Surveillance

It is difficult to detect professional surveillance, but certain anomalies can serve as warning signs.

### Signs of an IMSI Catcher or 2G Attack

- **Unexpected Network Downgrade:** Your phone switches from 4G/LTE to **2G (E or G)** or **3G** in an area where you normally have strong high-speed coverage.
- **Battery Drain & Heat:** Your phone becomes hot and the battery drains rapidly. This happens because the fake tower often forces the phone to transmit at maximum power.
- **Connectivity Issues:** Calls drop frequently, or you have full signal bars but cannot access the internet.
- **Strange SMS:** Receiving "Welcome" messages from unknown networks or blank SMS messages (silent SMS used for triangulation).

---

## 4. Defense and Mitigation Strategies

While it is nearly impossible to completely block a state-level actor, you can significantly increase the cost and difficulty of surveillance.

### A. Force 4G/LTE Only (Critical)

Since both SIAM and IMSI catchers often rely on downgrading you to 2G to break encryption, disabling 2G is a powerful defense.

- **Android:**
  1.  Dial `*#*#4636#*#*` to open the Testing menu.
  2.  Select **Phone Information**.
  3.  Find "Set Preferred Network Type".
  4.  Change it to **LTE Only** (or `NR/LTE` for 5G/4G).
  - _Note: This may prevent you from making standard voice calls if VoLTE is not supported by your carrier, but data/Signal calls will work._

- **iPhone:**
  - Go to **Settings > Cellular > Cellular Data Options > Voice & Data**.
  - Ensure **LTE** is selected. (Note: iOS does not allow a strict "LTE Only" lock as easily as Android, making iPhones slightly more vulnerable to downgrade attacks).

### B. Secure Communication Apps (Signal)

Standard SMS and voice calls are insecure and easily intercepted.

- Use **Signal** for all communications.
- **Enable "Relay Calls":** This features routes your calls through Signal's servers, hiding your IP address from the contact and potentially from the ISP.
  1.  Signal Settings > **Privacy** > **Calls**.
  2.  Enable **Always Relay Calls**.

### C. Physical Security (The Faraday Bag)

If you are attending a sensitive meeting or protest and do not need your phone:

- **Leave it at home:** This is the only 100% secure method.
- **Remove the Battery:** If your device allows it.
- **Faraday Bag:** Place the phone in a radio-frequency (RF) shielding bag. This physically blocks all signals (Cellular, WiFi, Bluetooth, GPS).
  - _DIY Option:_ Wrapping the phone in multiple layers of heavy-duty aluminum foil can act as a temporary measure, though it is less reliable than a commercial bag.

### D. Detection Tools (Advanced)

Some Android apps claim to detect IMSI catchers. **Use with caution**, as they generate false positives and often require "Root" access to function effectively.

- **SnoopSnitch:** Analyzes mobile network traffic for patches and interception. Requires a rooted phone with a Qualcomm chipset.
- **Cell Spy Catcher:** A simpler heuristic-based detector.

> **Raaznet Recommendation:** Do not rely solely on apps. If you suspect you are being targeted, assume your location is compromised and act accordingly (move to a different location, switch devices, or go offline).

---

## 5. Summary Checklist for Iranian Users

| Action                 | Impact                        | Difficulty |
| :--------------------- | :---------------------------- | :--------- |
| **Use Signal**         | Encrypts content              | Low        |
| **Enable Relay Calls** | Hides IP address              | Low        |
| **Force LTE Only**     | Prevents 2G downgrade attacks | Medium     |
| **Faraday Bag**        | Blocks all tracking           | Medium     |
| **Leave Phone Home**   | 100% Anonymity                | High       |

---

**References:**

- _Electronic Frontier Foundation (EFF) - Cell-Site Simulators_
- _The Intercept / Citizen Lab - Reports on SIAM and Iranian Mobile Surveillance_
- _Certfa - Signal Configuration Guides_
