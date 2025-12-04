---
title: "VPN Overview: How VPNs Protect Your Privacy"
tags: [vpn, privacy, encryption, internet-security, network-privacy]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Digital Security Beginners]
topics: ["VPN Technology", "Internet Privacy", "Network Security"]
summary: "Comprehensive guide explaining how VPNs work, their benefits and limitations, and when to use them for privacy protection."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of internet connectivity", "Familiarity with web browsers"]
estimated_read_time: "8 minutes"
---

# VPN Overview

Virtual Private Networks (VPNs) extend the end of your network to exit somewhere else in the world, providing privacy benefits by hiding your internet activity from your Internet Service Provider (ISP).

## How Internet Traffic Normally Works

Normally, an ISP can see the flow of internet traffic entering and exiting your network termination device (i.e., modem). While encryption protocols such as HTTPS prevent them from seeing exactly what you're posting or reading, they can still identify the domains you request.

## How VPNs Work

A VPN hides your browsing information from your ISP by shifting the trust you place in your network to a server somewhere else in the world. The ISP then only sees that you are connected to a VPN—nothing about the activity passing through it.

VPNs encrypt your traffic between your device and a server owned by your VPN provider:

- **From the perspective of anyone between you and the VPN server**: It looks like you're simply connecting to the VPN server
- **From the perspective of anyone between the VPN server and your destination**: All they can see is the VPN server connecting to the website

> **Important**: A VPN does not add any security or encryption to your traffic between the VPN server and your destination. You must still ensure HTTPS is in use regardless of whether you use a VPN.

> **Note**: When we refer to "Virtual Private Networks," we usually mean **commercial VPN providers** who you pay a monthly fee to route your internet traffic securely through their public servers. Workplace VPNs or self-hosted VPNs serve different purposes—typically accessing remote networks securely rather than protecting the privacy of your internet connection.

## Benefits of Using a VPN

A VPN has several advantages:

1. **Hiding traffic from your ISP** - Your browsing activity remains private from your internet provider
2. **Protecting downloads** - Conceals torrents and other downloads from your ISP and anti-piracy organizations
3. **IP address protection** - Hides your IP from third-party websites and services, helping you blend in and preventing IP-based tracking
4. **Bypassing geo-restrictions** - Access content restricted to certain geographic locations

VPNs can provide some of the same benefits as Tor, such as hiding your IP from websites and geographically shifting your network traffic. Good VPN providers will not cooperate with legal authorities from oppressive regimes, especially if you choose a provider outside your own jurisdiction.

## Limitations of VPNs

Understanding what VPNs cannot do is equally important:

- **Cannot encrypt data outside the VPN connection** - Traffic between the VPN server and your destination remains unprotected by the VPN
- **VPN providers can see your traffic** - They can view and modify your traffic the same way your ISP could
- **"No logging" policies cannot be verified** - These are promises, not guarantees
- **Does not provide absolute anonymity** - The VPN provider still has access to your real IP address, destination website information, and often a payment trail linked to you

### When VPNs Are Not Suitable

Using a VPN when accessing accounts tied to your real identity (like banking) is unlikely to be useful and may trigger spam and fraud detection systems.

If you need complete safety from the network itself, consider using [Tor](https://www.privacyguides.org/en/advanced/tor-overview/) in addition to or instead of a VPN.

**Never trust a VPN to secure connections to unencrypted HTTP destinations.** Use HTTPS to keep your passwords, session tokens, and queries safe from the VPN provider and other potential adversaries. Enable HTTPS-only mode in your browser to mitigate downgrade attacks.

## Common Questions

### Should I Use Encrypted DNS with a VPN?

**Probably not**, unless your VPN provider hosts the encrypted DNS servers themselves. Using DOH/DOT with third-party servers simply adds more entities to trust. Your VPN provider can still see which websites you visit based on IP addresses.

There may be advantages to enabling encrypted DNS for browser security features like ECH, but these technologies are relatively new and not yet widespread.

Your browser should already check TLS certificates with HTTPS and warn you about issues, making DNS spoofing protection less critical.

### Should I Use Tor and a VPN Together?

**Maybe.** Consider your threat model—if your adversary cannot extract information from your VPN provider, using a VPN alone may provide sufficient protection.

If you do use Tor, connecting through a commercial VPN provider is probably best. This is a complex subject covered in more detail in the [Tor overview](https://www.privacyguides.org/en/advanced/tor-overview/).

### What About VPN Providers Offering "Tor Nodes"?

Tor only supports TCP protocol. UDP (used by WebRTC, HTTP3/QUIC), ICMP, and other packets will be dropped. VPN providers typically route non-TCP packets through their VPN server to compensate.

When using Tor over VPN setups provided by VPN companies, you lose control over important Tor features such as Isolated Destination Address (using a different Tor circuit for every domain).

**This feature should be viewed as a convenient way to access hidden services on Tor, not for anonymity.** For proper anonymity, use the actual [Tor Browser](https://www.privacyguides.org/en/tor/).

## VPN Industry Concerns

### Commercial VPN Ownership

Most VPN services are owned by a small number of companies. These companies run many smaller VPN services to create the illusion of choice and maximize profit. Providers feeding into shell companies typically have poor privacy policies and shouldn't be trusted.

Be strict about which provider you choose, and be wary of VPN review sites that are often advertising vehicles open to the highest bidder.

## Emerging VPN Alternatives

### Multi-Party Relays (MPRs)

MPRs use multiple nodes owned by different parties so that no single party knows both who you are and what you're connecting to. This is the basic idea behind Tor, now offered by some paid services.

**How they work:**
1. **First server** (e.g., operated by Apple): Sees your device's IP and payment information but cannot see your destination website
2. **Second server** (e.g., operated by Cloudflare or Fastly): Makes the connection to your destination but only knows the first server's IP, not yours

This protection only exists if you trust the two companies not to collude to deanonymize you.

### Decentralized VPNs (dVPNs)

dVPNs use blockchain technology to distribute nodes across many different people, attempting to eliminate trust in a single party.

**Concerns with dVPNs:**
- Often default to a single node, requiring complete trust in a random person rather than an auditable VPN provider
- Multi-hop solutions come with stability and performance costs
- Exit node operators face legal liability for network misuse, discouraging regular people from running nodes
- Often used to push cryptocurrency rather than provide quality service
- Smaller networks are more vulnerable to [Sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack)

## Additional Resources

- [The Trouble with VPN and Privacy Review Sites](https://blog.privacyguides.org/2019/11/20/the-trouble-with-vpn-and-privacy-review-sites)
- [Free VPN App Investigation](https://top10vpn.com/research/free-vpn-investigations/ownership)
- [Hidden VPN owners unveiled: 101 VPN products run by just 23 companies](https://vpnpro.com/blog/hidden-vpn-owners-unveiled-97-vpns-23-companies)
- [VPN - a Very Precarious Narrative](https://overengineer.dev/blog/2019/04/08/very-precarious-narrative.html) by Dennis Schubert