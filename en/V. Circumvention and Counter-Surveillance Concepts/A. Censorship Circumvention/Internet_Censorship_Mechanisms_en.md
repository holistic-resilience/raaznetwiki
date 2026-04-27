---
title: "Internet Censorship Mechanisms in Iran"
tags: [censorship, iran, nin, dpi, filtering, infrastructure, internet-shutdown]
category: "Foundational Concepts"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Technical Users]
topics:
  [
    "National Information Network",
    "Deep Packet Inspection",
    "Protocol Filtering",
    "Throttling",
  ]
summary: "A comprehensive technical overview of how the Islamic Republic of Iran implements internet censorship, including the National Information Network (NIN), DPI, and protocol whitelisting."
source: "Raaznet Aggregated Research"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites:
  [
    "Basic understanding of internet connectivity",
    "Familiarity with network terms (IP, DNS)",
  ]
estimated_read_time: "15 minutes"
---

# Internet Censorship Mechanisms in Iran

To effectively bypass censorship, one must first understand how the censorship apparatus functions. The Islamic Republic of Iran operates one of the most sophisticated and centralized content control systems in the world, often referred to as the **"Filternet."**

This guide explains the technical infrastructure of Iran's internet, the specific mechanisms used to block content, and how authorities isolate Iranian users from the global web.

## 1. The Infrastructure: Centralized Control

Unlike many countries where Internet Service Providers (ISPs) connect directly to various global networks, Iran's internet architecture is highly centralized.

### The TIC Choke Point

All international traffic entering or leaving Iran must pass through the **Telecommunication Infrastructure Company (TIC)**. The TIC is a state-owned monopoly under the Ministry of Information and Communication Technology (ICT).

- **Centralization:** Because all traffic funnels through TIC gateways, the state has a "kill switch" capability and can apply uniform filtering rules across all ISPs (e.g., Irancell, MCI, Shatel).
- **Surveillance:** This centralization allows for the efficient deployment of Deep Packet Inspection (DPI) equipment on the country's main digital borders.

### The National Information Network (NIN)

Often called the "Halal Internet" or **SHOMA**, the NIN is an isolated domestic intranet designed to function independently of the global internet.

- **Dual-Stack Architecture:** Iranian users are effectively on two networks simultaneously: the global internet and the domestic NIN.
- **The "Shutdown" Strategy:** During protests, authorities can sever connections to the global internet while keeping the NIN operational. This keeps domestic banking, government services, and approved apps (like domestic messengers) running, minimizing economic damage while cutting off communication with the outside world.
- **Price Discrimination:** To encourage users to stay within the NIN, traffic to domestic websites is often priced significantly lower (e.g., 50% cheaper) than international traffic.

---

## 2. Core Blocking Mechanisms

The Iranian censorship apparatus uses a "defense-in-depth" approach, employing multiple layers of blocking to ensure users cannot access restricted content.

### A. DNS Hijacking and Poisoning

The Domain Name System (DNS) is the internet's phonebook, translating names like `google.com` into IP addresses like `142.250.1.1`.

- **The Mechanism:** When you request a blocked site, the ISP's DNS server intercepts the request and returns a false IP address (often redirecting to a rigid "peyvandha" block page) or no address at all (NXDOMAIN).
- **The Countermeasure:** Using encrypted DNS (DoH/DoT) can bypass this, but Iran has begun targeting these protocols as well (see section 4).

### B. IP Address Blocking (Blackholing)

Authorities maintain extensive lists of IP addresses associated with banned websites, VPN servers, and Tor nodes.

- **The Mechanism:** Routers at the TIC gateway simply drop packets destined for these IPs.
- **Target:** This is the primary method used to block known VPN servers and public proxies.

### C. Deep Packet Inspection (DPI)

DPI is the most advanced tool in Iran's arsenal. Unlike standard routing which looks only at the "envelope" (IP header), DPI opens the "envelope" to inspect the contents.

- **Keyword Filtering:** DPI scans unencrypted HTTP traffic for sensitive keywords (e.g., "protest," "human rights"). If found, the connection is reset (RST packet injection).
- **SNI Filtering:** For encrypted HTTPS traffic, the DPI system cannot read the content, but it can read the **Server Name Indication (SNI)** in the initial TLS handshake. This tells the censor which website you are trying to visit (e.g., `youtube.com`) before the encryption is established.
- **Protocol Identification:** DPI analyzes traffic patterns to identify VPN protocols (like OpenVPN, WireGuard, or Shadowsocks). If traffic looks like a VPN, it is dropped.

### D. Throttling (Bandwidth Shaping)

Instead of blocking a service outright, authorities may deliberately slow it down to the point of usability.

- **The Mechanism:** The TIC limits the bandwidth available for encrypted traffic or specific foreign connections.
- **The Goal:** To frustrate users into switching to fast, unencrypted domestic alternatives without technically "blocking" the service, which provides plausible deniability.

---

## 3. Advanced Repression Techniques (2024-2025 Context)

As circumvention tools have evolved, so has the censorship. Recent years have seen the deployment of aggressive new tactics.

### Protocol Whitelisting

In times of high tension, authorities switch from "blocking bad traffic" to "blocking everything except good traffic."

- **The Mechanism:** The firewall drops **all** packets that do not match a strict whitelist of approved protocols (specifically DNS, HTTP, and HTTPS).
- **Impact:** This effectively kills standard VPNs, UDP-based traffic (like gaming or VoIP), and random-port communications. Only tools that can perfectly camouflage themselves as standard HTTPS (e.g., V2Ray/VMess with WebSocket + TLS) can survive this.

### Blocking Encrypted Client Hello (ECH)

To fix the SNI privacy leak (mentioned in section 2C), the tech industry introduced **Encrypted Client Hello (ECH)**.

- **The Censorship:** Iran actively blocks ECH. Since ECH relies on encrypted DNS to distribute keys, the censor blocks the encrypted DNS requests or drops the specific ECH-enabled handshake packets. This forces browsers to fall back to cleartext SNI, which can then be filtered.

### Active Probing

Authorities actively hunt for private VPN servers.

- **The Mechanism:** If the censorship system sees a connection to an unknown server that _might_ be a VPN (e.g., a Shadowsocks server), it sends its own "probe" packets to that server.
- **The Trap:** If the server responds in a way that confirms it is running VPN software, the server's IP is immediately added to the national blocklist.
- **Countermeasure:** Modern tools utilize "probe resistance" (e.g., falling back to a fake website if the password is incorrect) to defeat this.

---

## 4. Diagnostics: Am I Blocked?

Understanding whether you are facing a censorship block or a technical failure is crucial for troubleshooting.

| Symptom                       | Probable Cause                                               | Diagnostic Tool                                 |
| :---------------------------- | :----------------------------------------------------------- | :---------------------------------------------- |
| **"Connection Reset" Error**  | DPI is likely terminating the connection (RST injection).    | Browser Developer Tools (Network Tab)           |
| **Redirect to `10.10.34.34`** | You have hit the standard government block page (Peyvandha). | Check URL bar                                   |
| **Slow, crawling speed**      | Throttling or UDP blocking (packet loss).                    | Speed test (compare domestic vs. international) |
| **Timeout (No response)**     | IP Blocking (Blackholing).                                   | Ping / Traceroute                               |

### Tools for Verification

- **OONI Probe:** A mobile and desktop app that tests blocking of websites and apps. It provides data on _how_ a site is blocked (DNS, TCP, or HTTP).
- **MTR (My Traceroute):** Helps identify where in the path packets are being dropped (e.g., if they die immediately at the Iran gateway).

## Summary

The Iranian censorship system is not a static wall but a dynamic, intelligent adversary. It combines the brute force of IP blocking with the precision of DPI and the strategic isolation of the NIN. Successful circumvention requires tools that mask the **destination** (IP/SNI), hide the **protocol** (Obfuscation), and resist **active probing**.

**Related Concepts:**

- [Comprehensive VPN Guide](vpn-comprehensive-guide)
- [Tor and Anonymity Networks](anonymity-networks-tor-and-i2p)
- [Alternative Access Methods](alternative-access-and-self-hosting)
