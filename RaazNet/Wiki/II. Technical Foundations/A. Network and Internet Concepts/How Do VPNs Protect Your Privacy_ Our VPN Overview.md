---
title: "VPN Overview: How VPNs Protect Your Privacy"
tags: [vpn, privacy, encryption, network-security, internet-privacy, anonymity]
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
estimated_read_time: "12 minutes"
---

# VPN Overview

Virtual Private Networks are a way of extending the end of your network to exit somewhere else in the world.

Normally, an ISP can see the flow of internet traffic entering and exiting your network termination device (i.e., modem). Encryption protocols such as HTTPS are commonly used on the internet, so they may not be able to see exactly what you're posting or reading, but they can get an idea of the domains you request.

Using a VPN hides even this information from your ISP by shifting the trust you place in your network to a server somewhere else in the world. As a result, the ISP then only sees that you are connected to a VPN and nothing about the activity that you're passing through it.

> **Note:** When we refer to "Virtual Private Networks" on this website, we are usually referring to **commercial** VPN providers, who you pay a monthly fee to in exchange for routing your internet traffic securely through their public servers. There are many other forms of VPN, such as ones you host yourself or ones operated by workplaces which allow you to securely connect to internal/employee network resources. However, these VPNs are usually designed for accessing remote networks securely, rather than protecting the privacy of your internet connection.

## How Does a VPN Work?

VPNs encrypt your traffic between your device and a server owned by your VPN provider. From the perspective of anyone between you and the VPN server, it looks like you're connecting to the VPN server. From the perspective of anyone between the VPN server and your destination site, all they can see is the VPN server connecting to the website.

**Traffic Flow:**
```
Your Device (with VPN Client) → [Encrypted] → VPN Server → The Internet → Your Destination
```

Note that a VPN does not add any security or encryption to your traffic between the VPN server and your destination on the internet. To access a website securely, you **must** still ensure HTTPS is in use regardless of whether you use a VPN.

## Should I Use a VPN?

**Yes**, almost certainly. A VPN has many advantages, including:

1. Hiding your traffic from **only** your Internet Service Provider
2. Hiding your downloads (such as torrents) from your ISP and anti-piracy organizations
3. Hiding your IP from third-party websites and services, helping you blend in and preventing IP-based tracking
4. Allowing you to bypass geo-restrictions on certain content

VPNs can provide *some* of the same benefits Tor provides, such as hiding your IP from the websites you visit and geographically shifting your network traffic. Good VPN providers will not cooperate with legal authorities from oppressive regimes, especially if you choose a VPN provider outside your own jurisdiction.

### VPN Limitations

VPNs cannot encrypt data outside the connection between your device and the VPN server. VPN providers can also see and modify your traffic the same way your ISP could, so there is still a level of trust you are placing in them. There is no way to verify a VPN provider's "no logging" policies in any way.

## When Isn't a VPN Suitable?

Using a VPN in cases where you're using your real-life or well-known identity online is unlikely to be useful. Doing so may trigger spam and fraud detection systems, such as if you were to log into your bank's website.

It's important to remember that a VPN will not provide you with absolute anonymity because the VPN provider itself will still have access to your real IP address, destination website information, and often a money trail that can be linked directly back to you. "No logging" policies are merely a promise; if you need complete safety from the network itself, consider using Tor in addition to or instead of a VPN.

You also should not trust a VPN to secure your connection to an unencrypted, HTTP destination. In order to keep what you actually do on the websites you visit private and secure, you must use HTTPS. This will keep your passwords, session tokens, and queries safe from the VPN provider and other potential adversaries in between the VPN server and your destination. You should enable HTTPS-only mode in your browser (if supported) to mitigate attacks which try to downgrade your connection from HTTPS to HTTP.

## Should I Use Encrypted DNS with a VPN?

Unless your VPN provider hosts the encrypted DNS servers themselves, **probably not**. Using DOH/DOT (or any other form of encrypted DNS) with third-party servers will simply add more entities to trust. Your VPN provider can still see which websites you visit based on the IP addresses and other methods.

That said, there may be some advantages to enabling encrypted DNS in order to enable other security features in your browser, such as ECH. Browser technologies which are reliant on in-browser encrypted DNS are relatively new and not yet widespread.

Another common reason encrypted DNS is recommended is that it prevents DNS spoofing. However, your browser should already be checking for TLS certificates with **HTTPS** and warn you about it. If you are not using **HTTPS**, then an adversary can still just modify anything other than your DNS queries and the end result will be little different.

## Should I Use Tor and a VPN?

Maybe. Tor is not necessarily suitable for everybody in the first place. Consider your threat model, because if your adversary is not capable of extracting information from your VPN provider, using a VPN alone may provide enough protection.

If you do use Tor, you are *probably* best off connecting to the Tor network via a commercial VPN provider. However, this is a complex subject.

### VPN Providers with "Tor Nodes"

Currently, Tor only supports the TCP protocol. UDP (used by WebRTC, HTTP3/QUIC, and other protocols), ICMP, and other packets will be dropped. To compensate for this, VPN providers typically will route all non-TCP packets through their VPN server (your first hop). Additionally, when using this Tor over VPN setup, you do not have control over other important Tor features such as Isolated Destination Address (using a different Tor circuit for every domain you visit).

The feature should be viewed as a *convenient* way to access hidden services on Tor, not to stay anonymous. For proper anonymity, use the actual Tor Browser.

## Commercial VPN Ownership

Most VPN services are owned by the same few companies. These companies run lots of smaller VPN services to create the illusion that you have more choice than you actually do and to maximize profit. Typically, these providers that feed into their shell company have terrible privacy policies and shouldn't be trusted with your internet traffic. You should be very strict about which provider you decide to use.

You should also be wary that many VPN review sites are merely advertising vehicles open to the highest bidder.

## Modern VPN Alternatives

Recently, some attempts have been made by various organizations to address issues which centralized VPNs have. These technologies are relatively new, but worth keeping an eye on as the field develops.

### Multi-Party Relays (MPRs)

Multi-Party Relays use multiple nodes owned by different parties, such that no individual party knows both who you are and what you're connecting to. This is the basic idea behind Tor, but now there are some paid services that try to emulate this model.

**Example: Apple's iCloud Private Relay**

1. **First server** (operated by Apple): Can see your device's IP when you connect to it, and has knowledge of your payment information and Apple ID tied to your iCloud subscription. However, it is unable to see what website you are connecting to.

2. **Second server** (operated by a partner CDN, such as Cloudflare or Fastly): Actually makes the connection to your destination website, but has no knowledge of your device. The only IP address it knows about is Apple's server's.

This protection by segmentation only exists if you trust the two companies to not collude with each other to deanonymize you.

### Decentralized VPNs (dVPNs)

Another attempt at solving the issues with centralized VPN services are dVPNs. These are based on blockchain technology and claim to eliminate trust in a single party by distributing the nodes across lots of different people.

**Concerns with dVPNs:**

- Many times a dVPN will default to a single node, meaning you need to trust that node completely, just like a traditional VPN
- Unlike a traditional VPN, this one node that can see all your traffic is a random person instead of your VPN provider that can be audited and has legal responsibilities
- Multi-hop is needed to solve this, but that comes with a stability and performance cost
- The exit node will need to deal with legal problems from misuse of the network, discouraging regular people from running nodes
- This makes it more attractive for a malicious actor with lots of resources to host one
- Many dVPNs are used to push a cryptocurrency rather than to make the best service
- They tend to be smaller networks with fewer nodes, making them more vulnerable to Sybil attacks

## Related Resources

- [The Trouble with VPN and Privacy Review Sites](https://blog.privacyguides.org/2019/11/20/the-trouble-with-vpn-and-privacy-review-sites)
- [Free VPN App Investigation](https://top10vpn.com/research/free-vpn-investigations/ownership)
- [Hidden VPN owners unveiled: 101 VPN products run by just 23 companies](https://vpnpro.com/blog/hidden-vpn-owners-unveiled-97-vpns-23-companies)
- [VPN - a Very Precarious Narrative](https://overengineer.dev/blog/2019/04/08/very-precarious-narrative.html) by Dennis Schubert