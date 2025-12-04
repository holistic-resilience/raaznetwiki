---
title: "DNS Filtering for Self-Hosting"
tags: [dns, self-hosting, privacy, ad-blocking, network-security, home-network]
category: "Self-Hosting"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Home Network Administrators, IoT Device Owners]
topics: ["DNS Filtering", "Network Privacy", "Self-Hosting"]
summary: "Guide to self-hosting DNS sinkhole solutions like Pi-hole and AdGuard Home for network-wide ad blocking and privacy protection."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic networking knowledge", "Home server or Raspberry Pi", "Basic Linux command line familiarity"]
estimated_read_time: "3 minutes"
---

# DNS Filtering

**Self-hosting DNS** is useful for providing [DNS filtering](https://cloudflare.com/learning/access-management/what-is-dns-filtering) on controlled platforms, such as smart TVs and other IoT devices, as no client-side software is needed.

> [!note]
> DNS solutions below are typically restricted to your home or local network unless you set up a more advanced configuration.

## What Are DNS Sinkholes?

[**DNS sinkholes**](https://en.wikipedia.org/wiki/DNS_sinkhole) use DNS filtering to block unwanted web content such as advertisements, trackers, and malicious domains at the network level.

## Recommended Solutions

### Pi-hole

**Pi-hole** is an open-source DNS sinkhole which features a friendly web interface to view insights and manage blocked content. Pi-hole is designed to be hosted on a Raspberry Pi, but it is not limited to such hardware.

| Resource | Link |
|----------|------|
| Homepage | [pi-hole.net](https://pi-hole.net/) |
| Documentation | [docs.pi-hole.net](https://docs.pi-hole.net/) |
| Source Code | [GitHub](https://github.com/pi-hole/pi-hole) |

### AdGuard Home

**AdGuard Home** is an open-source DNS sinkhole which features a polished web interface to view insights and manage blocked content.

| Resource | Link |
|----------|------|
| Homepage | [adguard.com](https://adguard.com/adguard-home/overview.html) |
| Documentation | [GitHub Wiki](https://github.com/AdguardTeam/AdGuardHome/wiki) |
| Source Code | [GitHub](https://github.com/AdguardTeam/AdGuardHome) |

## Related Threats Addressed

- **Service Provider Tracking** - Reduces visibility of your browsing habits
- **Surveillance Capitalism** - Blocks advertising and tracking infrastructure