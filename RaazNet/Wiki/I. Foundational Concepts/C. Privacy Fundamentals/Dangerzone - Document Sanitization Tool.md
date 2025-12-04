```yaml
---
title: "Dangerzone - Document Sanitization Tool"
tags: [security, privacy, malware-protection, document-safety, open-source, pdf-tools]
category: "Digital Security Tools"
difficulty: "Beginner"
audience: [General Public, Journalists, Activists, Privacy-Conscious Users]
topics: ["Document Security", "Malware Prevention", "File Sanitization"]
summary: "Free, open-source tool that converts potentially dangerous documents to safe PDFs by sanitizing them in an isolated sandbox."
source: "Freedom of the Press Foundation (FPF)"
content_type: "Tool Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Ability to install software"]
estimated_read_time: "3 minutes"
---
```

# Dangerzone

**Dangerzone** converts potentially dangerous PDFs, office documents, or images into safe PDFs by sanitizing them in an isolated environment.

> 🔗 **Official Website:** [dangerzone.rocks](https://dangerzone.rocks/)

## Key Features

| Feature | Description |
|---------|-------------|
| 🦠 **Malware Removal** | Destroys malware by rendering documents into pixels within a secure sandbox, then reconstructing them locally as clean PDFs |
| 📄 **Broad File Support** | Supports 20+ file types including PDFs, major office-suite formats, and common image types |
| 🔌 **Network Isolation** | Documents are sanitized in a sandbox with no network access—compromised documents cannot communicate externally |
| 🫴 **Free & Open Source** | Maintained by [Freedom of the Press Foundation](https://freedom.press/), a nonprofit defending press freedom |

## How It Works

1. A potentially untrusted document (e.g., email attachment) is loaded into Dangerzone
2. Inside an isolated sandbox, the document is converted to PDF format (if not already)
3. Each page is rendered into raw pixel data
4. The pixel data is reconstructed into a clean, safe PDF

This process eliminates any embedded malicious code, scripts, or exploits that may have been present in the original file.

## Supported Platforms

| Platform | Installation |
|----------|--------------|
| **macOS** | Available for Intel and Apple Silicon chips |
| **Windows** | MSI installer available |
| **Ubuntu/Debian** | Package installation via repository |
| **Fedora** | Package installation via repository |
| **Tails** | Integrated installation support |
| **Qubes OS** | Beta support available |
| **Other Linux** | Build from source |

## Download & Verification

- **Current Version:** 0.9.1
- **Download:** [Official Downloads Page](https://dangerzone.rocks/#downloads)
- **Verify Signatures:** [PGP Verification Guide](https://github.com/freedomofpress/dangerzone/blob/v0.9.1/INSTALL.md#verifying-pgp-signatures)

## Additional Resources

- [About Dangerzone](https://dangerzone.rocks/about/) — Detailed technical explanation
- [GitHub Repository](https://github.com/freedomofpress/dangerzone) — Source code and issue tracking
- [Installation Instructions](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md) — Platform-specific setup guides