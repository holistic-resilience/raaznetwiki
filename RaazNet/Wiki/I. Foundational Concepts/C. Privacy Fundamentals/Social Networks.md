---
title: "Privacy-Respecting Social Networks"
tags: [social-media, privacy, decentralization, mastodon, matrix, fediverse, activitypub]
category: "Digital Privacy"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["Social Networks", "Decentralization", "Online Privacy", "Federated Services"]
summary: "Guide to privacy-respecting decentralized social networks including Mastodon and Matrix, with recommended privacy settings and configuration."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of social media", "Basic computer literacy"]
estimated_read_time: "12 minutes"
---

# Privacy-Respecting Social Networks

Privacy-respecting social networks allow you to participate in online communities without surrendering personal information like your full name, phone number, and other data commonly requested by mainstream platforms.

> **Important**: No social networks are appropriate for private or sensitive communications. For direct messaging, use a recommended [instant messenger](https://www.privacyguides.org/en/real-time-communication/) with strong end-to-end encryption. Only use social media direct messages to establish a more secure communication channel with contacts.

## The Problem with Mainstream Social Media

Social media platforms face two major censorship issues:

1. **External Censorship**: Platforms often comply with illegitimate censorship requests from governments or enforce restrictive internal policies
2. **Access Barriers**: Requiring accounts to view publicly available content effectively censors privacy-conscious users unwilling to pay the privacy cost of registration

The recommended networks solve these issues by operating on open, decentralized protocols and allowing public content viewing without accounts.

## Understanding Decentralization

Decentralized social networks operate fundamentally differently from mainstream platforms, using an architecture similar to email.

### How It Works

Instead of creating an account under a single unified service (like Facebook or Discord), you choose an independent public server to join. Your server communicates with and discovers other servers—this is called **federation**.

### Benefits

- **No central authority** can censor your account across the entire network
- Greater resilience against platform-wide shutdowns
- Choice of communities with different rules and cultures

### Caveats

Each server is its own legal entity with:
- Its own privacy policy and terms of use
- Independent administration and moderation teams
- Varying levels of restrictiveness (some more privacy-respecting, others potentially worse)

The underlying software typically doesn't limit administrator powers, so server choice matters significantly.

## Achieving Censorship Resistance

While network-level censorship doesn't exist in decentralized networks, server-level censorship is possible. Administrators can **defederate** from other servers, limiting the content you see and people you can interact with.

### Options for Maximum Control

1. **Self-host the software**: Provides the same censorship resistance as any self-hosted website
2. **Use managed hosting services**: Providers handle technical aspects while you control moderation. This approach suits most users—you gain control without managing security vulnerabilities

When choosing a hosting provider, carefully review their terms of service and acceptable use policies. These are typically broader than individual server rules and less likely to be enforced with recourse.

## Mastodon

**Mastodon** is a social network based on open web protocols and free, open-source software using the **ActivityPub** protocol.

- [Homepage](https://joinmastodon.org/)
- [Documentation](https://docs.joinmastodon.org/)

### Why Mastodon?

1. **Strong Security Track Record**: Quick, coordinated patch releases for vulnerabilities, with backports to older versions for less experienced server hosts. Built-in update notifications help administrators stay current.

2. **Versatile Content Handling**: While primarily a microblogging platform, Mastodon handles longer posts, images, videos, and most ActivityPub content types. Your account becomes a central hub for following anyone across the fediverse.

3. **Comprehensive Privacy Controls**: Many built-in features limit data sharing, with new features developed with privacy in mind.

### ActivityPub Interoperability

Many platforms use ActivityPub, enabling cross-platform communication. For example, you can follow PeerTube video channels from your Mastodon account since both use ActivityPub.

### Choosing an Instance

Select a server aligned with your interests. Recommendations:
- **Avoid** *mastodon.social* and *mastodon.online*—operated by Mastodon's developers, concentrating too much control
- Seek advice from privacy-focused communities
- Prioritize separating software developers from server hosts for long-term decentralization health

### Recommended Privacy Settings

#### Public Profile Settings

| Setting | Recommendation | Reason |
|---------|---------------|--------|
| Automatically accept new followers | **Uncheck** | Enables private profile; review followers before accepting. You can still publish public posts if desired. |
| Show follows/followers on profile | **Uncheck** | Hides your social graph; rarely benefits others but can present risks to you |
| Display posting app | **Uncheck** | Prevents revealing your computing setup unnecessarily |

> **Note**: Other profile privacy controls are **requests**, not technical enforcement. Search engines aren't technically blocked—you're merely requesting they not index you. The only effective way to hide posts is using non-public visibility **and** limiting followers.

#### Preferences

- **Default post visibility**: Set to **Followers** to prevent accidental over-sharing (adjustable per post)

#### Automated Post Deletion

- **Enable automatic deletion** of old posts (default: 2 weeks)
- **Star/favorite** posts you want to keep permanently
- Adjust retention settings to your needs

> Old social media posts build comprehensive profiles over time. Publish ephemerally by default; keep posts longer only intentionally.

### Post Visibility Levels

| Level | Description | Privacy Note |
|-------|-------------|--------------|
| **Public** | Visible to anyone on the internet | Full exposure |
| **Quiet public** | Requests hiding from some feeds | Not a technical guarantee—treat as public |
| **Followers** | Only visible to followers | If you don't restrict followers, treat as public |
| **Specific people** | Only mentioned users see it | **Not secure**—Mastodon lacks E2EE; never use for sensitive communications |

With recommended settings, default to **Followers** and consciously choose **Public** on a case-by-case basis.

## Element (Matrix)

**Element** is the flagship client for the **Matrix** protocol, an open standard for decentralized communication via federated chat rooms.

- [Homepage](https://element.io/)
- [Privacy Policy](https://element.io/privacy)
- [Documentation](https://element.io/help)
- [Source Code](https://github.com/element-hq)

**Available on**: Web, Windows, macOS, Linux, Android (Google Play/GitHub), iOS

### Choosing a Homeserver

- Select a homeserver aligned with your chat topics
- **Avoid** *matrix.org*—operated by Matrix developers, concentrating control
- Consult resources like [joinmatrix.org](https://servers.joinmatrix.org/) for options

### Recommended Privacy Settings

Access via ⚙️ → **All settings**:

#### Sessions
- **Empty the session name** to display only the random Session ID, preventing device information exposure to other users

#### Preferences
- **Uncheck**: Send read receipts
- **Uncheck**: Send typing notifications

These reduce metadata exposure in public rooms.

#### Voice & Video
- **Uncheck**: Allow Peer-to-Peer for 1:1 calls
- **Uncheck**: Allow fallback call assist server

Prevents IP address exposure during one-to-one calls.

#### Security & Privacy

**Integration Manager** (*scalar.vector.im*):
- Consider **unchecking** "Enable the integration manager"
- Review the [Privacy Notice](https://element.io/integration-manager-privacy-notice) for data collection details
- Disabling doesn't affect bot or third-party service visibility

**Sessions**:
- *Optional*: Uncheck "Record client name, version, and URL" (may complicate multi-device session management)

#### Encryption
- *Optional*: Check "In encrypted rooms, only send messages to verified users"
- Limits communication to verified users/devices only
- May restrict viewable messages and interactions

## Selection Criteria

Recommended social networks must:

- Be free and open-source software
- Use federated protocols for inter-instance communication
- Have no non-technical federation restrictions
- Work in standard web browsers
- Allow public content viewing without accounts
- Support follower restrictions
- Enable followers-only posting
- Support modern security standards including multi-factor authentication

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/social-networks/)*