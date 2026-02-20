---
title: "Internet Architecture and Censorship Mechanisms"
tags:
  [
    iran-internet,
    censorship,
    dpi,
    nin,
    shoma,
    surveillance,
    network-architecture,
    infrastructure,
  ]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience:
  [General Public, Activists, Privacy-Conscious Users, Network Administrators]
topics:
  [
    "National Information Network",
    "Deep Packet Inspection",
    "DNS Hijacking",
    "Internet Shutdowns",
    "Throttling",
  ]
summary: "A comprehensive analysis of Iran's internet infrastructure, the National Information Network (SHOMA), and the technical mechanisms used by the state to filter, throttle, and monitor connectivity."
source: "Raaznet Aggregated Research"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites:
  [
    "Basic understanding of IP addresses and DNS",
    "Familiarity with how a browser loads a webpage",
  ]
estimated_read_time: "12 minutes"
last_updated: "2026-02-17"
---

# Internet Architecture and Censorship Mechanisms

## Overview: The Dual Network

The internet landscape in Iran is fundamentally different from most of the world. While users perceive a single "Internet," they are actually navigating a dual-layer system designed by the state to prioritize control and surveillance.

1.  **The Global Internet:** The unrestricted web (Google, Wikipedia, international news). Access to this layer is heavily restricted, throttled, and monitored.
2.  **The National Information Network (NIN):** Often referred to as **SHOMA** or the "Halal Internet." This is a domestic intranet that hosts Iranian websites, banking services, and government portals. It is designed to function independently of the global internet, allowing the state to cut off international access while keeping domestic services online.

To understand how to bypass censorship, one must first understand the architecture that enforces it.

---

## 1. The Architecture of Control

Unlike decentralized networks in other countries, Iran’s internet infrastructure is highly centralized to facilitate state control.

### The Gatekeeper: TIC

The **Telecommunication Infrastructure Company (TIC)** is the state monopoly under the Ministry of ICT. It is the _only_ entity legally allowed to buy bandwidth from the outside world and distribute it into Iran.

- **Choke Point:** All international traffic entering or leaving Iran must pass through TIC's gateways. This creates a single choke point where the state can implement nationwide filtering or shutdowns.

### The Enforcers: ISPs and Mobile Operators

Internet Service Providers (ISPs) like **Irancell**, **MCI (Hamrah-e Aval)**, and **Shatel** do not connect directly to the global internet. They purchase bandwidth from the TIC.

- **Delegated Censorship:** While TIC handles the main gateway, local ISPs are required to install equipment (often referred to as "Siam" or censorship boxes) that allows intelligence agencies to monitor and filter traffic at the consumer level.

### The Facilitator: Content Delivery Networks (CDNs)

Domestic cloud providers (such as **Arvan Cloud**) play a critical role in the NIN. By hosting major Iranian websites locally, they allow the government to sever international connections without crashing the country’s internal economy (banks, taxis, government services).

---

## 2. Technical Mechanisms of Censorship

The Islamic Republic employs a multi-layered approach to blocking content. If one method fails, another catches the traffic.

### A. DNS Hijacking and Poisoning

The Domain Name System (DNS) is the phonebook of the internet, translating names (like `youtube.com`) into IP addresses.

- **The Mechanism:** When a user in Iran requests a banned domain, the ISP’s DNS server intercepts the request and returns a false IP address.
- **The "10.10.34.34" Sign:** Frequently, banned domains resolve to the private IP address `10.10.34.34` (or similar internal IPs), which hosts a standardized block page.
- **Countermeasure:** Users often switch to encrypted DNS (DoH/DoT) to bypass this, but the state has begun blocking widely used DoH providers (like Cloudflare or Google) to force users back to ISP-controlled DNS.

### B. IP Address Blocking

The most basic form of censorship involves blacklisting specific IP addresses or entire ranges (subnets) associated with foreign hosting providers.

- **Collateral Damage:** This method is "messy." By blocking a range of IPs belonging to DigitalOcean or AWS to stop a VPN, the state often accidentally blocks innocent websites hosted on the same infrastructure.

### C. Deep Packet Inspection (DPI)

This is the most sophisticated tool in Iran's arsenal. Unlike simple IP blocking, DPI looks _inside_ the data packets traveling through the network.

- **SNI Filtering:** Even with HTTPS encryption, the initial "handshake" between a user and a server (specifically the **Server Name Indication** or SNI field) is unencrypted. DPI boxes read this field. If it contains `twitter.com` or `bbc.com`, the connection is immediately dropped (TCP Reset).
- **Protocol Fingerprinting:** DPI analyzes traffic patterns to identify VPN protocols. If a connection looks like OpenVPN, WireGuard, or Tor, the firewall drops the packets, regardless of the destination.

### D. Throttling and QoS Manipulation

Instead of blocking a service outright, the state often makes it unusable.

- **Bandwidth Throttling:** Encrypted traffic (which the state cannot read) is often deprioritized. A user might have a 100 Mbps connection to an Iranian site (NIN), but only 128 Kbps to an international VPN server.
- **Packet Loss Injection:** The firewall intentionally drops a percentage of packets for encrypted connections, causing constant buffering and timeouts, frustrating the user into giving up.

---

## 3. Surveillance and Monitoring

Censorship stops you from seeing content; surveillance watches what you see.

### ISP Data Retention

By law, Iranian ISPs must log and retain user data for at least six months (often longer). This includes:

- IP addresses assigned to the user.
- Timestamps of connections.
- List of domains visited (if using ISP DNS or HTTP).
- Mobile location data (Cell-ID).

### Active Probing

When the firewall detects a suspicious server (e.g., a private Shadowsock server), it may send its own "probe" packets to that server to see how it responds. If the server replies in a way that confirms it is a VPN, the IP is immediately blacklisted.

### SSL Stripping / MITM Attacks

While less common due to modern browser security (HSTS), state actors occasionally attempt Man-in-the-Middle (MITM) attacks. By tricking a user's browser into using HTTP instead of HTTPS, they can read passwords and messages in plain text.

---

## 4. Internet Shutdowns: The "Kill Switch"

When civil unrest occurs, the state escalates from filtering to disconnection.

### The "White-Listing" Model

During major shutdowns (like in 2019 or 2022), the internet is not simply "unplugged."

- **The Intranet Remains:** The NIN remains active. Users can open Iranian apps, transfer money, and visit government sites.
- **The Global Cut:** International traffic is dropped at the TIC gateway.
- **Selective Access:** A "White List" exists for critical infrastructure. Hospitals, banks, and certain government-aligned news agencies retain access to the global internet, while the general public is cut off.

### Mobile Data Blackouts

Shutdowns often start with mobile data (4G/LTE) in specific neighborhoods where protests are happening. This is a localized tactic to stop video uploads while keeping landline businesses operational.

---

## Summary of Threats

| Mechanism         | What it does                                   | Impact on User                                            |
| ----------------- | ---------------------------------------------- | --------------------------------------------------------- |
| **DNS Hijacking** | Redirects valid URLs to a block page.          | "Site not found" or standard filtering page.              |
| **SNI Blocking**  | Reads the domain name during HTTPS handshake.  | Connection resets immediately when loading a secure site. |
| **Throttling**    | Slows down encrypted/international traffic.    | VPNs connect but are too slow to use.                     |
| **NIN Isolation** | Cuts global internet, leaves local net active. | Only Iranian sites load; "Global internet is down."       |

**Next Steps for Users:**
To bypass these sophisticated architectures, users must move beyond simple proxies. Refer to the _Circumvention and Counter-Surveillance_ section for guides on **Obfuscation**, **Encrypted DNS**, and **Decentralized Storage**.
