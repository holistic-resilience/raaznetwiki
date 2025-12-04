---
title: "The Best Private and Secure Cloud Storage Providers"
tags: [cloud-storage, encryption, privacy, end-to-end-encryption, file-storage]
category: "Cloud Storage"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Remote Workers]
topics: ["Cloud Storage", "End-to-End Encryption", "Data Privacy"]
summary: "Guide to privacy-focused cloud storage providers with end-to-end encryption, including Proton Drive, Tresorit, and Peergos."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "6 minutes"
---

# Cloud Storage

Many cloud storage providers require your full trust that they will not look at your files. The alternatives listed below eliminate the need for trust by implementing secure end-to-end encryption (E2EE).

If these alternatives do not fit your needs, consider using encryption software like [Cryptomator](https://www.privacyguides.org/en/encryption/#cryptomator-cloud) with another cloud provider. Using Cryptomator in conjunction with any cloud provider may be a good idea to reduce the risk of encryption flaws in a provider's native clients.

> **Note on Nextcloud:** For technical users, Nextcloud is a recommended tool for self-hosting a file management suite. However, third-party Nextcloud storage providers are not recommended at this time due to concerns about Nextcloud's built-in E2EE functionality for home users.

---

## Recommended Providers

### Proton Drive

**Proton Drive** is an encrypted cloud storage provider from the popular encrypted email provider Proton Mail.

| Feature | Details |
|---------|---------|
| **Free Storage** | 2 GB (up to 5 GB with additional steps) |
| **Platforms** | Web, Windows, macOS, Android, iOS |
| **Audit Status** | Web application audited by Securitum (2021); mobile clients not yet publicly audited |

**Links:** [Homepage](https://proton.me/drive) | [Privacy Policy](https://proton.me/drive/privacy-policy) | [Source Code](https://github.com/ProtonMail/WebClients)

---

### Tresorit

**Tresorit** is a Swiss-Hungarian encrypted cloud storage provider founded in 2011, owned by Swiss Post (the national postal service of Switzerland).

| Feature | Details |
|---------|---------|
| **Platforms** | Web, Windows, macOS, Linux, Android, iOS |
| **Certifications** | ISO/IEC 27001:2013, Swiss Digital Trust Label |

**Security Audits:**
- **2022:** ISO/IEC 27001:2013 Compliance Certification by TÜV Rheinland InterCert Kft
- **2021:** Penetration Testing by Computest
- **2019:** Penetration Testing by Ernst & Young (confirmed data confidentiality claims)

The Swiss Digital Trust Label requires passing 35 criteria related to security, privacy, and reliability.

**Links:** [Homepage](https://tresorit.com/) | [Privacy Policy](https://tresorit.com/legal/privacy-policy)

---

### Peergos

**Peergos** is a decentralized protocol and open-source platform for storage, social media, and applications. It provides a secure and private space for storing, sharing, and editing photos, videos, documents, and more.

| Feature | Details |
|---------|---------|
| **Encryption** | Quantum-resistant E2EE |
| **Architecture** | Decentralized (built on IPFS) |
| **Self-Hosting** | Supported |
| **Platforms** | Web, Windows, macOS, Linux, Android |

**Key Features:**
- Built on InterPlanetary File System (IPFS) for censorship resistance
- Sync engine for bi-directional local folder synchronization
- WebDAV bridge for third-party application access
- Client, server, and CLI run from a single binary

**Security Audits:**
- **November 2024:** Audited by Radically Open Security (all issues fixed)
- **June 2019:** Audited by Cure53 (all issues fixed)

**Links:** [Homepage](https://peergos.org/) | [Privacy Policy](https://peergos.net/privacy.html) | [Documentation](https://book.peergos.org/) | [Source Code](https://github.com/Peergos/Peergos)

---

## Selection Criteria

### Minimum Requirements

All recommended providers must meet these criteria:

- Enforce end-to-end encryption
- Offer a free plan or trial period for testing
- Support TOTP, FIDO2 multifactor authentication, or passkey logins
- Provide a web interface with basic file management functionality
- Allow easy export of all files and documents

### Best-Case Features

Ideal providers would also include:

- Open-source clients
- Independent third-party audits of all clients
- Native clients for Linux, Android, Windows, macOS, and iOS
- Easy file sharing with other users
- Basic file preview and editing on the web interface

---

## Additional Notes

**ISO/IEC 27001:2013** compliance relates to a company's information security management system and covers the sales, development, maintenance, and support of their cloud services.