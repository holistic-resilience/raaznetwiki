---
title: "File Sharing and Sync"
tags: [file-sharing, encryption, privacy, syncthing, onionshare, peer-to-peer]
category: "File Management"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Remote Workers]
topics: ["File Sharing", "File Synchronization", "End-to-End Encryption"]
summary: "Guide to privacy-focused file sharing and synchronization tools with end-to-end encryption."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "6 minutes"
---

# File Sharing and Sync

Discover how to privately share your files between your devices, with your friends and family, or anonymously online.

## File Sharing

If you already use [Proton Drive](https://www.privacyguides.org/en/cloud/#proton-drive) or have a [Bitwarden](https://www.privacyguides.org/en/passwords/#bitwarden) Premium subscription, consider using their file sharing capabilities—both offer end-to-end encryption. Otherwise, the standalone options listed below ensure that the files you share are not read by a remote server.

### Send

**Send** is a fork of Mozilla's discontinued Firefox Send service that allows you to send files to others with a link. Files are encrypted on your device so they cannot be read by the server, and can be optionally password-protected.

- **Website**: [send.vis.ee](https://send.vis.ee/)
- **Public Instances**: [Available list](https://github.com/timvisee/send-instances)
- **Source Code**: [GitHub](https://github.com/timvisee/send)

#### Command-Line Usage

Send can be used via its web interface or via the [ffsend](https://github.com/timvisee/ffsend) CLI. For frequent file transfers, the CLI client avoids JavaScript-based encryption:

```bash
ffsend upload --host https://send.vis.ee/ FILE
```

### OnionShare

**OnionShare** is an open-source tool that lets you securely and anonymously share files of any size. It works by starting a web server accessible as a Tor onion service with an unguessable URL.

- **Website**: [onionshare.org](https://onionshare.org/)
- **Documentation**: [docs.onionshare.org](https://docs.onionshare.org/)
- **Platforms**: Windows, macOS, Linux, Flathub

OnionShare provides the option to connect via [Tor bridges](https://docs.onionshare.org/2.6.2/en/tor.html#automatic-censorship-circumvention) to circumvent censorship.

### File Sharing Criteria

Recommended tools must meet these requirements:

- Must not store decrypted data on a remote server
- Must be open-source software
- Must have clients for Linux, macOS, and Windows, or have a web interface

## File Sync

### Syncthing (Peer-to-Peer)

**Syncthing** is an open-source peer-to-peer continuous file synchronization utility. It synchronizes files between two or more devices over the local network or internet without a centralized server.

- **Website**: [syncthing.net](https://syncthing.net/)
- **Documentation**: [docs.syncthing.net](https://docs.syncthing.net/)
- **Platforms**: Windows, macOS, Linux, FreeBSD

**Key Features:**
- Uses the [Block Exchange Protocol](https://docs.syncthing.net/specs/bep-v1.html#bep-v1) for data transfer
- All data encrypted using TLS
- No centralized server required

### File Sync Criteria

#### Minimum Requirements

- Must not require a third-party remote/cloud server
- Must be open-source software
- Must have clients for Linux, macOS, and Windows, or have a web interface

#### Best-Case Features

- Mobile clients for iOS and Android with document preview support
- Photo backup support from iOS and Android
- File/folder sync on Android

## Additional Notes

### Proton Drive Sharing

Proton Drive allows you to share files or folders by generating a shareable public link or sending a unique link to a designated email address. Public links can be password-protected, set to expire, and completely revoked. File contents, names, and thumbnail previews are end-to-end encrypted.

### Bitwarden Send

With a premium subscription, Bitwarden Send allows secure file and text sharing with end-to-end encryption. Features include password protection and automatic deletion options.