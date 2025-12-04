```yaml
---
title: "Browse the Web More Securely"
tags: [browser-security, privacy, web-browsing, firefox, tracking-protection, digital-security]
category: "Internet Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Browser Configuration", "Privacy Protection", "Web Security"]
summary: "Comprehensive guide to choosing secure browsers and configuring them for enhanced privacy and security protection."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Familiarity with web browsers"]
estimated_read_time: "15 minutes"
related_guides: ["malware-protection", "anonymity-tools", "password-managers"]
---
```

# Browse the Web More Securely

A web browser is one of the digital tools most of us use daily. It is the main way many people access the internet. Because we rely so much on browsers, they are often targets for people who want to compromise your privacy or security. Follow the steps below to choose a more secure browser and strengthen its protection.

## Table of Contents

- [Choose a Web Browser](#choose-a-web-browser)
- [Change Your Default Browser](#change-your-default-browser)
- [Keep Your Browser Updated](#keep-your-browser-updated)
- [Use the Address Bar Properly](#use-the-address-bar-properly)
- [Set a Privacy-Focused Search Engine](#set-a-privacy-focused-search-engine)
- [Review Site Permissions](#review-site-permissions)
- [Secure Your Connections with HTTPS](#secure-your-connections-with-https)
- [Enable Tracking Protection](#enable-tracking-protection)
- [Disable the Built-in Password Manager](#disable-the-built-in-password-manager)
- [Install Protective Browser Extensions](#install-protective-browser-extensions)
- [Remove Unwanted Extensions](#remove-unwanted-extensions)
- [Delete Your Browsing History](#delete-your-browsing-history)
- [Use Private Browsing Mode](#use-private-browsing-mode)
- [Configure Startup Settings](#configure-startup-settings)
- [Recognize and Report Malicious Websites](#recognize-and-report-malicious-websites)

---

## Choose a Web Browser

Most operating systems come with pre-installed browsers like Safari (macOS/iOS) or Edge (Windows). These browsers are not designed with a primary focus on privacy and security. We recommend using more security-oriented alternatives.

### Recommended Browsers

| Browser | Platform | Key Features |
|---------|----------|--------------|
| **[Firefox](https://www.mozilla.org/en-US/firefox/all/)** | Windows, macOS, Linux, Android, iOS | Free, open-source, strong built-in security |
| **[Chromium](https://www.chromium.org/)** | Windows, macOS, Linux, Android | Free, open-source alternative to Chrome |
| **[DuckDuckGo Privacy Browser](https://duckduckgo.com/duckduckgo-help-pages/get-duckduckgo/browser/)** | Windows, macOS, iOS, Android | Auto-blocks trackers, upgrades to HTTPS |
| **[Tor Browser](https://www.torproject.org/download/)** | Windows, macOS, Linux, Android | Maximum anonymity through Tor network |

> **Tip:** Consider installing two browsers—one for sensitive activities and another for everyday browsing. This helps compartmentalize your online identity.

### Why These Recommendations?

- **Firefox** is free, open-source software with better built-in security than most browsers
- **Chrome/Chromium** offer high-quality security, though Chrome may send more data to Google than you're comfortable with
- **DuckDuckGo Privacy Browser** automatically blocks web trackers and upgrades insecure connections
- **Tor Browser** anonymizes your connections but significantly changes your browsing experience

> **Android Users:** Install secure browsers through [FFUpdater](https://github.com/Tobi823/ffupdater), a free and open-source installer available on [F-Droid](https://f-droid.org/en/packages/de.marmaro.krt.ffupdater/).

---

## Change Your Default Browser

By setting a privacy-focused browser as your default, links you click in other apps will open directly in a more secure browser.

### How to Change Your Default Browser

- **Firefox:** Follow [Mozilla's guide](https://support.mozilla.org/en-US/kb/make-firefox-your-default-browser) for Linux, macOS, and Windows
- **Chrome:** Instructions for [Windows/macOS](https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop) and [iOS](https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DiOS&oco=0)
- **Ubuntu:** [Change default browser settings](https://help.ubuntu.com/stable/ubuntu-help/net-default-browser.html)
- **Windows:** [Stop Edge from starting automatically](https://support.microsoft.com/microsoft-edge/stop-microsoft-edge-from-starting-automatically-c341c879-799a-dccd-d6be-bc51ecdd5804)

> **Important:** Deactivate or uninstall browsers you don't use. If using Chrome, avoid logging in with your Google account.

---

## Keep Your Browser Updated

Browser updates often contain critical security patches. Ensure automatic updates are enabled and periodically verify you have the latest version.

- **Firefox:** [Check for updates](https://support.mozilla.org/kb/update-firefox-latest-release)
- **Chrome/Chromium:** [Update Chrome](https://www.google.com/chrome/update/)
- **Tor Browser:** [Configure automatic updates](https://tb-manual.torproject.org/updating/)

---

## Use the Address Bar Properly

The address bar displays the URL of your current page and can be used to navigate directly to websites.

### Best Practices

- **Type complete addresses** (e.g., `securityinabox.org`) rather than just website names to avoid potentially malicious search results
- **Disable unwanted suggestions** from browsing history

### Configuration

**Firefox:**
- [Control address bar suggestions](https://support.mozilla.org/kb/address-bar-autocomplete-firefox#w_how-can-i-control-what-results-the-address-bar-shows-me)
- [Remove autocomplete results](https://support.mozilla.org/kb/address-bar-autocomplete-firefox#w_removing-autocomplete-results)
- [Disable search suggestions](https://support.mozilla.org/en-US/kb/search-suggestions-firefox#w_enabling-or-disabling-search-suggestions)

---

## Set a Privacy-Focused Search Engine

Search engines like Google and Bing build profiles of users and share personal information with third parties. Choose a search engine that doesn't track you:

- **[DuckDuckGo](https://duckduckgo.com/)** — No tracking, no profiling
- **[Startpage](https://www.startpage.com/)** — Google results without tracking
- **[Ecosia](https://www.ecosia.org/)** — Privacy-focused with environmental mission

Configure your default search engine in your browser settings to use one of these alternatives.

---

## Review Site Permissions

Websites may request access to your camera, microphone, location, and other sensitive features. Regularly review and restrict these permissions in your browser settings.

- **Firefox:** Settings → Privacy & Security → Permissions
- **Chrome/Chromium:** Settings → Privacy and security → Site Settings

---

## Secure Your Connections with HTTPS

HTTPS encrypts data between your device and websites, protecting sensitive information from surveillance.

### Enable HTTPS-Only Mode

Always verify that website addresses begin with `https://` (not just `http://`). Enable HTTPS-Only mode in your browser to automatically upgrade connections when possible.

> **What does the "S" mean?** The S in HTTPS stands for "secure." This protocol encrypts what you're viewing as it travels between your device and the website.

---

## Enable Tracking Protection

When you browse the web, cookies and trackers gather details about who you are, where you are, and what you've viewed online.

### Configuration Steps

**Firefox:**
- [Set Enhanced Tracking Protection to Standard or Strict](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop#w_adjust-your-global-enhanced-tracking-protection-settings)

**Chrome/Chromium:**
- [Enable Tracking Protection](https://support.google.com/chrome/answer/95647?sjid=10772239645414681785-EU#tracking_protection)
- [Set Safe Browsing to Enhanced protection](https://support.google.com/chrome/answer/9890866?hl=en&co=GENIE.Platform%3DDesktop&sjid=10772239645414681785-EU&oco=0#zippy=%2Cenhanced-protection)

### Additional Recommendations

- Configure your browser to delete data when you end your browsing session
- If a website doesn't work correctly with enhanced protection, disable it temporarily for that specific site only

---

## Disable the Built-in Password Manager

Most browsers can save passwords, but browser-based password managers put you at greater risk of attackers tricking your browser into revealing your credentials.

### Recommended Action

1. Remove all saved logins from your browser
2. Disable the password manager feature
3. Use a dedicated password manager like [KeePassXC](https://securityinabox.org/en/passwords/password-managers/#use-a-password-manager-installed-in-your-device) instead

> **If you must use browser password storage:** Avoid storing passwords for highly sensitive accounts and follow [best practices for browser password protection](https://securityinabox.org/en/passwords/password-managers/#if-you-decide-to-store-some-passwords-in-your-browser-or-email-client).

---

## Install Protective Browser Extensions

When you browse the web, you encounter code from unknown sources—this is why most malware infections originate from web pages.

### Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| **[Privacy Badger](https://privacybadger.org/)** | Prevents tracking and metadata collection |
| **[uBlock Origin](https://ublockorigin.com/)** | Blocks advertising and potentially malicious trackers |
| **[Facebook Container](https://addons.mozilla.org/en-US/firefox/addon/facebook-container/)** (Firefox) | Prevents Facebook from tracking your activity across the web |
| **[Zoom Redirector](https://addons.mozilla.org/en-US/firefox/addon/zoom-redirector/)** | Keeps Zoom calls within browser protections |
| **[NoScript](https://noscript.net/)** | Blocks potentially malicious scripts (advanced users) |

> **Note:** NoScript may cause websites to appear broken. [Learn to configure it properly](https://noscript.net/features).

### Extension Safety

- Only install extensions from trusted sources like the [Mozilla Add-ons repository](https://addons.mozilla.org/en-US/firefox/) or [Chrome Web Store](https://chromewebstore.google.com/category/extensions)
- Read [Mozilla's tips for assessing extension safety](https://support.mozilla.org/en-US/kb/tips-assessing-safety-extension) before installing from other sources

---

## Remove Unwanted Extensions

Extensions can be malicious and used to spy on you like any other software.

### Best Practices

- Remove all extensions you don't use or recognize
- Ensure your browser blocks pop-ups (a common malware delivery method)
- Regularly audit your installed extensions

---

## Delete Your Browsing History

Your browsing history is a list of websites you've visited. By default, browsers remember your browsing, download, form, and search histories.

Regularly clear this data or configure your browser to delete it automatically when closing.

- **Firefox:** [Clear browsing history](https://support.mozilla.org/kb/delete-browsing-search-download-history-firefox)
- **Chrome/Chromium:** Settings → Privacy and security → Clear browsing data

---

## Use Private Browsing Mode

Private browsing (Firefox) or Incognito mode (Chrome) prevents your browser from saving cookies or history for that session.

### What Private Browsing Does NOT Protect

- Your IP address remains visible to websites
- Traces may remain on your device
- Malware on your computer can still monitor activity

### How to Enable

- **Firefox:** [Open private browsing](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history#w_how-do-i-open-a-new-private-window) or [enable it permanently](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history#w_can-i-set-firefox-to-always-use-private-browsing)
- **Chrome/Chromium:** [Browse in Incognito mode](https://support.google.com/chrome/answer/95464)

> **Important:** Private browsing is useful for hiding activity from someone with physical access to your device, but it won't protect you from malware or network surveillance.

---

## Configure Startup Settings

If you're concerned about others accessing your browser, disable features that reveal your browsing habits.

### Recommended Settings

- Don't restore previous session tabs on startup
- Disable "most visited sites" suggestions on new tabs

Configure these options in your browser's settings under Startup or Home page preferences.

---

## Recognize and Report Malicious Websites

Modern browsers can detect and warn you about malicious websites. If you see a warning, avoid visiting that site.

### Learn More

- **Firefox:** [Phishing and Malware Protection](https://support.mozilla.org/en-US/kb/how-does-phishing-and-malware-protection-work)
- **Chrome/Chromium:** [Warnings about unsafe sites](https://support.google.com/chrome/answer/99020?hl=en&co=GENIE.Platform%3DDesktop)

### Report Suspicious Sites

If you encounter a malicious website without receiving a warning, [report it to Google Safe Browsing](https://developers.google.com/search/help/report-quality-issues) to help protect others.

---

## Additional Resources

- [Malware Protection Guide](https://securityinabox.org/en/phones-and-computers/malware/)
- [Anonymity Tools Guide](https://securityinabox.org/en/internet-connection/anonymity)
- [Password Manager Guide](https://securityinabox.org/en/passwords/password-managers/)
- [Multiple Identity Management](https://securityinabox.org/en/communication/multiple-identities/)

---

*Last updated: 12 September 2024*
*Source: [Security in a Box](https://securityinabox.org/en/internet-connection/safer-browsing/)*