---
title: "Passkeys: Passwordless Logins for Beginners"
tags: [passkeys, authentication, phishing-protection, passwordless, account-security]
category: "Authentication"
difficulty: "Beginner"
audience: [General Public, Journalists, Privacy-Conscious Users]
topics: ["Digital Security", "Account Protection", "Passwordless Authentication"]
summary: "Guide to setting up passkeys for phishing-resistant passwordless login using your phone, computer, or security key."
source: "Freedom of the Press Foundation"
content_type: "Tutorial"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Compatible device and browser"]
estimated_read_time: "6 minutes"
---

# Passkeys: Passwordless Logins for Beginners

One of the most common ways people get hacked is through phishing — when an attacker impersonates a trusted website to trick you into entering your credentials. But what if you never had to type in a password? Passwordless logins — known as passkeys — reduce your risk by enabling you to log in using credentials on your device, such as your phone or computer. Because a passkey will only work on the appropriate service, this approach is highly resistant to phishing attacks.

This guide walks through how to set up passkeys to boost the security of your online accounts.

## What's a Passkey?

Think of a passkey as a credential you store on your trusted device. Instead of proving your identity to an online service by typing in a password, passkeys prove your identity by showing you have access to a device — such as your phone — registered with your online account.

The [technology behind passkeys](https://en.wikipedia.org/wiki/WebAuthn) is being developed by [a major industry association](https://fidoalliance.org/members/).

Passkeys can be used:
- On your phone, using on-screen prompts and biometric face or fingerprint scanning
- On your desktop computer, with biometric face or fingerprint scanning
- On a compliant security key (e.g., [see this list](https://passkey.org/#:~:text=Do%20YubiKeys%20support%20passkeys%3F) from Yubico)

## Setting Up Passkeys

You don't have to stop using passwords if you don't want to. But where available, passkeys are a more secure option to avoid typing in a password to a website.

Passkeys do not yet work on all major operating systems and browsers, so [check this compatibility table](https://passkey.org/#TABLE) before getting started.

### Step-by-Step: Google Account Example

**Step 1:** In a supported desktop browser, navigate to [g.co/passkey](https://g.co/passkey) and log into your Google account. You will see the passkey registration menu in your account settings.

> **Note:** If you use Android and have previously tied this account to your device, you may already have "Automatically created passkeys" enabled, which allows you to receive login prompts on your mobile device.

**Step 2:** Press the "Create a passkey" button at the bottom of the screen.

**Step 3:** To add a passkey using your current device, press "Continue" twice. You may receive a pop-up asking you to confirm by entering your password, or a fingerprint or face scan if you have enabled them previously.

Once enabled, you will be able to log in using the passkey you registered on this device.

### Adding Passkeys to Additional Devices

After you have one passkey, you can add passkeys to additional devices by registering them in close proximity to your first device. You'll need to enable Bluetooth, as the devices use a combination of a secure web connection and Bluetooth.

To create a new passkey on another device:
1. Go to "Create a passkey"
2. Select "Choose another device"
3. Choose the device you'd like to use (phone, tablet, or security key)

**For mobile users:** When prompted, scan the QR code that appears on the screen. On your mobile device, click "Allow" > "Continue" > Choose your authentication method. On iOS or iPadOS, you may be prompted to turn on iCloud Keychain.

**For security key users:** When prompted, plug the security key into your USB port and tap its button to activate the device.

If you run into trouble, ensure your device is up to date and attempt to register again.

## Limitations of Passkeys

### Register Multiple Passkeys
In case you ever lose access to a device with your passkey, register more than one device.

### Device Security Matters
Passkeys are only as safe as the device on which you store them. Someone with your unlocked device could potentially sign into your accounts using your on-device prompts. Likewise, if you leave a passkey on someone else's device, they may be able to log in as you.

**Important:** Only use passkeys on devices you control, and ensure your device is properly encrypted and protected with a strong password.

### Enable Disk Encryption
- Modern iOS and Android devices should have disk encryption enabled by default
- For Windows: Enable [Bitlocker](https://support.microsoft.com/en-us/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)
- For macOS: Enable [FileVault](https://support.apple.com/en-us/HT204837)

### Limited Availability
Passkeys aren't yet supported on all major browsers or online services, but expect to see passkeys rolling out on a growing number of services in years to come. Until then, maintain long, unique passwords using a password manager.

## Additional Resources

- [Your smartphone and you: A handbook to modern mobile maintenance](https://freedom.press/training/your-smartphone-and-you-handbook-modern-mobile-maintenance/#make-sure-you-have-a-good-password) — Guide to setting up a strong device password
- [Choosing a password manager](https://freedom.press/training/blog/choosing-password-manager/) — For accounts that don't yet support passkeys

If you run into any trouble, journalists in need of support should [reach out to Freedom of the Press Foundation's digital security training team](https://freedom.press/training/request-training/).