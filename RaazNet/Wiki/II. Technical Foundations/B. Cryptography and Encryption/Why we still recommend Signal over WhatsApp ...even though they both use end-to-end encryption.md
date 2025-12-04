Blog › Why we still recommend Signal over WhatsApp ...even though they both use end-to-end encryption

# [Anchor](https://securityinabox.org/en/blog/why-we-still-recommend-signal-over-whatsapp/\#why-we-still-recommend-signal-over-whatsapp-even-though-they-bot) Why we still recommend Signal over WhatsApp ...even though they both use end-to-end encryption

By Maria Xynou & Chris Walker

Posted 2016.05.23

If you're using the latest version of WhatsApp, then you might have noticed the following notification:

![](https://securityinabox.org/media/en/blog/whatsapp-crypto.png)

WhatsApp Crypto message

Or you might have read about this when it was all over the [news](https://www.theguardian.com/technology/2016/apr/05/whatsapp-rolls-out-full-encryption-to-a-billion-messenger-users).

WhatsApp's collaboration with Open Whisper Systems recently brought _end-to-end encryption_ to the lives of a billion people around the world. (Open Whisper Systems develops Signal, an open source mobile messaging and VoIP app.) When WhatsApp integrated the encryption protocol developed for Signal, many of us began using end-to-end encryption without even realizing it.

Undoubtedly, this is an exciting and important development that will help protect the privacy of users all over the world. In this post, however, we would like to explain why we recommend Signal over WhatsApp, even though they both use the _same protocol_ for end-to-end encryption.

## [Anchor](https://securityinabox.org/en/blog/why-we-still-recommend-signal-over-whatsapp/\#source-code) Source code

We would like to start off by congratulating WhatsApp, not only for taking significant measures to protect the privacy of their users, but also for choosing to adopt an open encryption protocol that has been vetted by security experts rather than coming up with yet another proprietary encryption scheme with little or no external review.

Crypto is not the only aspect of security, however. Among other factors, the security of an app also depends on how an encryption protocol is integrated. When software is open source, we are able to review it, see how it has been implemented and verify that it does not contain malicious code. Closed source software, on the other hand, requires that we trust the claims of its developers.

While WhatsApp relies on the Signal protocol, which is an open standard, to encrypt its users' communications, the app itself is closed source. We trust Open Whisper Systems to have properly integrated the Signal protocol into WhatsApp, but the closed source nature of the app prevents us from identifying other aspects of the app that could impact our security.

Signal, on the other hand, is open source. As a result, we can verify that our communications are properly encrypted and review the overall security of the app.

## [Anchor](https://securityinabox.org/en/blog/why-we-still-recommend-signal-over-whatsapp/\#secure-data-storage) Secure data storage

The Signal protocol that was recently integrated into WhatsApp is a _communications_ protocol, which means that it only encrypts data _in transit_. It does _not_ encrypt data, such as our messaging history, that is stored on our phones.

Signal addresses this by providing its users with the option to (encrypt messages stored on their phones with a [passphrase](https://github.com/WhisperSystems/Signal-Android/wiki/Using-Signal#secure-storage), thus protecting those messages from anyone who gains physical access to their device. WhatsApp, on the other hand, [does not currently allow users to secure the messages stored on their phones](https://www.whatsapp.com/security/).

## [Anchor](https://securityinabox.org/en/blog/why-we-still-recommend-signal-over-whatsapp/\#verification) Verification

An essential component of digital security is the ability to verify that we are actually sending data to, and receiving data from, the person with whom we believe we are communicating. Without this ability, it is possible for someone to sit between us on the network when we first get in touch, decrypt our messages, record them, re-encrypt them and relay them back and forth. This is called a _man-in-the-middle_ attack.

In this scenario, merely recognizing our correspondent's voice is not enough to guarantee that our communication is properly encrypted. For that, we need some kind of cryptographic identity verification mechanism.

Both WhatsApp and Signal support identity verification for messages and voice calls. For messages, they rely on the same mechanism: users compare identity key fingerprints, then flag a contact as verified. For voice calls, however, the two apps work differently. Signal’s voice encryption protocol makes it easy for users to verify each call by reading off two words and making sure they match. WhatsApp’s voice call verification, however, depends on users having previously verified one another for messaging by comparing fingerprints.

## [Anchor](https://securityinabox.org/en/blog/why-we-still-recommend-signal-over-whatsapp/\#business-model) Business model

WhatsApp is owned by Facebook, while Signal is owned by [Open Whisper Systems](https://whispersystems.org/). They have very different business models.

It's well-known that advertising is at the heart of Facebook's business model, which is fueled by the vast quantities of data that users hand over to the company through its various services. Open Whisper Systems, on the other hand, is a _non-profit_, grant-funded group of free software developers whose [mission](https://whispersystems.org/) is to _“advance the state of the art for secure communication, while simultaneously making it easy for everyone to use”_.

It’s important to note that while the Signal protocol encrypts the content of our communications, it does not encrypt _metadata_ – information about information - such as who we contact, when and from where. Given Facebook’s willingness to implement end-to-end encryption in WhatsApp, which prevents even the company itself from accessing some of its users’ data, one can't help but wonder if the value has been in the metadata all along.

Unlike content data, which is harder and more expensive to process and retain, metadata is ideally suited to automated analysis by a computer. It can be stored in large quantities and reveals information (such as who you contacted, when and where) that is very difficult – if not impossible – to deny. Using metadata, analysts can map out an individual’s [political affiliation, interests, economic background, location and habits](http://www.theatlantic.com/technology/archive/2013/03/armed-with-facebook-likes-alone-researchers-can-tell-your-race-gender-and-sexual-orientation/273963/), as well as the network of people with whom that individual communicates. This information can be used to create group and individual profiles that are in great demand by an advertising industry desperate to know its audience.

Advertising might seem harmless, but it's important to remember that we are rarely in control of the profiles being created about us. As a result, these profiles may or may not be accurate. And regardless of the accuracy of our profiles, [research](http://www.newamerica.org/downloads/OTI-Data-an-Discrimination-FINAL-small.pdf) has shown that profiling can lead to various forms of discrimination. While it's not clear whether and to what extent WhatsApp users' metadata feeds into Facebook's advertising business model, it remains an important question. As Open Whisper Systems is not in the data business, we believe Signal is more likely to protect our metadata.

That said, it’s worth noting that Signal’s reliance on the Google Cloud Messaging platform means that Google — which is, of course, in the data business — does have access to some of the metadata produced by Signal. They know the current _IP address_ of any device that receives a Signal message, for example, but Signal’s architecture hides as much of this metadata as possible. The Signal protocol can be used independently from Google Play Services via [LibreSignal](https://libraries.io/github/LibreSignal/LibreSignal), a fork of Signal, which can be installed from [F-Droid](https://f-droid.org/), a free and open source Android app repository.

## [Anchor](https://securityinabox.org/en/blog/why-we-still-recommend-signal-over-whatsapp/\#using-signal) Using Signal

Today we are releasing a new [tool guide](https://securityinabox.org/en/guide/signal/android) that explains, step-by-step, how to install and use Signal, if you're not already doing so.