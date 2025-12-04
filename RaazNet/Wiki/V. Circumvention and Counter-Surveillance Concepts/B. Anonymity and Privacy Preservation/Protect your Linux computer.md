---
title: "Protect Your Linux Computer"
tags: [linux, security, privacy, ubuntu, system-hardening, digital-security]
category: "Device Security"
difficulty: "Intermediate"
audience: [Linux Users, Privacy-Conscious Users, IT Administrators]
topics: ["Operating System Security", "Privacy Protection", "System Hardening"]
summary: "Comprehensive security guide for Ubuntu Linux covering encryption, updates, app management, user accounts, and network security."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Linux/Ubuntu familiarity", "Understanding of system settings"]
estimated_read_time: "15 minutes"
---

# Protect Your Linux Computer

If you use Linux, you may have heard the myth that it is more secure than Windows. This is not necessarily true. Security depends on a combination of how you use your device and its software, which can have vulnerabilities discovered at any time. While most malware targets more widespread operating systems like Windows or Android, Linux users can still encounter malware by clicking infected links or opening malicious attachments.

Follow the steps in this guide to make your device more secure. Get in the habit of checking these settings periodically to ensure nothing has changed.

> **Note:** This guide specifically covers [Ubuntu Linux](https://ubuntu.com/desktop). If you use a different Linux distribution, the concepts apply but specific steps may vary—consult your distribution's documentation.

---

## Table of Contents

- [Initial Setup for New Linux Users](#initial-setup-for-new-linux-users)
- [Keep Your System Updated](#keep-your-system-updated)
- [App Management](#app-management)
- [User Account Security](#user-account-security)
- [Screen and Physical Security](#screen-and-physical-security)
- [Network and Connectivity](#network-and-connectivity)
- [Additional Resources](#additional-resources)

---

## Initial Setup for New Linux Users

If you're switching to Linux, take these security steps during installation:

1. **Follow the [official Ubuntu installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)**

2. **Enable full-disk encryption** during installation:
   - Choose "Erase disk and install Ubuntu"
   - In Advanced features, check "Use LVM and encryption"
   - Set a [strong disk passphrase](https://securityinabox.org/en/passwords/passwords) when prompted

3. **Create secure login credentials**:
   - Set a [strong passphrase](https://securityinabox.org/en/passwords/passwords)
   - Keep "Require my password to log in" enabled

> **Why this matters:** Your device may be confiscated or stolen, allowing someone to attempt breaking into it. Strong encryption and passphrases prevent unauthorized access even if someone has physical possession of your device.

---

## Keep Your System Updated

### Update Your Operating System

- Update from a trusted location (home or office), not public wifi
- Set aside time for updates—they may require downloads and restarts
- After updating, check again until no new updates appear
- Always restart when prompted after updates complete

**Steps:**
1. [Check which Ubuntu version you have](https://help.ubuntu.com/community/CheckingYourUbuntuVersion)
2. [Find the latest Ubuntu version](https://wiki.ubuntu.com/Releases)
3. Verify your hardware meets [minimum system requirements](https://help.ubuntu.com/community/Installation/SystemRequirements#Recommended_Minimum_System_Requirements)
4. [Upgrade Ubuntu](https://ubuntu.com/tutorials/upgrading-ubuntu-desktop#1-before-you-start)

### Enable Automatic App Updates

[Configure your system to update packages automatically](https://help.gnome.org/users/gnome-packagekit/stable/prefs.html.en).

> **Why this matters:** Vulnerabilities in code are discovered daily. Developers release patches to fix them, making regular updates essential for security.

---

## App Management

### Install Apps from Trusted Sources Only

Use [Ubuntu Software](https://help.ubuntu.com/lts/ubuntu-help/addremove-install.html.en) to install applications from repositories managed by distribution developers.

If you must install from elsewhere:
- Only download from official developer websites
- Avoid "mirror" download sites unless you trust the providers
- Plan to keep sensitive information off devices with untrusted apps

### Remove Unused Apps

[Remove applications](https://help.ubuntu.com/stable/ubuntu-help/addremove-remove) you don't need or use.

> **Why this matters:** Every installed app is a potential vulnerability. Unused apps may also transmit information about you without your knowledge.

### Review App Permissions and Connected Accounts

1. **Check app permissions:** Go to Settings > Applications and review each application
2. **Review connected accounts:** Check [online accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts.html) (Google, Facebook, NextCloud) and their [service access](https://help.ubuntu.com/stable/ubuntu-help/accounts-which-application.html)
3. [Remove accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts-remove.html) you don't use

> **Why this matters:** Apps with access to sensitive services (location, microphone, camera) can leak information or be exploited by attackers.

---

## User Account Security

### Create Separate User Accounts

- Create one account with administrative privileges
- Create standard (non-admin) accounts for daily use
- [Manage user accounts](https://help.ubuntu.com/stable/ubuntu-help/user-accounts.html)
- [Manage administrative privileges](https://help.ubuntu.com/stable/ubuntu-help/user-admin-change.html)

### Remove Unneeded Users

- [Delete unused accounts](https://help.ubuntu.com/stable/ubuntu-help/user-delete.html)
- Review accounts periodically to detect unauthorized additions

> **Why this matters:** Separate accounts protect sensitive information from other users and reduce your attack surface.

### Use Strong Passphrases

- Use passphrases longer than 16 characters
- [Change your password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html) if it's weak

---

## Screen and Physical Security

### Configure Screen Lock

- [Set your screen to lock](https://help.ubuntu.com/stable/ubuntu-help/privacy-screen-lock.html) after 1-5 minutes of inactivity
- **Avoid fingerprint or face unlock**—these can be forced from you; passphrases cannot

> **Why this matters:** Fingerprints can be faked, face unlock can be bypassed, and short passwords can be guessed. A long passphrase is the safest option.

### Control Lock Screen Notifications

[Hide lock screen notifications](https://help.ubuntu.com/stable/ubuntu-help/shell-notifications.html#lock-screen-notifications) to prevent information leakage when your device is locked.

### Physical Privacy Measures

- **Privacy filter:** Use a [physical privacy screen](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent shoulder surfing
- **Camera cover:** Use an adhesive bandage or sliding webcam cover on built-in cameras
- Advanced users can [disable camera access entirely](https://askubuntu.com/questions/166809/how-can-i-disable-my-webcam)

---

## Network and Connectivity

### Disable Unused Connections

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use [Airplane mode](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-airplane.html) for quick disconnection
- [Turn off Bluetooth](https://help.ubuntu.com/stable/ubuntu-help/bluetooth-turn-on-off.html) when not needed
- Disable [wireless hotspot](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-adhoc.html.en) if enabled
- Turn off wifi via Settings > Wi-Fi

> **Why this matters:** Active wireless connections can be exploited by nearby attackers. Your device broadcasts known network names, creating a unique fingerprint that can identify and target you.

### Manage Saved Wifi Networks

- Store network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of your device
- Regularly clear saved networks you no longer use

### Disable Unused Sharing Features

Check and disable if not needed:
- [File sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-personal.html)
- [Media sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-media.html)
- [Bluetooth sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-bluetooth.html)
- [Desktop sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-desktop.html)

### Use a Firewall

Install and configure [Gufw](https://help.ubuntu.com/community/Gufw) (graphical firewall interface).

> **Why this matters:** Firewalls monitor and control network connections, blocking unwanted access. They can detect when software unexpectedly tries to communicate or when malicious code attempts to "phone home."

### Manage Location Services

- [Turn off location services](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html) when not needed
- If using Google Maps, regularly clear your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location records can prove where you've been and who you've associated with, creating risks if your device is accessed by others.

---

## Additional Resources

- [Security in a Box: Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Linux Privacy Tips from Spread Privacy](https://spreadprivacy.com/linux-privacy-tips/)
- [How Security in a Box chooses recommended tools](https://securityinabox.org/en/about/how/#how-we-choose-the-tools-and-services-we-recommend)