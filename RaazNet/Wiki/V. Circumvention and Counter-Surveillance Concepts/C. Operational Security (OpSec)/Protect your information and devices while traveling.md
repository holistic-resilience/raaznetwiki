---
title: "Protect Your Information and Devices While Traveling"
tags: [travel-security, border-crossing, encryption, mobile-security, privacy-protection, digital-safety]
category: "Travel Security"
difficulty: "Intermediate"
audience: [Travelers, Activists, Journalists, Privacy-Conscious Users]
topics: ["Digital Security", "Border Security", "Data Protection", "Mobile Security"]
summary: "Comprehensive guide for protecting your devices, data, and communications when traveling and crossing international borders."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts", "Familiarity with mobile device settings"]
estimated_read_time: "15 minutes"
---

# Protect Your Information and Devices While Traveling

Traveling exposes you, your devices, and your data to many risks. Laptops and other devices can fail, get stolen, lost, damaged, or impounded. Data transmitted from public access points such as airport and hotel WiFi networks can be intercepted. Using untrusted systems may expose you to keyloggers and other attacks designed to capture sensitive information.

When crossing any national border, you have few if any rights to protest or refuse when a border control or customs officer wants to inspect any part of your luggage, including the data stored on your laptop, mobile device, digital camera, or recorder. In many countries, including the US, a customs officer needs no "probable cause" or warrant to search your machine or confiscate it for further inspection.

This guide provides recommendations to prepare for your travels and minimize risks for your data and devices when traveling and crossing borders.

---

## Basic Security Practices

These general security practices should be implemented with special care when planning a journey.

### Account Security
- Set **strong and unique passwords** for all your accounts before traveling
- Enable **[multi-factor authentication](https://securityinabox.org/en/passwords/2fa/)** on email, social media, and other accounts to minimize unauthorized access risk

### Device Security
- **Update your operating system and software** — outdated systems are more vulnerable to attacks
- Ensure an **updated antivirus** is running on your device
- **Avoid opening unrequested attachments or links** in emails or messages to prevent phishing attacks and malware infections
- **Set your device to lock automatically** when unattended, and require a password at login and when resuming from standby

### Research Your Destination
Investigate the situation of the country you will be visiting:
- Check if the internet is censored
- Verify if VPNs and circumvention tools are allowed
- Determine if [encryption is banned](https://securityinabox.org/en/assess-plan/safer-travel/#check-whether-encryption-is-legal-in-the-countries-youre-traveling-to)
- Research laws requiring disclosure of device passwords, encryption keys, or email credentials to border police

### Physical Awareness
**Watch out for shoulder surfers.** Be aware of who is in your immediate vicinity when typing passwords, passphrases, and PINs. Protect against observers watching your fingers on the keyboard or screen, and look for cameras in your environment.

---

## Prepare for Crossing Borders

### Minimize the Data You Carry

Ask yourself what data you actually need while traveling and what can be left behind.

**Recommended approach:**
1. Copy everything you don't need to another fully encrypted computer or hard drive that will remain safe at home or office
2. Delete unnecessary data from devices you'll travel with
3. Consider storing encrypted data or an entire system image on a [secure cloud service](https://securityinabox.org/en/files/backup/#encrypted-cloud-services) and traveling with a minimal laptop

> **Why this matters:** Data you're not carrying cannot be lost or stolen. When crossing borders, ensure you're not carrying any data that could be illegal in any country you're visiting—including unauthorized copies of copyrighted material or content that might be considered illegal. Such material found in a border search could result in device confiscation.

### Use an Alternative Email Address

1. Log out of your regular email accounts (whether using an app, email client, or browser)
2. Create a new web-based email account specifically for your travels
3. Use this address for all non-sensitive communications while traveling
4. Dispose of the account after your trip

> **Why this matters:** Border agents may want to check your mailbox, which may contain sensitive information. During travels, you'll likely use untrusted connections and systems, exposing your email to possible attacks. If this travel-only account is compromised, it provides no value to attackers beyond the end of your trip.

### Remove Your Accounts from Devices

- Log out of all accounts before crossing the border
- Remove (or [hide](https://securityinabox.org/en/assess-plan/safer-travel/#advanced-hide-your-sensitive-apps-in-your-mobile-device)) social media and sensitive apps from your devices
- Consider creating alternative profiles on major social media platforms, populated with harmless content (small talk, food photos, etc.) starting weeks or months in advance

> **Why this matters:** Border agents might inspect social media accounts found on your devices. By logging out and removing apps, you prevent them from discovering accounts with potentially compromising content.

### Clean Up Your Web Browsers

- Log out of all accounts (email, social networking, etc.)
- Clear temporary internet files and [browsing history](https://securityinabox.org/en/safer-browsing/#delete-your-browsing-history)

### Clean Up Your Chat Apps

- Evaluate which chat apps you have installed (in some countries, having Signal on your device at checkpoints may put you at risk)
- Search for sensitive words in your chat history and remove those conversations
- Change group names to non-descriptive titles if you're the admin
- Enable disappearing messages in sensitive chats
- Consider uninstalling messenger apps if needed, but note that having no messenger app can also appear suspicious

### [Advanced] Hide Sensitive Files or Folders

If you must carry sensitive files:

| Platform | Method |
|----------|--------|
| **Android** | [Protect files in the Safe folder](https://support.google.com/files/answer/9935264) of your Files app |
| **iOS** | [Hide photos in a Hidden album](https://support.apple.com/en-us/104987) |
| **Android/iOS** | Use [Tella](https://tella-app.org/features/#file-management) to hide sensitive files; on Android, you can also [camouflage Tella](https://tella-app.org/video-tutorials/#camouflaging-tella) as a calculator |
| **Computer** | [Create a hidden folder with VeraCrypt](https://securityinabox.org/en/files/secure-file-storage/#consider-whether-to-store-your-files-in-a-hidden-volume) |

---

## Use Encryption to Protect Your Data and Communications

### Check Whether Encryption Is Legal

Before traveling, [verify the encryption rules](https://securityinabox.org/en/files/secure-file-storage/#consider-whether-encryption-is-illegal-or-suspicious-in-your-jurisdiction) in each country you'll visit.

> **Important:** While encrypting device data is always advisable, the import, export, and/or use of cryptography is illegal in some countries. If encryption is illegal in your destination, the best approach is to [encrypt your data, upload it to secure cloud storage, and delete it from your travel devices](https://securityinabox.org/en/assess-plan/safer-travel/#minimize-the-data-youll-be-carrying-with-you).

### Encrypt Your Devices

- [Encrypt your entire devices](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-your-whole-device)
- [Encrypt your external storage devices](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-your-external-storage-devices)
- [Learn more about protecting sensitive data](https://securityinabox.org/en/files/secure-file-storage)

> **Note:** Using encryption makes data recovery harder if your hard drive is damaged. Advanced data recovery costs are typically beyond the resources of most human rights defenders and civil society organizations. [Maintaining good backups](https://securityinabox.org/en/files/backup/) is essential.

### [Advanced] Protect Your Cryptographic Keys

If you encrypt your email, your private PGP encryption keys are among the most valuable data on any device you carry. Pay particular attention to protecting them and the passphrase that unlocks them:
- Never allow devices containing keys to be in third-party hands without supervision
- Never leave these devices unattended when others have access
- Consider keeping private keys on an encrypted USB thumb drive worn around your neck, kept under your control at all times

---

## Public Access

When traveling, you may frequently use public systems—computers in libraries or public areas, or wired/wireless networks in hotels and conference centers. Each situation has specific risks.

### Shared Computers

**Always consider shared computers insecure.**

**Mitigation strategies:**
- Bring a small USB keyboard to reduce the risk of hardware keyloggers
- Travel with a custom live USB containing your trusted operating system and basic software to bypass the untrusted computer's standard setup

> **Why this matters:** The most likely way your security could be compromised while traveling is through logging into accounts on untrusted machines. Hardware keyloggers are dongles inserted between the keyboard and computer—check for these before using any keyboard that isn't your own. Software keyloggers and spyware are more dangerous because they're difficult to detect.

### Protect Your Connections on Untrusted Networks

- Configure your browser to connect only through **HTTPS**
- Install one or more **VPNs** before your trip
- [Use protective browser extensions](https://securityinabox.org/en/internet-connection/safer-browsing/#use-protective-browser-add-onsextensions), especially an ad blocker like [uBlock Origin](https://securityinabox.org/en/internet-connection/tools/#ublock-origin)
- Pay attention to security warnings when initiating connections—these may indicate a machine-in-the-middle (MITM) attack

> **Why this matters:** Untrusted connections (hotel WiFi, public hotspots, etc.) are constant when traveling. Rogue nodes in such networks may perpetrate MITM attacks, capturing site addresses, email contents, and communications. They can also divert your traffic to dangerous fake sites. Always use HTTPS, which encrypts all your traffic.

---

## Internet Censorship and Blockages

- [Learn how the internet works and how it can be censored](https://securityinabox.org/en/internet-connection/how-the-internet-works/)
- [Learn how to circumvent internet blockages and monitoring](https://securityinabox.org/en/internet-connection/circumvention/)

**For high-risk travelers:** If you're a human rights defender, journalist, or activist traveling to countries with sophisticated surveillance and limited internet access, contact [Front Line Defenders](https://www.frontlinedefenders.org/emergency-contact) or [Access Now Digital Security Helpline](https://www.accessnow.org/help) for country-specific recommendations.

---

## Mobile Phone Security

### Travel with a Different Phone

Mobile phones should generally be considered insecure. When traveling:
1. Leave your primary phone at home
2. Travel with a different mobile device that doesn't contain all your data
3. If you must take your work phone, back up all data to a separate device and remove it from your phone

For additional protection, see guides on securing [Android devices](https://securityinabox.org/en/phones-and-computers/android/) and [iPhones/iPads](https://securityinabox.org/en/phones-and-computers/ios/).

### Use Secure Messaging Apps

- [Check recommended messaging apps for secure communications](https://securityinabox.org/en/communication/tools/#more-secure-text-voice-and-video-chat-applications)
- [Read the guide on protecting online communication privacy](https://securityinabox.org/en/assess-plan/private-communication/)

Secure messaging apps can encrypt messages, files, and voice calls—offering some of the fastest ways to secure communications while traveling.

### [Advanced] Hide Sensitive Apps

- **Android:** [Hide sensitive apps with private space](https://support.google.com/android/answer/15341885)
- **iOS:** [Hide sensitive apps](https://support.apple.com/guide/iphone/lock-or-hide-or-an-app-iph00f208d05/ios#iphf1dd187d3)

---

## References

- [Lily Hay Newman, Matt Burgess, *How to Protect Yourself From Phone Searches at the US Border*, Wired, Apr 21, 2025](https://www.wired.com/story/how-to-protect-yourself-from-phone-searches-at-the-us-border/)
- [Nikita Mazurov, Matt Sledge, *Crossing the U.S. Border? Here's How to Protect Yourself*, The Intercept, March 29, 2025](https://theintercept.com/2025/03/29/customs-us-border-travel-airports-phone-searches/)
- [Andy Greenberg, Matt Burgess, *How to Enter the US With Your Digital Privacy Intact*, Wired, Mar 24, 2025](https://www.wired.com/2017/02/guide-getting-past-customs-digital-privacy-intact/)
- [Princeton University International Travel Guide](https://informationsecurity.princeton.edu/intltravel) — one of the most complete resources available