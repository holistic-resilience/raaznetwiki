---
title: "Choosing Your Hardware"
tags: [hardware-security, privacy, device-encryption, firmware, tpm, biometrics, network-security]
category: "Digital Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Security Practitioners]
topics: ["Hardware Security", "Device Selection", "Network Security", "Physical Security"]
summary: "Comprehensive guide to selecting and securing hardware for privacy, covering computers, security features, and network devices."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of encryption concepts"]
estimated_read_time: "12 minutes"
---

# Choosing Your Hardware

When it comes to discussions about privacy, hardware is often not thought about as much as what software we use. Your hardware should be considered the foundation on which you build the rest of your privacy setup.

## Picking a Computer

The internals of your devices process and store all of your digital data. It is important that all devices are supported by the manufacturer and developers by continuing to receive security updates.

### Hardware Security Programs

Different platforms offer varying levels of hardware security certification:

- **Windows Secured-core PCs** meet higher security criteria specified by Microsoft, including DMA protection and the ability to distrust Microsoft certificates—benefits available even to users of other operating systems
- **Android Ready SE** is a vendor collaboration ensuring devices follow best practices and include tamper-resistant hardware-backed storage for encryption keys
- **Apple SoC devices** running macOS leverage hardware security features that may not be available with third-party operating systems
- **ChromeOS on Chromebooks** provides optimal security by utilizing hardware features such as the hardware root-of-trust and verified boot

Even if you don't use these operating systems, participation in these programs indicates that manufacturers follow best practices for hardware security and updates.

### Preinstalled Operating Systems

New computers nearly always come with Windows preinstalled, unless you buy a Mac or a specialty Linux machine. It's usually a good idea to wipe the drive and install a fresh copy of your operating system of choice, even if that means just reinstalling Windows from scratch. Default Windows installations often come preloaded with bloatware, adware, or potentially malware due to agreements between hardware vendors and software vendors.

### Firmware Updates

Hardware often has security issues that are discovered and patched through firmware updates. Almost every component of your computer requires firmware to operate, from your motherboard to your storage devices.

**Automatic firmware management:**
- Apple devices, Chromebooks, most Android phones, and Microsoft Surface devices handle firmware updates automatically while supported

**Manual firmware management:**
- If you build your own PC, you may need to manually update your motherboard's firmware from your OEM's website
- Linux users can use the built-in `fwupd` tool to check for and apply firmware updates

### TPM and Secure Cryptoprocessors

Most computers and phones come equipped with a TPM (Trusted Platform Module) or similar secure cryptoprocessor which safely stores encryption keys and handles security-related functions. If your current machine lacks one, consider purchasing a newer computer with this feature. Some desktop and server motherboards have a "TPM header" that accepts a small accessory board containing the TPM.

> **Note:** Virtual TPMs are susceptible to side-channel attacks, and external TPMs are vulnerable to sniffing attacks when an attacker has physical access. The solution is including the secure processor inside the CPU itself, as with Apple's chips and Microsoft's Pluton processor.

### Biometrics

Many devices include fingerprint readers or face recognition capabilities. These can be convenient but aren't perfect.

**Key considerations:**
- Most devices fall back to a PIN or password when biometrics fail, so your security is still only as good as your password
- Biometrics can prevent shoulder-surfing attacks
- Most face authentication implementations require you to be looking at your phone from close range

**Disabling biometrics when needed:**
- **iOS:** Hold the side button and a volume button for 3 seconds to disable Face ID
- **Android:** Hold the power button and press Lockdown on the menu

> **Warning:** Android defines three security classes for biometrics. Check that your device is Class 3 before enabling biometrics.

### Device Encryption

If your device is encrypted, your data is most secure when the device is completely powered off—before you've entered your encryption key for the first time.

**Security states:**
- **Before First Unlock (BFU):** Higher security state before entering your password after power-on
- **After First Unlock (AFU):** Less secure against digital forensics toolkits and exploits

If you're concerned about an attacker with physical access to your device, consider turning it off fully whenever you aren't using it. Even AFU mode is effective against most threats when using a strong encryption key.

## External Hardware

Some threats can't be protected against by internal components alone. Evaluate whether these options are necessary for your threat model.

### Hardware Security Keys

Hardware keys use strong cryptography to authenticate you to devices or accounts. Because they cannot be copied, you can secure accounts so they can only be accessed with physical possession of the key, eliminating many remote attacks.

### Camera and Microphone Protection

**Camera protection options:**
- Camera blockers that physically prevent light from reaching the camera
- Devices without built-in cameras, using external cameras you can unplug
- Devices with built-in camera blockers or hardware switches

> **Warning:** Only buy covers that fit your laptop and won't cause damage when you close the lid. Covering the camera will interfere with automatic brightness and face authentication features.

**Microphone protection options:**
- Trust your OS's built-in permission controls
- Use devices without built-in microphones and external microphones you can unplug
- Some devices like MacBooks and iPads feature hardware microphone disconnect when the lid is closed
- Many computers have BIOS options to disable the camera and microphone entirely

### Privacy Screens

Privacy screens are films you can put over your display so the screen is only visible from certain angles. These are useful if your threat model includes others viewing your screen, but anyone could move to a different viewing angle.

### Dead Man's Switches

Dead man's switches stop machinery from operating without a human operator present. Applied to electronics, they can lock your device when you're not present.

**Options:**
- Some laptops can detect when you're present and lock automatically when you leave
- Cables like BusKill that lock or wipe your computer when disconnected

### Anti-Interdiction Protection

To prevent targeted attacks before a device is in your possession:
- Purchase devices in physical stores rather than ordering to your address
- Ensure your device supports secure boot/verified boot and enable it
- Avoid leaving your device unattended whenever possible

## Securing Your Network

### Compartmentalization

While virtual machines and sandboxing can separate activities on a computer, the best compartmentalization is physical separation. This is especially useful when software requires bypassing OS security features, such as anti-cheat software bundled with games.

**Recommendations:**
- Designate a separate machine for activities requiring security compromises
- Keep untrusted devices on a separate VLAN using a managed switch and capable router
- Use your router's "guest" network for IoT devices (smart fridge, thermostat, TV, etc.)

### Minimalism

The fewer devices connected to your network, the less potential attack surface and maintenance required. Consider inventorying every connected device in your home to help track what needs updates.

### Router Security

Your router handles all network traffic and acts as your first line of defense between you and the internet.

> **Note:** A lot of routers come with storage for file sharing across your network. We recommend not using networking devices for things other than networking—if your router is compromised, your files would also be compromised.

**Keeping routers updated:**
- Check your router's settings page (usually `192.168.1.1` or `192.168.0.1`) for automatic update options
- If automatic updates aren't supported, download updates manually from the manufacturer's site
- If your router is no longer supported by the manufacturer, check if it's supported by FOSS firmware
- Consider routers that come with FOSS firmware installed by default for longer support

**ISP router considerations:**
- Purchase a separate router and set your ISP router/modem into modem-only mode
- This allows continued security updates even when ISP-provided equipment is no longer updated
- Problems affecting your modem won't affect your router and vice versa