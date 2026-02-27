---
title: "Mainstream Social Media Security"
tags:
  [
    social-media,
    facebook,
    instagram,
    twitter,
    x,
    tiktok,
    linkedin,
    opsec,
    iran-security,
    account-hardening,
  ]
category: "Platform Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Iranian Users]
topics:
  [
    "Digital Hygiene",
    "Surveillance Resistance",
    "Account Security",
    "Anonymity",
  ]
summary: "Comprehensive guide to securing accounts on Facebook, Instagram, X (Twitter), and TikTok, specifically tailored to mitigate risks posed by the Iranian surveillance state."
source: "Raaznet Aggregated Knowledge"
content_type: "Guide"
security_level: "High"
language: "English"
last_updated: "2026-02-18"
---

# Mainstream Social Media Security

For Iranian users, mainstream social media platforms are a double-edged sword. They are vital tools for accessing information, organizing, and amplifying voices against censorship. However, they are also primary targets for surveillance by the Islamic Republic's security agencies (including FATA and IRGC intelligence). Authorities actively monitor these platforms to identify dissidents, map social networks, and gather evidence for prosecution.

This guide provides actionable steps to harden your accounts on **Meta (Facebook/Instagram)**, **X (formerly Twitter)**, and **TikTok**, with a specific focus on circumventing state monitoring and protecting your identity.

---

## ⚠️ Critical General Security Principles (Read First)

Before configuring specific apps, apply these "Golden Rules" to all your social media interactions within Iran.

### 1. The "Web Browser" Strategy

**Avoid installing official mobile apps** (Facebook, X, TikTok) on your primary smartphone whenever possible.

- **The Risk:** Mobile apps often have broad permissions to access your contact list, precise location, clipboard, and file system. They run in the background and can leak data even when using a VPN.
- **The Solution:** Access these platforms via a secure web browser (like Brave, Firefox, or Tor Browser) on your phone or desktop. This isolates the platform from your device's core data.

### 2. Never Use Iranian Phone Numbers for 2FA

Do not use SMS Two-Factor Authentication (2FA) linked to Irancell, MCI (Hamrah Aval), or Rightel.

- **The Risk:** Iranian telecommunication providers are legally required to cooperate with security services. SMS codes can be intercepted to hijack your accounts.
- **The Solution:** Use **Time-Based One-Time Passwords (TOTP)** via apps like **Raivo OTP** (iOS), **Aegis** (Android), or **Ente Auth**. If available, use a hardware security key (YubiKey) or Passkeys.

### 3. Sanitize Media (Metadata Removal)

Photos and videos contain hidden data (EXIF/Metadata) revealing the exact GPS location, time, and device model used.

- **The Risk:** Security forces use this data to locate where a protest video was filmed or identify the uploader.
- **The Solution:** Use an app like **Scrambled Exif** (Android) or **Metapho** (iOS) to strip metadata _before_ uploading. Take photos directly through the social media camera (less secure quality, but often strips metadata) or screenshot your own photo and upload the screenshot.

### 4. VPN Hygiene

Always ensure your VPN is active (with Kill Switch enabled) before opening any social media platform. Accidental connections via domestic IP addresses can deanonymize your account to the ISP.

---

## 🛡️ Meta Ecosystem: Facebook & Instagram

Given that Instagram is one of the few remaining vital lifelines for commerce and communication in Iran (despite filtering), securing your Meta account is critical.

### Identity & Anonymity

- **Pseudonyms:** If your activity is political, do not use your real name.
- **Separate Accounts:** Maintain a strict "air gap" between your personal life (family/friends) and your activist identity. Do not follow one account with the other.

### Privacy Settings Checklist

Navigate to **Settings & Privacy > Accounts Center** to manage these settings centrally.

1.  **Hide Your Connections:**
    - Set "Who can see your friends list?" and "Who can see people/pages you follow?" to **Only Me**.
    - _Why:_ Intelligence agents map dissident networks by analyzing who follows whom.
2.  **Disable "Link History" (Facebook):**
    - Meta recently introduced a feature that tracks every link you click.
    - _Action:_ Go to **Settings & Privacy > Browser** and toggle **OFF** "Allow Link History". Clear any existing history.
3.  **Two-Factor Authentication:**
    - Enable 2FA using an Authenticator App.
    - Generate **Backup Codes** and store them in an encrypted password manager (e.g., KeepassXC).

### Instagram Specifics

- **Close Friends Only:** For semi-private content, strictly use the "Close Friends" feature, but assume any viewer could screenshot your post.
- **Activity Status:** Go to **Messages and story replies > Show activity status** and turn it **OFF**. This prevents others from seeing when you are online (a metric used in interrogations to correlate activity with protests).
- **Suppressed Folders:** Be aware that "Hidden Requests" in DMs often contain phishing links sent by regime-aligned actors. Do not click links in DMs.

---

## 🐦 X (Twitter) Security

X is the primary platform for breaking news and political discourse. It is heavily monitored by state-sponsored bot farms and intelligence officers.

### Anonymity & Anti-Doxxing

- **Phone Number:** Go to **Settings > Privacy and safety > Discoverability and contacts**. Uncheck "Let people who have your phone number find you." Better yet, remove your phone number entirely if you have a reliable 2FA app set up.
- **Location:** Ensure "Precise Location" is disabled in your device settings for the app. Never tag your location in a Tweet.

### Account Hardening

1.  **Two-Factor Authentication:**
    - X has made SMS 2FA a paid feature. This is a blessing in disguise. Use the **Authentication App** method (free and more secure).
2.  **Protect Your Tweets:**
    - If you are under immediate threat, set your account to **Private** (`Settings > Privacy and safety > Audience and tagging > Protect your posts`). This prevents non-followers (including bots and OSINT investigators) from viewing your history.
3.  **Session Management:**
    - Regularly check **Settings > Security and account access > Apps and sessions**. Revoke access to any third-party apps you do not recognize or no longer use.

### Iranian Context: The "Cyber Army"

Be aware of "Cyber Army" tactics: mass-reporting accounts to trigger automated bans, and swarming posts with distractions.

- **Defensive Tactic:** Do not engage with suspicious accounts. Use "Block" rather than "Mute" to prevent them from seeing your future activities.

---

## 🎵 TikTok: High-Risk Warning

**Use with Extreme Caution.**
TikTok's parent company, ByteDance, has a history of data accessibility issues. Furthermore, TikTok collects an aggressive amount of device fingerprinting data (keystrokes, battery patterns, other installed apps).

**Raaznet Recommendation:** Do not install TikTok on a device used for sensitive activism or communication.

### If You Must Use TikTok:

1.  **The "Burner" Method:** Use TikTok only on a secondary device that has no SIM card, no personal contacts, and connects only via a trusted VPN.
2.  **Web Browser Access:** Use TikTok via a desktop browser or mobile browser rather than the app. This limits the data they can harvest.
3.  **Privacy Settings:**
    - Set account to **Private**.
    - Disable "Suggest your account to others" (Contacts, Facebook friends).
    - Set "Downloads" to **Off**.
    - Set "Following list" to **Only Me**.

---

## 🔗 LinkedIn: Anti-Doxxing

While primarily professional, LinkedIn is a goldmine for doxxing (revealing real-world identities).

- **Profile Visibility:** If you are a public activist, consider hibernating your LinkedIn or ensuring it does not link your current employment to your political identity.
- **Search Engines:** In settings, turn **OFF** "Profile visibility off LinkedIn" to stop Google from indexing your employment history.

---

## 🚨 Emergency Protocols (Arrest/Seizure)

If you are at risk of imminent arrest or device seizure:

1.  **Log Out:** Log out of all social media apps. Biometric unlock (FaceID/Fingerprint) can be forced; a strong password cannot be easily bypassed without your consent (though coercion is a risk).
2.  **Deactivate Temporarily:** Most platforms allow temporary deactivation. This removes your content from public view immediately without permanently deleting data (useful if you need to recover evidence later).
3.  **Panic Button:** If you have a trusted contact outside Iran (a "Digital Godparent"), give them emergency access codes to lock down or delete your accounts remotely if you go silent for a set period.

## Summary Checklist for Iranian Users

| Platform      | Critical Action Item                                                   |
| :------------ | :--------------------------------------------------------------------- |
| **All**       | **Disable SMS 2FA**; Use Authenticator Apps (Aegis/Raivo).             |
| **All**       | **Remove Metadata** (Location/Device info) from photos before posting. |
| **Facebook**  | Disable **Link History** in browser settings.                          |
| **Instagram** | Set **Following List** visibility to private/minimal.                  |
| **Twitter/X** | Remove phone number from "Discoverability".                            |
| **TikTok**    | **Do not install the app**; use web browser only.                      |
