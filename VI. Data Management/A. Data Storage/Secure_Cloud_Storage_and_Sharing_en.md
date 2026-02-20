---
title: "Secure Cloud Storage and Sharing"
tags:
  [
    cloud-storage,
    encryption,
    e2ee,
    privacy,
    iran,
    circumvention,
    file-sharing,
    data-sovereignty,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics:
  [
    "End-to-End Encryption",
    "Censorship Circumvention",
    "National Information Network",
    "Secure File Sharing",
  ]
summary: "Comprehensive guide to storing and sharing data securely in Iran, bypassing local surveillance (NIN) and using end-to-end encryption to protect against both domestic and international threats."
source: "Raaznet Aggregated Knowledge"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Working VPN/Circumvention Tool", "Basic understanding of encryption"]
estimated_read_time: "15 minutes"
---

# Secure Cloud Storage and Sharing

In the context of digital landscape, "the cloud" presents a dual threat. On one side, global providers (like Google or Dropbox) scan your data for commercial purposes and may comply with international sanctions or legal requests. On the other, the Islamic Republic's **National Information Network (NIN)** actively seeks to force users onto domestic platforms to monitor, intercept, and control data.

For an Iranian user, **Secure Cloud Storage** means ensuring that **only you** hold the keys to your data. Even if the server is seized, the company is subpoenaed, or the connection is intercepted by the Telecommunication Infrastructure Company of Iran (TIC), the data must remain unreadable.

This guide prioritizes **End-to-End Encryption (E2EE)** and censorship-resistant tools.

---

## ⚠️ Critical Warning: The Trap of Domestic Clouds

The Iranian government heavily subsidizes and promotes domestic "cloud" services (e.g., **ArvanCloud (Abr Arvan)**, **Pod**, **Shatel**, **Pars Online**). They offer high speeds and low costs (half-price traffic) to lure users away from the global internet.

> **⛔ DANGER:** **Never store sensitive data on Iranian domestic cloud providers.**
>
> - **Surveillance:** These companies are legally required to comply with the Islamic Republic's security apparatus.
> - **Deep Packet Inspection (DPI):** Traffic to these data centers is monitored.
> - **Sanctions & Complicity:** Several domestic providers, including ArvanCloud, have been sanctioned for their role in facilitating internet censorship and shutdowns.
> - **Data Sovereignty:** By using these services, you are voluntarily placing your data within the "digital borders" of the regime.

---

## Strategy 1: Native End-to-End Encrypted Providers

The safest option is to use a cloud provider where encryption is the default. The provider cannot read your files even if they want to.

### Proton Drive

Part of the Swiss-based Proton ecosystem (Mail, VPN).

- **Why it's recommended:**
  - **Proven Security:** Open source and audited. Uses E2EE for all files, filenames, and folders.
  - **Ecosystem:** If you already use Proton Mail (recommended for email), Drive is integrated.
  - **Censorship Resistance:** While Proton domains are often targeted by filtering, their VPN's "Stealth" protocol is effective at bypassing Iranian DPI, allowing you to access the Drive.
- **Free Tier:** 1 GB to 5 GB (varies by signup bonuses).
- **Payment in Iran:** Accepting payments is difficult due to sanctions. Proton accepts **Bitcoin**, which can be purchased via local exchanges (use a mixer or Monero swap before paying for privacy).
- **Platform:** Web, Android, iOS, Windows, macOS.

### Filen

A Germany-based, open-source encrypted storage provider.

- **Why it's recommended:**
  - **High Free Tier:** Offers 10 GB free, which is generous compared to competitors.
  - **Zero Knowledge:** Client-side encryption ensures Filen knows nothing about your data.
  - **Less Targeted:** As a smaller provider compared to Google or Proton, it may occasionally fly under the radar of the filtering committee's blocklists, though a VPN is still required.
- **Payment:** Accepts Crypto.

### Ente Photos (Google Photos Alternative)

If your goal is to back up photos without Google scanning faces or locations.

- **Why it's recommended:**
  - **E2EE:** Photos are encrypted on your phone before upload.
  - **Features:** detailed "Places" and "People" albums using **local** machine learning (on your device), not on the server.
  - **Open Source:** Fully auditable code.

---

## Strategy 2: "Bring Your Own Encryption" (Cryptomator)

Sometimes, you cannot access Proton or Filen due to heavy throttling, but major platforms like **Google Drive** or **OneDrive** might be accessible (or whitelisted for business reasons).

**Cryptomator** allows you to use these insecure clouds securely.

### How It Works

Cryptomator creates a "Vault" on your computer or phone. Anything you drag into this vault is encrypted _before_ it is synced to the cloud. Google/Microsoft only see a folder of nonsense gibberish files.

- **Pros:**
  - **Reliability:** Leverages the massive infrastructure and uptime of Google/Microsoft.
  - **Obfuscation:** To an observer (ISP/TIC), it just looks like standard HTTPS traffic to Google, which is common and often harder to block completely than specific VPN protocols.
- **Cons:**
  - Metadata (file modification times and approximate size) is still visible to the cloud provider.
- **Usage in Iran:**
  1.  Install Cryptomator (Desktop/Mobile).
  2.  Create a vault inside your Google Drive/Dropbox folder.
  3.  Unlock the vault with a strong password.
  4.  Place sensitive files inside the virtual drive.
  5.  Let the cloud app sync the _encrypted_ data.

> **Note:** Do not rely on "password protection" features built into Microsoft Office or PDFs. They are easily cracked. Use Cryptomator.

---

## Strategy 3: Decentralized & Peer-to-Peer (Syncthing)

**Syncthing** replaces the "cloud" entirely. It synchronizes files directly between your devices (e.g., between your phone and your laptop) without storing them on a central server.

- **Why it's vital for Iran:**
  - **No Central Target:** There is no "Syncthing.com" login page for the regime to block.
  - **Resilience:** It works over the internet but also over **Local LAN**. If the government cuts the international internet (Iron Curtain/National Internet mode), Syncthing can still sync files between devices connected to the same Wi-Fi router.
  - **Privacy:** Data never leaves your hardware unencrypted.
- **Setup:** Install on all devices. Exchange "Device IDs". Folders sync automatically when devices are online.

---

## Strategy 4: Secure File Sharing

When you need to send a file to a colleague, journalist, or friend, do not use Telegram or WhatsApp for highly sensitive documents (Telegram is not E2EE by default; WhatsApp metadata is owned by Meta).

### OnionShare

Uses the Tor network to create a temporary, anonymous file server on your computer.

- **Security Level:** Extreme.
- **Mechanism:** You add a file, it generates a `.onion` link. The recipient opens it in Tor Browser. The file moves directly from you to them.
- **Anonymity:** Hides your IP address and location completely.
- **Iran Context:** Requires a working Tor connection (use Tor Bridges like Snowflake or Meek).

### Wormhole.app / Send

For quick, web-based sharing.

- **Wormhole.app:** Uses E2EE. Fast. Link expires automatically.
- **PrivateBin:** For sharing text/code. Enable "Burn after reading".
- **Usage:**
  1.  Upload file.
  2.  Copy link.
  3.  Send link via Signal.
  4.  Recipient downloads file.
  5.  File is deleted from server.

---

## Comparison Summary

| Service          | Best For             | E2EE?  | Iran Accessibility  | Cost                                |
| :--------------- | :------------------- | :----- | :------------------ | :---------------------------------- |
| **Proton Drive** | General Storage      | ✅ Yes | Needs VPN (Stealth) | Free (limited) / Paid               |
| **Filen**        | Free Storage (10GB)  | ✅ Yes | Needs VPN           | Free / Paid                         |
| **Cryptomator**  | Using Google/Dropbox | ✅ Yes | Depends on Cloud    | Free (Desktop) / Small fee (Mobile) |
| **Syncthing**    | Syncing Devices      | ✅ N/A | High (P2P)          | Free (Open Source)                  |
| **OnionShare**   | Anonymous Sharing    | ✅ Yes | Needs Tor Bridge    | Free                                |
| **ArvanCloud**   | **NOTHING**          | ❌ No  | **Avoid**           | **High Risk**                       |

## Best Practices Checklist for Iranian Users

1.  **VPN is Mandatory:** Never access cloud storage without a trusted VPN. Use obfuscated protocols (V2Ray, Shadowsocks, OpenVPN + XOR) to hide the traffic type.
2.  **Redundancy:** "Two is one, one is none." Keep a local backup (USB drive) and a cloud backup. If the internet is cut, you need the local copy.
3.  **Sanitize Metadata:** Before uploading photos or documents, remove metadata (location, author name, device info) using tools like **ExifCleaner** or by sending the photo to yourself on Signal (which strips metadata).
4.  **Complex Passwords:** Your encryption is only as strong as your password. Use a diceware passphrase (e.g., `correct-horse-battery-staple`) stored in a password manager (e.g., **Bitwarden** or **KeepassXC**).
5.  **Panic Button:** If you are at risk of physical device seizure (detention/arrest), know how to uninstall these apps or wipe the local data quickly. On mobile, many of these apps (like Proton) offer a PIN lock or biometric wipe feature.
