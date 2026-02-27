---
title: "Anonymity Networks: Tor and I2P"
tags:
  [
    tor,
    i2p,
    anonymity,
    censorship-circumvention,
    bridges,
    webtunnel,
    snowflake,
    iran,
  ]
category: "Circumventing Censorship"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, General Public]
topics:
  [
    "Tor Network",
    "I2P",
    "Pluggable Transports",
    "Bridges",
    "Censorship Circumvention",
  ]
summary: "Comprehensive guide to using Tor and I2P for anonymity and censorship circumvention in Iran, featuring updated strategies for 2026 including WebTunnel and Snowflake."
source: "Raaznet Aggregated Resources"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of internet restrictions",
    "Installed Tor Browser or Orbot",
  ]
estimated_read_time: "15 minutes"
---

# Anonymity Networks: Tor and I2P

Standard VPNs often fail or are monitored. Anonymity networks like **Tor** and **I2P** offer a more robust layer of defense by routing traffic through a decentralized network of volunteers, making it significantly harder for the Islamic Republic to trace your activity or block your access to the global internet.

This guide focuses on safely using these networks in Iran, with specific attention to **bridges** and **obfuscation protocols** required to bypass the 2026-era blocking mechanisms.

---

## 1. The Tor Network (The Onion Router)

**Tor** is the primary tool for anonymous web browsing and censorship circumvention. It routes your traffic through three random servers (relays) worldwide, encrypting the data at each step.

### How Tor Protects You

- **Anonymity:** The website you visit cannot see your real IP address.
- **Privacy:** Your ISP (e.g., Irancell, MCI, TCI) cannot see what websites you visit; they can only see that you are using Tor (unless you use a bridge/VPN).
- **Circumvention:** By routing through other countries, you bypass local blocks on social media, news sites, and apps.

### Accessing Tor in Iran (2026 Update)

Direct connections to the Tor network are almost universally blocked in Iran. You **must** use a "Bridge" (Pluggable Transport) to disguise your Tor traffic as normal internet traffic.

#### Recommended Bridges for Iran

| Bridge Type    | Status in Iran (2026)  | Description                                                                                                                                                      |
| :------------- | :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **WebTunnel**  | **Highly Recommended** | Mimics encrypted web traffic (HTTPS/WebSocket). It is currently the most resilient method against Iran's Deep Packet Inspection (DPI) and "whitelist" filtering. |
| **Snowflake**  | **Variable**           | Uses temporary proxies run by volunteers in browsers. Effective during standard filtering but may fail during "total blackout" or aggressive whitelist phases.   |
| **obfs4**      | **Restricted**         | Standard obfuscation. Public obfs4 bridges are often blocked. Works best if you obtain a **private** bridge.                                                     |
| **Meek-Azure** | **Slow/Emergency**     | Routes traffic through Microsoft Azure. Very slow but hard to block without blocking Microsoft services.                                                         |

### How to Get Working Bridges

Since public bridges are often harvested and blocked by the censors, you need private or semi-private bridges.

1.  **Telegram Bot:**
    - Add **[@GetBridgesBot](https://t.me/GetBridgesBot)** on Telegram.
    - Type `/bridges` or specifically `/webtunnel` to get lines of code.
    - Copy the entire bridge line (starts with `webtunnel` or `obfs4`).
2.  **Email:**
    - Send an email to `bridges@torproject.org` from a Gmail or Riseup address.
    - Subject/Body: `get transport webtunnel` (or `get transport obfs4`).
3.  **Tor Browser Connection Assist:**
    - Modern versions of Tor Browser can automatically request bridges. Go to **Settings > Connection > Bridges > Request a Bridge**.

---

## 2. Using Tor on Your Devices

### Desktop (Windows, Linux, macOS)

**Tor Browser** is the only official way to use Tor on desktop.

1.  **Download:** Get the installer from a mirror site or via Telegram (`@GetTor_Bot`) if the main site is blocked.
2.  **Configure Bridge:**
    - Open Tor Browser. Click "Configure Connection".
    - Under "Bridges", select "Add a Bridge Manually" and paste the WebTunnel line you received.
    - Alternatively, select "Select a Built-in Bridge" and choose **Snowflake**.
3.  **Security Level:** Set to **"Safer"** or **"Safest"** in Privacy settings to disable JavaScript vulnerabilities.

> **Warning:** Do not install extra extensions (like ad blockers) on Tor Browser. This makes your "browser fingerprint" unique and easier to track.

### Android

**Tor Browser for Android** or **Orbot** are the standard tools.

- **Tor Browser:** Best for browsing the web.
- **Orbot:** A "VPN mode" app that routes _other_ apps (like Twitter or Telegram) through Tor.
  - _Tip:_ In Orbot settings, enable "VPN Mode" and select specific apps to route through Tor.
  - _Bridge Config:_ Tap the "onion" icon or settings to add your `WebTunnel` or `Snowflake` bridge.

### iOS (iPhone/iPad)

Use **Onion Browser**.

- It is less secure than the desktop version due to Apple's restrictions (it uses WebKit).
- It supports Snowflake and obfs4 bridges.
- **Orbot for iOS** is also available to tunnel traffic, but functionality is more limited than on Android.

---

## 3. I2P (The Invisible Internet Project)

**I2P** is a separate anonymity network. Unlike Tor, which is designed to access the "public" internet (clearnet), I2P is optimized for **hidden services** (eepsites) and peer-to-peer communication _within_ the network.

### Tor vs. I2P

| Feature          | Tor                                                         | I2P                                                                                                  |
| :--------------- | :---------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Primary Goal** | Anonymous access to the open web (Censorship Circumvention) | Resilient, internal decentralized network                                                            |
| **Routing**      | Onion Routing (Circuit of 3 nodes)                          | Garlic Routing (Packet switching, unidirectional tunnels)                                            |
| **Performance**  | Better for web browsing                                     | Better for P2P, chat, and file sharing                                                               |
| **Iran Context** | **Best for bypassing blocking** to read news/social media.  | **Best for resilient communication** if the global internet is cut off but internal mesh is working. |

### When to Use I2P in Iran

I2P is a backup communication layer. If the government implements a "Digital Curfew" or total cut-off from the international web, I2P nodes _inside_ Iran might still be able to communicate with each other, allowing for decentralized chat or file sharing without a central server.

---

## 4. Advanced Security Strategies for Iran

### The "VPN + Tor" Combination

Given the intense surveillance by Iranian ISPs, connecting directly to Tor (even with a bridge) can sometimes be flagged for Deep Packet Inspection (DPI) or simply blocked.

**Recommended Setup:** `User -> Trusted VPN -> Tor -> Internet`

1.  **Connect to a trusted VPN first** (e.g., Mullvad, IVPN, or a private Outline server).
2.  **Launch Tor Browser.**
3.  **Connect to Tor.**

**Why?**

- Your ISP sees only VPN traffic (which is common and harder to distinguish).
- The VPN provider sees you are connecting to Tor but cannot see _what_ you are doing inside Tor.
- Tor hides your destination from the VPN.

### Handling "Stealth Outages" and Whitelists

During periods like the January 2026 blackouts, Iran often blocks all traffic except domestic (NIN) IP addresses.

- **Snowflake** often fails here because the signaling servers are blocked.
- **WebTunnel** is your best bet, as it looks like traffic to a valid HTTPS site.
- **Intranets:** If international traffic is 0%, no tool will work. In these cases, look for **mesh messengers** (like Briar) or physical data exchange (Sneakernet).

### Risk Assessment

- **Correlation Attacks:** Tor does not protect against a global adversary who can see both ends of the connection. While unlikely to be a threat from the Iranian government alone for international sites, avoid logging into personal accounts (Google, Facebook) over Tor unless necessary, as this deanonymizes you to the platform.
- **Mobile Risks:** Android/iOS devices send massive amounts of telemetry. For high-risk work (whistleblowing), use **Tails OS** on a USB stick with a laptop, rather than a smartphone.

---

## 5. Summary Checklist

- [ ] **Download:** Tor Browser (Desktop) and Orbot (Android) _before_ a blackout.
- [ ] **Stockpile Bridges:** Get 5-10 fresh `webtunnel` and `obfs4` bridges from `@GetBridgesBot` and save them in a local text file.
- [ ] **VPN Backup:** Have a reliable VPN installed to act as the first hop.
- [ ] **Update:** Keep Tor Browser updated. Security flaws are dangerous.
- [ ] **Verification:** Check `https://check.torproject.org` to confirm you are successfully routed through Tor.
