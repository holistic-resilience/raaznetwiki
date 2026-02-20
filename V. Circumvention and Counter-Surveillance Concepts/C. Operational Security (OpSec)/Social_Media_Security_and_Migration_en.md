---
title: "Social Media Security and Migration"
tags:
  [
    social-media,
    privacy,
    account-security,
    digital-security,
    iran,
    censorship-circumvention,
    platform-migration,
    anonymity,
    opsec,
  ]
category: "Operational Security (OpSec)"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Human Rights Defenders]
topics:
  [
    "Social Media Hardening",
    "Identity Protection",
    "Platform Migration",
    "Anti-Surveillance",
  ]
summary: "Comprehensive guide for Iranian users on securing social media accounts, managing online identities, and migrating to privacy-focused alternatives to mitigate state surveillance."
source: "Raaznet Consolidated Guides"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites: ["Basic understanding of social media settings", "VPN usage"]
estimated_read_time: "20 minutes"
last_updated: "2026-02-17"
---

# Social Media Security and Migration

Social media is a vital tool for news, business, and connection, but it is also a primary vector for state surveillance, identification, and evidence gathering by security agencies. The Islamic Republic actively monitors platforms like Instagram, X (Twitter), and Telegram to identify dissenters, track networks, and suppress opposition.

This guide focuses on hardening your presence on major platforms, managing your identity to prevent doxing and arrest, and considering migration to decentralized alternatives that offer better resistance to censorship and control.

---

## I. Core Security Principles for Iranian Users

Before diving into specific apps, apply these universal rules to all your social media accounts.

### 1. Identity Compartmentalization (The "Two Lives" Strategy)

In a high-risk environment, mixing your personal identity with your political or activist identity is dangerous.

- **Public/Official Profile:** Use this for family, non-political work, and harmless hobbies. Keep it clean of sensitive content.
- **Activist/Anonymous Profile:** Use this for political discourse, organizing, or sharing news.
  - **Never** link this to your real phone number. Use a virtual number or a foreign SIM if possible.
  - **Never** allow apps to sync your contacts.
  - Use a pseudonym unrelated to your real name or nicknames.
  - Use a generic profile picture (avoid photos of your face, unique tattoos, or your home).
  - Always access this account via a trusted VPN or Tor.

### 2. Strong Authentication

- **Passwords:** Use unique, long passphrases (16+ characters) stored in a password manager (e.g., KeePassXC, Bitwarden).
- **2FA (Two-Factor Authentication):** **Avoid SMS 2FA.** Iranian mobile carriers (MCI, Irancell) are state-controlled and can intercept SMS codes. Use an authenticator app (like Aegis, Raivo, or Google Authenticator) or a hardware security key.

### 3. Metadata Hygiene

- **Location:** Disable location services for all social media apps. Never tag your real-time location in posts.
- **Photos/Videos:** Scrub metadata (EXIF data) before uploading. Tools like **ObscuraCam** or **Scrambled Exif** can remove location and device data from images.
- **Face Blurring:** If posting photos of protests or gatherings, ensure all faces are blurred to prevent facial recognition software from identifying participants.

---

## II. Platform-Specific Hardening

### Instagram (Meta)

Instagram is widely used in Iran but is heavily monitored.

- **Lockdown:** Set your account to **Private** if you are not a public figure. This forces you to approve followers.
- **Close Friends:** Use the "Close Friends" list for sensitive stories, but assume anyone can screenshot them.
- **Activity Status:** Go to Settings and turn off "Show Activity Status" to hide when you are online.
- **Hidden Words:** Use the "Hidden Words" feature to filter out harassment and bot comments automatically.
- **Disappearing Mode:** For sensitive DMs, use vanish mode, but remember that **Instagram DMs are not end-to-end encrypted by default**. Do not discuss sensitive operational details here.

### X (formerly Twitter)

A hub for political discourse, but also a playground for regime bots and trolls.

- **Protect Your Tweets:** If you are under threat, make your account private (Settings > Privacy and safety > Audience and tagging > Protect your posts).
- **Discoverability:** Go to _Privacy and safety > Discoverability and contacts_. Uncheck "Let people who have your email address/phone number find you."
- **Two-Factor Authentication:** X has limited SMS 2FA to paid users, which is actually a security benefit. Use an Authenticator App instead.
- **Cleaning History:** Tools like **Redact** or **TweetDelete** can wipe your old post history. Regular purging is recommended to minimize the data available for mining.

### Telegram

While technically a messenger, its Channels function as social media.

- **Phone Number Privacy:** Set "Who can see my phone number" to **Nobody** and "Who can find me by my number" to **My Contacts**.
- **Forwarded Messages:** Restrict who can forward your messages. Set "Who can add a link to my account when forwarding my messages" to **Nobody**.
- **Peer-to-Peer Calls:** Disable Peer-to-Peer calls or restrict them to contacts to hide your IP address.
- **Warning:** Telegram chats (Groups and Channels) are **not** end-to-end encrypted. The server has access to your data. Use "Secret Chats" for 1-on-1 sensitive conversations.

### TikTok

TikTok collects massive amounts of data and has unclear relationships with various governments regarding data sharing.

- **Avoid for Sensitive Use:** Due to aggressive data collection (clipboard access, location, keystroke monitoring in in-app browser), strictly avoid TikTok for activist communications.
- **Burner Device:** If you must use it, install it on a separate, isolated device or use the web version via a hardened browser.

---

## III. Doxing and Harassment Defense

"Doxing" is the public release of private information (address, phone number, workplace) to incite harassment. In Iran, this is often a precursor to state action.

### Prevention

1.  **Audit Your Footprint:** Search for your username and real name on Google. Request removal of personal info from data aggregators.
2.  **Social Media Cleanup:** Review old posts. Did you mention your university? Your neighborhood? A favorite cafe? Delete these details.
3.  **Lock Down Friends Lists:** Hide your "Following" and "Followers" lists on Facebook and Instagram to prevent mapping of your social network.

### Response

If you are targeted by a regime cyber-army or trolls:

1.  **Do Not Engage:** Replies boost their visibility.
2.  **Go Private:** Temporarily lock your accounts.
3.  **Block and Report:** Use mass-blocking tools like **Block Party** (if available/compatible) or manually block instigators.
4.  **Document:** Take screenshots of threats for potential future legal or asylum claims, then delete the notifications.

---

## IV. Social Media Migration: The "X-odus"

Due to the increasing toxicity and surveillance on centralized platforms like X and Instagram, many users are migrating to decentralized, privacy-respecting alternatives.

### Why Migrate?

- **Censorship Resistance:** Decentralized platforms are harder for a single government to block or pressure into removing content.
- **No Algorithmic Manipulation:** You see what you follow, not what a state-influenced algorithm wants you to see.
- **Privacy:** Better data handling and no selling of user data to third parties.

### Alternatives

#### 1. Mastodon (The Fediverse)

A decentralized network of independent servers.

- **Pros:** No central authority, supports chronological feeds, allows "content warnings" (useful for sensitive news), and supports pseudonymity.
- **How to Join:** You choose a "server" (instance). For Iranian users, look for instances hosted in jurisdictions with strong privacy laws (e.g., Switzerland, Iceland, Germany).
- **Security:** Choose a server with a clear privacy policy. Remember that server admins can technically see DMs (they are not E2EE).

#### 2. Bluesky

An alternative to X founded by Jack Dorsey.

- **Pros:** Familiar interface for X users, user-controlled moderation tools.
- **Cons:** Still centralized in terms of company ownership, though the protocol is open.

### Migration Tools

- **Fedifinder / Debirdify:** These tools help you find your X (Twitter) mutuals on Mastodon.
- **Cyd:** Helps back up your tweets and data from X before you delete your account.

### Migration Strategy for Iranian Users

1.  **Don't Delete Immediately:** Keep your old accounts active but dormant to prevent someone else from claiming your username and impersonating you.
2.  **Post a Redirect:** Pin a post on your old profile directing trusted followers to your new handle (e.g., "Find me on Mastodon @username").
3.  **Verification:** Cross-verify your new identity using your PGP key or a secure website if you have one.

---

## V. Emergency "Kill Switch" Protocol

If you are at risk of imminent arrest or device seizure:

1.  **Deactivate Accounts:** most platforms allow temporary deactivation. This hides your profile from public view immediately.
2.  **Log Out:** Log out of all sessions on all devices.
3.  **Unlink Devices:** Go to settings (e.g., Telegram Devices, WhatsApp Linked Devices) and terminate all active sessions.
4.  **Panic Button:** If using Android, consider apps like **Ripple** (by Guardian Project) that can trigger a "panic" sequence to wipe apps or send emergency messages.

**Remember:** Digital security is a process, not a product. Regularly review these settings, especially as platform policies and regime tactics evolve.
