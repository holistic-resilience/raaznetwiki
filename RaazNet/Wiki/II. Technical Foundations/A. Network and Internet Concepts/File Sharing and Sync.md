---
title: "File Sharing and Sync"
tags: [file-sharing, file-sync, encryption, privacy-tools, open-source, peer-to-peer]
category: "Digital Security Tools"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["File Sharing", "File Synchronization", "End-to-End Encryption", "Privacy Tools"]
summary: "Guide to privacy-respecting file sharing and synchronization tools with end-to-end encryption."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "6 minutes"
---

# File Sharing and Sync

Discover how to privately share your files between your devices, with your friends and family, or anonymously online.

## File Sharing Options

### Using Existing Services

If you already use **Proton Drive** or have a **Bitwarden Premium** subscription, consider using their built-in file sharing capabilities—both offer end-to-end encryption.

#### Proton Drive File Sharing

Proton Drive allows you to share files or folders by:
- Generating a shareable public link
- Sending a unique link to a designated email address

**Features:**
- Public links can be password-protected
- Links can be set to expire and completely revoked
- Email-shared links support custom permissions
- File contents, names, folder names, and thumbnail previews are end-to-end encrypted

#### Bitwarden Send (Premium)

With a premium subscription, Bitwarden Send allows you to share files and text securely with end-to-end encryption.

**Features:**
- Optional password protection for Send links
- Automatic deletion options
- Secure text and file sharing

### Standalone File Sharing Tools

For those without existing services, the following standalone options ensure files you share cannot be read by remote servers.

---

### Send

**Send** is a fork of Mozilla's discontinued Firefox Send service that allows you to send files to others with a link.

**Key Features:**
- Files are encrypted on your device before upload
- Server cannot read file contents
- Optional password protection
- Multiple public instances available
- Self-hosting option

**How to Use:**
- **Web Interface:** Visit [send.vis.ee](https://send.vis.ee/) or other public instances
- **Command Line:** Use the [ffsend](https://github.com/timvisee/ffsend) CLI client

**CLI Example:**
```bash
ffsend upload --host https://send.vis.ee/ FILE
```

> **Tip:** If you send files frequently, the CLI client is recommended to avoid JavaScript-based encryption in the browser.

**Resources:**
- [Homepage](https://send.vis.ee/)
- [Public Instances](https://github.com/timvisee/send-instances)
- [Documentation](https://github.com/timvisee/send#readme)
- [Source Code](https://github.com/timvisee/send)

---

### OnionShare

**OnionShare** is an open-source tool for secure and anonymous file sharing of any size.

**How It Works:**
1. Starts a web server accessible as a Tor onion service
2. Generates an unguessable URL
3. Share the URL with recipients to download or send files

**Key Features:**
- Complete anonymity through Tor network
- No file size limits
- No third-party servers involved
- Tor bridge support for censorship circumvention

**Availability:**
- Windows
- macOS
- Linux
- Flathub

**Resources:**
- [Homepage](https://onionshare.org/)
- [Documentation](https://docs.onionshare.org/)
- [Source Code](https://github.com/onionshare/onionshare)

---

## File Synchronization

### Syncthing (Peer-to-Peer)

**Syncthing** is an open-source peer-to-peer continuous file synchronization utility for syncing files between two or more devices.

**How It Works:**
- Uses the [Block Exchange Protocol](https://docs.syncthing.net/specs/bep-v1.html#bep-v1) for data transfer
- Works over local network or internet
- No centralized server required
- All data encrypted using TLS

**Key Features:**
- Peer-to-peer architecture (no cloud dependency)
- Continuous synchronization
- Cross-platform support
- Open-source and auditable

**Availability:**
- Windows
- macOS
- Linux
- FreeBSD

**Resources:**
- [Homepage](https://syncthing.net/)
- [Documentation](https://docs.syncthing.net/)
- [Source Code](https://github.com/syncthing)

---

## Selection Criteria

### File Sharing Requirements

| Requirement | Description |
|-------------|-------------|
| No server-side decryption | Must not store decrypted data on remote servers |
| Open-source | Source code must be publicly available |
| Cross-platform | Must support Linux, macOS, Windows, or have a web interface |

### File Sync Requirements

**Minimum Requirements:**
- Must not require third-party remote/cloud servers
- Must be open-source software
- Must support Linux, macOS, Windows, or have a web interface

**Ideal Features:**
- Mobile clients for iOS and Android with document preview support
- Photo backup support from iOS and Android
- File/folder sync on Android

---

## Quick Comparison

| Tool | Type | Anonymity | Self-Hostable | Requires Account |
|------|------|-----------|---------------|------------------|
| Send | File Sharing | No | Yes | No |
| OnionShare | File Sharing | Yes (Tor) | N/A (local) | No |
| Syncthing | File Sync | No | N/A (P2P) | No |
| Proton Drive | Both | No | No | Yes |
| Bitwarden Send | File Sharing | No | Yes | Yes (Premium) |