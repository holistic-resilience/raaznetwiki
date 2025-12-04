```yaml
---
title: "Tor Overview"
tags: [tor, privacy, anonymity, encryption, censorship-circumvention, vpn]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, Security Researchers]
topics: ["Anonymous Browsing", "Network Privacy", "Censorship Circumvention", "Digital Security"]
summary: "Comprehensive guide to Tor network architecture, safe connection practices, limitations, and how it provides anonymous internet access."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of internet networking", "Familiarity with VPN concepts", "Basic computer literacy"]
estimated_read_time: "15 minutes"
---
```

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

Before connecting, consider what you want to accomplish and who you're hiding your network activity from.

### When Direct Connection is Acceptable

If you:
- Live in a free country
- Access mundane content via Tor
- Aren't concerned about your ISP knowing you use Tor
- Want to help [destigmatize Tor usage](https://2019.www.torproject.org/about/torusers.html.en)

...you can likely connect directly via [Tor Browser](https://www.privacyguides.org/en/tor/) without concern.

### When to Use VPN + Tor

Consider using a VPN before connecting to Tor if:
- You already use a [trusted VPN provider](https://www.privacyguides.org/en/vpn/)
- Your threat model includes adversaries capable of extracting ISP information
- Your ISP itself is an adversary
- Local network administrators pose a threat

**Why VPN + Tor?**

Connecting directly to Tor makes your connection stand out. Network administrators [have successfully](https://edition.cnn.com/2013/12/17/justice/massachusetts-harvard-hoax) detected and correlated Tor traffic to identify specific users. Commercial VPN connections are far less suspicious since they're commonly used for mundane tasks like bypassing geo-restrictions.

**Connection chain:** You → VPN → Tor → Internet

- **Your ISP sees:** Normal VPN connection
- **Your VPN sees:** Connection to Tor network (but not accessed websites)
- **Tor sees:** Normal connection from VPN's IP address

This provides plausible deniability and additional protection if the Tor network is compromised.

> **Note:** This is not censorship circumvention advice. If Tor is blocked by your ISP, your VPN likely is too.

### Configurations to Avoid

These configurations harm your anonymity:
- You → Tor → VPN → Internet
- You → VPN → Tor → VPN → Internet
- Any other non-standard configuration

Normally, Tor frequently changes your circuit path. Choosing a permanent destination VPN eliminates this advantage and drastically harms anonymity. These bad configurations require custom proxy settings—if you avoid non-default configurations, you're fine.

### VPN/SSH Fingerprinting Considerations

The Tor Project [notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorPlusVPN#vpnssh-fingerprinting) that using a VPN to hide Tor activity may not be foolproof. VPNs are vulnerable to website traffic fingerprinting, and encrypted Tor traffic hidden by a VPN could theoretically be detected via similar methods.

Despite this, the benefits of using a VPN still outweigh these risks. If you believe pluggable transports (bridges) provide additional protection, you can use a bridge **and** a VPN together.

---

## What Tor is Not

### Tor is Not a Free VPN

The _Orbot_ mobile app has led many to describe Tor as a "free VPN," but this comparison poses dangers:

**Exit Node Risks:**
- Unlike VPN providers, Tor exit nodes can be _actively_ malicious
- Anyone can create exit nodes, making them hotspots for network logging and modification
- In 2020, many exit nodes [downgraded HTTPS to HTTP](https://therecord.media/thousands-of-tor-exit-nodes-attacked-cryptocurrency-users-over-the-past-year) to hijack cryptocurrency transactions
- Other attacks include replacing downloads via unencrypted channels with malware

**Visibility Concerns:**
- Tor usage is easily identifiable on networks
- Unlike VPNs, Tor makes you stand out as someone potentially evading authorities
- A real VPN provides plausible deniability ("I was just watching Netflix")

### Tor Usage is Not Undetectable

**Even with bridges and pluggable transports**, the Tor Project provides no tools to hide Tor usage from your ISP.

- **obfs4** (obfuscates traffic to "look like nothing") can be [detected](https://hackerfactor.com/blog/index.php?/archives/889-Tor-0day-Burning-Bridges.html) with standard traffic analysis
- **meek** (uses domain fronting) can also be detected
- **Snowflake** can be [detected](https://hackerfactor.com/blog/index.php?/archives/944-Tor-0day-Snowflake.html) before a Tor connection is established

Other pluggable transports rely on security through obscurity—they're not impossible to detect, just not worth building detectors for due to low usage.

> **Critical distinction:** Bypassing censorship is easier than evading detection. These techniques don't hide that _you specifically_ are using Tor from an interested party monitoring your network.

### Tor Browser is Not the Most Secure Browser

Anonymity can be attacked through browser vulnerabilities:

1. **Zero-day exploits:** Attackers find Critical/High vulnerabilities in Firefox nightly/beta builds, then check if they're exploitable in Tor Browser (vulnerability window can last weeks)
2. **Chained exploits:** Multiple Medium/Low vulnerabilities combined to achieve desired access (vulnerability window can last months)

**Mitigation:** Those at risk should consider using Whonix in [Qubes](https://www.privacyguides.org/en/os/qubes-overview/) to contain Tor browsing in a secure VM and protect against leaks.

---

## Path Building to Clearnet Services

"Clearnet services" are websites accessible with any browser. Tor connects you anonymously by routing traffic through thousands of volunteer-run nodes (relays).

Each time you connect, Tor chooses three nodes to build a "circuit":

### The Three Nodes

| Node | What It Knows | What It Doesn't Know |
|------|---------------|---------------------|
| **Entry (Guard) Node** | Your IP address | Your destination |
| **Middle Node** | Previous and next nodes | Your IP or destination |
| **Exit Node** | Destination website | Your IP address |

**Entry Node Persistence:** The Tor client randomly selects an entry node and keeps it for 2-3 months to protect against certain attacks.

---

## Path Building to Onion Services

"Onion Services" (hidden services) are websites accessible only through Tor Browser, with `.onion` domain names.

Connecting to an Onion Service routes traffic through **six nodes**:
- Three nodes protect _your_ anonymity
- Three nodes protect _the Onion Service's_ anonymity (hiding the website's true IP and location)

---

## Encryption

Tor encrypts each packet three times with keys from the exit, middle, and entry nodes (in that order).

**How it works:**
- Each node removes its own layer of encryption
- When the destination server returns data, the process reverses
- The exit node adds its encryption layer and sends it back

**Result:** No single party knows the entire path. The entry node knows who you are but not where you're going; the middle node knows neither; the exit node knows where you're going but not who you are. The destination server never knows your IP address.

---

## Caveats

- **User error:** Tor never protects you from exposing yourself by sharing too much personal information
- **Traffic modification:** Exit nodes can modify unencrypted traffic. Never download files from unencrypted `http://` websites over Tor
- **Traffic monitoring:** Exit nodes can monitor unencrypted traffic containing personally identifiable information
- **Global adversaries:** Powerful adversaries capable of passively watching all global network traffic are not something Tor protects against (using Tor with a VPN doesn't change this)
- **Advanced traffic analysis:** Well-funded adversaries watching most global network traffic may still deanonymize Tor users

> **Recommendation:** Only use HTTPS over Tor. Use the **official** Tor Browser—it's designed to prevent fingerprinting.

---

## Bridges: Limitations and Proper Use

Tor bridges are often suggested as an alternative to VPNs for hiding Tor usage. However, bridges provide only _transient_ censorship circumvention benefits.

### The Historical Analysis Problem

**Scenario:** Your ISP wants to identify Tor users from 4 months ago.

**With bridges:** Metadata logs may show you connected to an IP later revealed as a Tor bridge. You have virtually no other excuse for such a connection.

**With VPN + Tor:** Logs show only that you connected to a VPN's IP address. Since ISPs typically retain only metadata (not full traffic contents), they cannot determine what you accessed through that VPN, providing plausible deniability.

### When to Use Bridges

- When circumventing internet censorship _in the moment_
- When all VPN providers are blocked
- In conjunction with a VPN for additional fingerprinting protection (connect to an obfs4 bridge behind your VPN)

> **Emerging technology:** [WebTunnel](https://forum.torproject.org/t/tor-relays-announcement-webtunnel-a-new-pluggable-transport-for-bridges-now-available-for-deployment/8180) pluggable transport may mitigate some of these concerns.

---

## Additional Resources

- [Tor Browser User Manual](https://tb-manual.torproject.org/)
- [How Tor Works - Computerphile](https://youtube.com/watch?v=QRYzre4bf7I) (YouTube)
- [Tor Onion Services - Computerphile](https://youtube.com/watch?v=lVcbq_a5N9I) (YouTube)

---

## Technical Notes

1. **Guard relay persistence:** The first relay ("entry guard") remains constant for 2-3 months to protect against known anonymity-breaking attacks. [More information](https://blog.torproject.org/improving-tors-anonymity-changing-guard-parameters)

2. **Relay flags:** Special qualifications for circuit positions (e.g., "Guard", "Exit", "BadExit"), circuit properties (e.g., "Fast", "Stable"), or roles (e.g., "Authority", "HSDir"), assigned by directory authorities. [Glossary](https://metrics.torproject.org/glossary.html#relay-flag)