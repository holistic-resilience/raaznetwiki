```yaml
---
title: "Back Up and Recover from Information Loss"
tags: [backup, data-recovery, digital-security, encryption, cloud-storage]
category: "Data Protection"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Data Backup", "Information Recovery", "Digital Security", "Cloud Storage"]
summary: "Comprehensive guide on creating backup strategies, recovering lost data, and protecting information across devices and platforms."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file management"]
estimated_read_time: "12 minutes"
---
```

# Back Up and Recover from Information Loss

Data loss can happen through device failure, theft, confiscation, or accidental deletion. A solid backup strategy ensures you can recover your important information when disaster strikes. This guide covers recovery tools, backup planning, and implementation across different platforms.

## Table of Contents

- [[#Recover Deleted or Lost Information]]
- [[#Create a Backup Plan]]
- [[#Back Up Computer Files to a Local Device]]
- [[#Back Up Your Phone to a Local Device]]
- [[#Cloud Backup Considerations]]
- [[#Back Up Your Email]]
- [[#Scan and Back Up Printed Documents]]
- [[#Set a Backup Schedule]]
- [[#Practice Recovery]]
- [[#Establish Procedures for Coworkers]]
- [[#Other Considerations]]

---

## Recover Deleted or Lost Information

If you've lost data, start troubleshooting with the [Digital First Aid Kit's guide on lost data](https://digitalfirstaid.org/topics/lost-data/).

> [!warning] Act Quickly
> Recovery tools don't work if your device has written new data over deleted files. Stop using your device until you attempt recovery—the longer you wait, the less likely retrieval becomes.

### Recovery Tools

**Cross-Platform (Linux, macOS, Windows)**
- [TestDisk & PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec) — See the [official guide](https://www.cgsecurity.org/testdisk.pdf) for instructions

**Windows Only**
- [Recuva](https://www.ccleaner.com/recuva/) — See [their usage guide](https://www.ccleaner.com/knowledge/recuva-tip-search-for-files)

> [!info] Why This Works
> When you delete a file, it disappears from view but remains on your device until overwritten. Even emptying the Recycle Bin doesn't immediately destroy data. While this poses [security risks](https://securityinabox.org/en/files/destroy-sensitive-information), it also means accidental deletions can often be reversed.

---

## Create a Backup Plan

### Organize Your Information

Before creating a backup plan, consolidate files you intend to back up into a single location, such as the "Documents" folder.

### Map Your Information

Identify where your personal and work information currently exists:

- **Email** — May be on provider servers, your computer, or both
- **Multiple accounts** — Consider all email, social media, and service accounts
- **Removable media** — USB drives, portable hard drives, SD cards
- **Websites** — Content you've built over time
- **Non-digital** — Paper notebooks, diaries, letters

For detailed guidance, see the [Holistic Security manual on cataloguing information](https://holistic-security.tacticaltech.org/chapters/explore/2-4-understanding-and-cataloguing-our-information.html).

### Distinguish Primary Copies from Duplicates

The **primary copy** is the most up-to-date version—the one you would edit. Identify which copies are primary to ensure you're backing up current information, not outdated duplicates.

> [!example] Common Disaster Scenario
> You travel for a week, updating a spreadsheet on a USB stick. That USB copy becomes your primary—if lost before syncing, your office "backup" is actually outdated.

### Document Your Data Locations

Create a table mapping all your information:

| Data Type | Primary/Duplicate | Storage Device | Location |
|-----------|-------------------|----------------|----------|
| Research files | Primary | Computer hard drive | Office |
| Testimonies | Duplicate | USB memory stick | With me |
| Program databases | Primary | Computer hard drive | Office |
| Email & contacts | Primary | Email account | Email server |
| Text messages & contacts | Primary | Mobile phone | With me |
| Printed documents | Primary | Desk drawer | Office |

**Vulnerabilities in this example:**
- Hard drive crash loses most primary data
- No offline email backup
- No phone data backup
- No copies of printed documents

**Improved backup structure:**

| Data Type | Primary/Duplicate | Storage Device | Location |
|-----------|-------------------|----------------|----------|
| Testimonies | Primary | Computer hard drive | Office |
| Testimonies | Duplicate | USB memory stick | Home |
| Research files | Primary | Computer hard drive | Office |
| Research files | Duplicate | USB memory stick | With me |
| Email & contacts | Primary | Email account | Email server |
| Email & contacts | Duplicate | Thunderbird | Office computer |
| Phone data | Primary | Mobile phone | With me |
| Phone data | Duplicate | Computer hard drive | Office |
| Phone data | Duplicate | Backup SD card | Home |
| Printed documents | Primary | Desk drawer | Office |
| Scanned documents | Duplicate | External drive | Home |

---

## Back Up Computer Files to a Local Device

Store backups on portable media (external hard drives or USB sticks) so you can move them to a safer location.

> [!important] Encrypt Your Backups
> Backup files often contain your most sensitive information. Learn to protect them in the [guide on secure file storage](https://securityinabox.org/en/files/secure-file-storage).

### Platform-Specific Instructions

**Linux**
- Most distributions include backup tools
- Ubuntu uses Déjà Dup for backup and encryption — [See this guide](https://www.techtarget.com/searchdatabackup/tutorial/Tutorial-How-to-use-Linux-Deja-Dup-to-back-up-and-restore-files)

**macOS**
- [Back up using Time Machine](https://support.apple.com/en-us/HT201250)

**Windows**
- [Back up files to an external drive](https://www.microsoft.com/en-us/windows/learning-center/back-up-files)

---

## Back Up Your Phone to a Local Device

Connect your phone to your computer via USB cable. You may need manufacturer software. Set your phone to back up automatically.

### Android

- [Move files to your PC](https://support.google.com/android/answer/9064445)
- If local backup proves difficult, you can [back up to Google's cloud](https://support.google.com/android/answer/2819582) (note: data stored on Google servers)

### iOS

- [Back up to macOS](https://support.apple.com/en-us/HT211229)
- [Back up to Windows](https://support.apple.com/en-us/108967)

> [!tip] Enable Encryption
> Select the "Encrypt local backup" checkbox and create a strong password.

---

## Cloud Backup Considerations

> [!warning] Understanding "The Cloud"
> When you hear "cloud," think "other people's computers." Services like Google Drive, iCloud, or Dropbox store data on company-owned servers. Adversaries may have extended time to access your information without detection.

**When cloud backup makes sense:**
- High risk of device destruction or seizure
- Local backups might be found and confiscated

**Key decision:** Use a service with end-to-end encryption, or encrypt files yourself before uploading.

### Encrypt Before Uploading

- [Cryptomator](https://cryptomator.org/) — [Usage guide](https://docs.cryptomator.org/)
- [VeraCrypt](https://veracrypt.io/) — Create an encrypted volume, then copy to cloud

### End-to-End Encrypted Cloud Services

| Service | Free Storage | Notes |
|---------|--------------|-------|
| [Proton Drive](https://proton.me/drive) | 5 GB | Paid plans available |
| [Mega.io](https://mega.io/) | 20 GB | Paid plans available |
| [Sync](https://www.sync.com/) | 5 GB | Paid plans available |
| [Internxt](https://internxt.com/drive) | 10 GB | Paid plans available |
| [Skiff Drive](https://skiff.com/drive) | 10 GB | Paid plans available |
| [Filen](https://filen.io/) | 10 GB | Paid plans available |
| [PCloud](https://www.pcloud.com/) | — | Paid (pCloud Encryption) |
| [SpiderOak](https://spideroak.com/one/) | — | Paid plans |
| [Tresorit](https://tresorit.com/) | — | Paid plans |
| [Nextcloud](https://nextcloud.com/) | 2+ GB | Self-hosted or [choose a provider](https://nextcloud.com/providers/) |

### Built-in Cloud Backup Tools

**Android**
- [Back up to Google account](https://support.google.com/android/answer/2819582)
- Encrypted with Google Account password; some data uses screen lock PIN/pattern

**iOS / macOS**
- [Use iCloud](https://support.apple.com/en-us/HT204025)
- [Turn on Advanced Data Protection](https://support.apple.com/en-us/108756)

**Windows**
- [Use OneDrive](https://support.microsoft.com/office/back-up-your-documents-pictures-and-desktop-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057)

---

## Back Up Your Email

Use an email client like Thunderbird to download and back up email locally.

**Protocol options:**
- **POP3** — Downloads and deletes from server
- **IMAP** — Keeps copies on server

See [Thunderbird's documentation](https://support.mozilla.org/en-US/kb/difference-between-imap-and-pop3) for setup details.

---

## Scan and Back Up Printed Documents

Scan or photograph important papers. Back up these digital copies alongside your other electronic documents.

---

## Set a Backup Schedule

To cover all data types, you'll need a combination of software and processes. Ensure each data type exists in **at least two separate locations**.

---

## Practice Recovery

> [!tip] Test Your Backups
> After creating backups, verify you can actually open and use the files. The **restore procedure** is what matters—not just the backup procedure.

---

## Establish Procedures for Coworkers

If working with a team:

1. Document backup procedures for all staff
2. Share procedures and ensure everyone follows them
3. Communicate risks of data loss to your work
4. Collaboratively map all team data using the grid format above

---

## Other Considerations

Plan for complete recovery scenarios:

- **Software and licenses** — How will you reinstall?
- **Equipment replacement** — What if devices are lost, destroyed, or confiscated?
- **Alternative workspace** — Where can you work during a crisis?

> [!tip] Budget for Recovery
> Consider setting aside funds for data recovery and equipment replacement. This could be written into grant proposals.