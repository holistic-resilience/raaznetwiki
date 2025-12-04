# Enhanced Document

```yaml
---
title: "Device Integrity: Detecting Spyware and Malware on Mobile Devices"
tags: [device-security, spyware-detection, mobile-security, forensics, privacy-tools]
category: "Mobile Security"
difficulty: "Advanced"
audience: [Security Researchers, Privacy-Conscious Users, Journalists, Activists]
topics: ["Device Integrity", "Spyware Detection", "Mobile Forensics", "Digital Security"]
summary: "Guide to tools and techniques for validating mobile device integrity and detecting indicators of compromise from spyware like Pegasus."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of mobile operating systems", "Familiarity with command-line tools", "Understanding of threat modeling"]
estimated_read_time: "12 minutes"
---
```

# Device Integrity

These tools validate the integrity of mobile devices and check for indicators of compromise from spyware such as Pegasus, Predator, or KingsPawn. This guide focuses on **mobile security** because mobile devices typically have read-only systems with well-known configurations, making malicious modifications easier to detect than on desktop systems.

> **Note:** This is an advanced topic. These tools provide functionality most people don't need and often require in-depth technical knowledge to use effectively.

> **Critical Warning:** Scanning your device for public indicators of compromise is **not sufficient** to determine a device is "clean." These publicly-available tools can miss recent security developments and may provide a false sense of security.

## General Advice

Most system-level exploits on modern mobile devices—especially zero-click compromises—are **non-persistent**, meaning they don't remain active after a reboot. For this reason:

- **Minimum recommendation:** Reboot your device weekly
- **Higher-risk individuals:** Consider daily reboots

Rebooting means attackers must regularly re-infect your device to maintain access. However, rebooting won't protect against *persistent* malware, though this is less common on mobile devices due to secure/verified boot features.

## If You Suspect Compromise

### Who to Contact

| Situation | Contact |
|-----------|---------|
| Human rights defenders, journalists, civil society | [Amnesty International's Security Lab](https://securitylab.amnesty.org/contact-us) or [Access Now's Digital Security Helpline](https://accessnow.org/help) |
| Business or government devices | Your organization's security liaison |
| Personal devices | Local law enforcement (if appropriate) |

### Immediate Steps

1. Consider replacing the device completely
2. Consider changing your SIM/eSIM number
3. **Do not restore from backup**—the backup may be compromised

### Important Limitations

Indicators of compromise published by threat research organizations don't include all known indicators. These tools can present **false negatives** if your device is infected with spyware not detected by public indicators. Comprehensive forensic support requires access to non-public indicators and threat intelligence.

## External Verification Tools

External verification tools run on your computer and scan your mobile device for forensic traces that may indicate compromise.

> **Warning:** These tools can trigger false positives. If indicators of compromise are found, investigate further to determine actual risk. Findings that are years old likely indicate either false positives or previous (no longer active) compromise.

### Mobile Verification Toolkit (MVT)

**Mobile Verification Toolkit (MVT)** is a collection of utilities that automates scanning mobile devices for traces of known spyware campaigns. Developed by Amnesty International, it was released in 2021 during the Pegasus Project investigation.

- **Platforms:** macOS, Linux
- **Homepage:** [mvt.re](https://mvt.re/)
- **Source:** [GitHub](https://github.com/mvt-project/mvt)

**Key Points:**

- MVT is most useful for **iOS devices**—Android stores limited diagnostic information
- Encrypted iOS iTunes backups provide sufficient data to detect suspicious artifacts
- MVT is a command-line tool designed for technologists and forensic investigators

**Best Practices for iOS Users:**

1. Create regular (monthly) encrypted iTunes backups to enable future analysis
2. Trigger and externally backup *sysdiagnose* logs regularly (hold Power + Volume Up + Volume Down until vibration)
3. Enable [Lockdown Mode](https://support.apple.com/en-us/HT212650)

> **Warning:** Do not jailbreak or root your device unless you understand the security risks involved.

### iMazing (iOS)

**iMazing** provides a free spyware analyzer with a graphical interface that wraps MVT functionality, making it more accessible for non-technical users.

- **Platforms:** Windows, macOS
- **Homepage:** [imazing.com](https://imazing.com/)

All warnings and limitations that apply to MVT also apply to iMazing.

## On-Device Verification

These apps check your device and operating system for signs of tampering and validate device identity.

### Auditor (Android)

**Auditor** leverages hardware security features to provide device integrity monitoring. It validates device identity and operating system integrity using hardware-backed attestation.

- **Compatibility:** GrapheneOS or stock OS on [supported devices](https://attestation.app/about#device-support)
- **Homepage:** [attestation.app](https://attestation.app/)

**How Auditor Works:**

Auditor uses a Trust On First Use (TOFU) model with two devices:
- **Auditee:** The device being verified (must be a supported device)
- **Auditor:** The device performing verification (any Android 10+ device or GrapheneOS's remote service)

The process:
1. Devices establish a private key in the hardware-backed keystore
2. The auditor records the auditee's current state and configuration
3. Any subsequent tampering triggers an alert

**Important Considerations:**

- Auditor detects changes **after** initial pairing, not before
- Perform local attestation immediately after device installation, before connecting to the internet
- No personally identifiable information is submitted to the attestation service
- Sign up with an anonymous account for continuous remote attestation
- Consider using Orbot or a VPN if your threat model requires hiding your IP address

---

## Summary

| Tool | Platform | Best For | Skill Level |
|------|----------|----------|-------------|
| MVT | macOS/Linux | iOS forensic analysis | Advanced |
| iMazing | Windows/macOS | iOS analysis (GUI) | Intermediate |
| Auditor | Android | Device integrity verification | Intermediate |

Remember: No tool can guarantee your device is completely clean. These tools detect *known* indicators and should be part of a broader security strategy, not relied upon exclusively.