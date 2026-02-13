---
title: "DNS Protocols and Privacy"
tags:
  [dns, doh, dot, encryption, privacy, censorship-circumvention, iran-internet]
category: "Network and Internet Concepts"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users]
topics:
  [
    "DNS Security",
    "Encrypted DNS",
    "Censorship Circumvention",
    "Network Privacy",
  ]
summary: "A comprehensive guide to understanding DNS, its role in censorship and surveillance in Iran, and how to use encrypted protocols (DoH, DoT) to protect your digital footprint."
source: "RaazNet Aggregation"
content_type: "Educational Guide"
security_level: "Essential"
language: "English"
prerequisites:
  [
    "Basic understanding of internet browsing",
    "Familiarity with settings menus",
  ]
estimated_read_time: "10 minutes"
last_updated: "2026-02-12"
---

# DNS Protocols and Privacy

The **Domain Name System (DNS)** is frequently described as the "phonebook of the internet." It translates human-readable domain names (like `google.com`) into the numerical IP addresses (like `142.250.180.14`) that computers use to connect to each other.

For users in Iran, understanding DNS is not just technical trivia—it is a critical component of bypassing censorship and protecting privacy. The Islamic Republic's filtering infrastructure relies heavily on manipulating DNS traffic to block access to websites and apps.

## The Privacy Problem with Standard DNS

Traditionally, DNS queries are sent in **plaintext** (unencrypted) over the network (usually UDP port 53). This creates two major security risks:

1.  **Surveillance:** Any entity between your device and the DNS server—including your ISP (Irancell, MCI, TCI), network administrators, or government surveillance agencies—can see exactly which websites you are requesting.
2.  **Censorship and Hijacking:** Because the requests are visible, they can be intercepted. In Iran, the "Great Firewall" often inspects these requests. If you ask for a censored domain (e.g., `twitter.com`), the firewall intercepts the packet and sends back a fake response (DNS Poisoning). This redirects you to a blocking page (like _peyvandha_) or simply causes the connection to fail.

> **Key Takeaway:** Using standard, unencrypted DNS allows the regime to easily see what you are visiting and block your access.

---

## Encrypted DNS Protocols

To solve the issues of surveillance and tampering, new protocols were developed to encrypt DNS queries.

### 1. DNS over HTTPS (DoH)

**DNS over HTTPS** encrypts your DNS requests and sends them via the HTTPS protocol (Port 443), blending them in with normal secure web traffic.

- **Pros:** Hardest for censors to distinguish from regular web browsing. Blocking DoH often requires blocking the specific IP of the provider or breaking all HTTPS traffic.
- **Relevance to Iran:** DoH is generally the **most effective** method for bypassing DNS-based censorship in Iran, as Port 443 is rarely blocked entirely.

### 2. DNS over TLS (DoT)

**DNS over TLS** encrypts DNS traffic using the TLS protocol over a dedicated port (Port 853).

- **Pros:** Cleaner separation of DNS traffic from web traffic, supported natively by Android (Private DNS).
- **Relevance to Iran:** Because DoT uses a specific port (853), it is easier for Iranian firewalls to identify and block without affecting other web browsing. If "Private DNS" stops working on your Android phone, the regime has likely blocked Port 853 for that provider.

### 3. DNSCrypt

An older protocol that authenticates and encrypts DNS traffic. While robust, it requires specific software (like DNSCrypt-Proxy) and is less commonly supported natively by operating systems than DoH or DoT.

---

## Limitations: What Encrypted DNS Does NOT Hide

It is crucial to understand the limits of encrypted DNS. While it hides the _lookup_ of the domain, it does not hide the IP address you eventually connect to.

1.  **IP Address Visibility:** Even if you use DoH, your ISP can still see the IP address of the server you connect to after the lookup is finished.
2.  **SNI (Server Name Indication):** When your browser initiates a secure connection (HTTPS) to a website, it sends the domain name in the "Client Hello" packet in plaintext. This allows the regime to see which site you are visiting even if your DNS is encrypted.
    - _Note on ECH:_ A newer technology called **Encrypted Client Hello (ECH)** aims to fix this SNI leak. However, censorship systems (including in Iran and Russia) actively try to block ECH connections.

> **Recommendation:** Encrypted DNS is excellent for bypassing basic blocking and preventing ISP logging, but for high-risk anonymity, it should be used in conjunction with a **VPN** or **Tor**.

---

## Recommended DNS Providers

When choosing a DNS provider, prioritize those with strong privacy policies (no logging), support for DNSSEC (security validation), and high reliability.

| Provider       | DoT Hostname (Android)             | DoH Endpoint                           | Privacy Features                                          |
| :------------- | :--------------------------------- | :------------------------------------- | :-------------------------------------------------------- |
| **Quad9**      | `dns.quad9.net`                    | `https://dns.quad9.net/dns-query`      | Blocks malware; Swiss-based privacy laws.                 |
| **Cloudflare** | `1dot1dot1dot1.cloudflare-dns.com` | `https://cloudflare-dns.com/dns-query` | Fast; 24h log retention (anonymized).                     |
| **Mullvad**    | `doh.mullvad.net`                  | `https://doh.mullvad.net/dns-query`    | No logging; owned by a trusted VPN company.               |
| **Google**     | `dns.google`                       | `https://dns.google/dns-query`         | Reliable; susceptible to US jurisdiction data collection. |

> **Iran Connectivity Note:** Major providers like Cloudflare (`1.1.1.1`) and Google (`8.8.8.8`) are frequently throttled or disrupted in Iran. Quad9 or Mullvad are often better alternatives. If one stops working, switch to another.

---

## How to Enable Encrypted DNS

### On Android (Android 9+)

Android supports **DNS over TLS (DoT)** natively via the "Private DNS" feature.

1.  Go to **Settings** > **Network & Internet** > **Private DNS**.
2.  Select **Private DNS provider hostname**.
3.  Enter the hostname of your chosen provider (e.g., `dns.quad9.net`).
4.  Save.

_Troubleshooting:_ If your internet cuts out after enabling this, the port (853) is likely being blocked by the ISP. Turn it off or try a different provider.

### On Web Browsers (Firefox/Chrome)

Browsers use **DNS over HTTPS (DoH)**.

**Firefox:**

1.  Settings > Privacy & Security.
2.  Scroll down to **DNS over HTTPS**.
3.  Select "Max Protection" or "Increased Protection" and choose a provider (or add a custom one).

**Chrome / Brave:**

1.  Settings > Privacy and security > Security.
2.  Enable "Use secure DNS".
3.  Select "With" and choose a provider.

### Specialized Tools: RethinkDNS

For Android users in Iran, **[RethinkDNS](https://rethinkdns.com/)** is a highly recommended open-source tool.

- **Why:** It combines a firewall with an encrypted DNS resolver.
- **Feature:** It can route DNS requests over Tor or via specific proxies (DoH/DoT/DNSCrypt), making it highly resilient against censorship.

---

## Preventing DNS Leaks

A "DNS Leak" occurs when you are using a VPN, but your DNS requests are still being sent to your ISP outside the encrypted VPN tunnel. This reveals your browsing history to the ISP.

**How to test for leaks:**

1.  Connect to your VPN or configure your Encrypted DNS.
2.  Visit [DNSLeakTest.com](https://www.dnsleaktest.com) or [BrowserLeaks](https://browserleaks.com/dns).
3.  Run the "Extended Test".
4.  **Result Analysis:** You should only see IP addresses belonging to your VPN provider or your chosen DNS provider. If you see "Irancell," "MCI," or "Telecommunication Company of Iran," your DNS is leaking.

**Fixing Leaks:**

- Ensure your VPN client has "DNS Leak Protection" enabled.
- Hard-code Encrypted DNS settings in your browser or OS.
