[Skip to content](https://www.privacyguides.org/en/multi-factor-authentication/#ente-auth)

![](https://www.privacyguides.org/en/assets/img/cover/multi-factor-authentication.webp)

# Multifactor Authentication

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/multi-factor-authentication.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

Hardware Keys

[Hardware security key recommendations](https://www.privacyguides.org/en/security-keys/) have been moved to their own category.

**Multifactor Authentication Apps** implement a security standard adopted by the Internet Engineering Task Force (IETF) called **Time-based One-time Passwords**, or **TOTP**. This is a method where websites share a secret with you which is used by your authenticator app to generate a six (usually) digit code based on the current time, which you enter while logging in for the website to check. Typically, these codes are regenerated every 30 seconds, and once a new code is generated the old one becomes useless. Even if a hacker gets one six-digit code, there is no way for them to reverse that code to get the original secret or otherwise be able to predict what any future codes might be.

We highly recommend that you use mobile TOTP apps instead of desktop alternatives as Android and iOS have better security and app isolation than most desktop operating systems.

## Ente Auth

![Ente Auth logo](https://www.privacyguides.org/en/assets/img/multi-factor-authentication/ente-auth.svg)

**Ente Auth** is a free and open-source app which stores and generates TOTP tokens. It can be used with an online account to back up and sync your tokens across your devices (and access them via a web interface) in a secure, end-to-end encrypted fashion. It can also be used offline on a single device with no account necessary.

[Homepage](https://ente.io/auth) [Privacy Policy](https://ente.io/privacy "Privacy Policy") [Documentation](https://help.ente.io/auth "Documentation") [Source Code](https://github.com/ente-io/ente/tree/main/auth#readme "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=io.ente.auth)
- [App Store](https://apps.apple.com/app/id6444121398)
- [GitHub](https://github.com/ente-io/ente/releases?q=auth)
- [Web](https://auth.ente.io/)

## Aegis Authenticator (Android)

![Aegis logo](https://www.privacyguides.org/en/assets/img/multi-factor-authentication/aegis.png)

**Aegis Authenticator** is a free and open-source app for Android to manage your 2-step verification tokens for your online services. Aegis Authenticator operates completely offline/locally, but includes the option to export your tokens for backup unlike many alternatives.

[Homepage](https://getaegis.app/) [Privacy Policy](https://getaegis.app/aegis/privacy.html "Privacy Policy") [Documentation](https://github.com/beemdevelopment/Aegis/wiki "Documentation") [Source Code](https://github.com/beemdevelopment/Aegis "Source Code") [Contribute](https://buymeacoffee.com/beemdevelopment "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.beemdevelopment.aegis)
- [GitHub](https://github.com/beemdevelopment/Aegis/releases)

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

- Source code must be publicly available.
- Must not require internet connectivity.
- Cloud syncing must be optional, and (if available) sync functionality must be E2EE.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).