---
title: "Email Clients"
tags: ["email", "clients", "openpgp", "tool-recommendations"]
category: "Tool Recommendations"
difficulty: "intermediate"
audience: ["individuals", "power-users", "organizations"]
topics: ["email-security", "pgp-support", "oauth", "account-security"]
summary: "Recommends privacy-respecting email clients which support encryption and strong authentication across platforms."
source: "Privacy Guides"
content_type: "guide"
security_level: "medium"
language: "en"
prerequisites:
  ["Basic knowledge of email use", "Interest in secure email configuration"]
estimated_read_time: 10
---

[Skip to content](https://www.privacyguides.org/en/email-clients/#cross-platform)

![](https://www.privacyguides.org/en/assets/img/cover/email-clients.webp)

# Email Clients

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/email-clients.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)
- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

The **email clients** we recommend support both [OpenPGP](https://www.privacyguides.org/en/encryption/#openpgp) and strong authentication such as [Open Authorization (OAuth)](https://www.privacyguides.org/en/basics/account-creation/#sign-in-with-oauth). OAuth allows you to use [Multi-Factor Authentication](https://www.privacyguides.org/en/basics/multi-factor-authentication/) to prevent account theft.

Email does not provide forward secrecy

When using end-to-end encryption (E2EE) technology like OpenPGP, email will still have [some metadata](https://www.privacyguides.org/en/basics/email-security/#email-metadata-overview) that is not encrypted in the header of the email.

OpenPGP also does not support [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy), which means if either your or the recipient's private key is ever stolen, all previous messages encrypted with it will be exposed: [How do I protect my private keys?](https://www.privacyguides.org/en/basics/email-security/) Consider using a medium that provides forward secrecy:

[Real-time Communication](https://www.privacyguides.org/en/real-time-communication/)

## Cross-Platform

### Thunderbird

![Thunderbird logo](https://www.privacyguides.org/en/assets/img/email-clients/thunderbird.svg)

**Thunderbird** is a free, open-source, cross-platform email, newsgroup, news feed, and chat (XMPP, IRC, Matrix) client developed by the Thunderbird community, and previously by the Mozilla Foundation.

[Homepage](https://thunderbird.net/) [Privacy Policy](https://mozilla.org/privacy/thunderbird "Privacy Policy") [Documentation](https://support.mozilla.org/products/thunderbird "Documentation") [Source Code](https://hg.mozilla.org/comm-central "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=net.thunderbird.android)
- [GitHub](https://github.com/thunderbird/thunderbird-android/releases)
- [Windows](https://thunderbird.net/)
- [macOS](https://thunderbird.net/)
- [Linux](https://thunderbird.net/)
- [Flathub](https://flathub.org/apps/details/org.mozilla.Thunderbird)

Warning

When replying to someone on a mailing list in Thunderbird Mobile, the "reply" option may also include the mailing list. For more information see [thunderbird/thunderbird-android #3738](https://github.com/thunderbird/thunderbird-android/issues/3738).

#### Recommended Configuration

We recommend changing some of these settings to make Thunderbird Desktop a little more private.

These options can be found in  
→ **Settings** → **Privacy & Security**.

##### Web Content

- Uncheck **Remember websites and links I've visited**
- Uncheck **Accept cookies from sites**

##### Telemetry

- Uncheck **Allow Thunderbird to send technical and interaction data to Mozilla**

#### Thunderbird-user.js (advanced)

[`thunderbird-user.js`](https://github.com/HorlogeSkynet/thunderbird-user.js) is a set of configuration options that aims to disable as many of the web-browsing features within Thunderbird Desktop as possible in order to reduce attack surface and maintain privacy. Some of the changes are backported from the [Arkenfox project](https://www.privacyguides.org/en/desktop-browsers/#arkenfox-advanced).

## Platform Specific

### Apple Mail (macOS)

![Apple Mail logo](https://www.privacyguides.org/en/assets/img/email-clients/applemail.png)

**Apple Mail** is included in macOS and can be extended to have OpenPGP support with [GPG Suite](https://www.privacyguides.org/en/encryption/#gpg-suite), which adds the ability to send PGP-encrypted email.

[Homepage](https://support.apple.com/guide/mail/welcome/mac) [Privacy Policy](https://apple.com/legal/privacy/en-ww "Privacy Policy") [Documentation](https://support.apple.com/mail "Documentation")

For those using macOS Sonoma

Currently, GPG Suite does [not yet](https://gpgtools.com/sonoma) have a stable release for macOS Sonoma.

Apple Mail has the ability to load remote content in the background or block it entirely and hide your IP address from senders on [macOS](https://support.apple.com/guide/mail/mlhl03be2866/mac) and [iOS](https://support.apple.com/guide/iphone/iphf084865c7/ios).

### FairEmail (Android)

![FairEmail logo](https://www.privacyguides.org/en/assets/img/email-clients/fairemail.svg)

**FairEmail** is a minimal, open-source email app which uses open standards (IMAP, SMTP, OpenPGP) and minimizes data and battery usage.

[Homepage](https://email.faircode.eu/) [Privacy Policy](https://github.com/M66B/FairEmail/blob/master/PRIVACY.md "Privacy Policy") [Documentation](https://github.com/M66B/FairEmail/blob/master/FAQ.md "Documentation") [Source Code](https://github.com/M66B/FairEmail "Source Code") [Contribute](https://email.faircode.eu/donate "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=eu.faircode.email)
- [GitHub](https://github.com/M66B/FairEmail/releases)

### GNOME Evolution (GNOME)

![Evolution logo](https://www.privacyguides.org/en/assets/img/email-clients/evolution.svg)

**Evolution** is a personal information management application that provides integrated mail, calendaring and address book functionality. Evolution has extensive [documentation](https://help.gnome.org/users/evolution/stable) to help you get started.

[Homepage](https://wiki.gnome.org/Apps/Evolution) [Privacy Policy](https://wiki.gnome.org/Apps/Evolution/PrivacyPolicy "Privacy Policy") [Documentation](https://help.gnome.org/users/evolution/stable "Documentation") [Source Code](https://gitlab.gnome.org/GNOME/evolution "Source Code") [Contribute](https://gnome.org/donate "Contribute")

Downloads

- [Flathub](https://flathub.org/apps/details/org.gnome.Evolution)

### Kontact (KDE)

![Kontact logo](https://www.privacyguides.org/en/assets/img/email-clients/kontact.svg)

**Kontact** is a personal information manager (PIM) application from the [KDE](https://kde.org/) project. It provides a mail client, address book, RSS client, and an organizer.

[Homepage](https://kontact.kde.org/) [Privacy Policy](https://kde.org/privacypolicy-apps "Privacy Policy") [Documentation](https://kontact.kde.org/users "Documentation") [Source Code](https://invent.kde.org/pim/kmail "Source Code") [Contribute](https://kde.org/community/donations "Contribute")

Downloads

- [Linux](https://kontact.kde.org/download)
- [Flathub](https://flathub.org/apps/details/org.kde.kontact)

### Mailvelope (Browser)

![Mailvelope logo](https://www.privacyguides.org/en/assets/img/email-clients/mailvelope.svg)

**Mailvelope** is a browser extension that enables the exchange of encrypted emails following the OpenPGP encryption standard.

[Homepage](https://mailvelope.com/) [Privacy Policy](https://mailvelope.com/privacy-policy "Privacy Policy") [Documentation](https://mailvelope.com/faq "Documentation") [Source Code](https://github.com/mailvelope/mailvelope "Source Code")

Downloads

- [Firefox](https://addons.mozilla.org/firefox/addon/mailvelope)
- [Chrome](https://chrome.google.com/webstore/detail/mailvelope/kajibbejlbohfaggdiogboambcijhkke)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/mailvelope/dgcbddhdhjppfdfjpciagmmibadmoapc)

### NeoMutt (CLI)

![NeoMutt logo](https://www.privacyguides.org/en/assets/img/email-clients/mutt.svg)

**NeoMutt** is an open-source command line email reader for Linux and BSD. It's a fork of [Mutt](<https://en.wikipedia.org/wiki/Mutt_(email_client)>) with added features.

NeoMutt is a text-based client that has a steep learning curve. It is, however, very customizable.

[Homepage](https://neomutt.org/) [Documentation](https://neomutt.org/guide "Documentation") [Source Code](https://github.com/neomutt/neomutt "Source Code") [Contribute](https://paypal.com/paypalme/russon "Contribute")

Downloads

- [macOS](https://neomutt.org/distro)
- [Linux](https://neomutt.org/distro)

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

### Minimum Qualifications

- Apps developed for open-source operating systems must be open source.
- Must not collect telemetry, or have an easy way to disable all telemetry.
- Must support OpenPGP message encryption.

### Best-Case

Our best-case criteria represents what we would like to see from the perfect project in this category. Our recommendations may not include any or all of this functionality, but those which do may rank higher than others on this page.

- Should be open source.
- Should be cross-platform.
- Should not collect any telemetry by default.
- Should support OpenPGP natively, i.e. without extensions.
- Should support storing OpenPGP encrypted emails locally.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
