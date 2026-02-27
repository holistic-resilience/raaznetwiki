---
title: "Tor and Anonymity Networks"
tags:
  [
    tor,
    anonymity,
    censorship-circumvention,
    i2p,
    bridges,
    snowflake,
    orbot,
    digital-security,
    iran,
  ]
category: "Technical Foundations"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  ["Tor Network", "Anonymity", "Censorship Circumvention", "I2P", "Bridges"]
summary: "Comprehensive guide to using Tor and I2P for anonymity and censorship circumvention in Iran, including bridge configuration and mobile tools."
source: "Aggregated from Privacy Guides, Tor Project, and Security in a Box"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of internet browsing", "Familiarity with VPN concepts"]
estimated_read_time: "15 minutes"
---

# Tor and Anonymity Networks

While VPNs primarily shift trust from your ISP to a commercial provider, **Anonymity Networks** like Tor and I2P are designed to eliminate trust in any single party, making it significantly harder for the regime to track your identity or activity.

---

## 1. The Tor Network

**Tor (The Onion Router)** is a decentralized network of volunteer-operated servers that allows users to improve their privacy and security on the Internet. It is the gold standard for anonymity and is widely used to bypass the "Filternet" in Iran.

### How Tor Works

When you use Tor, your traffic does not go directly to the destination. Instead, it is routed through a "circuit" of three random nodes (relays):

1.  **Entry Node (Guard):** The only node that knows your IP address. It does not know what website you are visiting.
2.  **Middle Node:** Takes encrypted traffic from the Guard and passes it to the Exit. It knows neither your IP nor the destination.
3.  **Exit Node:** The final node that connects to the destination website. It knows the destination but not who sent the request.

**Encryption Layering:** Tor wraps your data in three layers of encryption (like an onion). Each node peels off one layer, ensuring that no single point in the chain knows both who you are and what you are doing.

### Tor vs. VPN

| Feature         | VPN (Virtual Private Network)                    | Tor (The Onion Router)                                        |
| :-------------- | :----------------------------------------------- | :------------------------------------------------------------ |
| **Trust**       | You must trust the VPN provider not to log data. | Trust is distributed; no single node sees the full path.      |
| **Anonymity**   | Low/Medium (Provider knows your ID).             | High (Mathematical anonymity).                                |
| **Speed**       | Generally fast.                                  | Slower due to multi-hop routing.                              |
| **Primary Use** | Privacy from ISP, Streaming, General browsing.   | **Anonymity**, Whistleblowing, Bypassing advanced censorship. |

> [!TIP] The Iranian Context: Tor + VPN
> In Iran, connecting directly to Tor can flag your connection for deep packet inspection (DPI) by the ISP.
> **Recommended Setup:** Connect to a trusted **VPN first**, then open **Tor**.
>
> - **Your ISP sees:** Encrypted traffic to a VPN server.
> - **The VPN sees:** You are connecting to Tor.
> - **Tor sees:** Traffic coming from the VPN IP, not your home IP.
>
> This provides "plausible deniability" and hides the fact that you are using Tor from local surveillance.

---

## 2. Circumventing Censorship: Bridges and Pluggable Transports

The Islamic Republic frequently blocks public Tor Entry Nodes. To access the network, you must use **Bridges** (private gateways) and **Pluggable Transports** (tools that disguise Tor traffic).

### Types of Transports

1.  **Snowflake:** Currently effective in Iran. It routes your traffic through temporary proxies run by volunteers in web browsers. It is difficult to block because the IP addresses change constantly.
2.  **obfs4:** Makes Tor traffic look like random, unreadable data. While effective in many regions, sophisticated Iranian firewalls sometimes identify and throttle `obfs4`.
3.  **meek (Azure/Amazon):** Uses "domain fronting" to make traffic look like it is going to a major cloud provider (e.g., Microsoft or Amazon). It is harder to block but slower.

### How to Get Bridges

Since standard bridge distribution methods may be blocked, use these methods:

- **Telegram Bot:** Send `/bridges` to `@GetBridgesBot` on Telegram.
- **Email:** Send an email from a Gmail or Riseup address to `bridges@torproject.org` with the body text `get transport obfs4` or `get transport snowflake`.
- **Tor Browser:** Inside the browser settings, use the "Request a bridge from torproject.org" feature (requires a working initial connection or another proxy).

---

## 3. Accessing Tor: Tools and Clients

### Desktop (Windows, macOS, Linux)

**[Tor Browser](https://www.torproject.org/)** is the only official and recommended way to browse the web anonymously on a computer. It is a modified version of Firefox with privacy patches.

- **Security Levels:**
  - **Standard:** Default experience.
  - **Safer:** Disables JavaScript on non-HTTPS sites; some fonts/symbols disabled.
  - **Safest:** JavaScript disabled globally (Recommended for high-risk activities).
- **Warning:** Do not resize the Tor Browser window. Keep it at the default size to prevent "fingerprinting" (identifying you based on screen resolution).

### Android

1.  **[Tor Browser for Android](https://play.google.com/store/apps/details?id=org.torproject.torbrowser):** The official browser. Good for surfing websites anonymously.
2.  **[Orbot](https://guardianproject.info/apps/orbot/):** A powerful proxy app. It creates a local Tor connection that _other apps_ can use.
    - _Use Case:_ You can configure Telegram or Twitter to route through Orbot to bypass censorship without a centralized VPN.
    - _VPN Mode:_ Orbot offers a "VPN Mode" to route the entire device's traffic through Tor.

### iOS (iPhone/iPad)

Due to Apple's restrictions, a full official Tor Browser does not exist.

1.  **[Onion Browser](https://onionbrowser.com/):** The recommended open-source browser.
    - _Limitation:_ Does not offer the same strict anti-fingerprinting protection as the desktop version.
2.  **Orbot for iOS:** Available to help route traffic for other apps, though less flexible than the Android version.

> [!WARNING]
> Do not use "fake" Tor apps from the App Store or Play Store. Only use apps endorsed by the Tor Project (Tor Browser, Onion Browser, Orbot). Fake apps may contain malware or log your traffic.

---

## 4. Critical Security Warnings

Using Tor requires behavioral changes to remain safe.

1.  **HTTPS is Mandatory:** Tor encrypts traffic _within_ the Tor network. Once it leaves the Exit Node to reach the target website, it is decrypted. If the website does not use HTTPS, the Exit Node can read your data (passwords, messages).
2.  **No Torrenting:** Never use BitTorrent over Tor. It slows down the network for everyone and leaks your real IP address.
3.  **Don't Add Plugins:** Do not install extensions (like AdBlock) on Tor Browser. They make your browser unique and identifiable (fingerprinting).
4.  **Document Safety:** Do not open PDF or DOC files downloaded via Tor while online. They may contain scripts that "phone home" and reveal your real IP. Download them, disconnect from the internet, and then open them.
5.  **Logins:** Logging into real-identity accounts (Gmail, Facebook) over Tor prevents the ISP from knowing you are there, but the service provider (Google/Facebook) will know you are using Tor. This may trigger security lockouts.

---

## 5. Onion Services (The Dark Web)

Tor allows websites to host content without revealing the server's location via **Onion Services** (addresses ending in `.onion`).

- **Traffic flows entirely inside the Tor network.**
- The traffic never hits a public "Exit Node," meaning it is end-to-end encrypted and metadata-free.
- This is ideal for whistleblowing platforms (e.g., SecureDrop) or accessing mirrors of blocked news sites (e.g., BBC or DW onion sites).

---

## 6. I2P (Invisible Internet Project)

**I2P** is an alternative anonymous network. Unlike Tor, which focuses on accessing the public internet anonymously, I2P is designed primarily as a closed, hidden ecosystem.

| Feature            | Tor                                          | I2P                                     |
| :----------------- | :------------------------------------------- | :-------------------------------------- |
| **Design Goal**    | Anonymous access to the open web (Clearnet). | Secure, internal communication network. |
| **Routing**        | Onion Routing (Circuit based).               | Garlic Routing (Packet switching).      |
| **Performance**    | Optimized for web browsing.                  | Optimized for hidden services and P2P.  |
| **P2P/Torrenting** | **Do not use.**                              | **Supported and effective.**            |

**When to use I2P in Iran:**

- For peer-to-peer file sharing or chat services that must remain entirely within a darknet environment.
- If Tor is temporarily blocked or heavily throttled, I2P's different traffic signature may provide a backup communication channel.

---

## 7. Contributing: Running a Snowflake Proxy

If you have access to uncensored internet (e.g., a VPS abroad or friends outside Iran), you can help Iranians connect to Tor by running a **Snowflake Proxy**.

1.  Install the Snowflake extension on Chrome or Firefox.
2.  Toggle the switch to "On".
3.  Your browser becomes a temporary bridge for censored users.

_Note: This does not compromise your privacy; you are only acting as a conduit for encrypted data._

---

## Summary Recommendation

- **For maximum anonymity:** Use **Tor Browser (Desktop)** with the security level set to "Safer" or "Safest".
- **For bypassing censorship on Android:** Use **Orbot** in VPN mode or **Tor Browser**.
- **If Tor is blocked:** Request **Bridges** (specifically Snowflake or obfs4) via Telegram or Email.
- **For file sharing:** Use **I2P** or **OnionShare**, never Tor.
