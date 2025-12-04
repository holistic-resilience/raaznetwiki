---
title: "Choosing Your Hardware for Privacy and Security"
tags: [hardware-security, privacy, device-encryption, firmware, network-security, threat-modeling]
category: "Hardware Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Practitioners, General Public]
topics: ["Hardware Security", "Device Selection", "Network Security", "Physical Security"]
summary: "Comprehensive guide to selecting and configuring hardware with privacy and security in mind, covering computers, external devices, and network equipment."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "12 minutes"
---

# Choosing Your Hardware for Privacy and Security

When discussing privacy, hardware is often overlooked in favor of software considerations. However, your hardware forms the foundation of your entire privacy setup and deserves careful attention.

## Selecting a Computer

Your devices process and store all your digital data. Ensuring they receive ongoing security updates from manufacturers and developers is essential.

### Hardware Security Programs

Several programs indicate manufacturers following security best practices:

- **Windows Secured-core PCs**: Meet Microsoft's higher security criteria, including [DMA protection](https://learn.microsoft.com/en-us/windows/security/information-protection/kernel-dma-protection-for-thunderbolt) and the ability to distrust Microsoft certificates—benefits available even to non-Windows users.

- **Android Ready SE**: A vendor collaboration ensuring devices follow [hardware best practices](https://source.android.com/docs/security/best-practices/hardware) with tamper-resistant storage for encryption keys.

- **Apple Silicon Macs**: Leverage [hardware security features](https://www.privacyguides.org/en/os/macos-overview/#hardware-security) unavailable with third-party operating systems.

- **Chromebooks**: Provide optimal [ChromeOS security](https://chromium.org/chromium-os/developer-library/reference/security/security-whitepaper) through hardware features like the [hardware root-of-trust](https://chromium.org/chromium-os/developer-library/reference/security/security-whitepaper/#hardware-root-of-trust-and-verified-boot).

Participation in these programs indicates good hardware security practices, regardless of which operating system you ultimately use.

### Preinstalled Operating Systems

New computers typically ship with Windows preinstalled. Consider wiping the drive and performing a fresh OS installation—even if reinstalling Windows—because default installations often include bloatware, [adware](https://bleepingcomputer.com/news/technology/lenovo-gets-a-slap-on-the-wrist-for-superfish-adware-scandal), or potentially [malware](https://zdnet.com/article/dell-poweredge-motherboards-ship-with-malware) from vendor agreements.

### Firmware Updates

Nearly every computer component requires firmware, from motherboard to storage devices. Security vulnerabilities are regularly discovered and patched through firmware updates.

**Managed devices** (Apple devices, Chromebooks, most Android phones, Microsoft Surface) handle firmware updates automatically while supported.

**Custom-built PCs** require manual motherboard firmware updates from the OEM's website. Linux users can use [`fwupd`](https://fwupd.org/) to check and apply available firmware updates.

### TPM and Secure Cryptoprocessors

Most modern computers and phones include a TPM (Trusted Platform Module) or similar secure cryptoprocessor for storing encryption keys and handling security functions. If your current device lacks this feature, consider upgrading. Some desktop motherboards accept TPM modules via a dedicated header.

> **Note**: Virtual TPMs are susceptible to side-channel attacks. External TPMs (separate from the CPU) are vulnerable to [sniffing attacks](https://pulsesecurity.co.nz/articles/TPM-sniffing) with physical access. Integrated solutions like Apple's chips and Microsoft's [Pluton](https://microsoft.com/en-us/security/blog/2020/11/17/meet-the-microsoft-pluton-processor-the-security-chip-designed-for-the-future-of-windows-pcs) processor address this by embedding the secure processor within the CPU.

### Biometrics

Fingerprint readers and facial recognition offer convenience but aren't infallible. When biometrics fail, devices fall back to PINs or passwords—meaning your security ultimately depends on password strength.

**Advantages**: Biometrics prevent shoulder-surfing attacks where someone watches you enter credentials.

**Face authentication safeguards**: Most implementations require you to be looking at the device from close range, preventing unauthorized unlock attempts.

**Emergency lockout options**:
- **iOS**: Hold side button + volume button for 3 seconds to disable Face ID
- **Android**: Hold power button and select "Lockdown"

> **Warning**: Android defines three [biometric security classes](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Verify your device is Class 3 before relying on biometrics.

### Device Encryption States

Encrypted devices are most secure when completely powered off—before you've entered your encryption key for the first time.

- **BFU (Before First Unlock)**: Maximum security state after power-on, before entering credentials
- **AFU (After First Unlock)**: Reduced security after initial authentication; more vulnerable to forensic tools and exploits

If physical device access is a concern, power off completely when not in use. While potentially impractical, even AFU mode protects against most threats when using a strong encryption key.

## External Hardware

Some threats require additional hardware solutions. Evaluate whether these apply to your specific threat model.

### Hardware Security Keys

These devices use strong cryptography for authentication and cannot be copied, ensuring accounts can only be accessed with physical possession of the key. This eliminates many remote attack vectors.

### Camera and Microphone Controls

**Camera protection options**:
- Physical camera blockers that prevent light from reaching the sensor
- Devices without built-in cameras, using external cameras you can disconnect
- Devices with built-in camera blockers or hardware disconnect switches

> **Warning**: Camera covers must fit properly to avoid damage when closing laptop lids. Covers will interfere with automatic brightness and face authentication.

**Microphone protection options**:
- Trust your OS's permission controls
- Use devices without built-in microphones with external, disconnectable microphones
- Some devices like [MacBooks and iPads](https://support.apple.com/guide/security/hardware-microphone-disconnect-secbbd20b00b/web) feature hardware microphone disconnects when the lid closes
- Many computers offer BIOS options to completely disable camera and microphone at the hardware level

### Privacy Screens

These films limit screen visibility to direct viewing angles, protecting against shoulder-surfing. However, they're not foolproof—someone can simply move to view from a different angle.

### Dead Man's Switches

These mechanisms lock or secure a device when the user isn't present:

- **Presence detection**: Some laptops can [detect user presence](https://support.microsoft.com/en-us/windows/managing-presence-sensing-settings-in-windows-11-82285c93-440c-4e15-9081-c9e38c1290bb) and lock automatically when you step away
- **Physical cables**: Devices like [BusKill](https://buskill.in/) lock or wipe your computer when disconnected

### Preventing Supply Chain Attacks

To reduce risk of targeted attacks before receiving a device:
- Purchase from physical retail stores rather than ordering to your address
- Ensure your device supports and has enabled secure boot/verified boot
- Avoid leaving devices unattended whenever possible

## Securing Your Network

### Physical Compartmentalization

While virtual machines and sandboxing provide software separation, physical separation offers the strongest compartmentalization—particularly useful when software requires bypassing OS security features (e.g., anti-cheat software in games).

**Practical implementation**:
- Designate separate machines for different purposes (e.g., a dedicated gaming machine)
- Use VLANs with managed switches and capable routers
- Enable "guest" networks on consumer routers for untrusted devices (IoT devices, smart appliances)

### Network Minimalism

Fewer connected devices mean less attack surface and easier maintenance. Inventory all connected devices in your home to track what needs updates.

### Router Security

Your router handles all network traffic and serves as your first line of defense.

> **Note**: Avoid using router storage features. If your router is compromised, stored files would be compromised as well.

**Key considerations**:

1. **Keep firmware updated**: Check router settings (typically at `192.168.1.1` or `192.168.0.1`) for automatic update options. If unavailable, manually download and apply updates from the manufacturer's site.

2. **Consider router lifespan**: Consumer routers often have limited support periods. Unsupported routers may work with [FOSS firmware](https://www.privacyguides.org/en/router/), or consider purchasing routers with FOSS firmware pre-installed for longer support.

3. **Separate router and modem**: If your ISP provides a combined device, purchasing a separate router and setting the ISP device to modem-only mode provides security benefits—you can receive router updates independently of ISP equipment support, and problems with one device won't affect the other.