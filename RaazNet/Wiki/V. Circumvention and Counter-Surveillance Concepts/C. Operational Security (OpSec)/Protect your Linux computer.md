```yaml
---
title: "Protect Your Linux Computer"
tags: [linux-security, privacy, ubuntu, device-protection, digital-security]
category: "Device Security"
difficulty: "Intermediate"
audience: [Linux Users, Privacy-Conscious Users, IT Administrators]
topics: ["Linux Security", "Privacy Protection", "System Hardening"]
summary: "Comprehensive security guide for Ubuntu Linux covering encryption, updates, permissions, connectivity, and privacy settings."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Linux/Ubuntu familiarity", "Understanding of system settings"]
estimated_read_time: "15 minutes"
---
```

# Protect Your Linux Computer

If you use Linux, you may have heard the myth that it is more secure than Windows. This is not necessarily true. Security depends on a combination of how we use our devices and their software, which can be found to have vulnerabilities at any time. While most malware targets more widespread operating systems like Windows or Android, you can still get malware as a Linux user if you click on an infected link or open a malicious attachment.

Follow the steps in this guide to make your device more secure. Get in the habit of checking these settings regularly to ensure nothing has changed.

> **Note:** This guide specifically covers [Ubuntu Linux](https://ubuntu.com/desktop). If you use another Linux distribution, you may need to look up comparable topics in your distribution's documentation.

---

## Initial Setup for New Linux Users

If you have just decided to switch to Linux:

1. [Follow the official Ubuntu installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
2. **Encrypt your device** by choosing "Erase disk and install Ubuntu" and checking "Use LVM and encryption" in Advanced features during disk setup
3. Choose a [strong disk passphrase](https://securityinabox.org/en/passwords/passwords) when prompted
4. When [creating your login details](https://ubuntu.com/tutorials/install-ubuntu-desktop#7-create-your-login-details), set a strong passphrase and keep "Require my password to log in" enabled

**Why this matters:** Your device may be confiscated or stolen, allowing someone to attempt to break into it. Strong passphrases for both disk encryption and your user account prevent unauthorized access.

---

## Keep Your System Updated

### Operating System Updates

- Update from a trusted location and internet connection (home or office, not public wifi)
- Set aside time for major updates—they may require downloads and restarts
- After updating, check for additional updates until none remain
- Always restart when prompted after updates complete

**Resources:**
- [Check available Ubuntu versions](https://wiki.ubuntu.com/Releases)
- [Check your current Ubuntu version](https://help.ubuntu.com/community/CheckingYourUbuntuVersion)
- [Upgrade Ubuntu](https://ubuntu.com/tutorials/upgrading-ubuntu-desktop#1-before-you-start)

### Application Updates

- [Enable automatic package updates](https://help.gnome.org/users/gnome-packagekit/stable/prefs.html.en)

**Why this matters:** New vulnerabilities are discovered daily. Developers release patches to fix them, making regular updates essential for security.

---

## Manage Your Applications

### Install Apps from Trusted Sources

- Use [Ubuntu Software](https://help.ubuntu.com/lts/ubuntu-help/addremove-install.html.en) for installing applications
- Only install from repositories managed by distribution developers
- If you must use apps from other sources, download only from official developer websites

### Remove Unnecessary Apps

- [Remove applications you don't use](https://help.ubuntu.com/stable/ubuntu-help/addremove-remove)

**Why this matters:** Unused apps may contain vulnerabilities and can transmit information about you. Removing them reduces your attack surface.

### Review App Permissions

- Go to **Settings > Applications** and review each app's permissions
- [Review connected online accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts.html) (Google, Facebook, NextCloud)
- Check which [services](https://help.ubuntu.com/stable/ubuntu-help/accounts-which-application.html) they can access
- [Remove unused accounts](https://help.ubuntu.com/stable/ubuntu-help/accounts-remove.html)

---

## User Account Security

### Create Separate User Accounts

- Create one account with admin privileges and others with standard privileges
- Use a standard user for day-to-day work
- [Manage user accounts](https://help.ubuntu.com/stable/ubuntu-help/user-accounts.html)
- [Manage administrative privileges](https://help.ubuntu.com/stable/ubuntu-help/user-admin-change.html)

### Remove Unneeded Users

- [Delete unused accounts](https://help.ubuntu.com/stable/ubuntu-help/user-delete.html)
- Audit who has administrative access

**Why this matters:** Separate accounts protect sensitive information if you share your device. Removing unused accounts reduces your attack surface.

### Use Strong Passphrases

- Use passphrases longer than 16 characters
- [Change your password](https://help.ubuntu.com/stable/ubuntu-help/user-changepassword.html)

---

## Screen and Physical Security

### Screen Lock Settings

- [Set your screen to lock quickly](https://help.ubuntu.com/stable/ubuntu-help/privacy-screen-lock.html) (1-5 minutes of inactivity)
- **Avoid fingerprint or face unlock**—these can be used against you by force

**Why this matters:** Long passphrases are the safest unlock method. Biometrics can be compelled or faked.

### Lock Screen Privacy

- [Hide notifications on the lock screen](https://help.ubuntu.com/stable/ubuntu-help/shell-notifications.html#lock-screen-notifications)

### Physical Privacy Measures

- **Privacy filter:** Use a screen privacy filter to prevent shoulder surfing. See the [Security Planner guide on privacy filters](https://securityplanner.consumerreports.org/tool/use-a-privacy-filter-screen)
- **Camera cover:** Use a small adhesive bandage or sliding webcam cover. Advanced users can [disable camera access entirely](https://askubuntu.com/questions/166809/how-can-i-disable-my-webcam)

---

## Location Privacy

- [Turn off location services](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html) when not needed
- If using Google Maps, regularly clear your [Timeline](https://support.google.com/accounts/answer/3118687#delete) and [Maps activity](https://support.google.com/maps/answer/3137804)

**Why this matters:** Location records can reveal where you've been and who you've associated with.

---

## Network and Connectivity Security

### Disable Unused Connections

- Power off devices completely at night
- Keep wifi, Bluetooth, and network sharing off when not in use
- [Enable Airplane mode](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-airplane.html) to quickly disable all wireless connections
- [Turn off Bluetooth](https://help.ubuntu.com/stable/ubuntu-help/bluetooth-turn-on-off.html) when not needed
- [Disable hotspot/tethering](https://help.ubuntu.com/stable/ubuntu-help/net-wireless-adhoc.html.en) when not in use
- Turn off wifi via **Settings > Wi-Fi**

**Why this matters:** Active wireless connections can be exploited by nearby attackers. Your device broadcasts the names of remembered networks, creating a unique fingerprint that can identify you.

### Manage Saved Networks

- Store network credentials in a [password manager](https://securityinabox.org/en/passwords/tools/#keepassxc) instead of on your device
- Regularly delete saved networks you no longer use

### Disable Unused Sharing Features

Check and disable if not needed:
- [File sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-personal.html)
- [Media sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-media.html)
- [Bluetooth sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-bluetooth.html)
- [Desktop sharing](https://help.ubuntu.com/stable/ubuntu-help/sharing-desktop.html)

### Enable a Firewall

- [Install and configure Gufw](https://help.ubuntu.com/community/Gufw)

**Why this matters:** Firewalls block unwanted connections to your device. They can also alert you when software attempts unexpected network communication. The default configuration provides adequate protection for most users.

---

## Additional Resources

- [Security in a Box: Malware Guide](https://securityinabox.org/en/phones-and-computers/malware)
- [Linux Privacy Tips from Spread Privacy](https://spreadprivacy.com/linux-privacy-tips/)