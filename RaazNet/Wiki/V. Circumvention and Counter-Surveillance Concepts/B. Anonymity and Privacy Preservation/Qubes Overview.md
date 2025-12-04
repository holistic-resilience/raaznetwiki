```yaml
---
title: "Qubes OS Overview"
tags: [qubes-os, virtualization, compartmentalization, xen, security-hardening]
category: "Operating Systems"
difficulty: "Intermediate"
audience: [Security Professionals, Privacy-Conscious Users, Activists, Journalists]
topics: ["Desktop Security", "Virtualization", "Threat Modeling", "Isolation"]
summary: "Introduction to Qubes OS, a security-focused operating system using Xen hypervisor compartmentalization to isolate applications in separate virtual machines."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of operating systems", "Familiarity with virtualization concepts", "Understanding of threat modeling"]
estimated_read_time: "8 minutes"
---
```

# Qubes OS Overview

[**Qubes OS**](https://www.privacyguides.org/en/desktop/#qubes-os) is an open-source operating system that uses the [Xen](https://en.wikipedia.org/wiki/Xen) hypervisor to provide strong security for desktop computing through isolated *qubes* (virtual machines). You can assign each *qube* a level of trust based on its purpose. Qubes OS provides security by using isolation, only permitting actions on a per-case basis—the opposite of [badness enumeration](https://ranum.com/security/computer_security/editorials/dumb).

## How Qubes OS Works

Qubes uses [compartmentalization](https://qubes-os.org/intro) to keep the system secure. Qubes are created from templates, with defaults for Fedora, Debian, and [Whonix](https://www.privacyguides.org/en/desktop/#whonix). The system also supports once-use [disposable](https://qubes-os.org/doc/how-to-use-disposables) qubes for temporary tasks.

> **Note:** The term *qubes* is gradually replacing "virtual machines" in documentation. Qubes are not entire virtual machines but maintain similar functionalities.

![Qubes architecture](https://www.privacyguides.org/en/assets/img/qubes/qubes-trust-level-architecture.png)

Each qube has a [colored border](https://qubes-os.org/screenshots) to help you track which security domain it belongs to. For example, you might use one color for banking and another for general browsing.

![Colored border](https://www.privacyguides.org/en/assets/img/qubes/r4.0-xfce-three-domains-at-work.png)

## Why Use Qubes OS?

Qubes OS is valuable when your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/) requires strong security and isolation—particularly if you handle untrusted files from unknown sources. The core principle: if a single qube is compromised, it won't affect the rest of the system.

Qubes OS uses [dom0](https://wiki.xenproject.org/wiki/Dom0) (a Xen VM) to control other qubes on the host OS. All qubes display individual application windows within dom0's desktop environment.

## Key Operations

### Copying and Pasting Text

You can [copy and paste text](https://qubes-os.org/doc/how-to-copy-and-paste-text) between qubes using `qvm-copy-to-vm` or these steps:

1. **Ctrl+C** — Copy within the current qube
2. **Ctrl+Shift+C** — Transfer to global clipboard
3. **Ctrl+Shift+V** — Make available in destination qube
4. **Ctrl+V** — Paste in destination qube

### File Exchange

To copy files between qubes, use **Copy to Other AppVM...** or **Move to Other AppVM...**. The **Move** option deletes the original file. Both options protect your clipboard from leaking to other qubes.

This method is more secure than air-gapped file transfer because air-gapped computers must still parse partitions or file systems—the inter-qube copy system does not.

> **Important:** Qubes do not have persistent filesystems. You can create and delete files, but changes are ephemeral unless explicitly saved to a template or persistent storage.

### Inter-VM Communication

The [qrexec framework](https://qubes-os.org/doc/qrexec) enables secure communication between domains. Built on the Xen library *vchan*, it facilitates [isolation through policies](https://qubes-os.org/news/2020/06/22/new-qrexec-policy-system).

## Connecting to Tor via VPN

Privacy Guides [recommends](https://www.privacyguides.org/en/advanced/tor-overview/) connecting to Tor through a [VPN](https://www.privacyguides.org/en/vpn/). Qubes simplifies this with ProxyVMs and Whonix.

After [creating a ProxyVM](https://forum.qubes-os.org/t/configuring-a-proxyvm-vpn-gateway/19061) for your VPN, chain your Whonix qubes to it by setting the NetVM of your Whonix Gateway (`sys-whonix`) to the ProxyVM:

| Qube Name | Description | NetVM |
|-----------|-------------|-------|
| sys-net | Default network qube (pre-installed) | *n/a* |
| sys-firewall | Default firewall qube (pre-installed) | sys-net |
| sys-proxyvm | VPN ProxyVM | sys-firewall |
| sys-whonix | Whonix Gateway VM | sys-proxyvm |
| anon-whonix | Whonix Workstation VM | sys-whonix |

## Additional Resources

Consult the extensive documentation on the [Qubes OS Website](https://qubes-os.org/doc). Offline copies are available from the [documentation repository](https://github.com/QubesOS/qubes-doc).

- [Arguably the world's most secure operating system](https://opentech.fund/news/qubes-os-arguably-the-worlds-most-secure-operating-system-motherboard) — Open Technology Fund
- [Software compartmentalization vs. physical separation](https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf) — J. Rutkowska
- [Partitioning my digital life into security domains](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html) — J. Rutkowska
- [Related Articles](https://qubes-os.org/news/categories/#articles) — Qubes OS