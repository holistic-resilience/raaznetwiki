```yaml
---
title: "Protect Your Linux Computer"
tags: [linux, security, privacy, ubuntu, system-hardening, digital-safety]
category: "Operating System Security"
difficulty: "Intermediate"
audience: [Linux Users, Privacy-Conscious Users, Activists, IT Administrators]
topics: ["Linux Security", "System Hardening", "Privacy Protection", "Ubuntu"]
summary: "Comprehensive guide to securing Ubuntu Linux computers through system settings, app management, encryption, and privacy controls."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Linux/Ubuntu familiarity", "Understanding of encryption concepts"]
estimated_read_time: "15 minutes"
---
```

# Protect Your Linux Computer

If you use Linux, you may have heard the myth that it is more secure than Windows. This is not necessarily true. Security depends on a combination of how you use your device and the software itself, which can be found to have vulnerabilities at any time. While most malware targets more widespread operating systems like Windows or Android, you can still get malware as a Linux user if you click on an infected link or open a malicious attachment.

Follow the steps in this guide to make your device more secure. Get in the habit of checking these settings regularly to ensure nothing has changed.

> **Note:** This guide specifically covers [Ubuntu Linux](https://ubuntu.com/desktop). If you use another Linux distribution, the concepts apply but specific steps may differ—consult your distribution's documentation.

---

## Table of Contents

- [Initial Setup for New Linux Users](#initial-setup-for-new-linux-users)
- [System Updates](#system-updates)
- [Application Management](#application-management)
- [User Account Security](#user-account-security)
- [Screen and Physical Security](#screen-and-physical-security)
- [Network and Connectivity](#network-and-connectivity)
- [Additional Resources](#additional-resources)

---

## Initial Setup for New Linux Users

If you're switching to Linux, take these essential security steps during installation:

1. **Follow the [official Ubuntu installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)**

2. **Enable full disk encryption** during installation:
   - Choose "Erase disk and install Ubuntu"
   - Check "Use LVM and encryption" in Advanced features during Disk setup
   - Set a [strong disk passphrase](https://securityinabox.org/en/passwords/passwords)

3. **Create secure login credentials**:
   - Set a [strong passphrase](https://securityinabox.org/en/passwords/passwords)
   - Keep "Require my password to log in" enabled

> **Why this matters:** Your device may be confiscated or stolen. Strong encryption and passphrases prevent unauthorized access even if someone has physical possession of your computer.

---

## System Updates

### Keep Your Operating System Current

- Update from a trusted location (home or office), not public wifi
- Set aside time for updates—they may require downloads and restarts
- After updating, check again for additional updates until none remain
- Always restart when prompted after updates complete

**Steps:**
1. [Check your current Ubuntu version](https://help.ubuntu.com/community/CheckingYourUbuntuVersion)
2. [Find the latest Ubuntu release](https://wiki.ubuntu.com/Releases)
3. Verify your hardware meets [minimum system requirements](https://help.ubuntu.com/community/Installation/SystemRequirements#Recommended_Minimum_System_Requirements)
4. [Upgrade Ubuntu](https://ubuntu.com/tutorials/upgrading-ubuntu-desktop#1-before-you-start)

### Enable Automatic App Updates

[Configure your system to update all packages automatically](https://help.gnome.org/users/gnome-packagekit/stable/prefs.html.en).

> **Why this matters:** Vulnerabilities are discovered daily. Developers release patches to fix them, making updates essential for security.

---

## Application Management

### Install Apps from Trusted Sources Only

Use [Ubuntu Software](https://help.ubuntu.com/lts/ubuntu-help/addremove-install.html.en) to install applications from official repositories.

If you must install software from elsewhere:
- Download only from official developer websites
- Avoid "mirror" download sites unless you trust the provider
- Consider keeping sensitive information off devices with third-party apps

### Remove Unused Applications

[Remove applications](https://help.ubuntu.com/stable/ubuntu-help/addremove-remove) you don't need or use.

> **Why this matters:** Each installed app is a potential vulnerability. Unused apps may also transmit data about you without your knowledge.

### Review App Permissions and Connected Accounts

1. **Check app permissions:** Go to Settings > Applications and review each application
2. **Review connected accounts:** Check [online accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts.html) (Google, Facebook, NextCloud) and their [service access](https://help.ubuntu.com/stable/ubuntu-help/accounts-which-application.html)
3. [Remove unused accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts-remove.html)

> **Why this matters:** Apps with access to your location, microphone, camera, or settings can leak information or be exploited by attackers.

---

## User Account Security

### Create Separate User Accounts

- Create one account with admin privileges and others with standard privileges
- Use a standard account for daily work
- [Manage user accounts](https://help.ubuntu.com/stable/ubuntu-help/user-accounts.html)
- [Manage administrative privileges](https://help.ubuntu.com/stable/ubuntu-help/user-admin-change.html)

### Remove Unneeded Users

- [Delete unused accounts](https://help.ubuntu.com/stable/ubuntu-help/user-delete.html)
- Check for accounts created without your knowledge

> **Why this matters:** Each user account is a potential entry point. Removing unused accounts reduces your attack surface.

### Use a Strong Passphrase

- Use a passphrase longer than 16 characters
- [Change your password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html) if needed

---

## Screen and Physical Security

### Configure Screen Lock

[Set your screen to lock](https://help.ubuntu.com/stable/ubuntu-help/privacy-screen-lock.html) after 1-5 minutes of inactivity.

> **Important:** Avoid fingerprint or face unlock. These can be used against you by force. A long passphrase is the safest option.

### Control Lock Screen Notifications

[Hide lock screen notifications](https://help.ubuntu.com/stable/ubuntu-help/shell-notifications.html#lock-screen-notifications) to prevent information leakage when your device is locked.

### Physical Privacy Measures

**Privacy filter:** Use a [privacy screen filter](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen) to prevent "shoulder surfing."

**Camera cover:** 
- Use a small adhesive bandage (the non-sticky center won't damage your lens)
- Or purchase a sliding webcam cover
- Advanced users can [disable camera access entirely](https://askubuntu.com/questions/166809/how-can-i-disable-my-webcam)

---

## Network and Connectivity

### Disable Unused Connections

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- Use [Airplane mode](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-airplane.html) for quick disconnection
- [Turn off Bluetooth](https://help.ubuntu.com/stable/ubuntu-help/bluetooth-turn-on-off.html) when not needed
- Disable [wireless hotspot](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-adhoc.html.en) if enabled
- Turn off wifi in Settings > Wi-Fi

> **Why this matters:** When Bluetooth or wifi is on, your device broadcasts the names of networks and devices it has connected to before. This creates a unique fingerprint that can identify and target your device.

### Manage Saved Wifi Networks

- Store network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of your device
- Regularly clear saved networks you no longer use

### Turn Off Sharing Services

Disable these if enabled:
- [File sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-personal.html)
- [Media sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-media.html)
- [Bluetooth sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-bluetooth.html)
- [Desktop sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-desktop.html)

### Enable a Firewall

[Use Gufw](https://help.ubuntu.com/community/Gufw) to manage your firewall. The default configuration provides adequate protection for most users.

> **Why this matters:** A firewall acts as a security guard, inspecting and controlling network connections. It can stop unwanted connections and alert you to suspicious outgoing traffic.

### Disable Location Services

- [Turn location services off](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html)
- If using Google Maps, clear your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

> **Why this matters:** Location records can prove where you've been and who you've associated with.

---

## Additional Resources

- [Security in a Box: Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Linux Privacy Tips from Spread Privacy](https://spreadprivacy.com/linux-privacy-tips/)
- [How Security in a Box Chooses Recommended Tools](https://securityinabox.org/en/about/how/#how-we-choose-the-tools-and-services-we-recommend)