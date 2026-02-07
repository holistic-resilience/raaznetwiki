---
title: "Secure File Exchange and Anonymity"
tags:
  [
    file-sharing,
    anonymity,
    onionshare,
    syncthing,
    metadata,
    iran-security,
    surveillance-circumvention,
    tor,
  ]
category: "Cryptography and Encryption"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, Whistleblowers]
topics:
  [
    "Anonymous File Transfer",
    "Metadata Sanitization",
    "Peer-to-Peer Sync",
    "Zero-Knowledge Cloud",
  ]
summary: "A comprehensive guide on transferring files securely and anonymously within the Iranian internet landscape, bypassing censorship and surveillance mechanisms."
source: "Raaznet Aggregation (Privacy Guides, Freedom of the Press Foundation, Tactical Tech)"
content_type: "Technical Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Working Tor Browser (with Bridges)", "Basic understanding of encryption"]
last_updated: "2026-02-06"
---

# Secure File Exchange and Anonymity

In the context of the Iranian internet (internally known as the National Information Network), transferring files is not merely a matter of convenience—it is a security operation. The regime employs Deep Packet Inspection (DPI) to analyze traffic, blocks major file-sharing platforms, and monitors domestic servers.

This guide outlines methods to share files while maintaining **confidentiality** (only the recipient can read it) and **anonymity** (no one knows who sent it).

---

## I. The Golden Rule: Sanitize Before You Share

Before transferring any file, you must understand that the file itself contains evidence. **Metadata** (data about data) can reveal your identity even if the transfer method is secure.

### Understanding Metadata Risks

Photos taken with smartphones often contain GPS coordinates, device models, and timestamps. Documents (Word, PDF) contain author names and edit history. If you send a photo of a protest to a journalist, the _content_ might be encrypted, but the _metadata_ could lead the Cyber Police (FATA) to your doorstep.

### Tools for Metadata Removal

Before uploading or sharing, "clean" your files.

- **MAT2 (Metadata Anonymisation Toolkit):** The standard for Linux/Tails users. It removes metadata from images, audio, and documents without compromising the file content.
- **ExifCleaner:** A drag-and-drop tool for Windows and macOS.
- **Scrambled Exif (Android):** An app that allows you to strip metadata before sharing a photo via Signal or Telegram.

> **Raaznet Warning:** Renaming a file does _not_ remove its metadata. You must use dedicated tools.

---

## II. Anonymous File Transfer (Tor-Based)

For the highest level of security, particularly for whistleblowers or high-risk activists, usage of the Tor network is mandatory. This hides your IP address from the recipient and the hosting provider.

> **Iranian Context Note:** Accessing Tor in Iran requires **Pluggable Transports** (Snowflake or Obfs4). Ensure your Tor connection is stable before initiating these transfers.

### 1. OnionShare

**OnionShare** is the gold standard for anonymous file exchange. It turns your computer into a temporary, anonymous web server accessible only via the Tor network.

- **How it works:** You add a file to OnionShare. It generates a `.onion` link. You send this link to the recipient (via Signal). The recipient opens the link in Tor Browser to download directly from your device.
- **Why it is secure:**
  - No third-party server stores your file.
  - The connection is end-to-end encrypted.
  - Once you close the app, the link stops working, leaving no digital trail on the internet.
- **Best for:** Sending sensitive documents to a single recipient without leaving a trace on a cloud server.

### 2. SecureDrop

**SecureDrop** is an open-source submission system used by major media organizations (e.g., The Guardian, The Washington Post) to accept leaks from sources.

- **Usage:** You do not install SecureDrop; you access a media organization's SecureDrop `.onion` address via Tor Browser.
- **Anonymity:** It is designed to minimize metadata. It does not log IP addresses or browser fingerprints.
- **Best for:** Whistleblowers submitting evidence of corruption or human rights violations to news outlets.

---

## III. Ephemeral & Encrypted Web Sharing

If the recipient cannot use Tor, or for faster transfers, use "dead drop" style web tools that use client-side encryption. This means the server owner cannot read the file.

### 1. Private "Send" Instances

Based on the now-discontinued Firefox Send, these services allow you to upload a file and generate a link that expires after a certain number of downloads or hours.

- **Recommended Tool:** **Send (Tim Visee fork)** or **Bitwarden Send**.
- **Features:**
  - **Password Protection:** Always set a password for the file link.
  - **Expiration:** Set the file to delete after **1 download** or **1 hour**.
- **Iranian Context:** Many public "Send" instances may be filtered. If using Bitwarden Send, a Premium subscription allows for file attachments.

### 2. Wormhole

**Wormhole.app** provides end-to-end encrypted file sharing. It is fast and works in the browser.

- **Streaming Mode:** For P2P transfers, if both users are online, the file is streamed directly.
- **Storage:** If the recipient is offline, encrypted files are stored for up to 24 hours.

---

## IV. Peer-to-Peer Synchronization (Bypassing the Cloud)

For teams working on shared projects who need to keep folders in sync without trusting Google Drive or Dropbox.

### Syncthing

**Syncthing** allows you to sync files between devices (e.g., your laptop and your colleague's phone) without a central server.

- **Security:** All communication is encrypted using TLS. Ideally, use "Untrusted Device" encryption if syncing to a device you don't fully control.
- **Censorship Resistance:** Syncthing does not rely on a central domain that can be easily blocked. It uses a distributed discovery protocol.
- **Offline Capability:** If both devices are on the same local network (e.g., a localized mesh network during an internet shutdown), Syncthing can sync files without internet access.

---

## V. Zero-Knowledge Cloud Storage

If you must store files in the cloud for later retrieval or sharing, you must ensure the provider cannot access them. This is critical if the provider receives a subpoena or if their servers are compromised.

### 1. Cryptomator (Cloud-Agnostic Encryption)

If you use Google Drive, Dropbox, or OneDrive (often accessible via VPN in Iran), you should **never** upload raw files.

- **Solution:** Use **Cryptomator**. It creates a "Vault" on your computer. Anything you drag into this vault is automatically encrypted _before_ it syncs to the cloud.
- **Benefit:** Even if Google or a state actor accesses your cloud account, they only see garbled, encrypted nonsense.

### 2. Proton Drive

Part of the Proton ecosystem (Switzerland-based).

- **Features:** End-to-end encryption by default. Includes secure file sharing links with password protection and expiration timers.
- **Iranian Context:** Proton's domains are frequently targeted by the filtering committee. Usage usually requires a VPN.

---

## VI. Critical Security Checklist for Iranian Users

1.  **Avoid Domestic Hosts:** Never use Iranian file-sharing services (e.g., UploadBoy, PicoFile) for sensitive data. These providers are legally required to log user data and provide access to security agencies.
2.  **VPN/Tor is Mandatory:** Even if a service like Google Drive is accessible without a VPN, do not use it without one. Your ISP can see the traffic destination and volume.
3.  **Use Signal for Links:** If you upload a file to a "Send" service, share the download link via **Signal** (with disappearing messages enabled), never via SMS or unencrypted Telegram.
4.  **Internet Shutdown Preparedness:** Install **Syncthing** and learn how to use it over local LAN. Keep a copy of **OnionShare** and **Tor Browser** installers on a USB drive to share with trusted contacts offline.
