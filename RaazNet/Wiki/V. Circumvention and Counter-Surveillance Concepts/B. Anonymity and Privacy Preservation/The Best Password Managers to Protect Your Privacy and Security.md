[Skip to content](https://www.privacyguides.org/en/passwords/#cloud-based)

![](https://www.privacyguides.org/en/assets/img/cover/passwords.webp)

# Password Managers

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/passwords.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)
- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)
- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)

**Password managers** allow you to securely store and manage passwords and other credentials with the use of a master password.

[Introduction to Passwords](https://www.privacyguides.org/en/basics/passwords-overview/)

Info

Built-in password managers in software like browsers and operating systems are sometimes not as good as dedicated password manager software. The advantage of a built-in password manager is good integration with the software, but it can often be very simple and lack privacy and security features that standalone offerings have.

For example, the password manager in Microsoft Edge doesn't offer end-to-end encryption at all. Google's password manager has [optional](https://support.google.com/accounts/answer/11350823) E2EE, and [Apple's](https://support.apple.com/HT202303) offers E2EE by default.

## Cloud-based

These password managers sync your passwords to a cloud server for easy accessibility from all your devices and safety against device loss.

### Bitwarden

![Bitwarden logo](https://www.privacyguides.org/en/assets/img/password-management/bitwarden.svg)

**Bitwarden** is a free and open-source password and passkey manager. It aims to solve password management problems for individuals, teams, and business organizations. Bitwarden is among the best and safest solutions to store all of your logins and passwords while conveniently keeping them synced between all of your devices.

[Homepage](https://bitwarden.com/) [Privacy Policy](https://bitwarden.com/privacy "Privacy Policy") [Documentation](https://bitwarden.com/help "Documentation") [Source Code](https://github.com/bitwarden "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.x8bit.bitwarden)
- [App Store](https://apps.apple.com/app/id1137397744)
- [GitHub](https://github.com/bitwarden/android/releases)
- [Windows](https://bitwarden.com/download)
- [macOS](https://bitwarden.com/download)
- [Linux](https://bitwarden.com/download)
- [Flathub](https://flathub.org/apps/details/com.bitwarden.desktop)
- [Firefox](https://addons.mozilla.org/firefox/addon/bitwarden-password-manager)
- [Chrome](https://chrome.google.com/webstore/detail/nngceckbapebfimnlniiiahkandclblb)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/jbkfoedolllekgbhcbcoahefnbanhhlh)
- [Safari](https://apps.apple.com/app/id1352778147)

Bitwarden uses [PBKDF2](https://bitwarden.com/help/kdf-algorithms/#pbkdf2) as its key derivation function (KDF) algorithm by default. It also offers [Argon2](https://bitwarden.com/help/kdf-algorithms/#argon2id), which is more secure, as an alternative. You can change your account's KDF algorithm in the web vault:

- Select **Settings → Security → Keys → KDF algorithm → Argon2id**

Bitwarden's server-side code is [open source](https://github.com/bitwarden/server), so if you don't want to use the Bitwarden cloud, you can easily host your own Bitwarden sync server.

### Proton Pass

![Proton Pass logo](https://www.privacyguides.org/en/assets/img/password-management/protonpass.svg)

**Proton Pass** is an open-source, end-to-end encrypted password manager developed by Proton, the team behind [Proton Mail](https://www.privacyguides.org/en/email/#proton-mail). It securely stores your login credentials, generates unique email aliases, and supports and stores passkeys.

[Homepage](https://proton.me/pass) [Privacy Policy](https://proton.me/pass/privacy-policy "Privacy Policy") [Documentation](https://proton.me/support/pass "Documentation") [Source Code](https://github.com/protonpass "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=proton.android.pass)
- [App Store](https://apps.apple.com/app/id6443490629)
- [Windows](https://proton.me/pass/download)
- [Firefox](https://addons.mozilla.org/firefox/addon/proton-pass)
- [Chrome](https://chromewebstore.google.com/detail/ghmbeldphafepmbegfdlkpapadhbakde)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/gcllgfdnfnllodcaambdaknbipemelie)
- [Web](https://pass.proton.me/)

With the acquisition of SimpleLogin in April 2022, Proton has offered a "hide-my-email" feature that lets you create 10 aliases (free plan) or unlimited aliases (paid plans).

The Proton Pass mobile apps and browser extension underwent an audit performed by Cure53 throughout May and June 2023. The security analysis company concluded:

> Proton Pass apps and components leave a rather positive impression in terms of security.

All issues were addressed and fixed shortly after the [report](https://res.cloudinary.com/dbulfrlrz/images/v1707561557/wp-pme/Cure53-proton-pass-20230717/Cure53-proton-pass-20230717.pdf).

### 1Password

![1Password logo](https://www.privacyguides.org/en/assets/img/password-management/1password.svg)

**1Password** is a password manager with a strong focus on security and ease-of-use that allows you to store passwords, passkeys, credit cards, software licenses, and any other sensitive information in a secure digital vault. Your vault is hosted on 1Password's servers for a [monthly fee](https://1password.com/sign-up).

1Password is [audited](https://support.1password.com/security-assessments) on a regular basis and provides exceptional customer support. 1Password is closed source; however, the security of the product is thoroughly documented in their [security white paper](https://1passwordstatic.com/files/security/1password-white-paper.pdf).

[Homepage](https://1password.com/) [Privacy Policy](https://1password.com/legal/privacy "Privacy Policy") [Documentation](https://support.1password.com/ "Documentation")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.onepassword.android)
- [App Store](https://apps.apple.com/app/id1511601750)
- [Windows](https://1password.com/downloads/windows)
- [macOS](https://1password.com/downloads/mac)
- [Linux](https://1password.com/downloads/linux)
- [Firefox](https://addons.mozilla.org/firefox/addon/1password-x-password-manager)
- [Chrome](https://chrome.google.com/webstore/detail/aeblfdkhhhdcdjpifhhbdiojplfjncoa)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/dppgmdbiimibapkepcbdbmkaabgiofem)
- [Safari](https://apps.apple.com/app/id1569813296)
- [Web](https://my.1password.com/signin)

Traditionally, 1Password has offered the best password manager user experience for people using macOS and iOS; however, it has now achieved feature parity across all platforms. 1Password's clients boast many features geared towards families and less technical people, such as an intuitive UI for ease-of-use and navigation, as well as advanced functionality. Notably, nearly every feature of 1Password is available within its native mobile or desktop clients.

Your 1Password vault is secured with both your master password and a randomized 34-character security key to encrypt your data on their servers. This security key adds a layer of protection to your data because your data is secured with high entropy regardless of your master password. Many other password manager solutions are entirely reliant on the strength of your master password to secure your data.

### Psono

![Psono logo](https://www.privacyguides.org/en/assets/img/password-management/psono.svg)

**Psono** is a free and open-source password manager from Germany, with a focus on password management for teams. Psono supports secure sharing of passwords, files, bookmarks, and emails. All secrets are protected by a master password.

[Homepage](https://psono.com/) [Privacy Policy](https://psono.com/privacy-policy "Privacy Policy") [Documentation](https://doc.psono.com/ "Documentation") [Source Code](https://gitlab.com/psono "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.psono.psono)
- [App Store](https://apps.apple.com/app/id1545581224)
- [Firefox](https://addons.mozilla.org/firefox/addon/psono-pw-password-manager)
- [Chrome](https://chrome.google.com/webstore/detail/eljmjmgjkbmpmfljlmklcfineebidmlo)
- [Docker Hub](https://hub.docker.com/r/psono/psono-client)

Psono provides extensive documentation for their product. The web-client for Psono can be self-hosted; alternatively, you can choose the full Community Edition or the Enterprise Edition with additional features.

In April 2024, Psono added [support for passkeys](https://psono.com/blog/psono-introduces-passkeys) for the browser extension only.

### Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

#### Minimum Requirements

- Must utilize strong, standards-based/modern E2EE.
- Must have thoroughly documented encryption and security practices.
- Must have a published audit from a reputable, independent third party.
- All non-essential telemetry must be optional.
- Must not collect more PII than is necessary for billing purposes.

#### Best-Case

Our best-case criteria represents what we would like to see from the perfect project in this category. Our recommendations may not include any or all of this functionality, but those which do may rank higher than others on this page.

- Telemetry should be opt-in (disabled by default) or not collected at all.
- Should be open source and reasonably self-hostable.

## Local Storage

These options allow you to manage an encrypted password database locally.

### KeePassXC

![KeePassXC logo](https://www.privacyguides.org/en/assets/img/password-management/keepassxc.svg)

**KeePassXC** is a community fork of KeePassX, a native cross-platform port of KeePass Password Safe, with the goal of extending and improving it with new features and bug fixes to provide a feature-rich, cross-platform, and modern open-source password manager.

[Homepage](https://keepassxc.org/) [Privacy Policy](https://keepassxc.org/privacy "Privacy Policy") [Documentation](https://keepassxc.org/docs "Documentation") [Source Code](https://github.com/keepassxreboot/keepassxc "Source Code") [Contribute](https://keepassxc.org/donate "Contribute")

Downloads

- [Windows](https://keepassxc.org/download/#windows)
- [macOS](https://keepassxc.org/download/#mac)
- [Linux](https://keepassxc.org/download/#linux)
- [Flathub](https://flathub.org/apps/details/org.keepassxc.KeePassXC)
- [Firefox](https://addons.mozilla.org/firefox/addon/keepassxc-browser)
- [Chrome](https://chrome.google.com/webstore/detail/oboonakemofpalcgghocfoadofidjkkk)

KeePassXC stores its export data as [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) files. You may encounter data loss if you import this file into another password manager. We advise you check each record manually.

### KeePassDX (Android)

![KeePassDX logo](https://www.privacyguides.org/en/assets/img/password-management/keepassdx.svg)

**KeePassDX** is a lightweight password manager for Android; it allows for editing encrypted data in a single file in KeePass format and can fill in forms securely.

[Homepage](https://keepassdx.com/) [Documentation](https://github.com/Kunzisoft/KeePassDX/wiki "Documentation") [Source Code](https://github.com/Kunzisoft/KeePassDX "Source Code") [Contribute](https://keepassdx.com/#donation "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.kunzisoft.keepass.free)
- [GitHub](https://github.com/Kunzisoft/KeePassDX/releases)

The [pro version](https://play.google.com/store/apps/details?id=com.kunzisoft.keepass.pro) of the app allows you to unlock cosmetic content and non-standard protocol features, but more importantly, it helps and encourages development.

### KeePassium (iOS & macOS)

![KeePassium logo](https://www.privacyguides.org/en/assets/img/password-management/keepassium.svg)

KeePassium is a commercial, open-source password manager made by KeePassium Labs that's compatible with other KeePass applications. It provides autofill support, passkey management, automatic two-way synchronization through [most cloud storage providers](https://support.keepassium.com/kb/sync), and more.

[Read our latest KeePassium review.](https://www.privacyguides.org/articles/2025/05/13/keepassium-review)

[Homepage](https://keepassium.com/) [Privacy Policy](https://keepassium.com/privacy/app "Privacy Policy") [Documentation](https://support.keepassium.com/ "Documentation") [Source Code](https://github.com/keepassium/KeePassium "Source Code") [Contribute](https://keepassium.com/donate "Contribute")

Downloads

- [App Store](https://apps.apple.com/us/app/id1435127111)

KeePassium offers a [Premium version](https://keepassium.com/pricing) with additional features such as support for multiple databases, YubiKey support, and a password audit tool.

KeePassium's iOS app has been [audited](https://cure53.de/pentest-report_keepassium.pdf) by Cure53 in October 2024, and all [issues](https://keepassium.com/blog/2024/11/independent-security-audit-complete) found in the audit were subsequently fixed.

### Gopass (CLI)

![Gopass logo](https://www.privacyguides.org/en/assets/img/password-management/gopass.svg)

**Gopass** is a minimal password manager for the command line written in Go. It can be used within scripting applications and works on all major desktop and server operating systems.

[Homepage](https://gopass.pw/) [Documentation](https://github.com/gopasspw/gopass/tree/master/docs "Documentation") [Source Code](https://github.com/gopasspw/gopass "Source Code") [Contribute](https://github.com/sponsors/dominikschulz "Contribute")

Downloads

- [Windows](https://gopass.pw/#install-windows)
- [macOS](https://gopass.pw/#install-macos)
- [Linux](https://gopass.pw/#install-linux)
- [FreeBSD](https://gopass.pw/#install-bsd)

### Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

- Must be cross-platform.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).