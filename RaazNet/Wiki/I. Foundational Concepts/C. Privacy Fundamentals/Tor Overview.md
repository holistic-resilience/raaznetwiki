```yaml
---
title: "Tor Overview"
tags: [tor, privacy, anonymity, encryption, censorship-circumvention, vpn]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, Security Researchers]
topics: ["Tor Network", "Anonymous Browsing", "Censorship Circumvention", "Network Privacy"]
summary: "Comprehensive guide to the Tor network covering how it works, safe connection practices, limitations, and integration with VPNs."
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

Tor works by routing your internet traffic through volunteer-operated servers instead of making a direct connection to your destination site. This obfuscates where traffic originates, and no server in the connection path can see the full route—meaning even the servers you use to connect cannot break your anonymity.

**Resources:**
- [Tor Project Homepage](https://torproject.org/)
- [Onion Service](http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/)
- [Documentation](https://tb-manual.torproject.org/)
- [Source Code](https://gitlab.torproject.org/tpo/core/tor)

---

## Safely Connecting to Tor

Before connecting to Tor, consider what you're trying to accomplish and who you're trying to hide your network activity from.

### When Direct Connection is Appropriate

If you:
- Live in a free country
- Access mundane content via Tor
- Aren't worried about your ISP knowing you use Tor
- Want to help [destigmatize](https://2019.www.torproject.org/about/torusers.html.en) Tor usage

...you can likely connect directly via [Tor Browser](https://www.privacyguides.org/en/tor/) without concern.

### When to Use VPN + Tor

Consider using a VPN before connecting to Tor if:
- You already use a [trusted VPN provider](https://www.privacyguides.org/en/vpn/)
- Your threat model includes adversaries capable of extracting information from your ISP
- Your threat model includes your ISP itself as an adversary
- Your threat model includes local network administrators

Connecting directly to Tor makes your connection stand out to network administrators or your ISP. This traffic [has been detected](https://edition.cnn.com/2013/12/17/justice/massachusetts-harvard-hoax) in the past to identify and deanonymize Tor users. Connecting to a VPN is almost always less suspicious since commercial VPNs are used for mundane tasks like bypassing geo-restrictions.

### Recommended Configuration

Connect to a VPN first, then access Tor normally. This creates:

```
You → VPN → Tor → Internet
```

**From your ISP's perspective:** You're accessing a VPN normally.
**From your VPN's perspective:** You're connecting to the Tor network, but not what sites you access.
**From Tor's perspective:** You're connecting normally, but only your VPN's IP would be exposed in a compromise scenario.

> **Note:** This is not censorship circumvention advice. If Tor is blocked by your ISP, your VPN likely is too. This recommendation aims to make your traffic blend in with typical VPN usage and provide plausible deniability.

### Configurations to Avoid

The following configurations are **not recommended:**
- You → Tor → VPN → Internet
- You → VPN → Tor → VPN → Internet
- Any other non-standard configuration

Some sources recommend these to evade Tor bans, but they harm your anonymity. Normally, Tor frequently changes your circuit path. Choosing a permanent destination VPN eliminates this advantage.

These bad configurations require deliberately setting up custom proxy settings—you won't create them accidentally.

### VPN/SSH Fingerprinting Considerations

The Tor Project [notes](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorPlusVPN#vpnssh-fingerprinting) that using a VPN to hide Tor activities may not be foolproof. VPNs can be vulnerable to website traffic fingerprinting. Encrypted Tor traffic hidden by a VPN could theoretically be detected via similar methods.

However, the benefits of using a VPN still outweigh these risks. If you believe pluggable transports (bridges) provide additional protection, you can use a bridge **and** a VPN together.

---

## What Tor is Not

Tor has drawbacks that should be carefully considered when choosing your privacy solution.

### Tor is Not a Free VPN

The _Orbot_ mobile app has led some to describe Tor as a "free VPN." This comparison poses dangers:

**Exit Node Risks:**
- Unlike VPN providers, Tor exit nodes can be _actively_ malicious
- Anyone can create exit nodes, making them hotspots for network logging and modification
- In 2020, many exit nodes were documented [downgrading HTTPS to HTTP](https://therecord.media/thousands-of-tor-exit-nodes-attacked-cryptocurrency-users-over-the-past-year) to hijack cryptocurrency transactions
- Other attacks include replacing downloads via unencrypted channels with malware

**Visibility:**
- Tor is easily identifiable on the network
- Using Tor makes you stand out as someone likely attempting to evade authorities
- Commercial VPNs provide plausible deniability ("I was just watching Netflix")

### Tor Usage is Not Undetectable

**Even with bridges and pluggable transports,** the Tor Project doesn't provide tools to completely hide Tor usage from your ISP.

- obfs4 (obfuscates traffic to "look like nothing") can be [detected](https://hackerfactor.com/blog/index.php?/archives/889-Tor-0day-Burning-Bridges.html) via traffic analysis
- meek (uses domain fronting) can also be detected
- Snowflake can be [detected](https://hackerfactor.com/blog/index.php?/archives/944-Tor-0day-Snowflake.html) before a Tor connection is established

**Key distinction:** Bypassing censorship is easier than evading detection. These techniques may circumvent blocks but don't hide that you specifically are using Tor from a targeted adversary.

### Tor Browser is Not the Most Secure Browser

Adversaries can exploit Tor Browser by:
1. Finding new Critical/High vulnerabilities in Firefox nightly/beta builds and checking if they're exploitable in Tor Browser (vulnerability period can last weeks)
2. Chaining multiple Medium/Low vulnerabilities together (vulnerability period can last months or longer)

Those at risk of browser vulnerabilities should consider additional protections like using Whonix in [Qubes](https://www.privacyguides.org/en/os/qubes-overview/) to contain Tor browsing in a secure VM.

---

## How Tor Builds Paths

### Connecting to Clearnet Services

"Clearnet services" are regular websites accessible with any browser. Tor routes your traffic through thousands of volunteer-run servers called nodes (or relays).

Every connection chooses three nodes to build a "circuit":

**Entry Node (Guard Node)**
- First node your Tor client connects to
- Can see your IP address but not your destination
- Randomly selected and maintained for 2-3 months to protect against certain attacks

**Middle Node**
- Second node in the circuit
- Sees which entry node traffic came from and which exit node it goes to
- Cannot see your IP address or destination domain
- Randomly selected for each new circuit

**Exit Node**
- Where your traffic leaves the Tor network
- Cannot see your IP address but knows the destination site
- Chosen randomly from nodes with an exit relay flag

### Connecting to Onion Services

Onion Services (hidden services) are websites only accessible via Tor Browser, with `.onion` domain names.

Connecting to an Onion Service routes traffic through **six** nodes total:
- Three nodes protect your anonymity
- Three nodes protect the Onion Service's anonymity (hiding its true IP and location)

### Encryption

Tor encrypts each packet three times with keys from the exit, middle, and entry nodes (in that order).

Each node removes its own layer of encryption. When the destination returns data, the process reverses. The exit node adds its encryption layer and sends it back through the circuit.

**Result:** No single party knows the entire path. The entry node knows who you are but not your destination; the middle node knows neither; the exit node knows your destination but not your identity.

---

## Important Caveats

- Tor **never protects you** from exposing yourself by mistake (sharing too much personal information)
- Tor exit nodes can **modify unencrypted traffic**—never download from unencrypted `http://` websites over Tor
- Tor exit nodes can **monitor unencrypted traffic**—always use HTTPS
- **Global Passive Adversaries** (those who can watch all network traffic globally) are not something Tor protects against
- Well-funded adversaries with capability to watch most network traffic may still deanonymize users through advanced traffic analysis

**Recommendation:** Only use the **official** Tor Browser for web browsing—it's designed to prevent fingerprinting.

---

## Bridges vs. VPNs

Tor bridges are often suggested as an alternative to VPNs for hiding Tor usage. However, bridges provide only **transient** benefits for censorship circumvention.

**The Problem:**
Bridges don't protect you from historical traffic log analysis. If your ISP later identifies a bridge IP you connected to, they can conclude with high confidence you were a Tor user.

**VPN Advantage:**
With a VPN, your ISP would only see you connected to a VPN's IP address. Since ISPs typically retain only metadata (not full traffic contents), they cannot determine what you connected to via that VPN, providing plausible deniability.

**When Bridges Are Appropriate:**
- When all VPN providers are blocked
- For circumventing censorship in the moment
- In conjunction with a VPN for additional fingerprinting protection (obfs4 bridge recommended)

> **Note:** [WebTunnel](https://forum.torproject.org/t/tor-relays-announcement-webtunnel-a-new-pluggable-transport-for-bridges-now-available-for-deployment/8180), a new pluggable transport being trialed, may mitigate some of these concerns.

---

## Additional Resources

- [Tor Browser User Manual](https://tb-manual.torproject.org/)
- [How Tor Works - Computerphile](https://youtube.com/watch?v=QRYzre4bf7I) (YouTube)
- [Tor Onion Services - Computerphile](https://youtube.com/watch?v=lVcbq_a5N9I) (YouTube)

---

## References

1. The first relay in your circuit is called an "entry guard" or "guard"—a fast and stable relay that remains first in your circuit for 2-3 months to protect against known anonymity-breaking attacks. See: [Tor Blog on Guard Parameters](https://blog.torproject.org/improving-tors-anonymity-changing-guard-parameters) and [Entry Guards Paper](https://www-users.cs.umn.edu/~hoppernj/single_guard.pdf)

2. Relay flags are special qualifications for circuit positions (e.g., "Guard", "Exit", "BadExit"), circuit properties (e.g., "Fast", "Stable"), or roles (e.g., "Authority", "HSDir"), as assigned by directory authorities. See: [Tor Metrics Glossary](https://metrics.torproject.org/glossary.html#relay-flag)