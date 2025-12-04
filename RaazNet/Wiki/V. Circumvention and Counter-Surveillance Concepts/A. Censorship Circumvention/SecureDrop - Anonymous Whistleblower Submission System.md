---
title: "SecureDrop - Anonymous Whistleblower Submission System"
tags: [securedrop, whistleblowing, anonymity, tor, encryption, journalism, open-source]
category: "Secure Communication"
difficulty: "Intermediate"
audience: [Whistleblowers, Journalists, Privacy-Conscious Users, Activists]
topics: ["Anonymous Submission", "Source Protection", "Secure Communication"]
summary: "Overview of SecureDrop, an open-source whistleblower submission system that enables anonymous document sharing with news organizations via Tor."
source: "Freedom of the Press Foundation"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of Tor Browser", "Familiarity with encryption concepts"]
estimated_read_time: "4 minutes"
---

# SecureDrop - Anonymous Whistleblower Submission System

SecureDrop is an open-source whistleblower submission system that news organizations and NGOs can install to securely accept documents from anonymous sources. It was originally designed by Aaron Swartz and Kevin Poulsen, and is now maintained by the Freedom of the Press Foundation.

## How to Submit Documents Anonymously

### Step 1: Prepare Your Environment

- **Use a safe location** — never use a work computer or network
- **Download Tor Browser** from [https://www.torproject.org](https://www.torproject.org/)

### Step 2: Configure Tor Browser Security

1. Click the **shield icon** in the browser toolbar
2. Click **Advanced Security Settings**
3. Select **Safest** for maximum protection
4. Close the Preferences tab

### Step 3: Access SecureDrop

Launch Tor Browser and navigate to the SecureDrop instance of your chosen news organization. You are now browsing anonymously.

## Participating News Organizations

SecureDrop is used by major news organizations worldwide, including:

| Organization | Description |
|--------------|-------------|
| **The Washington Post** | American daily newspaper (Washington, DC) |
| **The Guardian** | British daily newspaper |
| **Der Spiegel** | German media company |
| **The Globe and Mail** | Canadian newspaper |
| **Disclose** | French non-profit investigative media |
| **Greekleaks** | Greek investigative journalism network |

A complete directory of SecureDrop instances is available at [securedrop.org/directory](https://securedrop.org/directory/).

## Key Security Features

### No Third-Party Access
Servers are completely owned by and physically located inside the news organization. No external parties can be secretly subpoenaed for your data.

### Minimal Metadata Collection
SecureDrop does not log:
- IP addresses
- Browser information
- Computer identifiers

### End-to-End Encryption
All data is encrypted both in transit and at rest, protecting your submissions from interception.

### Air-Gapped Security
The system enforces security best practices for journalists and is designed for use in high-risk environments.

### Open Source
SecureDrop is licensed as free and open-source software, allowing independent security audits and transparency.

## Resources

- **Latest Release**: [SecureDrop 2.12.10](https://github.com/freedomofpress/securedrop/releases/tag/2.12.10) (September 24, 2025)
- **Documentation**: [docs.securedrop.org](https://docs.securedrop.org/en/stable/)
- **Source Code**: [GitHub Repository](https://github.com/freedomofpress/securedrop)
- **SecureDrop Workstation**: Desktop application for journalists ([Version 1.5.0](https://securedrop.org/news/securedrop-workstation-1_5_0-released/))

## Learn More

For comprehensive information about SecureDrop's security architecture and implementation, visit [securedrop.org/overview](https://securedrop.org/overview/).