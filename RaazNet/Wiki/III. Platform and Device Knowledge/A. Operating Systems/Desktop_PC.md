[Skip to content](https://www.privacyguides.org/en/desktop/#traditional-distributions)

![](https://www.privacyguides.org/en/assets/img/cover/desktop.webp)

# Desktop/PC

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/desktop.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

Linux distributions are commonly recommended for privacy protection and software freedom. If you don't already use Linux, below are some distributions we suggest trying out, as well as some general privacy and security improvement tips that are applicable to many Linux distributions.

- [General Linux Overview](https://www.privacyguides.org/en/os/linux-overview/)

## Traditional Distributions

### Fedora Linux

![Fedora logo](https://www.privacyguides.org/en/assets/img/linux-desktop/fedora.svg)

**Fedora Linux** is our recommended desktop distribution for people new to Linux. Fedora generally adopts newer technologies (e.g., [Wayland](https://wayland.freedesktop.org/) and [PipeWire](https://pipewire.org/)) before other distributions. These new technologies often come with improvements in security, privacy, and usability in general.

[Homepage](https://fedoraproject.org/) [Documentation](https://docs.fedoraproject.org/en-US/docs "Documentation") [Contribute](https://whatcanidoforfedora.org/ "Contribute")

Fedora comes in two primary desktop editions, [Fedora Workstation](https://fedoraproject.org/workstation), which uses the GNOME desktop environment, and [Fedora KDE Plasma Desktop](https://fedoraproject.org/kde), which uses KDE. Historically, Fedora Workstation has been more popular and widely recommended, but KDE has been gaining in popularity and provides an experience more similar to Windows, which may make transitioning to Linux easier for some. The security and privacy benefits of both editions are very similar, so it mostly comes down to personal preference.

Fedora has a semi-rolling release cycle. While some packages like the desktop environment are frozen until the next Fedora release, most packages (including the kernel) are updated frequently throughout the lifespan of the release. Each Fedora release is supported for one year, with a new version released every 6 months.

### openSUSE Tumbleweed

![openSUSE Tumbleweed logo](https://www.privacyguides.org/en/assets/img/linux-desktop/opensuse-tumbleweed.svg)

**openSUSE Tumbleweed** is a stable rolling release distribution.

openSUSE Tumbleweed uses [Btrfs](https://en.wikipedia.org/wiki/Btrfs) and [Snapper](https://en.opensuse.org/openSUSE:Snapper_Tutorial) to ensure that snapshots can be rolled back should there be a problem.

[Homepage](https://get.opensuse.org/tumbleweed) [Documentation](https://doc.opensuse.org/ "Documentation") [Contribute](https://shop.opensuse.org/ "Contribute")

Tumbleweed follows a rolling release model where each update is released as a snapshot of the distribution. When you upgrade your system, a new snapshot is downloaded. Each snapshot is run through a series of automated tests by [openQA](https://openqa.opensuse.org/) to ensure its quality.

### Arch Linux

![Arch logo](https://www.privacyguides.org/en/assets/img/linux-desktop/archlinux.svg)

**Arch Linux** is a lightweight, do-it-yourself (DIY) distribution, meaning that you only get what you install. For more information see their [FAQ](https://wiki.archlinux.org/title/Frequently_asked_questions).

[Homepage](https://archlinux.org/) [Documentation](https://wiki.archlinux.org/ "Documentation") [Contribute](https://archlinux.org/donate "Contribute")

Arch Linux has a rolling release cycle. There is no fixed release schedule and packages are updated very frequently.

Being a DIY distribution, you are [expected to set up and maintain](https://www.privacyguides.org/en/os/linux-overview/#arch-based-distributions) your system on your own. Arch has an [official installer](https://wiki.archlinux.org/title/Archinstall) to make the installation process a little easier.

A large portion of [Arch Linux’s packages](https://reproducible.archlinux.org/) are [reproducible](https://reproducible-builds.org/) [1](https://www.privacyguides.org/en/desktop/#fn:1).

## Atomic Distributions

**Atomic distributions** (sometimes also referred to as **immutable distributions**) are operating systems which handle package installation and updates by layering changes atop your core system image, rather than by directly modifying the system. Advantages of atomic distros include increased stability and the ability to easily roll back updates. See [_Traditional vs. Atomic Updates_](https://www.privacyguides.org/en/os/linux-overview/#traditional-vs-atomic-updates) for more info.

### Fedora Atomic Desktops

![Fedora logo](https://www.privacyguides.org/en/assets/img/linux-desktop/fedora.svg)

**Fedora Atomic Desktops** are variants of Fedora which use the `rpm-ostree` package manager and have a strong focus on containerized workflows and Flatpak for desktop applications. All of these variants follow the same release schedule as Fedora Workstation, benefiting from the same fast updates and staying very close to upstream.

[Homepage](https://fedoraproject.org/atomic-desktops) [Documentation](https://docs.fedoraproject.org/en-US/emerging "Documentation") [Contribute](https://whatcanidoforfedora.org/ "Contribute")

[Fedora Atomic Desktops](https://fedoramagazine.org/introducing-fedora-atomic-desktops) come in a variety of flavors depending on the desktop environment you prefer. As with the recommendation to avoid X11 in our [criteria](https://www.privacyguides.org/en/desktop/#criteria) for Linux distributions, we recommend avoiding flavors that support only the legacy X11 window system.

These operating systems differ from Fedora Workstation as they replace the [DNF](https://docs.fedoraproject.org/en-US/quick-docs/dnf) package manager with a much more advanced alternative called [`rpm-ostree`](https://coreos.github.io/rpm-ostree). The `rpm-ostree` package manager works by downloading a base image for the system, then overlaying packages over it in a [git](https://en.wikipedia.org/wiki/Git)-like commit tree. When the system is updated, a new base image is downloaded and the overlays will be applied to that new image.

After the update is complete, you will reboot the system into the new deployment. `rpm-ostree` keeps two deployments of the system so that you can easily roll back if something breaks in the new deployment. There is also the option to pin more deployments as needed.

[Flatpak](https://flatpak.org/) is the primary package installation method on these distributions, as `rpm-ostree` is only meant to overlay packages that cannot stay inside a container on top of the base image.

As an alternative to Flatpaks, there is the option of [Toolbx](https://docs.fedoraproject.org/en-US/fedora-silverblue/toolbox) to create [Podman](https://podman.io/) containers which mimic a traditional Fedora environment, a [useful feature](https://containertoolbx.org/) for the discerning developer. These containers share a home directory with the host operating system.

### NixOS

![NixOS logo](https://www.privacyguides.org/en/assets/img/linux-desktop/nixos.svg)

NixOS is an independent distribution based on the Nix package manager with a focus on reproducibility and reliability.

[Homepage](https://nixos.org/) [Documentation](https://nixos.org/learn.html "Documentation") [Contribute](https://nixos.org/donate.html "Contribute")

NixOS’s package manager keeps every version of every package in a different folder in the **Nix store**. Due to this you can have different versions of the same package installed on your system. After the package contents have been written to the folder, the folder is made read-only.

NixOS also provides atomic updates. It first downloads (or builds) the packages and files for the new system generation and then switches to it. There are different ways to switch to a new generation: you can tell NixOS to activate it after reboot, or you can switch to it at runtime. You can also _test_ the new generation by switching to it at runtime, but not setting it as the current system generation. If something in the update process breaks, you can just reboot and automatically and return to a working version of your system.

The Nix package manager uses a purely functional language—which is also called Nix—to define packages.

[Nixpkgs](https://github.com/nixos/nixpkgs) (the main source of packages) are contained in a single GitHub repository. You can also define your own packages in the same language and then easily include them in your config.

Nix is a source-based package manager; if there’s no pre-built available in the binary cache, Nix will just build the package from source using its definition. It builds each package in a sandboxed _pure_ environment, which is as independent of the host system as possible. Binaries built with this method are reproducible[1](https://www.privacyguides.org/en/desktop/#fn:1).

## Anonymity-Focused Distributions

### Whonix

![Whonix logo](https://www.privacyguides.org/en/assets/img/linux-desktop/whonix.svg)

**Whonix** is based on [Kicksecure](https://www.privacyguides.org/en/desktop/#kicksecure), a security-focused fork of Debian. It aims to provide privacy, security, and [Anonymity](https://www.privacyguides.org/en/basics/common-threats/#anonymity-vs-privacy) on the internet. Whonix is best used in conjunction with [Qubes OS](https://www.privacyguides.org/en/desktop/#qubes-os).

[Homepage](https://whonix.org/) [Onion Service](http://dds6qkxpwdeubwucdiaord2xgbbeyds25rbsgr73tbfpqpt4a6vjwsyd.onion/ "Onion Service") [Documentation](https://whonix.org/wiki/Documentation "Documentation") [Contribute](https://whonix.org/wiki/Donate "Contribute")

Whonix is meant to run as two virtual machines: a “Workstation” and a Tor “Gateway.” All communications from the Workstation must go through the Tor gateway. This means that even if the Workstation is compromised by malware of some kind, the true IP address remains hidden.

Some of its features include Tor Stream Isolation, [keystroke anonymization](https://whonix.org/wiki/Keystroke_Deanonymization#Kloak), [encrypted swap](https://github.com/Whonix/swap-file-creator), and a hardened memory allocator. Future versions of Whonix will likely include [full system AppArmor policies](https://github.com/roddhjav/apparmor.d) and a [sandboxed app launcher](https://whonix.org/wiki/Sandbox-app-launcher) to fully confine all processes on the system.

Whonix is best used [in conjunction with Qubes](https://whonix.org/wiki/Qubes/Why_use_Qubes_over_other_Virtualizers). We have a [recommended guide](https://www.privacyguides.org/en/os/qubes-overview/#connecting-to-tor-via-a-vpn) on configuring Whonix in conjunction with a VPN ProxyVM in Qubes to hide your Tor activities from your ISP.

### Tails

![Tails logo](https://www.privacyguides.org/en/assets/img/linux-desktop/tails.svg)

**Tails** is a live operating system based on Debian that routes all communications through Tor, which can boot on on almost any computer from a DVD, USB stick, or SD card installation. It uses [Tor](https://www.privacyguides.org/en/tor/) to preserve privacy and [Anonymity](https://www.privacyguides.org/en/basics/common-threats/#anonymity-vs-privacy) while circumventing censorship, and it leaves no trace of itself on the computer it is used on after it is powered off.

[Homepage](https://tails.net/) [Documentation](https://tails.net/doc/index.en.html "Documentation") [Contribute](https://tails.net/donate "Contribute")

Warning

Tails [doesn't erase](https://gitlab.tails.boum.org/tails/tails/-/issues/5356) the [video memory](https://en.wikipedia.org/wiki/Dual-ported_video_RAM) when shutting down. When you restart your computer after using Tails, it might briefly display the last screen that was displayed in Tails. If you shut down your computer instead of restarting it, the video memory will erase itself automatically after being unpowered for some time.

Tails is great for counter forensics due to amnesia (meaning nothing is written to the disk); however, it is not a hardened distribution like Whonix. It lacks many anonymity and security features that Whonix has and gets updated much less often (only once every six weeks). A Tails system that is compromised by malware may potentially bypass the transparent proxy, allowing for the user to be deanonymized.

Tails includes [uBlock Origin](https://www.privacyguides.org/en/browser-extensions/#ublock-origin) in Tor Browser by default, which may potentially make it easier for adversaries to fingerprint Tails users. [Whonix](https://www.privacyguides.org/en/desktop/#whonix) virtual machines may be more leak-proof, however they are not amnesic, meaning data may be recovered from your storage device.

By design, Tails is meant to completely reset itself after each reboot. Encrypted [persistent storage](https://tails.net/doc/persistent_storage/index.en.html) can be configured to store some data between reboots.

## Security-focused Distributions

Protects against the following threat(s):

- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)

### Qubes OS

![Qubes OS logo](https://www.privacyguides.org/en/assets/img/qubes/qubes_os.svg)

**Qubes OS** is an open-source operating system designed to provide strong security for desktop computing through secure virtual machines (or "qubes"). Qubes is based on Xen, the X Window System, and Linux. It can run most Linux applications and use most of the Linux drivers.

[Homepage](https://qubes-os.org/) [Onion Service](http://qubesosfasa4zl44o4tws22di6kepyzfeqv3tg4e3ztknltfxqrymdad.onion/ "Onion Service") [Privacy Policy](https://qubes-os.org/privacy "Privacy Policy") [Documentation](https://qubes-os.org/doc "Documentation") [Source Code](https://github.com/QubesOS "Source Code") [Contribute](https://qubes-os.org/donate "Contribute")

Qubes OS secures the computer by isolating subsystems (e.g., networking, USB, etc.) and applications in separate _qubes_. Should one part of the system be compromised via an exploit in a [Targeted Attack](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals), the extra isolation is likely to protect the rest of the _qubes_ and the core system.

For further information about how Qubes works, read our full [Qubes OS overview](https://www.privacyguides.org/en/os/qubes-overview/) page.

### Secureblue

![Secureblue logo](https://www.privacyguides.org/en/assets/img/linux-desktop/secureblue.svg)

**Secureblue** is a security-focused operating system based on [Fedora Atomic Desktops](https://www.privacyguides.org/en/desktop/#fedora-atomic-desktops). It includes a number of [security features](https://secureblue.dev/features) intended to proactively defend against the exploitation of both known and unknown vulnerabilities, and ships with [Trivalent](https://github.com/secureblue/Trivalent), their hardened, Chromium-based web browser.

[Homepage](https://secureblue.dev/) [Documentation](https://secureblue.dev/install "Documentation") [Source Code](https://github.com/secureblue/secureblue "Source Code") [Contribute](https://secureblue.dev/donate "Contribute")

**Trivalent** is Secureblue's hardened Chromium for desktop Linux inspired by [GrapheneOS](https://www.privacyguides.org/en/android/distributions/#grapheneos)'s Vanadium browser.

Secureblue also provides GrapheneOS's [hardened memory allocator](https://github.com/GrapheneOS/hardened_malloc) and enables it globally (including for Flatpaks).

### Kicksecure

While we [recommend against](https://www.privacyguides.org/en/os/linux-overview/#release-cycle) "perpetually outdated" distributions like Debian for desktop use in most cases, Kicksecure is a Debian-based operating system which has been hardened to be much more than a typical Linux install.

![Kicksecure logo](https://www.privacyguides.org/en/assets/img/linux-desktop/kicksecure.svg)

**Kicksecure**—in oversimplified terms—is a set of scripts, configurations, and packages that substantially reduce the attack surface of Debian. It covers a lot of privacy and hardening recommendations by default. It also serves as the base OS for [Whonix](https://www.privacyguides.org/en/desktop/#whonix).

[Homepage](https://kicksecure.com/) [Privacy Policy](https://kicksecure.com/wiki/Privacy_Policy "Privacy Policy") [Documentation](https://kicksecure.com/wiki/Documentation "Documentation") [Source Code](https://github.com/Kicksecure "Source Code") [Contribute](https://kicksecure.com/wiki/Donate "Contribute")

## Criteria

Choosing a Linux distro that is right for you will come down to a huge variety of personal preferences, and this page is **not** meant to be an exhaustive list of every viable distribution. Our Linux overview page has some advice on [choosing a distro](https://www.privacyguides.org/en/os/linux-overview/#choosing-your-distribution) in more detail. The distros on _this_ page do all generally follow the guidelines we covered there, and all meet these standards:

- Free and open source.
- Receives regular software and kernel updates.
- Avoids X11, as its last major release was [more than a decade](https://x.org/wiki/Releases) ago.
  - The notable exception here is Qubes, but the [isolation issues](https://blog.invisiblethings.org/2011/04/23/linux-security-circus-on-gui-isolation) which X11 typically has are avoided by virtualization. This isolation only applies to apps _running in different qubes_ (virtual machines); apps running in the _same_ qube are not protected from each other.
- Supports full-disk encryption during installation.
- Doesn't freeze regular releases for more than 1 year.
  - We [recommend against](https://www.privacyguides.org/en/os/linux-overview/#release-cycle) "Long Term Support" or "stable" distro releases for desktop usage.
- Supports a wide variety of hardware.
- Preference towards larger projects.
  - Maintaining an operating system is a major challenge, and smaller projects have a tendency to make more avoidable mistakes, or delay critical updates (or worse, disappear entirely). We lean towards projects which will likely be around 10 years from now (whether that's due to corporate backing or very significant community support), and away from projects which are hand-built or have a small number of maintainers.

In addition, [our standard criteria](https://www.privacyguides.org/en/about/criteria/) for recommended projects still applies. **Please note we are not affiliated with any of the projects we recommend.**

* * *

1. Reproducibility entails the ability to verify that packages and binaries made available to the end user match the source code, which can be useful against potential [Supply Chain Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-certain-organizations). [↩](https://www.privacyguides.org/en/desktop/#fnref:1) [↩](https://www.privacyguides.org/en/desktop/#fnref2:1)


Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).