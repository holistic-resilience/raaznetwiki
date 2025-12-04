[Skip to content](https://www.privacyguides.org/en/self-hosting/#dns-filtering)

![](https://www.privacyguides.org/en/assets/img/cover/router.webp)

# Self-Hosting

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/self-hosting/index.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)

**Self-hosting** software and services can be a way to achieve a higher level of privacy through digital sovereignty, particularly independence from cloud servers controlled by product developers or vendors. By self-hosting, we mean hosting applications and data on your own hardware.

Self-hosting your own solutions requires advanced technical knowledge and a deep understanding of the associated risks. By becoming the host for yourself and possibly others, you take on responsibilities you might not otherwise have. Self-hosting privacy software improperly can leave you worse off than using e.g. an end-to-end encrypted service provider, so it is best avoided if you are not already comfortable doing so.

## DNS Filtering

- ![AdGuard Home logo](https://www.privacyguides.org/en/assets/img/self-hosting/adguard-home.svg)[AdGuard Home](https://www.privacyguides.org/en/self-hosting/dns-filtering/#adguard-home)
- ![Pi-Hole logo](https://www.privacyguides.org/en/assets/img/self-hosting/pi-hole.svg)[Pi-Hole](https://www.privacyguides.org/en/self-hosting/dns-filtering/#pi-hole)

[Learn more](https://www.privacyguides.org/en/self-hosting/dns-filtering/)

## Email Servers

- ![Stalwart logo](https://www.privacyguides.org/en/assets/img/self-hosting/stalwart.svg)[Stalwart](https://www.privacyguides.org/en/self-hosting/email-servers/#stalwart)
- ![Mailcow logo](https://www.privacyguides.org/en/assets/img/self-hosting/mailcow.svg)[Mailcow](https://www.privacyguides.org/en/self-hosting/email-servers/#mailcow)
- ![Mail-in-a-Box logo](https://www.privacyguides.org/en/assets/img/self-hosting/mail-in-a-box.svg)[Mail-in-a-Box](https://www.privacyguides.org/en/self-hosting/email-servers/#mail-in-a-box)

[Learn more](https://www.privacyguides.org/en/self-hosting/email-servers/)

## File Management

- ![PhotoPrism logo](https://www.privacyguides.org/en/assets/img/self-hosting/photoprism.svg)[PhotoPrism](https://www.privacyguides.org/en/self-hosting/file-management/#photoprism)
- ![FreedomBox logo](https://www.privacyguides.org/en/assets/img/self-hosting/freedombox.svg)[FreedomBox](https://www.privacyguides.org/en/self-hosting/file-management/#freedombox)
- ![Nextcloud logo](https://www.privacyguides.org/en/assets/img/self-hosting/nextcloud.svg)[Nextcloud](https://www.privacyguides.org/en/self-hosting/file-management/#nextcloud)

[Learn more](https://www.privacyguides.org/en/self-hosting/file-management/)

## Password Management

### Vaultwarden

![Vaultwarden logo](https://www.privacyguides.org/en/assets/img/self-hosting/vaultwarden.svg#only-light)![Vaultwarden logo](https://www.privacyguides.org/en/assets/img/self-hosting/vaultwarden-dark.svg#only-dark)

**Vaultwarden** is an alternative implementation of [Bitwarden](https://www.privacyguides.org/en/passwords/#bitwarden)'s sync server written in Rust and compatible with official Bitwarden clients, perfect for self-hosted deployment where running the resource-heavy, [official service](https://github.com/bitwarden/server) might not be ideal.

[Repository](https://github.com/dani-garcia/vaultwarden#readme) [Documentation](https://github.com/dani-garcia/vaultwarden/wiki "Documentation") [Source Code](https://github.com/dani-garcia/vaultwarden "Source Code") [Contribute](https://github.com/sponsors/dani-garcia "Contribute")

## Social Networks

Self-hosting your own instance of a social network software can help circumvent potential [censorship on a server level](https://www.privacyguides.org/en/social-networks/#censorship-resistance) by a public server's administrator or admin team.

### Mastodon

![Mastodon logo](https://www.privacyguides.org/en/assets/img/social-networks/mastodon.svg)

**Mastodon** is a social network based on open web protocols and free, open-source software. It uses the decentralized **ActivityPub** protocol.

[Homepage](https://joinmastodon.org/ "Homepage")[Admin Documentation](https://docs.joinmastodon.org/admin/prerequisites "Admin Documentation")

Mastodon [integrates with the Tor network](https://docs.joinmastodon.org/admin/optional/tor) for more extreme scenarios where even your underlying hosting provider is subject to censorship, but this may limit who can access your content to only other servers which integrate with Tor (like most other hidden services).

Mastodon benefits greatly from a large and active self-hosting community, and its administration is comprehensively documented. While many other ActivityPub platforms can require extensive technical knowledge to run and troubleshoot, Mastodon has very stable and tested releases, and it can generally be run securely without issue by anyone who can use the Linux command line and follow step-by-step instructions.

### Element

![Element logo](https://www.privacyguides.org/en/assets/img/social-networks/element.svg)

**Element** is the flagship client for the **Matrix** protocol, an open standard that enables decentralized communication by way of federated chat rooms.

[Homepage](https://element.io/ "Homepage")[Admin Documentation](https://element-hq.github.io/synapse/latest "Admin Documentation")[Source Code](https://github.com/element-hq "Source Code")

## Frontends

Self-hosting your own instance of a web-based frontend can help you circumvent rate limits that you may encounter on high-traffic, public instances. It is important that you have other people using your instance as well in order for you to blend in. You should be careful with where and how you are hosting, as other peoples' usage will be linked to your hosting.

- ![Redlib logo](https://www.privacyguides.org/en/assets/img/frontends/redlib.svg)[**Redlib (Reddit)**](https://www.privacyguides.org/en/frontends/#redlib)


* * *


[Admin Documentation](https://github.com/redlib-org/redlib#deployment "Admin Documentation")[Source Code](https://github.com/redlib-org/redlib "Source Code")

- ![ProxiTok logo](https://www.privacyguides.org/en/assets/img/frontends/proxitok.svg)[**ProxiTok (TikTok)**](https://www.privacyguides.org/en/frontends/#proxitok)


* * *


[Admin Documentation](https://github.com/pablouser1/ProxiTok/wiki/Self-hosting "Admin Documentation")[Source Code](https://github.com/pablouser1/ProxiTok "Source Code")

- ![Invidious logo](https://www.privacyguides.org/en/assets/img/frontends/invidious.svg#only-light)![Invidious logo](https://www.privacyguides.org/en/assets/img/frontends/invidious-dark.svg#only-dark)[**Invidious (YouTube)**](https://www.privacyguides.org/en/frontends/#invidious)


* * *


[Homepage](https://invidious.io/ "Homepage")[Admin Documentation](https://docs.invidious.io/installation "Admin Documentation")[Source Code](https://github.com/iv-org/invidious "Source Code")

- ![Piped logo](https://www.privacyguides.org/en/assets/img/frontends/piped.svg)[**Piped (YouTube)**](https://www.privacyguides.org/en/frontends/#piped)


* * *


[Admin Documentation](https://docs.piped.video/docs/self-hosting "Admin Documentation")[Source Code](https://github.com/TeamPiped/Piped "Source Code")


## More Tools...

Tool recommendations in other categories of the website also provide a self-hosted option, so you could consider this if you are confident in your ability to host the software after reading their documentation.

- ![Peergos logo](https://www.privacyguides.org/en/assets/img/cloud/peergos.svg)[**Peergos**](https://www.privacyguides.org/en/cloud/#peergos)


* * *


[Homepage](https://peergos.org/ "Homepage")[Admin Documentation](https://github.com/peergos/peergos#usage---running-locally-to-log-in-to-another-instance "Admin Documentation")[Source Code](https://github.com/Peergos/Peergos "Source Code")

- ![Addy.io logo](https://www.privacyguides.org/en/assets/img/email-aliasing/addy.svg)[**Addy.io**](https://www.privacyguides.org/en/email-aliasing/#addyio)


* * *


[Homepage](https://addy.io/ "Homepage")[Admin Documentation](https://addy.io/self-hosting "Admin Documentation")[Source Code](https://github.com/anonaddy "Source Code")

- ![SimpleLogin logo](https://www.privacyguides.org/en/assets/img/email-aliasing/simplelogin.svg)[**SimpleLogin**](https://www.privacyguides.org/en/email-aliasing/#simplelogin)


* * *


[Homepage](https://addy.io/ "Homepage")[Admin Documentation](https://github.com/simple-login/app#prerequisites "Admin Documentation")[Source Code](https://github.com/simple-login "Source Code")

- ![Ente logo](https://www.privacyguides.org/en/assets/img/photo-management/ente.svg)[**Ente Photos**](https://www.privacyguides.org/en/photo-management/#ente-photos)


* * *


[Homepage](https://ente.io/ "Homepage")[Admin Documentation](https://help.ente.io/self-hosting "Admin Documentation")[Source Code](https://github.com/ente-io/ente "Source Code")

- ![CryptPad logo](https://www.privacyguides.org/en/assets/img/document-collaboration/cryptpad.svg)[**CryptPad**](https://www.privacyguides.org/en/document-collaboration/#cryptpad)


* * *


[Homepage](https://cryptpad.fr/ "Homepage")[Admin Documentation](https://docs.cryptpad.org/en/admin_guide/index.html "Admin Documentation")[Source Code](https://github.com/xwiki-labs/cryptpad "Source Code")

- ![Send logo](https://www.privacyguides.org/en/assets/img/file-sharing-sync/send.svg)[**Send**](https://www.privacyguides.org/en/file-sharing/#send)


* * *


[Homepage](https://send.vis.ee/ "Homepage")[Admin Documentation](https://github.com/timvisee/send/blob/master/docs/deployment.md "Admin Documentation")[Source Code](https://github.com/timvisee/send "Source Code")

- ![LibreTranslate logo](https://www.privacyguides.org/en/assets/img/language-tools/libretranslate.png)[**LibreTranslate**](https://www.privacyguides.org/en/language-tools/#libretranslate)


* * *


[Homepage](https://libretranslate.com/ "Homepage")[Admin Documentation](https://docs.libretranslate.com/ "Admin Documentation")[Source Code](https://github.com/LibreTranslate/LibreTranslate "Source Code")

- ![Miniflux logo](https://www.privacyguides.org/en/assets/img/news-aggregators/miniflux.svg#only-light)![Miniflux logo](https://www.privacyguides.org/en/assets/img/news-aggregators/miniflux-dark.svg#only-dark)[**Miniflux**](https://www.privacyguides.org/en/news-aggregators/#miniflux)


* * *


[Homepage](https://miniflux.app/ "Homepage")[Admin Documentation](https://miniflux.app/docs/index.html#administration-guide "Admin Documentation")[Source Code](https://github.com/miniflux/v2 "Source Code")

- ![Standard Notes logo](https://www.privacyguides.org/en/assets/img/notebooks/standard-notes.svg)[**Standard Notes**](https://www.privacyguides.org/en/notebooks/#standard-notes)


* * *


[Homepage](https://standardnotes.com/ "Homepage")[Admin Documentation](https://standardnotes.com/help/47/can-i-self-host-standard-notes "Admin Documentation")[Source Code](https://github.com/standardnotes "Source Code")

- ![PrivateBin logo](https://www.privacyguides.org/en/assets/img/pastebins/privatebin.svg)[**PrivateBin**](https://www.privacyguides.org/en/pastebins/#privatebin)


* * *


[Homepage](https://privatebin.info/ "Homepage")[Admin Documentation](https://github.com/PrivateBin/PrivateBin/blob/master/doc/Installation.md "Admin Documentation")[Source Code](https://github.com/PrivateBin/PrivateBin "Source Code")

- ![Paaster logo](https://www.privacyguides.org/en/assets/img/pastebins/paaster.svg)[**Paaster**](https://www.privacyguides.org/en/pastebins/#paaster)


* * *


[Homepage](https://paaster.io/ "Homepage")[Admin Documentation](https://github.com/WardPearce/paaster#deployment "Admin Documentation")[Source Code](https://github.com/WardPearce/paaster "Source Code")

- ![SimpleX Chat logo](https://www.privacyguides.org/en/assets/img/messengers/simplex.svg)[**SimpleX Chat**](https://www.privacyguides.org/en/real-time-communication/#simplex-chat)


* * *


[Homepage](https://simplex.chat/ "Homepage")[Admin Documentation](https://simplex.chat/docs/server.html "Admin Documentation")[Source Code](https://github.com/simplex-chat "Source Code")


Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).