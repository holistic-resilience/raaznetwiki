# Enhanced Document

```yaml
---
title: "Device Integrity: Mobile Security Verification Guide"
tags: [mobile-security, spyware-detection, device-verification, forensics, privacy-tools]
category: "Digital Security"
difficulty: "Advanced"
audience: [Security Professionals, Journalists, Activists, Privacy-Conscious Users]
topics: ["Mobile Security", "Spyware Detection", "Device Forensics", "Integrity Verification"]
summary: "Guide to verifying mobile device integrity and detecting spyware using tools like MVT, iMazing, and Auditor."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of mobile operating systems", "Command-line familiarity (for MVT)"]
estimated_read_time: "12 minutes"
---
```

# Device Integrity: Mobile Security Verification Guide

This guide covers tools and techniques for validating mobile device integrity and detecting indicators of compromise from spyware such as Pegasus, Predator, or KingsPawn.

## Important Limitations

> **Advanced Topic**: These tools require technical knowledge and are designed for individuals facing elevated security threats. Most users do not need these capabilities.

> **Critical Warning**: Scanning for public indicators of compromise is **not sufficient** to confirm a device is "clean." These tools can miss recent threats and may provide false security assurance.

## General Recommendations

### Regular Reboots

Most system-level mobile exploits—especially zero-click compromises—are **non-persistent** and do not survive a device reboot.

**Recommendations:**
- **Minimum**: Reboot weekly
- **Enhanced security**: Reboot daily

Rebooting forces attackers to re-infect your device to maintain access. However, it does not protect against persistent malware (which is less common on modern mobile devices due to secure/verified boot features).

## If You Suspect Compromise

### Seek Professional Help

Contact appropriate resources based on your situation:

| Situation | Contact |
|-----------|---------|
| Human rights defenders, journalists, civil society | [Amnesty International's Security Lab](https://securitylab.amnesty.org/contact-us) |
| Business or government devices | Your organization's security liaison |
| General compromise | Local law enforcement |

### Immediate Actions

1. **Consider replacing the device completely**
2. **Consider changing your SIM/eSIM number**
3. **Do not restore from backup**—backups may also be compromised

### Understanding Tool Limitations

These tools check against **publicly available** indicators of compromise. Not all indicators are public, meaning:
- Tools may show **false negatives** if infected with undetected spyware
- Comprehensive forensic analysis requires access to non-public threat intelligence

---

## External Verification Tools

These tools run on your computer and scan your mobile device for forensic traces.

### Mobile Verification Toolkit (MVT)

**Developer**: Amnesty International (released 2021, Pegasus Project context)

MVT is a command-line utility collection that automates scanning mobile devices for traces of known spyware campaigns.

**Platform Support:**
- macOS
- Linux

**Key Characteristics:**
- More effective for **iOS** than Android (iOS stores more diagnostic data)
- Android capabilities are limited due to minimal diagnostic information storage
- Requires technical expertise to operate

**iOS Best Practices with MVT:**

1. **Create monthly iTunes backups** — Enables retrospective analysis when new threats are discovered
2. **Trigger and backup sysdiagnose logs regularly** — Provides valuable forensic data
   - *Method*: Hold Power + Volume Up + Volume Down until brief vibration
   - *Location*: Settings > Privacy & Security > Analytics & Improvements > Analytics Data
3. **Enable Lockdown Mode** for enhanced protection

> **Warning**: Do not jailbreak your device for deeper scans unless you have expertise. Jailbreaking introduces significant security risks.

**Resources:**
- [Homepage](https://mvt.re/)
- [Source Code](https://github.com/mvt-project/mvt)

---

### iMazing (iOS)

**Purpose**: GUI wrapper for MVT, making spyware analysis accessible to non-technical users.

**Platform Support:**
- Windows
- macOS

**Key Features:**
- Free spyware analyzer tool
- Automates and guides users through MVT scanning process
- Interactive interface for iOS device analysis

> All MVT limitations apply to iMazing as well.

**Resources:**
- [Homepage](https://imazing.com/)
- [Documentation](https://imazing.com/spyware-analyzer)

---

## On-Device Verification Tools

Apps that check your device and operating system for tampering and validate device identity.

### Auditor (Android)

**Developer**: GrapheneOS

**Purpose**: Hardware-based device integrity monitoring through attestation.

**Compatibility:**
- GrapheneOS
- Stock OS on [supported devices](https://attestation.app/about#device-support)

**How It Differs from Scanning Tools:**

Auditor doesn't scan for malware. Instead, it:
- Verifies device identity using hardware-backed keystore
- Confirms operating system hasn't been tampered with or downgraded
- Provides robust integrity verification of the device itself

**How Auditor Works:**

Requires **two devices**:
- **Auditee**: Device being verified (must be supported)
- **Auditor**: Device performing verification (any Android 10+ or remote web service)

**Process:**
1. Establishes Trust On First Use (TOFU) relationship between devices
2. Creates private key in hardware-backed keystore
3. Records current device state and configuration
4. Alerts if tampering is detected after initial pairing

**Important Considerations:**

- TOFU model means Auditor only detects changes **after** initial pairing
- Perform local attestation immediately after device installation, before connecting to internet
- Consider using Orbot or VPN if your threat model requires IP address privacy from attestation service
- Anonymous account signup recommended for remote attestation

**Resources:**
- [Homepage](https://attestation.app/)
- [Documentation](https://attestation.app/about)
- [Source Code](https://attestation.app/source)

**Downloads:**
- Google Play
- GitHub
- GrapheneOS App Store

---

## Additional Resources

- [Amnesty International's Security Lab](https://amnesty.org/en/tech) — Civil society forensic support
- [Access Now's Digital Security Helpline](https://accessnow.org/help) — Digital security assistance
- [Privacy Guides Community](https://discuss.privacyguides.net/) — Discussion and support

---

## Summary

| Tool | Platform | Type | Best For |
|------|----------|------|----------|
| MVT | macOS/Linux | External scan | iOS forensic analysis |
| iMazing | Windows/macOS | External scan (GUI) | Non-technical iOS users |
| Auditor | Android | On-device verification | GrapheneOS integrity monitoring |

**Remember**: No tool can guarantee a device is completely clean. These tools check against known, public indicators only. For comprehensive forensic analysis, professional support with access to non-public threat intelligence is required.