[Skip to content](https://www.privacyguides.org/en/real-time-communication/#signal)

![](https://www.privacyguides.org/en/assets/img/cover/real-time-communication.webp)

# Real-Time Communication

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/real-time-communication.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)
- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)
- [Mass Surveillance](https://www.privacyguides.org/en/basics/common-threats/#mass-surveillance-programs)
- [Surveillance Capitalism](https://www.privacyguides.org/en/basics/common-threats/#surveillance-as-a-business-model)

These recommendations for encrypted **real-time communication** are great for securing your sensitive communications. These instant messengers come in the form of many [types of communication networks](https://www.privacyguides.org/en/advanced/communication-network-types/).

[Video: It's time to stop using SMS](https://www.privacyguides.org/videos/2025/01/24/its-time-to-stop-using-sms-heres-why)

## Signal

![Signal logo](https://www.privacyguides.org/en/assets/img/messengers/signal.svg)

**Signal** is a mobile app developed by Signal Messenger LLC. The app provides instant messaging and calls secured with the Signal protocol, an extremely secure encryption protocol which supports forward secrecy[2](https://www.privacyguides.org/en/real-time-communication/#fn:1) and post-compromise security.[3](https://www.privacyguides.org/en/real-time-communication/#fn:2)

[Homepage](https://signal.org/) [Privacy Policy](https://signal.org/legal/#privacy-policy "Privacy Policy") [Documentation](https://support.signal.org/ "Documentation") [Source Code](https://github.com/signalapp "Source Code") [Contribute](https://signal.org/donate "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms)
- [App Store](https://apps.apple.com/app/id874139669)
- [GitHub](https://github.com/signalapp/Signal-Android/releases)
- [Android](https://signal.org/android/apk)
- [Windows](https://signal.org/download/windows)
- [macOS](https://signal.org/download/macos)
- [Linux](https://signal.org/download/linux)

Signal requires your phone number for registration, however you should create a username to hide your phone number from your contacts:

1. In Signal, open the app's settings and tap your account profile at the top.
2. Tap **Username** and choose **Continue** on the "Set up your Signal username" screen.
3. Enter a username. Your username will always be paired with a unique set of digits to keep your username unique and prevent people from guessing it. For example if you enter "John" your username might end up being `@john.35`. By default, only 2 digits are paired with your username when you create it, but you can add more digits until you reach the username length limit (32 characters).
4. Go back to the main app settings page and select **Privacy**.
5. Select **Phone Number**.
6. Change the **Who Can See My Number** setting to **Nobody**.
7. (Optional) Change the **Who Can Find Me By Number** setting to **Nobody** as well, if you want to prevent people who already have your phone number from discovering your Signal account/username

We have some additional tips on configuring and hardening your Signal installation:

[Signal Configuration and Hardening](https://blog.privacyguides.org/2022/07/07/signal-configuration-and-hardening)

Contact lists on Signal are encrypted using your Signal PIN and the server does not have access to them. Personal profiles are also encrypted and only shared with contacts you chat with.

Signal supports [private groups](https://signal.org/blog/signal-private-group-system), where the server has no record of your group memberships, group titles, group avatars, or group attributes. Signal has minimal metadata when [Sealed Sender](https://signal.org/blog/sealed-sender) is enabled. The sender address is encrypted along with the message body, and only the recipient address is visible to the server. Sealed Sender is only enabled for people in your contacts list, but can be enabled for all recipients with the increased risk of receiving spam.

The protocol was independently [audited](https://eprint.iacr.org/2016/1013.pdf) in 2016. The specification for the Signal protocol can be found in their [documentation](https://signal.org/docs).

### Molly (Android)

If you use Android and your threat model requires protecting against [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals) you may consider using this alternative app, which features a number of security and usability improvements, to access the Signal network.

![Molly logo](https://www.privacyguides.org/en/assets/img/messengers/molly.svg)

**Molly** is an alternative Signal client for Android which allows you to encrypt the local database with a passphrase at rest, to have unused RAM data securely shredded, to route your connection via Tor, and [more](https://blog.privacyguides.org/2022/07/07/signal-configuration-and-hardening#privacy-and-security-features). It also has usability improvements including scheduled backups, automatic locking, and the ability to use your Android phone as a linked device instead of the primary device for a Signal account.

[Homepage](https://molly.im/) [Privacy Policy](https://signal.org/legal/#privacy-policy "Privacy Policy") [Documentation](https://github.com/mollyim/mollyim-android/wiki "Documentation") [Source Code](https://github.com/mollyim/mollyim-android "Source Code") [Contribute](https://opencollective.com/mollyim "Contribute")

Downloads

- [F-Droid](https://molly.im/fdroid)
- [Accrescent](https://accrescent.app/app/im.molly.app)
- [GitHub](https://github.com/mollyim/mollyim-android/releases)

Molly is updated every two weeks to include the latest features and bug fixes from Signal. The exception is security issues, which are patched as soon as possible. That said, you should be aware that there might be a slight delay compared to upstream, which may affect actions such as [migrating from Signal to Molly](https://github.com/mollyim/mollyim-android/wiki/Migrating-From-Signal#migrating-from-signal).

Note that you are trusting multiple parties by using Molly, as you now need to trust the Signal team _and_ the Molly team to deliver safe and timely updates.

**Molly-FOSS** is a version of Molly which removes proprietary code like the Google services used by both Signal and Molly at the expense of some features (like battery-saving push notifications via Google Play Services). You can set up push notifications without Google Play Services in either version of Molly with [UnifiedPush](https://unifiedpush.org/). Using this notification delivery method requires access to a [MollySocket](https://github.com/mollyim/mollysocket) server, but you can choose a public MollySocket instance for this.[1](https://www.privacyguides.org/en/real-time-communication/#fn:3)

Both versions of Molly provide the same security improvements and support [reproducible builds](https://github.com/mollyim/mollyim-android/tree/main/reproducible-builds), meaning it's possible to confirm that the compiled APKs match the source code.

## SimpleX Chat

![SimpleX Chat logo](https://www.privacyguides.org/en/assets/img/messengers/simplex.svg)

**SimpleX Chat** is an instant messenger that doesn't depend on any unique identifiers such as phone numbers or usernames. Its decentralized network makes SimpleX Chat an effective tool against [Censorship](https://www.privacyguides.org/en/basics/common-threats/#avoiding-censorship).

[Homepage](https://simplex.chat/) [Privacy Policy](https://simplex.chat/privacy "Privacy Policy") [Documentation](https://simplex.chat/docs/simplex.html "Documentation") [Source Code](https://github.com/simplex-chat "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app)
- [App Store](https://apps.apple.com/app/id1605771084)
- [GitHub](https://github.com/simplex-chat/simplex-chat/releases)
- [Windows](https://simplex.chat/downloads/#desktop-app)
- [macOS](https://simplex.chat/downloads/#desktop-app)
- [Linux](https://simplex.chat/downloads/#desktop-app)
- [Flathub](https://flathub.org/en/apps/chat.simplex.simplex)

SimpleX Chat provides direct messaging, group chats, and E2EE calls secured with the [SimpleX Messaging Protocol](https://github.com/simplex-chat/simplexmq/blob/stable/protocol/simplex-messaging.md), which uses double ratchet encryption with quantum resistance. Additionally, SimpleX Chat provides metadata protection by using unidirectional ["simplex queues"](https://github.com/simplex-chat/simplexmq/blob/stable/protocol/simplex-messaging.md#simplex-queue) to deliver messages.

To participate in conversations on SimpleX Chat, you must scan a QR code or click an invite link. This allows you to verify a contact out-of-band, which protects against man-in-the-middle attacks by network providers. Your data can be exported and imported onto another device, as there are no central servers where this is backed up.

You can find a full list of the privacy and security [features](https://github.com/simplex-chat/simplex-chat#privacy-and-security-technical-details-and-limitations) implemented in SimpleX Chat in the app's repository.

SimpleX Chat was independently audited in [July 2024](https://simplex.chat/blog/20241014-simplex-network-v6-1-security-review-better-calls-user-experience.html#simplex-cryptographic-design-review-by-trail-of-bits) and in [October 2022](https://simplex.chat/blog/20221108-simplex-chat-v4.2-security-audit-new-website).

## Briar

![Briar logo](https://www.privacyguides.org/en/assets/img/messengers/briar.svg)

**Briar** is an encrypted instant messenger that [connects](https://briarproject.org/how-it-works) to other clients using the [Tor network](https://www.privacyguides.org/en/alternative-networks/#tor), making it an effective tool at circumventing [Censorship](https://www.privacyguides.org/en/basics/common-threats/#avoiding-censorship). Briar can also connect via Wi-Fi or Bluetooth when in local proximity. Briar’s local mesh mode can be useful when internet availability is a problem.

[Homepage](https://briarproject.org/) [Privacy Policy](https://briarproject.org/privacy-policy "Privacy Policy") [Documentation](https://code.briarproject.org/briar/briar/-/wikis/home "Documentation") [Source Code](https://code.briarproject.org/briar/briar "Source Code") [Contribute](https://code.briarproject.org/briar/briar#donate "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=org.briarproject.briar.android)
- [Windows](https://briarproject.org/download-briar-desktop)
- [Linux](https://briarproject.org/download-briar-desktop)
- [Flathub](https://flathub.org/apps/details/org.briarproject.Briar)

To add a contact on Briar, you must both add each other first. You can either exchange `briar://` links or scan a contact’s QR code if they are nearby.

Briar has a fully [published specification](https://code.briarproject.org/briar/briar-spec). Briar supports forward secrecy[2](https://www.privacyguides.org/en/real-time-communication/#fn:1) by using the Bramble [Handshake](https://code.briarproject.org/briar/briar-spec/blob/master/protocols/BHP.md) and [Transport](https://code.briarproject.org/briar/briar-spec/blob/master/protocols/BTP.md) protocol.

The client software was independently [audited](https://briarproject.org/news/2017-beta-released-security-audit), and the anonymous routing protocol uses the Tor network which has also been audited.

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

### Minimum Requirements

- Must have open-source clients.
- Must not require sharing personal identifiers (particularly phone numbers or emails) with contacts.
- Must use E2EE for private messages by default.
- Must support E2EE for all messages.
- Must support forward secrecy[2](https://www.privacyguides.org/en/real-time-communication/#fn:1)
- Must have a published audit from a reputable, independent third party.

### Best-Case

Our best-case criteria represents what we would like to see from the perfect project in this category. Our recommendations may not include any or all of this functionality, but those which do may rank higher than others on this page.

- Should support future secrecy (post-compromise security)[3](https://www.privacyguides.org/en/real-time-communication/#fn:2)
- Should have open-source servers.
- Should use a decentralized network, i.e. [federated or P2P](https://www.privacyguides.org/en/advanced/communication-network-types/).
- Should use E2EE for all messages by default.
- Should support Linux, macOS, Windows, Android, and iOS.

* * *

1. You may refer to this step-by-step tutorial in German on how to set up UnifiedPush as the notification provider for Molly: [https://kuketz-blog.de/messenger-wechsel-von-signal-zu-molly-unifiedpush-mollysocket-ntfy](https://kuketz-blog.de/messenger-wechsel-von-signal-zu-molly-unifiedpush-mollysocket-ntfy). [↩](https://www.privacyguides.org/en/real-time-communication/#fnref:3)

2. [Forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy) is where keys are rotated very frequently, so that if the current encryption key is compromised, it does not expose **past** messages as well. [↩](https://www.privacyguides.org/en/real-time-communication/#fnref:1) [↩](https://www.privacyguides.org/en/real-time-communication/#fnref2:1) [↩](https://www.privacyguides.org/en/real-time-communication/#fnref3:1)

3. Future secrecy (or [post-compromise security](https://eprint.iacr.org/2016/221.pdf)) is a feature where an attacker is prevented from decrypting **future** messages after compromising a private key, unless they compromise more session keys in the future as well. This effectively forces the attacker to intercept all communication between parties since they lose access as soon as a key exchange occurs that is not intercepted. [↩](https://www.privacyguides.org/en/real-time-communication/#fnref:2) [↩](https://www.privacyguides.org/en/real-time-communication/#fnref2:2)


Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).