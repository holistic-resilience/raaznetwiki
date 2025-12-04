---
title: "SecureDrop - Anonymous Whistleblower Submission System"
tags: [securedrop, whistleblowing, anonymity, tor, encryption, journalism, source-protection]
category: "Secure Communication"
difficulty: "Intermediate"
audience: [Whistleblowers, Journalists, Activists, Privacy-Conscious Users]
topics: ["Anonymous Communication", "Source Protection", "Secure Document Sharing"]
summary: "Overview of SecureDrop, an open-source whistleblower submission system enabling anonymous document sharing with news organizations via Tor."
source: "Freedom of the Press Foundation"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of Tor Browser", "Awareness of operational security concepts"]
estimated_read_time: "4 minutes"
---

# SecureDrop - Anonymous Whistleblower Submission System

SecureDrop is an open-source whistleblower submission system that news organizations and NGOs can install to securely accept documents from anonymous sources. It was originally designed by Aaron Swartz and Kevin Poulsen, and is now maintained by the Freedom of the Press Foundation.

## How to Use SecureDrop Anonymously

### Step 1: Prepare Your Environment

- **Use a safe location** — never use a work computer or your home network if you're concerned about surveillance
- **Download Tor Browser** from the official source: [https://www.torproject.org](https://www.torproject.org/)

### Step 2: Configure Tor Browser Security

1. Launch Tor Browser
2. Click the **shield icon** in the browser toolbar
3. Click **Advanced Security Settings**
4. Select **Safest** for maximum protection
5. Close the Preferences tab

### Step 3: Access SecureDrop

Navigate to the organization's SecureDrop `.onion` address using Tor Browser. You can find verified SecureDrop instances in the [official directory](https://securedrop.org/directory/).

## Participating News Organizations

SecureDrop is used by major news organizations worldwide, including:

| Organization | Description |
|--------------|-------------|
| **The Washington Post** | American daily newspaper (Washington, DC) |
| **The Guardian** | British daily newspaper |
| **Der Spiegel** | German media company |
| **The Globe and Mail** | Canadian newspaper |
| **Disclose** | French non-profit investigative media |
| **Greekleaks** | Greek investigative journalism network (Reporters United) |

View the complete directory at [securedrop.org/directory](https://securedrop.org/directory/)

## Key Security Features

### No Third-Party Access
The SecureDrop server is completely owned by and physically located within the news organization. No external parties can be secretly subpoenaed for access.

### Minimal Metadata Collection
SecureDrop does not log:
- IP addresses
- Browser information
- Computer identifiers

### End-to-End Encryption
All data is encrypted both in transit and at rest, protecting submissions from interception.

### Air-Gapped Architecture
The system is designed to operate in high-risk environments with security best practices enforced for journalists handling sensitive materials.

### Open Source
SecureDrop is licensed as free and open-source software, allowing independent security audits and community contributions.

## Resources

- **Latest Release**: [SecureDrop 2.12.10](https://github.com/freedomofpress/securedrop/releases/tag/2.12.10) (September 24, 2025)
- **Documentation**: [docs.securedrop.org](https://docs.securedrop.org/en/stable/)
- **Source Code**: [GitHub Repository](https://github.com/freedomofpress/securedrop)
- **SecureDrop Workstation**: Desktop application for journalists ([v1.5.0 released](https://securedrop.org/news/securedrop-workstation-1_5_0-released/))

## Learn More

For detailed information about SecureDrop's architecture and security model, visit the [official overview](https://securedrop.org/overview/).