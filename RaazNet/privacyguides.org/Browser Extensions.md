---
title: "Browser Extensions"
tags:
  [privacy, security, browser-extensions, content-blocking, tracking-protection]
category: "Tool Recommendations"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Technical Users]
topics: ["Web Privacy", "Ad Blocking", "Extension Security"]
summary: "Recommendations and guidance on privacy-preserving browser extensions like uBlock Origin, uBlock Origin Lite, and AdGuard, and how to minimize extension-related risks."
source: "Privacy Guides"
content_type: "Recommendation Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic web browsing knowledge"]
estimated_read_time: "7 minutes"
---

[Skip to content](https://www.privacyguides.org/en/browser-extensions/#content-blockers)

![](https://www.privacyguides.org/en/assets/img/cover/browser-extensions.webp)

# Browser Extensions

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/browser-extensions.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

In general, we recommend keeping your browser extensions to a minimum to decrease your attack surface. They have privileged access within your browser, require you to trust the developer, can make you [stand out](https://en.wikipedia.org/wiki/Device_fingerprint#Browser_fingerprint), and [weaken](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/0ei-UCHNm34/m/lDaXwQhzBAAJ) site isolation.

However, some provide functionality which can outweigh these downsides in certain situations, particularly when it comes to [content blocking](https://www.privacyguides.org/en/basics/common-threats/#mass-surveillance-programs).

Don't install extensions which you don't immediately have a need for, or ones that duplicate the functionality of your browser. For example, [Brave](https://www.privacyguides.org/en/desktop-browsers/#brave) users don't need to install uBlock Origin, because Brave Shields already provides the same functionality.

## Content Blockers

### uBlock Origin

![uBlock Origin logo](https://www.privacyguides.org/en/assets/img/browsers/ublock_origin.svg)

**uBlock Origin** is a popular content blocker that could help you block ads, trackers, and fingerprinting scripts.

[Repository](https://github.com/gorhill/uBlock#readme) [Privacy Policy](https://github.com/gorhill/uBlock/wiki/Privacy-policy "Privacy Policy") [Documentation](https://github.com/gorhill/uBlock/wiki "Documentation") [Source Code](https://github.com/gorhill/uBlock "Source Code")

Downloads

- [Firefox](https://addons.mozilla.org/firefox/addon/ublock-origin)
- [Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak)

We suggest following the [developer's documentation](https://github.com/gorhill/uBlock/wiki/Blocking-mode) and picking one of the "modes". Additional filter lists can impact performance and [may increase attack surface](https://portswigger.net/research/ublock-i-exfiltrate-exploiting-ad-blockers-with-css).

These are some other [filter lists](https://github.com/gorhill/uBlock/wiki/Dashboard:-Filter-lists) that you may want to consider adding:

- Check **Privacy** > **AdGuard URL Tracking Protection**
- Add [Actually Legitimate URL Shortener Tool](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt)

### uBlock Origin Lite

uBlock Origin also has a "Lite" version of their extension, which offers a very limited feature-set compared to the original extension. However, it has a few distinct advantages over its full-fledged sibling, so you may want to consider it if...

- ...you don't want to grant full "read/modify website data" permissions to any extensions (even a trusted one like uBlock Origin)
- ...you want a more resource (memory/CPU) efficient content blocker[1](https://www.privacyguides.org/en/browser-extensions/#fn:1)
- ...your browser only supports Manifest V3 extensions

![uBlock Origin Lite logo](https://www.privacyguides.org/en/assets/img/browsers/ublock_origin_lite.svg)

**uBlock Origin Lite** is a Manifest V3 compatible content blocker. Compared to the original _uBlock Origin_, this extension does not require broad "read/modify data" permissions to function, which lowers the risk of [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy) on your browser if a malicious rule is added to a filter list.

[Repository](https://github.com/uBlockOrigin/uBOL-home#readme) [Privacy Policy](https://github.com/uBlockOrigin/uBOL-home/wiki/Privacy-policy "Privacy Policy") [Documentation](https://github.com/uBlockOrigin/uBOL-home/wiki "Documentation") [Source Code](https://github.com/gorhill/uBlock/tree/master/platform/mv3 "Source Code")

Downloads

- [Chrome](https://chrome.google.com/webstore/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/cimighlppcgcoapaliogpjjdehbnofhn)
- [Safari](https://apps.apple.com/app/id6745342698)

We only recommend this version of uBlock Origin if you never want to make any changes to your filter lists, because it only supports a few pre-selected lists and offers no additional customization options, including the ability to select elements to block manually. These restrictions are due to limitations in Manifest V3's design.

This version offers three levels of blocking: "Basic" works without requiring any special privileges to view and modify site content, while the "Optimal" and "Complete" levels do require that broad permission, but offer a better filtering experience with additional cosmetic rules and scriptlet injections.

If you set the default filtering mode to "Optimal" or "Complete" the extension will request read/modify access to **all** websites you visit. However, you also have the option to change the setting to "Optimal" or "Complete" on a **per-site** basis by adjusting the slider in the extension's pop-up panel on any given site. When you do so, the extension will request read/modify access to that site only. Therefore, if you want to take advantage of uBlock Origin Lite's "permission-less" configuration, you should probably leave the default setting as "Basic" and only adjust it higher on sites where that level is not adequate.

uBlock Origin Lite only receives block list updates whenever the extension is updated from your browser's extension marketplace, as opposed to on demand. Google has an [expedited review process](https://developer.chrome.com/docs/webstore/skip-review) for filter updates, which means you still typically receive filter list updates as frequently as uBlock Origin Lite chooses to publish a release (historically every 2-7 days). However, only so-called " [safe rules](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest#safe_rules)" can be updated, which may limit the update frequency of lists using advanced techniques.

### AdGuard

We recommend [Safari](https://www.privacyguides.org/en/mobile-browsers/#safari-ios) for iOS users, which unfortunately is not supported by uBlock Origin. Luckily, AdGuard provides an adequate alternative:

![AdGuard logo](https://www.privacyguides.org/en/assets/img/browsers/adguard.svg)

**AdGuard for iOS** is a free and open-source content-blocking extension for Safari that uses the native [Content Blocker API](https://developer.apple.com/documentation/safariservices/creating_a_content_blocker).

[Homepage](https://adguard.com/en/adguard-ios/overview.html) [Privacy Policy](https://adguard.com/privacy/ios.html "Privacy Policy") [Documentation](https://kb.adguard.com/ios "Documentation") [Source Code](https://github.com/AdguardTeam/AdguardForiOS "Source Code")

Downloads

- [App Store](https://apps.apple.com/app/id1047223162)

Additional filter lists do slow things down and may increase your attack surface, so only apply what you need. AdGuard for iOS has some premium features; however, standard Safari content blocking is free of charge.

## Criteria

- Must not replicate built-in browser or OS functionality.
- Must directly impact user privacy, i.e. must not simply provide information.

---

1. uBlock Origin Lite _itself_ will consume no resources, because it uses newer APIs which make the browser process the filter lists natively, instead of running JavaScript code within the extension to handle the filtering. However, this resource advantage is only [theoretical](<https://github.com/uBlockOrigin/uBOL-home/wiki/Frequently-asked-questions-(FAQ)#is-ubol-more-efficient-cpu--and-memory-wise-than-ubo>), because it's possible that standard uBlock Origin's filtering code is more efficient than your browser's native filtering code. This has not yet been benchmarked.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
