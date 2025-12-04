```yaml
---
title: "Privacy-Focused Frontends for Popular Websites"
tags: [privacy, frontends, youtube, reddit, tiktok, self-hosting, open-source]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Self-Hosters, Technical Users]
topics: ["Alternative Frontends", "Privacy Protection", "Self-Hosting"]
summary: "Guide to open-source frontends that provide privacy-respecting access to Reddit, TikTok, and YouTube without tracking or account requirements."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of web browsers", "Familiarity with privacy concepts"]
estimated_read_time: "8 minutes"
---
```

# Privacy-Focused Frontends for Popular Websites

Sometimes services force you to sign up for an account by blocking content with popups, or they break without JavaScript enabled. Privacy-focused frontends allow you to circumvent these restrictions while avoiding surveillance.

## Important Considerations

### Self-Hosting
If you self-host these frontends, ensure other people use your instance so you can blend in. Be careful about where and how you host, as others' usage will be linked to your hosting.

### Using Public Instances
When using someone else's instance, read their privacy policy (if available). Owners can modify policies, so they may not reflect defaults. Some instances offer [Tor](https://www.privacyguides.org/en/tor/) .onion addresses for additional privacy, provided your queries don't contain personally identifiable information.

---

## Reddit

### Redlib

**Redlib** is an open-source frontend to Reddit that is also self-hostable.

- [Repository](https://github.com/redlib-org/redlib)
- [Public Instances](https://github.com/redlib-org/redlib-instances/blob/main/instances.md)
- [Documentation](https://github.com/redlib-org/redlib?tab=readme-ov-file#table-of-contents)

> **Note:** [Old Reddit](https://old.reddit.com/) requires less JavaScript than new Reddit but has blocked public VPN IP addresses. You can use Old Reddit with Tor via the onion service: `https://old.reddittorjg6rue252oqsxryoxengawnmo46qy4kyii5wtqnwfj4ooad.onion`

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

> **Note:** YouTube has gradually rolled out changes that have thwarted some methods used by third-party frontends. If you experience reliability issues, try another frontend that uses a different extraction method.

### Invidious (Web)

**Invidious** is a free and open-source frontend for YouTube that is also self-hostable. Some instances offer Tor onion services or I2P eepsites.

- [Homepage](https://invidious.io/)
- [Public Instances](https://docs.invidious.io/instances)
- [Documentation](https://docs.invidious.io/)
- [Source Code](https://github.com/iv-org/invidious)

> **Warning:** Invidious does not proxy video streams by default. Videos still make direct connections to Google's servers (e.g., `googlevideo.com`). To enable proxying, enable *Proxy videos* in settings or add `&local=true` to the URL.

> **Tip:** Works without JavaScript. Does not provide privacy by itself—avoid logging into accounts.

### Piped (Web)

**Piped** is a free and open-source frontend for YouTube that is also self-hostable. Requires JavaScript to function.

- [Repository](https://github.com/TeamPiped/Piped)
- [Public Instances](https://github.com/TeamPiped/documentation/blob/main/content/docs/public-instances/index.md)
- [Documentation](https://docs.piped.video/docs)

> **Tip:** Useful for [SponsorBlock](https://sponsor.ajay.app/) without installing an extension. Does not provide privacy by itself—avoid logging into accounts.

### FreeTube (Desktop)

**FreeTube** is a free and open-source desktop application for YouTube. It extracts data using [YouTube.js](https://github.com/LuanRT/YouTube.js) or the Invidious API (configurable with fallback). Subscriptions, playlists, watch history, and search history are saved locally.

- [Homepage](https://freetubeapp.io/)
- [Documentation](https://docs.freetubeapp.io/)
- [Source Code](https://github.com/FreeTubeApp/FreeTube)
- **Platforms:** Windows, macOS, Linux, [Flathub](https://flathub.org/apps/details/io.freetubeapp.FreeTube)

**Features:**
- Blocks all YouTube advertisements by default
- Optional [SponsorBlock](https://sponsor.ajay.app/) integration

> **Warning:** Your IP address may still be known to YouTube, Invidious, or SponsorBlock depending on configuration. Consider using a [VPN](https://www.privacyguides.org/en/vpn/) or [Tor](https://www.privacyguides.org/en/tor/) if your threat model requires hiding your IP.

### Yattee (iOS/macOS/tvOS)

**Yattee** is a free and open-source privacy-oriented video player for Apple platforms. Due to App Store restrictions, [extra setup steps](https://web.archive.org/web/20230330122839/https://gonzoknows.com/posts/Yattee) are required. Connects to Invidious or Piped instances. Subscriptions are saved locally.

- [Homepage](https://github.com/yattee/yattee)
- [Documentation](https://github.com/yattee/yattee/wiki)
- **Download:** [App Store](https://apps.apple.com/app/id1595136629) | [GitHub](https://github.com/yattee/yattee/releases)

**Features:**
- Blocks all YouTube advertisements by default
- Optional SponsorBlock integration

> **Warning:** Your IP address may be known to YouTube, Invidious, Piped, or SponsorBlock depending on configuration. Consider using a VPN or Tor if needed.

### LibreTube (Android)

**LibreTube** is a free and open-source Android application using the Piped API. Subscriptions and playlists are saved locally.

- [Homepage](https://libretube.dev/)
- [Documentation](https://libretube.dev/#faq)
- [Source Code](https://github.com/libre-tube/LibreTube)
- **Download:** [GitHub](https://github.com/libre-tube/LibreTube/releases)

**Features:**
- Blocks all YouTube advertisements by default
- SponsorBlock integration (fully configurable or can be disabled)
- Per-video disable option via player button

> **Warning:** Your IP address will be visible to YouTube, Piped, or SponsorBlock depending on configuration. Consider using a VPN or Tor if needed.

### NewPipe (Android)

**NewPipe** is a free and open-source Android application supporting YouTube, SoundCloud, media.ccc.de, Bandcamp, and PeerTube. Subscriptions and playlists are saved locally.

- [Homepage](https://newpipe.net/)
- [Documentation](https://newpipe.net/FAQ)
- [Source Code](https://github.com/TeamNewPipe/NewPipe)
- **Download:** [GitHub](https://github.com/TeamNewPipe/NewPipe/releases)

> **Warning:** Your IP address will be visible to video providers. Consider using a VPN or Tor if your threat model requires hiding your IP.

---

## Selection Criteria

These frontends are recommended because they address services that:
- Normally require JavaScript to function
- Normally require an account
- Block access from commercial VPNs

**Requirements for recommended frontends:**
- Must be open-source software
- Must be self-hostable
- Must provide all basic website functionality available to anonymous users