---
title: "Data Classification and Mapping"
tags:
  [
    data-privacy,
    risk-assessment,
    operational-security,
    digital-security,
    asset-management,
    iran-context,
  ]
category: "Data Management"
difficulty: "Beginner"
audience: [Activists, Journalists, General Public, NGO Workers]
topics:
  [
    "Data Inventory",
    "Risk Assessment",
    "Information Classification",
    "Threat Modeling",
  ]
summary: "A comprehensive guide for Iranian users to catalog, classify, and assess digital assets. Learn how to prioritize protection against state surveillance, physical seizure, and data loss."
source: "Raaznet Aggregated (Tactical Tech, Security in a Box, Privacy Guides)"
content_type: "Educational Guide"
security_level: "Foundational"
language: "English"
prerequisites: ["Basic understanding of file management"]
estimated_read_time: "10 minutes"
---

# Data Classification and Mapping

You cannot protect what you do not know you have. In the context of the Iranian digital landscape—where threats range from state-sponsored phishing and domestic traffic interception to physical device seizure at checkpoints—having a vague idea of your digital footprint is insufficient.

**Data Classification and Mapping** is the foundational process of creating an inventory of your digital life. It allows you to identify which files would put you at risk if discovered by the Islamic Republic's security apparatus and helps you decide where to allocate your strongest security measures.

## 1. The Three States of Information

To map your data effectively, you must understand the three states in which it exists. Each state has unique vulnerabilities in Iran.

| State              | Definition                                                                           | Iranian Threat Context                                                                                                                                 |
| :----------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data at Rest**   | Information stored on a device or server (e.g., hard drive, USB, cloud storage).     | **High Risk:** Confiscation of phones/laptops at protests or checkpoints; raids on homes/offices. Access to domestic cloud servers (e.g., ArvanCloud). |
| **Data in Motion** | Information travelling over a network (e.g., sending an email, browsing, messaging). | **High Risk:** Deep Packet Inspection (DPI) by the Telecommunication Infrastructure Company (TIC); interception of SMS/unencrypted HTTP.               |
| **Data in Use**    | Information currently being processed by RAM or viewed on a screen.                  | **Medium Risk:** Shoulder surfing in public; screen recording malware; screenshots taken by compromised apps.                                          |

---

## 2. Categorizing Your Information Assets

Before mapping _where_ data is, you must define _what_ it is. In a high-risk environment, data isn't just "work" or "personal"; it is categorized by the danger it poses.

### Types of Assets to Inventory

1.  **Communications:** Emails, chat logs (Telegram, WhatsApp, Signal), contact lists, SMS history.
2.  **Documents:** PDFs, Word docs, research notes, financial records, scans of ID cards (Kart-e Melli).
3.  **Media:** Photos and videos (especially of protests or gatherings), voice notes.
4.  **Credentials:** Passwords, seed phrases for crypto wallets, recovery codes, encryption keys.
5.  **Metadata:** Often overlooked. Location data embedded in photos, browser history, VPN connection logs, and "Last Seen" timestamps.

### Classification Levels

Adopt a classification system based on the potential impact of exposure.

- **🔴 Critical (High Risk):** Information that could lead to arrest, interrogation, harassment, or physical danger for you or others.
  - _Examples:_ Identities of fellow activists, details of safe houses, evidence of human rights violations, admin credentials for dissenting channels.
- **🟡 Private (Medium Risk):** Information that is personal and should be private, but may not lead to legal persecution.
  - _Examples:_ Personal family photos, financial data, health records, private chats about non-political topics.
- **🟢 Public/Low Risk:** Information already known or harmless.
  - _Examples:_ Public social media posts (that comply with local restrictions), generic educational materials.

---

## 3. The Mapping Process

You need to create a "Data Map" or "Asset Register." This is a living document (or mental model) that answers: **What do I have, where is it, and who holds the keys?**

> **Security Warning:** Do not create this map in a way that creates a roadmap for an interrogator. If you write this down, use a disguised file name inside an encrypted volume (e.g., Veracrypt) and delete it after memorizing the strategy.

### Step-by-Step Mapping

For every category of information (e.g., "Protest Photos"), ask the following questions:

#### A. Where is the Primary Copy?

The **Primary Copy** is the version you actively use or edit.

- _Locations:_ Smartphone gallery, Laptop "Documents" folder, Physical notebook, Domestic email provider (e.g., Chapaar - **Unsafe**), International provider (e.g., Gmail).

#### B. Where are the Copies/Backups?

Users often secure their phone but forget the automatic backup sitting on a cloud server.

- _Hidden Locations:_ iCloud/Google Drive auto-backups, Telegram "Saved Messages," unencrypted USB drives given to colleagues, sent items in email.

#### C. Who has Access?

- _Authorized:_ You, your colleagues, family.
- _Unauthorized but Capable:_
  - **Domestic Service Providers:** If you store data on Iranian platforms (Bale, Eitaa, Rubika, ArvanCloud), assume the government has full access.
  - **International Providers:** Google or Meta may comply with legal requests or have accounts compromised via SMS 2FA interception.
  - **Physical Adversaries:** Security forces at a detention center.

---

## 4. Creating Your Data Map (Template)

Use this structure to visualize your data sprawl.

| Asset Name         | Sensitivity | Primary Location         | Backup Location                 | Current Protection     | Action Required                                                          |
| :----------------- | :---------- | :----------------------- | :------------------------------ | :--------------------- | :----------------------------------------------------------------------- |
| **Signal Chats**   | 🔴 Critical | Phone (Internal Storage) | None (Disappearing messages on) | App Lock + Screen Lock | Verify "Registration Lock" is on.                                        |
| **Protest Videos** | 🔴 Critical | Phone Gallery            | Google Photos (Cloud)           | Phone Pattern Lock     | **DANGER:** Disable Google Photos sync. Move to Hidden/Encrypted folder. |
| **Project Plans**  | 🟡 Private  | Laptop Desktop           | USB Stick                       | Laptop Password        | Encrypt USB stick. Enable Full Disk Encryption.                          |
| **Contacts**       | 🔴 Critical | Phone Contacts           | SIM Card                        | None                   | Remove sensitive contacts from SIM. Use nicknames.                       |
| **Email Archive**  | 🟡 Private  | Gmail                    | None                            | Password + SMS 2FA     | **Upgrade:** Switch 2FA from SMS to Authenticator App.                   |

---

## 5. Analyzing the Gaps

Once mapped, analyze your vulnerabilities against specific local threats.

### Threat 1: The "Cloud" Trap

Many users believe deleting a file from their phone is enough. However, if you have mapped your data, you might realize:

- Your phone automatically syncs to a cloud.
- **Action:** Check sync settings on Google Photos, iCloud, and DropBox. Ensure sensitive photos are _only_ stored in encrypted containers (like Cryptomator) before being uploaded to any cloud.

### Threat 2: Domestic Hosting

Did your map reveal data stored on Iranian super-apps or email services?

- **Reality:** Iranian law requires domestic providers to store logs and content accessible to the judiciary/security forces.
- **Action:** Immediately migrate Critical (🔴) and Private (🟡) data away from domestic providers to secure, international, or self-hosted alternatives.

### Threat 3: Physical Seizure

If your map shows critical data on a "Laptop at Home" and a "USB Key in Pocket":

- **Reality:** A USB key in your pocket is highly vulnerable at a stop-and-search.
- **Action:** Do not carry critical data on portable media unless it is heavily encrypted (e.g., with VeraCrypt). Prefer storing data in a hidden, encrypted cloud volume rather than carrying physical evidence.

### Threat 4: Metadata Retention

Your map lists "Photos."

- **Reality:** Photos contain GPS coordinates and timestamp data (EXIF) that prove you were at a specific location at a specific time.
- **Action:** Use tools like _ObscuraCam_ or _Scrambled Exif_ to strip metadata before storage or sharing.

## 6. Minimization and Retention Policy

The most secure data is data that does not exist. Part of your classification strategy must be a **Deletion Policy**.

1.  **Review:** Look at your data map. Is there "Critical" data you no longer need?
2.  **Purge:** Securely delete files (using tools like _BleachBit_ or _Shred_) rather than just moving them to the Recycle Bin.
3.  **Automate:** Set Signal/Telegram messages to auto-delete (Disappearing Messages) for sensitive chats.

## Checklist: After Mapping

- [ ] I have identified all devices and accounts where my data lives.
- [ ] I have classified data based on the risk of arrest or harassment.
- [ ] I have located all "phantom" backups (cloud syncs, old USBs).
- [ ] I have removed all sensitive data from domestic (Iranian) platforms.
- [ ] I have established a schedule to re-evaluate this map (e.g., every 3 months).
