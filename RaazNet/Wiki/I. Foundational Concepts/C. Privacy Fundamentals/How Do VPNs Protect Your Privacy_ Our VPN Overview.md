---
title: "VPN Overview: How VPNs Protect Your Privacy"
tags: [vpn, privacy, encryption, network-security, isp, tor]
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

Normally, an ISP can see the flow of internet traffic entering and exiting your network termination device (i.e., modem). While encryption protocols such as HTTPS prevent them from seeing exactly what you're posting or reading, they can still identify the [domains you request](https://www.privacyguides.org/en/advanced/dns-overview/#why-shouldnt-i-use-encrypted-dns).

Using a VPN hides this information from your ISP by shifting trust to a server elsewhere in the world. The ISP then only sees that you are connected to a VPN—nothing about the activity passing through it.

> **Note:** When we refer to "Virtual Private Networks" here, we mean **commercial** VPN providers that you pay monthly to route your internet traffic securely through their public servers. Other VPN types exist (self-hosted or workplace VPNs for accessing internal resources), but these are designed for remote network access rather than protecting internet connection privacy.

## How Does a VPN Work?

VPNs encrypt your traffic between your device and a server owned by your VPN provider:

- **From the perspective of anyone between you and the VPN server:** It appears you're simply connecting to the VPN server
- **From the perspective of anyone between the VPN server and your destination:** They only see the VPN server connecting to the website

> **Important:** A VPN does not add security or encryption to traffic between the VPN server and your destination. You **must** still ensure HTTPS is in use to access websites securely, regardless of VPN usage.

## Should I Use a VPN?

**Yes**, almost certainly. A VPN provides several advantages:

1. **Hiding traffic from your ISP** — Your Internet Service Provider cannot see your browsing activity
2. **Protecting downloads** — Conceals torrents and other downloads from ISPs and anti-piracy organizations
3. **IP address privacy** — Hides your IP from third-party websites, helping prevent IP-based tracking
4. **Bypassing geo-restrictions** — Access content that may be blocked in your region

VPNs can provide some benefits similar to Tor, such as hiding your IP from websites and geographically shifting your network traffic. Good VPN providers will not cooperate with legal authorities from oppressive regimes, especially if located outside your jurisdiction.

### VPN Limitations

- VPNs cannot encrypt data outside the connection between your device and the VPN server
- VPN providers can see and modify your traffic just as your ISP could
- There is no way to verify a VPN provider's "no logging" policies

## When Isn't a VPN Suitable?

**Using your real identity online:** A VPN is unlikely to be useful when using your real-life or well-known identity. It may trigger spam and fraud detection systems, such as when logging into your bank's website.

**Requiring absolute anonymity:** A VPN will not provide complete anonymity because the provider still has access to:
- Your real IP address
- Destination website information
- Often a money trail linked back to you

"No logging" policies are merely promises. For complete safety from the network itself, consider using [Tor](https://www.privacyguides.org/en/advanced/tor-overview/) in addition to or instead of a VPN.

**Unencrypted connections:** Never trust a VPN to secure connections to unencrypted HTTP destinations. Use HTTPS to keep passwords, session tokens, and queries safe from the VPN provider and other adversaries. Enable HTTPS-only mode in your browser to mitigate downgrade attacks.

## Should I Use Encrypted DNS with a VPN?

**Probably not**, unless your VPN provider hosts the encrypted DNS servers themselves.

Using DOH/DOT (or any encrypted DNS) with third-party servers adds more entities to trust. Your VPN provider can still see which websites you visit based on IP addresses and other methods.

However, there may be advantages to enabling encrypted DNS for other browser security features like ECH. These technologies are relatively new and not yet widespread.

> **Note on DNS spoofing:** While encrypted DNS prevents DNS spoofing, your browser should already check [TLS certificates](https://en.wikipedia.org/wiki/Transport_Layer_Security#Digital_certificates) with HTTPS and warn you about issues. Without HTTPS, an adversary can modify other elements besides DNS queries anyway.

## Should I Use Tor and a VPN Together?

**Maybe.** Tor is not suitable for everyone. Consider your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/)—if your adversary cannot extract information from your VPN provider, a VPN alone may provide sufficient protection.

If you do use Tor, you are probably best off connecting to the Tor network via a commercial VPN provider. This is a complex subject covered in more detail on the [Tor overview](https://www.privacyguides.org/en/advanced/tor-overview/) page.

### VPN Providers with "Tor Nodes"

Tor currently only supports the TCP protocol. UDP (used by WebRTC, HTTP3/QUIC, and other protocols), ICMP, and other packets will be dropped. VPN providers typically route all non-TCP packets through their VPN server to compensate.

When using Tor over VPN through a provider's built-in feature, you lose control over important Tor features such as [Isolated Destination Address](https://whonix.org/wiki/Stream_Isolation) (using a different Tor circuit for every domain visited).

> **Recommendation:** This feature should be viewed as a convenient way to access hidden services on Tor, not for staying anonymous. For proper anonymity, use the actual [Tor Browser](https://www.privacyguides.org/en/tor/).

## Commercial VPN Ownership Concerns

Most VPN services are owned by a [small number of companies](https://vpnpro.com/blog/hidden-vpn-owners-unveiled-97-vpns-23-companies). These companies run many smaller VPN services to create an illusion of choice while maximizing profit. Providers feeding into shell companies typically have poor privacy policies and shouldn't be trusted with your internet traffic.

**Be strict about which provider you choose.** Also be wary that many VPN review sites are advertising vehicles open to the highest bidder.

## Modern VPN Alternatives

### Multi-Party Relays (MPRs)

MPRs use multiple nodes owned by different parties, ensuring no single party knows both who you are and what you're connecting to. This is the basic idea behind Tor, but paid services now try to emulate this model.

**Example: Apple's iCloud Private Relay**
1. **First server (Apple-operated):** Sees your device's IP and payment information tied to your Apple ID, but cannot see your destination website
2. **Second server (partner CDN like Cloudflare or Fastly):** Makes the connection to your destination but only knows Apple's server IP, not your device

This protection only exists if you trust the two companies not to collude to deanonymize you.

### Decentralized VPNs (dVPNs)

dVPNs use blockchain technology and distribute nodes across many people to eliminate trust in a single party. However, significant concerns exist:

- **Single-node defaults:** Many dVPNs default to a single node, requiring complete trust in that node—a random person rather than an auditable VPN provider with legal responsibilities
- **Multi-hop trade-offs:** Needed to solve the trust problem but comes with stability and performance costs
- **Legal liability:** Exit nodes must handle legal problems from network misuse, discouraging regular people from running nodes and making it attractive for malicious actors with resources
- **Cryptocurrency focus:** Many dVPNs prioritize pushing cryptocurrency over providing quality service
- **Vulnerability:** Smaller networks with fewer nodes are more susceptible to [Sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack)

## Additional Resources

- [The Trouble with VPN and Privacy Review Sites](https://blog.privacyguides.org/2019/11/20/the-trouble-with-vpn-and-privacy-review-sites)
- [Free VPN App Investigation](https://top10vpn.com/research/free-vpn-investigations/ownership)
- [Hidden VPN owners unveiled: 101 VPN products run by just 23 companies](https://vpnpro.com/blog/hidden-vpn-owners-unveiled-97-vpns-23-companies)
- [VPN - a Very Precarious Narrative](https://overengineer.dev/blog/2019/04/08/very-precarious-narrative.html) by Dennis Schubert
- [Privacy Guides VPN Recommendations](https://www.privacyguides.org/en/vpn/)