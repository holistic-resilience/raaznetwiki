---
title: "Information in Motion: Protecting Data During Transfer and Communication"
tags: [digital-security, privacy, metadata, data-protection, network-security, surveillance]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Activists, Privacy-Conscious Users, Security Practitioners]
topics: ["Data Transfer Security", "Metadata Awareness", "Network Privacy", "Digital Communications"]
summary: "Guide to understanding and protecting information as it moves through digital channels, including metadata risks and network vulnerabilities."
source: "Tactical Tech - Holistic Security"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of Information at Rest concepts"]
estimated_read_time: "6 minutes"
---

# Information in Motion

Information "in motion" refers to data actively being transferred or communicated rather than stored. This includes:

- **Transfer**: Moving offices, sharing email attachments, backing up files to external servers
- **Communications**: Phone calls, video calls, meetings, emails, and text messages

Understanding what information moves through these channels helps identify threats and develop appropriate protections. When cataloging information in motion, consider:

- How the information is transferred
- Its physical or virtual routes
- Who may access it along the way

## Key Characteristics of Digital Information

### Replication

Digital information is constantly replicated. Every time a file is saved, altered, or emailed, a copy is made. Recognizing this improves security planning—deleted files may exist in multiple locations.

### Metadata

Metadata is information created *about and by* the processes our devices carry out. It can be very difficult to distort or hide. Examples include:

| Type | Description | Can It Be Changed? |
|------|-------------|-------------------|
| **IP Addresses** | Your location when connecting to the internet, and addresses of sites you visit | Partially (via VPN/Tor) |
| **Mobile Location Data** | Phone movement between cell towers, SIM card ID, IMEI number | IMEI generally cannot be changed |
| **Email Headers** | Senders, recipients, timestamps, subjects, attachment indicators | Some can be obscured; servers require basic routing info |
| **Image Data** | Location where photo was taken, camera/lens brand, editing software | Can be stripped with image processing tools |
| **Document Properties** | Author, creation date, modification history | Can be removed via privacy settings or tools like Metadata Anonymization Toolkit |

> **Important**: Because we don't create metadata consciously and may not know it exists, it's often overlooked. Individual pieces may seem trivial, but collectively they reveal locations, networks, behavior patterns, and deviations from routines.

## The Path of Information Through Digital Channels

When information travels to the internet, it passes through multiple points where it can be monitored or intercepted:

```
Your Device → Local Network → ISP → Internet Infrastructure → Destination Service
```

### Potential Access Points

1. **Local Network (Router/LAN)**: Activities can be monitored at home, office, or public internet cafes

2. **Internet Service Providers**: Telecoms companies operating infrastructure can access data in transit

3. **State Entities**: Government surveillance at country "gateways" captures data and metadata

4. **Third Parties**: Advertising companies gather data about online activities

5. **Service Providers**: Email and social networking platforms may access, sell, or hand over data

## Mapping Your Information in Motion

Create a table to audit information you transfer or communicate:

| Information Type | Transfer Method | Route/Path | Who Can Access | Protection Needed |
|-----------------|-----------------|------------|----------------|-------------------|
| *Example: Client emails* | *Email* | *Device → ISP → Email provider → Recipient* | *ISP, email provider, state surveillance* | *End-to-end encryption* |

## Next Steps

After mapping both information in motion and information at rest, consider improvements to your security strategy:

- **Access policies**: Define who can access which information
- **Encryption**: Use tools for encrypting chats and emails
- **Secure deletion**: Implement software for securely removing data from devices
- **Metadata stripping**: Remove identifying information before sharing files

For practical implementation strategies, see [Security in-a-Box](https://securityinabox.org/en).

---

**Related Topics**: Information at Rest, Security Indicators