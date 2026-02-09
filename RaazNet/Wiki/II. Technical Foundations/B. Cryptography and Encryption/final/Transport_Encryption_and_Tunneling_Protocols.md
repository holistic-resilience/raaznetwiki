---
title: "Transport Encryption and Tunneling Protocols"
tags:
  [
    encryption,
    tls,
    vpn,
    tunneling,
    v2ray,
    shadowsocks,
    tor,
    censorship-circumvention,
    iran,
    dpi,
    https,
  ]
category: "Technical Foundations"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users]
topics:
  [
    "Data in Transit",
    "Network Security",
    "Censorship Circumvention",
    "Deep Packet Inspection",
  ]
summary: "A comprehensive guide to how data is secured in transit, covering TLS/SSL, standard VPN protocols, and advanced obfuscation methods (V2Ray, Reality, Shadowsocks) necessary to bypass Iranian censorship."
source: "Raaznet Aggregation"
content_type: "Technical Guide"
security_level: "Essential"
language: "English"
prerequisites:
  [
    "Basic understanding of internet connectivity",
    "Familiarity with VPN concepts",
  ]
estimated_read_time: "12 minutes"
---

# Transport Encryption and Tunneling Protocols

Understanding how data moves across the internet is a matter of safety and accessibility. **Transport Encryption** ensures that data moving between your device and a server cannot be read by intermediaries (like the Telecommunication Company of Iran - TCI, or mobile operators like MCI and Irancell). **Tunneling Protocols** allow you to encapsulate that traffic to bypass censorship filters and hide your destination.

This guide details the mechanisms of secure data transport and the specific protocols required to circumvent the Islamic Republic's Deep Packet Inspection (DPI) systems.

---

## 1. Transport Encryption: Securing Data in Motion

Data "in motion" refers to information traveling over a network. Without encryption, this data is sent in "plaintext," allowing Internet Service Providers (ISPs) and surveillance agencies to read emails, passwords, and browsing history.

### HTTPS and TLS (Transport Layer Security)

The foundation of secure web browsing is **TLS** (the successor to SSL). When you visit a website starting with `https://`, TLS encrypts the communication.

- **How it works:** Your browser and the server perform a "handshake" to agree on encryption keys. Once established, the content of the communication is encrypted.
- **What it hides:** The specific pages you visit (e.g., `youtube.com/watch?v=123`), your passwords, and the content of forms.
- **What it does NOT hide:** The **SNI (Server Name Indication)**. Even with HTTPS, the ISP knows you are connected to `youtube.com`, even if they cannot see the video you are watching.

### The Iranian Context: SNI Filtering and MITM

The Islamic Republic uses **SNI Filtering** to block websites. By reading the unencrypted "Hello" packet at the start of a TLS connection, the firewall sees the destination domain and terminates the connection if it is blacklisted.

**Advanced Defense: Encrypted Client Hello (ECH)**
To counter SNI filtering, modern protocols are adopting ECH (formerly ESNI). ECH encrypts the SNI extension, preventing the ISP from seeing which specific website hosted on a Cloudflare or CDN IP you are trying to visit.

- _Status:_ While powerful, Iran's firewall aggressively blocks ECH handshakes or throttles connections that use it. Disabling or enabling ECH may be necessary depending on the specific blocking method of the day.

**Man-in-the-Middle (MITM) Attacks**
Iranian state actors have historically attempted to issue fake digital certificates to intercept encrypted traffic.

- **Defense:** Modern browsers use "Certificate Transparency" logs and pinning. Always heed browser warnings if you see "Connection is not private." Never install "root certificates" demanded by Iranian apps or domestic services, as this grants them the ability to decrypt your HTTPS traffic.

---

## 2. Standard VPN Protocols

Virtual Private Networks (VPNs) create an encrypted tunnel between your device and a server outside Iran. However, not all VPN protocols are equal in the face of censorship.

### OpenVPN (TCP/UDP)

An open-source, highly secure industry standard.

- **Pros:** Audited security, strong encryption (AES-256).
- **Cons in Iran:** **Highly Detectable.** The "handshake" of OpenVPN is easily identified by DPI systems. Using standard OpenVPN in Iran usually results in severe throttling or a complete connection reset.

### WireGuard

A modern, lightweight, and extremely fast protocol.

- **Pros:** High performance, instant connection, battery-efficient for mobile.
- **Cons in Iran:** WireGuard was designed for speed, not stealth. Its traffic pattern is distinct and easily blocked by the Great Firewall. It generally requires an obfuscation layer (like UDP2RAW or Shadowsocks) to work in Iran.

### IKEv2 / IPsec

Common on iOS and corporate networks.

- **Status in Iran:** Frequently blocked on mobile networks (MCI/Irancell) but occasionally works on home DSL/FTTH during periods of lower censorship. Not recommended for critical anonymity due to closed-source implementations on some platforms.

---

## 3. Stealth and Obfuscation Protocols (Censorship Circumvention)

Because standard protocols (OpenVPN/WireGuard) are easily blocked, Iranian users must rely on **Obfuscated Tunneling Protocols**. These protocols disguise VPN traffic to look like normal web traffic (HTTPS), making it difficult for the regime to block without shutting down the entire internet.

### Shadowsocks

Originally developed to bypass China's firewall, Shadowsocks is a secure SOCKS5 proxy.

- **Mechanism:** It encrypts traffic but does not strip headers like a VPN. It is lighter and faster.
- **Evolution:** Standard Shadowsocks is now often detected by active probing.
- **Current State:** Must be used with plugins like **v2ray-plugin** or **Cloak** to remain effective in Iran.

### V2Ray (VMess / VLESS)

Part of Project V, V2Ray is a sophisticated platform for building proxies.

- **VMess:** The classic protocol. It relies on system time being synchronized.
- **VLESS:** A lightweight version of VMess without its own encryption (relying on the underlying TLS instead), reducing overhead.
- **Importance:** Widely used in Iran via clients like **v2rayNG** (Android), **V2Box** (iOS), and **Nekoray** (PC).

### Xray and "Reality" (The Current Gold Standard)

Xray is a superset of V2Ray. Its protocol, **VLESS-XTLS-Reality**, is currently one of the most effective methods for bypassing the National Information Network (NIN).

- **How "Reality" Works:** It mimics a connection to a real, high-reputation foreign website (like Microsoft, Yahoo, or Amazon). It steals the TLS handshake of that site to fool the censor into thinking you are browsing a legitimate, allowed website.
- **Why it works in Iran:** It eliminates the need for the user to buy a domain name, and it is extremely resistant to active probing by the censor.

### Trojan

Trojan is designed to look exactly like an HTTPS server.

- **Mechanism:** If the firewall probes a Trojan server, it responds with a valid-looking 404 page or a fake website. If the correct password (hash) is provided, it tunnels the traffic.
- **Trojan-Go:** An enhanced version often used to tunnel via Cloudflare (CDN) to hide the server IP address.

---

## 4. Tor and Onion Routing

Tor (The Onion Router) routes traffic through three random volunteer nodes (Guard, Middle, Exit), encrypting the data at each step.

### Anonymity vs. Speed

Tor provides the highest level of **anonymity** (hiding _who_ you are), whereas VPNs/Proxies primarily provide **privacy** (hiding _what_ you do) and **circumvention**.

- **Warning:** Tor is slow. It is ideal for whistleblowing, secure text communication, and reading static pages, but poor for video streaming.

### Connecting to Tor in Iran

Direct connections to the Tor network are blocked. You **must** use Pluggable Transports (Bridges):

1.  **Obfs4:** Obfuscates Tor traffic to look like random data. Often blocked in Iran.
2.  **Snowflake:** Uses ephemeral WebRTC proxies run by volunteers in free countries. **Highly recommended for Iran.** It is difficult to block because the entry points change constantly.
3.  **WebTunnel:** A newer bridge type that mimics HTTPS traffic (similar to how Trojan/VLESS works).

> **OpSec Note:** Do not use Tor with a full-screen browser window, as this can leak your screen resolution and fingerprint. Use the Tor Browser defaults.

---

## 5. SSH Tunneling

Secure Shell (SSH) is a standard tool for managing servers, but it can act as an encrypted SOCKS proxy (`ssh -D`).

- **Usage:** During times of heavy "internet shutdown" where only domestic intranet is available, users sometimes tunnel traffic through a domestic VPS which then tunnels to a foreign VPS.
- **Risk:** The protocol is easily identified. While encrypted, the _pattern_ of using SSH for high-bandwidth tunneling is detectable by traffic analysis algorithms.

---

## 6. Selection Strategy for Iranian Users

The digital battlefield in Iran changes daily. A protocol that works today may be blocked tomorrow.

| Requirement                | Recommended Protocol                   | Client Examples             |
| :------------------------- | :------------------------------------- | :-------------------------- |
| **High Speed / Streaming** | VLESS-Reality, Trojan                  | v2rayNG, Streisand, Hiddify |
| **Maximum Anonymity**      | Tor + Snowflake/WebTunnel              | Tor Browser, Orbot          |
| **Backup / Stability**     | Shadowsocks + Cloak                    | Shadowsocks client          |
| **Standard VPN**           | WireGuard (Only if wrapped in UDP2RAW) | TunSafe (modified configs)  |

### Critical Security Warnings

1.  **Avoid "Free" VPN Apps:** Most free VPNs on the Play Store/App Store collect user data, sell bandwidth, or are honey-pots operated by intelligence services. If you are not paying for the product (or setting up your own server), you are the product.
2.  **Kill Switch:** Always enable the "Always-on VPN" or "Block connections without VPN" feature in your OS settings. This prevents your real IP from leaking if the tunnel drops.
3.  **DNS Leaks:** Ensure your tunneling tool handles DNS requests. If your traffic is encrypted but your DNS requests go to TCI/MCI, the government knows exactly which sites you are visiting.

## Related Topics

- [[Understanding Digital Surveillance]]
- [[Network and Internet Concepts]]
- [[Censorship Circumvention]]
