---
title: "Device Integrity Verification Tools"
tags: [security, privacy, mobile-security, malware-detection, forensics, spyware]
category: "Digital Security"
difficulty: "Advanced"
audience: [Privacy-Conscious Users, Activists, Journalists, Security Professionals]
topics: ["Mobile Security", "Device Verification", "Spyware Detection", "Digital Forensics"]
summary: "Guide to tools for validating mobile device integrity and detecting indicators of compromise from spyware like Pegasus."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of mobile operating systems", "Familiarity with command-line tools (for MVT)"]
estimated_read_time: "10 minutes"
---

# Device Integrity Verification Tools

These tools validate the integrity of mobile devices and check for indicators of compromise by spyware such as Pegasus, Predator, or KingsPawn. This guide focuses on **mobile security** because mobile devices typically have read-only systems with well-known configurations, making malicious modifications easier to detect than on traditional desktop systems.

> **Note:** These tools provide functionality most people don't need and often require in-depth technical knowledge to use effectively.

## Critical Limitations

Scanning your device for public indicators of compromise is **not sufficient** to determine that a device is "clean" or untargeted by spyware. These publicly-available scanning tools can miss recent security developments and provide a false sense of security.

### Why Public Tools Have Limitations

1. **Indicators lag behind threats** — Threat research organizations publish indicators of compromise, but not all indicators are made public
2. **False negatives are possible** — Your device may be infected with spyware not detected by public indicators
3. **Comprehensive analysis requires** access to non-public indicators, research, and threat intelligence

## General Protective Advice

Most system-level exploits on modern mobile devices—especially zero-click compromises—are **non-persistent**, meaning they don't remain or run automatically after a reboot.

**Recommendations:**
- Reboot your device at least **once weekly** (minimum)
- If non-persistent malware is a particular concern, consider **daily reboots**
- Understand that rebooting won't protect against persistent malware (though this is less common on mobile devices due to secure/verified boot)

## If You Suspect Compromise

### Who to Contact

| Situation | Contact |
|-----------|---------|
| Human rights defenders, journalists, civil society | [Amnesty International's Security Lab](https://securitylab.amnesty.org/contact-us) |
| Business or government devices | Your organization's security liaison |
| Personal devices | Local law enforcement (if appropriate) |

### Immediate Steps to Consider

- **Replace the device completely**
- **Change your SIM/eSIM number**
- **Do not restore from backup** — the backup may be compromised

---

## External Verification Tools

External verification tools run on your computer and scan your mobile device for forensic traces helpful in identifying potential compromise.

> **Warning:** Public indicators of compromise are insufficient to determine that a device is "clean." Reliable forensic support requires access to non-public indicators and threat intelligence.
>
> Civil society support is available through:
> - [Amnesty International's Security Lab](https://amnesty.org/en/tech)
> - [Access Now's Digital Security Helpline](https://accessnow.org/help)

### Mobile Verification Toolkit (MVT)

**Mobile Verification Toolkit (MVT)** is a collection of utilities that simplifies and automates scanning mobile devices for traces of known spyware campaigns. Developed by Amnesty International and released in 2021 during the [Pegasus Project](https://forbiddenstories.org/about-the-pegasus-project).

- **Platforms:** macOS, Linux
- **Homepage:** [mvt.re](https://mvt.re/)
- **Source Code:** [GitHub](https://github.com/mvt-project/mvt)

#### iOS vs Android Capabilities

| Platform | Effectiveness | Notes |
|----------|---------------|-------|
| **iOS** | More useful | Encrypted iTunes backups contain sufficient data for detecting suspicious artifacts |
| **Android** | Limited | Stores minimal diagnostic information useful for triage |

#### Best Practices for iOS Users

1. **Create monthly iTunes backups** — Enables detection of past infections when new threats are discovered
2. **Trigger sysdiagnose logs regularly** — Hold *Power + Volume Up + Volume Down* until you feel a brief vibration; find logs in **Settings > Privacy & Security > Analytics & Improvements > Analytics Data**
3. **Enable [Lockdown Mode](https://support.apple.com/en-us/HT212650)** — Provides additional protection against sophisticated attacks

> **Warning:** Do not jailbreak or root your device unless you understand the security implications. Jailbreaking exposes your device to considerable security risks.

### iMazing (iOS)

**iMazing** provides a free spyware analyzer tool for iOS devices, acting as a GUI wrapper for MVT. Much easier to use than MVT's command-line interface.

- **Platforms:** Windows, macOS
- **Homepage:** [imazing.com](https://imazing.com/)
- **Documentation:** [Spyware Analyzer](https://imazing.com/spyware-analyzer)

All MVT limitations and warnings apply to this tool as well.

---

## On-Device Verification

These apps check your device and operating system for signs of tampering and validate device identity.

> **Warning:** Using these apps is insufficient to determine that a device is "clean" or untargeted by spyware.

### Auditor (Android)

**Auditor** leverages hardware security features to provide device integrity monitoring by validating device identity and operating system integrity. Currently works only with **GrapheneOS** or stock operating systems on [supported devices](https://attestation.app/about#device-support).

- **Platform:** Android
- **Homepage:** [attestation.app](https://attestation.app/)
- **Source Code:** [attestation.app/source](https://attestation.app/source)

#### How Auditor Works

Auditor performs attestation and intrusion detection using **two devices**:
- **Auditee:** The device being verified (must be a [supported device](https://attestation.app/about#device-support))
- **Auditor:** The device performing verification (any Android 10+ device or GrapheneOS remote service)

**Process:**
1. Uses a [Trust On First Use (TOFU)](https://en.wikipedia.org/wiki/Trust_on_first_use) model to establish a private key in the hardware-backed keystore
2. The auditor records the current state and configuration of the auditee
3. Any tampering after pairing triggers an alert about device state changes

#### Important Considerations

- Auditor detects changes **after** initial pairing, not during or before
- [Perform local attestation](https://grapheneos.org/install/web#verifying-installation) immediately after device installation, before any internet connection
- Sign up with an anonymous account for remote attestation
- Consider using [Orbot](https://orbot.app/) or a VPN if your threat model requires hiding your IP from the attestation service

---

## Summary

| Tool | Platform | Type | Best For |
|------|----------|------|----------|
| MVT | macOS/Linux | External scan | iOS forensic analysis |
| iMazing | Windows/macOS | External scan (GUI) | Non-technical iOS users |
| Auditor | Android | On-device | GrapheneOS integrity verification |

**Remember:** No tool can definitively prove a device is clean. These tools are one component of a broader security strategy.