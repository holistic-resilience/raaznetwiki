---
title: "Internet Architecture and Censorship Mechanics"
tags:
  [
    internet-infrastructure,
    censorship,
    surveillance,
    dpi,
    dns,
    encryption,
    iran-internet,
    network-security,
  ]
category: "Technical Foundations"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Technical Users]
topics:
  [
    "Network Architecture",
    "Censorship Methods",
    "Surveillance Mechanisms",
    "National Information Network",
  ]
summary: "A technical overview of how the internet functions, how the Iranian regime intercepts and blocks traffic, and the theoretical foundations of circumvention."
source: "RaazNet Aggregated Knowledge"
content_type: "Educational Guide"
security_level: "Essential"
language: "English"
prerequisites: ["Basic Computer Literacy"]
estimated_read_time: "12 minutes"
last_updated: "2026-02-12"
---

# Internet Architecture and Censorship Mechanics

To effectively bypass censorship and protect one's privacy in Iran, it is essential to understand how the internet functions and where the regime's control mechanisms are physically and digitally located. This guide demystifies the path your data takes and explains the specific technologies used by the Islamic Republic to monitor, filter, and throttle connections.

## The Path of Data: Information in Motion

The internet is not a cloud; it is a physical network of cables, routers, and servers. When you access a website or send a message, your data travels through specific "choke points" where surveillance and censorship occur.

### The Connection Chain

1.  **Your Device:** The starting point (phone, laptop).
2.  **Local Network (LAN/Wi-Fi):** Your home router or public Wi-Fi access point.
3.  **Internet Service Provider (ISP):** Companies like Irancell, MCI, Shatel, or Mokhaberat. In Iran, all ISPs are required by law to implement state-mandated filtering and logging.
4.  **The Gateway (TIC):** All international traffic in Iran passes through the **Telecommunication Infrastructure Company (TIC)**. This is the digital border control of the country where the heaviest censorship (The Great Firewall of Iran) is applied.
5.  **The Internet Backbone:** The global network of fiber optic cables.
6.  **Destination Server:** The computer hosting the website or service (e.g., Google, Instagram, or a VPN server).

### Vulnerability Points

- **Local Network:** Vulnerable to nearby eavesdroppers.
- **ISP & TIC:** The primary adversaries. They have full visibility of unencrypted traffic and metadata of encrypted traffic. They utilize **Deep Packet Inspection (DPI)** to analyze traffic contents and headers.

---

## Iran's National Information Network (NIN)

The Islamic Republic has developed an intranet known as the **National Information Network (NIN)** (often referred to as "SHOMA" or the "Halal Internet").

### Strategic Goal

The NIN is designed to allow the government to cut off access to the global internet (International connectivity) while keeping domestic services (banking, government portals, internal messaging apps) operational. This allows for "internet shutdowns" that cripple communication with the outside world without collapsing the internal economy.

### Implications for Users

- **Split Tunneling Risks:** Domestic apps often require direct connections, while international apps require a VPN. Using them simultaneously can lead to leaks.
- **Traffic Differentiation:** ISPs offer cheaper rates for domestic traffic to incentivize users to stay within the NIN, where surveillance is absolute.

---

## Mechanics of Censorship

The regime uses a multi-layered approach to block access to information. Understanding these methods helps in selecting the right circumvention tools.

### 1. DNS Tampering (The Phonebook Attack)

When you type a domain (e.g., `youtube.com`), your device asks a DNS server for the IP address.

- **The Attack:** Iranian ISPs intercept this request and return a fake IP address (DNS Spoofing) or no address at all (DNS Blocking).
- **The Countermeasure:** Using **Encrypted DNS** (DoH - DNS over HTTPS, or DoT - DNS over TLS). This encrypts the lookup so the ISP cannot see what domain you are resolving.

### 2. IP Blocking (Blackholing)

The firewall contains a list of IP addresses belonging to banned services (e.g., Telegram servers, known VPN nodes).

- **The Attack:** The gateway simply drops all packets destined for these IPs.
- **The Countermeasure:** Rotating proxies and VPNs that frequently change their IP addresses or use "residential" IPs that are harder to ban.

### 3. Deep Packet Inspection (DPI)

This is the most advanced tool in the regime's arsenal. Unlike simple IP blocking, DPI examines the _content_ and _metadata_ of the data packets as they pass through.

- **SNI Filtering:** Even if traffic is encrypted (HTTPS), the initial "handshake" often contains the **Server Name Indication (SNI)** in plain text, revealing the website you are visiting.
- **Protocol Recognition:** DPI analyzes traffic patterns (packet size, timing) to identify VPN protocols (like OpenVPN or WireGuard) and block them, even if the data itself is encrypted.
- **The Countermeasure:**
  - **Obfuscation:** Making VPN traffic look like normal HTTPS browsing (e.g., using Shadowsocks, V2Ray/VMess, or Obfs4).
  - **ECH (Encrypted Client Hello):** A newer technology that encrypts the SNI, preventing the ISP from seeing the destination domain during the handshake.

### 4. Throttling and Bandwidth Shaping

Instead of a hard block, the regime often degrades the quality of encrypted connections to make them unusable.

- **The Method:** The ISP detects encrypted tunneling protocols and deliberately slows them down, causing timeouts and disconnections.

---

## Mechanics of Surveillance

Surveillance is distinct from censorship; one stops you from speaking, the other watches what you say.

### 1. Metadata Analysis

Even with end-to-end encryption (like Signal or WhatsApp), the ISP can see **metadata**:

- **Who:** Your IP address and the IP address of the server you are talking to.
- **When:** Time and duration of the connection.
- **How Much:** The volume of data transferred.
- _Inference:_ By correlating these data points, intelligence agencies can deduce relationships and activities.

### 2. Man-in-the-Middle (MitM) Attacks

The regime may attempt to insert itself between you and the destination.

- **Certificate Injection:** A user might be tricked into installing a government "root certificate" (often required for university or office networks). This allows the attacker to decrypt HTTPS traffic, read it, re-encrypt it, and send it on.
- **Warning:** Never install custom root certificates on your personal devices unless you strictly trust the issuer.

### 3. Active Probing

When the Great Firewall detects a suspicious connection (like a ShadowSocks server), it may send its own "probes" to that server to see if it responds like a proxy. If it does, the server is blocked.

---

## Technical Foundations of Circumvention

To defeat these systems, digital safety tools rely on three core concepts:

### 1. Tunneling (The Pipe)

Tunneling wraps your data packets inside another protocol. It creates a direct, virtual link between your device and a server outside Iran.

- **Goal:** To bypass the local ISP's routing rules and exit to the free internet from a different jurisdiction.

### 2. Encryption (The Envelope)

Encryption scrambles the data so that any interceptor (ISP or TIC) sees only gibberish.

- **Transport Encryption:** Protects data from your device to the VPN server (e.g., WireGuard, OpenVPN).
- **End-to-End Encryption (E2EE):** Protects data from your device to the recipient's device (e.g., Signal, PGP). Even the VPN provider cannot read E2EE data.

### 3. Obfuscation (The Camouflage)

Because Iran uses DPI to block standard tunnels, **Obfuscation** is critical. It modifies the "fingerprint" of the data packets to make them look like harmless traffic (usually standard HTTPS web browsing or video streaming).

- **Pluggable Transports:** Tools like **Snowflake** or **v2ray-plugin** disguise traffic to fool the firewall.

## Summary Checklist for Iranian Users

When configuring your digital defense, ensure your strategy addresses all layers:

1.  **DNS:** Is your DNS request encrypted? (Use DoH/DoT).
2.  **SNI:** Is your destination domain visible? (Use tools with ECH or obfuscation).
3.  **Protocol:** Is your VPN protocol identifiable? (Avoid raw OpenVPN; use obfuscated protocols).
4.  **Metadata:** Are you leaking your location? (Use a VPN/Tor to mask your IP).
5.  **Trust:** Do you trust the network provider? (Assume all Iranian ISPs are compromised).

## Related Topics

- [[DNS_Protocols_and_Privacy]]
- [[Tor_and_Anonymity_Networks]]
- [[VPN_Technology_and_Providers]]
- [[Secure_Browsing_and_Web_Hygiene]]
