```yaml
---
title: "Email Aliasing"
tags: [email, privacy, aliasing, security, identity-protection]
category: "Email Security"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users]
topics: ["Email Privacy", "Identity Protection", "Digital Security"]
summary: "Guide to email aliasing services that generate unique addresses for each website, protecting your main email and identity."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic email usage", "Understanding of email addresses"]
estimated_read_time: "6 minutes"
---
```

# Email Aliasing

An **email aliasing service** allows you to easily generate a new email address for every website you register for. The email aliases you generate are then forwarded to an email address of your choosing, hiding both your "main" email address and the identity of your email provider.

Email aliasing can also act as a safeguard in case your email provider ever ceases operation. In that scenario, you can easily re-route your aliases to a new email address. In turn, however, you are placing trust in the aliasing service to continue functioning.

## Benefits of Email Aliasing

### Over Plus Addressing

True email aliasing is better than plus addressing commonly used and supported by many providers, which allows you to create aliases like `yourname+[anythinghere]@example.com`, because websites, advertisers, and tracking networks can trivially remove anything after the `+` sign. Organizations like the [IAB](https://en.wikipedia.org/wiki/Interactive_Advertising_Bureau) require that advertisers normalize email addresses so that they can be correlated and tracked, regardless of users' privacy wishes.

### Over Catch-All Aliases

- Aliases can be turned on and off individually when you need them, preventing websites from emailing you randomly
- Replies are sent from the alias address, shielding your real email address

### Over Temporary Email Services

- Aliases are permanent and can be turned on again if you need to receive something like a password reset
- Emails are sent to your trusted mailbox rather than stored by the alias provider
- Temporary email services typically have public mailboxes which can be accessed by anyone who knows the address, while aliases are private to you

## Recommended Providers

> [!warning] Trust Considerations
> Using an aliasing service requires trusting both your email provider and your aliasing provider with your unencrypted messages. Some providers mitigate this with automatic PGP encryption, which reduces the number of parties you need to trust from two to one by encrypting incoming emails before they are delivered to your final mailbox provider.

### Addy.io

**Addy.io** lets you create 10 domain aliases on a shared domain for free, or unlimited "standard" aliases.

- **Website:** [addy.io](https://addy.io/)
- **Apps:** Android, iOS, Firefox, Chrome

**Free Plan Features:**
- 10 Shared Aliases
- Unlimited Standard Aliases
- No Outgoing Replies
- 1 Recipient Mailbox
- Automatic PGP Encryption

Standard aliases end in a domain like `@[username].addy.io` or a custom domain on paid plans. However, this can be detrimental to privacy because people can trivially tie your standard aliases together based on the domain name alone. They are useful where a shared domain might be blocked by a service.

Securitum audited Addy.io in September 2023 and no significant vulnerabilities were identified. Payment options include cryptocurrency and voucher codes from ProxyStore.

### SimpleLogin

**SimpleLogin** is a free service which provides email aliases on a variety of shared domain names, and optionally provides paid features like unlimited aliases and custom domains.

- **Website:** [simplelogin.io](https://simplelogin.io/)
- **Apps:** Android, iOS, Firefox, Chrome, Edge, Safari

**Free Plan Features:**
- 10 Shared Aliases
- Unlimited Replies
- 1 Recipient Mailbox
- Automatic PGP Encryption (paid plans only)

SimpleLogin was acquired by Proton AG in April 2022. If you use Proton Mail for your primary mailbox, SimpleLogin is a great choice. As both products are now owned by the same company, you only have to trust a single entity.

You can link your SimpleLogin account with your Proton account. If you have Proton Pass Plus, Proton Unlimited, or any multi-user Proton plan, you will have SimpleLogin Premium for free.

Securitum audited SimpleLogin in early 2022 and all issues were addressed.

## Selection Criteria

When choosing an email aliasing provider, consider:

- Number of free aliases available
- Support for custom domains
- Reply capabilities
- PGP encryption support
- Integration with your existing email provider
- Security audit history
- Privacy policy and data handling practices