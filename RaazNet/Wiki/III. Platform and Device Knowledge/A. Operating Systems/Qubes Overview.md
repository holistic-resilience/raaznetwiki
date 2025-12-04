```yaml
---
title: "Qubes OS Overview: Security Through Compartmentalization"
tags: [qubes-os, virtualization, compartmentalization, xen-hypervisor, operating-systems, privacy]
category: "Operating Systems"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Security Researchers, Activists, Journalists]
topics: ["Desktop Security", "Virtualization", "Threat Modeling", "Isolation"]
summary: "Comprehensive overview of Qubes OS, a security-focused operating system using Xen hypervisor and compartmentalized virtual machines (qubes) for strong isolation."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of operating systems", "Familiarity with virtualization concepts", "Understanding of threat modeling"]
estimated_read_time: "8 minutes"
---
```

# Qubes OS Overview

[**Qubes OS**](https://www.privacyguides.org/en/desktop/#qubes-os) is an open-source operating system that uses the [Xen](https://en.wikipedia.org/wiki/Xen) hypervisor to provide strong security for desktop computing through isolated *qubes* (virtual machines). You can assign each *qube* a level of trust based on its purpose. Qubes OS provides security through isolation, permitting actions only on a per-case basis—the opposite of [badness enumeration](https://ranum.com/security/computer_security/editorials/dumb).

## How Qubes OS Works

Qubes uses [compartmentalization](https://qubes-os.org/intro) to keep the system secure. Qubes are created from templates, with defaults for Fedora, Debian, and [Whonix](https://www.privacyguides.org/en/desktop/#whonix). The system also supports once-use [disposable](https://qubes-os.org/doc/how-to-use-disposables) *qubes*.

> **Note:** The term *qubes* is gradually replacing "virtual machines" in documentation. Qubes are not entire virtual machines but maintain similar functionalities.

![Qubes architecture](https://www.privacyguides.org/en/assets/img/qubes/qubes-trust-level-architecture.png)

Each qube has a [colored border](https://qubes-os.org/screenshots) to help you track which security domain it belongs to. For example, you might use one color for banking and another for general untrusted browsing.

![Colored border example](https://www.privacyguides.org/en/assets/img/qubes/r4.0-xfce-three-domains-at-work.png)

## Why Use Qubes OS?

Qubes OS is ideal when your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/) requires strong security and isolation—particularly if you regularly open untrusted files from unknown sources. The core principle: if a single qube is compromised, it won't affect the rest of the system.

Qubes OS uses [dom0](https://wiki.xenproject.org/wiki/Dom0) (a Xen VM) to control other *qubes* on the host OS. All qubes display individual application windows within dom0's desktop environment.

## Key Operations

### Copying and Pasting Text

You can [copy and paste text](https://qubes-os.org/doc/how-to-copy-and-paste-text) between qubes using `qvm-copy-to-vm` or these steps:

1. **Ctrl+C** — Copy within the current qube
2. **Ctrl+Shift+C** — Make the buffer available to the global clipboard
3. **Ctrl+Shift+V** — Access the global clipboard in the destination qube
4. **Ctrl+V** — Paste the contents

### File Exchange

To copy or move files between qubes, use **Copy to Other AppVM...** or **Move to Other AppVM...**. The **Move** option deletes the original file. Both options protect your clipboard from being leaked to other qubes.

This method is more secure than air-gapped file transfer, as air-gapped computers must still parse partitions or file systems—not required with inter-qube copying.

> **Important:** Qubes do not have persistent filesystems. You can create and delete files, but changes are ephemeral. Modifications aren't immediately committed and can be easily undone.

Learn more: [Copy and move files](https://qubes-os.org/doc/how-to-copy-and-move-files)

### Inter-VM Communication

The [qrexec framework](https://qubes-os.org/doc/qrexec) enables communication between domains. Built on the Xen library *vchan*, it facilitates [isolation through policies](https://qubes-os.org/news/2020/06/22/new-qrexec-policy-system).

## Connecting to Tor via VPN

Privacy Guides [recommends](https://www.privacyguides.org/en/advanced/tor-overview/) connecting to Tor via a [VPN](https://www.privacyguides.org/en/vpn/) provider. Qubes makes this straightforward using ProxyVMs and Whonix.

After [creating a ProxyVM](https://forum.qubes-os.org/t/configuring-a-proxyvm-vpn-gateway/19061) connected to your VPN, chain your Whonix qubes to that ProxyVM **before** they connect to Tor by setting the NetVM of your Whonix **Gateway** (`sys-whonix`) to the new ProxyVM.

| Qube Name | Description | NetVM |
|-----------|-------------|-------|
| sys-net | Default network qube (pre-installed) | *n/a* |
| sys-firewall | Default firewall qube (pre-installed) | sys-net |
| sys-proxyvm | VPN ProxyVM you created | sys-firewall |
| sys-whonix | Whonix Gateway VM | sys-proxyvm |
| anon-whonix | Whonix Workstation VM | sys-whonix |

## Additional Resources

Consult the extensive [Qubes OS documentation](https://qubes-os.org/doc) for more information. Offline copies are available from the [documentation repository](https://github.com/QubesOS/qubes-doc).

### Recommended Reading

- [Arguably the world's most secure operating system](https://opentech.fund/news/qubes-os-arguably-the-worlds-most-secure-operating-system-motherboard) — Open Technology Fund
- [Software compartmentalization vs. physical separation](https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf) — J. Rutkowska
- [Partitioning my digital life into security domains](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html) — J. Rutkowska
- [Related Articles](https://qubes-os.org/news/categories/#articles) — Qubes OS