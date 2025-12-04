---
title: "Choosing Your Hardware for Privacy and Security"
tags: [hardware-security, privacy, device-encryption, firmware, threat-modeling, network-security]
category: "Hardware Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Practitioners, General Public]
topics: ["Hardware Security", "Device Selection", "Network Security", "Physical Security"]
summary: "Comprehensive guide to selecting and configuring hardware with privacy and security in mind, covering computers, firmware, encryption, and network devices."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of threat modeling concepts"]
estimated_read_time: "12 minutes"
---

# Choosing Your Hardware for Privacy and Security

When discussing privacy, hardware often receives less attention than software choices. However, your hardware forms the foundation of your entire privacy setup and deserves careful consideration.

## Selecting a Computer

Your devices process and store all your digital data. Ensuring they receive ongoing security updates from manufacturers and developers is essential.

### Hardware Security Programs

Several programs indicate manufacturers following security best practices:

- **Windows Secured-core PCs**: Meet Microsoft's higher security criteria, including [DMA protection](https://learn.microsoft.com/en-us/windows/security/information-protection/kernel-dma-protection-for-thunderbolt). These benefits extend to users of other operating systems.

- **Android Ready SE**: A vendor collaboration ensuring devices follow [hardware best practices](https://source.android.com/docs/security/best-practices/hardware) and include tamper-resistant storage for encryption keys.

- **Apple Silicon Macs**: Leverage [hardware security features](https://www.privacyguides.org/en/os/macos-overview/#hardware-security) that may not be available with third-party operating systems.

- **ChromeOS on Chromebooks**: Provides optimal [security](https://chromium.org/chromium-os/developer-library/reference/security/security-whitepaper) by utilizing hardware features like the [hardware root-of-trust](https://chromium.org/chromium-os/developer-library/reference/security/security-whitepaper/#hardware-root-of-trust-and-verified-boot).

Even if you don't use these operating systems, participation in these programs indicates the manufacturer follows hardware security best practices.

### Preinstalled Operating Systems

New computers typically come with Windows preinstalled. Consider wiping the drive and performing a fresh OS installation—even if reinstalling Windows. Default installations often include bloatware, [adware](https://bleepingcomputer.com/news/technology/lenovo-gets-a-slap-on-the-wrist-for-superfish-adware-scandal), or potentially [malware](https://zdnet.com/article/dell-poweredge-motherboards-ship-with-malware) due to vendor agreements.

### Firmware Updates

Hardware components require firmware to operate, and security vulnerabilities are regularly discovered and patched. Apple devices, Chromebooks, most Android phones, and Microsoft Surface devices handle firmware updates automatically while supported.

For custom-built PCs, manually update your motherboard firmware from the manufacturer's website. Linux users can use the [`fwupd`](https://fwupd.org/) tool to check for and apply available firmware updates.

### TPM and Secure Cryptoprocessors

Most modern computers and phones include a TPM (Trusted Platform Module) or similar secure cryptoprocessor that safely stores encryption keys and handles security functions. If your current device lacks one, consider upgrading. Some desktop motherboards include a "TPM header" for adding this capability.

> **Note**: Virtual TPMs are susceptible to side-channel attacks. External TPMs are vulnerable to [sniffing attacks](https://pulsesecurity.co.nz/articles/TPM-sniffing) when attackers have physical access. The most secure solution is a processor-integrated secure element, as found in Apple chips and Microsoft's [Pluton](https://microsoft.com/en-us/security/blog/2020/11/17/meet-the-microsoft-pluton-processor-the-security-chip-designed-for-the-future-of-windows-pcs).

### Biometrics

Fingerprint readers and facial recognition offer convenience but aren't perfect. Devices typically fall back to PIN or password authentication, meaning your security remains dependent on password strength.

Biometrics excel at preventing shoulder-surfing attacks. Modern face authentication implementations require direct gaze and close proximity, limiting unauthorized unlock attempts.

**Disabling biometrics when needed:**
- **iOS**: Hold the side button and a volume button for 3 seconds
- **Android**: Hold the power button and select "Lockdown"

> **Warning**: Android defines three [security classes](https://source.android.com/docs/security/features/biometric/measure#biometric-classes) for biometrics. Verify your device is Class 3 before enabling biometrics.

### Device Encryption States

Encrypted devices are most secure when completely powered off—before you've entered your encryption key for the first time. This state is called "Before First Unlock" (BFU). After entering your password post-reboot, the device enters "After First Unlock" (AFU) mode.

AFU is considerably less secure against digital forensics tools and exploits compared to BFU. If concerned about physical device access, power off completely when not in use. While potentially impractical, even AFU mode provides effective protection against most threats with a strong encryption key.

## External Hardware

Some threats require additional hardware solutions. Evaluate whether these options align with your threat model.

### Hardware Security Keys

These devices use strong cryptography for authentication and cannot be copied, requiring physical possession to access secured accounts. This eliminates many remote attack vectors.

### Camera and Microphone Protection

**Cameras:**
- Physical camera covers prevent light from reaching the sensor
- External cameras can be unplugged when not in use
- Some devices include built-in camera blockers or hardware disconnect switches
- Many BIOS settings allow disabling cameras entirely

> **Warning**: Ensure camera covers fit properly and won't damage your laptop when closed. Covering cameras interferes with automatic brightness and face authentication.

**Microphones:**
- OS permission controls are typically the primary protection
- Consider devices without built-in microphones, using external ones instead
- [MacBooks and iPads](https://support.apple.com/guide/security/hardware-microphone-disconnect-secbbd20b00b/web) feature hardware microphone disconnection when the lid closes
- BIOS options can disable microphones at the hardware level

### Privacy Screens

Privacy screen films limit viewing angles, preventing others from seeing your display. However, they aren't foolproof—someone can simply move to view from a different angle.

### Dead Man's Switches

These mechanisms lock or wipe devices when you're not present:

- Some laptops [detect presence](https://support.microsoft.com/en-us/windows/managing-presence-sensing-settings-in-windows-11-82285c93-440c-4e15-9081-c9e38c1290bb) and lock automatically when you leave
- Cables like [BusKill](https://buskill.in/) lock or wipe your computer when disconnected

### Anti-Interdiction Protection

To prevent targeted attacks before receiving a device:
- Purchase from physical retail stores rather than shipping to your address
- Enable secure boot/verified boot
- Avoid leaving devices unattended

## Securing Your Network

### Physical Compartmentalization

While virtual machines and sandboxing provide software separation, physical separation offers the strongest compartmentalization. This is especially useful when software requires bypassing OS security features, such as anti-cheat systems in games.

Consider designating separate machines for different purposes (e.g., a dedicated gaming machine) on separate VLANs. This requires a managed switch and router supporting segregated networks.

Most consumer routers support a separate "guest" network isolated from your main network—ideal for untrusted devices like IoT equipment (smart appliances, thermostats, TVs).

### Network Minimalism

Fewer connected devices mean reduced attack surface and less maintenance. Inventory all connected devices in your home to track what needs updates.

### Router Security

Your router handles all network traffic and serves as your first line of defense.

> **Note**: Avoid using router storage features for file sharing. If your router is compromised, stored files are also compromised.

**Key router considerations:**

1. **Keep firmware updated**: Check your router's admin page (typically `192.168.1.1` or `192.168.0.1`) for automatic update options

2. **Manual updates**: If automatic updates aren't available, regularly download and apply updates from the manufacturer

3. **End-of-support devices**: Check if [FOSS firmware](https://www.privacyguides.org/en/router/) supports your router, or purchase routers with FOSS firmware pre-installed for longer support

4. **Separate router and modem**: If your ISP provides a combined unit, consider purchasing a separate router and setting the ISP device to modem-only mode. This ensures continued security updates independent of ISP support and isolates problems between devices.