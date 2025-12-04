---
title: "Email Aliasing"
tags: [email, privacy, security, aliasing, identity-protection]
category: "Digital Security"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Security Practitioners]
topics: ["Email Privacy", "Identity Protection", "Digital Security"]
summary: "Guide to email aliasing services that protect your primary email address and enhance privacy when registering for online services."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic email usage", "Understanding of online account registration"]
estimated_read_time: "6 minutes"
---

# Email Aliasing

An **email aliasing service** allows you to easily generate a new email address for every website you register for. The email aliases you generate are then forwarded to an email address of your choosing, hiding both your "main" email address and the identity of your email provider.

Email aliasing can also act as a safeguard in case your email provider ever ceases operation. In that scenario, you can easily re-route your aliases to a new email address. In turn, however, you are placing trust in the aliasing service to continue functioning.

## Benefits of Email Aliasing

### Over Plus Addressing

True email aliasing is better than plus addressing commonly used and supported by many providers, which allows you to create aliases like `yourname+[anythinghere]@example.com`, because websites, advertisers, and tracking networks can trivially remove anything after the `+` sign.

Organizations like the [IAB](https://en.wikipedia.org/wiki/Interactive_Advertising_Bureau) require that advertisers normalize email addresses so that they can be correlated and tracked, regardless of users' privacy wishes.

### Over Catch-All Aliases

- Aliases can be turned on and off individually when you need them, preventing websites from emailing you randomly
- Replies are sent from the alias address, shielding your real email address

### Over Temporary Email Services

- Aliases are permanent and can be turned on again if you need to receive something like a password reset
- Emails are sent to your trusted mailbox rather than stored by the alias provider
- Temporary email services typically have public mailboxes which can be accessed by anyone who knows the address, while aliases are private to you

## Recommended Providers

Using an aliasing service requires trusting both your email provider and your aliasing provider with your unencrypted messages. Some providers mitigate this slightly with **automatic PGP encryption**, which reduces the number of parties you need to trust from two to one by encrypting incoming emails before they are delivered to your final mailbox provider.

### Addy.io

**Addy.io** lets you create 10 domain aliases on a shared domain for free, or unlimited "standard" aliases.

**Free Plan Features:**
- 10 Shared Aliases
- Unlimited Standard Aliases
- No Outgoing Replies
- 1 Recipient Mailbox
- Automatic PGP Encryption

**Key Details:**
- Standard aliases end in `@[username].addy.io` or a custom domain on paid plans
- Payment options include cryptocurrency and voucher codes from ProxyStore
- Securitum audited Addy.io in September 2023 with no significant vulnerabilities identified

**Note:** If you cancel a paid subscription, most paid features (including custom domains) will be deactivated after the billing cycle ends, and catch-all will be enabled if previously disabled.

**Links:** [Homepage](https://addy.io/) | [Privacy Policy](https://addy.io/privacy) | [Documentation](https://addy.io/faq)

### SimpleLogin

**SimpleLogin** is a free service which provides email aliases on a variety of shared domain names, and optionally provides paid features like unlimited aliases and custom domains.

**Free Plan Features:**
- 10 Shared Aliases
- Unlimited Replies
- 1 Recipient Mailbox
- Automatic PGP Encryption (paid plans only)

**Key Details:**
- Acquired by Proton AG in April 2022
- If you use Proton Mail, SimpleLogin integrates seamlessly with your account
- Proton Pass Plus, Proton Unlimited, or multi-user Proton plans include SimpleLogin Premium
- Anonymous purchase available via ProxyStore voucher codes
- Securitum audited SimpleLogin in early 2022 with all issues addressed

**Note:** When your subscription ends, existing aliases continue to work, but you cannot create new aliases beyond the free plan limit or add new domains, directories, or mailboxes.

**Links:** [Homepage](https://simplelogin.io/) | [Privacy Policy](https://simplelogin.io/privacy) | [Documentation](https://simplelogin.io/docs)

## Choosing a Provider

When selecting an email aliasing service, consider:

1. **Trust requirements** - You're trusting the aliasing provider with your email content
2. **PGP encryption support** - Reduces trust requirements by encrypting before forwarding
3. **Integration** - SimpleLogin integrates well with Proton ecosystem
4. **Pricing and payment options** - Both offer cryptocurrency and anonymous payment methods
5. **Security audits** - Both providers have undergone independent security audits

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/email-aliasing/)*