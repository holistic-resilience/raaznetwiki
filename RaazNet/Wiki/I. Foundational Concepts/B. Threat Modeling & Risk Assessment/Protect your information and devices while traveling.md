---
title: "Protect Your Information and Devices While Traveling"
tags: [travel-security, border-crossing, device-protection, data-minimization, encryption, privacy]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, Human Rights Defenders]
topics: ["Travel Security", "Border Crossing", "Device Protection", "Data Privacy"]
summary: "Comprehensive guide for protecting digital devices and data when traveling, with specific focus on border crossing preparation and using public networks safely."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts", "Familiarity with password management"]
estimated_read_time: "15 minutes"
---

# Protect Your Information and Devices While Traveling

Traveling exposes you, your devices, and your data to significant risks. Laptops and other devices can fail, get stolen, lost, damaged, or impounded. Data transmitted from public access points such as airport and hotel wifi networks can be intercepted. Using untrusted systems may expose you to keyloggers and other attacks designed to capture sensitive information.

When crossing any national border, you have few if any rights to protest or refuse when a border control or customs officer wants to inspect any part of your luggage, including data stored on your laptop, mobile device, digital camera, or recorder. In many countries, including the US, a customs officer needs no "probable cause" or warrant to search your machine or confiscate it for further inspection.

This guide provides recommendations to prepare for your travels and minimize risks for your data and devices when traveling and crossing borders.

---

## Basic Security Practices

Implement these general security practices with special care when planning a journey:

- **Set strong, unique passwords** for all your accounts before traveling
- **Enable multi-factor authentication** on email, social media, and other accounts whenever possible
- **Update your operating system and software** — outdated systems are more vulnerable to attacks
- **Run updated antivirus software** on your devices
- **Avoid opening unrequested attachments or links** in emails or other messages to prevent phishing attacks and malware infections
- **Research your destination country** — check if the internet is censored, if VPNs and circumvention tools are allowed, if encryption is banned, and if laws require handing over passwords or encryption keys to border police
- **Configure automatic device locking** when unattended, and require passwords at login and when resuming from standby
- **Watch for shoulder surfers** — be aware of who is nearby when typing passwords, passphrases, and PINs, and look for cameras that could capture your keystrokes

---

## Prepare for Crossing Borders

### Minimize the Data You Carry

- Assess what data you actually need while traveling versus what can be left behind
- Copy unneeded data to a fully encrypted computer or hard drive at home and delete it from travel devices
- Consider storing encrypted data or a system image on a secure cloud service, traveling with a minimal laptop, and downloading what you need at your destination

**Why this matters:** Data you don't carry cannot be lost or stolen. Ensure you're not carrying anything potentially illegal in destination countries (copyrighted material, certain images, etc.), as such material could result in device confiscation.

### Use an Alternative Email Address

- Log out of your regular email accounts
- Create a new web-based email account specifically for your travels
- Use this address only for non-sensitive communications
- Dispose of the account after your trip

**Why this matters:** Border agents may check your mailbox, and untrusted connections expose your email to attacks. A temporary travel email limits the consequences if the account is compromised.

### Remove Accounts from Your Devices

- Log out of all accounts before crossing borders
- Remove or hide social media and other sensitive apps
- Consider creating secondary profiles on major platforms, populated with harmless content starting weeks in advance

**Why this matters:** Border agents may inspect social media accounts found on your devices. Logging out and removing apps prevents access to potentially compromising content.

### Clean Up Your Web Browsers

- Log out of all accounts (email, social networking, etc.)
- Clear temporary internet files and browsing history

### Clean Up Your Chat Apps

- Consider which chat apps might raise concerns (in some countries, having Signal visible may increase risk)
- Search for and remove sensitive conversations
- Rename groups to non-descriptive names if you're an admin
- Enable disappearing messages in sensitive chats
- Consider uninstalling messenger apps if time is short, though absence of any messaging app may also appear suspicious

### [Advanced] Hide Sensitive Files or Folders

- **Android:** Use the Safe folder in your Files app
- **iOS:** Use the Hidden album for photos
- **Both platforms:** Use Tella to hide sensitive files; on Android, Tella can be camouflaged as a calculator
- **Computers:** Create a hidden folder with VeraCrypt

**Why this matters:** If you must carry sensitive files, hiding them in encrypted, concealed locations provides additional protection during border inspections.

---

## Use Encryption to Protect Your Data and Communications

### Check Encryption Legality

Before traveling, verify whether encryption import, export, or use is legal in your destination countries.

If encryption is illegal, the safest approach is to encrypt your data, upload it to secure cloud storage, delete it from travel devices, and download it after arrival.

### Encrypt Your Devices

- Enable full-device encryption
- Encrypt external storage devices
- Maintain good backups — encryption makes data recovery harder if hardware fails

**Why this matters:** Encryption ensures that anyone accessing your device without your passphrase sees only random data. However, encrypted drives are harder to recover from physical damage, making backups essential.

### [Advanced] Protect Your Cryptographic Keys

If you use PGP email encryption, your private keys are among the most valuable data on your device. Pay particular attention to protecting them and their passphrases:

- Never leave devices unattended when others have access
- Consider keeping private keys on an encrypted USB drive that stays on your person rather than on your travel devices

---

## Public Access

### Shared Computers

Always consider shared computers (libraries, hotels, conference centers) as insecure.

- **Hardware keyloggers:** Check for suspicious dongles between the keyboard cable and computer
- **Software keyloggers/spyware:** Much harder to detect; consider these mitigations:
  - Bring a small USB keyboard to reduce hardware keylogger risk
  - Travel with a custom live USB containing your own operating system to bypass the untrusted computer entirely

### Protect Connections on Untrusted Networks

When using hotel wifi, municipal hotspots, or other untrusted networks:

- Configure your browser to use HTTPS-only mode
- Install one or more VPNs before your trip
- Use protective browser extensions, especially an ad blocker like uBlock Origin
- Pay attention to certificate warnings — they may indicate a machine-in-the-middle (MITM) attack (though absence of warnings doesn't guarantee safety)

**Why this matters:** Rogue nodes on untrusted networks can intercept site addresses and email contents, or redirect you to malicious fake sites. HTTPS and VPNs encrypt your traffic to prevent interception.

---

## Internet Censorship and Blockages

- Learn how internet censorship works
- Research circumvention methods before traveling
- If you're a human rights defender, journalist, or activist traveling to countries with sophisticated surveillance, contact [Front Line Defenders](https://www.frontlinedefenders.org/emergency-contact) or [Access Now Digital Security Helpline](https://www.accessnow.org/help) for country-specific recommendations

---

## Mobile Phone Security

### Travel with a Different Phone

Mobile phones should generally be considered insecure. The best practice is to:

- Leave your primary phone at home
- Travel with a different device that doesn't contain all your data
- If you must bring your work phone, back up all data and remove it from the device

### Use Secure Messaging Apps

Use end-to-end encrypted messaging apps for communications while traveling. These can encrypt messages, files, and voice calls.

### [Advanced] Hide Sensitive Apps

- **Android:** Hide sensitive apps using Private Space
- **iOS:** Lock or hide apps using built-in functionality

---

## References

- [Lily Hay Newman, Matt Burgess, *How to Protect Yourself From Phone Searches at the US Border*, Wired, Apr 21, 2025](https://www.wired.com/story/how-to-protect-yourself-from-phone-searches-at-the-us-border/)
- [Nikita Mazurov, Matt Sledge, *Crossing the U.S. Border? Here's How to Protect Yourself*, The Intercept, March 29 2025](https://theintercept.com/2025/03/29/customs-us-border-travel-airports-phone-searches/)
- [Andy Greenberg, Matt Burgess, *How to Enter the US With Your Digital Privacy Intact*, Wired, Mar 24, 2025](https://www.wired.com/2017/02/guide-getting-past-customs-digital-privacy-intact/)
- [Princeton University International Travel Guide](https://informationsecurity.princeton.edu/intltravel)