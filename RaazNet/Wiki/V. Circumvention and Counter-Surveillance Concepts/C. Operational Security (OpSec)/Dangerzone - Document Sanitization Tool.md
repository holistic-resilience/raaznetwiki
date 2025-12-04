---
title: "Dangerzone - Document Sanitization Tool"
tags: [document-security, malware-protection, pdf-sanitization, open-source-tools, privacy-tools]
category: "Security Tools"
difficulty: "Beginner"
audience: [Journalists, Activists, Privacy-Conscious Users, General Public]
topics: ["Document Security", "Malware Protection", "Digital Safety"]
summary: "Free, open-source tool that converts potentially dangerous documents into safe PDFs by sanitizing them in a secure sandbox."
source: "Freedom of the Press Foundation (FPF)"
content_type: "Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Ability to install software"]
estimated_read_time: "3 minutes"
---

# Dangerzone

**Dangerzone** is a free, open-source tool that converts potentially dangerous PDFs, office documents, or images into safe PDFs. It is developed and maintained by [Freedom of the Press Foundation](https://freedom.press/) (FPF).

- **Website:** [dangerzone.rocks](https://dangerzone.rocks/)
- **Current Version:** 0.9.1

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Malware Removal** | Destroys malware by rendering documents into pixels in a secure sandbox, then reconstructing them locally as a PDF |
| **Broad File Support** | Supports 20+ file types including PDFs, major office-suite formats, and common image types |
| **Network Isolation** | Documents are sanitized in a sandbox with no network access, preventing compromised documents from communicating externally |
| **Open Source** | Free software maintained by a nonprofit organization dedicated to press freedom |

---

## How It Works

1. **Isolation**: The document is opened inside a secure sandbox environment
2. **Conversion**: The document is converted to PDF format (if not already a PDF)
3. **Pixel Rendering**: Each page is rendered into raw pixel data
4. **Reconstruction**: The pixel data is converted back into a clean PDF

This process effectively strips any embedded malicious code, macros, or hidden content from the original document.

---

## Download & Installation

### Verification
Before installing, you can [verify PGP signatures](https://github.com/freedomofpress/dangerzone/blob/v0.9.1/INSTALL.md#verifying-pgp-signatures) to ensure download integrity.

### By Platform

| Platform | Installation |
|----------|--------------|
| **macOS (Intel)** | [Download DMG](https://github.com/freedomofpress/dangerzone/releases/download/v0.9.1/Dangerzone-0.9.1-i686.dmg) |
| **macOS (Apple Silicon)** | [Download DMG](https://github.com/freedomofpress/dangerzone/releases/download/v0.9.1/Dangerzone-0.9.1-arm64.dmg) |
| **Windows** | [Download MSI](https://github.com/freedomofpress/dangerzone/releases/download/v0.9.1/Dangerzone-0.9.1.msi) |
| **Ubuntu / Debian** | [Installation Guide](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md#ubuntu-debian) |
| **Fedora** | [Installation Guide](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md#fedora) |
| **Tails** | [Installation Guide](https://tails.net/doc/persistent_storage/additional_software/dangerzone/index.en.html) |
| **Other Linux** | [Build from Source](https://github.com/freedomofpress/dangerzone/blob/main/BUILD.md) |
| **Qubes OS** (Beta) | [Installation Guide](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md#qubes-os) |

> **Note for macOS users:** Not sure which chip you have? [Check here](https://support.apple.com/en-us/HT211814).

---

## Use Cases

Dangerzone is particularly useful when handling:

- Email attachments from unknown senders
- Documents downloaded from untrusted sources
- Files received through anonymous submission systems
- Any document where the source cannot be fully verified

---

## Additional Resources

- [Learn More About Dangerzone](https://dangerzone.rocks/about/)
- [GitHub Repository](https://github.com/freedomofpress/dangerzone)
- [Freedom of the Press Foundation](https://freedom.press/)