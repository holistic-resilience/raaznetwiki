---
title: "Video Conferencing and Remote Collaboration Security"
tags:
  [
    video-conferencing,
    remote-work,
    signal,
    jitsi,
    zoom,
    google-meet,
    webrtc,
    iran-blackout,
    censorship-circumvention,
  ]
category: "Communication Platform"
difficulty: "Intermediate"
audience: [General Public, Activists, Remote Workers, Journalists]
topics:
  [
    "Secure Meetings",
    "Metadata Protection",
    "Censorship Circumvention",
    "Collaborative Tools",
  ]
summary: "Comprehensive guide to secure video conferencing and collaboration in Iran, focusing on the 2026 internet blackout context, WebRTC leak prevention, and end-to-end encrypted alternatives like Signal and Jitsi Meet."
source: "Raaznet Aggregated Resources"
content_type: "Wiki"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of VPNs", "Signal installed (optional but recommended)"]
estimated_read_time: "10 minutes"
last_updated: "2026-02-18"
---

# Video Conferencing and Remote Collaboration Security

This guide prioritizes tools that offer resilience against censorship and strong **End-to-End Encryption (E2EE)** to protect users from surveillance.

---

## 1. The Threat Landscape in Iran

When organizing video meetings or collaborating remotely, Iranian users face specific threats beyond standard corporate data harvesting:

- **Surveillance of Metadata:** Intelligence agencies (MOIS/IRGC) can monitor who calls whom, the duration, and the participants' IP addresses even if they cannot decrypt the content.
- **Forced Decryption:** If a participant is detained, they may be forced to unlock their device. Cloud-stored recordings (e.g., on Zoom or Google servers) are vulnerable to account compromise.
- **IP Address Leaks:** Peer-to-Peer (P2P) connections can reveal your true IP address to other participants, exposing your location even if you use a VPN (via WebRTC leaks).
- **AI Analysis:** Platforms like Zoom have historically updated terms to allow AI training on user data. In a high-risk context, automated voice analysis could theoretically be used for identification.

---

## 2. Top Recommendation: Signal

For most users, **Signal** is the safest and most resilient option for both 1-on-1 and group calls. As of February 2026, Signal has increased its group call capacity, making it a viable competitor to Zoom for small-to-medium gatherings.

### Why Signal?

- **True End-to-End Encryption:** Always on. No setting to "forget" to enable.
- **Metadata Minimization:** Signal knows _that_ you communicated, but not _who_ you spoke to or _what_ was said.
- **Resilience:** Signal's protocol is often better at functioning through censorship (using proxies) than heavy video streaming protocols.

### Key Configurations for Security

1.  **Group Call Limit:** Signal now supports up to **75 participants** in a group call.
2.  **Relay Calls (Hide IP):** By default, calls might connect P2P to improve quality, revealing your IP to the contact.
    - _Action:_ Go to **Settings > Privacy > Calls** and enable **"Always Relay Calls"**. This routes traffic through Signal servers, masking your IP address (though it may slightly reduce call quality).
3.  **Group Links:** Instead of adding members manually, create a Group Link.
    - _Action:_ In Group Settings, enable **Group Link** and turn on **"Approve New Members"** to prevent infiltration.

---

## 3. Alternative: Jitsi Meet

**Jitsi Meet** is a free, open-source video conferencing tool that runs in a browser without requiring an account. It is the best alternative for users who cannot install apps or need to join from a desktop.

### Critical Warning: Default Encryption vs. E2EE

By default, Jitsi encrypts data _in transit_ (between you and the server), but the server can theoretically see the stream. To be secure, you **must** enable End-to-End Encryption.

### How to Use Jitsi Securely

1.  **Use a Trusted Instance:** Avoid random Jitsi servers. Use instances hosted by privacy organizations:
    - `meet.jit.si` (Official - 8x8 owned, subject to US/EU laws)
    - `vc.autistici.org` (Autistici/Inventati - Italian activist collective)
    - `meet.greenhost.net` (Greenhost - Dutch privacy host)
2.  **Enable E2EE:**
    - Once inside the meeting, click the **Security Options** (shield icon) or "More Actions" menu.
    - Toggle **"End-to-End Encryption"** on.
    - _Note:_ All participants must be using a compatible browser (Chromium-based like Brave, Ungoogled Chromium, or Chrome) for this to work.
3.  **No Account Needed:** Do not link your Google or Facebook account if prompted.

---

## 4. Mainstream Platforms (Zoom, Google Meet, Teams)

**Warning:** These platforms are not private by design. They collect vast amounts of telemetry and metadata. Use them only if required for work or education, and assume the connection is monitored.

### Zoom

- **Status in Iran:** Often blocked (Error 403) or requires a VPN.
- **Hardening Steps:**
  1.  **Use the Web Client:** Avoid installing the Zoom app, which runs with high privileges. Join via browser (`Join from your browser` link usually hidden at the bottom of the launch page).
  2.  **Enable E2EE:** Free accounts support E2EE. The host must enable "End-to-End Encryption" in their web portal settings before the meeting. Look for the **green shield with a padlock** icon in the top left during the meeting to verify.
  3.  **Avoid Cloud Recording:** Never record meetings to the cloud.

### Google Meet / Microsoft Teams

- **Privacy Risk:** These services are fully integrated into corporate surveillance ecosystems. They do not offer true E2EE for consumer accounts (only "encryption in transit"). Google and Microsoft hold the keys to decrypt your stream.
- **Recommendation:** Avoid for sensitive activism or protest organization.

---

## 5. Critical Technical Risk: WebRTC Leaks

Even if you use a VPN, your browser's **WebRTC** (Web Real-Time Communication) feature—which powers browser-based video calls like Jitsi and Google Meet—can leak your _real_ IP address to the website admin or other participants.

### How to Prevent WebRTC Leaks

1.  **Browser Selection:** Use **Brave** or **Firefox**.
2.  **Configuration:**
    - **Brave:** Go to Settings > Shields > Change "Fingerprinting blocking" to **Strict**. (Note: This may break some Jitsi features; test beforehand).
    - **Firefox:** Type `about:config` in the address bar. Search for `media.peerconnection.enabled` and set it to **false**.
      - _Warning:_ Disabling WebRTC completely breaks Jitsi/Google Meet.
    - **Better Option for Firefox:** Use the `uBlock Origin` extension. Go to Settings > check **"Prevent WebRTC from leaking local IP addresses"**. This allows the call to work but tries to hide the local IP.
3.  **VPN Kill Switch:** Ensure your VPN client has "Leak Protection" and a "Kill Switch" enabled.

---

## 6. Secure Remote Collaboration (Docs & Spreadsheets)

Collaborating on Google Docs allows Google to see every keystroke. In the current threat environment, safer alternatives are necessary.

### Recommended Tools

| Tool                | Best For                                                                   | Security Feature                                                                 |
| :------------------ | :------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **Proton Docs**     | Real-time document editing                                                 | E2EE, integrated with Proton Drive. Servers in Switzerland.                      |
| **CryptPad**        | Docs, Spreadsheets, Kanban                                                 | Zero-knowledge encryption. No account required (can use anonymous "guest" pads). |
| **Skiff** (Defunct) | _Note:_ Skiff was acquired and shut down. Do not attempt to use old links. | N/A                                                                              |

### Best Practices for Collaboration

- **Password Protect Links:** If sharing a CryptPad or Proton Doc link via a non-secure channel (like email), ensure the document itself has a separate password sent via Signal.
- **Metadata Scrubbing:** Before sharing files (PDFs, Images, Word Docs), use tools like **MAT2** or **ExifCleaner** to remove metadata (author name, GPS location, device info).

---

## 7. Operational Security Checklist for Meetings

Before joining a sensitive meeting:

- [ ] **Check VPN:** Ensure it is active and obfuscated (Stealth protocol) to bypass DPI filtering.
- [ ] **Environment:** Check your physical background. Does it reveal your location (distinctive window view, street signs)? Use a background blur or virtual background.
- [ ] **Microphone:** Mute by default. Unmute only when speaking.
- [ ] **Screen Sharing:** Close all other tabs and applications before sharing your screen. Notifications from other apps can reveal sensitive info.
- [ ] **Recording:** Assume you are being recorded. Do not say anything you wouldn't want played in a court.

---

**Related Topics:**

- [[Signal_Messenger_Comprehensive_Guide]]
- [[Google_Services_Privacy_and_Hardening]]
- [[VPN_and_Censorship_Circumvention_Strategies]]
