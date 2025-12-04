---
title: "Social Networks"
tags: [privacy, social-media, decentralization, mastodon, matrix, federation, activitypub]
category: "Social Networks"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Digital Rights Advocates]
topics: ["Social Media Privacy", "Decentralized Networks", "Federated Protocols"]
summary: "Guide to privacy-respecting social networks using decentralized protocols like ActivityPub and Matrix."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of social media", "Familiarity with account management"]
estimated_read_time: "12 minutes"
---

# Social Networks

These privacy-respecting **social networks** allow you to participate in online communities without giving up your personal information like your full name, phone number, and other data commonly requested by tech companies.

## The Problem with Mainstream Social Media

A growing problem among social media platforms is censorship in two forms:

1. **Government and policy-based censorship**: Platforms often acquiesce to illegitimate censorship requests from malicious governments or enforce restrictive internal policies
2. **Access restrictions**: Requiring accounts to access content that would otherwise be freely available—effectively censoring privacy-conscious users who cannot pay the privacy cost of creating an account

The social networks recommended here solve these issues by operating on open, decentralized protocols. They also don't require accounts to view publicly available content.

> **Important**: No social networks are appropriate for private or sensitive communications. For direct conversations, use a recommended [instant messenger](https://www.privacyguides.org/en/real-time-communication/) with strong end-to-end encryption. Only use social media direct messages to establish contact before moving to a more secure platform.

## Understanding Decentralization

Decentralized social networks use a fundamentally different architecture than mainstream platforms—similar to how email works.

### How It Works

Instead of creating an account under a single, unified service (like Facebook or Discord), you choose an independent, public server to join. Your server can communicate with and discover other servers through a process called **federation**.

### Benefits

- **No central censorship authority**: No single entity can ban your account across the entire network
- **Server independence**: Each server operates as its own legal entity with its own policies
- **Choice and flexibility**: You can select a server aligned with your values and needs

### Considerations

Each server has its own:
- Privacy policy and terms of use
- Administration team and moderators
- Level of restrictiveness (some more privacy-respecting, others potentially worse)

The underlying software typically doesn't limit administrator powers, so server choice matters significantly.

## Achieving Censorship Resistance

While network-level censorship doesn't exist in decentralized systems, server administrators can still:
- Ban or silence accounts
- **Defederate** from other servers (limiting your content access and interactions)

### Options for Maximum Control

1. **Self-host the software**: Provides the same censorship resistance as any self-hosted website
2. **Use managed hosting services**: Providers handle technical aspects while you control moderation—often the better approach for most users who want control without technical burden

When choosing a hosting provider, carefully review their terms of service and acceptable use policies. These are typically broader than individual server rules and less likely to be enforced with recourse.

## Mastodon

**Mastodon** is a social network based on open web protocols and free, open-source software using the **ActivityPub** protocol.

- [Homepage](https://joinmastodon.org/)
- [Documentation](https://docs.joinmastodon.org/)

### Why Mastodon?

1. **Strong security track record**: Quick, coordinated patch releases for vulnerabilities with backports to older versions, plus built-in update notifications for administrators

2. **Content versatility**: While primarily a microblogging platform, it handles longer posts, images, videos, and other content types—making it an ideal "central hub" for following anyone on ActivityPub-compatible platforms (like PeerTube)

3. **Comprehensive privacy controls**: Built-in features to limit data sharing, with new features developed with privacy in mind

### Choosing an Instance

Select a server aligned with the content you want to post or read about. 

**Recommendation**: Avoid *mastodon.social* and *mastodon.online*—they're operated by the same company that develops Mastodon. For decentralization's long-term health, it's better to separate software developers from server hosts.

### Recommended Privacy Settings

#### Public Profile Settings

| Setting | Recommendation | Reason |
|---------|---------------|--------|
| Automatically accept new followers | **Uncheck** | Creates a private profile where you review follow requests; you can still publish public posts if desired |
| Show follows and followers on profile | **Uncheck** | Hides your social graph—rarely beneficial to others but potentially risky for you |
| Display from which app you sent a post | **Uncheck** | Prevents revealing your computing setup |

> **Note**: Profile settings like "hide from search engines" are **requests**, not technical controls. Search engines can still read your profile. The only effective way to hide posts is using non-public visibility **and** limiting followers.

#### Preferences

Change your default posting visibility to prevent accidental over-sharing. You can always adjust visibility when composing individual posts.

#### Automated Post Deletion

- **Enable**: Automatically delete old posts
- **Default**: Deletes posts after 2 weeks unless you favorite (star) them

This approach treats most posts as ephemeral while letting you intentionally preserve important content. Older posts are rarely relevant but can build a comprehensive profile about you over time.

### Posting Visibility Levels

| Level | Description | Privacy Note |
|-------|-------------|--------------|
| **Public** | Anyone on the internet | Fully public |
| **Quiet public** | Requests hiding from some feeds | Not a technical guarantee—treat as public |
| **Followers** | Only your followers | If you don't restrict followers, treat as public |
| **Specific people** | Only mentioned users | Mastodon's DMs—**no E2EE**, don't use for private communications |

**Best practice**: Post to **Followers** by default; use **Public** intentionally and case-by-case.

## Element (Matrix)

**Element** is the flagship client for the **Matrix** protocol, an open standard enabling decentralized communication through federated chat rooms.

- [Homepage](https://element.io/)
- [Privacy Policy](https://element.io/privacy)
- [Documentation](https://element.io/help)
- [Source Code](https://github.com/element-hq)

**Available on**: Web, Windows, macOS, Linux, Android (Google Play, GitHub), iOS

### Choosing a Homeserver

Select a homeserver aligned with the subjects you want to discuss. Resources like [joinmatrix.org](https://servers.joinmatrix.org/) can help.

**Recommendation**: Avoid *matrix.org*—operated by the same company that develops Matrix. Separating developers from server hosts benefits long-term decentralization.

### Recommended Privacy Settings

Access via ⚙ → **All settings**:

#### Sessions
- **Empty the session name** to display only the random Session ID instead of revealing your device and client information

#### Preferences
- **Uncheck**: Send read receipts
- **Uncheck**: Send typing notifications

These reduce metadata exposure in public rooms.

#### Voice & Video
- **Uncheck**: Allow Peer-to-Peer for 1:1 calls
- **Uncheck**: Allow fallback call assist server

Prevents IP address exposure during one-to-one communication.

#### Security & Privacy

**Integration Manager** (scalar.vector.im):
- Consider **unchecking** "Enable the integration manager" to limit third-party data sharing (doesn't affect bot visibility)
- Review the [Privacy Notice](https://element.io/integration-manager-privacy-notice) for details

**Sessions**:
- *Optional*: Uncheck "Record the client name, version, and url" (may make managing multiple sessions harder)

#### Encryption
- *Optional*: Check "In encrypted rooms, only send messages to verified users"

This ensures only verified users and devices receive your messages in encrypted rooms, though it may limit your interactions.

## Selection Criteria

These recommendations follow specific requirements:

- **Free and open-source software**
- **Federated protocol** for inter-instance communication
- **No non-technical federation restrictions**
- **Usable in standard web browsers**
- **Public content accessible without accounts**
- **Profile follower restrictions available**
- **Followers-only posting option**
- **Modern security standards** (including multifactor authentication support)