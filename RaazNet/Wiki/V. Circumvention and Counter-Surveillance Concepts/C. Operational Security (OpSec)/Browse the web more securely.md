```yaml
---
title: "Browse the Web More Securely"
tags: [browser-security, privacy, web-browsing, digital-security, tracking-protection]
category: "Internet Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Browser Configuration", "Privacy Protection", "Web Security"]
summary: "Comprehensive guide to choosing, configuring, and using web browsers securely to protect your privacy and security online."
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

## Choose a Web Browser

Most operating systems come with pre-installed browsers like Safari (macOS/iOS) or Edge (Windows). These browsers are not designed with a primary focus on privacy and security. We strongly recommend using more security and privacy-oriented software as your default browser.

### Recommended Browsers

- **[Firefox](https://www.mozilla.org/en-US/firefox/all/)** - Free, open-source, with better built-in security. Available for Windows, macOS, Linux, Android, and iOS.
- **[Chromium](https://www.chromium.org/)** - Free, open-source alternative to Chrome. On Linux, install through your software installer. On Android, install via [FFUpdater](https://f-droid.org/en/packages/de.marmaro.krt.ffupdater/).
- **[Chrome](https://support.google.com/chrome/answer/95346)** - High-quality security, but consider that it may send data to Google. Avoid logging into your Google account when using it.
- **[DuckDuckGo Privacy Browser](https://duckduckgo.com/duckduckgo-help-pages/get-duckduckgo/browser/)** - Automatically blocks web trackers and upgrades HTTP connections to HTTPS.
- **[Tor Browser](https://www.torproject.org/download/)** - For advanced privacy and accessing blocked websites. Read more in the [guide on anonymization tools](https://securityinabox.org/en/internet-connection/anonymity).

> **Tip:** Consider installing more than one browser—use one for sensitive activities and another for everyday browsing. See the [guide on multiple identity management](https://securityinabox.org/en/communication/multiple-identities/#different-devices).

## Change Your Default Browser

Setting a privacy-focused browser as your default ensures that links you click in other apps open in a more secure browser.

- [Make Firefox your default browser](https://support.mozilla.org/en-US/kb/make-firefox-your-default-browser) (Linux, macOS, Windows)
- [Make Chrome your default browser](https://support.google.com/chrome/answer/95417) (Windows, macOS, iOS)
- [Change default browser on Ubuntu](https://help.ubuntu.com/stable/ubuntu-help/net-default-browser.html)
- [Stop Edge from auto-starting on Windows](https://support.microsoft.com/microsoft-edge/stop-microsoft-edge-from-starting-automatically-c341c879-799a-dccd-d6be-bc51ecdd5804)

Deactivate or uninstall browsers you don't use.

## Keep Your Browser Updated

Browsers update automatically, but periodically verify you have the latest version:

- [Check Firefox updates](https://support.mozilla.org/kb/update-firefox-latest-release)
- [Update Chrome](https://www.google.com/chrome/update/)
- [Update Tor Browser](https://tb-manual.torproject.org/updating/)

## Use the Address Bar Correctly

If you know a website's complete address (e.g., `securityinabox.org`), type it directly in the address bar rather than searching for it. Typing just the site name without the extension (`.org`) opens your search engine, which may show malicious results.

### Configure Address Bar Settings

**Firefox:**
- [Control address bar suggestions](https://support.mozilla.org/kb/address-bar-autocomplete-firefox#w_how-can-i-control-what-results-the-address-bar-shows-me)
- [Remove autocomplete results](https://support.mozilla.org/kb/address-bar-autocomplete-firefox#w_removing-autocomplete-results)
- [Disable search suggestions](https://support.mozilla.org/en-US/kb/search-suggestions-firefox#w_enabling-or-disabling-search-suggestions)

## Set a Privacy-Friendly Default Search Engine

Search engines like Google and Bing build profiles of users and share personal information with third parties. Choose a search engine that doesn't track you:

- **[DuckDuckGo](https://duckduckgo.com/)** - No tracking, no profiling
- **[Startpage](https://www.startpage.com/)** - Google results without tracking
- **[Ecosia](https://www.ecosia.org/)** - Plants trees with ad revenue, privacy-focused

## Review Site Permissions

Check which websites have access to your camera, microphone, location, and notifications. Remove permissions from sites that don't need them.

## Secure Your Connections with HTTPS

HTTPS encrypts data between your device and websites, protecting sensitive information from eavesdroppers.

- **Activate HTTPS-Only mode** in your browser settings
- **Verify addresses** begin with `https://`, not just `http://`

## Enable Tracking Protection

Enable strict privacy protection to prevent third-party tracking:

**Firefox:**
- [Set Enhanced Tracking Protection to Standard or Strict](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop#w_adjust-your-global-enhanced-tracking-protection-settings)

**Chrome/Chromium:**
- [Enable Tracking Protection](https://support.google.com/chrome/answer/95647#tracking_protection)
- [Set Safe Browsing to Enhanced protection](https://support.google.com/chrome/answer/9890866)

Configure your browser to delete data when you close it. If a site doesn't work correctly, you can temporarily disable tracking protection for that specific site.

## Turn Off the Built-in Password Manager

Browser password managers put you at greater risk of attackers tricking your browser into revealing passwords.

- Remove all saved logins from your browser
- Disable the built-in password manager
- Use a dedicated password manager like [KeePassXC](https://securityinabox.org/en/passwords/password-managers/#use-a-password-manager-installed-in-your-device) instead

If you must use browser password storage, avoid storing passwords for highly sensitive accounts.

## Install Protective Browser Extensions

Choose extensions based on your circumstances. On shared or managed devices, you may need to reconfigure these regularly.

### Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| **Privacy Badger** | Prevents tracking and metadata collection |
| **uBlock Origin** | Blocks advertising and trackers (some may be malicious) |
| **Facebook Container** (Firefox) | Prevents Facebook from tracking your browsing |
| **Zoom Redirector** | Opens Zoom links in browser for added protection |
| **NoScript** (Advanced) | Blocks code from unknown websites to prevent infection |

> **Note:** NoScript may cause websites to appear broken. [Learn to configure NoScript](https://noscript.net/features) to minimize this.

## Remove Unwanted Extensions and Block Pop-ups

- Remove extensions you don't use or recognize
- Ensure pop-up blocking is enabled
- Only install extensions from trusted sources:
  - [Mozilla Add-ons](https://addons.mozilla.org/en-US/firefox/)
  - [Chrome Web Store](https://chromewebstore.google.com/category/extensions)

Read [Mozilla's tips for assessing extension safety](https://support.mozilla.org/en-US/kb/tips-assessing-safety-extension) before installing from other sources.

## Delete Your Browsing History

Your browsing history includes websites visited, downloads, and form data. Regularly clear this data or configure automatic deletion.

## Use Private Browsing or Incognito Mode

Private browsing prevents your browser from saving history, cookies, and form data for that session.

**Important limitations—private browsing does NOT:**
- Hide your IP address
- Prevent traces on shared devices
- Protect against malware

**Firefox:**
- [Open a private window](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history#w_how-do-i-open-a-new-private-window)
- [Always use private browsing](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history#w_can-i-set-firefox-to-always-use-private-browsing)

**Chrome/Chromium:**
- [Browse in Incognito mode](https://support.google.com/chrome/answer/95464)

## Hide Recently Viewed Sites

If others may access your browser, disable features that show recently visited pages or tabs from your last session.

## Recognize and Report Malicious Websites

Modern browsers warn you about phishing, malware, and social engineering sites. If you see a warning, don't visit that site.

- [Firefox Phishing and Malware Protection](https://support.mozilla.org/en-US/kb/how-does-phishing-and-malware-protection-work)
- [Chrome unsafe site warnings](https://support.google.com/chrome/answer/99020)
- [Report to Google Safe Browsing](https://developers.google.com/search/help/report-quality-issues)

---

## Further Reading

- [Malware Protection Guide](https://securityinabox.org/en/phones-and-computers/malware/)
- [Anonymity Tools Guide](https://securityinabox.org/en/internet-connection/anonymity)
- [Password Managers Guide](https://securityinabox.org/en/passwords/password-managers/)