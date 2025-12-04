[Skip to content](https://www.privacyguides.org/en/frontends/#reddit)

![](https://www.privacyguides.org/en/assets/img/cover/frontends.webp)

# Frontends

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/frontends.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

Sometimes services will try to force you to sign up for an account by blocking access to content with annoying popups. They might also break without JavaScript enabled. These frontends can allow you to circumvent these restrictions.

If you choose to self-host these frontends, it is important that you have other people using your instance as well in order for you to blend in. You should be careful with where and how you are hosting, as other peoples' usage will be linked to your hosting.

When you are using an instance run by someone else, make sure to read the privacy policy of that specific instance (if available). They can be modified by their owners and therefore may not reflect the default policy. Some instances have [Tor](https://www.privacyguides.org/en/tor/) .onion addresses, which may grant some privacy as long as your search queries don't contain personally identifiable information.

## Reddit

### Redlib

![Redlib logo](https://www.privacyguides.org/en/assets/img/frontends/redlib.svg)

**Redlib** is an open-source frontend to the [Reddit](https://reddit.com/) website that is also self-hostable. You can access Redlib through a number of public instances.

[Repository](https://github.com/redlib-org/redlib) [Public Instances](https://github.com/redlib-org/redlib-instances/blob/main/instances.md "Public Instances") [Documentation](https://github.com/redlib-org/redlib?tab=readme-ov-file#table-of-contents "Documentation") [Source Code](https://github.com/redlib-org/redlib "Source Code")

Note

The [Old Reddit](https://old.reddit.com/) website doesn't require as much JavaScript as the new Reddit website does, but it has recently blocked access to IP addresses reserved for public VPNs. You can use Old Reddit in conjunction with the [Tor](https://www.privacyguides.org/en/tor/) Onion that was [launched in October 2022](https://forum.torproject.org/t/reddit-onion-service-launch/5305) at [https://old.reddittorjg6rue252oqsxryoxengawnmo46qy4kyii5wtqnwfj4ooad.onion](https://old.reddittorjg6rue252oqsxryoxengawnmo46qy4kyii5wtqnwfj4ooad.onion/).

Tip

Redlib is useful if you want to disable JavaScript in your browser, such as [Tor Browser](https://www.privacyguides.org/en/tor/#tor-browser) on the Safest security level.

## TikTok

### ProxiTok

![ProxiTok logo](https://www.privacyguides.org/en/assets/img/frontends/proxitok.svg)

**ProxiTok** is an open-source frontend to the [TikTok](https://tiktok.com/) website that is also self-hostable.

There are a number of public instances, with some that offer a [Tor](https://www.privacyguides.org/en/tor/) onion service or an [I2P](https://www.privacyguides.org/en/alternative-networks/#i2p-the-invisible-internet-project) eepsite.

[Repository](https://github.com/pablouser1/ProxiTok) [Public Instances](https://github.com/pablouser1/ProxiTok/wiki/Public-instances "Public Instances") [Documentation](https://github.com/pablouser1/ProxiTok/wiki "Documentation") [Source Code](https://github.com/pablouser1/ProxiTok "Source Code")

Tip

ProxiTok is useful if you want to disable JavaScript in your browser, such as [Tor Browser](https://www.privacyguides.org/en/tor/#tor-browser) on the Safest security level.

## YouTube

**Note:** YouTube has gradually rolled out changes to its video player and API that have thwarted some of the methods used by third-party frontends for extracting YouTube data. If you experience reliability issues with one YouTube frontend, consider trying out another that uses a different extraction method.

### Invidious

![Invidious logo](https://www.privacyguides.org/en/assets/img/frontends/invidious.svg#only-light)![Invidious logo](https://www.privacyguides.org/en/assets/img/frontends/invidious-dark.svg#only-dark)

**Invidious** is a free and open-source frontend for [YouTube](https://youtube.com/) that is also self-hostable.

There are a number of public instances, with some that offer a [Tor](https://www.privacyguides.org/en/tor/) onion service or an [I2P](https://www.privacyguides.org/en/alternative-networks/#i2p-the-invisible-internet-project) eepsite.

[Homepage](https://invidious.io/) [Public Instances](https://docs.invidious.io/instances "Public Instances") [Documentation](https://docs.invidious.io/ "Documentation") [Source Code](https://github.com/iv-org/invidious "Source Code") [Contribute](https://invidious.io/donate "Contribute")

Warning

Invidious does not proxy video streams by default. Videos watched through Invidious will still make direct connections to Google's servers (e.g. `googlevideo.com`); however, some instances support video proxying—simply enable _Proxy videos_ within the instances' settings or add `&local=true` to the URL.

Tip

Invidious is useful if you want to disable JavaScript in your browser, such as [Tor Browser](https://www.privacyguides.org/en/tor/#tor-browser) on the Safest security level. It does not provide privacy by itself, and we don’t recommend logging into any accounts.

### Piped

![Piped logo](https://www.privacyguides.org/en/assets/img/frontends/piped.svg)

**Piped** is a free and open-source frontend for [YouTube](https://youtube.com/) that is also self-hostable.

Piped requires JavaScript in order to function and there are a number of public instances.

[Repository](https://github.com/TeamPiped/Piped) [Public Instances](https://github.com/TeamPiped/documentation/blob/main/content/docs/public-instances/index.md "Public Instances") [Documentation](https://docs.piped.video/docs "Documentation") [Source Code](https://github.com/TeamPiped/Piped "Source Code") [Contribute](https://github.com/TeamPiped/Piped#donations "Contribute")

Tip

Piped is useful if you want to use [SponsorBlock](https://sponsor.ajay.app/) without installing an extension. It does not provide privacy by itself, and we don’t recommend logging into any accounts.

### FreeTube

![FreeTube logo](https://www.privacyguides.org/en/assets/img/frontends/freetube.svg)

**FreeTube** is a free and open-source desktop application for [YouTube](https://youtube.com/). FreeTube extracts data from YouTube using its built-in API based on [YouTube.js](https://github.com/LuanRT/YouTube.js) or the [Invidious](https://www.privacyguides.org/en/frontends/#invidious) API. You can configure either as the default, with the other serving as a fallback.

When using FreeTube, your subscription list, playlists, watch history and search history are saved locally on your device.

[Homepage](https://freetubeapp.io/) [Privacy Policy](https://freetubeapp.io/privacy.php "Privacy Policy") [Documentation](https://docs.freetubeapp.io/ "Documentation") [Source Code](https://github.com/FreeTubeApp/FreeTube "Source Code") [Contribute](https://liberapay.com/FreeTube "Contribute")

Downloads

- [Windows](https://freetubeapp.io/#download)
- [macOS](https://freetubeapp.io/#download)
- [Linux](https://freetubeapp.io/#download)
- [Flathub](https://flathub.org/apps/details/io.freetubeapp.FreeTube)

Warning

When using FreeTube, your IP address may still be known to YouTube, [Invidious](https://instances.invidious.io/), or [SponsorBlock](https://sponsor.ajay.app/) depending on your configuration. Consider using a [VPN](https://www.privacyguides.org/en/vpn/) or [Tor](https://www.privacyguides.org/en/tor/) if your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/) requires hiding your IP address.

By default, FreeTube blocks all YouTube advertisements. In addition, FreeTube optionally integrates with [SponsorBlock](https://sponsor.ajay.app/) to help you skip sponsored video segments.

### Yattee

![Yattee logo](https://www.privacyguides.org/en/assets/img/frontends/yattee.svg)

**Yattee** is a free and open-source privacy oriented video player for iOS, tvOS, and macOS for [YouTube](https://youtube.com/). Due to App Store restrictions, you will need to take a few [extra steps](https://web.archive.org/web/20230330122839/https://gonzoknows.com/posts/Yattee) before you can use Yattee to watch YouTube. Yattee allows you to connect to instances of [Invidious](https://www.privacyguides.org/en/frontends/#invidious) or [Piped](https://www.privacyguides.org/en/frontends/#piped).

When using Yattee, your subscription list is saved locally on your device.

[Homepage](https://github.com/yattee/yattee) [Privacy Policy](https://r.yattee.stream/docs/privacy.html "Privacy Policy") [Documentation](https://github.com/yattee/yattee/wiki "Documentation") [Source Code](https://github.com/yattee/yattee "Source Code") [Contribute](https://github.com/yattee/yattee/wiki/Donations "Contribute")

Downloads

- [App Store](https://apps.apple.com/app/id1595136629)
- [GitHub](https://github.com/yattee/yattee/releases)

Warning

When using Yattee, your IP address may still be known to YouTube, [Invidious](https://instances.invidious.io/), [Piped](https://github.com/TeamPiped/Piped/wiki/Instances), or [SponsorBlock](https://sponsor.ajay.app/) depending on your configuration. Consider using a [VPN](https://www.privacyguides.org/en/vpn/) or [Tor](https://www.privacyguides.org/en/tor/) if your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/) requires hiding your IP address.

By default, Yattee blocks all YouTube advertisements. In addition, Yattee optionally integrates with [SponsorBlock](https://sponsor.ajay.app/) to help you skip sponsored video segments.

### LibreTube (Android)

![LibreTube logo](https://www.privacyguides.org/en/assets/img/frontends/libretube.svg#only-light)![LibreTube logo](https://www.privacyguides.org/en/assets/img/frontends/libretube-dark.svg#only-dark)

**LibreTube** is a free and open-source Android application for [YouTube](https://youtube.com/) which uses the [Piped](https://www.privacyguides.org/en/frontends/#piped) API.

Your subscription list and playlists are saved locally on your Android device.

[Homepage](https://libretube.dev/) [Privacy Policy](https://github.com/libre-tube/LibreTube/blob/master/PRIVACY_POLICY.md "Privacy Policy") [Documentation](https://libretube.dev/#faq "Documentation") [Source Code](https://github.com/libre-tube/LibreTube "Source Code") [Contribute](https://github.com/libre-tube/LibreTube#donate "Contribute")

Downloads

- [GitHub](https://github.com/libre-tube/LibreTube/releases)

Warning

When using LibreTube, your IP address will be visible to YouTube, [Piped](https://github.com/TeamPiped/Piped/wiki/Instances), or [SponsorBlock](https://sponsor.ajay.app/) depending on your configuration. Consider using a [VPN](https://www.privacyguides.org/en/vpn/) or [Tor](https://www.privacyguides.org/en/tor/) if your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/) requires hiding your IP address.

By default, LibreTube blocks all YouTube advertisements. Additionally, LibreTube uses [SponsorBlock](https://sponsor.ajay.app/) to help you skip sponsored video segments. You are able to fully configure the types of segments that SponsorBlock will skip, or disable it completely. There is also a button on the video player itself to disable it for a specific video if desired.

### NewPipe (Android)

![NewPipe logo](https://www.privacyguides.org/en/assets/img/frontends/newpipe.svg)

**NewPipe** is a free and open-source Android application for [YouTube](https://youtube.com/), [SoundCloud](https://soundcloud.com/), [media.ccc.de](https://media.ccc.de/), [Bandcamp](https://bandcamp.com/), and [PeerTube](https://joinpeertube.org/)

.

Your subscription list and playlists are saved locally on your Android device.

[Homepage](https://newpipe.net/) [Privacy Policy](https://newpipe.net/legal/privacy "Privacy Policy") [Documentation](https://newpipe.net/FAQ "Documentation") [Source Code](https://github.com/TeamNewPipe/NewPipe "Source Code") [Contribute](https://newpipe.net/donate "Contribute")

Downloads

- [GitHub](https://github.com/TeamNewPipe/NewPipe/releases)

Warning

When using NewPipe, your IP address will be visible to the video providers used. Consider using a [VPN](https://www.privacyguides.org/en/vpn/) or [Tor](https://www.privacyguides.org/en/tor/) if your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/) requires hiding your IP address.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

We only consider frontends if one of the following is true for a platform:

- Normally only accessible with JavaScript enabled.
- Normally only accessible with an account.
- Blocks access from commercial [VPNs](https://www.privacyguides.org/en/vpn/).

Recommended frontends...

- Must be open-source software.
- Must be self-hostable.
- Must provide all basic website functionality available to anonymous users.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).