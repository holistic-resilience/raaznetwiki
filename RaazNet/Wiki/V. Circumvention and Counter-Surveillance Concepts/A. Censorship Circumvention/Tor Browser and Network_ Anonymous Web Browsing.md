[Skip to content](https://www.privacyguides.org/en/tor/#tor-browser)

![](https://www.privacyguides.org/en/assets/img/cover/tor.webp)

# Tor Browser

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/tor.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)
- [Mass Surveillance](https://www.privacyguides.org/en/basics/common-threats/#mass-surveillance-programs)
- [Censorship](https://www.privacyguides.org/en/basics/common-threats/#avoiding-censorship)

**Tor** is a group of volunteer-operated servers that allows you to connect for free and improve your privacy and security on the Internet. Individuals and organizations can also share information over the Tor network with ".onion hidden services" without compromising their privacy. Because Tor traffic is difficult to block and trace, Tor is an effective censorship circumvention tool.

[Detailed Tor Overview](https://www.privacyguides.org/en/advanced/tor-overview/) [Video: Why You Need Tor](https://www.privacyguides.org/videos/2025/03/02/why-you-need-tor)

Tip

Before connecting to Tor, please ensure you've read our [overview](https://www.privacyguides.org/en/advanced/tor-overview/) on what Tor is and how to connect to it safely. We often recommend connecting to Tor through a trusted [VPN provider](https://www.privacyguides.org/en/vpn/), but you have to do so **properly** to avoid decreasing your anonymity.

There are a variety of ways to connect to the Tor network from your device, the most commonly used being the **Tor Browser**, a fork of Firefox designed for [anonymous](https://www.privacyguides.org/en/basics/common-threats/#anonymity-vs-privacy) browsing for desktop computers and Android.

Some of these apps are better than others; making a determination comes down to your threat model. If you are a casual Tor user who is not worried about your ISP collecting evidence against you, using mobile browser apps like [Onion Browser](https://www.privacyguides.org/en/tor/#onion-browser-ios) to access the Tor network is probably fine. Increasing the number of people who use Tor on an everyday basis helps reduce the bad stigma of Tor, and lowers the quality of "lists of Tor users" that ISPs and governments may compile.

If more complete anonymity is paramount to your situation, you should **only** be using the desktop Tor Browser client, ideally in a [Whonix](https://www.privacyguides.org/en/desktop/#whonix) \+ [Qubes](https://www.privacyguides.org/en/desktop/#qubes-os) configuration. Mobile browsers are less common on Tor (and more fingerprintable as a result), and other configurations are not as rigorously tested against deanonymization.

## Tor Browser

![Tor Browser logo](https://www.privacyguides.org/en/assets/img/browsers/tor.svg)

**Tor Browser** is the top choice if you need anonymity, as it provides you with access to the Tor network and bridges, and it includes default settings and extensions that are automatically configured by the default security levels: _Standard_, _Safer_ and _Safest_.

[Homepage](https://torproject.org/) [Onion Service](http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/ "Onion Service") [Documentation](https://tb-manual.torproject.org/ "Documentation") [Source Code](https://gitlab.torproject.org/tpo/applications/tor-browser "Source Code") [Contribute](https://donate.torproject.org/ "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=org.torproject.torbrowser)
- [Android](https://torproject.org/download/#android)
- [Windows](https://torproject.org/download)
- [macOS](https://torproject.org/download)
- [Linux](https://torproject.org/download)

Danger

You should **never** install any additional extensions on Tor Browser or edit `about:config` settings, including the ones we suggest for Firefox. Browser extensions and non-standard settings make you stand out from others on the Tor network, thus making your browser easier to [fingerprint](https://support.torproject.org/glossary/browser-fingerprinting).

The Tor Browser is designed to prevent fingerprinting, or identifying you based on your browser configuration. Therefore, it is imperative that you do **not** modify the browser beyond the default [security levels](https://tb-manual.torproject.org/security-settings). When modifying the security level setting, you **must** always restart the browser before continuing to use it. Otherwise, [the security settings may not be fully applied](https://www.privacyguides.org/articles/2025/05/02/tor-security-slider-flaw), putting you at a higher risk of fingerprinting and exploits than you may expect based on the setting chosen.

In addition to installing Tor Browser on your computer directly, there are also operating systems designed specifically to connect to the Tor network such as [Whonix](https://www.privacyguides.org/en/desktop/#whonix) on [Qubes OS](https://www.privacyguides.org/en/desktop/#qubes-os), which provide even greater security and protections than the standard Tor Browser alone.

## Onion Browser (iOS)

![Onion Browser logo](https://www.privacyguides.org/en/assets/img/self-contained-networks/onion_browser.svg)

**Onion Browser** is an open-source browser that lets you browse the web anonymously over the Tor network on iOS devices and is endorsed by the [Tor Project](https://support.torproject.org/glossary/onion-browser).

[Read our latest Onion Browser review.](https://www.privacyguides.org/articles/2024/09/18/onion-browser-review)

[Homepage](https://onionbrowser.com/) [Privacy Policy](https://onionbrowser.com/privacy-policy "Privacy Policy") [Documentation](https://onionbrowser.com/faqs "Documentation") [Source Code](https://github.com/OnionBrowser/OnionBrowser "Source Code") [Contribute](https://onionbrowser.com/donate "Contribute")

Downloads

- [App Store](https://apps.apple.com/app/id519296448)

Onion Browser does not provide the same levels of privacy protections as Tor Browser does on desktop platforms. For casual use it is a perfectly fine way to access hidden services, but if you're concerned about being traced or monitored by advanced adversaries you should not rely on this as an anonymity tool.

[Notably](https://github.com/privacyguides/privacyguides.org/issues/2929), Onion Browser does not _guarantee_ all requests go through Tor. When using the built-in version of Tor, [your real IP **will** be leaked via WebRTC and audio/video streams](https://onionbrowser.com/faqs) due to limitations of WebKit. It is _safer_ to use Onion Browser alongside [Orbot](https://www.privacyguides.org/en/alternative-networks/#orbot), but this still comes with some limitations on iOS.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).