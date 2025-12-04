```yaml
---
title: "Privacy-Respecting Frontends for Popular Platforms"
tags: [privacy, frontends, self-hosting, youtube, reddit, tiktok]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Self-Hosters, Technical Users]
topics: ["Alternative Frontends", "Privacy Tools", "Self-Hosting"]
summary: "Guide to open-source frontend alternatives for Reddit, TikTok, and YouTube that bypass tracking and JavaScript requirements."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of web privacy", "Familiarity with VPNs and Tor (optional)"]
estimated_read_time: "8 minutes"
---
```

# Privacy-Respecting Frontends for Popular Platforms

Sometimes services force you to sign up for an account by blocking access to content with annoying popups, or they break without JavaScript enabled. Privacy-respecting frontends can help you circumvent these restrictions while reducing tracking.

## Important Considerations

### Self-Hosting
If you choose to self-host these frontends, ensure other people use your instance as well so you can blend in. Be careful with where and how you host, as other users' activity will be linked to your hosting.

### Using Public Instances
When using an instance run by someone else, read the privacy policy of that specific instance (if available). Owners can modify policies, so they may not reflect defaults. Some instances have Tor .onion addresses, which may grant additional privacy as long as your search queries don't contain personally identifiable information.

---

## Reddit

### Redlib

**Redlib** is an open-source frontend to Reddit that is also self-hostable. You can access Redlib through a number of public instances.

- [Repository](https://github.com/redlib-org/redlib)
- [Public Instances](https://github.com/redlib-org/redlib-instances/blob/main/instances.md)
- [Documentation](https://github.com/redlib-org/redlib?tab=readme-ov-file#table-of-contents)

> **Note:** The Old Reddit website doesn't require as much JavaScript as new Reddit, but it has recently blocked access to IP addresses reserved for public VPNs. You can use Old Reddit with the Tor Onion service at: `https://old.reddittorjg6rue252oqsxryoxengawnmo46qy4kyii5wtqnwfj4ooad.onion/`

> **Tip:** Redlib is useful if you want to disable JavaScript in your browser, such as Tor Browser on the Safest security level.

---

## TikTok

### ProxiTok

**ProxiTok** is an open-source frontend to TikTok that is also self-hostable. There are a number of public instances, with some offering Tor onion services or I2P eepsites.

- [Repository](https://github.com/pablouser1/ProxiTok)
- [Public Instances](https://github.com/pablouser1/ProxiTok/wiki/Public-instances)
- [Documentation](https://github.com/pablouser1/ProxiTok/wiki)

> **Tip:** ProxiTok is useful if you want to disable JavaScript in your browser, such as Tor Browser on the Safest security level.

---

## YouTube

> **Note:** YouTube has gradually rolled out changes to its video player and API that have thwarted some methods used by third-party frontends. If you experience reliability issues with one frontend, consider trying another that uses a different extraction method.

### Web-Based Frontends

#### Invidious

**Invidious** is a free and open-source frontend for YouTube that is also self-hostable. There are a number of public instances, with some offering Tor onion services or I2P eepsites.

- [Homepage](https://invidious.io/)
- [Public Instances](https://docs.invidious.io/instances)
- [Documentation](https://docs.invidious.io/)
- [Source Code](https://github.com/iv-org/invidious)

> **Warning:** Invidious does not proxy video streams by default. Videos watched through Invidious will still make direct connections to Google's servers (e.g. `googlevideo.com`). To enable proxying, enable *Proxy videos* in the instance settings or add `&local=true` to the URL.

> **Tip:** Invidious is useful if you want to disable JavaScript in your browser. It does not provide privacy by itself—we don't recommend logging into any accounts.

#### Piped

**Piped** is a free and open-source frontend for YouTube that is also self-hostable. Piped requires JavaScript to function.

- [Repository](https://github.com/TeamPiped/Piped)
- [Public Instances](https://github.com/TeamPiped/documentation/blob/main/content/docs/public-instances/index.md)
- [Documentation](https://docs.piped.video/docs)

> **Tip:** Piped is useful if you want to use SponsorBlock without installing an extension. It does not provide privacy by itself—we don't recommend logging into any accounts.

### Desktop Applications

#### FreeTube

**FreeTube** is a free and open-source desktop application for YouTube. It extracts data using its built-in API based on YouTube.js or the Invidious API. You can configure either as the default, with the other serving as a fallback.

Your subscription list, playlists, watch history, and search history are saved locally on your device.

- [Homepage](https://freetubeapp.io/)
- [Privacy Policy](https://freetubeapp.io/privacy.php)
- [Documentation](https://docs.freetubeapp.io/)
- [Source Code](https://github.com/FreeTubeApp/FreeTube)

**Available for:** Windows, macOS, Linux (including Flathub)

> **Warning:** Your IP address may still be known to YouTube, Invidious, or SponsorBlock depending on your configuration. Consider using a VPN or Tor if your threat model requires hiding your IP address.

**Features:**
- Blocks all YouTube advertisements by default
- Optional SponsorBlock integration to skip sponsored segments

### Mobile Applications

#### Yattee (iOS/tvOS/macOS)

**Yattee** is a free and open-source privacy-oriented video player for iOS, tvOS, and macOS. Due to App Store restrictions, you may need to take extra steps before using Yattee. It connects to Invidious or Piped instances.

Your subscription list is saved locally on your device.

- [Homepage](https://github.com/yattee/yattee)
- [Privacy Policy](https://r.yattee.stream/docs/privacy.html)
- [Documentation](https://github.com/yattee/yattee/wiki)

**Available on:** App Store, GitHub

> **Warning:** Your IP address may still be known to YouTube, Invidious, Piped, or SponsorBlock depending on your configuration. Consider using a VPN or Tor if your threat model requires hiding your IP address.

**Features:**
- Blocks all YouTube advertisements by default
- Optional SponsorBlock integration

#### LibreTube (Android)

**LibreTube** is a free and open-source Android application for YouTube which uses the Piped API. Your subscription list and playlists are saved locally on your Android device.

- [Homepage](https://libretube.dev/)
- [Privacy Policy](https://github.com/libre-tube/LibreTube/blob/master/PRIVACY_POLICY.md)
- [Documentation](https://libretube.dev/#faq)
- [Source Code](https://github.com/libre-tube/LibreTube)

**Available on:** GitHub

> **Warning:** Your IP address will be visible to YouTube, Piped, or SponsorBlock depending on your configuration. Consider using a VPN or Tor if your threat model requires hiding your IP address.

**Features:**
- Blocks all YouTube advertisements by default
- SponsorBlock integration with configurable segment types
- Per-video SponsorBlock toggle

#### NewPipe (Android)

**NewPipe** is a free and open-source Android application supporting multiple platforms: YouTube, SoundCloud, media.ccc.de, Bandcamp, and PeerTube.

Your subscription list and playlists are saved locally on your Android device.

- [Homepage](https://newpipe.net/)
- [Privacy Policy](https://newpipe.net/legal/privacy)
- [Documentation](https://newpipe.net/FAQ)
- [Source Code](https://github.com/TeamNewPipe/NewPipe)

**Available on:** GitHub

> **Warning:** Your IP address will be visible to the video providers used. Consider using a VPN or Tor if your threat model requires hiding your IP address.

---

## Selection Criteria

These frontends are recommended because they address common issues with mainstream platforms:
- Normally only accessible with JavaScript enabled
- Normally only accessible with an account
- Blocks access from commercial VPNs

**All recommended frontends must:**
- Be open-source software
- Be self-hostable
- Provide all basic website functionality available to anonymous users