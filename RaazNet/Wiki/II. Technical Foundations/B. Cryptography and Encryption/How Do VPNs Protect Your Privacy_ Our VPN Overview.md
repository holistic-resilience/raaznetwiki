---
title: "VPN Overview: How VPNs Protect Your Privacy"
tags: [vpn, privacy, encryption, network-security, isp, anonymity]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["VPN Technology", "Network Privacy", "Internet Security"]
summary: "Comprehensive guide explaining how VPNs work, their benefits and limitations, and when to use them for privacy protection."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of internet connectivity", "Familiarity with encryption concepts"]
estimated_read_time: "10 minutes"
---

# VPN Overview

Virtual Private Networks (VPNs) extend the end of your network to exit somewhere else in the world, providing privacy benefits by shifting trust from your Internet Service Provider to a VPN server.

> **Note:** When we refer to "Virtual Private Networks" here, we mean **commercial VPN providers**—paid services that route your internet traffic securely through their public servers. Other VPN types (self-hosted or workplace VPNs) are designed for accessing remote networks securely, not for protecting internet connection privacy.

## How Does a VPN Work?

Normally, an ISP can see the flow of internet traffic entering and exiting your network device. While encryption protocols like HTTPS prevent them from seeing exact content, they can still identify the [domains you request](https://www.privacyguides.org/en/advanced/dns-overview/#why-shouldnt-i-use-encrypted-dns).

VPNs encrypt your traffic between your device and the VPN provider's server:

- **From your ISP's perspective:** They only see you're connected to a VPN server—nothing about your actual activity
- **From websites' perspective:** They see the VPN server connecting, not your real IP address

**Important:** A VPN does not add security or encryption between the VPN server and your destination. You must still ensure HTTPS is in use for secure website access.

## Should I Use a VPN?

**Yes**, almost certainly. VPN advantages include:

1. Hiding your traffic from your Internet Service Provider
2. Hiding downloads (such as torrents) from your ISP and anti-piracy organizations
3. Hiding your IP from third-party websites, helping you blend in and preventing IP-based tracking
4. Bypassing geo-restrictions on certain content

VPNs can provide some benefits similar to Tor, such as hiding your IP from websites and geographically shifting your network traffic. Good VPN providers won't cooperate with oppressive legal authorities, especially if located outside your jurisdiction.

## VPN Limitations

**VPNs cannot:**
- Encrypt data outside the connection between your device and the VPN server
- Prevent the VPN provider from seeing and modifying your traffic
- Guarantee "no logging" policies (these are unverifiable promises)

## When Isn't a VPN Suitable?

### Using Your Real Identity Online

Using a VPN while logged into accounts tied to your real identity (like banking websites) may trigger spam and fraud detection systems.

### When You Need Absolute Anonymity

A VPN will not provide absolute anonymity because:
- The VPN provider has access to your real IP address
- They can see destination website information
- There's often a money trail linking back to you

For complete safety from the network itself, consider using [Tor](https://www.privacyguides.org/en/advanced/tor-overview/) in addition to or instead of a VPN.

### Unencrypted Connections

Never trust a VPN to secure connections to unencrypted HTTP destinations. Use HTTPS to keep passwords, session tokens, and queries safe from the VPN provider and other adversaries. Enable HTTPS-only mode in your browser to mitigate downgrade attacks.

## Should I Use Encrypted DNS with a VPN?

**Probably not**, unless your VPN provider hosts the encrypted DNS servers themselves.

Using DOH/DOT with third-party servers adds more entities to trust. Your VPN provider can still see which websites you visit based on IP addresses. However, encrypted DNS may enable other browser security features like ECH (Encrypted Client Hello).

**Regarding DNS spoofing:** Your browser should already check TLS certificates with HTTPS and warn you about issues. Without HTTPS, adversaries can modify content beyond DNS queries anyway.

## Should I Use Tor and a VPN Together?

**Maybe.** Consider your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/). If your adversary cannot extract information from your VPN provider, a VPN alone may provide sufficient protection.

If you do use Tor, connecting via a commercial VPN provider is probably best. See the [Tor overview](https://www.privacyguides.org/en/advanced/tor-overview/) for detailed guidance.

### VPN Providers with "Tor Nodes"

Tor only supports TCP protocol. UDP (WebRTC, HTTP3/QUIC), ICMP, and other packets are dropped. VPN providers typically route non-TCP packets through their VPN server to compensate.

**Limitations of this approach:**
- You lack control over important Tor features like [Isolated Destination Address](https://whonix.org/wiki/Stream_Isolation) (using different Tor circuits per domain)
- This should be viewed as a convenient way to access hidden services, not for anonymity

For proper anonymity, use the actual [Tor Browser](https://www.privacyguides.org/en/tor/).

## Commercial VPN Ownership Concerns

Most VPN services are owned by a [few companies](https://vpnpro.com/blog/hidden-vpn-owners-unveiled-97-vpns-23-companies). These companies run multiple smaller VPN services to create an illusion of choice while maximizing profit. Providers feeding into shell companies typically have poor privacy policies.

**Be wary of VPN review sites**—many are advertising vehicles open to the highest bidder.

## Modern VPN Alternatives

### Multi-Party Relays (MPRs)

MPRs use multiple nodes owned by different parties, ensuring no single party knows both your identity and your destination. This is Tor's basic principle, now offered by some paid services.

**Example: Apple's iCloud Private Relay**
1. **First server (Apple):** Sees your device IP and payment information, but not your destination
2. **Second server (CDN partner like Cloudflare):** Makes the connection to your destination but only knows Apple's server IP

**Caveat:** This protection only works if you trust both companies not to collude.

### Decentralized VPNs (dVPNs)

dVPNs use blockchain technology to distribute nodes across many people, attempting to eliminate single-party trust.

**Significant concerns:**
- Often default to a single node, requiring complete trust in a random person (not an auditable provider with legal responsibilities)
- Multi-hop solutions have stability and performance costs
- Exit nodes face legal liability issues from network misuse
- This discourages regular people from running nodes while attracting malicious actors
- Many dVPNs prioritize cryptocurrency promotion over service quality
- Smaller networks are more vulnerable to [Sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack)

## Further Reading

- [The Trouble with VPN and Privacy Review Sites](https://blog.privacyguides.org/2019/11/20/the-trouble-with-vpn-and-privacy-review-sites)
- [Free VPN App Investigation](https://top10vpn.com/research/free-vpn-investigations/ownership)
- [Hidden VPN owners unveiled: 101 VPN products run by just 23 companies](https://vpnpro.com/blog/hidden-vpn-owners-unveiled-97-vpns-23-companies)
- [VPN - a Very Precarious Narrative](https://overengineer.dev/blog/2019/04/08/very-precarious-narrative.html) by Dennis Schubert