---
title: "Android Security Hardening and Customization"
tags:
  [
    android,
    mobile-security,
    privacy,
    grapheneos,
    censorship-circumvention,
    device-hardening,
    iran-security,
  ]
category: "Platform and Device Knowledge"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, General Public]
topics:
  [
    "Mobile Operating Systems",
    "App Management",
    "System Hardening",
    "Surveillance Defense",
  ]
summary: "A comprehensive guide to securing Android devices, choosing privacy-focused operating systems like GrapheneOS, and hardening stock Android against surveillance and censorship in the Iranian context."
source: "Raaznet Wiki"
content_type: "Educational Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic Android familiarity",
    "Understanding of app permissions",
    "Access to device settings",
  ]
estimated_read_time: "20 minutes"
last_updated: "2026-02-17"
---

# Android Security Hardening and Customization

Android is the most widely used mobile operating system in Iran. While the core Android system (AOSP) is secure by design, most devices sold by manufacturers (Samsung, Xiaomi, etc.) come with invasive tracking, bloatware, and potential security vulnerabilities. For Iranian users facing state surveillance, internet censorship, and device confiscation risks, a standard Android setup is often insufficient.

This guide covers how to choose a secure operating system, harden your device against physical and remote attacks, and manage applications privately to bypass censorship and minimize data collection.

## 1. Operating System Choice

The foundation of your mobile security is the operating system itself. While stock Android receives security updates, it is deeply integrated with Google services and manufacturer telemetry.

### The Gold Standard: GrapheneOS

**GrapheneOS** is the recommended choice for high-risk users, including activists and journalists. It is a hardened version of Android that prioritizes privacy and security without sacrificing usability.

- **Device Support:** Exclusive to **Google Pixel** devices. This is because Pixels meet specific hardware security requirements (Titan M2 security chip, verified boot support for custom keys).
- **Key Features:**
  - **Sandboxed Google Play:** Runs Google services as regular apps without special system privileges. You get app compatibility (notifications, maps) without giving Google deep access to your device.
  - **Hardened Memory Allocator:** Makes it significantly harder for attackers to exploit memory corruption vulnerabilities.
  - **Network & Sensor Toggles:** Granular control to cut off network or sensor access for specific apps.
  - **Auto-Reboot:** Automatically reboots the device after a set period of inactivity, returning it to a fully encrypted "Before First Unlock" (BFU) state.

> **Note for Iranian Users:** While Pixel phones are less common than Samsung or Xiaomi in Iran, acquiring one for GrapheneOS provides the highest level of protection against state forensic tools and remote exploitation.

### Stock Android (Samsung, Xiaomi, etc.)

If you cannot use GrapheneOS, you must harden your stock Android device.

- **Avoid "Rooting":** Rooting your device breaks the Android security model (Verified Boot) and makes it easier for malware or forensic tools to compromise your system. **Do not root your phone** unless you have a specific, advanced technical requirement and understand the risks.
- **Updates are Critical:** Ensure your device is still receiving security updates. If your phone is "End-of-Life" (no longer supported), it is vulnerable to known exploits.
  - _Samsung:_ Offers up to 4-7 years of updates on newer models.
  - _Xiaomi/Other:_ Support windows vary; check manufacturer sites.

### A Note on Other Custom ROMs

- **LineageOS / /e/ OS:** While these remove Google services, they often weaken security by requiring unlocked bootloaders without verified boot support or by using "userdebug" builds. They are generally **not recommended** for high-security threat models compared to stock Android or GrapheneOS.

---

## 2. System Hardening & Configuration

Whether on GrapheneOS or Stock Android, these settings reduce your attack surface.

### Network Security & Censorship Circumvention

- **VPN Kill Switch:** Always use a trusted VPN (e.g., Mullvad, IVPN, or a self-hosted outline). Enable "Block connections without VPN" in Android settings to prevent traffic leaks if the VPN drops.
  - _Settings → Network & internet → VPN → (Gear Icon) → Block connections without VPN._
- **Private DNS:** Encrypt your DNS queries to bypass simple ISP censorship and DNS poisoning.
  - _Settings → Network & internet → Private DNS._ Use a provider that supports DoT (DNS over TLS).
- **Disable 2G:** 2G networks are insecure and easily intercepted (IMSI catchers). Android 12+ allows disabling 2G.
  - _Settings → Network & internet → SIMs → Allow 2G (Turn Off)._
- **Wi-Fi & Bluetooth:** Turn off when not in use to prevent tracking via MAC address or beacon probing. Disable "Auto-join" for public networks.

### Privacy & Permissions

- **Sensors:** Android 12+ allows you to completely disable the Microphone and Camera system-wide from the Quick Settings tiles. Use this before entering sensitive meetings or protests.
- **Location:**
  - Set permission to "While using the app" or "Ask every time."
  - Disable "Precise Location" for apps that don't need it (e.g., weather apps).
  - **Wi-Fi & Bluetooth Scanning:** Disable these in _Location Services_ settings to prevent location tracking even when GPS is off.
- **Advertising ID:** Delete your advertising ID to stop cross-app tracking.
  - _Settings → Privacy → Ads → Delete advertising ID._

### Isolation Features

- **Private Space (Android 15+):** A native feature to lock sensitive apps behind a separate biometric/PIN. Useful for hiding VPNs, secure messengers, or documentation apps during casual inspections.
- **User Profiles:** Create a secondary user profile for sensitive activities. Data is encrypted separately. In an emergency, you can end the session, putting that profile back into a strictly encrypted state.
  - _Settings → System → Multiple Users._
- **Work Profile (Shelter):** If you must use intrusive Iranian apps (e.g., banking, ride-sharing apps that require extensive permissions), install them inside a Work Profile using an app like **Shelter**. This isolates them from your main contacts and files. You can "freeze" the work profile when not in use.

---

## 3. App Management in Iran

Accessing the Google Play Store is often restricted in Iran due to sanctions or censorship. However, avoid third-party Iranian app stores (e.g., Cafe Bazaar, Myket) as they may host modified APKs or share user data with authorities.

### Recommended App Sources

1.  **Obtainium:**
    - _Best for:_ Direct updates from GitHub/GitLab.
    - _Why:_ Bypasses app store censorship entirely. You get the APK directly from the developer's release page. Ideal for Signal, Tor, and other censorship-circumvention tools.
2.  **Aurora Store:**
    - _Best for:_ Accessing Google Play Store apps anonymously.
    - _Why:_ No Google account required. It spoofs device info to bypass "This item is not available in your country" errors.
3.  **F-Droid (via Droid-ify or Neo Store clients):**
    - _Best for:_ Free and Open Source Software (FOSS).
    - _Why:_ Apps are auditable and generally privacy-respecting. Use the "Droid-ify" client for a better experience and faster updates than the official F-Droid app.

### Essential Privacy Apps

| Category      | Recommended App             | Notes                                                                                       |
| :------------ | :-------------------------- | :------------------------------------------------------------------------------------------ |
| **Browser**   | **Mull** or **Vanadium**    | Mull (hardened Firefox) or Vanadium (GrapheneOS Chrome). Install **uBlock Origin** on Mull. |
| **Messaging** | **Signal**                  | Enable "Registration Lock" and disappearing messages.                                       |
| **Keyboard**  | **HeliBoard**               | Open-source keyboard that does not log keystrokes or send data to the cloud.                |
| **Camera**    | **Secure Camera**           | Removes EXIF metadata (location, device model) from photos by default.                      |
| **2FA**       | **Aegis**                   | Open-source 2FA. **Avoid SMS 2FA** in Iran due to SIM swapping/interception risks.          |
| **Tor**       | **Orbot** / **Tor Browser** | For anonymous routing.                                                                      |

---

## 4. Physical Security & Device Integrity

### Encryption States: BFU vs. AFU

- **BFU (Before First Unlock):** When your phone is powered off or rebooted, it is in its most secure state. Encryption keys are not in memory.
- **AFU (After First Unlock):** Once you unlock your phone once, keys are loaded into memory. This makes the device more vulnerable to forensic tools (like Cellebrite) used by law enforcement.
- **Recommendation:** If you are in a high-risk situation (e.g., crossing a border, attending a protest), **power off your device completely**.

### Device Verification

- **Auditor App:** If you use GrapheneOS, use the **Auditor** app to verify that your operating system hasn't been tampered with or downgraded. It uses hardware-backed attestation to ensure device integrity.

### Panic Scenarios

- **Lockdown Mode:**
  - _Stock Android:_ Hold Power button → Tap "Lockdown". This disables biometrics (fingerprint/face) and notifications on the lock screen, forcing a PIN entry to unlock.
  - _iOS:_ Similar feature available; Android's implementation varies by version.
- **Auto-Wipe:** Configure your device to factory reset after a set number of failed password attempts (usually 15-30). This protects data if the device is seized and brute-forced.

## Summary Checklist for Iranian Users

1.  **Hardware:** Use a Google Pixel with GrapheneOS if possible. If not, use a supported Samsung/Android device with the latest updates.
2.  **App Sources:** Use Obtainium or Aurora Store. Avoid Cafe Bazaar.
3.  **Isolation:** Put domestic Iranian apps in a Shelter Work Profile or separate User Profile.
4.  **Network:** Always use a VPN with a Kill Switch. Disable 2G.
5.  **Physical:** Use a strong alphanumeric passphrase (not a pattern or short PIN). Power off device in high-risk zones.
