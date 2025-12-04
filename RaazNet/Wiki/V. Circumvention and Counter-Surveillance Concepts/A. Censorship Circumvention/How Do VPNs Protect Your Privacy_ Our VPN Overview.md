---
title: "VPN Overview: How VPNs Protect Your Privacy"
tags: [vpn, privacy, encryption, network-security, internet-privacy]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Digital Security Beginners]
topics: ["VPN Technology", "Network Privacy", "Internet Security"]
summary: "Comprehensive guide explaining how VPNs work, their benefits and limitations, and when to use them for privacy protection."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of internet connectivity", "Familiarity with web browsing"]
estimated_read_time: "12 minutes"
---

# VPN Overview

Virtual Private Networks (VPNs) extend the end of your network to exit somewhere else in the world, providing privacy benefits by hiding your internet activity from your Internet Service Provider (ISP).

Normally, an ISP can see the flow of internet traffic entering and exiting your network termination device (i.e., modem). While encryption protocols such as HTTPS prevent them from seeing exactly what you're posting or reading, they can still identify the domains you request.

Using a VPN hides this information from your ISP by shifting the trust you place in your network to a server elsewhere in the world. As a result, the ISP only sees that you are connected to a VPN and nothing about the activity passing through it.

> **Note:** When we refer to "Virtual Private Networks" here, we typically mean **commercial VPN providers**—services you pay a monthly fee to in exchange for routing your internet traffic securely through their public servers. Other forms of VPN exist, such as self-hosted solutions or workplace VPNs for accessing internal resources, but these are designed for remote network access rather than protecting internet connection privacy.

## How Does a VPN Work?

VPNs encrypt your traffic between your device and a server owned by your VPN provider:

- **From the perspective of anyone between you and the VPN server:** It appears you're simply connecting to the VPN server
- **From the perspective of anyone between the VPN server and your destination:** They only see the VPN server connecting to the website

> **Important:** A VPN does not add security or encryption to traffic between the VPN server and your destination. You **must** still ensure HTTPS is in use to access websites securely, regardless of whether you use a VPN.

## Should I Use a VPN?

**Yes**, almost certainly. A VPN provides several advantages:

1. **Hiding traffic from your ISP** — Your internet activity remains private from your service provider
2. **Protecting downloads** — Conceals torrents and other downloads from ISPs and anti-piracy organizations
3. **Masking your IP address** — Helps you blend in and prevents IP-based tracking by third-party websites
4. **Bypassing geo-restrictions** — Allows access to content restricted by geographic location

VPNs can provide some benefits similar to Tor, such as hiding your IP from websites and geographically shifting your network traffic. Good VPN providers will not cooperate with legal authorities from oppressive regimes, especially if you choose a provider outside your jurisdiction.

### VPN Limitations

- VPNs cannot encrypt data outside the connection between your device and the VPN server
- VPN providers can see and modify your traffic just as your ISP could
- There is no way to verify a VPN provider's "no logging" policies
- You are still placing trust in the VPN provider

## When Isn't a VPN Suitable?

### Using Your Real Identity

Using a VPN while accessing services with your real-life or well-known identity is unlikely to be useful. It may trigger spam and fraud detection systems—for example, when logging into your bank's website.

### When You Need True Anonymity

A VPN will not provide absolute anonymity because the VPN provider still has access to:
- Your real IP address
- Destination website information
- Often a money trail linked back to you

"No logging" policies are merely promises. If you need complete safety from the network itself, consider using [Tor](https://www.privacyguides.org/en/advanced/tor-overview/) in addition to or instead of a VPN.

### Unencrypted Connections

Never trust a VPN to secure your connection to an unencrypted HTTP destination. To keep your activity private and secure, you must use HTTPS. This protects your passwords, session tokens, and queries from both the VPN provider and other potential adversaries. Enable HTTPS-only mode in your browser to mitigate downgrade attacks.

## Should I Use Encrypted DNS with a VPN?

**Probably not**, unless your VPN provider hosts the encrypted DNS servers themselves.

Using DOH/DOT (or any other form of encrypted DNS) with third-party servers adds more entities to trust. Your VPN provider can still see which websites you visit based on IP addresses and other methods.

However, there may be advantages to enabling encrypted DNS for other browser security features like ECH. These browser technologies are relatively new and not yet widespread.

### DNS Spoofing Concerns

Encrypted DNS is sometimes recommended to prevent DNS spoofing. However, your browser should already check TLS certificates with HTTPS and warn you about issues. If you're not using HTTPS, an adversary can modify other elements besides DNS queries anyway.

## Should I Use Tor and a VPN Together?

**Maybe.** Tor is not suitable for everyone. Consider your threat model—if your adversary cannot extract information from your VPN provider, using a VPN alone may provide sufficient protection.

If you do use Tor, you're probably best off connecting to the Tor network via a commercial VPN provider. This is a complex subject covered in more detail in the [Tor overview](https://www.privacyguides.org/en/advanced/tor-overview/).

## Should I Access Tor Through VPN Providers That Provide "Tor Nodes"?

This approach has significant limitations:

**Protocol Limitations:**
- Tor currently only supports TCP protocol
- UDP (used by WebRTC, HTTP3/QUIC), ICMP, and other packets will be dropped
- VPN providers typically route non-TCP packets through their VPN server (your first hop)

**Control Limitations:**
- You don't have control over important Tor features like Isolated Destination Address (using different Tor circuits for each domain)

This feature should be viewed as a **convenient way to access hidden services on Tor**, not as a method to stay anonymous. For proper anonymity, use the actual [Tor Browser](https://www.privacyguides.org/en/tor/).

## Commercial VPN Ownership

Most VPN services are owned by a small number of companies. These companies run many smaller VPN services to create the illusion of choice while maximizing profit. Providers feeding into shell companies typically have poor privacy policies and shouldn't be trusted with your internet traffic.

**Be cautious of:**
- VPN review sites that are advertising vehicles for the highest bidder
- Free VPN services with questionable ownership
- Providers with unclear corporate structures

## Modern VPN Alternatives

### Multi-Party Relays (MPRs)

MPRs use multiple nodes owned by different parties, ensuring no single party knows both who you are and what you're connecting to. This is the basic idea behind Tor, but some paid services now emulate this model.

**How Apple's iCloud Private Relay Works:**

1. **First server (operated by Apple):** Sees your device's IP and payment information but cannot see your destination website
2. **Second server (operated by partner CDN like Cloudflare or Fastly):** Makes the connection to your destination but only knows Apple's server IP, not your device

This protection by segmentation only works if you trust the two companies not to collude to deanonymize you.

### Decentralized VPNs (dVPNs)

dVPNs attempt to solve centralized VPN issues using blockchain technology and distributed nodes. However, they have significant drawbacks:

**Trust Issues:**
- Many dVPNs default to a single node, requiring complete trust in that node
- Unlike traditional VPNs, this node is a random person rather than an auditable provider with legal responsibilities
- Multi-hop solutions exist but reduce stability and performance

**Legal and Security Concerns:**
- Exit nodes must handle legal problems from network misuse
- This discourages regular people from running nodes
- Makes it attractive for malicious actors with resources to host nodes
- Smaller networks are more vulnerable to Sybil attacks

**Cryptocurrency Focus:**
- Many dVPNs prioritize pushing cryptocurrency over providing quality service

## Additional Resources

- [The Trouble with VPN and Privacy Review Sites](https://blog.privacyguides.org/2019/11/20/the-trouble-with-vpn-and-privacy-review-sites)
- [Free VPN App Investigation](https://top10vpn.com/research/free-vpn-investigations/ownership)
- [Hidden VPN owners unveiled: 101 VPN products run by just 23 companies](https://vpnpro.com/blog/hidden-vpn-owners-unveiled-97-vpns-23-companies)
- [VPN - a Very Precarious Narrative](https://overengineer.dev/blog/2019/04/08/very-precarious-narrative.html) by Dennis Schubert