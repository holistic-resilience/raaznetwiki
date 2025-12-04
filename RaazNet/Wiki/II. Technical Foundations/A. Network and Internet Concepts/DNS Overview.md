```yaml
---
title: "DNS Overview"
tags: [dns, encryption, privacy, networking, security, surveillance]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Practitioners, System Administrators]
topics: ["DNS", "Encrypted DNS", "Network Privacy", "Internet Security"]
summary: "Comprehensive guide to DNS, encrypted DNS protocols (DoH, DoT, DNSCrypt), and privacy considerations for domain name resolution."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic networking concepts", "Command line familiarity"]
estimated_read_time: "15 minutes"
---
```

# DNS Overview

The [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) is the "phone book of the Internet." DNS translates domain names to IP addresses so browsers and other services can load Internet resources through a decentralized network of servers.

## What is DNS?

When you visit a website, a numerical address is returned. For example, when you visit `privacyguides.org`, the address `192.98.54.105` is returned.

DNS has existed since the [early days](https://en.wikipedia.org/wiki/Domain_Name_System#History) of the Internet. DNS requests made to and from DNS servers are **not** generally encrypted. In a residential setting, a customer is given servers by the ISP via [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol).

Unencrypted DNS requests can be easily **surveilled** and **modified** in transit. In some parts of the world, ISPs are ordered to perform [DNS filtering](https://en.wikipedia.org/wiki/DNS_blocking). When you request the IP address of a blocked domain, the server may not respond or may respond with a different IP address. Since the DNS protocol is not encrypted, ISPs (or any network operator) can use [Deep Packet Inspection (DPI)](https://en.wikipedia.org/wiki/Deep_packet_inspection) to monitor requests and block them based on common characteristics, regardless of which DNS server is used.

### Demonstrating Unencrypted DNS Visibility

Using packet capture tools, we can observe what an outside party sees with unencrypted DNS:

1. **Capture DNS traffic** using `tshark` (part of [Wireshark](https://en.wikipedia.org/wiki/Wireshark)):

```bash
tshark -w /tmp/dns.pcap udp port 53 and host 1.1.1.1 or host 8.8.8.8
```

2. **Send DNS lookups** using `dig` (Linux/macOS) or `nslookup` (Windows):

**Linux/macOS:**
```bash
dig +noall +answer privacyguides.org @1.1.1.1
dig +noall +answer privacyguides.org @8.8.8.8
```

**Windows:**
```powershell
nslookup privacyguides.org 1.1.1.1
nslookup privacyguides.org 8.8.8.8
```

3. **Analyze the captured packets:**

```bash
wireshark -r /tmp/dns.pcap
# or
tshark -r /tmp/dns.pcap
```

The captured data reveals complete visibility into DNS queries:

| No. | Time | Source | Destination | Protocol | Info |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.000000 | 192.0.2.1 | 1.1.1.1 | DNS | Standard query A privacyguides.org |
| 2 | 0.293395 | 1.1.1.1 | 192.0.2.1 | DNS | Standard query response A 198.98.54.105 |
| 3 | 1.682109 | 192.0.2.1 | 8.8.8.8 | DNS | Standard query A privacyguides.org |
| 4 | 2.154698 | 8.8.8.8 | 192.0.2.1 | DNS | Standard query response A 198.98.54.105 |

An observer could monitor or modify any of these packets.

---

## Encrypted DNS Protocols

Encrypted DNS refers to several protocols that protect DNS queries from surveillance and modification.

### DNSCrypt

[DNSCrypt](https://en.wikipedia.org/wiki/DNSCrypt) was one of the first methods of encrypting DNS queries. It operates on port 443 using TCP or UDP. However, DNSCrypt was never submitted to the [IETF](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) or standardized through the [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) process, limiting its adoption. It has been largely replaced by DNS over HTTPS.

### DNS over TLS (DoT)

[DNS over TLS](https://en.wikipedia.org/wiki/DNS_over_TLS) is defined in [RFC 7858](https://datatracker.ietf.org/doc/html/rfc7858). Support exists in Android 9+, iOS 14+, and Linux via [systemd-resolved](https://freedesktop.org/software/systemd/man/resolved.conf.html#DNSOverTLS=) (version 237+).

**Limitations:**
- Operates on dedicated port 853, which is easily blocked by restrictive firewalls
- Complex protocol with varying RFC compliance across implementations
- Industry preference has shifted toward DoH

### DNS over HTTPS (DoH)

[DNS over HTTPS](https://en.wikipedia.org/wiki/DNS_over_HTTPS), defined in [RFC 8484](https://datatracker.ietf.org/doc/html/rfc8484), packages queries in [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2) and provides security with HTTPS.

**Browser Support:** Firefox 60+, Chrome 83+

**Native OS Support:**
- iOS 14+, macOS 11+
- Microsoft Windows
- Android 13+ (not enabled by default)
- Linux: Requires third-party software (systemd implementation pending)

---

## Operating System Configuration

### Android
Android 9+ supports DNS over TLS natively through Private DNS settings.

### Apple Devices (iOS, iPadOS, tvOS, macOS)
Both DoT and DoH are supported via [configuration profiles](https://support.apple.com/guide/security/configuration-profile-enforcement-secf6fb9f053/web) or the [DNS Settings API](https://developer.apple.com/documentation/networkextension/dns_settings).

> **Note:** If a VPN is active, resolution within the VPN tunnel uses the VPN's DNS settings, not system-wide settings.

Apple doesn't provide a native interface for creating encrypted DNS profiles. [Secure DNS profile creator](https://dns.notjakob.com/tool.html) is an unofficial tool for this purpose. Signed profiles are preferred as they validate origin and integrity.

### Linux
`systemd-resolved` doesn't yet [support DoH](https://github.com/systemd/systemd/issues/8639). To use DoH on Linux, install a proxy like [dnscrypt-proxy](https://wiki.archlinux.org/title/Dnscrypt-proxy) to forward DNS queries over HTTPS.

---

## Privacy Limitations of Encrypted DNS

Even with encrypted DNS, outside parties can still determine your browsing activity through several methods:

### IP Address Observation

Observers can see the IP addresses your devices access. If `privacyguides.org` is at `198.98.54.105` and your device requests data from that address, your destination is revealed.

**Limitations of this method:**
- Only useful when IP addresses host few websites
- Ineffective for shared platforms (GitHub Pages, Cloudflare, Netlify, WordPress, etc.)
- Ineffective behind reverse proxies (common on the modern Internet)

### Server Name Indication (SNI)

When multiple websites share an IP address (common with CDNs and DDoS protection services), [Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication) reveals which site you're visiting during the TLS handshake.

To observe SNI in captured traffic:
```bash
tshark -r /tmp/pg.pcap -Tfields -Y tls.handshake.extensions_server_name -e tls.handshake.extensions_server_name
```

**Mitigation:** [TLS v1.3](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3) introduces [Encrypted Client Hello (ECH)](https://blog.cloudflare.com/encrypted-client-hello), which prevents SNI leakage. However, some governments ([China](https://zdnet.com/article/china-is-now-blocking-all-encrypted-https-traffic-using-tls-1-3-and-esni), [Russia](https://zdnet.com/article/russia-wants-to-ban-the-use-of-secure-protocols-such-as-tls-1-3-doh-dot-esni)) have begun blocking ECH.

### Online Certificate Status Protocol (OCSP)

When visiting HTTPS websites, browsers may check if certificates have been revoked using [OCSP](https://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol). This check uses unencrypted HTTP, revealing the certificate's unique serial number.

Network observers can match serial numbers with public certificates to determine which sites you're visiting. [Certificate Transparency](https://en.wikipedia.org/wiki/Certificate_Transparency) logs can also be checked for serial numbers.

---

## When to Use Encrypted DNS

**Use encrypted DNS when:**
- You want privacy from your ISP
- Your ISP makes obnoxious redirects on failed DNS queries
- You want basic protection against DNS-based tracking

**Don't rely solely on encrypted DNS when:**
- Trying to be anonymous → **Use Tor**
- Avoiding censorship → **Use VPN or Tor**
- In locations with internet filtering where visiting forbidden resources may have consequences

> **Important:** When using a VPN, use your VPN's DNS servers. You're already trusting them with all your network activity.

---

## Additional DNS Security Features

### DNSSEC (Domain Name System Security Extensions)

[DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions) authenticates DNS responses to prevent manipulation or poisoning. It does **not** provide privacy—it ensures data integrity through hierarchical digital signatures.

**How it works:**
1. Root DNS server signs a key for the TLD nameserver (e.g., `.org`)
2. TLD nameserver signs a key for the domain's authoritative nameserver
3. Each level validates the next, ensuring responses haven't been tampered with

### QNAME Minimization

Traditional DNS queries reveal the full domain name to every server in the resolution chain. QNAME minimization ([RFC 7816](https://datatracker.ietf.org/doc/html/rfc7816)) reduces information disclosure by only asking each server for the minimum information needed:

| Server | Traditional Query | Minimized Query |
| --- | --- | --- |
| Root server | "What's the IP of discuss.privacyguides.net?" | "What's the nameserver for .net?" |
| .net server | "What's the IP of discuss.privacyguides.net?" | "What's the nameserver for privacyguides.net?" |
| Domain server | "What's the IP of discuss.privacyguides.net?" | "What's the IP of discuss.privacyguides.net?" |

### EDNS Client Subnet (ECS)

[EDNS Client Subnet](https://en.wikipedia.org/wiki/EDNS_Client_Subnet) allows DNS resolvers to share your approximate network location with authoritative servers to optimize content delivery (e.g., directing you to nearby CDN servers).

**Privacy concern:** This reveals information about your location. For example, if your IP is `198.51.100.32`, the DNS provider might share `198.51.100.0/24` with the authoritative server.

**Test if your DNS leaks ECS data:**
```bash
dig +nocmd -t txt o-o.myaddr.l.google.com +nocomments +noall +answer +stats
```

If results include `edns0-client-subnet`, your DNS provider is sharing location information:
```
o-o.myaddr.l.google.com. 60 IN TXT "198.51.100.32"
o-o.myaddr.l.google.com. 60 IN TXT "edns0-client-subnet 198.51.100.0/24"
```

---

## Further Resources

- [List of recommended DNS servers](https://www.privacyguides.org/en/dns/)
- [DNS Security Extensions (DNSSEC) overview](https://cloud.google.com/dns/docs/dnssec) — Google
- [DNSSEC: An Introduction](https://blog.cloudflare.com/dnssec-an-introduction) — Cloudflare