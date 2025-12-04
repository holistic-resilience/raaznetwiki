```yaml
---
title: "Privacy Respecting Web Browsers for Android and iOS"
tags: [privacy, mobile-browsers, android, ios, brave, safari, chromium]
category: "Mobile Privacy"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Mobile Users]
topics: ["Mobile Security", "Browser Privacy", "Digital Privacy"]
summary: "Recommended privacy-focused mobile web browsers and configuration settings for Android and iOS devices."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic smartphone usage", "Understanding of browser settings"]
estimated_read_time: "12 minutes"
---
```

# Privacy Respecting Web Browsers for Android and iOS

These are the currently recommended **mobile web browsers** and configurations for standard/non-anonymous internet browsing. If you need to browse the internet anonymously, you should use [Tor](https://www.privacyguides.org/en/tor/) instead.

---

## Brave Browser

**Brave Browser** includes a built-in content blocker and [privacy features](https://brave.com/privacy-features), many of which are enabled by default. Brave is built upon the Chromium web browser project, so it should feel familiar and have minimal website compatibility issues.

**Resources:**
- [Homepage](https://brave.com/) | [Onion Service](https://brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/)
- [Privacy Policy](https://brave.com/privacy/browser) | [Documentation](https://support.brave.com/) | [Source Code](https://github.com/brave/brave-browser)

**Downloads:**
- [Google Play](https://play.google.com/store/apps/details?id=com.brave.browser) | [App Store](https://apps.apple.com/app/id1052879175)
- [GitHub](https://github.com/brave/brave-browser/releases) | [F-Droid](https://brave-browser-apk-release.s3.brave.com/fdroid/repo/index.html)

### Recommended Brave Configuration

> **Note:** Tor Browser is the only way to truly browse the internet anonymously. All browsers other than Tor Browser will be traceable by *somebody* in some regard.

Settings location: **☰ → Settings → Brave Shields & privacy** (Android) or **☰ → Settings → Shields & Privacy** (iOS)

#### Brave Shields Global Defaults

Brave includes anti-fingerprinting measures in its [Shields](https://support.brave.com/hc/articles/360022973471-What-is-Shields) feature. Configure these options [globally](https://support.brave.com/hc/articles/360023646212-How-do-I-configure-global-and-site-specific-Shields-settings) across all pages.

##### Android Settings
- Select **Aggressive** under *Block trackers & ads*
- Enable **Auto-redirect AMP pages**
- Enable **Auto-redirect tracking URLs**
- Select **Require all connections to use HTTPS (strict)** under *Upgrade connections to HTTPS*
- Select **Block third-party cookies** under *Block Cookies*
- Enable **Block Fingerprinting**
- Enable **Prevent fingerprinting via language settings**
- Enable **Forget me when I close this site**
- (Optional) Enable **Block Scripts**

##### iOS Settings
- Select **Aggressive** under *Trackers & Ads Blocking*
- Select **Strict** under *Upgrade Connections to HTTPS*
- Enable **Auto-Redirect AMP pages**
- Enable **Auto-Redirect Tracking URLs**
- Enable **Block Fingerprinting**
- Select **Site Tabs Closed** under *Auto Shred*
- (Optional) Enable **Block Scripts**

> **Important:** Keep the default filter lists. Using extra content filter lists will make you stand out from other Brave users and may increase attack surface if there is an exploit in Brave.

#### Additional Privacy Settings

##### Android Only
- Enable **Clear data on exit** (under Clear browsing data)
- Select **Disable non-proxied UDP** under [WebRTC IP handling policy](https://support.brave.com/hc/articles/360017989132-How-do-I-change-my-Privacy-Settings#webrtc)
- (Optional) Select **No protection** under *Safe Browsing*
- Disable **Allow sites to check if you have payment methods saved**
- Disable **Javascript optimization & security**
- Enable **Close tabs on exit**
- Uncheck all social media components (under Social Media Blocking)

##### Both Platforms
- Disable **Allow privacy-preserving product analytics (P3A)**
- Disable **Automatically send diagnostic reports**
- Disable **Automatically send daily usage ping to Brave**

#### Leo Settings
Location: **☰ → Settings → Leo**
- Disable **Show autocomplete suggestions in address bar**

#### Search Engine Settings
Location: **☰ → Settings → Search engines**
- Disable **Show search suggestions**

#### Brave Sync
[Brave Sync](https://support.brave.com/hc/articles/360059793111-Understanding-Brave-Sync) allows your browsing data (history, bookmarks, etc.) to be accessible on all your devices without requiring an account and protects it with E2EE.

---

## Cromite (Android Only)

**Cromite** is a Chromium-based browser with built-in ad blocking, fingerprinting protections, and other [privacy and security enhancements](https://github.com/uazo/cromite/blob/master/docs/FEATURES.md). It is a fork of the discontinued Bromite browser.

**Resources:**
- [Homepage](https://cromite.org/)
- [Privacy Policy](https://github.com/uazo/cromite/blob/master/docs/PRIVACY_POLICY.md) | [Documentation](https://github.com/uazo/cromite?tab=readme-ov-file#docs) | [Source Code](https://github.com/uazo/cromite)

**Downloads:**
- [F-Droid](https://cromite.org/fdroid/repo/?fingerprint=49F37E74DEE483DCA2B991334FB5A0200787430D0B5F9A783DD5F13695E9517B) | [GitHub](https://github.com/uazo/cromite/releases/latest)

### Recommended Configuration

Settings location: **⋮ → ⚙ Settings → Privacy and security**

#### Browsing Data
- Enable **Close all open tabs on exit**

#### Incognito Mode
- Enable **Open external links in incognito**

#### Security
- Enable **Always use secure connections**

> **Note:** HTTP is extremely uncommon nowadays, so this should have little to no impact on your day-to-day browsing.

#### Adblock Plus Settings
Location: **⋮ → ⚙ Settings → Adblock Plus settings**

Cromite contains a customized version of Adblock Plus with EasyList enabled by default.

- (Optional) Enable **Enable anti-circumvention and snippets** — increases content blocking effectiveness but may make you stand out

> **Warning:** Using extra filter lists will make you stand out from other Cromite users and may increase attack surface if a malicious rule is added.

#### Legacy Adblock Settings
Location: **⋮ → ⚙ Settings → Legacy Adblock settings**
- Disable the autoupdate setting (disables update checks for unmaintained Bromite adblock filter)

---

## Safari (iOS Only)

On iOS, any app that can browse the web is [restricted](https://developer.apple.com/app-store/review/guidelines) to using Apple's [WebKit framework](https://developer.apple.com/documentation/webkit). This means browsers like Brave on iOS don't use the same engine as their Android counterparts.

**Safari** is the default browser in iOS with [privacy features](https://support.apple.com/guide/iphone/browse-the-web-privately-iphb01fc3c85/ios) including:
- [Intelligent Tracking Prevention](https://webkit.org/blog/7675/intelligent-tracking-prevention)
- Isolated and ephemeral Private Browsing tabs
- Fingerprinting protection and randomization
- Private Relay (for iCloud+ subscribers)

**Resources:**
- [Homepage](https://apple.com/safari) | [Privacy Policy](https://apple.com/legal/privacy/data/en/safari) | [Documentation](https://support.apple.com/guide/iphone/browse-the-web-iph1fbef4daa/ios)

### Recommended Safari Configuration

Settings location: **⚙ Settings → Apps → Safari**

#### Allow Safari to Access
Disable all of the following to prevent Siri from using Safari content:
- Learn from this App
- Show in App
- Show on Home Screen
- Suggest App

#### Search
- Disable **Search Engine Suggestions** — prevents sending address bar input to your search engine

#### Profiles
Safari allows you to separate your browsing with different profiles. All cookies, history, and website data are separate for each profile. Use different profiles for different purposes (e.g., Shopping, Work, School).

#### Privacy & Security
- Enable **Prevent Cross-Site Tracking** — enables WebKit's Intelligent Tracking Protection
- Enable **Require Face ID/Touch ID to Unlock Private Browsing**
- Disable **Fraudulent Website Warning** — prevents IP logging by Google/Tencent Safe Browsing (reduces phishing protection)
- Enable **Not Secure Connection Warning**
- Disable **Highlights** — prevents Safari from sending webpage information to Apple

#### Settings for Websites
Set the following to **Ask**:
- Camera
- Microphone
- Location

#### Advanced Settings
Location: **⚙ Settings → Apps → Safari → Advanced**

##### Fingerprinting Mitigations
- Select **All Browsing** or **Private Browsing**

##### Privacy Preserving Ad Measurement
- Disable **Privacy Preserving Ad Measurement**

> **Note:** [Private Click Measurement](https://webkit.org/blog/11529/introducing-private-click-measurement-pcm) has little privacy concerns, but its automatic disabling in Private Browsing suggests disabling it entirely.

#### Always-on Private Browsing
1. Open Safari and tap the Tabs button (bottom right)
2. Expand the Tab Groups list
3. Select **Private**

Private Browsing uses a new [ephemeral](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410529-ephemeral) session for each tab, meaning tabs are isolated from one another.

> **Note:** Private Browsing does not save cookies and website data, so you won't remain signed in to sites.

#### iCloud Sync
Safari History, Tab Groups, iCloud Tabs, and saved passwords are E2EE. However, bookmarks are [not encrypted by default](https://support.apple.com/HT202303).

To enable E2EE for bookmarks and downloads:
1. Go to **⚙ Settings → iCloud → Advanced Data Protection**
2. Enable **Advanced Data Protection**

If not using Advanced Data Protection, set Safari's default download location to a local folder: **⚙ Settings → Apps → Safari → General → Downloads**

---

## Selection Criteria

These recommendations are based on the following minimum requirements:

- Must support automatic updates
- Must receive engine updates from upstream releases quickly
- Must support content blocking
- Privacy-enhancing changes should not negatively impact user experience

For complete criteria details, see [Privacy Guides' standard criteria](https://www.privacyguides.org/en/about/criteria/).