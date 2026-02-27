---
title: "Network Traffic Privacy and VPNs"
tags:
  [
    vpn,
    tor,
    censorship-circumvention,
    iran,
    deep-packet-inspection,
    network-security,
    shadowsocks,
    privacy,
  ]
category: "Circumvention and Counter-Surveillance"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "VPN Protocols",
    "Tor Network",
    "Censorship Resistance",
    "DNS Security",
    "Self-Hosted VPNs",
  ]
summary: "A comprehensive guide to protecting network traffic against surveillance and censorship in Iran. Covers the selection of secure VPNs, self-hosted circumvention tools (Outline, Amnezia), and the use of the Tor network with bridges."
source: "Raaznet Wiki Aggregation"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of internet connectivity",
    "Ability to install software",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-17"
---

# Network Traffic Privacy and VPNs

Network privacy is synonymous with physical safety. The state utilizes sophisticated **Deep Packet Inspection (DPI)** to monitor traffic, identifying and blocking encrypted connections. Furthermore, the implementation of the **National Information Network (NIN)**—a domestic intranet—creates a dual-threat environment where users face both censorship of the global internet and extensive surveillance on domestic traffic.

This guide details how to encrypt your network traffic effectively to bypass censorship and prevent Internet Service Providers (ISPs) and state actors from analyzing your online activity.

---

## 1. Understanding the Threat: What the ISP Sees

Without protection, your ISP (and by extension, the government) can see:

- **DNS Queries:** The names of the websites you visit (e.g., `twitter.com`).
- **IP Addresses:** The destination servers you communicate with.
- **SNI (Server Name Indication):** Even with HTTPS, the initial handshake reveals the domain name in cleartext.
- **Traffic Patterns:** The volume and timing of data, which can reveal the type of activity (e.g., streaming, VoIP calls).

To counter this, we utilize **tunneling** and **encryption** technologies, primarily VPNs and the Tor network.

---

## 2. Virtual Private Networks (VPNs)

A VPN creates an encrypted tunnel between your device and a server outside Iran. It shifts trust from your ISP to the VPN provider.

### The Risks of "Free" VPNs

In Iran, thousands of "free" VPNs circulate on Telegram and third-party app stores. **Avoid these.**

- **Malware:** Many contain spyware used to log user activity.
- **Data Selling:** Free services often monetize by selling user traffic data.
- **State-Run Honeypots:** Some free VPNs are operated by intelligence agencies to identify dissidents.

### Criteria for Choosing a VPN in Iran

When selecting a commercial VPN, ensure it meets these specific requirements:

1.  **Obfuscation/Stealth Protocols:** Standard protocols (OpenVPN, WireGuard) are easily identified and throttled by Iran's DPI. Look for proprietary stealth protocols or support for **V2Ray**, **Shadowsocks**, or **Obfsproxy**.
2.  **No-Logs Policy:** The provider must not store traffic logs. Ideally, this has been verified by a third-party audit or court case.
3.  **Jurisdiction:** The provider should be based in a country with strong privacy laws (e.g., Switzerland, Sweden, Iceland) and outside the "14 Eyes" intelligence alliance.
4.  **Kill Switch:** Essential to cut internet access immediately if the VPN connection drops, preventing data leaks.

### Recommended Commercial Providers

Based on security audits and resilience against censorship:

| Provider       | Key Features for Iran                                                                                           | Payment Anonymity     |
| :------------- | :-------------------------------------------------------------------------------------------------------------- | :-------------------- |
| **Mullvad**    | High transparency, no account required (numbered IDs), supports bridges and obfuscation (Shadowsocks).          | Cash, Monero, Crypto  |
| **IVPN**       | Strong ethics, supports V2Ray obfuscation (Desktop/iOS) to bypass DPI.                                          | Cash, Monero, Bitcoin |
| **Proton VPN** | "Stealth" protocol designed to look like normal HTTPS traffic. Free tier is unlimited (though often congested). | Cash, Bitcoin         |

---

## 3. Self-Hosted and Decentralized Circumvention

When commercial VPN IP addresses are blocked, self-hosted solutions are often the most resilient method for Iranian users. These tools rely on protocols designed specifically to defeat censorship.

### Outline VPN (Shadowsocks)

- **Mechanism:** Uses the Shadowsocks protocol to masquerade internet traffic as random data, making it hard for DPI to identify.
- **Deployment:** Requires a server (VPS) outside Iran. You generate "access keys" to share with trusted circles.
- **Pros:** Highly resilient; widely used in Iran.
- **Cons:** Not a full anonymity tool (the VPS provider sees the traffic).

### Amnezia VPN

- **Mechanism:** An open-source client that simplifies setting up your own VPN on a VPS.
- **Protocols:** Supports **XRay (VLESS)** and **Reality**, which are currently among the most effective protocols for bypassing the Great Firewall of China and Iran's filtering.
- **Pros:** Extremely difficult to detect; user-friendly setup.

### V2Ray / XRay / VLESS

These are the underlying protocols used by many modern circumvention tools ("v2ray configs" shared on Telegram).

- **Warning:** Only use configs from **trusted sources**. Malicious configs can route traffic through compromised servers, exposing your data.

---

## 4. The Tor Network

Tor (The Onion Router) provides anonymity by routing traffic through three random volunteer nodes, encrypting it at each step. Unlike a VPN, no single server knows both who you are and where you are going.

### Tor Bridges (Crucial for Iran)

Direct connections to the Tor network are often blocked in Iran. You must use **Pluggable Transports (Bridges)**:

- **Snowflake:** Makes Tor traffic look like a WebRTC video call. Very effective in Iran.
- **obfs4:** Makes traffic look like random, unreadable data.

### Accessing Tor

- **Desktop:** Use the official **Tor Browser**. Configure bridges via _Settings > Connection > Bridges > Select a Built-in Bridge_.
- **Android:** Use **Tor Browser** (official) or **Orbot** (routes other apps through Tor).
- **iOS:** Use **Onion Browser** (limited privacy compared to desktop) or **Orbot**.

> **Security Note:** Do not use Tor for banking or logging into accounts tied to your real identity (like government portals), as this can flag your account for fraud or de-anonymize you through behavioral analysis.

---

## 5. DNS Security (DoH / DoT)

DNS manipulation is a common censorship tactic. Even with a VPN, DNS leaks can expose your browsing history to the ISP.

- **DNS over HTTPS (DoH) / DNS over TLS (DoT):** Encrypts DNS queries so the ISP cannot see or spoof them.
- **Implementation:**
  - Enable "Secure DNS" in browser settings (Firefox/Chrome/Brave).
  - Use tools like **RethinkDNS** (Android) or **DNSCrypt-Proxy** (Desktop) to force encrypted DNS system-wide.
  - **Note:** Encrypted DNS alone bypasses basic blockages but does _not_ hide your IP address or bypass IP-based blocking.

---

## 6. Advanced Configuration & Risks

### VPN Over Tor vs. Tor Over VPN

- **Tor over VPN (You -> VPN -> Tor -> Internet):** The most common setup. Hides Tor usage from your ISP. Useful if using Tor is criminalized or flagged.
- **VPN over Tor:** Generally not recommended due to performance issues and complexity, unless accessing specific `.onion` sites that require IP stability.

### The "TunnelVision" Vulnerability (CVE-2024-3661)

A technique where attackers on the local network (e.g., a compromised ISP router) can force traffic outside the VPN tunnel using DHCP Option 121.

- **Mitigation:** Android is immune. On Windows/Linux/macOS, ensure your VPN client has a strict **Kill Switch** and firewall rules that block non-VPN traffic.

### Split Tunneling Risks

Split tunneling allows some apps to bypass the VPN.

- **In Iran:** Useful for accessing banking apps or domestic services (Snapp, Divar) that block foreign IPs.
- **Risk:** Ensure sensitive apps (Browsers, Telegram, Instagram, Signal) are **never** excluded from the VPN tunnel.

---

## 7. Operational Security Checklist

1.  **Verify the Blockage:** Before assuming censorship, check [OONI Explorer](https://ooni.org/) or use a different connection to confirm the site is down.
2.  **Test for Leaks:** Visit [browserleaks.com](https://browserleaks.com) while connected.
    - **IP Leak:** Ensure your real Iranian IP is not visible.
    - **DNS Leak:** Ensure the DNS servers detected belong to your VPN provider, not an Iranian ISP (e.g., MCI, Irancell).
    - **WebRTC Leak:** Disable WebRTC in your browser if your real IP is exposed.
3.  **Kill Switch:** Always enable the VPN Kill Switch ("Block connections without VPN") to prevent accidental exposure during disconnections.
4.  **Protocol Hopping:** If one protocol (e.g., OpenVPN UDP) stops working, switch to another (e.g., WireGuard or Stealth).

---

## 8. Summary of Tools

| Need                                | Recommended Tool                                                                    |
| :---------------------------------- | :---------------------------------------------------------------------------------- |
| **High Anonymity / Whistleblowing** | **Tor Browser** (Desktop) with Snowflake bridge.                                    |
| **Daily Circumvention (Mobile)**    | **Mullvad** or **IVPN** (if paid); **Orbot** (free).                                |
| **Bypassing Severe Blocking**       | **AmneziaWG**, **V2RayNG** (Android), **V2Box** (iOS) with trusted private configs. |
| **Sharing Access with Family**      | **Outline VPN** (Self-hosted).                                                      |

_This guide aggregates data from Privacy Guides, Security in a Box, and Freedom of the Press Foundation, localized for the Iranian digital landscape._
