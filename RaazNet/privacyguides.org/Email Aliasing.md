---
title: "Email Aliasing"
tags:
  [
    "email",
    "aliasing",
    "account-security",
    "tracking-protection",
    "tool-recommendations",
  ]
category: "Tool Recommendations"
difficulty: "intermediate"
audience: ["individuals", "power-users", "privacy-enthusiasts"]
topics:
  [
    "email-privacy",
    "aliasing-services",
    "account-compartmentalization",
    "threat-mitigation",
  ]
summary: "Explains how dedicated email aliasing services improve privacy and reduce tracking, and recommends trustworthy providers."
source: "Privacy Guides"
content_type: "guide"
security_level: "medium"
language: "en"
prerequisites:
  ["Basic understanding of email", "Familiarity with online accounts"]
estimated_read_time: 10
---

[Skip to content](https://www.privacyguides.org/en/email-aliasing/#benefits)

![](https://www.privacyguides.org/en/assets/img/cover/email-aliasing.webp)

# Email Aliasing

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/email-aliasing.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)
- [Public Exposure](https://www.privacyguides.org/en/basics/common-threats/#limiting-public-information)

An **email aliasing service** allows you to easily generate a new email address for every website you register for. The email aliases you generate are then forwarded to an email address of your choosing, hiding both your "main" email address and the identity of your [email provider](https://www.privacyguides.org/en/email/).

Email aliasing can also act as a safeguard in case your email provider ever ceases operation. In that scenario, you can easily re-route your aliases to a new email address. In turn, however, you are placing trust in the aliasing service to continue functioning.

## Benefits

Using a service which allows you to individually manage email aliases has a number of benefits over conventional mailbox management/filtering methods:

### Over Plus Addressing

True email aliasing is better than plus addressing commonly used and supported by many providers, which allows you to create aliases like `yourname+[anythinghere]@example.com`, because websites, advertisers, and tracking networks can trivially remove anything after the `+` sign. Organizations like the [IAB](https://en.wikipedia.org/wiki/Interactive_Advertising_Bureau) require that advertisers [normalize email addresses](https://shkspr.mobi/blog/2023/01/the-iab-loves-tracking-users-but-it-hates-users-tracking-them) so that they can be correlated and tracked, regardless of users' privacy wishes.

### Over Catch-All Aliases

Using a dedicated email aliasing service has a number of benefits over a catch-all alias on a custom domain:

- Aliases can be turned on and off individually when you need them, preventing websites from emailing you randomly.
- Replies are sent from the alias address, shielding your real email address.

### Over Temporary Email Services

Email aliasing services also have a number of benefits over "temporary email" services:

- Aliases are permanent and can be turned on again if you need to receive something like a password reset.
- Emails are sent to your trusted mailbox rather than stored by the alias provider.
- Temporary email services typically have public mailboxes which can be accessed by anyone who knows the address, while aliases are private to you.

## Recommended Providers

- ![Addy.io logo](https://www.privacyguides.org/en/assets/img/email-aliasing/addy.svg)[Addy.io](https://www.privacyguides.org/en/email-aliasing/#addyio)
- ![SimpleLogin logo](https://www.privacyguides.org/en/assets/img/email-aliasing/simplelogin.svg)[SimpleLogin](https://www.privacyguides.org/en/email-aliasing/#simplelogin)

Our email aliasing recommendations are providers that allow you to create aliases on domains they control, as well as on your own custom domain(s) for a modest yearly fee. They can also be self-hosted if you want maximum control. However, using a custom domain can have privacy-related drawbacks: If you are the only person using your custom domain, your actions can be easily tracked across websites simply by looking at the domain name in the email address and ignoring everything before the `@` symbol.

Using an aliasing service requires trusting both your email provider and your aliasing provider with your unencrypted messages. Some providers mitigate this slightly with automatic PGP encryption[1](https://www.privacyguides.org/en/email-aliasing/#fn:1), which reduces the number of parties you need to trust from two to one by encrypting incoming emails before they are delivered to your final mailbox provider.

### Addy.io

![Addy.io logo](https://www.privacyguides.org/en/assets/img/email-aliasing/addy.svg)

**Addy.io** lets you create 10 domain aliases on a shared domain for free, or unlimited ["standard" aliases](https://addy.io/faq/#what-is-a-standard-alias).

[Homepage](https://addy.io/) [Privacy Policy](https://addy.io/privacy "Privacy Policy") [Documentation](https://addy.io/faq "Documentation") [Source Code](https://github.com/anonaddy "Source Code") [Contribute](https://addy.io/donate "Contribute")

Downloads

- [Google Play](https://addy.io/faq/#is-there-an-android-app)
- [App Store](https://addy.io/faq/#is-there-an-ios-app)
- [Firefox](https://addons.mozilla.org/firefox/addon/addy_io)
- [Chrome](https://chrome.google.com/webstore/detail/iadbdpnoknmbdeolbapdackdcogdmjpe)

The number of shared aliases (which end in a shared domain like `@addy.io`) that you can create depends on the [plan](https://addy.io/#pricing) you are subscribed to. You can pay for these plans using [cryptocurrency](https://addy.io/help/subscribing-with-cryptocurrency) or purchase a voucher code from [ProxyStore](https://addy.io/help/voucher-codes), Addy.io's official reseller.

You can create unlimited standard aliases which end in a domain like `@[username].addy.io` or a custom domain on paid plans. However, as previously mentioned, this can be detrimental to privacy because people can trivially tie your standard aliases together based on the domain name alone. They are useful where a shared domain might be blocked by a service.

Securitum [audited](https://addy.io/blog/addy-io-passes-independent-security-audit) Addy.io in September 2023 and no significant vulnerabilities [were identified](https://addy.io/addy-io-security-audit.pdf).

Notable free features:

- 10 Shared Aliases
- Unlimited Standard Aliases
- No Outgoing Replies
- 1 Recipient Mailbox
- Automatic PGP Encryption[1](https://www.privacyguides.org/en/email-aliasing/#fn:1)

If you cancel your subscription, you will still enjoy the features of your paid plan until the billing cycle ends. After the end of your current billing cycle, most paid features (including any custom domains) will be [deactivated](https://addy.io/faq/#what-happens-if-i-have-a-subscription-but-then-cancel-it), paid account settings will be reverted to their defaults, and catch-all will be enabled if it was previously disabled.

### SimpleLogin

![SimpleLogin logo](https://www.privacyguides.org/en/assets/img/email-aliasing/simplelogin.svg)

**SimpleLogin** is a free service which provides email aliases on a variety of shared domain names, and optionally provides paid features like unlimited aliases and custom domains.

[Homepage](https://simplelogin.io/) [Privacy Policy](https://simplelogin.io/privacy "Privacy Policy") [Documentation](https://simplelogin.io/docs "Documentation") [Source Code](https://github.com/simple-login "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=io.simplelogin.android)
- [App Store](https://apps.apple.com/app/id1494359858)
- [GitHub](https://github.com/simple-login/Simple-Login-Android/releases)
- [Firefox](https://addons.mozilla.org/firefox/addon/simplelogin)
- [Chrome](https://chrome.google.com/webstore/detail/dphilobhebphkdjbpfohgikllaljmgbn)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/diacfpipniklenphgljfkmhinphjlfff)
- [Safari](https://apps.apple.com/app/id6475835429)

SimpleLogin was [acquired by Proton AG](https://proton.me/news/proton-and-simplelogin-join-forces) as of April 8, 2022. If you use Proton Mail for your primary mailbox, SimpleLogin is a great choice. As both products are now owned by the same company you now only have to trust a single entity. We also expect that SimpleLogin will be more tightly integrated with Proton's offerings in the future. SimpleLogin continues to support forwarding to any email provider of your choosing.

You can link your SimpleLogin account in the settings with your Proton account. If you have Proton Pass Plus, Proton Unlimited, or any multi-user Proton plan, you will have SimpleLogin Premium for free. You can also purchase a voucher code for SimpleLogin Premium anonymously via their official reseller [ProxyStore](https://simplelogin.io/faq).

Securitum [audited](https://simplelogin.io/blog/security-audit) SimpleLogin in early 2022 and all issues [were addressed](https://simplelogin.io/audit2022/web.pdf).

Notable free features:

- 10 Shared Aliases
- Unlimited Replies
- 1 Recipient Mailbox
- Automatic PGP Encryption[1](https://www.privacyguides.org/en/email-aliasing/#fn:1) is only available on paid plans

When your subscription ends, all aliases you created will still be able to receive and send emails. However, you cannot create any new aliases that would exceed the free plan limit, nor can you add a new domain, directory, or mailbox.

## Criteria

**Please note we are not affiliated with any of the providers we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we evaluate email aliasing providers to the same standard as our regular [email provider criteria](https://www.privacyguides.org/en/email/#criteria) where applicable. We suggest you familiarize yourself with this list before choosing an email aliasing service, and conduct your own research to ensure the provider you choose is the right choice for you.

---

1. Automatic PGP encryption allows you to encrypt non-encrypted incoming emails before they are forwarded to your mailbox, making sure your primary mailbox provider never sees unencrypted email content. a[ a](https://www.privacyguides.org/en/email-aliasing/#fnref:1) [ a](https://www.privacyguides.org/en/email-aliasing/#fnref2:1) [ a](https://www.privacyguides.org/en/email-aliasing/#fnref3:1)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
