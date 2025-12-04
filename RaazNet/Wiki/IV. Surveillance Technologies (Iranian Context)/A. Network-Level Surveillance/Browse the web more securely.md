```yaml
---
title: "Browse the Web More Securely"
tags: [browser-security, privacy, web-browsing, tracking-protection, digital-security]
category: "Internet Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Web Browser Security", "Privacy Protection", "Tracking Prevention"]
summary: "Comprehensive guide to choosing secure browsers, configuring privacy settings, and protecting yourself while browsing the web."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Familiarity with web browsers"]
estimated_read_time: "15 minutes"
---
```

# Browse the Web More Securely

A web browser is one of the digital tools most of us use daily. It is the main way many people access the internet. Because we rely so much on browsers, they are often targets for people who want to compromise your privacy or security. Follow the steps below to choose a more secure browser and strengthen its protection.

## Table of Contents

- [Choose a Web Browser](#choose-a-web-browser)
- [Change Your Device's Default Browser](#change-your-devices-default-browser)
- [Keep Your Browser Updated](#keep-your-browser-updated)
- [Use the Address Bar Properly](#use-the-address-bar-properly)
- [Set Your Default Search Engine](#set-your-default-search-engine)
- [Review Site Permissions](#review-site-permissions)
- [Secure Your Connections](#secure-your-connections)
- [Enable Tracking Protection](#enable-tracking-protection)
- [Disable the Built-in Password Manager](#disable-the-built-in-password-manager)
- [Use Protective Browser Extensions](#use-protective-browser-extensions)
- [Manage Extensions and Pop-ups](#manage-extensions-and-pop-ups)
- [Delete Your Browsing History](#delete-your-browsing-history)
- [Use Private Browsing Mode](#use-private-browsing-mode)
- [Control Startup and Homepage Settings](#control-startup-and-homepage-settings)
- [Recognize and Report Malicious Websites](#recognize-and-report-malicious-websites)

---

## Choose a Web Browser

Most operating systems come with pre-installed browsers (Safari on macOS/iOS, Edge on Windows). These browsers are not designed with privacy and security as their primary focus. We recommend using more security-oriented alternatives.

### Recommended Browsers

| Browser | Platforms | Notes |
|---------|-----------|-------|
| [Firefox](https://www.mozilla.org/en-US/firefox/all/) | Windows, macOS, Linux, Android, iOS | Free, open-source, excellent built-in security |
| [Chromium](https://www.chromium.org/) | Windows, macOS, Linux, Android | Free, open-source alternative to Chrome |
| [DuckDuckGo Privacy Browser](https://duckduckgo.com/duckduckgo-help-pages/get-duckduckgo/browser/) | Windows, macOS, iOS, Android | Automatically blocks trackers and upgrades to HTTPS |
| [Tor Browser](https://www.torproject.org/download/) | Windows, macOS, Linux, Android | For anonymized browsing; see [anonymization guide](https://securityinabox.org/en/internet-connection/anonymity) |

> **Tip:** Consider installing two browsers—one for sensitive activities and another for everyday browsing. Read more in the [multiple identity management guide](https://securityinabox.org/en/communication/multiple-identities/#different-devices).

**On Android:** You can install secure browsers through [FFUpdater](https://github.com/Tobi823/ffupdater), available on [F-Droid](https://f-droid.org/en/packages/de.marmaro.krt.ffupdater/).

### Why This Matters

Firefox is free, open-source software with better built-in security than most browsers. While Chrome has quality security, it's proprietary and may send more data to Google than you're comfortable with. If using Chrome, consider not logging into your Google account.

---

## Change Your Device's Default Browser

Setting a privacy-focused browser as your default ensures that links you click in other apps open in a more secure environment.

### How to Change Your Default Browser

- **Firefox:** [Instructions for all platforms](https://support.mozilla.org/en-US/kb/make-firefox-your-default-browser)
- **Chrome:** [Windows/macOS](https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop) | [iOS](https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DiOS&oco=0)
- **Ubuntu:** [Change default browser](https://help.ubuntu.com/stable/ubuntu-help/net-default-browser.html)
- **Windows:** [Stop Edge from auto-starting](https://support.microsoft.com/microsoft-edge/stop-microsoft-edge-from-starting-automatically-c341c879-799a-dccd-d6be-bc51ecdd5804)

> **Important:** Deactivate or uninstall browsers you don't use. Always think twice before opening links received through messages or emails—see the [malware guide](https://securityinabox.org/en/phones-and-computers/malware/#pause-before-you-click-and-be-cautious-when-you-receive-a-link).

---

## Keep Your Browser Updated

Browser updates patch security vulnerabilities. While browsers typically update automatically, verify periodically.

- **Firefox:** [Check for updates](https://support.mozilla.org/kb/update-firefox-latest-release)
- **Chrome/Chromium:** [Update guide](https://www.google.com/chrome/update/)
- **Tor Browser:** [Update instructions](https://tb-manual.torproject.org/updating/)

---

## Use the Address Bar Properly

The address bar displays the current web address and allows you to navigate directly to websites.

### Best Practices

- **Type complete addresses** (e.g., `securityinabox.org`) rather than just the site name to avoid potentially malicious search results
- **Configure autocomplete** to limit suggestions from browsing history

### Configuration

**Firefox:**
- [Control address bar suggestions](https://support.mozilla.org/kb/address-bar-autocomplete-firefox#w_how-can-i-control-what-results-the-address-bar-shows-me)
- [Remove autocomplete results](https://support.mozilla.org/kb/address-bar-autocomplete-firefox#w_removing-autocomplete-results)
- [Disable search suggestions](https://support.mozilla.org/en-US/kb/search-suggestions-firefox#w_enabling-or-disabling-search-suggestions)

---

## Set Your Default Search Engine

Search engines like Google and Bing build profiles of users, track devices, and share personal information with third parties.

### Privacy-Focused Alternatives

Choose a search engine that doesn't track you:
- [DuckDuckGo](https://duckduckgo.com/)
- [Startpage](https://www.startpage.com/)
- [Ecosia](https://www.ecosia.org/)

Configure your default search engine in your browser settings.

---

## Review Site Permissions

Websites may request access to your camera, microphone, location, and other sensitive features. Review and restrict these permissions in your browser settings.

---

## Secure Your Connections

### Enable HTTPS-Only Mode

The "S" in HTTPS stands for "secure." HTTPS encrypts data between your device and the website, protecting sensitive information from eavesdroppers.

**Actions:**
1. Activate HTTPS-Only mode in your browser settings
2. Verify addresses begin with `https://` (not just `http://`)

---

## Enable Tracking Protection

When you browse, cookies and trackers collect details about your identity, location, and online activity.

### Configuration Steps

**Firefox:**
- [Set Enhanced Tracking Protection to Standard or Strict](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop#w_adjust-your-global-enhanced-tracking-protection-settings)

**Chrome/Chromium:**
- [Enable Tracking Protection](https://support.google.com/chrome/answer/95647?sjid=10772239645414681785-EU#tracking_protection)
- [Set Safe Browsing to Enhanced protection](https://support.google.com/chrome/answer/9890866?hl=en&co=GENIE.Platform%3DDesktop&sjid=10772239645414681785-EU&oco=0#zippy=%2Cenhanced-protection)

**Additional Steps:**
- Configure your browser to delete data when you end sessions
- If a website breaks, disable tracking protection temporarily for that specific site only

---

## Disable the Built-in Password Manager

Browser-based password managers are convenient but put you at greater risk of attackers tricking your browser into revealing passwords.

**Recommended Actions:**
1. Remove all saved logins from your browser
2. Disable the built-in password manager
3. Use a dedicated password manager like [KeePassXC](https://securityinabox.org/en/passwords/password-managers/#use-a-password-manager-installed-in-your-device)

If you must use browser-based password storage, avoid it for highly sensitive accounts and follow [these recommendations](https://securityinabox.org/en/passwords/password-managers/#if-you-decide-to-store-some-passwords-in-your-browser-or-email-client).

---

## Use Protective Browser Extensions

Extensions can significantly enhance your security and privacy, but only install those you trust from official sources.

### Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| **Privacy Badger** | Prevents tracking and metadata collection |
| **uBlock Origin** | Blocks advertising and trackers (some malicious) |
| **Facebook Container** (Firefox) | Prevents Facebook from tracking your web activity |
| **Zoom Redirector** | Opens Zoom links in browser for added protection |
| **NoScript** | Blocks potentially malicious scripts from unknown websites |

> **Note:** NoScript may cause websites to appear broken. [Learn to configure NoScript](https://noscript.net/features) to minimize issues.

### Trusted Sources
- [Mozilla Add-ons for Firefox](https://addons.mozilla.org/en-US/firefox/)
- [Chrome Web Store](https://chromewebstore.google.com/category/extensions)

Read [Mozilla's tips for assessing extension safety](https://support.mozilla.org/en-US/kb/tips-assessing-safety-extension) before installing from other sources.

---

## Manage Extensions and Pop-ups

- **Remove** all extensions you don't use or recognize
- **Enable** pop-up blocking in your browser settings

Extensions can be malicious and used for surveillance. Only keep what you actively need and trust.

---

## Delete Your Browsing History

By default, browsers remember your browsing, download, form, and search histories. Regularly clear this data or configure automatic deletion.

---

## Use Private Browsing Mode

Private browsing (Firefox) or Incognito mode (Chrome) prevents the browser from saving cookies and history for that session.

### Limitations

Private browsing does **NOT**:
- Change your IP address
- Prevent traces on the device
- Protect against malware surveillance

[Learn more about private browsing limitations](https://support.mozilla.org/kb/common-myths-about-private-browsing)

### How to Enable

- **Firefox:** [Open private window](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history#w_how-do-i-open-a-new-private-window) | [Always use private browsing](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history#w_can-i-set-firefox-to-always-use-private-browsing)
- **Chrome/Chromium:** [Browse in Incognito mode](https://support.google.com/chrome/answer/95464)

For protection against malware and surveillance, see the guides on [malware](https://securityinabox.org/en/phones-and-computers/malware/) and [anonymity](https://securityinabox.org/en/internet-connection/anonymity).

---

## Control Startup and Homepage Settings

If others may access your browser, disable features that reveal your browsing habits:
- Turn off "restore previous session" on startup
- Disable "most visited sites" suggestions

---

## Recognize and Report Malicious Websites

Modern browsers warn you about phishing, malware, and social engineering sites. If you see a warning, don't visit that website.

### Learn More
- [Firefox Phishing and Malware Protection](https://support.mozilla.org/en-US/kb/how-does-phishing-and-malware-protection-work)
- [Chrome warnings about unsafe sites](https://support.google.com/chrome/answer/99020?hl=en&co=GENIE.Platform%3DDesktop)

### Report Suspicious Sites
[Report to Google Safe Browsing](https://developers.google.com/search/help/report-quality-issues) to help improve protection for everyone.

---

*Last updated: 12 September 2024*