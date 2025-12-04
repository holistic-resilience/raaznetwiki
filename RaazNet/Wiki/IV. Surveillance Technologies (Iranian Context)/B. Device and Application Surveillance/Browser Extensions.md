---
title: "Browser Extensions for Privacy"
tags: [privacy, browser-extensions, content-blocking, ublock-origin, adguard]
category: "Browser Privacy"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users]
topics: ["Browser Security", "Content Blocking", "Privacy Protection"]
summary: "Guide to recommended privacy-focused browser extensions, focusing on content blockers like uBlock Origin and AdGuard."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic browser usage"]
estimated_read_time: "6 minutes"
---

# Browser Extensions for Privacy

In general, keep your browser extensions to a minimum to decrease your attack surface. Extensions have privileged access within your browser, require you to trust the developer, can make you [stand out through fingerprinting](https://en.wikipedia.org/wiki/Device_fingerprint#Browser_fingerprint), and [weaken site isolation](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/0ei-UCHNm34/m/lDaXwQhzBAAJ).

However, some extensions provide functionality that outweighs these downsides, particularly for content blocking.

> **Key Principle:** Don't install extensions you don't immediately need, or ones that duplicate your browser's built-in functionality. For example, Brave users don't need uBlock Origin because Brave Shields provides the same functionality.

## Content Blockers

### uBlock Origin

**uBlock Origin** is a popular content blocker that helps you block ads, trackers, and fingerprinting scripts.

**Resources:**
- [Repository & Documentation](https://github.com/gorhill/uBlock/wiki)
- [Privacy Policy](https://github.com/gorhill/uBlock/wiki/Privacy-policy)

**Downloads:**
- [Firefox](https://addons.mozilla.org/firefox/addon/ublock-origin)
- [Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak)

**Configuration Tips:**
- Follow the [developer's documentation on blocking modes](https://github.com/gorhill/uBlock/wiki/Blocking-mode)
- Be cautious with additional filter lists—they can impact performance and [increase attack surface](https://portswigger.net/research/ublock-i-exfiltrate-exploiting-ad-blockers-with-css)

**Recommended Additional Filters:**
- Enable **Privacy > AdGuard URL Tracking Protection**
- Add [Actually Legitimate URL Shortener Tool](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt)

### uBlock Origin Lite

A "Lite" version with limited features but distinct advantages. Consider it if:

- You don't want to grant full "read/modify website data" permissions to any extension
- You want a more resource-efficient content blocker
- Your browser only supports Manifest V3 extensions

**Downloads:**
- [Chrome](https://chrome.google.com/webstore/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/cimighlppcgcoapaliogpjjdehbnofhn)
- [Safari](https://apps.apple.com/app/id6745342698)

**Important Considerations:**
- Only supports pre-selected filter lists with no manual element blocking
- Filter updates occur only when the extension updates (typically every 2-7 days)
- For "permission-less" configuration, leave default setting as "Basic" and adjust per-site as needed
- Setting to "Optimal" or "Complete" grants read/modify access to all visited sites

### AdGuard for iOS

For Safari users on iOS (where uBlock Origin isn't available), AdGuard provides an adequate alternative.

**AdGuard for iOS** is a free, open-source content-blocking extension using Safari's native [Content Blocker API](https://developer.apple.com/documentation/safariservices/creating_a_content_blocker).

**Downloads:**
- [App Store](https://apps.apple.com/app/id1047223162)

**Notes:**
- Standard Safari content blocking is free
- Additional filter lists slow performance and increase attack surface—only apply what you need
- Some premium features available

## Extension Selection Criteria

When evaluating browser extensions for privacy:

1. **Must not replicate built-in functionality** - Don't duplicate what your browser or OS already provides
2. **Must directly impact user privacy** - Should actively protect privacy, not just provide information

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/browser-extensions/)*