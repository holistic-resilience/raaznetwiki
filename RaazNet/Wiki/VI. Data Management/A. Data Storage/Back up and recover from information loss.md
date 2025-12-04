```yaml
---
title: "Back Up and Recover from Information Loss"
tags: [backup, data-recovery, digital-security, encryption, cloud-storage]
category: "Data Protection"
difficulty: "Intermediate"
audience: [General Public, Activists, IT Administrators, Privacy-Conscious Users]
topics: ["Data Backup", "File Recovery", "Cloud Storage Security", "Digital Security"]
summary: "Comprehensive guide to creating backup strategies, recovering lost data, and protecting information across devices and cloud services."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file management"]
estimated_read_time: "15 minutes"
---
```

# Back Up and Recover from Information Loss

Losing important data can be devastating—whether from hardware failure, theft, accidental deletion, or malicious attack. This guide covers how to recover lost information and, more importantly, how to create a robust backup strategy to prevent future data loss.

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

If you've already lost data, start troubleshooting with the [Digital First Aid Kit's guide on lost data](https://digitalfirstaid.org/topics/lost-data/).

### Important: Act Quickly

Data recovery tools only work if your device hasn't overwritten your deleted information. **Stop using your device immediately** until you've attempted recovery. The longer you use your computer after deletion, the less likely recovery becomes.

> **Why recovery is possible:** When you delete a file, it disappears from view but remains on your device. Even emptying the Recycle Bin or Trash doesn't immediately remove files from your hard drive. See [[Destroy Sensitive Information]] to understand how this can also be a security risk.

### Recovery Tools

**Cross-Platform (Linux, macOS, Windows)**
- [TestDisk & PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec) — See the [official guide](https://www.cgsecurity.org/testdisk.pdf) for instructions

**Windows Only**
- [Recuva](https://www.ccleaner.com/recuva/) — See [their usage guide](https://www.ccleaner.com/knowledge/recuva-tip-search-for-files)

---

## Create a Backup Plan

### Step 1: Organize Your Information

Move all folders containing files you want to back up into a single location, such as your "Documents" folder. This simplifies the backup process.

### Step 2: Map Your Information

Identify where your personal and work information currently exists:

- **Email** — On your provider's server, your computer, or both
- **Multiple accounts** — Different email, social media, and cloud accounts
- **Removable media** — USB drives, portable hard drives
- **Websites** — Content you've published online
- **Physical documents** — Notebooks, diaries, letters, contracts

For detailed guidance, see the [Holistic Security manual on cataloguing information](https://holistic-security.tacticaltech.org/chapters/explore/2-4-understanding-and-cataloguing-our-information.html).

### Step 3: Identify Primary Copies vs. Duplicates

The **primary copy** is the most up-to-date version—the one you would edit. This distinction is critical for backup planning.

> **Example disaster scenario:** You back up only duplicates of an important document. The primary copy gets lost before duplicates are updated. If you've been editing a file on a USB stick while traveling, that becomes your primary copy.

### Step 4: Document Your Data Locations

Create a table mapping all your data. Here's a basic example:

| Data Type | Primary/Duplicate | Storage Device | Location |
|-----------|-------------------|----------------|----------|
| Research files | Primary | Computer hard drive | Office |
| Testimonies | Duplicate | USB memory stick | With me |
| Program databases | Primary | Computer hard drive | Office |
| Shared documents | Duplicate | Office server | Office |
| Videos and pictures | Duplicate | External hard disk | Home |
| Email & contacts | Primary | Email account | Email server |
| Text messages & contacts | Primary | Mobile phone | With me |
| Printed documents | Primary | Desk drawer | Office |

**Analyze the gaps:** In this example:
- If the office computer crashes, only duplicates on external media survive
- No offline copy of email or address book exists
- No backup of mobile phone data
- No duplicates of printed documents

### Improved Backup Structure Example

| Data Type | Primary/Duplicate | Storage Device | Location |
|-----------|-------------------|----------------|----------|
| Testimonies | Primary | Computer hard drive | Office |
| Testimonies | Duplicate | USB memory stick | Home |
| Research files | Primary | Computer hard drive | Office |
| Research files | Duplicate | USB memory stick | With me |
| Program databases | Primary | Computer hard drive | Office |
| Program databases | Duplicate | External drive | Home |
| Email & contacts | Primary | Email account | Email server |
| Email & contacts | Duplicate | Thunderbird | Office |
| Phone data | Primary | Mobile phone | With me |
| Phone data | Duplicate | Computer hard drive | Office |
| Phone data | Duplicate | Backup SD card | Home |
| Printed documents | Primary | Desk drawer | Office |
| Scanned documents | Duplicate | External drive | Home |
| All documents backup | Duplicate | Office server | Office |

---

## Back Up Computer Files to a Local Device

Store backups on portable media (external hard drives or USB sticks) so you can keep them in a separate, safe location.

> **Security note:** Backup files often contain your most sensitive information. Protect them with encryption. See [[Secure File Storage]] for guidance.

### Platform-Specific Instructions

**Linux**
- Most distributions include backup tools
- Ubuntu: Use [Déjà Dup](https://www.techtarget.com/searchdatabackup/tutorial/Tutorial-How-to-use-Linux-Deja-Dup-to-back-up-and-restore-files) (built-in, supports encryption)

**macOS**
- Use [Time Machine](https://support.apple.com/en-us/HT201250) to back up to an external drive

**Windows**
- Follow [Microsoft's backup guide](https://www.microsoft.com/en-us/windows/learning-center/back-up-files)

---

## Back Up Your Phone to a Local Device

Back up your phone to your computer, then store that backup on external media. Enable automatic backups when possible.

### Android

- [Transfer files to PC via USB](https://support.google.com/android/answer/9064445)
- Alternative: [Back up to Google cloud services](https://support.google.com/android/answer/2819582) (note: data stored on Google servers)

### iOS

- [Back up to macOS](https://support.apple.com/en-us/HT211229)
- [Back up to Windows](https://support.apple.com/en-us/108967)
- **Important:** Select "Encrypt local backup" and create a strong password

---

## Cloud Backup Considerations

> **Remember:** "The cloud" means "other people's computers." Services like Google Drive, iCloud, or Dropbox store your data on company-owned servers. Adversaries may have extended time to access your information without detection.

**When local backup is better:** You can notice suspicious activity on devices in your possession more easily than on remote servers.

**When cloud backup makes sense:** If your devices or workspace might be destroyed, or local backups could be seized, encrypted cloud storage may be appropriate.

### Option 1: Encrypt Files Before Uploading

- [Cryptomator](https://cryptomator.org/) — [Usage guide](https://docs.cryptomator.org/)
- [VeraCrypt](https://veracrypt.io/) — Create an encrypted volume, then upload it

### Option 2: Use End-to-End Encrypted Services

| Service | Free Storage | Notes |
|---------|--------------|-------|
| [Proton Drive](https://proton.me/drive) | 5 GB | Then paid |
| [Mega.io](https://mega.io/) | 20 GB | Then paid |
| [Sync](https://www.sync.com/) | 5 GB | Then paid |
| [Internxt](https://internxt.com/drive) | 10 GB | Then paid |
| [Skiff Drive](https://skiff.com/drive) | 10 GB | Then paid |
| [Filen](https://filen.io/) | 10 GB | Then paid |
| [Nextcloud](https://nextcloud.com/) | 2 GB+ | Self-hosted or [choose a provider](https://nextcloud.com/providers/) |
| [PCloud](https://www.pcloud.com/) | Paid only | pCloud Encryption option |
| [SpiderOak](https://spideroak.com/one/) | Paid only | — |
| [Tresorit](https://tresorit.com/) | Paid only | — |

### Option 3: Use Built-in Device Backup Tools

**Android**
- [Back up to Google](https://support.google.com/android/answer/2819582) — Encrypted with your Google password; some data uses your screen lock for encryption

**iOS**
- [Use iCloud](https://support.apple.com/en-us/HT204025)
- [Encrypt backups](https://support.apple.com/en-us/108756)

**macOS**
- [Use iCloud](https://support.apple.com/en-us/HT204025)
- [Enable Advanced Data Protection](https://support.apple.com/en-us/108756)

**Windows**
- [Use OneDrive](https://support.microsoft.com/office/back-up-your-documents-pictures-and-desktop-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057)

---

## Back Up Your Email

Use an email client like [Thunderbird](https://www.thunderbird.net/) to download and back up your email locally.

**Protocol options:**
- **POP3** — Downloads email and deletes from server
- **IMAP** — Downloads email and keeps copy on server

See [Thunderbird's documentation](https://support.mozilla.org/en-US/kb/difference-between-imap-and-pop3) for details. Most email providers offer setup instructions for both protocols.

---

## Scan and Back Up Printed Documents

Scan or photograph all important papers. Back up these digital copies alongside your other electronic documents using the methods described above.

---

## Set a Backup Schedule

To protect all data types, you'll need a combination of software and processes. **Ensure each data type exists in at least two separate locations.**

---

## Practice Recovery

After creating backups, **test them**. Verify you can:
- Open the backup files
- Use them as intended
- Restore them to a working state

> **Key insight:** The restore procedure—not the backup procedure—is what matters when disaster strikes.

---

## Establish Procedures for Coworkers

If working with a team:

1. **Document procedures** for reliable, secure backups
2. **Share with all staff** and ensure understanding
3. **Communicate risks** of data loss to your work
4. **Collaborate on mapping** all team data using a grid like the examples above

---

## Other Considerations

Plan for complete recovery scenarios:

- **Software and licenses** — How will you reinstall applications?
- **Equipment replacement** — How will you replace lost, destroyed, or confiscated devices?
- **Alternative workspace** — Where can you work during a crisis?

**Budget for recovery:** Consider setting aside funds for data loss scenarios. Include this in grant applications or operational budgets.