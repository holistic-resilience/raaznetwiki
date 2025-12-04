---
title: "SecureDrop - Anonymous Whistleblower Submission System"
tags: [whistleblowing, anonymity, tor, encryption, journalism, secure-communication]
category: "Secure Communication Tools"
difficulty: "Intermediate"
audience: [Whistleblowers, Journalists, Activists, Privacy-Conscious Users]
topics: ["Anonymous Communication", "Document Submission", "Source Protection"]
summary: "Overview of SecureDrop, an open-source whistleblower submission system that enables anonymous document sharing with news organizations via Tor."
source: "SecureDrop.org (Freedom of the Press Foundation)"
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

### Step 2: Configure Tor for Maximum Security

1. Launch Tor Browser
2. Click the **shield icon** in the browser toolbar
3. Click **Advanced Security Settings**
4. Select **Safest** and close the Preferences tab
5. Navigate to the SecureDrop instance of your chosen organization

### Step 3: Submit Your Documents

Access the SecureDrop directory to find participating news organizations and submit your documents through their secure portals.

## Participating Organizations

SecureDrop is used by major news organizations worldwide, including:

| Organization | Description |
|--------------|-------------|
| **The Washington Post** | American daily newspaper (Washington, DC) |
| **The Guardian** | British daily newspaper |
| **Der Spiegel** | German media company |
| **Disclose** | French non-profit investigative media |
| **Greekleaks** | Greek investigative journalism network |
| **The Globe and Mail** | Canadian newspaper |

View the complete directory at [securedrop.org/directory](https://securedrop.org/directory/)

## Key Security Features

### No Third Parties
The server is completely owned by and physically located inside the news organization. No external parties can be secretly subpoenaed for your information.

### Minimal Metadata Collection
SecureDrop does not log:
- IP addresses
- Browser information
- Computer identifiers

### End-to-End Encryption
All data is encrypted both in transit and at rest, protecting your submissions from interception.

### Air-Gapped Architecture
The system enforces security best practices for journalists and is designed for use in high-risk environments.

### Open Source
SecureDrop is licensed as free and open-source software, allowing independent security audits and transparency.

## Resources

- **Latest Release**: SecureDrop 2.12.10 (September 24, 2025)
- **Documentation**: [docs.securedrop.org](https://docs.securedrop.org/en/stable/)
- **Source Code**: [GitHub Repository](https://github.com/freedomofpress/securedrop/)
- **SecureDrop Workstation**: Desktop application for journalists (v1.5.0)

## Related Topics

- [[Tor Browser]]
- [[Anonymous Communication]]
- [[Whistleblower Protection]]
- [[Encryption Basics]]