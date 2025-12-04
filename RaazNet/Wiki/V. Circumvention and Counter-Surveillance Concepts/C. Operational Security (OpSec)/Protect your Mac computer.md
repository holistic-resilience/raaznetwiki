```yaml
---
title: "Protect Your Mac Computer"
tags: [macos, device-security, privacy, hardening, apple]
category: "Device Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists]
topics: ["macOS Security", "Privacy Protection", "Device Hardening"]
summary: "Comprehensive security guide for Mac computers covering system updates, privacy settings, and protection against surveillance."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Access to a Mac computer"]
estimated_read_time: "20 minutes"
---
```

# Protect Your Mac Computer

If you use a Mac, you may have heard the myth that Mac computers are more secure. This is not necessarily true. Security depends on a combination of how we use our devices and their own software, which can be found to have vulnerabilities at any time. Follow the steps in this guide to make your device more secure. Get in the habit of checking these settings from time to time, to make sure nothing has changed.

---

## Use the Latest Version of Your Operating System

When updating software, do it from a trusted location like your home or office, not at an internet cafe or coffee shop. Updating to the latest version of your operating system may require you to download software and restart a number of times. Set aside time for this where you do not need to do work on your device.

After updating, check again if there are any further updates available until you do not see any additional new updates. If the latest version of macOS will not run on your computer, it is best to consider buying a new device. Always restart your device when prompted to do so after downloading the update.

**Additional Resources:**
- [What to do if your computer doesn't have enough storage space to install](https://support.apple.com/en-us/102624)
- [Learn more about updating old versions of macOS](https://support.apple.com/en-us/102662)

> **Why this matters:** New vulnerabilities in the code that runs in your devices and apps are found every day. Malicious attackers may exploit these vulnerabilities to get into your devices. Software developers regularly release code that fixes those vulnerabilities, which is why it is very important to install updates and use the latest version of the operating system.

---

## Turn Lockdown Mode On

We strongly suggest [turning Lockdown Mode on](https://support.apple.com/en-us/105120) on your Mac computer. Most likely you will not see any or much difference in the way your device works, but you will be much better protected.

> **Why this matters:** [Lockdown Mode](https://support.apple.com/en-us/105120) limits infection strategies used by sophisticated spyware like [Pegasus](https://securityinabox.org/en/blog/pegasus-project-questions-and-answers/). Features of the Lockdown Mode should be used by everyone and should really be part of a standard operating system.

---

## Use Apps from Trusted Sources

- [Install apps from the App Store](https://support.apple.com/en-us/111105)
- [Only allow apps downloaded from the App Store](https://support.apple.com/en-us/102445#changesettings) unless you know what you are doing
- **Advanced:** Learn how to [temporarily override your security settings to install an app you trust](https://support.apple.com/en-us/102445#openanyway)

> **Why this matters:** [Apple's App Store](https://www.apple.com/app-store/) is the official app store for macOS. This centralized way of distributing apps makes it easier for Apple to monitor the offered apps for major security violations. If you decide to install apps from other sources, take additional steps to protect yourself, like planning to keep sensitive or personal information off that device.

---

## Remove Apps That You Do Not Need

[Learn how to uninstall apps on your Mac](https://support.apple.com/en-us/102610).

*Note: It is difficult and risky to uninstall many default apps that your Mac has pre-installed, like Safari or iTunes.*

> **Why this matters:** Removing apps you do not use helps limit the number of apps that might be vulnerable. Apps you do not use may also transmit information about you that you may not want to share with others, like your location.

---

## Use Privacy-Friendly Apps

- Browse the web with [Firefox](https://securityinabox.org/en/internet-connection/tools/#firefox)
- Read your email with [Thunderbird](https://www.thunderbird.net/)
- Use [free and open source software for almost everything you need to do on a Mac computer](https://github.com/serhii-londar/open-source-mac-os-apps)

> **Why this matters:** Mac computers come with built-in software, like Safari or iTunes, that have a history of [privacy](https://www.theregister.com/2024/04/30/apple_safari_europe_tracking/) and [security issues](https://www.techradar.com/news/apple-itunes-has-a-serious-security-flaw-you-really-should-know-about). You can use more privacy-friendly apps instead.

---

## Check Your App Permissions

Review all permissions one by one to make sure they are enabled only for apps you use. The following permissions are specifically suspicious as they are very regularly used by malicious applications:
- Location
- Photos
- Contacts
- Calendar
- Microphone
- Camera
- Usage logs

Review the topics linked in the ["Control the personal information you share with apps" section of the macOS guide on how to guard your privacy on Mac](https://support.apple.com/en-gw/guide/mac-help/mh35847/mac#mchlpa3b92d9).

> **Why this matters:** Apps that access sensitive digital details or services can leak that information or be exploited by attackers. If you do not need an app to use a particular service, turn that permission off.

---

## Turn Off Location and Wipe History

- Get in the habit of turning off location services overall, or when you are not using them
- Regularly check and clear your location history if you have it turned on
- Learn how to [turn off location services overall or just for specific apps](https://support.apple.com/en-gw/guide/maps/mpsa33caac1f/mac)
- If you use Google Maps, follow the instructions [for your Google Maps Timeline](https://support.google.com/accounts/answer/3118687#delete) and [your Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Many devices keep track of where we are using GPS, cell phone towers, and wifi networks. If your device is keeping a record of your physical location, it makes it possible for someone to find you or use that record to prove that you have been in certain places or associated with specific people.

---

## Create Separate User Accounts

Create more than one user account on your device, with one having "admin" (administrative) privileges and the others with "standard" (non-admin) privileges. Consider using a standard user for your day-to-day work.

[Learn how to add a user on Mac](https://support.apple.com/en-gw/guide/mac-help/mchl3e281fc9/mac)

> **Why this matters:** If you must share your devices with co-workers or family, you can better protect your device and sensitive information by setting up separate users to keep your administrative permissions and sensitive files protected.

---

## Remove Unneeded Accounts

[Learn how to delete unneeded accounts](https://support.apple.com/en-gw/guide/mac-help/mchlp1557/mac)

> **Why this matters:** If you don't intend for someone else to access your device, it is better to not leave that additional "door" open on your machine (this is called "reducing your attack surface"). Checking what user accounts are associated with your device could also reveal accounts that have been created without your knowledge.

---

## Secure the Accounts Connected with Your Device

- Review [Apple's checklist to protect your Apple ID and password](https://support.apple.com/en-us/102614)
- Set a [strong password](https://securityinabox.org/en/passwords/passwords/)
- [Enable 2-factor authentication](https://support.apple.com/en-us/102660)
- Do not share your Apple ID account with anyone
- [Check your device list](https://support.apple.com/en-us/102649) to see which devices are connected to your Apple ID account
- Take a [screenshot](https://support.apple.com/en-us/102646) of results showing suspicious activity
- Follow the [steps suggested by Apple if you think your Apple ID has been compromised](https://support.apple.com/en-us/102560)
- Consider turning on [Advanced Data Protection for iCloud](https://support.apple.com/en-us/108756) to enable end-to-end encryption

> **Why this matters:** Most devices have accounts associated with them. More than one device may be logged in at a time. If someone else has access to your accounts without your authorization, these steps will help you see and stop this.

---

## Protect Your Account with a Strong Passphrase

- Use a [long passphrase](https://securityinabox.org/en/passwords/passwords) (longer than 16 characters), not a short password
- Disable [automatic login](https://support.apple.com/en-us/102316)
- [Learn how to change the login password on Mac](https://support.apple.com/en-vn/guide/mac-help/mchlp1550/14.0/mac/14.0)
- Make sure that [FileVault is turned on](https://support.apple.com/en-vn/guide/mac-help/mh11785/mac)
- **Do not use TouchID** to log in to your Mac computer unless you have a disability which makes typing impossible

> **Why this matters:** Your device may be confiscated or stolen, which may allow someone to break into it. A strong passphrase prevents someone from accessing your machine just by turning it on and guessing a short password. If you are arrested, detained, or searched, you might easily be forced to unlock your device with your fingerprint. Someone who has dusted for your fingerprints can make a fake version of your finger to unlock your device.

---

## Set Your Screen to Sleep and Lock

- [Set your screen to lock a short time after you stop using it (5 minutes is good)](https://support.apple.com/en-in/guide/mac-help/mh11784/mac)
- [Require a password when the computer wakes from sleep or the screensaver activates](https://support.apple.com/en-in/guide/mac-help/mchlp2270/mac)

---

## Control What Can Be Seen When Locked

- Learn how to pause notifications when the device is sleeping or the screen is locked in the [guide on how to change notifications settings on Mac](https://support.apple.com/en-in/guide/mac-help/mh40583/mac)
- [Use Control Centre to turn on a Focus, for example Do Not Disturb](https://support.apple.com/en-in/guide/mac-help/mchl999b7c1a/14.0/mac/14.0)
- [Turn off notifications just for specific apps or websites](https://support.apple.com/en-in/guide/mac-help/mchl39cc046c/mac)

> **Why this matters:** A strong screen lock will give you some protection if your device is stolen or seized—but if you don't turn off notifications that show up on your lock screen, whoever has your device can see information that might leak when your contacts send you messages or you get new email.

---

## Disable Voice Controls

- [Learn how to turn off Siri](https://support.apple.com/en-in/guide/mac-help/mchl6b029310/mac#mchl9bf44710)
- [Delete Siri requests and dictation history on Mac](https://support.apple.com/en-gb/guide/mac-help/mchlf55961c0/mac)
- If you must use voice control, follow the [Security Planner instructions to do so more safely](https://securityplanner.consumerreports.org/tool/secure-your-smart-speaker)

> **Why this matters:** If you set up a device so you can speak to it to control it, it becomes possible for someone else to install code on your device that could capture what your device is listening to. If you have a disability that makes it difficult for you to type, you may find voice control necessary—but otherwise, it is much safer to turn it off.

---

## Use a Physical Privacy Filter

[See the Security Planner guide on privacy filters](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen)

> **Why this matters:** Some human rights defenders have had their information stolen or their accounts compromised when someone looked over their shoulder at their screen or used a security camera to do so. A privacy filter makes this kind of attack, often called shoulder surfing, less likely to succeed.

---

## Use a Camera Cover

1. Figure out whether and where your device has cameras (your computer might have more than one)
2. Create a low-tech camera cover: apply a small adhesive bandage on your camera and peel it off when you need to use the camera (a bandage works better than a sticker because the middle part has no adhesive)
3. Alternatively, search for "webcam privacy cover thin slide" for your device model
4. [Disable your camera for specific apps](https://support.apple.com/en-ie/guide/mac-help/mchlf6d108da/mac)
5. To disable the built-in camera altogether: go to **Settings > Screen Time > Content & Privacy**, enable the Content & Privacy toggle, click App Restrictions, turn off the Allow Camera toggle, and click Done. [Learn more](https://support.apple.com/en-ie/guide/mac-help/mchl3a19a9e7/14.0/mac/14.0)

> **Why this matters:** Malicious software may turn on the camera on your device in order to spy on you and the people around you, or to find out where you are, without you knowing it.

---

## Turn Off Connectivity You're Not Using

- Completely power off your computer at night
- Keep wifi, Bluetooth, and/or network sharing off and only enable them when needed
- [View this guide to understanding wifi menu icons on Mac](https://support.apple.com/guide/mac-help/wi-fi-menu-icons-on-mac-mchlcedc581e/mac)
- [Ensure the "Internet Sharing" checkbox is un-checked](https://support.apple.com/guide/mac-help/share-internet-connection-mac-network-users-mchlp1540/14.0/mac/14.0)

> **Why this matters:** All wireless communication channels could be abused by attackers around us who may try to get to our devices by exploiting weak spots in these networks. When you turn Bluetooth or wifi on, your device tries to look for any device or network it remembers. Someone snooping nearby can use this to identify your device, making it easy for someone to target you.

---

## Clear Your Saved Wifi Networks

- Save network names and passwords in your [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of in your device's list of networks
- If you do save networks, make sure to remove them when no longer needed

> **Why this matters:** Erasing wifi networks your device has saved and telling your device not to remember networks makes it harder for someone to identify and target your device.

---

## Turn Off Sharing You're Not Using

- [Turn AirDrop off](https://support.apple.com/guide/mac-help/airdrop-mac-send-files-devices-mh35868/mac#mchl3aad4788)
- [Review Sharing settings on Mac](https://support.apple.com/guide/mac-help/change-sharing-settings-mchl26e04309/mac) and un-check services you are not using

> **Why this matters:** If you leave sharing features on when you are not using them, malicious people may exploit them to get at files on your device.

---

## Use a Firewall

- [Learn how to block connections to your Mac with a firewall](https://support.apple.com/guide/mac-help/block-connections-to-your-mac-with-a-firewall-mh34041/mac)
- Enable "stealth" mode to keep your computer more secure. See [macOS official documentation on the stealth mode](https://support.apple.com/en-jo/guide/mac-help/mh17133/mac)

> **Why this matters:** Firewalls