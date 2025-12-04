```yaml
---
title: "Dangerzone - Document Sanitization Tool"
tags: [document-security, malware-protection, pdf-sanitization, open-source, privacy-tools]
category: "Security Tools"
difficulty: "Beginner"
audience: [Journalists, Activists, Privacy-Conscious Users, General Public]
topics: ["Document Security", "Malware Protection", "Privacy Tools"]
summary: "Free, open-source tool that converts potentially dangerous documents to safe PDFs by sanitizing them in a secure sandbox."
source: "Freedom of the Press Foundation (FPF)"
content_type: "Tool Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Ability to install software"]
estimated_read_time: "3 minutes"
---
```

# Dangerzone

**Take potentially dangerous PDFs, office documents, or images and convert them to safe PDFs.**

Dangerzone is a free and open-source document sanitization tool maintained by [Freedom of the Press Foundation](https://freedom.press/) (FPF). It protects users from malware hidden in documents by converting files to safe PDFs through a secure sandboxing process.

- **Website:** [dangerzone.rocks](https://dangerzone.rocks/)
- **Source Code:** [GitHub Repository](https://github.com/freedomofpress/dangerzone)

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Malware Removal** | Destroys malware by rendering documents into pixels in a secure sandbox, then reconstructing them as clean PDFs |
| **Broad File Support** | Supports 20+ file types including PDFs, major office-suite formats, and common image types |
| **Network Isolation** | Documents are sanitized in a sandbox with no network access, preventing compromised documents from communicating externally |
| **Open Source** | Free software maintained by a nonprofit organization dedicated to press freedom |

---

## How It Works

1. **Isolation**: The document is opened inside a secure sandbox environment
2. **Conversion**: The document is converted to PDF format (if not already)
3. **Pixel Rendering**: Each page is rendered into raw pixel data
4. **Reconstruction**: The pixel data is converted back into a clean PDF

This process ensures that any malicious code embedded in the original document is destroyed during the pixel conversion step.

---

## Supported Platforms

| Platform | Installation |
|----------|--------------|
| **macOS** | Available for Intel and Apple Silicon chips |
| **Windows** | MSI installer available |
| **Ubuntu/Debian** | Package installation via repository |
| **Fedora** | Package installation via repository |
| **Tails** | Integrated installation guide available |
| **Qubes OS** | Beta support available |
| **Other Linux** | Build from source |

---

## Download

**Current Version:** 0.9.1

Download the appropriate version for your system from the [official downloads page](https://dangerzone.rocks/#downloads).

For security verification, see [How to verify PGP signatures](https://github.com/freedomofpress/dangerzone/blob/v0.9.1/INSTALL.md#verifying-pgp-signatures).

---

## Use Cases

- **Journalists**: Safely open documents from unknown sources
- **Activists**: Protect against targeted malware attacks via document attachments
- **Organizations**: Sanitize email attachments before opening
- **General Users**: Add a layer of protection when handling suspicious files

---

## Related Resources

- [About Dangerzone](https://dangerzone.rocks/about/)
- [Installation Guide](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md)
- [Freedom of the Press Foundation](https://freedom.press/)