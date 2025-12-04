```yaml
---
title: "SecureDrop - Anonymous Whistleblower Submission System"
tags: [securedrop, whistleblowing, anonymity, tor, encryption, journalism, open-source]
category: "Anonymous Communication"
difficulty: "Intermediate"
audience: [Whistleblowers, Journalists, Activists, Privacy-Conscious Users]
topics: ["Anonymous Submission", "Source Protection", "Secure Communication", "Investigative Journalism"]
summary: "Overview of SecureDrop, an open-source anonymous document submission system used by news organizations to securely receive tips from sources."
source: "SecureDrop.org - Freedom of the Press Foundation"
content_type: "Reference"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of Tor Browser", "Awareness of digital anonymity concepts"]
estimated_read_time: "4 minutes"
---
```

# SecureDrop - Anonymous Whistleblower Submission System

SecureDrop is an open-source whistleblower submission system that news organizations and NGOs can use to securely accept documents and communicate with anonymous sources.

## How to Submit Documents Anonymously

### Step 1: Prepare Your Environment
- Use a safe location—**never** a work computer or network
- Consider using a computer that cannot be traced back to you

### Step 2: Download and Install Tor Browser
1. Go to [https://www.torproject.org](https://www.torproject.org/)
2. Download and install the desktop version of Tor Browser
3. Launch Tor Browser

### Step 3: Configure Security Settings
1. Click the **shield icon** in the browser toolbar
2. Click **Advanced Security Settings**
3. Select **Safest** for maximum protection
4. Close the Preferences tab

### Step 4: Access SecureDrop
- Navigate to the SecureDrop directory and find your target organization
- Use the organization's `.onion` address to submit documents

## Key Security Features

| Feature | Description |
|---------|-------------|
| **No Third Parties** | Servers are completely owned by and located inside the news organization—no external hosting that could be subpoenaed |
| **Minimal Metadata** | Does not log IP addresses, browser information, or computer details |
| **End-to-End Encryption** | Data is encrypted in transit and at rest |
| **Air-Gapped Security** | Designed to protect against hackers and can be used in high-risk environments |
| **Open Source** | Licensed as free and open-source software for transparency and auditing |

## Organizations Using SecureDrop

SecureDrop is used by major news organizations worldwide, including:

- **The Washington Post** (United States)
- **The Guardian** (United Kingdom)
- **Der Spiegel** (Germany)
- **The Globe and Mail** (Canada)
- **Disclose** (France)
- **Greekleaks / Reporters United** (Greece)

A complete directory of SecureDrop instances is available at [securedrop.org/directory](https://securedrop.org/directory/).

## Technical Information

- **Current Version**: SecureDrop 2.12.10 (September 24, 2025)
- **Workstation Version**: SecureDrop Workstation 1.5.0
- **Documentation**: [docs.securedrop.org](https://docs.securedrop.org/en/stable/)
- **Source Code**: [GitHub - freedomofpress/securedrop](https://github.com/freedomofpress/securedrop)

## Related Resources

- [[Tor Browser]] - Required for anonymous access
- [[Digital Anonymity Best Practices]]
- [[Encryption Basics]]
- [[Whistleblower Protection]]