---
title: "File Sharing and Sync"
tags: [file-sharing, encryption, privacy, syncthing, onionshare, peer-to-peer]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users]
topics: ["File Sharing", "File Synchronization", "End-to-End Encryption"]
summary: "Guide to privately sharing files between devices or anonymously online using encrypted, open-source tools."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "4 minutes"
---

# File Sharing and Sync

Discover how to privately share your files between your devices, with your friends and family, or anonymously online.

## File Sharing

If you already use [Proton Drive](https://www.privacyguides.org/en/cloud/#proton-drive) or have a [Bitwarden](https://www.privacyguides.org/en/passwords/#bitwarden) Premium subscription, consider using the file sharing capabilities that they each offer, both of which use end-to-end encryption. Otherwise, the standalone options listed here ensure that the files you share are not read by a remote server.

### Send

**Send** is a fork of Mozilla's discontinued Firefox Send service which allows you to send files to others with a link. Files are encrypted on your device so that they cannot be read by the server, and they can be optionally password-protected as well.

- **Homepage**: [send.vis.ee](https://send.vis.ee/)
- **Public Instances**: [github.com/timvisee/send-instances](https://github.com/timvisee/send-instances)
- **Source Code**: [github.com/timvisee/send](https://github.com/timvisee/send)

Send can be used via its web interface or via the [ffsend](https://github.com/timvisee/ffsend) CLI. If you are familiar with the command-line and send files frequently, the CLI client avoids JavaScript-based encryption. You can specify the `--host` flag to use a specific server:

```bash
ffsend upload --host https://send.vis.ee/ FILE
```

### OnionShare

**OnionShare** is an open-source tool that lets you securely and anonymously share a file of any size. It works by starting a web server accessible as a Tor onion service, with an unguessable URL that you can share with recipients to download or send files.

- **Homepage**: [onionshare.org](https://onionshare.org/)
- **Documentation**: [docs.onionshare.org](https://docs.onionshare.org/)
- **Source Code**: [github.com/onionshare/onionshare](https://github.com/onionshare/onionshare)
- **Platforms**: Windows, macOS, Linux, Flathub

OnionShare provides the option to connect via [Tor bridges](https://docs.onionshare.org/2.6.2/en/tor.html#automatic-censorship-circumvention) to circumvent censorship.

### File Sharing Criteria

Requirements for recommended file sharing tools:

- Must not store decrypted data on a remote server
- Must be open-source software
- Must have clients for Linux, macOS, and Windows; or have a web interface

## File Sync

### Syncthing (P2P)

**Syncthing** is an open-source peer-to-peer continuous file synchronization utility. It synchronizes files between two or more devices over the local network or the internet without using a centralized server. It uses the [Block Exchange Protocol](https://docs.syncthing.net/specs/bep-v1.html#bep-v1) to transfer data between devices, with all data encrypted using TLS.

- **Homepage**: [syncthing.net](https://syncthing.net/)
- **Documentation**: [docs.syncthing.net](https://docs.syncthing.net/)
- **Source Code**: [github.com/syncthing](https://github.com/syncthing)
- **Platforms**: Windows, macOS, Linux, FreeBSD

### File Sync Criteria

**Minimum Requirements:**
- Must not require a third-party remote/cloud server
- Must be open-source software
- Must have clients for Linux, macOS, and Windows; or have a web interface

**Best-Case:**
- Should have mobile clients for iOS and Android with document preview support
- Should support photo backups from iOS and Android, and optionally file/folder sync on Android

## Notes on Existing Services

**Proton Drive** allows you to share files or folders by generating a shareable public link or sending a unique link to a designated email address. Public links can be protected with a password, set to expire, and completely revoked. File contents, file and folder names, and thumbnail previews are end-to-end encrypted.

**Bitwarden Send** (Premium subscription required) allows you to share files and text securely with end-to-end encryption. Features include password protection and automatic deletion.