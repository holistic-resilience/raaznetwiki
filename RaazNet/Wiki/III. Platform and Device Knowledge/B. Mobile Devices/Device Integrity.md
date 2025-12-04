# Enhanced Document

```yaml
---
title: "Device Integrity: Detecting Mobile Spyware and Malware"
tags: [device-security, mobile-security, spyware-detection, forensics, privacy-tools, malware]
category: "Mobile Security"
difficulty: "Advanced"
audience: [Security Professionals, Journalists, Human Rights Defenders, Privacy-Conscious Users]
topics: ["Device Integrity", "Spyware Detection", "Mobile Forensics", "Digital Security"]
summary: "Guide to validating mobile device integrity and detecting indicators of compromise from spyware like Pegasus using tools such as MVT and Auditor."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Intermediate computer literacy", "Basic understanding of mobile operating systems", "Familiarity with command-line tools (for MVT)"]
estimated_read_time: "12 minutes"
---
```

# Device Integrity: Detecting Mobile Spyware and Malware

These tools validate the integrity of mobile devices and check for indicators of compromise from spyware such as Pegasus, Predator, or KingsPawn. This guide focuses on **mobile security** because mobile devices typically have read-only systems with well-known configurations, making malicious modifications easier to detect than on traditional desktop systems.

> **Note**: This is an advanced topic requiring in-depth technical knowledge. Most people do not need these tools for everyday use.

## Critical Limitations

Scanning your device for public indicators of compromise is **not sufficient** to determine that a device is "clean." These publicly-available scanning tools:
- May miss recent security developments
- Can provide a false sense of security
- Only detect known, published indicators
- Cannot guarantee absence of undiscovered spyware

## General Advice

### Regular Rebooting

Most system-level exploits on modern mobile devices—especially zero-click compromises—are **non-persistent**, meaning they don't survive a reboot.

**Recommendations:**
- **Minimum**: Reboot weekly
- **High-risk individuals**: Reboot daily

Rebooting forces attackers to re-infect your device to maintain access. However, it does not protect against persistent malware (which is less common due to secure/verified boot features).

### If You Suspect Compromise

**Seek professional help from:**
- **Human rights defenders/journalists**: [Amnesty International's Security Lab](https://securitylab.amnesty.org/contact-us)
- **Business/government devices**: Your organization's security liaison
- **General**: Local law enforcement

**Immediate actions to consider:**
- Replace the device completely
- Change your SIM/eSIM number
- Do not restore from backup (it may be compromised)

## External Verification Tools

External verification tools run on your computer and scan your mobile device for forensic traces helpful in identifying potential compromise.

> **Warning**: Public indicators alone are insufficient. Reliable forensic support requires access to non-public indicators and threat intelligence, available through [Amnesty International's Security Lab](https://amnesty.org/en/tech) or [Access Now's Digital Security Helpline](https://accessnow.org/help).

### Mobile Verification Toolkit (MVT)

**MVT** is a collection of utilities that automates scanning mobile devices for traces of known spyware campaigns. Developed by Amnesty International, it was released in 2021 during the Pegasus Project investigation.

**Platform support:** macOS, Linux

**Key characteristics:**
- More effective for **iOS** than Android (iOS stores more diagnostic data)
- Command-line tool designed for technologists and forensic investigators
- Requires technical expertise to use effectively

**Best practices for iOS users:**
1. Create monthly encrypted iTunes backups for retrospective analysis
2. Trigger and externally back up *sysdiagnose* logs regularly
   - On newer phones: Hold *Power* + *Volume Up* + *Volume Down* until vibration
   - Find logs in: **Settings** > **Privacy & Security** > **Analytics & Improvements** > **Analytics Data**
3. Enable [Lockdown Mode](https://support.apple.com/en-us/HT212650)

> **Warning**: Do not jailbreak or root your device for deeper scans unless you have expertise. Jailbreaking creates significant security vulnerabilities.

### iMazing (iOS)

**iMazing** provides a free spyware analyzer with a graphical interface that wraps MVT functionality, making it accessible to non-technical users.

**Platform support:** Windows, macOS

This tool automates MVT's scanning process with interactive guidance. All MVT limitations apply equally here.

## On-Device Verification

These apps check your device and operating system for signs of tampering and validate device identity.

### Auditor (Android)

**Auditor** leverages hardware security features for device integrity monitoring. It validates device identity and operating system integrity through hardware-backed attestation.

**Compatibility:** GrapheneOS or stock OS on [supported devices](https://attestation.app/about#device-support)

**How it differs from other tools:**
- Not a scanning/analysis tool
- Uses hardware-backed keystore for device verification
- Verifies the OS hasn't been tampered with via verified boot
- Does **not** check for malicious user-level apps

**How Auditor works:**
1. Uses Trust On First Use (TOFU) model between two devices
2. **Auditee**: The device being verified (must be supported)
3. **Auditor**: Any Android 10+ device or GrapheneOS remote service
4. Establishes private key in hardware-backed keystore
5. Records device state and configuration
6. Alerts you to any subsequent changes

**Important**: Auditor only detects changes **after** initial pairing. Perform local attestation immediately after device installation, before connecting to the internet.

**Privacy considerations:**
- No personally identifiable information submitted to attestation service
- Sign up with anonymous account for remote attestation
- Use Orbot or a VPN if your threat model requires hiding your IP address

---

## Summary

| Tool | Platform | Type | Best For |
|------|----------|------|----------|
| MVT | macOS/Linux | External scan | iOS forensic analysis |
| iMazing | Windows/macOS | External scan (GUI) | Non-technical iOS users |
| Auditor | Android | On-device | GrapheneOS integrity verification |

**Remember**: No tool can guarantee your device is completely clean. These tools detect known indicators but cannot identify novel or unpublished spyware. For high-risk individuals, professional forensic support is essential.