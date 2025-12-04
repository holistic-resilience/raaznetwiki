[Skip to content](https://www.privacyguides.org/en/cloud/#proton-drive)

![](https://www.privacyguides.org/en/assets/img/cover/cloud.webp)

# Cloud Storage

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/cloud.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)
- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)

Many **cloud storage providers** require your full trust that they will not look at your files. The alternatives listed below eliminate the need for trust by implementing secure end-to-end encryption.

If these alternatives do not fit your needs, we suggest you look into using encryption software like [Cryptomator](https://www.privacyguides.org/en/encryption/#cryptomator-cloud) with another cloud provider. Using Cryptomator in conjunction with **any** cloud provider (including these) may be a good idea to reduce the risk of encryption flaws in a provider's native clients.

Looking for Nextcloud?

For more technical readers, Nextcloud is [still a recommended tool](https://www.privacyguides.org/en/self-hosting/file-management/#nextcloud) for self-hosting a file management suite, however we do not recommend third-party Nextcloud storage providers at the moment, because we do [not recommend](https://discuss.privacyguides.net/t/dont-recommend-nextcloud-e2ee/10352/29) Nextcloud's built-in E2EE functionality for home users.

## Proton Drive

![Proton Drive logo](https://www.privacyguides.org/en/assets/img/cloud/protondrive.svg)

**Proton Drive** is an encrypted cloud storage provider from the popular encrypted email provider [Proton Mail](https://www.privacyguides.org/en/email/#proton-mail).

The initial free storage is limited to 2 GB, but with the completion of [certain steps](https://proton.me/support/more-free-storage-existing-users), additional storage can be obtained up to 5 GB.

[Homepage](https://proton.me/drive) [Privacy Policy](https://proton.me/drive/privacy-policy "Privacy Policy") [Documentation](https://proton.me/support/drive "Documentation") [Source Code](https://github.com/ProtonMail/WebClients "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=me.proton.android.drive)
- [App Store](https://apps.apple.com/app/id1509667851)
- [Windows](https://proton.me/drive/download)
- [macOS](https://proton.me/drive/download)

The Proton Drive web application has been independently audited by Securitum in [2021](https://proton.me/community/open-source), but the brand new mobile clients have not yet been publicly audited by a third party.

## Tresorit

![Tresorit logo](https://www.privacyguides.org/en/assets/img/cloud/tresorit.svg)

**Tresorit** is a Swiss-Hungarian encrypted cloud storage provider founded in 2011. Tresorit is owned by the Swiss Post, the national postal service of Switzerland.

[Homepage](https://tresorit.com/) [Privacy Policy](https://tresorit.com/legal/privacy-policy "Privacy Policy") [Documentation](https://support.tresorit.com/ "Documentation")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.tresorit.mobile)
- [App Store](https://apps.apple.com/app/id722163232)
- [Windows](https://tresorit.com/download)
- [macOS](https://tresorit.com/download)
- [Linux](https://tresorit.com/download)

Tresorit has received a number of independent security audits:

- [2022](https://tresorit.com/blog/tresorit-receives-iso-27001-certification): ISO/IEC 27001:2013[1](https://www.privacyguides.org/en/cloud/#fn:1) Compliance [Certification](https://certipedia.com/quality_marks/9108644476) by TÜV Rheinland InterCert Kft
- [2021](https://tresorit.com/blog/fresh-penetration-testing-confirms-tresorit-security): Penetration Testing by Computest
  - This review assessed the security of the Tresorit web client, Android app, Windows app, and associated infrastructure.
  - Computest discovered two vulnerabilities which have been resolved.
- [2019](https://tresorit.com/blog/ernst-young-review-verifies-tresorits-security-architecture): Penetration Testing by Ernst & Young.
  - This review analyzed the full source code of Tresorit and validated that the implementation matches the concepts described in Tresorit's [white paper](https://prodfrontendcdn.azureedge.net/202208011608/tresorit-encryption-whitepaper.pdf).
  - Ernst & Young additionally tested the web, mobile, and desktop clients. They concluded:


    > Test results found no deviation from Tresorit’s data confidentiality claims.

They have also received the Digital Trust Label, a certification from the [Swiss Digital Initiative](https://efd.admin.ch/en/swiss-digital-initiative-en) which requires passing [35 criteria](https://swiss-digital-initiative.org/criteria) related to security, privacy, and reliability.

## Peergos

![Peergos logo](https://www.privacyguides.org/en/assets/img/cloud/peergos.svg)

**Peergos** is a decentralized protocol and open-source platform for storage, social media, and applications. It provides a secure and private space where users can store, share, view, and edit their photos, videos, documents, etc.

Peergos secures your files with quantum-resistant E2EE and ensures all data about your files remains private. It is also [self-hostable](https://book.peergos.org/features/self).

[Homepage](https://peergos.org/) [Privacy Policy](https://peergos.net/privacy.html "Privacy Policy") [Documentation](https://book.peergos.org/ "Documentation") [Source Code](https://github.com/Peergos/Peergos "Source Code") [Contribute](https://github.com/peergos/peergos#support "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=peergos.android)
- [GitHub](https://github.com/Peergos/web-ui/releases)
- [Windows](https://peergos.org/download#windows)
- [macOS](https://peergos.org/download#macos)
- [Linux](https://peergos.org/download#linux)
- [Web](https://peergos.net/)

Peergos is built on top of the [InterPlanetary File System (IPFS)](https://ipfs.tech/), a peer-to-peer architecture that protects against [Censorship](https://www.privacyguides.org/en/basics/common-threats/#avoiding-censorship).

The client, server, and command line interface for Peergos all run from the same binary. Additionally, Peergos includes a [sync engine](https://book.peergos.org/features/sync) (accessible via the native apps) for bi-directionally synchronizing a local folder with a Peergos folder, and a [webdav bridge](https://book.peergos.org/features/webdav) to allow other applications to access your Peergos storage. You can refer to Peergos's documentation for a full overview of their numerous features.

Peergos was [audited](https://peergos.org/posts/security-audit-2024) in November 2024 by Radically Open Security and all issues were fixed. They were previously [audited](https://cure53.de/pentest-report_peergos.pdf) by Cure53 in June 2019, and all found issues were subsequently fixed.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

### Minimum Requirements

- Must enforce E2EE.
- Must offer a free plan or trial period for testing.
- Must support TOTP or FIDO2 multifactor authentication, or passkey logins.
- Must offer a web interface which supports basic file management functionality.
- Must allow for easy exports of all files/documents.

### Best-Case

Our best-case criteria represents what we would like to see from the perfect project in this category. Our recommendations may not include any or all of this functionality, but those which do may rank higher than others on this page.

- Clients should be open source.
- Clients should be audited in their entirety by an independent third party.
- Should offer native clients for Linux, Android, Windows, macOS, and iOS.
  - These clients should integrate with native OS tools for cloud storage providers, such as Files app integration on iOS, or DocumentsProvider functionality on Android.
- Should support easy file sharing with other users.
- Should offer at least basic file preview and editing functionality on the web interface.

* * *

1. [ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001):2013 compliance relates to the company's [information security management system](https://en.wikipedia.org/wiki/Information_security_management) and covers the sales, development, maintenance and support of their cloud services. [↩](https://www.privacyguides.org/en/cloud/#fnref:1)


Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).