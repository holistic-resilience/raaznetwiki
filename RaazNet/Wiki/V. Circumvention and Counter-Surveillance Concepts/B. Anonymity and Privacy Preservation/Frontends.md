```yaml
---
title: "Privacy-Respecting Frontends for Popular Platforms"
tags: [privacy, frontends, youtube, reddit, tiktok, self-hosting, open-source]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Self-Hosters, Technical Users]
topics: ["Alternative Frontends", "Privacy Tools", "Self-Hosting"]
summary: "Guide to open-source frontends that provide privacy-respecting access to Reddit, TikTok, and YouTube without tracking or account requirements."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of web privacy", "Familiarity with browser settings"]
estimated_read_time: "8 minutes"
---
```

# Privacy-Respecting Frontends for Popular Platforms

Sometimes services force you to sign up for an account by blocking access to content with annoying popups, or they break without JavaScript enabled. Privacy-respecting frontends can help you circumvent these restrictions while reducing tracking.

## Key Considerations

### Self-Hosting
If you choose to self-host these frontends, ensure other people use your instance as well so you can blend in. Be careful about where and how you host, as other users' activity will be linked to your hosting.

### Using Public Instances
When using an instance run by someone else, read the privacy policy of that specific instance (if available). Operators can modify policies, so they may not reflect the default. Some instances offer [Tor](https://www.privacyguides.org/en/tor/) .onion addresses, which may grant additional privacy as long as your queries don't contain personally identifiable information.

---

## Reddit

### Redlib

**Redlib** is an open-source frontend to Reddit that is also self-hostable.

- [Repository](https://github.com/redlib-org/redlib)
- [Public Instances](https://github.com/redlib-org/redlib-instances/blob/main/instances.md)
- [Documentation](https://github.com/redlib-org/redlib?tab=readme-ov-file#table-of-contents)

> **Note:** [Old Reddit](https://old.reddit.com/) requires less JavaScript than new Reddit but has blocked access from public VPN IP addresses. You can use Old Reddit with the Tor Onion service at `https://old.reddittorjg6rue252oqsxryoxengawnmo46qy4kyii5wtqnwfj4ooad.onion/`

> **Tip:** Redlib works without JavaScript, making it ideal for [Tor Browser](https://www.privacyguides.org/en/tor/#tor-browser) on the Safest security level.

---

## TikTok

### ProxiTok

**ProxiTok** is an open-source frontend to TikTok that is also self-hostable. Some public instances offer Tor onion services or I2P eepsites.

- [Repository](https://github.com/pablouser1/ProxiTok)
- [Public Instances](https://github.com/pablouser1/ProxiTok/wiki/Public-instances)
- [Documentation](https://github.com/pablouser1/ProxiTok/wiki)

> **Tip:** ProxiTok works without JavaScript, making it ideal for Tor Browser on the Safest security level.

---

## YouTube

> **Note:** YouTube has gradually rolled out changes to its video player and API that have thwarted some methods used by third-party frontends. If you experience reliability issues with one frontend, try another that uses a different extraction method.

### Invidious (Web)

**Invidious** is a free and open-source web frontend for YouTube that is also self-hostable. Some instances offer Tor onion services or I2P eepsites.

- [Homepage](https://invidious.io/)
- [Public Instances](https://docs.invidious.io/instances)
- [Documentation](https://docs.invidious.io/)
- [Source Code](https://github.com/iv-org/invidious)

> **Warning:** Invidious does not proxy video streams by default. Videos will still make direct connections to Google's servers (e.g., `googlevideo.com`). To enable proxying, enable *Proxy videos* in settings or add `&local=true` to the URL.

> **Tip:** Invidious works without JavaScript. It does not provide privacy by itself—we don't recommend logging into any accounts.

### Piped (Web)

**Piped** is a free and open-source frontend for YouTube that is also self-hostable. Piped requires JavaScript to function.

- [Repository](https://github.com/TeamPiped/Piped)
- [Public Instances](https://github.com/TeamPiped/documentation/blob/main/content/docs/public-instances/index.md)
- [Documentation](https://docs.piped.video/docs)

> **Tip:** Piped is useful if you want to use [SponsorBlock](https://sponsor.ajay.app/) without installing an extension. It does not provide privacy by itself—we don't recommend logging into any accounts.

### FreeTube (Desktop)

**FreeTube** is a free and open-source desktop application for YouTube. It extracts data using its built-in API based on [YouTube.js](https://github.com/LuanRT/YouTube.js) or the Invidious API. You can configure either as default with the other as fallback.

Your subscription list, playlists, watch history, and search history are saved locally on your device.

- [Homepage](https://freetubeapp.io/)
- [Privacy Policy](https://freetubeapp.io/privacy.php)
- [Documentation](https://docs.freetubeapp.io/)
- [Source Code](https://github.com/FreeTubeApp/FreeTube)

**Available for:** Windows, macOS, Linux, [Flathub](https://flathub.org/apps/details/io.freetubeapp.FreeTube)

> **Warning:** Your IP address may still be known to YouTube, Invidious, or SponsorBlock depending on your configuration. Consider using a [VPN](https://www.privacyguides.org/en/vpn/) or [Tor](https://www.privacyguides.org/en/tor/) if your threat model requires hiding your IP address.

FreeTube blocks all YouTube advertisements by default and optionally integrates with SponsorBlock to skip sponsored segments.

### Yattee (iOS/macOS/tvOS)

**Yattee** is a free and open-source privacy-oriented video player for iOS, tvOS, and macOS. Due to App Store restrictions, you may need to take [extra steps](https://web.archive.org/web/20230330122839/https://gonzoknows.com/posts/Yattee) before use. Yattee connects to Invidious or Piped instances.

Your subscription list is saved locally on your device.

- [Homepage](https://github.com/yattee/yattee)
- [Privacy Policy](https://r.yattee.stream/docs/privacy.html)
- [Documentation](https://github.com/yattee/yattee/wiki)

**Available on:** [App Store](https://apps.apple.com/app/id1595136629), [GitHub](https://github.com/yattee/yattee/releases)

> **Warning:** Your IP address may still be known to YouTube, Invidious, Piped, or SponsorBlock depending on your configuration. Consider using a VPN or Tor if your threat model requires hiding your IP address.

Yattee blocks all YouTube advertisements by default and optionally integrates with SponsorBlock.

### LibreTube (Android)

**LibreTube** is a free and open-source Android application for YouTube using the Piped API. Your subscription list and playlists are saved locally on your device.

- [Homepage](https://libretube.dev/)
- [Privacy Policy](https://github.com/libre-tube/LibreTube/blob/master/PRIVACY_POLICY.md)
- [Documentation](https://libretube.dev/#faq)
- [Source Code](https://github.com/libre-tube/LibreTube)

**Download:** [GitHub](https://github.com/libre-tube/LibreTube/releases)

> **Warning:** Your IP address will be visible to YouTube, Piped, or SponsorBlock depending on your configuration. Consider using a VPN or Tor if your threat model requires hiding your IP address.

LibreTube blocks all YouTube advertisements by default and uses SponsorBlock to skip sponsored segments. You can fully configure which segment types to skip or disable it entirely.

### NewPipe (Android)

**NewPipe** is a free and open-source Android application supporting YouTube, SoundCloud, media.ccc.de, Bandcamp, and PeerTube. Your subscription list and playlists are saved locally on your device.

- [Homepage](https://newpipe.net/)
- [Privacy Policy](https://newpipe.net/legal/privacy)
- [Documentation](https://newpipe.net/FAQ)
- [Source Code](https://github.com/TeamNewPipe/NewPipe)

**Download:** [GitHub](https://github.com/TeamNewPipe/NewPipe/releases)

> **Warning:** Your IP address will be visible to the video providers used. Consider using a VPN or Tor if your threat model requires hiding your IP address.

---

## Selection Criteria

### Why These Platforms Need Frontends
- Normally only accessible with JavaScript enabled
- Normally require an account
- Block access from commercial VPNs

### Requirements for Recommended Frontends
- Must be open-source software
- Must be self-hostable
- Must provide all basic website functionality available to anonymous users