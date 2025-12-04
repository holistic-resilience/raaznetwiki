[Skip to content](https://www.privacyguides.org/en/security-keys/#yubico-security-key)

![](https://www.privacyguides.org/en/assets/img/cover/multi-factor-authentication.webp)

# Security Keys

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/security-keys.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)
- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)

A physical **security key** adds a very strong layer of protection to your online accounts. Compared to [authenticator apps](https://www.privacyguides.org/en/multi-factor-authentication/), the [FIDO2](https://www.privacyguides.org/en/basics/multi-factor-authentication/#fido-fast-identity-online) security key protocol is immune to phishing, and cannot be compromised without physical possession of the key itself. Many services support FIDO2/WebAuthn as a multifactor authentication option for securing your account, and some services allow you to use a security key as a strong single-factor authenticator with passwordless authentication.

## Yubico Security Key

![Security Key Series by Yubico](https://www.privacyguides.org/en/assets/img/security-keys/yubico-security-key.webp)

The **Yubico Security Key** series is the most cost-effective hardware security key with FIDO Level 2 certification[1](https://www.privacyguides.org/en/security-keys/#fn:1). It supports FIDO2/WebAuthn and FIDO Universal 2nd Factor (U2F), and works out of the box with most services that support a security key as a second factor, as well as many password managers.

[Homepage](https://yubico.com/products/security-key) [Privacy Policy](https://yubico.com/support/terms-conditions/privacy-notice "Privacy Policy") [Documentation](https://docs.yubico.com/ "Documentation")

These keys are available in both USB-C and USB-A variants, and both options support NFC for use with a mobile device as well.

This key provides only basic FIDO2 functionality, but for most people that is all you will need. Some notable features the Security Key series does **not** have include:

- [Yubico Authenticator](https://yubico.com/products/yubico-authenticator)
- CCID Smart Card support (PIV-compatible)
- OpenPGP

If you need any of those features, you should consider their higher-end [YubiKey](https://www.privacyguides.org/en/security-keys/#yubikey) series instead.

Warning

The firmware of Yubico's Security Keys is not updatable. If you want features in newer firmware versions, or if there is a vulnerability in the firmware version you are using, you would need to purchase a new key.

## YubiKey

![YubiKeys](https://www.privacyguides.org/en/assets/img/security-keys/yubikey.png)

The **YubiKey** series from Yubico are among the most popular security keys with FIDO Level 2 Certification[1](https://www.privacyguides.org/en/security-keys/#fn:1). The **YubiKey 5 Series** has a wide range of features such as FIDO2/WebAuthn and FIDOU2F, [TOTP and HOTP](https://developers.yubico.com/OATH) authentication, [Personal Identity Verification (PIV)](https://developers.yubico.com/PIV), and [OpenPGP](https://developers.yubico.com/PGP).

[Homepage](https://yubico.com/products/yubikey-5-overview) [Privacy Policy](https://yubico.com/support/terms-conditions/privacy-notice "Privacy Policy") [Documentation](https://docs.yubico.com/ "Documentation")

The [comparison table](https://yubico.com/store/compare) shows how the YubiKeys compare to each other and to Yubico's [Security Key](https://www.privacyguides.org/en/security-keys/#yubico-security-key) series in terms of features and other specifications. One of the benefits of the YubiKey series is that one key can do almost everything you could expect from a hardware security key. We encourage you to take their [quiz](https://yubico.com/quiz) before purchasing in order to make sure you choose the right security key.

YubiKeys can be programmed using the [YubiKey Manager](https://yubico.com/support/download/yubikey-manager) or [YubiKey Personalization Tools](https://yubico.com/support/download/yubikey-personalization-tools). For managing TOTP codes, you can use the [Yubico Authenticator](https://yubico.com/products/yubico-authenticator). All of Yubico's clients are open source.

For models which [support HOTP and TOTP](https://support.yubico.com/hc/articles/360013790319-How-many-accounts-can-I-register-my-YubiKey-with), the secrets are stored encrypted on the key and never exposed to the devices they are plugged into. Once a seed (shared secret) is given to the Yubico Authenticator, it will only give out the six-digit codes, but never the seed. This security model helps limit what an attacker can do if they compromise one of the devices running the Yubico Authenticator and make the YubiKey resistant to a physical attacker.

Warning

The firmware of YubiKey is not updatable. If you want features in newer firmware versions, or if there is a vulnerability in the firmware version you are using, you would need to purchase a new key.

## Nitrokey

![Nitrokey](https://www.privacyguides.org/en/assets/img/security-keys/nitrokey.jpg)

**Nitrokey** has a cost-effective security key capable of FIDO2/WebAuthn and FIDOU2F called the **Nitrokey Passkey**. For support for features such as PIV, OpenPGP, and TOTP and HOTP authentication, you need to purchase one of their other keys like the **Nitrokey 3**. Currently, only the **Nitrokey 3A Mini** has [FIDO Level 1 Certification](https://nitrokey.com/news/2024/nitrokey-3a-mini-receives-official-fido2-certification).

[Homepage](https://nitrokey.com/) [Privacy Policy](https://nitrokey.com/data-privacy-policy "Privacy Policy") [Documentation](https://docs.nitrokey.com/ "Documentation")

The [comparison table](https://nitrokey.com/products/nitrokeys#:~:text=The%20Nitrokey%20Family) shows how the different Nitrokey models compare to each other in terms of features and other specifications. Refer to Nitrokey's [documentation](https://docs.nitrokey.com/nitrokeys/features) for more details about the features available on your Nitrokey.

Nitrokey models can be configured using the [Nitrokey app](https://nitrokey.com/download).

Warning

Excluding the Nitrokey 3, Nitrokeys which support HOTP and TOTP do not have encrypted storage, making them vulnerable to physical attacks.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

### Minimum Requirements

- Must use high-quality, tamper-resistant hardware security modules.
- Must support the latest FIDO2 specification.
- Must not allow private key extraction.
- Devices which cost over $35 must support handling OpenPGP and S/MIME.

### Best-Case

Our best-case criteria represents what we would like to see from the perfect project in this category. Our recommendations may not include any or all of this functionality, but those which do may rank higher than others on this page.

- Should be available in USB-C form factor.
- Should be available with NFC.
- Should support TOTP secret storage.
- Should support secure firmware updates.

* * *

1. Some governments or other organizations may require a key with Level 2 certification, but most people do not have to worry about this distinction. [↩](https://www.privacyguides.org/en/security-keys/#fnref:1) [↩](https://www.privacyguides.org/en/security-keys/#fnref2:1)


Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).