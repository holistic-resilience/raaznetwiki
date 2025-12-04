[Skip to content](https://www.privacyguides.org/en/android/distributions/#grapheneos)

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/android/distributions.md?plain=1 "Edit this page")

# Alternative Distributions

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)
- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)

A **custom Android-based operating system** (sometimes referred to as a **custom ROM**) can be a way to achieve a higher level of privacy and security on your device. This is in contrast to the "stock" version of Android which comes with your phone from the factory, and is often deeply integrated with Google Play Services as well as other vendor software.

We recommend installing GrapheneOS if you have a Google Pixel as it provides improved security hardening and additional privacy features. The reasons we don't list other operating systems or devices are as follows:

- They often have [weaker security](https://www.privacyguides.org/en/android/#install-a-custom-distribution).
- Support is frequently dropped when the maintainer loses interest or upgrades their device, which is in contrast to the predictable [support cycle](https://grapheneos.org/faq#device-lifetime) that GrapheneOS follows.
- They generally have few or no notable privacy or security improvements that make installing them worthwhile.

## GrapheneOS

![GrapheneOS logo](https://www.privacyguides.org/en/assets/img/android/grapheneos.svg#only-light)![GrapheneOS logo](https://www.privacyguides.org/en/assets/img/android/grapheneos-dark.svg#only-dark)

**GrapheneOS** is the best choice when it comes to privacy and security.

GrapheneOS provides additional [security hardening](https://en.wikipedia.org/wiki/Hardening_(computing)) and privacy improvements. It has a [hardened memory allocator](https://github.com/GrapheneOS/hardened_malloc), network and sensor permissions, and various other [security features](https://grapheneos.org/features). GrapheneOS also comes with full firmware updates and signed builds, so verified boot is fully supported.

[Homepage](https://grapheneos.org/) [Privacy Policy](https://grapheneos.org/faq#privacy-policy "Privacy Policy") [Documentation](https://grapheneos.org/faq "Documentation") [Source Code](https://grapheneos.org/source "Source Code") [Contribute](https://grapheneos.org/donate "Contribute")

GrapheneOS supports [sandboxed Google Play](https://grapheneos.org/usage#sandboxed-google-play), which runs Google Play Services fully sandboxed like any other regular app. This means you can take advantage of most Google Play Services, such as push notifications, while giving you full control over their permissions and access, and while containing them to a specific [work profile](https://www.privacyguides.org/en/os/android-overview/#work-profile) or [user profile](https://www.privacyguides.org/en/os/android-overview/#user-profiles) of your choice.

[Google Pixel phones](https://www.privacyguides.org/en/mobile-phones/#google-pixel) are the only devices that currently meet GrapheneOS's [hardware security requirements](https://grapheneos.org/faq#future-devices).

By default, Android makes many network connections to Google to perform DNS connectivity checks, to sync with current network time, to check your network connectivity, and for many other background tasks. GrapheneOS replaces these with connections to servers operated by GrapheneOS and subject to their privacy policy. This hides information like your IP address [from Google](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers), but means it is trivial for an admin on your network or ISP to see you are making connections to `grapheneos.network`, `grapheneos.org`, etc. and deduce what operating system you are using.

If you want to hide information like this from an adversary on your network or ISP, you **must** use a [trusted VPN](https://www.privacyguides.org/en/vpn/) in addition to changing the connectivity check setting to **Standard (Google)**. It can be found in ![⚙](https://www.privacyguides.org/en/assets/external/cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2699.svg)**Settings** → **Network & internet** → **Internet connectivity checks**. This option allows you to connect to Google's servers for connectivity checks, which, alongside the usage of a VPN, helps you blend in with a larger pool of Android devices.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

- Must be open-source software.
- Must support bootloader locking with custom AVB key support.
- Must receive major Android updates within 0-1 months of release.
- Must receive Android feature updates (minor version) within 0-14 days of release.
- Must receive regular security patches within 0-5 days of release.
- Must **not** be "rooted" out of the box.
- Must **not** enable Google Play Services by default.
- Must **not** require system modification to support Google Play Services.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).