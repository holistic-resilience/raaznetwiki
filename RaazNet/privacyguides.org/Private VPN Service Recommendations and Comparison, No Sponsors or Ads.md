---
title: "VPN Services"
tags: [vpn, wireguard, openvpn, privacy, providers]
category: "Tool Recommendations"
difficulty: "Beginner"
audience: "General Users"
topics: [network-privacy, censorship-resistance, isp-tracking]
summary: "Objective recommendations and criteria for trustworthy VPN services which enhance privacy against ISPs and local networks."
source: "https://www.privacyguides.org/en/vpn/"
content_type: "guide"
security_level: "Standard"
language: "en"
prerequisites: []
estimated_read_time: 18
---

[Skip to content](https://www.privacyguides.org/en/vpn/#recommended-providers)

![](https://www.privacyguides.org/en/assets/img/cover/vpn.webp)

# VPN Services

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/vpn.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

If you're looking for additional _privacy_ from your ISP, on a public Wi-Fi network, or while torrenting files, a **VPN** may be the solution for you.

VPNs do not provide anonymity

Using a VPN will **not** keep your browsing habits anonymous, nor will it add additional security to non-secure (HTTP) traffic.

If you are looking for **anonymity**, you should use the Tor Browser. If you're looking for added **security**, you should always ensure you're connecting to websites using HTTPS. A VPN is not a replacement for good security practices.

[Download Tor](https://torproject.org/) [Tor Myths & FAQ](https://www.privacyguides.org/en/advanced/tor-overview/)

[Detailed VPN Overview](https://www.privacyguides.org/en/basics/vpn-overview/)

## Recommended Providers

Our recommended providers use encryption, support WireGuard & OpenVPN, and have a no logging policy. Read our [full list of criteria](https://www.privacyguides.org/en/vpn/#criteria) for more information.

| Provider                                                   | Countries | WireGuard | Port Forwarding | IPv6            | Anonymous Payments |
| ---------------------------------------------------------- | --------- | --------- | --------------- | --------------- | ------------------ |
| [Mullvad](https://www.privacyguides.org/en/vpn/#mullvad)   | 49+       |           |                 |                 | Monero, Cash       |
| [IVPN](https://www.privacyguides.org/en/vpn/#ivpn)         | 37+       |           |                 | Outgoing Only   | Monero, Cash       |
| [Proton](https://www.privacyguides.org/en/vpn/#proton-vpn) | 112+      |           | Partial Support | Limited Support | Cash               |

### Proton VPN

![Proton VPN logo](https://www.privacyguides.org/en/assets/img/vpn/protonvpn.svg)

**Proton VPN** is a strong contender in the VPN space, and they have been in operation since 2016. Proton AG is based in Switzerland and offers a limited free tier, as well as a more featured premium option.

[Homepage](https://protonvpn.com/) [Privacy Policy](https://protonvpn.com/privacy-policy "Privacy Policy") [Documentation](https://protonvpn.com/support "Documentation") [Source Code](https://github.com/ProtonVPN "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=ch.protonvpn.android)
- [App Store](https://apps.apple.com/app/id1437005085)
- [GitHub](https://github.com/ProtonVPN/android-app/releases)
- [Windows](https://protonvpn.com/download-windows)
- [macOS](https://protonvpn.com/download-macos)
- [Linux](https://protonvpn.com/support/linux-vpn-setup)

#### 112 Countries

Proton VPN has [servers in 112 countries](https://protonvpn.com/vpn-servers) or [5](https://protonvpn.com/support/how-to-create-free-vpn-account) if you use their [free plan](https://protonvpn.com/free-vpn/server).

Picking a VPN provider with a server nearest to you will reduce latency of the network traffic you send. This is because of a shorter route (fewer hops) to the destination.

We also think it's better for the security of the VPN provider's private keys if they use [dedicated servers](https://en.wikipedia.org/wiki/Dedicated_hosting_service), instead of cheaper shared solutions (with other customers) such as [virtual private servers](https://en.wikipedia.org/wiki/Virtual_private_server).

#### Independently Audited

As of January 2020, Proton VPN has undergone an independent audit by SEC Consult. SEC Consult found some medium and low risk vulnerabilities in Proton VPN's Windows, Android, and iOS applications, all of which were "properly fixed" by Proton VPN before the reports were published. None of the issues identified would have provided an attacker remote access to your device or traffic. You can view individual reports for each platform at [protonvpn.com](https://protonvpn.com/blog/open-source). In April 2022 Proton VPN underwent [another audit](https://protonvpn.com/blog/no-logs-audit). A [letter of attestation](https://proton.me/blog/security-audit-all-proton-apps) was provided for Proton VPN's apps on 9th November 2021 by [Securitum](https://research.securitum.com/).

#### Open-Source Clients

Proton VPN provides the source code for their desktop and mobile clients in their [GitHub organization](https://github.com/ProtonVPN).

#### Accepts Cash

Proton VPN, in addition to accepting credit/debit cards, PayPal, and [Bitcoin](https://www.privacyguides.org/en/advanced/payments/#other-coins-bitcoin-ethereum-etc), also accepts **cash/local currency** as an anonymous form of payment.

#### WireGuard Support

Proton VPN supports the WireGuard® protocol.

#### Limited IPv6 Support

Proton [now supports IPv6](https://protonvpn.com/support/prevent-ipv6-vpn-leaks) in their browser extension and Linux client.

#### Remote Port Forwarding

Proton VPN currently only supports ephemeral remote [port forwarding](https://protonvpn.com/support/port-forwarding) via NAT-PMP.

#### Anti-Censorship

Proton VPN has their [Stealth](https://protonvpn.com/blog/stealth-vpn-protocol) protocol which may help in situations where VPN protocols like OpenVPN or WireGuard are blocked.

#### Mobile Clients

Proton VPN has published clients in major app stores and on GitHub.

How to opt out of sharing telemetry

On Android, Proton hides telemetry settings under the misleadingly labeled " **Help us fight censorship**" menu in the settings panel. On other platforms these settings can be found under the " **Usage statistics**" menu.

### IVPN

![IVPN logo](https://www.privacyguides.org/en/assets/img/vpn/ivpn.svg)

**IVPN** is another premium VPN provider, and they have been in operation since 2009.

[Homepage](https://ivpn.net/) [Privacy Policy](https://ivpn.net/privacy "Privacy Policy") [Documentation](https://ivpn.net/knowledgebase/general "Documentation") [Source Code](https://github.com/ivpn "Source Code")

### Mullvad

![Mullvad logo](https://www.privacyguides.org/en/assets/img/vpn/mullvad.svg)

**Mullvad** is a fast and inexpensive VPN with a serious focus on transparency and security.

[Homepage](https://mullvad.net/) [Onion Service](http://o54hon2e2vj6c7m3aqqu6uyece65by3vgoxxhlqlsvkmacw6a7m7kiad.onion/ "Onion Service") [Privacy Policy](https://mullvad.net/en/help/privacy-policy "Privacy Policy") [Documentation](https://mullvad.net/en/help "Documentation") [Source Code](https://github.com/mullvad "Source Code")

## Criteria

Danger

It is important to note that using a VPN provider will not make you anonymous, but it will give you better privacy in certain situations. A VPN is not a tool for illegal activities. Don't rely on a "no log" policy.

**Please note we are not affiliated with any of the providers we recommend. This allows us to provide completely objective recommendations.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements for any VPN provider wishing to be recommended.

### Technology

We require all our recommended VPN providers to provide standard configuration files which can be used in a generic, open-source client.

### Privacy

We prefer our recommended providers to collect as little data as possible.

### Security

A VPN is pointless if it can't even provide adequate security.

### Trust

We require our recommended providers to be public about their ownership or leadership.

### Marketing

With the VPN providers we recommend we like to see responsible marketing.

### Additional Functionality

While not strictly requirements, there are some factors we looked into when determining which providers to recommend.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
