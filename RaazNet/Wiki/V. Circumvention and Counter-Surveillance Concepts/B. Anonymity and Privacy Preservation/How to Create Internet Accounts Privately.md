---
title: "How to Create Internet Accounts Privately"
tags: [privacy, account-security, authentication, email-aliases, password-management, oauth]
category: "Digital Privacy"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users]
topics: ["Account Security", "Privacy Protection", "Authentication Methods"]
summary: "Guide to creating online accounts while minimizing data exposure and maintaining privacy through various authentication methods."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of passwords"]
estimated_read_time: "8 minutes"
---

# How to Create Internet Accounts Privately

Often people sign up for services without thinking. Maybe it's a streaming service to watch that new show everyone's talking about, or an account that gives you a discount for your favorite fast food place. Whatever the case may be, you should consider the implications for your data now and later on down the line.

There are risks associated with every new service that you use. Data breaches, disclosure of customer information to third parties, and rogue employees accessing data are all possibilities that must be considered when giving your information out. You need to be confident that you can trust the service, which is why we don't recommend storing valuable data on anything but the most mature and battle-tested products. That usually means services which provide end-to-end encryption (E2EE) and have undergone a cryptographic audit.

It can also be difficult to delete accounts on some services. Sometimes overwriting data associated with an account is possible, but in other cases the service will keep an entire history of changes to the account.

## Terms of Service & Privacy Policy

The Terms of Service (ToS) are the rules that you agree to follow when using the service. With larger services these rules are often enforced by automated systems. Sometimes these automated systems can make mistakes. For example, you may be banned or locked out of your account on some services for using a VPN or VoIP number. Appealing such bans is often difficult and involves an automated process that isn't always successful. This is one reason why we wouldn't suggest using Gmail for email—email is crucial for access to other services you might have signed up for.

The Privacy Policy describes how the service will use your data, and it is worth reading so that you understand how your data will be used. A company or organization might not be legally obligated to follow everything contained in the policy (it depends on the jurisdiction). We recommend having some idea what your local laws are and what they permit a provider to collect.

**Look for particular terms such as:**
- "data collection"
- "data analysis"
- "cookies"
- "ads"
- "3rd-party" services

Sometimes you will be able to opt out from data collection or from sharing your data, but it is best to choose a service that respects your privacy from the start.

Keep in mind you're also placing your trust in the company or organization to comply with their own privacy policy.

## Authentication Methods

There are usually multiple ways to sign up for an account, each with their own benefits and drawbacks.

### Email and Password

The most common way to create a new account is with an email address and password. When using this method, you should use a password manager and follow best practices regarding passwords.

> **Tip:** You can use your password manager to organize other authentication methods too! Just add the new entry and fill the appropriate fields—you can add notes for things like security questions or a backup key.

You will be responsible for managing your login credentials. For added security, you can set up multi-factor authentication (MFA) on your accounts.

#### Email Aliases

If you don't want to give your real email address to a service, you have the option to use an alias. Alias services allow you to generate new email addresses that forward all emails to your main address. This can help:

- **Prevent tracking across services**
- **Manage marketing emails** that sometimes come with the sign-up process (these can be filtered automatically based on the alias they are sent to)
- **Identify breached services**—if a service gets hacked, you might start receiving phishing or spam emails to the address you used to sign up; using unique aliases for each service helps identify exactly what service was compromised

### Sign in with OAuth ("Sign in with...")

[Open Authorization (OAuth)](https://en.wikipedia.org/wiki/OAuth) is an authentication protocol that allows you to register for a service without sharing much information with the service provider by using an existing account you have with another service instead. Whenever you see something along the lines of "Sign in with *provider name*" on a registration form, it's typically using OAuth.

When you sign in with OAuth, it will open a login page with the provider you choose, and your existing account and new account will be connected. Your password won't be shared, but some basic information typically will (you can review it during the login request). This process is needed every time you want to log in to the same account.

**Advantages:**
- **Security**: You don't have to trust the security practices of the service you're logging into when it comes to storing your login credentials because they are stored with the external OAuth provider. Common OAuth providers like Apple and Google typically follow the best security practices, continuously audit their authentication systems, and don't store credentials inappropriately (such as in plain text).
- **Ease-of-use**: Multiple accounts are managed by a single login.

**Disadvantages:**
- **Privacy**: The OAuth provider you log in with will know the services you use.
- **Centralization**: If the account you use for OAuth is compromised, or you aren't able to log in to it, all other accounts connected to it are affected.

OAuth can be especially useful in situations where you could benefit from deeper integration between services. We recommend limiting OAuth to only where you need it, and always protecting the main account with MFA.

All the services that use OAuth will be as secure as your underlying OAuth provider's account. For example, if you want to secure an account with a hardware key, but that service doesn't support hardware keys, you can secure the account you use with OAuth with a hardware key instead—now you essentially have hardware MFA on all your accounts. However, weak authentication on your OAuth provider account means that any account tied to that login will also be weak.

> **Warning:** There is an additional danger when using "Sign in with Google," "Facebook," or another service. The OAuth process typically allows for *bidirectional* data sharing. For example, logging in to a forum with your Twitter account could grant that forum access to do things on your Twitter account such as post, read your messages, or access other personal data. OAuth providers will typically present you with a list of things you are granting the external service access to—always read through that list and don't inadvertently grant the external service access to anything it doesn't require.

Malicious applications, particularly on mobile devices where the application has access to the WebView session used for logging in to the OAuth provider, can also abuse this process by hijacking your session with the OAuth provider and gaining access to your OAuth account. Using the "Sign in with" option should usually be considered a matter of convenience that you only use with services you trust to not be actively malicious.

### Phone Number

We recommend avoiding services that require a phone number for sign up. A phone number can identify you across multiple services, and depending on data sharing agreements this will make your usage easier to track—particularly if one of those services is breached, as the phone number is often **not** encrypted.

You should avoid giving out your real phone number if you can. Some services will allow the use of VoIP numbers, however these often trigger fraud detection systems, causing an account to be locked down, so we don't recommend that for important accounts.

In many cases you will need to provide a number that you can receive SMS or calls from, particularly when shopping internationally in case there is a problem with your order at border screening. It's common for services to use your number as a verification method—don't let yourself get locked out of an important account because you wanted to be clever and give a fake number!

### Username and Password Only

Some services allow you to register without using an email address and only require you to set a username and password. These services may provide increased anonymity when combined with a VPN or Tor. 

> **Important:** For these accounts there will most likely be **no way to recover your account** in the event you forget your username or password.