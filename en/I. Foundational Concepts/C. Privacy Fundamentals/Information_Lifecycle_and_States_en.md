---
title: "Information Lifecycle and States"
tags:
  [
    information-security,
    data-protection,
    data-lifecycle,
    encryption,
    risk-assessment,
    digital-privacy,
    iran-security,
  ]
category: "Foundational Concepts"
difficulty: "Intermediate"
audience: [Activists, Journalists, Human Rights Defenders, General Public]
topics:
  [
    "Data States",
    "Information Management",
    "Digital Security",
    "Threat Modeling",
  ]
summary: "A comprehensive guide to understanding the three states of information (At Rest, In Motion, In Use) and the data lifecycle. Includes strategies for mapping, classifying, and protecting assets against surveillance and seizure in the Iranian context."
source: "Raaznet Aggregation (Tactical Tech, Privacy Guides, Security in a Box)"
content_type: "Educational Guide"
security_level: "Foundational"
language: "English"
prerequisites:
  ["Basic digital literacy", "Understanding of encryption concepts"]
estimated_read_time: "10 minutes"
---

# Information Lifecycle and States

To build a robust digital security strategy, you must first understand the nature of the information you are trying to protect. Information is not static; it moves, changes form, and exists in different environments. In the context of Iran, where threats range from physical device seizure by security forces to deep packet inspection (DPI) of network traffic, understanding where your data lives and how it travels is critical.

This guide defines the three primary states of information, outlines the information lifecycle, and provides a framework for mapping and classifying your digital assets to apply appropriate protection measures.

---

## The Three States of Information

Information security controls are designed to protect data in three distinct states. Vulnerabilities and attack vectors differ depending on which state the data is currently in.

### 1. Information at Rest

**Definition:** Information that is physically stored on a medium and is not currently being accessed or transmitted.

- **Examples:** Files on a laptop hard drive, photos on a smartphone gallery, backups on a USB stick, documents in a filing cabinet, or emails stored on a provider’s server (e.g., Gmail servers).
- **Primary Risks in Iran:**
  - **Physical Seizure:** Confiscation of laptops or phones during arrests, home raids, or border crossings.
  - **Theft:** Stolen devices containing sensitive data.
  - **Server Compromise:** Unencrypted data stored on servers (especially domestic Iranian servers) can be accessed by authorities via court order or coercion.
- **Key Defense:** **Full Disk Encryption (FDE)** and strong, unique passphrases. If the device is seized, the data remains unreadable without the key.

### 2. Information in Motion (Transit)

**Definition:** Information that is moving from one location to another via a network.

- **Examples:** Sending an email, sending a message on Telegram or Signal, browsing a website, or uploading files to the cloud.
- **Primary Risks in Iran:**
  - **Interception:** The Telecommunication Infrastructure Company (TIC) and other entities monitor internet traffic. Unencrypted traffic (HTTP, SMS) is easily read.
  - **Metadata Analysis:** Even if the content is encrypted, traffic patterns and metadata (who you are talking to and when) can be analyzed.
- **Key Defense:** **End-to-End Encryption (E2EE)** (e.g., Signal) and tunneling protocols like **VPNs** or **Tor** to wrap traffic in an encrypted tunnel, protecting it from local ISP surveillance.

### 3. Information in Use

**Definition:** Information currently actively being processed by a computer system, residing in the Random Access Memory (RAM), CPU caches, or being displayed on a screen.

- **Examples:** A document open in Microsoft Word, an unencrypted database being queried, or a message currently visible on your phone screen.
- **Primary Risks in Iran:**
  - **Endpoint Compromise:** Malware (like spyware or keyloggers) can capture data before it is encrypted for storage or transmission.
  - **Shoulder Surfing:** Surveillance cameras or individuals observing your screen in public spaces (cafes, protests).
- **Key Defense:** Endpoint security (antivirus, updates), operational security (awareness of surroundings), and using trusted, clean devices.

---

## The Information Lifecycle

Data does not just appear; it follows a lifecycle from creation to destruction. Security must be applied at every stage.

1.  **Creation/Collection:**
    - The moment data is generated (e.g., typing a document, taking a photo, recording a voice note).
    - _Risk:_ Metadata (location, device ID) is often embedded automatically upon creation.

2.  **Storage:**
    - The data is saved to a medium (Information at Rest).
    - _Decision:_ Is this stored locally or in the cloud? Is it encrypted?

3.  **Usage:**
    - The data is accessed, modified, or processed (Information in Use).
    - _Decision:_ Who has access to modify this data?

4.  **Sharing/Transmission:**
    - The data is moved to another user or system (Information in Motion).
    - _Decision:_ What channel is used? Is it secure against interception?

5.  **Archival:**
    - Data is moved to long-term storage.
    - _Risk:_ "Forgotten" data often lacks current security patches or oversight. Old backups are a common target for investigators.

6.  **Destruction:**
    - The data is permanently removed.
    - _Risk:_ Simply "deleting" a file usually only removes the reference to it, not the actual data. Forensic tools can recover "deleted" files. Secure deletion (shredding/wiping) is required.

---

## Mapping Your Information Ecosystem

To protect your information, you must first know it exists. An **Information Map** is an inventory of your digital and physical assets.

Create a spreadsheet or document with the following columns for every category of information you handle (e.g., Financial Records, Contact Lists, Protest Planning Docs):

| Asset Category                   | State       | Location             | Access      | Sensitivity     | Protection                                       |
| :------------------------------- | :---------- | :------------------- | :---------- | :-------------- | :----------------------------------------------- |
| _Example: Activist Contact List_ | _At Rest_   | _Signal App (Phone)_ | _Only Me_   | _High (Secret)_ | _Signal PIN, Screen Lock, Disappearing Messages_ |
| _Example: Grant Proposal_        | _In Motion_ | _Email Attachment_   | _NGO Staff_ | _Confidential_  | _PGP Encryption, Proton Mail_                    |

### Key Mapping Questions

1.  **What information is it?** (Group similar types: financial, personal, operational).
2.  **Where does it reside?** (Physical location, device, cloud service, third-party platform).
3.  **Who has access?** (Colleagues, family, service providers, admins).
4.  **How sensitive is it?** (See classification below).

---

## Data Classification

Not all data requires the same level of protection. Classifying data helps prioritize your limited resources.

- **Secret (High Risk):** Information that, if disclosed, could result in arrest, physical harm, or severe repression.
  - _Examples:_ Identities of protesters, unreleased investigative reports, passwords, private keys.
  - _Requirement:_ Strong encryption, strict access control, offline storage where possible.
- **Confidential (Medium Risk):** Information that is private but strictly internal. Disclosure would cause reputational damage or administrative issues.
  - _Examples:_ Internal meeting notes, financial drafts, non-sensitive personal emails.
  - _Requirement:_ Standard encryption, access limited to team members.
- **Public (Low Risk):** Information intended for public consumption.
  - _Examples:_ Published articles, public statements, educational materials.
  - _Requirement:_ Integrity checks (ensuring it hasn't been altered), but confidentiality is not required.

---

## Security Strategies for the Iranian Context

### 1. Protecting Data at Rest

- **Encryption is Mandatory:** Use Full Disk Encryption (BitLocker for Windows, FileVault for macOS, LUKS for Linux, and standard encryption on Android/iOS).
- **Hidden Volumes:** For high-risk data, use tools like **VeraCrypt** to create hidden encrypted containers. If forced to reveal a password, you can reveal a "decoy" partition while the sensitive data remains hidden.
- **Travel Clean:** When crossing borders or attending protests, carry devices with minimal data. Use a secondary "burner" phone if possible.

### 2. Protecting Data in Motion

- **Assume Monitoring:** Assume all SMS and regular phone calls are monitored by Iranian telecommunication providers.
- **Use Signal:** Signal is the gold standard for text and voice communication. It minimizes metadata and encrypts content end-to-end.
- **Tor and VPNs:** Never access sensitive websites (HTTP) without a VPN or Tor. This prevents the ISP from seeing which specific pages you are visiting. Ensure your VPN is trusted and uses obfuscation to bypass censorship.

### 3. Protecting Data in Use

- **Environment Awareness:** Be aware of CCTV cameras in cafes or public spaces that could record your screen or keyboard input.
- **Malware Hygiene:** Iranian threat actors often use "social engineering" (fake apps, phishing emails) to install spyware. Never open unexpected attachments.
- **Disconnect:** For extremely sensitive tasks (e.g., decrypting a whistleblower submission), use an "air-gapped" machine—a computer that is physically verified and never connected to the internet.

### 4. Lifecycle Management

- **Data Minimization:** "If you don't have it, they can't seize it." Regularly delete chats and files you no longer need.
- **Secure Deletion:** When selling or discarding a device, ensure it is wiped. On magnetic hard drives, use tools to overwrite data. On SSDs and phones, ensure encryption was enabled before the factory reset, which renders the data unrecoverable.

---

## Related Topics

- **[[Core_Concepts_Privacy_vs_Security|Privacy vs. Security]]**
- **[[Digital_Footprint_and_Metadata|Digital Footprint and Metadata]]**
- **[[Information_at_Rest|Protecting Information at Rest]]**
- **[[Secure_Communication_Guide|Secure Communication]]**
