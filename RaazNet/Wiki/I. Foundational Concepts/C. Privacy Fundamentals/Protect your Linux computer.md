---
title: "Protect Your Linux Computer"
tags: [linux, security, privacy, ubuntu, system-hardening, digital-security]
category: "Operating System Security"
difficulty: "Intermediate"
audience: [Linux Users, Privacy-Conscious Users, Activists, IT Administrators]
topics: ["Linux Security", "Ubuntu", "System Hardening", "Privacy Protection"]
summary: "Comprehensive security guide for Ubuntu Linux covering system updates, app management, user accounts, encryption, and privacy settings."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Linux/Ubuntu familiarity", "Understanding of system settings"]
estimated_read_time: "15 minutes"
---

# Protect Your Linux Computer

*Updated 13 June 2024*

If you use Linux, you may have heard the myth that it is more secure than Windows. This is not necessarily true. Security depends on a combination of how we use our devices and their software, which can have vulnerabilities discovered at any time. While most malware targets more widespread operating systems like Windows or Android, you can still encounter malware as a Linux user—for example, by clicking an infected link or opening a malicious attachment.

This guide specifically covers **Ubuntu Linux**. If you use another Linux distribution, the concepts apply but specific steps may differ.

---

## Table of Contents

- [Setting Up a New Linux Installation](#setting-up-a-new-linux-installation)
- [Keep Your System Updated](#keep-your-system-updated)
- [Manage Applications Securely](#manage-applications-securely)
- [User Account Security](#user-account-security)
- [Screen Lock and Physical Security](#screen-lock-and-physical-security)
- [Location and Privacy Settings](#location-and-privacy-settings)
- [Network and Connectivity Security](#network-and-connectivity-security)
- [Additional Resources](#additional-resources)

---

## Setting Up a New Linux Installation

When installing Ubuntu fresh:

1. Follow the [official Ubuntu installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
2. **Enable full-disk encryption** by selecting "Erase disk and install Ubuntu" and checking "Use LVM and encryption" in Advanced features during disk setup
3. Choose a [strong disk passphrase](https://securityinabox.org/en/passwords/passwords) when prompted
4. When [creating login details](https://ubuntu.com/tutorials/install-ubuntu-desktop#7-create-your-login-details), set a strong passphrase and keep "Require my password to log in" enabled

> **Why this matters:** Your device may be confiscated or stolen. Strong encryption and passphrases prevent unauthorized access to your data.

---

## Keep Your System Updated

### Operating System Updates

- Update from a trusted location (home or office), not public wifi
- Set aside time for updates—they may require downloads and restarts
- Check for additional updates after each round until none remain
- Always restart when prompted after updates complete

**Steps:**
1. [Check which Ubuntu version you have](https://help.ubuntu.com/community/CheckingYourUbuntuVersion)
2. [Find the latest available version](https://wiki.ubuntu.com/Releases)
3. Verify your hardware meets [minimum system requirements](https://help.ubuntu.com/community/Installation/SystemRequirements#Recommended_Minimum_System_Requirements)
4. [Upgrade Ubuntu](https://ubuntu.com/tutorials/upgrading-ubuntu-desktop#1-before-you-start)

### Application Updates

[Configure automatic package updates](https://help.gnome.org/users/gnome-packagekit/stable/prefs.html.en) to keep all installed software current.

> **Why this matters:** Vulnerabilities are discovered daily. Developers release patches to fix them, making updates essential for security.

---

## Manage Applications Securely

### Install from Trusted Sources

Use [Ubuntu Software](https://help.ubuntu.com/lts/ubuntu-help/addremove-install.html.en) for installing applications. Only install from repositories managed by distribution developers or directly from developer websites.

### Remove Unused Applications

[Remove applications](https://help.ubuntu.com/stable/ubuntu-help/addremove-remove) you don't need. Each installed app is a potential vulnerability.

### Review App Permissions

- Go to **Settings > Applications** and review each app's permissions
- [Review connected online accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts.html) (Google, Facebook, NextCloud)
- Check which [services they can access](https://help.ubuntu.com/stable/ubuntu-help/accounts-which-application.html)
- [Remove accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts-remove.html) you don't use

> **Why this matters:** Apps with access to sensitive information (location, microphone, camera) can leak data or be exploited by attackers.

---

## User Account Security

### Create Separate User Accounts

- Create one account with administrative privileges
- Create standard (non-admin) accounts for daily work
- [Manage user accounts](https://help.ubuntu.com/stable/ubuntu-help/user-accounts.html)
- [Manage administrative privileges](https://help.ubuntu.com/stable/ubuntu-help/user-admin-change.html)

### Remove Unnecessary Users

[Remove unneeded accounts](https://help.ubuntu.com/stable/ubuntu-help/user-delete.html) to reduce your attack surface. Check for accounts you didn't create.

### Use Strong Passphrases

- Use passphrases longer than 16 characters
- [Change your password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html) if needed

> **Why this matters:** Separate accounts protect sensitive information from other users. Strong passphrases prevent unauthorized access if your device is stolen.

---

## Screen Lock and Physical Security

### Configure Screen Lock

[Set your screen to lock](https://help.ubuntu.com/stable/ubuntu-help/privacy-screen-lock.html) after 1-5 minutes of inactivity.

**Important:** Avoid fingerprint or face unlock. These can be used against you under duress. A passphrase is the safest option.

### Hide Lock Screen Notifications

[Hide notifications on the lock screen](https://help.ubuntu.com/stable/ubuntu-help/shell-notifications.html#lock-screen-notifications) to prevent information leakage.

### Physical Privacy Measures

- **Privacy filter:** Use a screen privacy filter to prevent shoulder surfing. See the [Security Planner guide](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen)
- **Camera cover:** Use a sliding cover or small bandage over your webcam. Advanced users can [disable camera access entirely](https://askubuntu.com/questions/166809/how-can-i-disable-my-webcam)

---

## Location and Privacy Settings

[Turn off location services](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html) when not needed.

If you use Google Maps, regularly clear your location history:
- [Google Maps Timeline](https://support.google.com/accounts/answer/3118687#delete)
- [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location records can prove where you've been and who you've been near—information that could be used against you.

---

## Network and Connectivity Security

### Disable Unused Connections

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use [Airplane mode](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-airplane.html) to quickly disable all wireless connections
- [Turn off Bluetooth](https://help.ubuntu.com/stable/ubuntu-help/bluetooth-turn-on-off.html) when not needed
- Disable [wireless hotspot](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-adhoc.html.en) if enabled
- Turn off wifi in **Settings > Wi-Fi**

> **Why this matters:** When wifi or Bluetooth is on, your device broadcasts names of previously connected networks—creating a unique fingerprint that can identify you.

### Manage Saved Networks

- Store network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) rather than your device
- Regularly clear saved networks you no longer use

### Disable Unused Sharing

Turn off any sharing features you don't actively use:
- [File sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-personal.html)
- [Media sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-media.html)
- [Bluetooth sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-bluetooth.html)
- [Desktop sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-desktop.html)

### Enable a Firewall

[Use Gufw](https://help.ubuntu.com/community/Gufw) to manage your firewall. The default configuration provides adequate protection for most users.

> **Why this matters:** Firewalls monitor incoming and outgoing connections, blocking unauthorized access attempts. They can alert you to suspicious activity from malicious software.

---

## Additional Resources

- [Security in a Box: Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Linux Privacy Tips from Spread Privacy](https://spreadprivacy.com/linux-privacy-tips/)

---

*Get in the habit of checking these settings periodically to ensure nothing has changed.*