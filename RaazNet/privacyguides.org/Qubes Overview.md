---
title: "Qubes OS Overview"
tags: [qubes-os, virtualization, isolation, operating-systems, security]
category: "Operating Systems"
difficulty: "Advanced"
audience: "Advanced Users"
topics: [compartmentalization, vm-isolation, tor, vpn]
summary: "Overview of Qubes OS, a security-focused operating system using compartmentalization and isolated qubes for strong desktop security."
source: "https://www.privacyguides.org/en/os/qubes-overview/"
content_type: "guide"
security_level: "High"
language: "en"
prerequisites:
  ["Familiarity with Linux", "Understanding of virtualization concepts"]
estimated_read_time: 10
---

[Skip to content](https://www.privacyguides.org/en/os/qubes-overview/#how-does-qubes-os-work)

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/os/qubes-overview.md?plain=1 "Edit this page")

# Qubes Overview

[**Qubes OS**](https://www.privacyguides.org/en/desktop/#qubes-os) is an open-source operating system which uses the [Xen](https://en.wikipedia.org/wiki/Xen) hypervisor to provide strong security for desktop computing through isolated _qubes_, (which are Virtual Machines). You can assign each _qube_ a level of trust based on its purpose. Qubes OS provides security by using isolation. It only permits actions on a per-case basis and therefore is the opposite of [badness enumeration](https://ranum.com/security/computer_security/editorials/dumb).

## How does Qubes OS work?

Qubes uses [compartmentalization](https://qubes-os.org/intro) to keep the system secure. Qubes are created from templates, the defaults being for Fedora, Debian and [Whonix](https://www.privacyguides.org/en/desktop/#whonix). Qubes OS also allows you to create once-use [disposable](https://qubes-os.org/doc/how-to-use-disposables) _qubes_.

The term _qubes_ is gradually being updated to avoid referring to them as "virtual machines".

Some of the information here and on the Qubes OS documentation may contain conflicting language as the "appVM" term is gradually being changed to "qube". Qubes are not entire virtual machines, but maintain similar functionalities to VMs.

![Qubes architecture](https://www.privacyguides.org/en/assets/img/qubes/qubes-trust-level-architecture.png)

Qubes Architecture, Credit: What is Qubes OS Intro

Each qube has a [colored border](https://qubes-os.org/screenshots) that can help you keep track of the domain in which it runs. You could, for example, use a specific color for your banking browser, while using a different color for a general untrusted browser.

![Colored border](https://www.privacyguides.org/en/assets/img/qubes/r4.0-xfce-three-domains-at-work.png)

Qubes window borders, Credit: Qubes Screenshots

## Why Should I use Qubes?

Qubes OS is useful if your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/) requires strong security and isolation, such as if you think you'll be opening untrusted files from untrusted sources. A typical reason for using Qubes OS is to open documents from unknown sources, but the idea is that if a single qube is compromised it won't affect the rest of the system.

Qubes OS utilizes [dom0](https://wiki.xenproject.org/wiki/Dom0) Xen VM for controlling other _qubes_ on the host OS, all of which display individual application windows within dom0's desktop environment.

### Copying and Pasting Text

You can [copy and paste text](https://qubes-os.org/doc/how-to-copy-and-paste-text) using `qvm-copy-to-vm` or the documented key sequence.

### File Exchange

To copy and paste files and directories (folders) from one _qube_ to another, you can use the options **Copy to Other AppVM...** or **Move to Other AppVM...**.

Qubes do not have their own filesystems.

You can [copy and move files](https://qubes-os.org/doc/how-to-copy-and-move-files) between _qubes_.

### Inter-VM Interactions

The [qrexec framework](https://qubes-os.org/doc/qrexec) is a core part of Qubes which allows communication between domains.

## Connecting to Tor via a VPN

We [recommend](https://www.privacyguides.org/en/advanced/tor-overview/) connecting to the Tor network via a [VPN](https://www.privacyguides.org/en/vpn/) provider, and Qubes makes this easy to do with a combination of ProxyVMs and Whonix.

## Additional Resources

For additional information we encourage you to consult the extensive Qubes OS documentation pages located on the [Qubes OS Website](https://qubes-os.org/doc).

- [Arguably the world's most secure operating system](https://opentech.fund/news/qubes-os-arguably-the-worlds-most-secure-operating-system-motherboard) (Open Technology Fund)
- [Software compartmentalization vs. physical separation](https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf) (J. Rutkowska)
- [Partitioning my digital life into security domains](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html) (J. Rutkowska)
- [Related Articles](https://qubes-os.org/news/categories/#articles) (Qubes OS)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
