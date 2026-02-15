---
title: "Device Integrity Verification Tools"
tags: [device-security, mobile-security, spyware-detection, forensics, integrity-verification]
category: "Device Security"
difficulty: "Advanced"
audience: [Security Professionals, Activists, Journalists, Privacy-Conscious Users]
topics: ["Mobile Security", "Spyware Detection", "Device Forensics", "Integrity Verification"]
summary: "Guide to tools for verifying mobile device integrity and detecting spyware like Pegasus, Predator, or KingsPawn."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of mobile operating systems", "Command-line familiarity (for MVT)"]
estimated_read_time: "10 minutes"
---

# Device Integrity Verification Tools

These tools validate the integrity of mobile devices and check for indicators of compromise by spyware and malware such as Pegasus, Predator, or KingsPawn.

> [!warning] Advanced Topic
> These tools provide functionality most people don't need and often require in-depth technical knowledge to use effectively.

> [!danger] Critical Limitation
> Scanning your device for public indicators of compromise is **not sufficient** to determine that a device is "clean." These publicly-available scanning tools can miss recent security developments and may give you a false sense of security.

## General Advice

Most system-level exploits on modern mobile devices—especially zero-click compromises—are **non-persistent**, meaning they won't remain or run automatically after a reboot.

**Recommendations:**
- Reboot your device at least once per week
- If non-persistent malware is a particular concern, reboot daily
- Understand that rebooting doesn't protect against persistent malware (though this is less common on mobile devices due to secure/verified boot)

## If You Suspect Compromise

### Who to Contact

| Situation | Contact |
|-----------|---------|
| Human rights defender, journalist, or civil society organization | [Amnesty International's Security Lab](https://securitylab.amnesty.org/contact-us) |
| Business or government device | Your enterprise/agency security liaison |
| Other situations | Local law enforcement |

### Immediate Actions to Consider

1. **Replace the device completely**
2. **Change your SIM/eSIM number**
3. **Do not restore from backup** (backups may be compromised)

### Understanding Tool Limitations

Indicators of compromise published by threat research organizations are not comprehensive—many indicators remain private. These tools can present **false negatives** if your device is infected with spyware not detected by public indicators. Reliable forensic support requires access to non-public indicators and threat intelligence.

## External Verification Tools

External verification tools run on your computer and scan your mobile device for forensic traces.

> [!danger] Important
> Public indicators of compromise are insufficient to determine that a device is "clean." Reliable forensic support requires access to non-public indicators, research, and threat intelligence.
>
> Civil society support is available through:
> - [Amnesty International's Security Lab](https://amnesty.org/en/tech)
> - [Access Now's Digital Security Helpline](https://accessnow.org/help)

> [!note] False Positives
> These tools can trigger false positives. If indicators of compromise are found, investigate further to determine actual risk. Some reports may be based on websites visited in the past, and old findings may indicate previous (no longer active) compromise.

### Mobile Verification Toolkit (MVT)

**Mobile Verification Toolkit (MVT)** is a collection of utilities that simplifies scanning mobile devices for traces of known spyware campaigns. Developed by Amnesty International and released in 2021 during the Pegasus Project.

- **Homepage:** [mvt.re](https://mvt.re/)
- **Source Code:** [GitHub](https://github.com/mvt-project/mvt)
- **Platforms:** macOS, Linux

#### Platform Considerations

| Platform | Effectiveness | Notes |
|----------|---------------|-------|
| iOS | More effective | Encrypted iTunes backups provide substantial files for detecting suspicious artifacts |
| Android | Limited | Stores minimal diagnostic information useful for triage |

#### Best Practices for iOS Users

1. **Create regular iTunes backups** (monthly minimum) to enable future forensic analysis if new threats are discovered
2. **Trigger and backup sysdiagnose logs** regularly for potential forensic investigators
   - On newer phones: Hold *Power* + *Volume Up* + *Volume Down* until you feel a brief vibration
   - Logs appear in: **Settings** > **Privacy & Security** > **Analytics & Improvements** > **Analytics Data**
3. **Enable [Lockdown Mode](https://blog.privacyguides.org/2022/10/27/macos-ventura-privacy-security-updates/#lockdown-mode)**

> [!warning] Jailbreaking Warning
> MVT allows deeper scans on jailbroken devices, but **do not jailbreak or root your device** unless you know exactly what you're doing. Jailbreaking exposes your device to considerable security risks.

### iMazing (iOS)

**iMazing** provides a free spyware analyzer tool for iOS devices that acts as a GUI wrapper for MVT, making it more accessible for non-technical users.

- **Homepage:** [imazing.com](https://imazing.com/)
- **Documentation:** [Spyware Analyzer](https://imazing.com/spyware-analyzer)
- **Platforms:** Windows, macOS

iMazing automates and guides you through using MVT to scan for publicly-accessible indicators of compromise. All MVT warnings and limitations apply equally to this tool.

## On-Device Verification

These apps check your device and operating system for signs of tampering and validate device identity.

> [!warning]
> Using these apps is insufficient to determine that a device is "clean" and not targeted with a particular spyware tool.

### Auditor (Android)

**Auditor** leverages hardware security features to provide device integrity monitoring by validating device identity and operating system integrity.

- **Homepage:** [attestation.app](https://attestation.app/)
- **Documentation:** [About](https://attestation.app/about)
- **Supported Devices:** GrapheneOS or stock OS on [supported devices](https://attestation.app/about#device-support)
- **Downloads:** Google Play, GitHub, GrapheneOS App Store

#### How Auditor Differs from Other Tools

Auditor is **not** a scanning/analysis tool. It uses your device's hardware-backed keystore to:
- Verify device identity
- Ensure the operating system hasn't been tampered with or downgraded via verified boot

This provides robust integrity checking of the device itself but doesn't check whether user-level apps are malicious.

#### How Auditor Works

Auditor requires **two devices**:
- **Auditee:** The device being verified (must be a [supported device](https://attestation.app/about#device-support))
- **Auditor:** The device performing verification (any Android 10+ device or GrapheneOS's remote web service)

**Process:**
1. A [Trust On First Use (TOFU)](https://en.wikipedia.org/wiki/Trust_on_first_use) model establishes a private key in the hardware-backed keystore
2. The auditor records the current state and configuration of the auditee
3. Any subsequent tampering with the auditee's operating system triggers an alert

#### Important Considerations

- Auditor can only detect changes **after** initial pairing, not during or before
- [Perform local attestation](https://grapheneos.org/install/web#verifying-installation) immediately after device installation, before any internet connection
- No personally identifiable information is submitted to the attestation service
- Sign up with an anonymous account and enable remote attestation for continuous monitoring
- If your threat model requires IP address privacy, use [Orbot](https://www.privacyguides.org/en/alternative-networks/#orbot) or a [VPN](https://www.privacyguides.org/en/vpn/)