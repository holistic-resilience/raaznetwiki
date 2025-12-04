---
title: "DNS Resolvers: Privacy-Focused Providers and Tools"
tags: [dns, privacy, encryption, networking, security, filtering]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, System Administrators, Security Enthusiasts]
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
| **DNS0.eu** | Cleartext, DoH/3, DoH, DoT, DoQ | Anonymized | Anonymized | Server-based | Yes |
| **Cloudflare** | Cleartext, DoH/3, DoT | Anonymized | No | Server-based | No |
| **Quad9** | Cleartext, DoH, DoT, DNSCrypt | Anonymized | Optional | Server-based (malware blocking default) | Yes |
| **AdGuard Public DNS** | Cleartext, DoH/3, DoT, DoQ, DNSCrypt | Anonymized | Anonymized | Server-based | Yes |
| **Control D Free DNS** | Cleartext, DoH/3, DoT, DoQ | No | No | Server-based | Yes |
| **Mullvad** | DoH, DoT | No | No | Server-based | Yes |

### Provider Privacy Notes

- **AdGuard**: Stores aggregated performance metrics and a 24-hour database of requested domains for threat identification
- **Cloudflare**: Limited non-personally identifiable query data stored for 25 hours maximum
- **Control D**: Free resolvers retain no data; Premium resolvers log specific account data only
- **DNS0.eu**: Collects threat intelligence data shared with security research partners; no personally identifiable information
- **Mullvad**: Explicitly claims no DNS request logging for both subscribers and non-subscribers
- **Quad9**: Collects threat monitoring data; does not collect IP addresses or personally identifiable information

## Cloud-Based DNS Filtering

These services offer web dashboards for customizing block lists and can be used across multiple networks.

### Control D

Customizable DNS service for blocking security threats, unwanted content, and advertisements at the DNS level. Offers paid plans plus free preconfigured DNS resolvers.

**Available on:** Android (Google Play), iOS (App Store), Windows, macOS, Linux

### NextDNS

Customizable DNS service with security threat blocking, content filtering, and advertisement blocking. Offers a fully functional free plan with limited use.

**Key considerations:**
- Account-based usage enables insights and logging by default (configurable)
- Free plan: 300,000 DNS queries/month limit; filtering disabled after threshold but DNS continues functioning
- Public DoH available at `https://dns.nextdns.io`
- Public DoT/DoQ available at `dns.nextdns.io`

**Available on:** iOS (App Store), Windows, macOS, Linux

## Encrypted DNS Proxies

These tools provide local proxies for forwarding unencrypted DNS to encrypted resolvers, useful on platforms without native encrypted DNS support.

### RethinkDNS

Open-source Android client supporting DoH, DoT, DNSCrypt, and DNS Proxy. Additional features include DNS response caching, local query logging, and firewall functionality.

> **Note:** While RethinkDNS uses the Android VPN slot, you can still use a VPN or Orbot by adding a WireGuard configuration or manually configuring Orbot as a proxy server.

**Available on:** Android (Google Play, GitHub)

### DNSCrypt-Proxy

DNS proxy supporting DNSCrypt, DoH, and Anonymized DNS.

> **Warning:** The anonymized DNS feature does not anonymize other network traffic.

**Available on:** Windows, macOS, Linux

## Selection Criteria

All recommended DNS products must:
- Support DNSSEC
- Support QNAME Minimization
- Anonymize ECS or disable it by default

All recommended public providers must:
- Not log personal data to disk
- Support anycast or geo-steering (recommended)