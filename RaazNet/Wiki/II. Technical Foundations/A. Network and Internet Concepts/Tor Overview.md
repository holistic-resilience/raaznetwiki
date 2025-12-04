```yaml
---
title: "Tor Overview"
tags: [tor, privacy, anonymity, censorship-circumvention, vpn, onion-services]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, Security Researchers]
topics: ["Tor Network", "Anonymous Browsing", "Censorship Circumvention", "Network Security"]
summary: "Comprehensive guide to understanding Tor, including how it works, safe connection practices, limitations, and when to use VPNs alongside Tor."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of internet networking", "Familiarity with VPN concepts", "Basic computer literacy"]
estimated_read_time: "15 minutes"
---
```

# Tor Overview

**Tor** is a free, decentralized network designed for using the internet with maximum privacy. When used properly, it enables private and anonymous browsing and communications. Because Tor traffic is difficult to block and trace, it serves as an effective censorship circumvention tool.

Tor works by routing your internet traffic through volunteer-operated servers instead of making a direct connection to your destination site. This obfuscates where traffic originates, and no server in the connection path can see the complete route—meaning even the servers you use to connect cannot break your anonymity.

**Official Resources:**
- [Tor Project Homepage](https://torproject.org/)
- [Onion Service](http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/)
- [Documentation](https://tb-manual.torproject.org/)
- [Source Code](https://gitlab.torproject.org/tpo/core/tor)

---

## Safely Connecting to Tor

Before connecting to Tor, carefully consider your objectives and who you're trying to hide your network activity from.

### When Direct Connection is Acceptable

If you:
- Live in a free country
- Access mundane content via Tor
- Aren't worried about your ISP or local network administrators knowing you use Tor
- Want to help [destigmatize](https://2019.www.torproject.org/about/torusers.html.en) Tor usage

...you can likely connect to Tor directly via [Tor Browser](https://www.privacyguides.org/en/tor/) without concern.

### When to Use a VPN with Tor

Consider using a VPN before connecting to Tor if:
- You already use a [trusted VPN provider](https://www.privacyguides.org/en/vpn/)
- Your threat model includes adversaries capable of extracting information from your ISP
- Your threat model includes your ISP itself as an adversary
- Your threat model includes local network administrators

**Why this matters:** Connecting directly to Tor makes your connection stand out to local network administrators or your ISP. This traffic [has been detected](https://edition.cnn.com/2013/12/17/justice/massachusetts-harvard-hoax) in the past to identify and deanonymize specific Tor users. Commercial VPN connections are far less suspicious because everyday consumers use them for mundane tasks like bypassing geo-restrictions.

### Recommended Connection Chain

Connect to a VPN first, then access Tor normally:

```
You → VPN → Tor → Internet
```

**From each perspective:**
- **Your ISP:** Sees normal VPN traffic
- **Your VPN:** Sees you connecting to Tor, but not what websites you access
- **Tor network:** Sees a normal connection; if compromised, only your VPN's IP is exposed

This is **not** censorship circumvention advice—if Tor is blocked by your ISP, your VPN likely is too. This recommendation aims to make your traffic blend in with commonplace VPN traffic and provide plausible deniability.

### Configurations to Avoid

**Do not use these configurations:**
- You → Tor → VPN → Internet
- You → VPN → Tor → VPN → Internet
- Any other non-standard configuration

Some sources recommend these to evade Tor bans (exit nodes blocked by websites), but they harm your anonymity. Normally, Tor frequently changes your circuit path. Choosing a permanent destination VPN eliminates this advantage.

These bad configurations require custom proxy settings inside Tor Browser or your VPN client. As long as you avoid non-default configurations, you're fine.

### VPN/SSH Fingerprinting Consideration

The Tor Project [notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorPlusVPN#vpnssh-fingerprinting) that using a VPN to hide Tor activities may not be foolproof. VPNs can be vulnerable to website traffic fingerprinting, where adversaries guess visited websites based on traffic patterns.

Encrypted Tor traffic hidden by a VPN could potentially be detected via similar methods. No research papers exist on this subject, and we consider VPN benefits to outweigh these risks, but it's worth keeping in mind.

If you believe pluggable transports (bridges) provide additional protection, you can use a bridge **and** a VPN together.

---

## What Tor is Not

Tor is not perfect for all privacy scenarios. Consider these limitations when deciding if Tor is appropriate for your needs.

### Tor is Not a Free VPN

The *Orbot* mobile app has led many to describe Tor as a "free VPN" for all device traffic. However, this poses dangers:

**Exit Node Risks:**
- Unlike VPN providers, Tor exit nodes can be *actively* malicious
- Anyone can create exit nodes, making them hotspots for network logging and modification
- In 2020, many exit nodes were documented [downgrading HTTPS to HTTP](https://therecord.media/thousands-of-tor-exit-nodes-attacked-cryptocurrency-users-over-the-past-year) to hijack cryptocurrency transactions
- Other attacks include replacing downloads via unencrypted channels with malware
- HTTPS mitigates these threats to an extent

**Perception Issues:**
- Tor is easily identifiable on networks
- Using Tor makes you stand out as someone potentially evading authorities
- Commercial VPNs provide plausible deniability ("I was just watching Netflix")

### Tor Usage is Not Undetectable

**Even with bridges and pluggable transports,** the Tor Project provides no tools to hide Tor usage from your ISP. Even obfuscated "pluggable transports" or non-public bridges don't hide that you're using a private communications channel.

**Detection capabilities:**
- **obfs4** (obfuscates traffic to "look like nothing"): Can be [detected](https://hackerfactor.com/blog/index.php?/archives/889-Tor-0day-Burning-Bridges.html) via standard traffic analysis
- **meek** (uses domain fronting): Similarly detectable
- **Snowflake**: Can be [easily detected](https://hackerfactor.com/blog/index.php?/archives/944-Tor-0day-Snowflake.html) *before* a Tor connection is established
- **Other transports**: Rely on security through obscurity; not worth building detectors for due to low usage

**Key distinction:** Bypassing censorship is easier than evading detection. Censorship circumvention techniques don't hide that *you specifically* are using Tor from an interested party monitoring your network.

### Tor Browser is Not the Most Secure Browser

Adversaries targeting Tor Browser users can:
1. Find new Critical/High vulnerabilities in Firefox nightly or beta builds, then check exploitability in Tor Browser (vulnerability window can last weeks)
2. Chain multiple Medium/Low vulnerabilities until achieving desired access (vulnerability window can last months or longer)

**Additional protection:** Those at risk should consider using Whonix in [Qubes](https://www.privacyguides.org/en/os/qubes-overview/) to contain Tor browsing in a secure virtual machine and protect against leaks.

---

## How Tor Routing Works

### Path Building to Clearnet Services

"Clearnet services" are websites accessible with any browser. Tor connects you anonymously by routing traffic through thousands of volunteer-run servers called nodes (or relays).

Each connection builds a path through three nodes—called a "circuit":

**1. Entry Node (Guard Node)**
- First node your Tor client connects to
- Can see your IP address
- Cannot see what you're connecting to
- Randomly selected and kept for 2-3 months to protect against certain attacks

**2. Middle Node**
- Second node in the circuit
- Sees which node traffic came from (entry) and where it goes next
- Cannot see your IP address or destination domain
- Randomly selected for each new circuit

**3. Exit Node**
- Point where your traffic leaves Tor and reaches your destination
- Cannot see your IP address
- Knows what site it's connecting to
- Randomly chosen from nodes with exit relay flags

### Path Building to Onion Services

"Onion Services" (hidden services) are websites only accessible via Tor Browser, with `.onion` domain names.

Connecting to an Onion Service routes traffic through **six nodes**:
- Three nodes protect *your* anonymity
- Three nodes protect *the Onion Service's* anonymity (hiding the website's true IP and location)

### Encryption

Tor encrypts each packet three times with keys from the exit, middle, and entry nodes (in that order).

Each node removes its own encryption layer. When the destination returns data, the process reverses. This ensures:
- **Entry node:** Knows who you are, not where you're going
- **Middle node:** Knows neither who you are nor where you're going
- **Exit node:** Knows where you're going, not who you are
- **Destination server:** Never knows your IP address

---

## Important Caveats

- Tor **never protects** you from exposing yourself by mistake (sharing too much personal information)
- Exit nodes can **modify** unencrypted traffic—**never** download from unencrypted `http://` websites over Tor
- Exit nodes can **monitor** unencrypted traffic containing personally identifiable information
- **Always use HTTPS** over Tor; ensure your browser upgrades HTTP traffic automatically
- **Global Passive Adversaries** (capable of watching all network traffic globally) are not something Tor protects against—using a VPN doesn't change this
- Well-funded adversaries watching *most* global network traffic may still deanonymize Tor users through advanced traffic analysis

**Recommendation:** Use only the **official Tor Browser**—it's designed to prevent fingerprinting.

---

## Bridges vs. VPNs

### Limitations of Bridges

Tor bridges are often suggested as alternatives to VPNs for hiding Tor usage. While bridges may provide adequate censorship circumvention, this is only a *transient* benefit.

**The problem with historical analysis:**

If your ISP wants to identify Tor users from 4 months ago, and you used a bridge, their metadata logs may show you connected to an IP later revealed as a Tor bridge. You have virtually no other excuse for such a connection.

**Contrast with VPN usage:**

With a VPN, logs would only show you connected to a VPN's IP address. Since ISPs typically retain only metadata (not full traffic contents), they cannot determine what you connected to via that VPN after the fact.

### When to Use Bridges

Bridges provide the most benefit for circumventing censorship *in the moment*, but aren't adequate substitutes for VPN benefits. Use bridges when:
- All VPN providers are blocked
- You want additional protection alongside a VPN

**If combining bridge + VPN:** Connect to an obfs4 bridge behind your VPN for optimal fingerprinting protection (rather than meek or Snowflake).

**Note:** The [WebTunnel](https://forum.torproject.org/t/tor-relays-announcement-webtunnel-a-new-pluggable-transport-for-bridges-now-available-for-deployment/8180) pluggable transport may mitigate some concerns—this technology is still developing.

---

## Additional Resources

- [Tor Browser User Manual](https://tb-manual.torproject.org/)
- [How Tor Works - Computerphile](https://youtube.com/watch?v=QRYzre4bf7I) (YouTube)
- [Tor Onion Services - Computerphile](https://youtube.com/watch?v=lVcbq_a5N9I) (YouTube)

---

## Technical Notes

1. **Guard Relay Selection:** The first relay ("entry guard" or "guard") is a fast, stable relay that remains first in your circuit for 2-3 months to protect against known anonymity-breaking attacks. See the Tor Project's [blog post](https://blog.torproject.org/improving-tors-anonymity-changing-guard-parameters) and [research paper](https://www-users.cs.umn.edu/~hoppernj/single_guard.pdf) on entry guards.

2. **Relay Flags:** Special qualifications for circuit positions (e.g., "Guard", "Exit", "BadExit"), circuit properties (e.g., "Fast", "Stable"), or roles (e.g., "Authority", "HSDir"), assigned by directory authorities. See the [glossary](https://metrics.torproject.org/glossary.html#relay-flag).