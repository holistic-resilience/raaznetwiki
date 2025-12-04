---
title: "File Sharing and Sync"
tags: [file-sharing, encryption, privacy, syncthing, onionshare, end-to-end-encryption]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Security Practitioners]
topics: ["File Sharing", "File Synchronization", "End-to-End Encryption", "Privacy Tools"]
summary: "Guide to privacy-focused file sharing and synchronization tools including Send, OnionShare, and Syncthing."
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

If you already use [Proton Drive](https://www.privacyguides.org/en/cloud/#proton-drive) or have a [Bitwarden](https://www.privacyguides.org/en/passwords/#bitwarden) Premium subscription, consider using the file sharing capabilities that they each offer, both of which use end-to-end encryption. Otherwise, the standalone options listed here ensure that the files you share are not read by a remote server.

### Send

**Send** is a fork of Mozilla's discontinued Firefox Send service which allows you to send files to others with a link. Files are encrypted on your device so that they cannot be read by the server, and they can be optionally password-protected as well. The maintainer of Send hosts a [public instance](https://send.vis.ee/). You can use other public instances, or you can host Send yourself.

**Resources:**
- [Homepage](https://send.vis.ee/)
- [Public Instances](https://github.com/timvisee/send-instances)
- [Documentation](https://github.com/timvisee/send#readme)
- [Source Code](https://github.com/timvisee/send)

Send can be used via its web interface or via the [ffsend](https://github.com/timvisee/ffsend) CLI. If you are familiar with the command-line and send files frequently, we recommend using the CLI client to avoid JavaScript-based encryption. You can specify the `--host` flag to use a specific server:

```bash
ffsend upload --host https://send.vis.ee/ FILE
```

### OnionShare

**OnionShare** is an open-source tool that lets you securely and anonymously share a file of any size. It works by starting a web server accessible as a Tor onion service, with an unguessable URL that you can share with the recipients to download or send files.

**Resources:**
- [Homepage](https://onionshare.org/)
- [Onion Service](http://lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion/)
- [Documentation](https://docs.onionshare.org/)
- [Source Code](https://github.com/onionshare/onionshare)

**Available for:** Windows, macOS, Linux, Flathub

OnionShare provides the option to connect via [Tor bridges](https://docs.onionshare.org/2.6.2/en/tor.html#automatic-censorship-circumvention) to circumvent censorship.

### File Sharing Criteria

Requirements for recommended file sharing tools:
- Must not store decrypted data on a remote server
- Must be open-source software
- Must either have clients for Linux, macOS, and Windows; or have a web interface

## File Sync

### Syncthing (P2P)

**Syncthing** is an open-source peer-to-peer continuous file synchronization utility. It is used to synchronize files between two or more devices over the local network or the internet. Syncthing does not use a centralized server; it uses the [Block Exchange Protocol](https://docs.syncthing.net/specs/bep-v1.html#bep-v1) to transfer data between devices. All data is encrypted using TLS.

**Resources:**
- [Homepage](https://syncthing.net/)
- [Documentation](https://docs.syncthing.net/)
- [Source Code](https://github.com/syncthing)

**Available for:** Windows, macOS, Linux, FreeBSD

### File Sync Criteria

**Minimum Requirements:**
- Must not require a third-party remote/cloud server
- Must be open-source software
- Must either have clients for Linux, macOS, and Windows; or have a web interface

**Best-Case Features:**
- Should have mobile clients for iOS and Android which at least support document previews
- Should support photo backups from iOS and Android, and optionally support file/folder sync on Android

## Additional Notes

### Proton Drive File Sharing

Proton Drive allows you to share files or folders by generating a shareable public link or sending a unique link to a designated email address. Public links can be protected with a password, set to expire, and completely revoked, while links shared via email can have custom permissions and be similarly revoked. File contents, file and folder names, and thumbnail previews are end-to-end encrypted.

### Bitwarden Send

With a premium subscription, Bitwarden Send allows you to share files and text securely with end-to-end encryption. A password can be required along with the Send link. Bitwarden Send also features automatic deletion.