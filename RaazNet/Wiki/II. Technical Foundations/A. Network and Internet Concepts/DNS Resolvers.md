[Skip to content](https://www.privacyguides.org/en/dns/#recommended-providers)

![](https://www.privacyguides.org/en/assets/img/cover/dns.webp)

# DNS Resolvers

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/dns.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

Encrypted **DNS** with third-party servers should only be used to get around basic [DNS blocking](https://en.wikipedia.org/wiki/DNS_blocking) when you can be sure there won't be any consequences. Encrypted DNS will not help you hide any of your browsing activity.

[Learn more about DNS](https://www.privacyguides.org/en/advanced/dns-overview/)

## Recommended Providers

These are our favorite public DNS resolvers based on their privacy and security characteristics, and their worldwide performance. Some of these services offer basic DNS-level blocking of malware or trackers depending on the server you choose, but if you want to be able to see and customize what is blocked, you should use a dedicated DNS filtering product instead.

| DNS Provider | Protocols | Logging / Privacy Policy | [ECS](https://www.privacyguides.org/en/advanced/dns-overview/#what-is-edns-client-subnet-ecs) | Filtering | Signed Apple Profile |
| --- | --- | --- | --- | --- | --- |
| [**DNS0.eu**](https://dns0.eu/) | Cleartext <br>DoH/3 <br>DoH<br>DoT<br>DoQ | Anonymized[4](https://www.privacyguides.org/en/dns/#fn:4) | Anonymized | Based on server choice. | Yes |
| [**Cloudflare**](https://developers.cloudflare.com/1.1.1.1/setup) | Cleartext <br>DoH/3 <br>DoT | Anonymized[2](https://www.privacyguides.org/en/dns/#fn:2) | No | Based on server choice. | No |
| [**Quad9**](https://quad9.net/) | Cleartext <br>DoH<br>DoT<br>DNSCrypt | Anonymized[6](https://www.privacyguides.org/en/dns/#fn:6) | Optional | Based on server choice. Malware blocking is included by default. | Yes <br>[iOS](https://docs.quad9.net/Setup_Guides/iOS/iOS_14_and_later_(Encrypted))<br>[macOS](https://docs.quad9.net/Setup_Guides/MacOS/Big_Sur_and_later_(Encrypted)) |
| [**AdGuard Public DNS**](https://adguard-dns.io/en/public-dns.html) | Cleartext <br>DoH/3 <br>DoT<br>DoQ<br>DNSCrypt | Anonymized[1](https://www.privacyguides.org/en/dns/#fn:1) | Anonymized | Based on server choice. Filter list being used can be found here. | Yes |
| [**Control D Free DNS**](https://controld.com/free-dns) | Cleartext <br>DoH/3 <br>DoT<br>DoQ | No[3](https://www.privacyguides.org/en/dns/#fn:3) | No | Based on server choice. | Yes <br>[iOS](https://docs.controld.com/docs/ios-platform)<br>[macOS](https://docs.controld.com/docs/macos-platform#manual-setup-profile) |
| [**Mullvad**](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls) | DoH<br>DoT | No[5](https://www.privacyguides.org/en/dns/#fn:5) | No | Based on server choice. Filter list being used can be found here. | Yes |

## Cloud-Based DNS Filtering

These DNS filtering solutions offer a web dashboard where you can customize the block lists to your exact needs. These services can be used easily across multiple networks.

### Control D

![Control D logo](https://www.privacyguides.org/en/assets/img/dns/control-d.svg)

**Control D** is a customizable DNS service which lets you block security threats, unwanted content, and advertisements on a DNS level.

In addition to their paid plans, they offer a number of preconfigured DNS resolvers you can use for free.

[Homepage](https://controld.com/) [Privacy Policy](https://controld.com/privacy "Privacy Policy") [Documentation](https://docs.controld.com/docs/getting-started "Documentation") [Source Code](https://github.com/Control-D-Inc/ctrld "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.controld.setuputility)
- [App Store](https://apps.apple.com/app/1518799460)
- [GitHub](https://github.com/Control-D-Inc/ctrld/releases)
- [Windows](https://docs.controld.com/docs/gui-setup-utility)
- [macOS](https://docs.controld.com/docs/gui-setup-utility)
- [Linux](https://docs.controld.com/docs/ctrld)

### NextDNS

![NextDNS logo](https://www.privacyguides.org/en/assets/img/dns/nextdns.svg)

**NextDNS** is a customizable DNS service which lets you block security threats, unwanted content, and advertisements on a DNS level.

They offer a fully functional free plan for limited use.

[Homepage](https://nextdns.io/) [Privacy Policy](https://nextdns.io/privacy "Privacy Policy") [Documentation](https://help.nextdns.io/ "Documentation") [Source Code](https://github.com/nextdns/nextdns "Source Code")

Downloads

- [App Store](https://apps.apple.com/app/nextdns/id1463342498)
- [GitHub](https://github.com/nextdns/nextdns/releases)
- [Windows](https://github.com/nextdns/nextdns/wiki/Windows)
- [macOS](https://apps.apple.com/us/app/nextdns/id1464122853)
- [Linux](https://github.com/nextdns/nextdns/wiki)

When used with an account, NextDNS will enable insights and logging features by default (as some features require it). You can choose retention time and log storage location for any logs you choose to keep, or disable logs altogether.

NextDNS's free plan is fully functional, but should not be relied upon for security or other critical filtering applications, because after 300,000 DNS queries in a month all filtering, logging, and other account-based functionality are disabled. It can still be used as a regular DNS provider after that point, so your devices will continue to function and make secure queries via DNS-over-HTTPS (DoH), just without your filter lists.

NextDNS also offers a public DoH service at `https://dns.nextdns.io` and DNS-over-TLS/QUIC (DoT/DoQ) at `dns.nextdns.io`, which are available by default in Firefox and Chromium, and subject to their default, no-logging [privacy policy](https://nextdns.io/privacy).

## Encrypted DNS Proxies

Encrypted DNS proxy software provides a local proxy for the [unencrypted DNS](https://www.privacyguides.org/en/advanced/dns-overview/#unencrypted-dns) resolver to forward to. Typically, it is used on platforms that don't natively support [encrypted DNS](https://www.privacyguides.org/en/advanced/dns-overview/#what-is-encrypted-dns).

### RethinkDNS

![RethinkDNS logo](https://www.privacyguides.org/en/assets/img/android/rethinkdns.svg#only-light)![RethinkDNS logo](https://www.privacyguides.org/en/assets/img/android/rethinkdns-dark.svg#only-dark)

**RethinkDNS** is an open-source Android client that supports [DoH](https://www.privacyguides.org/en/advanced/dns-overview/#dns-over-https-doh), [DoT](https://www.privacyguides.org/en/advanced/dns-overview/#dns-over-tls-dot), [DNSCrypt](https://www.privacyguides.org/en/advanced/dns-overview/#dnscrypt) and DNS Proxy. It also provides additional functionality such as caching DNS responses, locally logging DNS queries, and using the app as a firewall.

[Homepage](https://rethinkdns.com/) [Privacy Policy](https://rethinkdns.com/privacy "Privacy Policy") [Documentation](https://docs.rethinkdns.com/ "Documentation") [Source Code](https://github.com/celzero/rethink-app "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.celzero.bravedns)
- [GitHub](https://github.com/celzero/rethink-app/releases)

While RethinkDNS takes up the Android VPN slot, you can still use a VPN or Orbot with the app by [adding a WireGuard configuration](https://docs.rethinkdns.com/proxy/wireguard) or [manually configuring Orbot as a Proxy server](https://docs.rethinkdns.com/firewall/orbot), respectively.

### DNSCrypt-Proxy

![DNSCrypt-Proxy logo](https://www.privacyguides.org/en/assets/img/dns/dnscrypt-proxy.svg)

**DNSCrypt-Proxy** is a DNS proxy with support for [DNSCrypt](https://www.privacyguides.org/en/advanced/dns-overview/#dnscrypt), [DoH](https://www.privacyguides.org/en/advanced/dns-overview/#dns-over-https-doh), and [Anonymized DNS](https://github.com/DNSCrypt/dnscrypt-proxy/wiki/Anonymized-DNS).

[Repository](https://github.com/DNSCrypt/dnscrypt-proxy#readme) [Documentation](https://github.com/DNSCrypt/dnscrypt-proxy/wiki "Documentation") [Source Code](https://github.com/DNSCrypt/dnscrypt-proxy "Source Code") [Contribute](https://opencollective.com/dnscrypt/contribute "Contribute")

Downloads

- [Windows](https://github.com/DNSCrypt/dnscrypt-proxy/wiki/Installation-Windows)
- [macOS](https://github.com/DNSCrypt/dnscrypt-proxy/wiki/Installation-macOS)
- [Linux](https://github.com/DNSCrypt/dnscrypt-proxy/wiki/Installation-linux)

Warning

The anonymized DNS feature does [not](https://www.privacyguides.org/en/advanced/dns-overview/#why-shouldnt-i-use-encrypted-dns) anonymize other network traffic.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

All DNS products...

- Must support [DNSSEC](https://www.privacyguides.org/en/advanced/dns-overview/#what-is-dnssec).
- Must support [QNAME Minimization](https://www.privacyguides.org/en/advanced/dns-overview/#what-is-qname-minimization).
- Must anonymize [ECS](https://www.privacyguides.org/en/advanced/dns-overview/#what-is-edns-client-subnet-ecs) or disable it by default.

Additionally, all public providers...

- Must not log any personal data to disk.
  - As noted in the footnotes, some providers collect query information for purposes like security research, but in that case the data must not be associated with any PII such as IP address, etc.
- Should support [anycast](https://en.wikipedia.org/wiki/Anycast) or geo-steering.

* * *

1. AdGuard stores aggregated performance metrics of their DNS servers, namely the number of complete requests to a particular server, the number of blocked requests, and the speed of processing requests. They also keep and store the database of domains requested within the last 24 hours.


> We need this information to identify and block new trackers and threats.
> We also log how many times this or that tracker has been blocked. We need this information to remove outdated rules from our filters.


AdGuard DNS: [_Privacy Policy_](https://adguard-dns.io/en/privacy.html) [↩](https://www.privacyguides.org/en/dns/#fnref:1)

2. Cloudflare collects and stores only the limited DNS query data that is sent to the 1.1.1.1 resolver. The 1.1.1.1 resolver service does not log personal data, and the bulk of the limited non-personally identifiable query data is stored only for 25 hours.

1.1.1.1 Public DNS Resolver: [_Cloudflare’s commitment to privacy_](https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver) [↩](https://www.privacyguides.org/en/dns/#fnref:2)

3. Control D only logs specific account data for Premium resolvers with custom DNS profiles. Free resolvers do not retain any data.

Control D: [_Privacy Policy_](https://controld.com/privacy) [↩](https://www.privacyguides.org/en/dns/#fnref:3)

4. DNS0.eu collects some data for their threat intelligence feeds to monitor for newly registered/observed/active domains and other bulk data. That data is shared with some [partners](https://docs.dns0.eu/data-feeds/introduction) for e.g. security research. They do not collect any personally identifiable information.

DNS0.eu: [_Privacy Policy_](https://dns0.eu/privacy) [↩](https://www.privacyguides.org/en/dns/#fnref:4)

5. Mullvad's DNS service is available to both subscribers and non-subscribers of Mullvad VPN. Their privacy policy explicitly claims they do not log DNS requests in any way.

Mullvad: [_No-logging of user activity policy_](https://mullvad.net/en/help/no-logging-data-policy) [↩](https://www.privacyguides.org/en/dns/#fnref:5)

6. Quad9 collects some data for the purposes of threat monitoring and response. That data may then be remixed and shared for purposes like furthering their security research. Quad9 does not collect or record IP addresses or other data they deem personally identifiable.

Quad9: [_Data and Privacy Policy_](https://quad9.net/privacy/policy) [↩](https://www.privacyguides.org/en/dns/#fnref:6)


Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).