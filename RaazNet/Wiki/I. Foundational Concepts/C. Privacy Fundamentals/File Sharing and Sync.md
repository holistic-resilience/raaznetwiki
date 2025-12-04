---
title: "File Sharing and Sync"
tags: [file-sharing, encryption, privacy, syncthing, onionshare, peer-to-peer]
category: "Digital Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["File Sharing", "File Synchronization", "End-to-End Encryption", "Anonymous Sharing"]
summary: "Guide to privacy-respecting file sharing and synchronization tools with end-to-end encryption."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "6 minutes"
---

# File Sharing and Sync

Discover how to privately share your files between your devices, with your friends and family, or anonymously online.

## File Sharing

If you already use [Proton Drive](https://www.privacyguides.org/en/cloud/#proton-drive) or have a [Bitwarden](https://www.privacyguides.org/en/passwords/#bitwarden) Premium subscription, consider using their built-in file sharing capabilities—both offer end-to-end encryption. Otherwise, the standalone options listed below ensure that the files you share cannot be read by a remote server.

### Send

**Send** is a fork of Mozilla's discontinued Firefox Send service that allows you to send files to others via a link. Files are encrypted on your device so they cannot be read by the server, and can be optionally password-protected.

**Key Features:**
- Client-side encryption before upload
- Optional password protection
- Self-hostable or use [public instances](https://github.com/timvisee/send-instances)
- Command-line client available ([ffsend](https://github.com/timvisee/ffsend))

**Links:** [Homepage](https://send.vis.ee/) | [Documentation](https://github.com/timvisee/send#readme) | [Source Code](https://github.com/timvisee/send)

**CLI Usage Example:**
```bash
ffsend upload --host https://send.vis.ee/ FILE
```

> **Tip:** If you send files frequently and are comfortable with the command line, the CLI client avoids JavaScript-based encryption in the browser.

### OnionShare

**OnionShare** is an open-source tool for securely and anonymously sharing files of any size. It works by starting a web server accessible as a Tor onion service with an unguessable URL.

**Key Features:**
- Anonymous file sharing via Tor
- No file size limits
- Direct peer-to-peer transfer (no server storage)
- Support for [Tor bridges](https://docs.onionshare.org/2.6.2/en/tor.html#automatic-censorship-circumvention) to circumvent censorship

**Links:** [Homepage](https://onionshare.org/) | [Documentation](https://docs.onionshare.org/) | [Source Code](https://github.com/onionshare/onionshare)

**Availability:** Windows, macOS, Linux, [Flathub](https://flathub.org/apps/org.onionshare.OnionShare)

### File Sharing Criteria

Requirements for recommended file sharing tools:
- Must not store decrypted data on a remote server
- Must be open-source software
- Must have clients for Linux, macOS, and Windows, or provide a web interface

---

## File Sync

### Syncthing (P2P)

**Syncthing** is an open-source peer-to-peer continuous file synchronization utility. It synchronizes files between two or more devices over the local network or internet without using a centralized server.

**Key Features:**
- Peer-to-peer synchronization (no central server)
- Uses the [Block Exchange Protocol](https://docs.syncthing.net/specs/bep-v1.html#bep-v1) for data transfer
- All data encrypted using TLS
- Works across local networks and the internet

**Links:** [Homepage](https://syncthing.net/) | [Documentation](https://docs.syncthing.net/) | [Source Code](https://github.com/syncthing)

**Availability:** Windows, macOS, Linux, FreeBSD

### File Sync Criteria

**Minimum Requirements:**
- Must not require a third-party remote/cloud server
- Must be open-source software
- Must have clients for Linux, macOS, and Windows, or provide a web interface

**Best-Case Features:**
- Mobile clients for iOS and Android with document preview support
- Photo backup support from iOS and Android
- File/folder sync capability on Android

---

## Additional Options

### Proton Drive
[Proton Drive](https://proton.me/support/drive-shareable-link) allows sharing files or folders via public links or designated email addresses. Public links can be password-protected, set to expire, and revoked. File contents, names, and thumbnails are end-to-end encrypted.

### Bitwarden Send
With a [premium subscription](https://bitwarden.com/help/about-bitwarden-plans/#compare-personal-plans), [Bitwarden Send](https://bitwarden.com/products/send) enables secure file and text sharing with end-to-end encryption, optional password protection, and automatic deletion.