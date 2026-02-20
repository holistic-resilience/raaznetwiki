---
title: "WhatsApp Security Guide"
tags:
  [
    whatsapp,
    meta,
    encryption,
    privacy,
    metadata,
    surveillance,
    iran,
    censorship,
    proxy,
    2fa,
  ]
category: "Communication Platform"
difficulty: "Beginner"
audience: [General Public, Iranian Users, Families]
topics:
  [
    "Secure Messaging",
    "Bypassing Censorship",
    "Account Security",
    "Metadata Risks",
  ]
summary: "Comprehensive guide for Iranian users on securing WhatsApp, enabling proxies, protecting against account hijacking, and understanding metadata risks."
source: "Raaznet Aggregated Resources"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Installed WhatsApp", "Basic settings knowledge"]
estimated_read_time: "10 minutes"
last_updated: "2026-02-18"
---

# WhatsApp Security Guide for Iranian Users

**Verdict:** While WhatsApp uses strong end-to-end encryption for message content, it is owned by Meta (Facebook) and collects significant metadata (who you talk to, when, and where). **It is NOT recommended for high-risk activism or sensitive political organization.** For those purposes, use **Signal**. However, WhatsApp remains a vital tool for staying in touch with family and friends. This guide helps you maximize its security within the Iranian context.

---

## 1. Installation and Connectivity in Iran

### Official Sources Only

Avoid "modified" versions of WhatsApp commonly found on Telegram channels or unofficial app stores (e.g., _GBWhatsApp_, _WhatsApp Plus_, _WhatsApp Gold_). These versions often contain malware, spyware, or backdoors that can expose your data to state actors or criminals. They also risk your account being permanently banned by Meta.

- **Android:** Download only from Google Play Store or the official website APK.
- **iOS:** Download only from the Apple App Store.

### Bypassing Censorship (Proxy Support)

WhatsApp is frequently blocked or restricted in Iran. If you cannot access WhatsApp via a VPN, you can use the built-in Proxy feature.

**How to Enable Proxy:**

1.  Go to **Settings** > **Storage and Data** > **Proxy**.
2.  Tap **Set-up Proxy**.
3.  Enter a trusted proxy address (often shared by digital rights groups like _TechVantage_ or _Toosheh_).
4.  Tap **Save**. A green checkmark indicates a successful connection.

> **Note:** Using a proxy hides your IP address from WhatsApp, but the proxy provider can see your IP. Ensure you use proxies from trusted sources.

---

## 2. Critical Account Security

### Two-Step Verification (2FA)

**This is the most important setting to prevent account hijacking.** Iranian security agencies have been known to intercept SMS verification codes to hijack accounts. Enabling 2FA adds a PIN code that only you know.

1.  Go to **Settings** > **Account** > **Two-step verification**.
2.  Tap **Turn On**.
3.  Enter a 6-digit PIN. **Do not use simple sequences (123456) or dates of birth.**
4.  (Optional but Recommended) Add an email address to reset the PIN if you forget it. Ensure this email is secure and uses a strong password.

### Email Verification

WhatsApp recently added email verification as an alternative login method, useful if SMS delivery is blocked or intercepted.

1.  Go to **Settings** > **Account** > **Email Address**.
2.  Verify your email.

---

## 3. Protecting Your Data

### End-to-End Encrypted Backups

By default, WhatsApp backups stored on Google Drive or iCloud are **NOT** encrypted by WhatsApp. This means if the cloud provider is compromised or subpoenaed, your messages can be read. You must enable End-to-End Encrypted (E2EE) Backups manually.

1.  Go to **Settings** > **Chats** > **Chat Backup**.
2.  Tap **End-to-end Encrypted Backup**.
3.  Tap **Turn On**.
4.  Create a password or generate a 64-digit encryption key.
    - **Warning:** If you lose this password/key, **no one** (including WhatsApp) can restore your backup. Store it in a secure Password Manager.

### Disappearing Messages

To minimize the data available on your device (and the recipient's device) if seized, enable disappearing messages.

1.  **Default for New Chats:** Settings > Privacy > Default message timer > Select 24 hours or 7 days.
2.  **For Existing Chats:** Open the chat > Tap contact name > Disappearing Messages.

---

## 4. Privacy Hardening

### Minimize Data Leaks

Configure who can see your activity to avoid social engineering or stalking.

- **Go to Settings > Privacy:**
  - **Last Seen & Online:** Set to **Nobody**. (Prevents monitoring of your activity patterns).
  - **Profile Photo:** Set to **My Contacts** or **Nobody**.
  - **About:** Set to **Nobody**.
  - **Groups:** Set to **My Contacts**. (Prevents strangers or bots from adding you to malicious groups).

### Advanced Privacy Features

- **Silence Unknown Callers:** Settings > Privacy > Calls > Turn On **Silence Unknown Callers**. This blocks spam and harassment calls often used to locate users.
- **Protect IP Address in Calls:** Settings > Privacy > Advanced > Turn On **Protect IP address in calls**.
  - _Why?_ Standard calls connect devices directly (P2P), revealing your IP address (and rough location) to the other person. This setting relays the call through WhatsApp servers, hiding your IP.

---

## 5. The Metadata Risk (Important for Activists)

Even with all settings enabled, Meta (Facebook) collects **Metadata**. They may not know _what_ you said (content), but they know:

- **Who** you spoke to.
- **When** you spoke and for how long.
- **Where** you were (IP address location).
- **Device info** (Phone model, OS).

In the context of Iranian surveillance, this "social graph" can be enough to map a network of protesters or activists. **If you require anonymity, do not use WhatsApp. Use Signal.**

---

## 6. Common Scams in Iran

### "Verification Code" Scam

**Scenario:** You receive an SMS code from WhatsApp, followed by a message from a friend or stranger saying, "I sent my code to you by mistake, please send it back."
**Action:** **NEVER share this code.** It is the key to your account. If you share it, the attacker will hijack your WhatsApp.

### "Family Emergency" Scam

**Scenario:** A message from an unknown number claiming to be a family member who has "changed their number" and needs money urgently.
**Action:** Call the family member on their _original_ number to verify. Do not send money or information.

### Malicious Links

**Scenario:** Links promising "Free Internet," "VPN Breaker," or "Protest News."
**Action:** Do not click suspicious links. They may lead to phishing sites or install malware.

---

## 7. Device Security

- **Screen Lock:** Enable App Lock in WhatsApp (Settings > Privacy > App Lock).
  - _Risk:_ In Iran, security forces may force you to unlock your phone with your fingerprint/face. Using a PIN or disabling biometrics before entering high-risk areas is recommended.
- **Linked Devices:** Regularly check **Settings > Linked Devices**. Log out of any session you do not recognize immediately.

---

### Quick Security Checklist

- [ ] Two-Step Verification (PIN) enabled.
- [ ] End-to-End Encrypted Backups enabled.
- [ ] Privacy settings (Last Seen, Groups) restricted to "My Contacts" or "Nobody".
- [ ] "Protect IP address in calls" enabled.
- [ ] Official app version installed (No GBWhatsApp).
