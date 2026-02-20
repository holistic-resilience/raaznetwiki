---
title: "Self-Hosted Storage Solutions"
tags:
  [
    self-hosting,
    digital-sovereignty,
    nextcloud,
    syncthing,
    onionshare,
    iran-security,
    encryption,
  ]
category: "Data Storage"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, System Administrators]
topics:
  [
    "Self-Hosting",
    "File Synchronization",
    "Photo Management",
    "Bypassing Censorship",
  ]
summary: "Comprehensive guide to self-hosting storage services to achieve digital sovereignty, with specific strategies for bypassing Iranian internet restrictions and surveillance."
source: "Raaznet Aggregation"
content_type: "Guide"
security_level: "Advanced"
language: "English"
prerequisites:
  [
    "Linux command line proficiency",
    "Basic networking knowledge",
    "Hardware (Laptop/Raspberry Pi)",
  ]
estimated_read_time: "12 minutes"
---

# Self-Hosted Storage Solutions

**Self-hosting** involves running applications and storing data on your own hardware rather than relying on third-party cloud providers like Google Drive, Dropbox, or iCloud. For Iranian users, this is a critical step toward **digital sovereignty**—eliminating reliance on foreign corporations that may ban users due to sanctions, and avoiding domestic platforms compliant with the Islamic Republic's surveillance apparatus.

> **Warning:** Self-hosting places the burden of security entirely on you. If you fail to update your software, secure your network, or encrypt your disks, you may be more vulnerable than if you used a reputable cloud provider. In the Iranian context, physical security (raids) is a major threat; unencrypted home servers can become evidence against you.

---

## Why Self-Host in Iran?

1.  **Censorship Resistance:** Your data is accessible even if international internet (the "Global Internet") is throttled or cut off, provided you are within the local network or using resilient protocols.
2.  **Sanctions Evasion:** Avoid sudden account closures by western tech companies complying with sanctions.
3.  **Privacy from Surveillance:** By hosting locally (or on a trusted foreign VPS) with encryption, you prevent domestic ISP snooping and foreign intelligence data mining.

---

## Recommended Hardware

You do not need expensive enterprise gear.

- **Old Laptops:** Excellent choice as they have a built-in UPS (battery) and keyboard/screen for debugging.
- **Single-Board Computers (SBCs):** Devices like Raspberry Pi 4/5 or Odroid. Small, low power, easy to hide.
- **FreedomBox:** A software system designed to run on SBCs to make self-hosting easy for non-experts.

---

## File Synchronization & Storage

These tools replace services like Dropbox or Google Drive.

### Syncthing (Top Recommendation)

**Syncthing** is a continuous file synchronization program. It synchronizes files between two or more computers in real-time.

- **Why it's best for Iran:** It is **Peer-to-Peer (P2P)**. There is no central server to block. Devices communicate directly using TLS encryption. If the internet is cut but you have a local mesh network (e.g., between neighbors via Wi-Fi), Syncthing keeps working.
- **Privacy:** All data is authenticated and encrypted. No data is stored on third-party servers.
- **Usage:** Install on your phone and your home server/laptop. Folders sync automatically.
- **Note:** Syncthing is for _synchronization_, not typically for accessing files via a web browser.

### Nextcloud

**Nextcloud** is a comprehensive productivity suite. It offers file storage (like Dropbox), calendars, contacts, and document editing.

- **Pros:** User-friendly web interface, massive plugin ecosystem (Notes, Tasks, Deck).
- **Cons:** Resource heavy. Requires a web server (Apache/Nginx) and database (MariaDB).
- **Security Warning:** Nextcloud's "End-to-End Encryption" app is often experimental and buggy. **Do not rely on it for critical data.** Instead, rely on **Full Disk Encryption (LUKS)** of the server itself or use **Cryptomator** on the client side before uploading files to Nextcloud.

### Peergos

**Peergos** allows you to store, share, and view photos and documents in a secure web interface.

- **Features:** Built on IPFS (InterPlanetary File System), it offers quantum-resistant encryption and is completely decentralized.
- **Privacy:** It is designed so that even the server admin cannot see the user's data or friend list.

---

## Photo Management

Alternatives to Google Photos or iCloud Photos.

### Ente Photos (Self-Hosted)

**Ente** is an end-to-end encrypted photo management tool. While they offer a cloud service, the server ("Museum") is open source and self-hostable.

- **Security:** Unlike most self-hosted galleries, Ente is **End-to-End Encrypted (E2EE)** by design. Even if your server is compromised, the photos remain encrypted.
- **Features:** Automatic backups from iOS/Android, semantic search (runs locally), and sharing.
- **Complexity:** Requires running MinIO (object storage) and PostgreSQL alongside the Ente server.

### PhotoPrism

**PhotoPrism** is an AI-powered photo app for the decentralized web.

- **Features:** Excellent face recognition and automatic tagging without sending data to Google/Apple.
- **Warning:** **No End-to-End Encryption.** Files are stored unencrypted on the disk. You _must_ run this on a trusted server with full disk encryption.

---

## Anonymous File Sharing

For sharing files with others without revealing your identity or location.

### OnionShare

**OnionShare** lets you securely and anonymously share files, host websites, and chat using the **Tor Network**.

- **How it works:** It creates a temporary `.onion` web address on your computer. The recipient opens this address in Tor Browser to download the file.
- **Relevance to Iran:**
  - **Bypasses NAT/Firewalls:** Works even if you don't have a public IP (which is standard for home users in Iran).
  - **Anonymity:** The regime cannot easily trace who is hosting the file.
  - **Circumvention:** Tor bridges (Snowflake/Meek) are often required to connect to the Tor network from Iran initially.

### PrivateBin

**PrivateBin** is a minimalist, open-source online pastebin where the server has zero knowledge of pasted data.

- **Usage:** Paste text/code, get a link. The data is encrypted/decrypted in the browser. The server only sees encrypted gibberish.
- **Self-Hosting:** Easy to host on a small VPS.

---

## 🇮🇷 Implementation Guide: The Iranian Context

Self-hosting in Iran presents unique challenges regarding connectivity and physical security.

### 1. Connectivity: Bypassing CGNAT and Censorship

Most home internet connections in Iran are behind **CGNAT** (Carrier-Grade NAT), meaning you do not have a public IP address. You cannot simply "open a port" to access your server from outside.

**Solutions:**

- **Tor Onion Services:** Configure your services (Nextcloud/SSH) as a Tor Hidden Service.
  - _Pros:_ Bypasses CGNAT completely; high anonymity; no need for a static IP.
  - _Cons:_ Slow speeds; requires Tor Browser or Tor-aware apps on the client side.
- **Reverse SSH Tunnels:** If you have a cheap VPS outside Iran (and a way to reach it), you can tunnel your home server's traffic to that VPS.
  - _Command:_ `ssh -R 8080:localhost:80 user@foreign-vps-ip`
- **Tailscale / Headscale:** Creates a private mesh VPN.
  - _Note:_ The official Tailscale coordination server might be blocked. **Headscale** is a self-hosted alternative you can run on a VPS to coordinate your devices.

### 2. Hosting Location: Domestic vs. Foreign

- **Home Server (Recommended for Privacy):**
  - _Risk:_ Physical raid/theft. Internet blackouts disconnect you.
  - - Mitigation:\* **Mandatory Full Disk Encryption (LUKS)**. Use a "kill switch" (power off) if raid is imminent.
- **Domestic VPS (ArvanCloud, Parspack, etc.):**
  - _Risk:_ **EXTREME.** Domestic providers are legally required to provide backend access to intelligence services. Traffic is monitored.
  - _Verdict:_ **Never host sensitive data on Iranian domestic cloud providers**, even with encryption. They can snapshot your memory (RAM) and keys.
- **Foreign VPS:**
  - _Risk:_ Payment difficulties (requires crypto/foreign cards), blocking by the Great Firewall (GFW).
  - _Mitigation:_ Use obfuscated protocols (VLESS-Reality, Hysteria2) to tunnel traffic to your VPS.

### 3. Data Encryption Strategy

Because physical seizure of devices is a realistic threat for activists in Iran:

- **At Rest (Disk):** Use **LUKS** (Linux Unified Key Setup) on your server. If the power is pulled, the data is unreadable without the passphrase.
- **At Rest (Cloud/Backup):** If you back up your self-hosted data to a cloud (even a foreign one), use **Cryptomator** or **Restic** to encrypt it client-side first.
- **In Transit:** Always enforce **HTTPS**. Use **Let's Encrypt** for certificates. If using Tor Onion Services, end-to-end encryption is automatic.

### 4. Summary of Recommendations for Iran

| Need              | Recommended Tool       | Configuration Note                                                         |
| :---------------- | :--------------------- | :------------------------------------------------------------------------- |
| **File Sync**     | **Syncthing**          | Enable "Global Discovery"; use local Wi-Fi sync during internet blackouts. |
| **Cloud Storage** | **Nextcloud**          | Access via **Tor Onion Service** or **Headscale** VPN to bypass CGNAT.     |
| **Photos**        | **Ente (Self-Hosted)** | Ensure the server is on LUKS-encrypted storage.                            |
| **Sharing**       | **OnionShare**         | Requires Tor Bridge (Snowflake) to connect initially.                      |

---

_Sources: Privacy Guides, Freedom of the Press Foundation, Security in a Box, Tactical Tech._
