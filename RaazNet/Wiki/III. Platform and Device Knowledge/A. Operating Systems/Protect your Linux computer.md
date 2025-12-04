```yaml
---
title: "Protect Your Linux Computer"
tags: [linux, security, privacy, ubuntu, operating-system, digital-security]
category: "Device Security"
difficulty: "Intermediate"
audience: [Linux Users, Privacy-Conscious Users, Activists, IT Administrators]
topics: ["Linux Security", "Operating System Hardening", "Privacy Protection", "Ubuntu"]
summary: "Comprehensive security guide for Ubuntu Linux covering system updates, app management, user accounts, privacy settings, and network security."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Linux/Ubuntu familiarity", "Understanding of system settings navigation"]
estimated_read_time: "15 minutes"
related_guides: ["malware-protection", "password-security", "encryption-basics"]
last_updated: "2024-06-13"
---
```

# Protect Your Linux Computer

If you use Linux, you may have heard the myth that it is more secure than Windows. This is not necessarily true. Security depends on a combination of how you use your device and its software, which can have vulnerabilities discovered at any time. While most malware targets more widespread operating systems like Windows or Android, you can still encounter malware as a Linux user—for example, by clicking an infected link or opening a malicious attachment.

This guide covers **Ubuntu Linux** specifically. If you use another Linux distribution, the concepts apply but specific steps may differ—consult your distribution's documentation.

> **Tip:** Get in the habit of checking these settings periodically to ensure nothing has changed.

---

## Getting Started with Linux

If you're switching to Linux for the first time:

1. **Follow the [official Ubuntu installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)**
2. **Enable full disk encryption** during installation:
   - Choose "Erase disk and install Ubuntu"
   - Check "Use LVM and encryption" in Advanced features
   - Set a [strong disk passphrase](https://securityinabox.org/en/passwords/passwords)
3. **Create secure login credentials**:
   - Use a [strong passphrase](https://securityinabox.org/en/passwords/passwords)
   - Keep "Require my password to log in" enabled

> **Why this matters:** Your device could be confiscated or stolen. Strong encryption and passphrases prevent unauthorized access even if someone has physical possession of your computer.

---

## System Updates

### Keep Your Operating System Current

- Update from a trusted location (home or office), not public wifi
- Set aside time for major updates—they may require multiple restarts
- After updating, check again until no new updates appear
- Always restart when prompted after updates complete

**Steps:**
1. [Check the latest Ubuntu version available](https://wiki.ubuntu.com/Releases)
2. [Compare to your installed version](https://help.ubuntu.com/community/CheckingYourUbuntuVersion)
3. Verify your hardware meets [minimum system requirements](https://help.ubuntu.com/community/Installation/SystemRequirements#Recommended_Minimum_System_Requirements)
4. [Upgrade Ubuntu](https://ubuntu.com/tutorials/upgrading-ubuntu-desktop#1-before-you-start)

### Keep Apps Updated

[Configure automatic package updates](https://help.gnome.org/users/gnome-packagekit/stable/prefs.html.en) to ensure all software stays current.

> **Why this matters:** Vulnerabilities are discovered daily. Developers release patches to fix them, making updates essential for security.

---

## Application Management

### Install Apps from Trusted Sources

Use [Ubuntu Software](https://help.ubuntu.com/lts/ubuntu-help/addremove-install.html.en) for installing applications. Only install from repositories managed by distribution developers.

If you must use software from other sources:
- Download only from official developer websites
- Avoid "mirror" download sites unless you trust the providers
- Plan to keep sensitive information off devices with unverified software

### Remove Unused Apps

[Remove applications](https://help.ubuntu.com/stable/ubuntu-help/addremove-remove) you no longer need.

> **Why this matters:** Every installed app is a potential vulnerability. Unused apps may also transmit information about you without your knowledge.

### Review App Permissions

1. Go to **Settings > Applications**
2. Click each application to review its permissions
3. [Review connected online accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts.html) (Google, Facebook, NextCloud)
4. Check which [services](https://help.ubuntu.com/stable/ubuntu-help/accounts-which-application.html) they can [access](https://help.ubuntu.com/stable/ubuntu-help/accounts-disable-service.html)
5. [Remove accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts-remove.html) you don't use

---

## User Account Security

### Create Separate User Accounts

Set up multiple accounts with different privilege levels:
- One **administrator** account for system changes
- **Standard** accounts for daily work

**Resources:**
- [Manage user accounts](https://help.ubuntu.com/stable/ubuntu-help/user-accounts.html)
- [Manage administrative privileges](https://help.ubuntu.com/stable/ubuntu-help/user-admin-change.html)

> **Why this matters:** Separate accounts protect sensitive information if you share your device, and limit damage from compromised applications.

### Remove Unnecessary Users

- [Delete unneeded accounts](https://help.ubuntu.com/stable/ubuntu-help/user-delete.html)
- Review accounts periodically—unknown accounts may indicate compromise

### Use Strong Passphrases

- Use passphrases **longer than 16 characters**
- [Change your password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html) if it's currently weak

---

## Screen and Physical Security

### Configure Screen Lock

[Set your screen to lock](https://help.ubuntu.com/stable/ubuntu-help/privacy-screen-lock.html) after 1-5 minutes of inactivity.

> **Important:** Avoid fingerprint or face unlock. These can be used against you by force, and have been defeated by fake fingerprints and photos.

### Hide Lock Screen Notifications

[Configure lock screen notification settings](https://help.ubuntu.com/stable/ubuntu-help/shell-notifications.html#lock-screen-notifications) to prevent information leakage.

### Physical Privacy Measures

**Privacy filter:** Use a [privacy screen filter](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent "shoulder surfing"—when someone views your screen from the side.

**Camera cover:** 
- Locate all cameras (built-in and external)
- Use a small adhesive bandage (the non-sticky center won't damage the lens)
- Or purchase a sliding webcam cover
- Advanced users can [disable camera access entirely](https://askubuntu.com/questions/166809/how-can-i-disable-my-webcam)

---

## Privacy Settings

### Disable Location Services

1. [Turn off location services](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html)
2. If using Google Maps, clear your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location history can prove you were in certain places or with specific people—information that could be used against you.

---

## Network Security

### Disable Unused Connectivity

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use [Airplane mode](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-airplane.html) to quickly disable all wireless connections
- [Turn off Bluetooth](https://help.ubuntu.com/stable/ubuntu-help/bluetooth-turn-on-off.html) when not needed
- Disable [wireless hotspot](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-adhoc.html.en) sharing
- Turn off wifi via **Settings > Wi-Fi**

> **Why this matters:** When wifi or Bluetooth is on, your device broadcasts the names of networks and devices it has connected to before. This creates a unique fingerprint that can identify and track you.

### Manage Saved Wifi Networks

- Store network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of on your device
- Regularly delete saved networks you no longer use
- Disable automatic network discovery

### Disable Unused Sharing Features

Check and disable if not needed:
- [File sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-personal.html)
- [Media sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-media.html)
- [Bluetooth sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-bluetooth.html)
- [Desktop sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-desktop.html)

### Enable the Firewall

[Install and configure Gufw](https://help.ubuntu.com/community/Gufw) (graphical firewall interface).

> **Why this matters:** Firewalls monitor network connections and block unauthorized access. The default configuration provides adequate protection for most users, but it must be enabled.

---

## Additional Resources

- [Security in a Box: Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Linux Privacy Tips from Spread Privacy](https://spreadprivacy.com/linux-privacy-tips/)
- [How Security in a Box chooses recommended tools](https://securityinabox.org/en/about/how/#how-we-choose-the-tools-and-services-we-recommend)