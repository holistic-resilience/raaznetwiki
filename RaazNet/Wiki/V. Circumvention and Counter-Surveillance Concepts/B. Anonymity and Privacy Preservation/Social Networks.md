---
title: "Privacy-Respecting Social Networks"
tags: [privacy, social-media, decentralization, mastodon, matrix, fediverse, activitypub]
category: "Social Networks"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, General Public, Activists]
topics: ["Digital Privacy", "Decentralized Platforms", "Social Media Alternatives"]
summary: "Guide to privacy-respecting decentralized social networks including Mastodon and Matrix/Element, with recommended privacy settings."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of social media concepts"]
estimated_read_time: "12 minutes"
---

# Privacy-Respecting Social Networks

These privacy-respecting social networks allow you to participate in online communities without giving up personal information like your full name, phone number, and other data commonly requested by tech companies.

> [!warning] Not for Private Communications
> **No** social networks are appropriate for private or sensitive communications. For direct messaging, use a recommended instant messenger with strong end-to-end encryption. Only use social media direct messages to establish a more private and secure chat platform with your contacts.

## The Problem with Traditional Social Media

A growing problem among social media platforms is censorship in two forms:

1. **Government and Policy Censorship**: Platforms often acquiesce to illegitimate censorship requests from malicious governments or their own internal policies
2. **Access Walls**: They require accounts to access content that would otherwise be published freely on the open internet, effectively censoring privacy-conscious users who cannot pay the privacy cost of creating an account

The social networks recommended here solve these issues by:
- Operating on open, decentralized protocols
- Not requiring accounts to view publicly available content

## Understanding Decentralization

Decentralized social networks are built on an architecture fundamentally different from mainstream platforms, yet similar to email. Instead of opening an account under a single, unified service like Facebook or Discord, you choose an independent, public server to join. Your server can communicate with and discover other servers—this is known as *federation*.

### Benefits of Decentralization

- **No central authority** can censor your account across the entire network
- Greater choice in terms of service and moderation policies
- Community-driven governance

### Caveats to Consider

Each server is its own legal entity with its own:
- Privacy policy and terms of use
- Administration team and moderators
- Content policies (some more restrictive, some less)

While many servers are far *less* restrictive and more privacy-respecting than traditional platforms, some can be *more* restrictive or potentially *worse* for your privacy.

## Censorship Resistance Strategies

While network-level censorship doesn't exist in decentralized networks, server-level censorship is possible. Administrators can *defederate* from other servers, limiting content you can view and people you can interact with.

### Options for Maximum Control

1. **Self-host the software**: Gives you the same censorship resistance as any self-hosted website
2. **Use a managed hosting service**: Providers handle technical aspects while you control moderation. This is often better than self-hosting because you benefit from greater control without worrying about technical problems or unpatched security vulnerabilities

> [!tip] Choosing a Hosting Provider
> Review your hosting provider's terms of service and acceptable use policies before registering. These are often broader than typical server rules and less likely to be enforced with recourse, but can still be restrictive.

---

## Mastodon

**Mastodon** is a social network based on open web protocols and free, open-source software using the **ActivityPub** protocol.

- **Website**: [joinmastodon.org](https://joinmastodon.org/)
- **Documentation**: [docs.joinmastodon.org](https://docs.joinmastodon.org/)

### Why Mastodon?

1. **Strong Security Track Record**: Quick, coordinated patch releases for vulnerabilities with backports to older branches, plus built-in update notifications for administrators

2. **Versatile Content Support**: While primarily microblogging, it handles longer posts, images, videos, and content from other ActivityPub platforms—making it an ideal "central hub" for following anyone regardless of their platform

3. **Comprehensive Privacy Controls**: Many built-in features to limit data sharing, with new features developed with privacy in mind

### ActivityPub Interoperability

Many platforms use ActivityPub, meaning they can communicate across different software. For example, you can follow PeerTube video channels with a Mastodon account because both use ActivityPub.

### Choosing an Instance

- Choose a server aligned with the content you want to post or read
- **Avoid** *mastodon.social* and *mastodon.online*—they're operated by Mastodon's developers, which concentrates too much control
- Separating software developers from server hosts benefits long-term decentralization

### Recommended Privacy Settings

#### Public Profile Settings

| Setting | Recommendation | Reason |
|---------|---------------|--------|
| Automatically accept new followers | **Uncheck** | Enables private profile; review followers before accepting |
| Show follows and followers on profile | **Uncheck** | Hides your social graph from public view |
| Display from which app you sent a post | **Uncheck** | Prevents revealing your computing setup |

> [!note] Private Profiles Still Allow Public Posts
> With a private profile, you can still *choose* to publish publicly visible posts that non-followers can boost. Unchecking automatic follower acceptance gives you the *choice* between publishing to everyone or a select group.

#### Important Note on Privacy Controls

Settings like hiding your profile from search engines are **not** technical controls—they're requests. Nothing actually stops a search engine from reading your profile. The only effective way to hide posts is to:
1. Post with non-public (followers only) visibility
2. Limit who can follow your account

#### Preferences

Change your default posting visibility to prevent accidental over-sharing. You can always adjust visibility when composing individual posts.

#### Automated Post Deletion

- **Enable**: Automatically delete old posts
- **Default**: Delete posts after 2 weeks unless favorited (starred)

> [!tip] Why Delete Old Posts?
> Posts older than a few weeks are rarely read but can build a comprehensive profile about you over time. Publish ephemerally by default; keep posts longer only intentionally.

### Posting Visibility Levels

| Level | Description | Privacy Note |
|-------|-------------|--------------|
| **Public** | Anyone on the internet | Full exposure |
| **Quiet public** | Requests hiding from some feeds | Not a technical guarantee—treat as public |
| **Followers** | Only your followers | If you don't restrict followers, treat as public |
| **Specific people** | Only mentioned users | No E2EE—never rely on for private communications |

**Recommended default**: Post to **Followers** by default; use **Public** intentionally on a case-by-case basis.

---

## Element (Matrix)

**Element** is the flagship client for the **Matrix** protocol, an open standard enabling decentralized communication through federated chat rooms.

- **Website**: [element.io](https://element.io/)
- **Protocol Specification**: [spec.matrix.org](https://spec.matrix.org/latest)
- **Source Code**: [github.com/element-hq](https://github.com/element-hq)

### Platforms Available

- Web, Windows, macOS, Linux
- Android (Google Play, GitHub)
- iOS (App Store)

### Choosing a Homeserver

- Choose a homeserver aligned with your chat topics
- Third-party resources like [joinmatrix.org](https://servers.joinmatrix.org/) can help
- **Avoid** *matrix.org*—operated by Matrix's developers, concentrating too much control

### Recommended Privacy Settings

Access via **⚙ Settings → All settings**

#### Sessions

By default, session names reveal your Matrix client and platform. To prevent revealing device information:
- Empty the session name to display only the randomly generated Session ID

#### Preferences

| Setting | Recommendation |
|---------|---------------|
| Send read receipts | **Uncheck** |
| Send typing notifications | **Uncheck** |

This reduces metadata exposure when chatting in public rooms.

#### Voice & Video

| Setting | Recommendation | Reason |
|---------|---------------|--------|
| Allow Peer-to-Peer for 1:1 calls | **Uncheck** | Prevents IP address exposure |
| Allow fallback call assist server | **Uncheck** | Prevents IP address exposure |

#### Security & Privacy

**Integration Manager (scalar.vector.im)**
- Consider unchecking **Enable the integration manager** on public homeservers
- This doesn't affect visibility of bots or third-party services
- Review Element's [Integration Manager Privacy Notice](https://element.io/integration-manager-privacy-notice) for details

**Sessions**
- *Optional*: Uncheck **Record the client name, version, and url** (may make session management harder with multiple devices)

#### Encryption

- *Optional*: Check **In encrypted rooms, only send messages to verified users**

> [!warning] Verification Impact
> With this enabled, unverified users and unverified devices won't receive your messages in encrypted rooms. This may limit your interactions.

---

## Selection Criteria

These recommendations follow these requirements:

- **Open Source**: Must be free and open-source software
- **Federation**: Must use a federated protocol for inter-instance communication
- **No Arbitrary Restrictions**: Must not have non-technical restrictions on federation
- **Browser Access**: Must be usable in a standard web browser
- **Public Accessibility**: Must make public content accessible without an account
- **Privacy Controls**: Must allow limiting followers and posting to followers only
- **Modern Security**: Must support modern web security standards including multifactor authentication