---
title: "How to Create Internet Accounts Privately"
tags: [privacy, security, account-management, authentication, email-aliases, oauth]
category: "Digital Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Security Beginners]
topics: ["Account Security", "Privacy Protection", "Authentication Methods"]
summary: "Guide to creating online accounts with privacy in mind, covering authentication methods, email aliases, and security considerations."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of passwords"]
estimated_read_time: "8 minutes"
---

# Account Creation

Often people sign up for services without thinking. Maybe it's a streaming service to watch that new show everyone's talking about, or an account that gives you a discount for your favorite fast food place. Whatever the case may be, you should consider the implications for your data now and later on down the line.

There are risks associated with every new service that you use. Data breaches, disclosure of customer information to third parties, and rogue employees accessing data are all possibilities that must be considered when giving your information out. You need to be confident that you can trust the service, which is why we don't recommend storing valuable data on anything but the most mature and battle-tested products. That usually means services which provide end-to-end encryption (E2EE) and have undergone a cryptographic audit.

It can also be difficult to delete accounts on some services. Sometimes overwriting data associated with an account is possible, but in other cases the service will keep an entire history of changes to the account.

## Terms of Service & Privacy Policy

The Terms of Service (ToS) are the rules that you agree to follow when using the service. With larger services, these rules are often enforced by automated systems that can make mistakes. For example, you may be banned or locked out of your account for using a VPN or VoIP number. Appealing such bans is often difficult and involves an automated process that isn't always successful. This is one reason we wouldn't suggest using Gmail for email—email is crucial for access to other services you might have signed up for.

The Privacy Policy explains how the service will use your data. A company or organization might not be legally obligated to follow everything contained in the policy, depending on the jurisdiction. We recommend understanding your local laws and what they permit a provider to collect.

**Key terms to look for:**
- "Data collection"
- "Data analysis"
- "Cookies"
- "Ads"
- "3rd-party" services

Sometimes you can opt out from data collection or sharing, but it's best to choose a service that respects your privacy from the start.

## Authentication Methods

There are usually multiple ways to sign up for an account, each with their own benefits and drawbacks.

### Email and Password

The most common way to create a new account is with an email address and password. When using this method, you should use a password manager and follow best practices regarding passwords.

> **Tip:** You can use your password manager to organize other authentication methods too! Add the new entry and fill the appropriate fields—you can add notes for things like security questions or backup keys.

You will be responsible for managing your login credentials. For added security, set up multi-factor authentication (MFA) on your accounts.

#### Email Aliases

If you don't want to give your real email address to a service, you can use an alias. Alias services allow you to generate new email addresses that forward all emails to your main address. This can help:

- **Prevent tracking** across services
- **Manage marketing emails** that come with the sign-up process (filter automatically based on alias)
- **Identify breaches**—if a service gets hacked, unique aliases help identify exactly which service was compromised

### Sign in with OAuth ("Sign in with...")

[Open Authorization (OAuth)](https://en.wikipedia.org/wiki/OAuth) is an authentication protocol that allows you to register for a service without sharing much information with the provider by using an existing account with another service instead.

When you sign in with OAuth, it opens a login page with your chosen provider, connecting your existing and new accounts. Your password won't be shared, but some basic information typically will (you can review it during the login request).

**Advantages:**
- **Security:** You don't have to trust the security practices of the service you're logging into—credentials are stored with the external OAuth provider
- **Ease-of-use:** Multiple accounts are managed by a single login

**Disadvantages:**
- **Privacy:** The OAuth provider will know the services you use
- **Centralization:** If your OAuth account is compromised or inaccessible, all connected accounts are affected

**Important considerations:**
- All services using OAuth will be as secure as your underlying OAuth provider's account
- If you want hardware key security but a service doesn't support it, you can secure your OAuth account with a hardware key instead
- OAuth often allows *bidirectional* data sharing—always read the permissions list carefully before granting access
- Malicious applications can abuse OAuth by hijacking your session—only use OAuth with services you trust

### Phone Number

We recommend avoiding services that require a phone number for sign up. A phone number can identify you across multiple services, and depending on data sharing agreements, this makes your usage easier to track—particularly if one service is breached, as phone numbers are often **not** encrypted.

**Practical considerations:**
- Some services allow VoIP numbers, but these often trigger fraud detection systems
- For international shopping, you may need a number for SMS/call verification
- Don't get locked out of important accounts by providing fake numbers

### Username and Password Only

Some services allow registration without an email address, requiring only a username and password. These services may provide increased anonymity when combined with a VPN or Tor.

> **Warning:** For these accounts, there will most likely be **no way to recover your account** if you forget your username or password.