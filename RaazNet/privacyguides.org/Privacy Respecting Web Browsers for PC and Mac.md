---
title: "Desktop Browsers"
tags: [browsers, desktop, firefox, brave, mullvad-browser, privacy]
category: "Tool Recommendations"
difficulty: "Beginner"
audience: "General Users"
topics:
  [
    browser-hardening,
    tracking-protection,
    fingerprinting,
    https,
    dns-over-https,
  ]
summary: "Recommended privacy-respecting web browsers and configurations for desktop operating systems."
source: "https://www.privacyguides.org/en/desktop-browsers/"
content_type: "guide"
security_level: "Standard"
language: "en"
prerequisites: []
estimated_read_time: 15
---

[Skip to content](https://www.privacyguides.org/en/desktop-browsers/#mullvad-browser)

![](https://www.privacyguides.org/en/assets/img/cover/desktop-browsers.webp)

# Desktop Browsers

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/desktop-browsers.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

These are our currently recommended **desktop web browsers** and configurations for standard/non-anonymous browsing. We recommend [Mullvad Browser](https://www.privacyguides.org/en/desktop-browsers/#mullvad-browser) if you are focused on strong privacy protections and anti-fingerprinting out of the box, [Firefox](https://www.privacyguides.org/en/desktop-browsers/#firefox) for casual internet browsers looking for a good alternative to Google Chrome, and [Brave](https://www.privacyguides.org/en/desktop-browsers/#brave) if you need Chromium browser compatibility.

If you need to browse the internet anonymously, you should use [Tor](https://www.privacyguides.org/en/tor/) instead. We make some configuration recommendations on this page, but all browsers other than Tor Browser will be traceable by _somebody_ in some manner or another.

## Mullvad Browser

![Mullvad Browser logo](https://www.privacyguides.org/en/assets/img/browsers/mullvad_browser.svg)

**Mullvad Browser** is a version of [Tor Browser](https://www.privacyguides.org/en/tor/#tor-browser) with Tor network integrations removed. It aims to provide to VPN users Tor Browser's anti-fingerprinting browser technologies, which are key protections against [Mass Surveillance](https://www.privacyguides.org/en/basics/common-threats/#mass-surveillance-programs). It is developed by the Tor Project and distributed by [Mullvad](https://www.privacyguides.org/en/vpn/#mullvad), and does **not** require the use of Mullvad's VPN.

[Homepage](https://mullvad.net/en/browser) [Privacy Policy](https://mullvad.net/en/help/privacy-policy "Privacy Policy") [Documentation](https://mullvad.net/en/help/tag/mullvad-browser "Documentation") [Source Code](https://gitlab.torproject.org/tpo/applications/mullvad-browser "Source Code")

Downloads

- [Windows](https://mullvad.net/en/download/browser/windows)
- [macOS](https://mullvad.net/en/download/browser/macos)
- [Linux](https://mullvad.net/en/download/browser/linux)

Like [Tor Browser](https://www.privacyguides.org/en/tor/), Mullvad Browser is designed to prevent fingerprinting by making your browser fingerprint identical to all other Mullvad Browser users, and it includes default settings and extensions that are automatically configured by the default security levels: _Standard_, _Safer_ and _Safest_.

Therefore, it is imperative that you do not modify the browser at all outside adjusting the default [security levels](https://tb-manual.torproject.org/security-settings). When adjusting the security level, you **must** always restart the browser before continuing to use it. Otherwise, [the security settings may not be fully applied](https://www.privacyguides.org/articles/2025/05/02/tor-security-slider-flaw), putting you at a higher risk of fingerprinting and exploits than you may expect based on the setting chosen.

Modifications other than adjusting this setting would make your fingerprint unique, defeating the purpose of using this browser. If you want to configure your browser more heavily and fingerprinting is not a concern for you, we recommend [Firefox](https://www.privacyguides.org/en/desktop-browsers/#firefox) instead.

### Anti-Fingerprinting

**Without** using a [VPN](https://www.privacyguides.org/en/vpn/), Mullvad Browser provides the same protections against [naive fingerprinting scripts](https://github.com/arkenfox/user.js/wiki/3.3-Overrides-%5BTo-RFP-or-Not%5D#-fingerprinting) as other private browsers like Firefox+ [Arkenfox](https://www.privacyguides.org/en/desktop-browsers/#arkenfox-advanced) or [Brave](https://www.privacyguides.org/en/desktop-browsers/#brave). Mullvad Browser provides these protections out of the box, at the expense of some flexibility and convenience that other private browsers can provide.

For the strongest anti-fingerprinting protection, we recommend using Mullvad Browser in conjunction **with** a VPN, whether that is Mullvad or another recommended VPN provider. When using a VPN with Mullvad Browser, you will share a fingerprint and a pool of IP addresses with many other users, giving you a "crowd" to blend in with. This strategy is the only way to thwart advanced tracking scripts, and is the same anti-fingerprinting technique used by Tor Browser.

Note that while you can use Mullvad Browser with any VPN provider, other people on that VPN must also be using Mullvad Browser for this "crowd" to exist, something which is more likely on Mullvad VPN compared to other providers, particularly this close to the launch of Mullvad Browser. Mullvad Browser does not have built-in VPN connectivity, nor does it check whether you are using a VPN before browsing; your VPN connection has to be configured and managed separately.

Mullvad Browser comes with the _uBlock Origin_ and _NoScript_ browser extensions pre-installed. While we typically discourage adding _additional_ [browser extensions](https://www.privacyguides.org/en/browser-extensions/), these extensions that come pre-installed with the browser should **not** be removed or configured outside their default values, because doing so would noticeably make your browser fingerprint distinct from other Mullvad Browser users. It also comes pre-installed with the Mullvad Browser Extension, which _can_ be safely removed without impacting your browser fingerprint if you would like, but is also safe to keep even if you don't use Mullvad VPN.

### Private Browsing Mode

Mullvad Browser operates in permanent private browsing mode, meaning your history, cookies, and other site data will always be cleared every time the browser is closed. Your bookmarks, browser settings, and extension settings will still be preserved.

This is required to prevent advanced forms of tracking, but does come at the cost of convenience and some Firefox features, such as Multi-Account Containers. Remember you can always use multiple browsers, for example, you could consider using Firefox+Arkenfox for a few sites that you want to stay logged in on or otherwise don't work properly in Mullvad Browser, and Mullvad Browser for general browsing.

### Mullvad Leta

Mullvad Browser comes with [**Mullvad Leta**](https://www.privacyguides.org/en/search-engines/#mullvad-leta) as the default search engine, which functions as a proxy to either Google or Brave search results (configurable on the Mullvad Leta homepage).

If you are a Mullvad VPN user, there is some risk in using services like Mullvad Leta which are offered by your VPN provider themselves. This is because Mullvad theoretically has access to your true IP address (via their VPN) and your search activity (via Leta); the latter is information a VPN is typically intended to separate. Even though Mullvad collects very little information about their VPN subscribers or Leta users, you should consider a different [search engine](https://www.privacyguides.org/en/search-engines/) if this risk concerns you.

## Firefox

![Firefox logo](https://www.privacyguides.org/en/assets/img/browsers/firefox.svg)

**Firefox** provides strong privacy settings such as [Enhanced Tracking Protection](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop), which can help block various [types of tracking](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop#w_what-enhanced-tracking-protection-blocks).

[Homepage](https://firefox.com/) [Privacy Policy](https://mozilla.org/privacy/firefox "Privacy Policy") [Documentation](https://support.mozilla.org/products/firefox "Documentation") [Source Code](https://hg.mozilla.org/mozilla-central "Source Code") [Contribute](https://donate.mozilla.org/ "Contribute")

Downloads

- [Windows](https://mozilla.org/firefox/windows)
- [macOS](https://mozilla.org/firefox/mac)
- [Linux](https://mozilla.org/firefox/linux)
- [Flathub](https://flathub.org/apps/details/org.mozilla.firefox)

Warning

Firefox includes a unique [download token](https://bugzilla.mozilla.org/show_bug.cgi?id=1677497#c0) in downloads from Mozilla's website and uses telemetry in Firefox to send the token. The token is **not** included in releases from the [Mozilla FTP](https://ftp.mozilla.org/pub/firefox/releases/).

### Recommended Firefox Configuration

These options can be found in → **Settings**.

#### Search

- Uncheck **Show search suggestions**

Search suggestion features may not be available in your region.

Search suggestions send everything you type in the address bar to the default search engine, regardless of whether you submit an actual search. Disabling search suggestions allows you to more precisely control what data you send to your search engine provider.

##### Firefox Suggest (US only)

[Firefox Suggest](https://support.mozilla.org/kb/firefox-suggest) is a feature similar to search suggestions which is only available in the US. We recommend disabling it for the same reason we recommend disabling search suggestions. If you don't see these options under the **Address Bar** header, you do not have the new experience and can ignore these changes.

- Uncheck **Suggestions from Firefox**
- Uncheck **Suggestions from sponsors**

#### Privacy & Security

##### Enhanced Tracking Protection

- Select **Strict** Enhanced Tracking Protection

This protects you by blocking social media trackers, fingerprinting scripts (note that this does not protect you from _all_ fingerprinting), cryptominers, cross-site tracking cookies, and some other tracking content. ETP protects against many common threats, but it does not block all tracking avenues because it is designed to have minimal to no impact on site usability.

##### Sanitize on Close

If you want to stay logged in to particular sites, you can allow exceptions in **Cookies and Site Data** → **Manage Exceptions...**

- Check **Delete cookies and site data when Firefox is closed**

This protects you from persistent cookies, but does not protect you against cookies acquired during any one browsing session. When this is enabled, it becomes possible to easily cleanse your browser cookies by simply restarting Firefox. You can set exceptions on a per-site basis, if you wish to stay logged in to a particular site you visit often.

##### Telemetry

- Uncheck **Allow Firefox to send technical and interaction data to Mozilla**
- Uncheck **Allow Firefox to install and run studies**
- Uncheck **Allow Firefox to send backlogged crash reports on your behalf**

According to Mozilla's privacy policy for Firefox,

> Firefox sends data about your Firefox version and language; device operating system and hardware configuration; memory, basic information about crashes and errors; outcome of automated processes like updates, safebrowsing, and activation to us. When Firefox sends data to us, your IP address is temporarily collected as part of our server logs.

Additionally, the Mozilla Accounts service collects [some technical data](https://mozilla.org/privacy/mozilla-accounts). If you use a Mozilla Account you can opt out:

1. Open your [profile settings on accounts.firefox.com](https://accounts.firefox.com/settings#data-collection)
2. Uncheck **Data Collection and Use** > **Help improve Firefox Accounts**

##### Website Advertising Preferences

- Uncheck **Allow websites to perform privacy-preserving ad measurement**

With the release of Firefox 128, a new setting for [privacy-preserving attribution](https://support.mozilla.org/kb/privacy-preserving-attribution) (PPA) has been added and [enabled by default](https://blog.privacyguides.org/2024/07/14/mozilla-disappoints-us-yet-again-2). PPA allows advertisers to use your web browser to measure the effectiveness of web campaigns, instead of using traditional JavaScript-based tracking. We consider this behavior to be outside the scope of a user agent's responsibilities, and the fact that it is disabled by default in Arkenfox is an additional indicator for disabling this feature.

##### HTTPS-Only Mode

- Select **Enable HTTPS-Only Mode in all windows**

This prevents you from unintentionally connecting to a website in plain-text HTTP. Sites without HTTPS are uncommon nowadays, so this should have little to no impact on your day-to-day browsing.

##### DNS over HTTPS

If you use a [DNS over HTTPS provider](https://www.privacyguides.org/en/dns/):

- Select **Max Protection** and choose a suitable provider

Max Protection enforces the use of DNS over HTTPS, and a security warning will show if Firefox can’t connect to your secure DNS resolver, or if your secure DNS resolver says that records for the domain you are trying to access do not exist. This stops the network you're connected to from secretly downgrading your DNS security.

#### Sync

[Firefox Sync](https://hacks.mozilla.org/2018/11/firefox-sync-privacy) allows your browsing data (history, bookmarks, etc.) to be accessible on all your devices and protects it with E2EE.

### Arkenfox (advanced)

Use Mullvad Browser for advanced anti-fingerprinting

[Mullvad Browser](https://www.privacyguides.org/en/desktop-browsers/#mullvad-browser) provides the same anti-fingerprinting protections as Arkenfox out of the box, and does not require the use of Mullvad's VPN to benefit from these protections. Coupled with a VPN, Mullvad Browser can thwart more advanced tracking scripts which Arkenfox cannot. Arkenfox still has the advantage of being much more flexible, and allowing per-site exceptions for websites which you need to stay logged in to.

The [Arkenfox project](https://github.com/arkenfox/user.js) provides a set of carefully considered options for Firefox. If you [decide](https://github.com/arkenfox/user.js/wiki/1.1-To-Arkenfox-or-Not) to use Arkenfox, a [few options](https://github.com/arkenfox/user.js/wiki/3.2-Overrides-[Common]) are subjectively strict and/or may cause some websites to not work properly—which you can [easily change](https://github.com/arkenfox/user.js/wiki/3.1-Overrides) to suit your needs. We **strongly recommend** reading through their full [wiki](https://github.com/arkenfox/user.js/wiki). Arkenfox also enables [container](https://support.mozilla.org/kb/containers#w_for-advanced-users) support.

Arkenfox only aims to thwart basic or naive tracking scripts through canvas randomization and Firefox's built-in fingerprint resistance configuration settings. It does not aim to make your browser blend in with a large crowd of other Arkenfox users in the same way Mullvad Browser or Tor Browser do, which is the only way to thwart advanced fingerprint tracking scripts. Remember that you can always use multiple browsers, for example, you could consider using Firefox+Arkenfox for a few sites that you want to stay logged in to or otherwise trust, and Mullvad Browser for general browsing.

## Brave

![Brave logo](https://www.privacyguides.org/en/assets/img/browsers/brave.svg)

**Brave Browser** includes a built-in content blocker and [privacy features](https://brave.com/privacy-features), many of which are enabled by default.

Brave is built upon the Chromium web browser project, so it should feel familiar and have minimal website compatibility issues.

[Homepage](https://brave.com/) [Onion Service](https://brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/ "Onion Service") [Privacy Policy](https://brave.com/privacy/browser "Privacy Policy") [Documentation](https://support.brave.com/ "Documentation") [Source Code](https://github.com/brave/brave-browser "Source Code")

Downloads

- [GitHub](https://github.com/brave/brave-browser/releases)
- [Windows](https://brave.com/download)
- [macOS](https://brave.com/download)
- [Linux](https://brave.com/linux)
- [Flathub](https://flathub.org/apps/com.brave.Browser)

Warning

Brave adds a " [referral code](https://github.com/brave/brave-browser/wiki/Brave%E2%80%99s-Use-of-Referral-Codes)" to the file name in downloads from the Brave website, which is used to track which source the browser was downloaded from, for example `BRV002` in a download named `Brave-Browser-BRV002.pkg`. The installer will then ping Brave's server with the referral code at the end of the installation process. If you're concerned about this, you can rename the installer file before opening it.

### Recommended Brave Configuration

These options can be found in → **Settings**.

#### Shields

Brave includes some anti-fingerprinting measures in its [Shields](https://support.brave.com/hc/articles/360022973471-What-is-Shields) feature. We suggest configuring these options [globally](https://support.brave.com/hc/articles/360023646212-How-do-I-configure-global-and-site-specific-Shields-settings) across all pages that you visit.

Shields' options can be downgraded on a per-site basis as needed, but by default we recommend setting the following:

- Select **Aggressive** under _Trackers & ads blocking_

Use default filter lists

Brave allows you to select additional content filters within the internal `brave://adblock` page. We advise against using this feature; instead, keep the default filter lists. Using extra lists will make you stand out from other Brave users and may also increase attack surface if there is an exploit in Brave and a malicious rule is added to one of the lists you use.

- Select **Strict** under _Upgrade connections to HTTPS_
- (Optional) Select **Block Scripts**
- Check **Block fingerprinting**
- Select **Block third-party cookies**
- Check **Forget me when I close this site**
- Uncheck all social media components

#### Privacy and security

- Select **Don’t allow sites to use JavaScript optimization** under _Security_ → _Manage JavaScript optimization & security_
- Select **Automatically remove permissions from unused sites** under _Sites and Shields Settings_
- Select **Disable non-proxied UDP** under [_WebRTC IP Handling Policy_](https://support.brave.com/hc/articles/360017989132-How-do-I-change-my-Privacy-Settings#webrtc)
- Uncheck **Use Google services for push messaging**
- Select **Auto-redirect AMP pages**
- Select **Auto-redirect tracking URLs**
- Select **Prevent sites from fingerprinting me based on my language preferences**

##### Tor windows

[**Private Window with Tor**](https://support.brave.com/hc/articles/360018121491-What-is-a-Private-Window-with-Tor-Connectivity) allows you to route your traffic through the Tor network in Private Windows and access .onion services, which may be useful in some cases. However, Brave is **not** as resistant to fingerprinting as the Tor Browser is, and far fewer people use Brave with Tor, so you will stand out. If your threat model requires strong anonymity, use the [Tor Browser](https://www.privacyguides.org/en/tor/#tor-browser).

##### Data Collection

- Uncheck **Allow privacy-preserving product analytics (P3A)**
- Uncheck **Automatically send daily usage ping to Brave**
- Uncheck **Automatically send diagnostic reports**

#### Web3

Brave's Web3 features can potentially add to your browser fingerprint and attack surface. Unless you use any of these features, they should be disabled.

- Select **Extensions (no fallback)** under _Default Ethereum wallet_
- Select **Extensions (no fallback)** under _Default Solana wallet_

#### Extensions

- Uncheck all built-in extensions you don't use

#### Search engine

We recommend disabling search suggestions in Brave for the same reason we recommend disabling this feature in [Firefox](https://www.privacyguides.org/en/desktop-browsers/#search).

- Uncheck **Show search suggestions**

#### System

- Uncheck **Continue running background apps when Brave is closed** to disable background apps

#### Brave Sync

[Brave Sync](https://support.brave.com/hc/articles/360059793111-Understanding-Brave-Sync) allows your browsing data (history, bookmarks, etc.) to be accessible on all your devices without requiring an account and protects it with E2EE.

#### Brave Rewards and Wallet

**Brave Rewards** lets you receive Basic Attention Token (BAT) cryptocurrency for performing certain actions within Brave. It relies on a custodial account and KYC from a select number of providers. We do not recommend BAT as a [private cryptocurrency](https://www.privacyguides.org/en/cryptocurrency/), nor do we recommend using a [custodial wallet](https://www.privacyguides.org/en/advanced/payments/#wallet-custody), so we would discourage using this feature.

**Brave Wallet** operates locally on your computer, but does not support any private cryptocurrencies, so we would discourage using this feature as well.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

### Minimum Requirements

- Must be open-source software.
- Must support automatic updates.
- Must receive engine updates in 0-1 days from upstream release.
- Must be available on Linux, macOS, and Windows.
- Any changes required to make the browser more privacy-respecting must not negatively impact user experience.
- Must block third-party cookies by default.
- Must support [state partitioning](https://developer.mozilla.org/docs/Web/Privacy/State_Partitioning) to mitigate cross-site tracking.[1](https://www.privacyguides.org/en/desktop-browsers/#fn:1)

### Best-Case

Our best-case criteria represents what we would like to see from the perfect project in this category. Our recommendations may not include any or all of this functionality, but those which do may rank higher than others on this page.

- Should include built-in content blocking functionality.
- Should support cookie compartmentalization (à la [Multi-Account Containers](https://support.mozilla.org/kb/containers)).
- Should support Progressive Web Apps (PWAs).
- Should not include add-on functionality (bloatware) that does not impact user privacy.
- Should not collect telemetry by default.
- Should provide an open-source sync server implementation.
- Should default to a [private search engine](https://www.privacyguides.org/en/search-engines/).

---

1. Brave's implementation is detailed at [Brave Privacy Updates: Partitioning network-state for privacy](https://brave.com/privacy-updates/14-partitioning-network-state). [↩](https://www.privacyguides.org/en/desktop-browsers/#fnref:1)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
