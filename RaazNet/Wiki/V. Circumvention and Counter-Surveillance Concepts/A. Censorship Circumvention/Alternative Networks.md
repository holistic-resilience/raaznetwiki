[Skip to content](https://www.privacyguides.org/en/alternative-networks/#anonymizing-networks)

![](https://www.privacyguides.org/en/assets/img/cover/alternative-networks.webp)

# Alternative Networks

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/alternative-networks.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)
- [Mass Surveillance](https://www.privacyguides.org/en/basics/common-threats/#mass-surveillance-programs)
- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

## Anonymizing Networks

When it comes to anonymizing networks, we want to specially note that [Tor](https://www.privacyguides.org/en/advanced/tor-overview/) is our top choice. It is by far the most utilized, robustly studied, and actively developed anonymous network. Using other networks could be more likely to endanger your [Anonymity](https://www.privacyguides.org/en/basics/common-threats/#anonymity-vs-privacy), unless you know what you're doing.

### Tor

![Tor logo](https://www.privacyguides.org/en/assets/img/self-contained-networks/tor.svg)

The **Tor** network is a group of volunteer-operated servers that allows you to connect for free and improve your privacy and security on the Internet. Individuals and organizations can also share information over the Tor network with ".onion hidden services" without compromising their privacy. Because Tor traffic is difficult to block and trace, Tor is an effective [Censorship](https://www.privacyguides.org/en/basics/common-threats/#avoiding-censorship) circumvention tool.

[Homepage](https://torproject.org/ "Homepage")[Onion Service](http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/ "Onion Service")[Documentation](https://tb-manual.torproject.org/ "Documentation")[Source Code](https://gitlab.torproject.org/tpo/core/tor "Source Code")[Contribute](https://donate.torproject.org/ "Contribute")

The recommended way to access the Tor network is via the official Tor Browser, which we have covered in more detail on a dedicated page:

[Tor Browser Info](https://www.privacyguides.org/en/tor/) [Detailed Tor Overview](https://www.privacyguides.org/en/advanced/tor-overview/)

You can access the Tor network using other tools; making this determination comes down to your threat model. If you are a casual Tor user who is not worried about your ISP collecting evidence against you, using apps like [Orbot](https://www.privacyguides.org/en/alternative-networks/#orbot) or mobile browser apps to access the Tor network is probably fine. Increasing the number of people who use Tor on an everyday basis helps reduce the bad stigma of Tor, and lowers the quality of "lists of Tor users" that ISPs and governments may compile.

Try it out!

You can try connecting to _Privacy Guides_ via Tor at [xoe4vn5uwdztif6goazfbmogh6wh5jc4up35bqdflu6bkdc5cas5vjqd.onion](http://www.xoe4vn5uwdztif6goazfbmogh6wh5jc4up35bqdflu6bkdc5cas5vjqd.onion/).

#### Orbot

![Orbot logo](https://www.privacyguides.org/en/assets/img/self-contained-networks/orbot.svg)

**Orbot** is a mobile application which routes traffic from any app on your device through the Tor network.

[Homepage](https://orbot.app/) [Privacy Policy](https://orbot.app/privacy-policy "Privacy Policy") [Documentation](https://orbot.app/faqs "Documentation") [Source Code](https://orbot.app/code "Source Code") [Contribute](https://orbot.app/donate "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android)
- [App Store](https://apps.apple.com/app/id1609461599)
- [GitHub](https://github.com/guardianproject/orbot/releases)
- [F-Droid](https://guardianproject.info/fdroid)

We previously recommended enabling the _Isolate Destination Address_ preference in Orbot settings. While this setting can theoretically improve privacy by enforcing the use of a different circuit for each IP address you connect to, it doesn't provide a practical advantage for most applications (especially web browsing), can come with a significant performance penalty, and increases the load on the Tor network. We no longer recommend adjusting this setting from its default value unless you know you need to.[1](https://www.privacyguides.org/en/alternative-networks/#fn:1)

[Android](https://www.privacyguides.org/en/alternative-networks/#__tabbed_1_1)[iOS](https://www.privacyguides.org/en/alternative-networks/#__tabbed_1_2)

Orbot can proxy individual apps if they support SOCKS or HTTP proxying. It can also proxy all your network connections using [VpnService](https://developer.android.com/reference/android/net/VpnService) and can be used with the VPN kill switch in ![⚙](https://www.privacyguides.org/en/assets/external/cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2699.svg)**Settings** → **Network & internet** → **VPN** → ![⚙](https://www.privacyguides.org/en/assets/external/cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2699.svg) → **Block connections without VPN**.

Orbot is often outdated on Google Play and the Guardian Project's F-Droid repository, so consider downloading directly from the GitHub repository instead. All versions are signed using the same signature, so they should be compatible with each other.

On iOS, Orbot has some limitations that could potentially cause crashes or leaks: iOS does not have an effective OS-level feature to block connections without a VPN like Android does, and iOS has an artificial memory limit for network extensions that makes it challenging to run Tor in Orbot without crashes. Currently, it is always safer to use Tor on a desktop computer compared to a mobile device.

#### Snowflake

![Snowflake logo](https://www.privacyguides.org/en/assets/img/self-contained-networks/snowflake.svg#only-light)![Snowflake logo](https://www.privacyguides.org/en/assets/img/self-contained-networks/snowflake-dark.svg#only-dark)

**Snowflake** allows you to donate bandwidth to the Tor Project by operating a "Snowflake proxy" within your browser.

People who are censored can use Snowflake proxies to connect to the Tor network. Snowflake is a great way to contribute to the network even if you don't have the technical know-how to run a Tor relay or bridge.

[Homepage](https://snowflake.torproject.org/) [Documentation](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake/-/wikis/Technical%20Overview "Documentation") [Source Code](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake "Source Code") [Contribute](https://donate.torproject.org/ "Contribute")

You can enable Snowflake in your browser by opening it in another tab and turning the switch on. You can leave it running in the background while you browse to contribute your connection. We don't recommend installing Snowflake as a browser extension, because adding third-party extensions can increase your attack surface.

[Run Snowflake in your Browser](https://snowflake.torproject.org/embed.html)

Snowflake does not increase your privacy in any way, nor is it used to connect to the Tor network within your personal browser. However, if your internet connection is uncensored, you should consider running it to help people in censored networks achieve better privacy themselves. There is no need to worry about which websites people are accessing through your proxy—their visible browsing IP address will match their Tor exit node, not yours.

Running a Snowflake proxy is low-risk, even more so than running a Tor relay or bridge which are already not particularly risky endeavors. However, it does still proxy traffic through your network which can be impactful in some ways, especially if your network is bandwidth-limited. Make sure you understand [how Snowflake works](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake/-/wikis/home) before deciding whether to run a proxy.

### I2P (The Invisible Internet Project)

![I2P logo](https://www.privacyguides.org/en/assets/img/self-contained-networks/i2p.svg#only-light)![I2P logo](https://www.privacyguides.org/en/assets/img/self-contained-networks/i2p-dark.svg#only-dark)

**I2P** is a network layer which encrypts your connections and routes them via a network of computers distributed around the world. It is mainly focused on creating an alternative, privacy-protecting network rather than making regular internet connections anonymous.

[Homepage](https://geti2p.net/en) [Documentation](https://geti2p.net/en/about/software "Documentation") [Source Code](https://github.com/i2p/i2p.i2p "Source Code") [Contribute](https://geti2p.net/en/get-involved "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=net.i2p.android)
- [Android](https://geti2p.net/en/download#android)
- [Windows](https://geti2p.net/en/download#windows)
- [macOS](https://geti2p.net/en/download#mac)
- [Linux](https://geti2p.net/en/download#unix)

Unlike Tor, all I2P traffic is internal to the I2P network, which means regular internet websites are **not** directly accessible from I2P. Instead, you can connect to websites which are hosted anonymously and directly on the I2P network, which are called "eepsites" and have domains which end in `.i2p`.

Try it out!

You can try connecting to _Privacy Guides_ via I2P at [privacyguides.i2p](http://privacyguides.i2p/?i2paddresshelper=fvbkmooriuqgssrjvbxu7nrwms5zyhf34r3uuppoakwwsm7ysv6q.b32.i2p).

Also, unlike Tor, every I2P node will relay traffic for other users by default, instead of relying on dedicated relay volunteers to run nodes. There are approximately [10,000](https://metrics.torproject.org/networksize.html) relays and bridges on the Tor network compared to ~50,000 on I2P, meaning there is potentially more ways for your traffic to be routed to maximize anonymity. I2P also tends to be more performant than Tor, although this is likely a side effect of Tor being more focused on regular "clearnet" internet traffic and thus using more bottle necked exit nodes. Hidden service performance is generally considered to be much better on I2P compared to Tor. While running P2P applications like BitTorrent is challenging on Tor (and can massively impact Tor network performance), it is very easy and performant on I2P.

There are downsides to I2P's approach, however. Tor relying on dedicated exit nodes means more people in less safe environments can use it, and the relays that do exist on Tor are likely to be more performant and stable, as they generally aren't run on residential connections. Tor is also far more focused on **browser privacy** (i.e. anti-fingerprinting), with a dedicated [Tor Browser](https://www.privacyguides.org/en/tor/) to make browsing activity as anonymous as possible. I2P is used via your [regular web browser](https://www.privacyguides.org/en/desktop-browsers/), and while you can configure your browser to be more privacy-protecting, you probably still won't have the same browser fingerprint as other I2P users (there's no "crowd" to blend in with in that regard).

Tor is likely to be more resistant to censorship, due to their robust network of bridges and varying [pluggable transports](https://tb-manual.torproject.org/circumvention). On the other hand, I2P uses directory servers for the initial connection which are varying/untrusted and run by volunteers, compared to the hard-coded/trusted ones Tor uses which are likely easier to block.

* * *

1. The `IsolateDestAddr` setting is discussed on the [Tor mailing list](https://lists.torproject.org/pipermail/tor-talk/2012-May/024403) and [Whonix's Stream Isolation documentation](https://whonix.org/wiki/Stream_Isolation), where both projects suggest that it is usually not a good approach for most people. [↩](https://www.privacyguides.org/en/alternative-networks/#fnref:1)


Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).