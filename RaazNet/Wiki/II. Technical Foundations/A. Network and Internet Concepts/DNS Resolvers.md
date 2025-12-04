---
title: "DNS Resolvers: Privacy-Focused Options"
tags: [dns, privacy, security, encryption, networking, digital-security]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Professionals, General Public]
topics: ["DNS Security", "Privacy Protection", "Network Security", "Encrypted DNS"]
summary: "Comprehensive guide to privacy-focused DNS resolvers, cloud-based DNS filtering services, and encrypted DNS proxy software."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of internet networking", "Familiarity with DNS concepts"]
estimated_read_time: "8 minutes"
---

# DNS Resolvers

Encrypted **DNS** with third-party servers should only be used to get around basic [DNS blocking](https://en.wikipedia.org/wiki/DNS_blocking) when you can be sure there won't be any consequences. Encrypted DNS will not help you hide any of your browsing activity.

## Recommended Providers

These are recommended public DNS resolvers based on their privacy and security characteristics, and their worldwide performance. Some services offer basic DNS-level blocking of malware or trackers depending on the server you choose. For customizable blocking, consider a dedicated DNS filtering product instead.

| DNS Provider | Protocols | Logging / Privacy Policy | ECS | Filtering | Signed Apple Profile |
| --- | --- | --- | --- | --- | --- |
| **DNS0.eu** | Cleartext, DoH/3, DoH, DoT, DoQ | Anonymized | Anonymized | Based on server choice | Yes |
| **Cloudflare** | Cleartext, DoH/3, DoT | Anonymized | No | Based on server choice | No |
| **Quad9** | Cleartext, DoH, DoT, DNSCrypt | Anonymized | Optional | Based on server choice (malware blocking default) | Yes |
| **AdGuard Public DNS** | Cleartext, DoH/3, DoT, DoQ, DNSCrypt | Anonymized | Anonymized | Based on server choice | Yes |
| **Control D Free DNS** | Cleartext, DoH/3, DoT, DoQ | No | No | Based on server choice | Yes |
| **Mullvad** | DoH, DoT | No | No | Based on server choice | Yes |

## Cloud-Based DNS Filtering

These DNS filtering solutions offer a web dashboard for customizing block lists. They can be used easily across multiple networks.

### Control D

**Control D** is a customizable DNS service that blocks security threats, unwanted content, and advertisements at the DNS level. In addition to paid plans, they offer free preconfigured DNS resolvers.

- [Homepage](https://controld.com/)
- [Privacy Policy](https://controld.com/privacy)
- [Documentation](https://docs.controld.com/docs/getting-started)

**Available on:** Google Play, App Store, Windows, macOS, Linux

### NextDNS

**NextDNS** is a customizable DNS service for blocking security threats, unwanted content, and advertisements at the DNS level. They offer a fully functional free plan for limited use.

- [Homepage](https://nextdns.io/)
- [Privacy Policy](https://nextdns.io/privacy)
- [Documentation](https://help.nextdns.io/)

**Available on:** App Store, Windows, macOS, Linux

> **Note:** When used with an account, NextDNS enables insights and logging features by default. You can customize retention time and log storage location, or disable logs entirely.

> **Important:** The free plan is fully functional but limited to 300,000 DNS queries per month. After this limit, filtering and logging are disabled, though the service continues functioning as a regular DNS provider.

NextDNS also offers public DoH service at `https://dns.nextdns.io` and DoT/DoQ at `dns.nextdns.io`, available by default in Firefox and Chromium.

## Encrypted DNS Proxies

Encrypted DNS proxy software provides a local proxy for unencrypted DNS resolvers. This is primarily useful on platforms that don't natively support encrypted DNS.

### RethinkDNS

**RethinkDNS** is an open-source Android client supporting DoH, DoT, DNSCrypt, and DNS Proxy. Additional features include DNS response caching, local DNS query logging, and firewall functionality.

- [Homepage](https://rethinkdns.com/)
- [Privacy Policy](https://rethinkdns.com/privacy)
- [Documentation](https://docs.rethinkdns.com/)

**Available on:** Google Play, GitHub

> **Tip:** While RethinkDNS uses the Android VPN slot, you can still use a VPN or Orbot by adding a WireGuard configuration or manually configuring Orbot as a proxy server.

### DNSCrypt-Proxy

**DNSCrypt-Proxy** is a DNS proxy supporting DNSCrypt, DoH, and Anonymized DNS.

- [Repository](https://github.com/DNSCrypt/dnscrypt-proxy)
- [Documentation](https://github.com/DNSCrypt/dnscrypt-proxy/wiki)

**Available on:** Windows, macOS, Linux

> **Warning:** The anonymized DNS feature does **not** anonymize other network traffic.

## Selection Criteria

All recommended DNS products must:

- Support DNSSEC
- Support QNAME Minimization
- Anonymize ECS or disable it by default

All public providers must:

- Not log any personal data to disk
- Support anycast or geo-steering (recommended)

## Privacy Policy Notes

### AdGuard
Stores aggregated performance metrics and a database of domains requested within the last 24 hours for threat identification and filter maintenance.

### Cloudflare
Collects limited DNS query data. Does not log personal data; non-personally identifiable query data is stored only for 25 hours.

### Control D
Only logs specific account data for Premium resolvers with custom DNS profiles. Free resolvers do not retain any data.

### DNS0.eu
Collects data for threat intelligence feeds to monitor domains. Data is shared with partners for security research. No personally identifiable information is collected.

### Mullvad
Available to both VPN subscribers and non-subscribers. Privacy policy explicitly states they do not log DNS requests.

### Quad9
Collects some data for threat monitoring and response, which may be shared for security research. Does not collect or record IP addresses or personally identifiable data.