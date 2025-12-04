---
title: "Information in Motion: Understanding Data Transfer and Communication Security"
tags: [data-security, metadata, digital-communications, network-security, privacy]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Activists, Privacy-Conscious Users, Security Practitioners]
topics: ["Data Protection", "Metadata Awareness", "Network Security"]
summary: "Guide to understanding security risks when information is transferred or communicated digitally, including metadata exposure and network interception points."
source: "Tactical Tech - Holistic Security"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of Information at Rest concepts"]
estimated_read_time: "6 minutes"
---

# Information in Motion

Information "in motion" refers to data as it moves between locations or people. This occurs in two primary ways:

- **Transfer**: Moving files between locations—such as relocating offices, sharing email attachments, or backing up sensitive files to another server
- **Communications**: Real-time exchanges—phone calls, video conferences, meetings, emails, and text messages

To protect information in motion, you must first identify what you share, understand the threats to that information, and then implement appropriate safeguards. When cataloguing this information, consider:

- How the information is transferred
- Its physical or virtual routes
- Who may be able to access it along the way

## Key Characteristics of Digital Information

### Replication

Digital information is constantly replicated. Every time a file is saved, altered, or emailed, a copy is made. Understanding this fundamental characteristic is essential for developing an effective security strategy.

### Metadata

Metadata is information created *about and by* the processes our computers and phones carry out. It can be very difficult to distort or hide. Examples include:

| Type | Description | Can It Be Changed? |
|------|-------------|-------------------|
| **IP Addresses** | Your location when connecting to the internet, plus IP addresses of sites you visit | Partially (via VPN/Tor) |
| **Mobile Phone Data** | Location data, SIM card identifiers, and device IMEI number | Generally no—IMEI is permanent |
| **Email Headers** | Senders, recipients, timestamps, subjects, and attachment indicators | Partially—some can be obscured, but servers require basic routing information |
| **Image Data** | Location where photo was taken, file size, camera/lens brand, editing software used | Yes—using image processing or metadata stripping software |
| **Document Properties** | Author information, creation and modification dates | Yes—via privacy settings or tools like the Metadata Anonymization Toolkit |

> **Important**: Because we don't consciously create metadata and may not know it exists, it's often overlooked. Individual pieces may seem trivial, but collectively metadata can reveal locations you frequently visit, your network of contacts, your behaviour patterns, and when you deviate from them.

## The Journey of Digital Information

When information travels through digital channels, it passes through multiple points where it can potentially be monitored or intercepted:

1. **Local Network**: Your router and local area network (LAN)—whether at office, home, or internet café—where activities can be monitored
2. **Internet Service Providers**: ISPs and telecoms companies that operate infrastructure and transfer your data
3. **State Surveillance**: Government entities that capture and monitor data at country "gateways" and other infrastructure points
4. **Third-Party Trackers**: Advertising companies and data brokers gathering information about online activities
5. **Service Providers**: Email, social networking, and cloud service providers who may access, sell, or hand over your data

## Mapping Your Information in Motion

Create an inventory of your information in motion by documenting:

- What information is being transferred or communicated
- The method of transfer (email, messaging app, file sharing, etc.)
- The route it takes (which networks and services it passes through)
- Who could potentially access it at each point
- What protections are currently in place

## Improving Your Security Strategy

After mapping both your information in motion and [[Information at Rest|information at rest]], consider implementing:

- **Access policies**: Define who can access which information
- **Encryption**: Use tools that encrypt chats, emails, and file transfers
- **Secure deletion**: Employ software for securely removing data from devices
- **Metadata removal**: Strip identifying metadata before sharing files

---

## Further Resources

For practical strategies and hands-on tips for securing your digital information, visit [Security in-a-Box](https://securityinabox.org/en).