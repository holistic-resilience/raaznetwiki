---
title: "DNS Resolvers: Privacy-Focused Providers and Tools"
tags: [dns, privacy, encryption, security, networking, digital-security]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Professionals, Technical Users]
topics: ["DNS Security", "Encrypted DNS", "Privacy Protection", "Network Security"]
summary: "Comprehensive guide to privacy-respecting DNS resolvers, cloud-based filtering services, and encrypted DNS proxy tools."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of DNS", "Familiarity with network concepts"]
estimated_read_time: "8 minutes"
---

# DNS Resolvers

Encrypted **DNS** with third-party servers should only be used to get around basic [DNS blocking](https://en.wikipedia.org/wiki/DNS_blocking) when you can be sure there won't be any consequences. Encrypted DNS will not help you hide any of your browsing activity.

## Recommended Public DNS Providers

These are recommended public DNS resolvers based on their privacy and security characteristics, and worldwide performance. Some offer basic DNS-level blocking of malware or trackers depending on the server you choose. For customizable blocking, consider a dedicated DNS filtering product instead.

| DNS Provider | Protocols | Logging | ECS | Filtering | Signed Apple Profile |
| --- | --- | --- | --- | --- | --- |
| **DNS0.eu** | Cleartext, DoH/3, DoH, DoT, DoQ | Anonymized | Anonymized | Based on server choice | Yes |
| **Cloudflare** | Cleartext, DoH/3, DoT | Anonymized | No | Based on server choice | No |
| **Quad9** | Cleartext, DoH, DoT, DNSCrypt | Anonymized | Optional | Based on server choice (malware blocking default) | Yes |
| **AdGuard Public DNS** | Cleartext, DoH/3, DoT, DoQ, DNSCrypt | Anonymized | Anonymized | Based on server choice | Yes |
| **Control D Free DNS** | Cleartext, DoH/3, DoT, DoQ | No | No | Based on server choice | Yes |
| **Mullvad** | DoH, DoT | No | No | Based on server choice | Yes |

## Cloud-Based DNS Filtering

These DNS filtering solutions offer web dashboards for customizing block lists and can be used across multiple networks.

### Control D

A customizable DNS service that blocks security threats, unwanted content, and advertisements at the DNS level. Offers paid plans plus free preconfigured DNS resolvers.

- **Platforms**: Android (Google Play), iOS (App Store), Windows, macOS, Linux
- **Features**: Customizable filtering, multiple preconfigured options

### NextDNS

A customizable DNS service with security threat blocking, content filtering, and ad blocking at the DNS level. Offers a functional free plan with limited usage.

- **Platforms**: iOS (App Store), Windows, macOS, Linux
- **Features**: Insights and logging (optional), customizable retention settings

**Important Notes:**
- Free plan limited to 300,000 DNS queries/month before filtering disables
- Public DoH available at `https://dns.nextdns.io`
- Public DoT/DoQ available at `dns.nextdns.io`

## Encrypted DNS Proxies

These tools provide local proxies for forwarding unencrypted DNS to encrypted resolvers, useful on platforms without native encrypted DNS support.

### RethinkDNS

An open-source Android client supporting DoH, DoT, DNSCrypt, and DNS Proxy with additional firewall functionality.

- **Platform**: Android (Google Play, GitHub)
- **Features**: DNS caching, local query logging, firewall capabilities
- **VPN Compatibility**: Can work alongside VPN or Orbot via WireGuard configuration or manual proxy setup

### DNSCrypt-Proxy

A DNS proxy supporting DNSCrypt, DoH, and Anonymized DNS.

- **Platforms**: Windows, macOS, Linux
- **Features**: Multiple protocol support, anonymized DNS option

> **Warning**: The anonymized DNS feature does not anonymize other network traffic.

## Selection Criteria

All recommended DNS products must:
- Support DNSSEC
- Support QNAME Minimization
- Anonymize ECS or disable it by default

Public providers must additionally:
- Not log personal data to disk
- Support anycast or geo-steering (recommended)

## Provider Privacy Details

| Provider | Privacy Notes |
| --- | --- |
| **AdGuard** | Stores aggregated performance metrics; maintains 24-hour domain request database for threat identification |
| **Cloudflare** | Limited query data stored for 25 hours; no personal data logging |
| **Control D** | Free resolvers retain no data; Premium accounts log specific account data |
| **DNS0.eu** | Collects threat intelligence data; shares with security research partners; no PII collected |
| **Mullvad** | Explicitly claims no DNS request logging |
| **Quad9** | Collects threat monitoring data; does not collect IP addresses or PII |