---
title: "Signal Messenger Comprehensive Guide"
tags:
  [
    signal,
    iran,
    censorship-circumvention,
    privacy,
    operational-security,
    encrypted-messaging,
  ]
category: "III. Platform and Device Knowledge"
topics:
  [
    "Secure Communication",
    "Censorship Resistance",
    "Metadata Minimization",
    "Mobile Security",
  ]
audience: [General Public, Activists, Journalists]
difficulty: "Intermediate"
source: "Raaznet Aggregated Data"
last_updated: "2026-02-18"
---

# Signal Messenger Comprehensive Guide for Iranian Users

Signal is widely considered the gold standard for secure communication due to its open-source nature, comprehensive end-to-end encryption (E2EE), and minimal metadata retention. Unlike Telegram or WhatsApp, Signal encrypts virtually all data, including profile information and group metadata, making it the primary recommendation for activists and journalists in Iran.

This guide covers installation, censorship circumvention, and essential hardening steps tailored to the Iranian threat landscape (internet shutdowns, device seizure, and surveillance).

---

## 1. Installation and Censorship Circumvention

In Iran, access to the Signal network is frequently blocked. You will likely need a circumvention tool to connect.

### Getting the App

- **Android:** Download the APK directly from [signal.org/android/apk](https://signal.org/android/apk) if the Google Play Store is blocked. Verify the signing certificate if possible.
- **iOS:** Requires access to the Apple App Store.
- **Alternative (Android):** Consider **Molly** (see Section 6), a hardened fork of Signal often used by activists.

### Connecting via Proxy

If you cannot connect via a standard VPN, Signal supports built-in TLS proxies.

1.  **Find a Proxy:** Search for `#SignalProxy` or `#IRanASignalProxy` on X (Twitter) or Mastodon. _Warning: Only use proxies from trusted sources to avoid metadata logging._
2.  **Configure:**
    - **Android/iOS:** Settings > Data and Storage > **Use Proxy**.
    - Toggle **On** and enter the proxy address.
    - If successful, a green checkmark will appear.

> **Note:** A Signal proxy only hides the fact that you are using Signal from your ISP; it does not encrypt your traffic inside the proxy tunnel (though Signal's traffic is already encrypted). For better anonymity, route Signal through a system-wide VPN (e.g., V2Ray/Xray/Orbot).

---

## 2. Profile Anonymity and Hiding Your Identity

As of 2026, Signal allows you to completely hide your phone number. This is critical in Iran to prevent authorities from correlating your Signal activity with your SIM card identity.

### Hiding Your Phone Number

1.  Go to **Settings > Privacy > Phone Number**.
2.  **Who can see my number:** Set to **Nobody**.
3.  **Who can find me by number:** Set to **Nobody**.
    - _Effect:_ Even if an interrogator has your phone number saved in their contacts, they will **not** see your Signal account unless you message them first.

### Setting a Username

Instead of sharing your phone number, share a username.

1.  Go to **Settings > Profile**.
2.  Create a unique username (e.g., `azadi_404.99`). It must end in two digits.
3.  Share your **QR code** or username link.
4.  _Note:_ You can change or delete this username at any time to sever ties with previous contacts.

### Profile Hygiene

- **Name:** Do not use your real legal name. Use a pseudonym.
- **Photo:** Do not use a photo of your face. Use a generic image (landscape, object) or an avatar. This prevents facial recognition bots from linking your Signal profile to other social media.

---

## 3. Communication Security Settings

Default settings are not sufficient for high-risk users.

### "Always Relay Calls" (Crucial)

By default, Signal calls connect P2P (Peer-to-Peer) for quality, which reveals your IP address to the person you are calling.

- **Enable:** Settings > Privacy > Advanced > **Always relay calls**.
- _Why:_ This routes calls through Signal servers, masking your IP address from the recipient and protecting your location.

### Link Previews

- **Disable:** Settings > Chats > **Generate link previews**.
- _Why:_ Generating a preview requires sending the URL to Signal/the website, which can leak your interest in specific content or reveal your IP to the target website.

### Typing Indicators and Read Receipts

- **Disable:** Settings > Privacy > **Read receipts** and **Typing indicators**.
- _Why:_ In a high-pressure situation, knowing _exactly when_ you read a message can be used against you (e.g., "We know you saw the protest coordination message at 4:00 PM").

---

## 4. Data Minimization & Forensics Defense

If your phone is seized by the FATA (Cyber Police) or IRGC, they will attempt to extract data. Your best defense is ensuring the data does not exist.

### Disappearing Messages (Auto-Delete)

This is your primary defense against device seizure.

1.  **Global Default:** Settings > Privacy > **Disappearing Messages**.
    - Set a default timer for _all new chats_ (e.g., 4 weeks for general, 1 hour for operations).
2.  **Active Threads:** Tap the chat header > **Disappearing Messages**.
    - **High Risk (Protest/Action):** Set to 5 minutes or 1 hour.
    - **Medium Risk:** Set to 1 week.

### Registration Lock (Anti-Hijacking)

Prevents authorities from hijacking your account by cloning your SIM card or intercepting SMS.

- **Enable:** Settings > Account > **Registration Lock**.
- **Action:** Set a PIN. Signal will require this PIN to register your number on a new device.
- _Warning:_ If you forget this PIN, you will be locked out of your account for 7 days if you reinstall.

### Screen Security

- **Android:** Settings > Privacy > **Screen security** (Blocks screenshots).
- **iOS:** Settings > Privacy > **Hide Screen in App Switcher**.
- **Incognito Keyboard (Android):** Settings > Privacy > **Incognito Keyboard** (Prevents Gboard/Samsung Keyboard from learning your typing history).

---

## 5. Backups: Cloud vs. Local

Signal introduced Secure Cloud Backups in late 2025. You must choose carefully based on your threat model.

| Feature            | Secure Cloud Backup   | Local Backup (Android)        | No Backup                  |
| :----------------- | :-------------------- | :---------------------------- | :------------------------- |
| **Convenience**    | High (Easy restore)   | Medium (Manual file copy)     | Low                        |
| **Security**       | High (E2EE)           | High (Passphrase protected)   | **Maximum**                |
| **Risk**           | Cloud metadata exists | File exists on device storage | Data is gone if phone lost |
| **Recommendation** | General Users         | Technologists                 | **Activists / Protesters** |

> **Critical Warning for Activists:** If you are attending a protest or fear imminent arrest, **disable backups** and delete old message history. A recovery key found in your notebook or password manager can be forced out of you.

---

## 6. Advanced: Molly (Android Only)

For Android users, **Molly** is a hardened fork of Signal recommended for high-risk environments.

- **Database Encryption:** Molly allows you to encrypt the database with a passphrase _separate_ from your system lock screen.
- **RAM Shredding:** Clears sensitive data from memory to prevent cold-boot attacks.
- **Tor Integration:** Native support for Orbot/Tor routing.
- **FOSS:** The "Molly-FOSS" version removes Google proprietary code, ideal for de-googled phones (GrapheneOS).

---

## 7. Protest & Emergency Protocols

### Before a Protest

1.  **Update Signal:** Ensure you have the latest security patches.
2.  **Shorten Disappearing Timers:** Set to minutes.
3.  **Clean Up:** Delete old threads and "Leave" groups that are no longer active.
    - _How to Leave:_ Open Group > Settings > **Leave Group**.
    - _Then Delete:_ Long press the chat > **Delete**. (Leaving is not enough; the history remains unless you delete).
4.  **Hide the App:** Use your launcher to hide the Signal icon or move it to a "Secure Folder" (Samsung) or "Private Space" (Android 15+).

### During Arrest/Seizure

- **Lock Your Phone:** If you cannot destroy the data, turn the phone **off** completely. This puts the encryption keys in a "cold" state (BFU - Before First Unlock), making forensic extraction significantly harder than if the phone is merely "locked" (AFU).

---

## 8. Common Scams & Attacks

- **"Signal Support" Phishing:** You may receive messages claiming your account will be deleted unless you click a link or send a code. **Signal never asks for SMS codes.** Block and report these accounts.
- **Fake Proxies:** Avoid proxies promoted by suspicious channels, as they can monitor metadata (IP addresses and timing), though they cannot read message content.

## Summary Checklist for Iranian Users

- [ ] **VPN/Proxy:** Configured and tested.
- [ ] **Phone Number:** Hidden ("Nobody").
- [ ] **Username:** Set (no real name).
- [ ] **Registration Lock:** PIN Enabled.
- [ ] **Relay Calls:** Always On.
- [ ] **Disappearing Messages:** On by default (1 week or less).
- [ ] **Backups:** Disabled or strictly managed.
