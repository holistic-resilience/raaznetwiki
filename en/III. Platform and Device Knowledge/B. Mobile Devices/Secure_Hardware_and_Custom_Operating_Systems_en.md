---
title: "Secure Hardware and Custom Operating Systems"
tags:
  [
    mobile-security,
    hardware,
    grapheneos,
    android,
    custom-rom,
    iran-security,
    verified-boot,
  ]
category: "Platform and Device Knowledge"
difficulty: "Advanced"
audience: [Activists, Journalists, High-Risk Users, Privacy-Conscious Citizens]
topics:
  [
    "Secure Hardware",
    "De-Googled Android",
    "GrapheneOS",
    "Anti-Forensics",
    "Sanction Circumvention",
  ]
summary: "A comprehensive guide to selecting secure mobile hardware and installing privacy-focused operating systems like GrapheneOS, tailored for the Iranian threat landscape."
source: "Raaznet Aggregated Resources"
content_type: "Wiki Article"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic technical literacy",
    "Ability to obtain specific hardware (Pixel)",
    "Understanding of Android flashing",
  ]
estimated_read_time: "15 minutes"
last_updated: "2026-02-18"
---

# Secure Hardware and Custom Operating Systems

ُtandard commercial smartphones often fail to provide adequate protection. Manufacturers like Samsung, Xiaomi, and Apple design devices for convenience and data collection, not for resistance against forensic extraction or targeted espionage.

This guide focuses on **hardening the physical layer** of your mobile security by selecting the right hardware and replacing the stock operating system with a secure, privacy-respecting alternative.

## 1. Hardware Selection: The Foundation

Software security relies entirely on hardware integrity. If the hardware is compromised or insecure, no operating system can fully protect you.

### Recommended Device: Google Pixel

Despite the irony of recommending a Google product for privacy, **Google Pixel** phones (specifically Pixel 6 and newer) are currently the only devices that meet the strict hardware security requirements for a truly secure setup.

- **Titan M2 Security Chip:** A dedicated hardware component that handles encryption keys and verified boot. It isolates your most sensitive data (like your passcode) from the main processor, making it extremely difficult for forensic tools (like Cellebrite used by Iranian authorities) to brute-force your password.
- **Verified Boot with Custom Keys:** Unlike other brands, Pixels allow you to lock the bootloader with _custom_ cryptographic keys. This ensures that only your trusted operating system (e.g., GrapheneOS) can run on the device. If an attacker tries to tamper with the OS, the phone will refuse to boot.
- **Hardware Microphone/Camera Kill Switches:** Not physical switches, but deep hardware-level software toggles in Android 12+ (enhanced by GrapheneOS) allow you to completely cut power to sensors.

### Hardware to Avoid

- **Samsung/Xiaomi/Huawei:** These manufacturers often make it difficult or impossible to re-lock the bootloader after installing a custom OS. An unlocked bootloader is a major security risk; if your phone is seized, an attacker can easily flash malicious software onto it.
- **Motorola:** As of late 2024/early 2025, reports indicate a ban or restrictions on Motorola devices in Iran due to security concerns following hardware-based attacks in the region. Avoid these devices to prevent unnecessary scrutiny or confiscation.
- **Carrier-Locked Phones:** Never buy a phone locked to a specific carrier (e.g., AT&T, T-Mobile imports). They cannot be modified.

### Iranian Context: Acquisition and The "Hamta" Registry

Acquiring a Pixel in Iran presents challenges:

1.  **Availability:** Google does not officially sell in Iran. You must rely on the "grey market" or personal imports.
2.  **Hamta Registry (Design considerations):** Iran's mobile registry scheme links your device's IMEI to your passport and national ID. This destroys anonymity.
    - **Mitigation:** Consider using your secure device as a **"Wi-Fi Only"** device. Do not insert a SIM card. Instead, use a cheap portable 4G modem (MiFi) for internet access. If the MiFi is seized or tracked, your secure phone (containing your data) remains hardware-decoupled from the SIM identity.

---

## 2. Custom Operating Systems

Replacing the stock Android OS removes the "surveillance capitalism" layer (Google Play Services) and hardens the device against forensic attacks.

### Top Recommendation: GrapheneOS

**GrapheneOS** is a hardened, privacy-focused mobile OS compatible _only_ with Google Pixel phones. It is widely considered the gold standard for high-risk mobile security.

#### Why GrapheneOS for Iranian Users?

- **De-Googling & Sanction Evasion:** By default, GrapheneOS does not include Google Play Services.
  - _Benefit:_ You avoid US sanctions that often block Iranian IPs from accessing Google services ("Error 403").
  - _Benefit:_ You eliminate the constant telemetry data sent to Google servers, which could potentially be intercepted or subpoenaed.
- **Sandboxed Play Services:** If you absolutely need an app that requires Google (e.g., for specific push notifications), GrapheneOS allows you to install Google Play Services as a standard, unprivileged app. It runs in a "sandbox" and cannot access your files or location unless you explicitly permit it.
- **Hardened Security:**
  - **Auto-Reboot:** You can set the phone to automatically reboot after a specific period of inactivity (e.g., 1 hour). A rebooted phone is in "Before First Unlock" (BFU) state, where encryption keys are evicted from memory, making forensic extraction nearly impossible.
  - **PIN Scrambling:** Moves the keypad numbers to random positions to prevent attackers from guessing your PIN based on fingerprint smudges on the screen.
  - **Duress Password:** You can set a specific "fake" PIN that, if entered, can wipe the device or open a dummy profile (though relying on this under physical threat carries extreme risks).

### Alternative: DivestOS

If you cannot afford a Pixel or already own a supported device (like an older OnePlus or Fairphone), **DivestOS** is a solid alternative.

- **Pros:** Removes proprietary blobs, supports older hardware, focuses on debloating.
- **Cons:** Security is lower than GrapheneOS (often cannot re-lock bootloader on non-Pixel devices).
- **Use Case:** repurposing an old phone as a dedicated, offline media viewer or single-purpose secure device.

> **Warning:** Avoid standard "Custom ROMs" like **LineageOS** for high-security needs. While good for privacy from Google, they often require an unlocked bootloader and run in "userdebug" mode, which weakens the device's physical security against police extraction tools.

---

## 3. Implementation Strategy

### Step 1: Procurement

- Buy a **Google Pixel 6a, 7, or 8** (series). "a" series are cheaper and offer identical security features.
- Ideally, buy with cash or cryptocurrency. If buying in Iran, try to avoid linking the purchase to your primary identity if possible.

### Step 2: Installation

- **GrapheneOS Web Installer:** The installation process is now accessible via a web browser (Chrome/Edge/Brave). You do not need command-line expertise.
- **Crucial Step:** Ensure you **re-lock the bootloader** at the end of the installation. The installer will prompt you to do this. This is what secures the Verified Boot chain.

### Step 3: Device Verification (Auditor App)

- GrapheneOS includes an app called **Auditor**. This app uses the Titan M2 chip to cryptographically verify that your operating system has not been tampered with.
- You can pair your device with another GrapheneOS phone or the Auditor web service to receive alerts if your OS is modified (e.g., via an "Evil Maid" attack while you were detained).

### Step 4: App Ecosystem (The "De-Googled" Life)

Without the Google Play Store, you need alternative ways to get apps.

- **Obtainium:** Recommended. Downloads apps directly from the developer's GitHub/GitLab releases. Keeps them updated automatically. Best for open-source tools (Signal, Tor Browser, etc.).
- **Aurora Store:** An anonymous client for the Google Play Store. Allows you to download mainstream apps without signing into a Google account.
  - _Note:_ Use a VPN or Tor when using Aurora Store to hide your Iranian IP from Google.
- **F-Droid:** A repository of free and open-source software (FOSS). Use the **F-Droid Basic** client for better security and faster updates.

## 4. Threat Model: Physical Seizure & Interrogation

In Iran, the likelihood of a phone being physically inspected by Basij or security forces at checkpoints is high.

- **Separate Profiles:** GrapheneOS supports user profiles. You can have a "Decoy" profile that looks normal (boring photos, standard apps) and a "Hidden" profile for your sensitive work.
  - _Risk:_ Forensic tools can detect the existence of multiple profiles. This strategy works better against casual inspection (street checkpoint) than a full forensic lab analysis.
- **The "Kill Switch" (Auto-Reboot):** Set your auto-reboot timer aggressively (e.g., 10-30 minutes). If your phone is taken from you while unlocked, it will reboot itself shortly, returning to a fully encrypted state that is much harder to crack.
- **Power Off Immediately:** If you are in a situation where arrest is imminent, fully power off the device. Do not just lock the screen.

## Summary Checklist

- [ ] **Hardware:** Google Pixel 6 or newer.
- [ ] **OS:** GrapheneOS installed and bootloader LOCKED.
- [ ] **Connectivity:** Wi-Fi only (preferred) or data-only SIM in a separate MiFi router.
- [ ] **Apps:** Installed via Obtainium or Aurora Store (No Google Account signed in).
- [ ] **Config:** Auto-reboot timer set; Wi-Fi/Bluetooth auto-timeout enabled.
- [ ] **Verification:** Auditor app configured.

---

**Related Articles:**

- [Advanced_Mobile_Threats_and_Countermeasures](advanced-mobile-threats-and-countermeasures)
- [Android_Security_and_Hardening](android-security-and-hardening)
- [Privacy_Focused_Mobile_Apps_and_Stores](privacy-focused-mobile-apps-and-stores)
