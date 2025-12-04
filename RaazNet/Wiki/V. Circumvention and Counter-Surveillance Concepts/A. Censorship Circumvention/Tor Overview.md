---
title: "Tor Overview"
tags: [tor, privacy, anonymity, encryption, censorship-circumvention, vpn]
category: "Privacy Networks"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, Security Researchers]
topics: ["Tor Network", "Anonymous Browsing", "Traffic Encryption", "Censorship Circumvention"]
summary: "Comprehensive guide to understanding Tor network architecture, safe connection practices, limitations, and how traffic routing provides anonymity."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic networking concepts", "Understanding of VPNs", "Familiarity with browser security"]
estimated_read_time: "15 minutes"
---

# Tor Overview

**Tor** is a free, decentralized network designed for maximum internet privacy. When used properly, it enables private and anonymous browsing and communications. Because Tor traffic is difficult to block and trace, it serves as an effective censorship circumvention tool.

Tor routes your internet traffic through volunteer-operated servers instead of making direct connections to websites. This obfuscates traffic origin, and no server in the connection path can see the complete route—meaning even the servers you connect through cannot break your anonymity.

**Resources:**
- [Tor Project Homepage](https://torproject.org/)
- [Onion Service](http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/)
- [Documentation](https://tb-manual.torproject.org/)
- [Source Code](https://gitlab.torproject.org/tpo/core/tor)

---

## Safely Connecting to Tor

Before connecting to Tor, consider what you're trying to accomplish and who you're hiding your network activity from.

### When Direct Connection is Acceptable

If you:
- Live in a free country
- Access mundane content via Tor
- Aren't worried about your ISP or local network administrators knowing you use Tor
- Want to help [destigmatize](https://2019.www.torproject.org/about/torusers.html.en) Tor usage

You can likely connect directly via [Tor Browser](https://www.privacyguides.org/en/tor/) without concern.

### When to Use VPN + Tor

Consider using a VPN before connecting to Tor if:
- You already use a [trusted VPN provider](https://www.privacyguides.org/en/vpn/)
- Your threat model includes adversaries capable of extracting information from your ISP
- Your threat model includes your ISP itself as an adversary
- Your threat model includes local network administrators

**Why VPN + Tor?**

Connecting directly to Tor makes your connection stand out. Network administrators [have detected and correlated](https://edition.cnn.com/2013/12/17/justice/massachusetts-harvard-hoax) Tor traffic to identify and deanonymize specific users. Connecting to a VPN is almost always less suspicious since commercial VPNs are used for mundane tasks like bypassing geo-restrictions.

**Recommended connection chain:**
```
You → VPN → Tor → Internet
```

From this setup:
- **Your ISP sees:** Normal VPN connection
- **Your VPN sees:** Connection to Tor network (but not which sites you visit)
- **Tor sees:** Normal connection from your VPN's IP

This provides plausible deniability and an additional layer of protection if the Tor network is compromised.

> **Note:** This is not censorship circumvention advice. If Tor is blocked by your ISP, your VPN likely is too.

### Configurations to Avoid

**Do NOT use these configurations:**
- You → Tor → VPN → Internet
- You → VPN → Tor → VPN → Internet
- Any other non-standard configuration

These configurations are sometimes recommended to evade Tor bans but are harmful because:
- Tor normally changes your circuit path frequently for security
- Choosing a permanent destination VPN eliminates this advantage
- This drastically harms your anonymity

These bad configurations require custom proxy settings—if you're using default settings, you're fine.

### VPN/SSH Fingerprinting Considerations

The Tor Project [notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorPlusVPN#vpnssh-fingerprinting) that using a VPN to hide Tor activities may not be foolproof. VPNs are vulnerable to website traffic fingerprinting, where adversaries can guess visited websites based on traffic patterns.

Encrypted Tor traffic hidden by a VPN could potentially be detected similarly. However, the benefits of using a VPN still outweigh these risks.

If you believe pluggable transports (bridges) provide additional protection, you can use a bridge **and** a VPN together.

---

## What Tor is Not

Tor has important limitations to consider when choosing your privacy solution.

### Tor is Not a Free VPN

The *Orbot* mobile app has led many to describe Tor as a "free VPN." However, this comparison is dangerous:

**Exit Node Risks:**
- Unlike VPN providers, Tor exit nodes can be _actively_ [malicious](https://www.privacyguides.org/en/advanced/tor-overview/#caveats)
- Anyone can create exit nodes, making them hotspots for network logging and modification
- In 2020, many exit nodes were documented [hijacking cryptocurrency transactions](https://therecord.media/thousands-of-tor-exit-nodes-attacked-cryptocurrency-users-over-the-past-year) by downgrading HTTPS to HTTP
- Other attacks include replacing downloads via unencrypted channels with malware

**Visibility Concerns:**
- Tor is easily identifiable on networks
- Using Tor makes you stand out as someone likely evading authorities
- Commercial VPNs provide better plausible deniability ("I was just watching Netflix")

### Tor Usage is Not Undetectable

**Even with bridges and pluggable transports**, Tor Project provides no tools to completely hide Tor usage from your ISP.

- Obfuscated transports like **obfs4** and **meek** can be [detected](https://hackerfactor.com/blog/index.php?/archives/889-Tor-0day-Burning-Bridges.html) via traffic analysis
- **Snowflake** can be [detected](https://hackerfactor.com/blog/index.php?/archives/944-Tor-0day-Snowflake.html) before a Tor connection is even established
- Other transports rely on security through obscurity

**Key distinction:** Bypassing censorship is easier than evading detection. Censorship circumvention techniques don't hide that *you specifically* are using Tor from an interested party monitoring your network.

### Tor Browser is Not the Most Secure Browser

Anonymity and security are different properties. Tor Browser is based on Firefox, and vulnerabilities can be exploited by:

1. Finding Critical/High vulnerabilities in Firefox nightly/beta builds, then checking if they're exploitable in Tor Browser (vulnerability window: weeks)
2. Chaining multiple Medium/Low vulnerabilities together (vulnerability window: months or longer)

**For high-risk users:** Consider using Whonix in [Qubes](https://www.privacyguides.org/en/os/qubes-overview/) to contain Tor browsing in a secure VM and protect against leaks.

---

## How Tor Routing Works

### Path Building to Clearnet Services

"Clearnet services" are regular websites accessible with any browser. Tor routes traffic through thousands of volunteer-run servers called nodes (or relays).

Every Tor connection chooses three nodes to build a path called a "circuit":

```
Your Device → Entry Node → Middle Node → Exit Node → Destination Website
```

#### Entry Node (Guard Node)
- First node your Tor client connects to
- **Can see:** Your IP address
- **Cannot see:** What you're connecting to
- Randomly selected and kept for 2-3 months to protect against certain attacks

#### Middle Node
- Second node in the circuit
- **Can see:** Which entry node traffic came from, which exit node it goes to
- **Cannot see:** Your IP address or destination domain
- Randomly selected for each new circuit

#### Exit Node
- Where traffic leaves Tor network and reaches your destination
- **Can see:** What site it's connecting to
- **Cannot see:** Your IP address
- Randomly selected from nodes with exit relay flag

### Path Building to Onion Services

Onion Services (hidden services) are websites only accessible via Tor Browser, with `.onion` domain names.

Traffic routes through **six** nodes total:
- Three nodes protect *your* anonymity
- Three nodes protect *the Onion Service's* anonymity (hiding the server's true IP and location)

```
Your Device → [Your 3 Nodes] → [Service's 3 Nodes] → Destination Server
```

### Encryption

Tor encrypts each packet three times with keys from the exit, middle, and entry nodes (in that order).

Each node removes its own layer of encryption. When data returns, the process reverses—each node adds its encryption layer before passing data back.

**Result:** No single party knows the entire path:
- Entry node knows who you are, not where you're going
- Middle node knows neither who you are nor your destination
- Exit node knows your destination, not who you are
- Destination server never knows your IP address

---

## Important Caveats

- **User error:** Tor never protects you from accidentally exposing your real identity
- **Traffic modification:** Exit nodes can modify unencrypted traffic. **Never** download files from unencrypted `http://` websites over Tor
- **Traffic monitoring:** Exit nodes can monitor unencrypted traffic containing personally identifiable information
- **Global adversaries:** Tor doesn't protect against adversaries who can passively watch all network traffic globally (and using Tor with a VPN doesn't change this)
- **Traffic analysis:** Well-funded adversaries watching most global network traffic may still deanonymize Tor users through advanced traffic analysis

**Recommendation:** Only use the **official** Tor Browser, designed to prevent fingerprinting.

---

## Bridges vs. VPN Protection

### Bridge Limitations

Bridges provide censorship circumvention but only offer *transient* benefits. They don't protect against historical traffic log analysis.

**Example scenario:** Your ISP wants to identify Tor users from 4 months ago. With limited metadata logging, they can see you connected to an IP later revealed as a Tor bridge—providing high confidence you were a Tor user.

### VPN Advantage

With VPN + Tor: ISP logs show only that you connected to a VPN's IP address. Since ISPs typically retain only metadata (not full traffic contents), they cannot determine what you connected to via that VPN, providing plausible deniability.

### Combined Approach

If you believe bridges aid against fingerprinting beyond what VPN encryption provides, use both together. Connect to an **obfs4 bridge** behind your VPN for optimal fingerprinting protection (rather than meek or Snowflake).

> **Note:** The [WebTunnel](https://forum.torproject.org/t/tor-relays-announcement-webtunnel-a-new-pluggable-transport-for-bridges-now-available-for-deployment/8180) pluggable transport may mitigate some bridge detection concerns—this technology is still developing.

---

## Additional Resources

- [Tor Browser User Manual](https://tb-manual.torproject.org/)
- [How Tor Works - Computerphile](https://youtube.com/watch?v=QRYzre4bf7I) (YouTube)
- [Tor Onion Services - Computerphile](https://youtube.com/watch?v=lVcbq_a5N9I) (YouTube)

---

## Technical Notes

1. **Entry guards** remain the first relay in your circuit for 2-3 months to protect against known anonymity-breaking attacks. See the Tor Project's [blog post](https://blog.torproject.org/improving-tors-anonymity-changing-guard-parameters) and [research paper](https://www-users.cs.umn.edu/~hoppernj/single_guard.pdf) on entry guards.

2. **Relay flags** are special qualifications for circuit positions (e.g., "Guard", "Exit", "BadExit"), circuit properties (e.g., "Fast", "Stable"), or roles (e.g., "Authority", "HSDir"), assigned by directory authorities. See the [glossary](https://metrics.torproject.org/glossary.html#relay-flag) for details.