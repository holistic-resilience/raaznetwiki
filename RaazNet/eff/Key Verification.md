---
title: "Key Verification"
tags: [privacy, security, digital-rights]
category: "General Security"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users]
topics: ["Digital Security", "Privacy"]
summary: "Security and privacy guide from EFF Surveillance Self-Defense"
source: "Electronic Frontier Foundation (EFF)"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy"]
estimated_read_time: "5 minutes"



---

[Skip to main content](https://ssd.eff.org/module/key-verification#main-content)

- [About](https://ssd.eff.org/pages/about-surveillance-self-defense)
- [Language](https://ssd.eff.org/module/key-verification#)  - [English](https://ssd.eff.org/module/key-verification)
  - [አማርኛ](https://ssd.eff.org/am/module/%E1%8B%A8%E1%89%81%E1%88%8D%E1%8D%8D-%E1%88%9B%E1%88%A8%E1%8C%8B%E1%8C%88%E1%8C%AB-%E1%89%A5%E1%88%8D%E1%88%83%E1%89%B5)
  - [العربية](https://ssd.eff.org/ar/module/%D8%A7%D9%84%D8%AA%D8%AD%D9%82%D9%82-%D9%85%D9%86-%D8%A7%D9%84%D9%85%D9%81%D8%A7%D8%AA%D9%8A%D8%AD)
  - [Español](https://ssd.eff.org/es/module/verificando-las-llaves)
  - [Français](https://ssd.eff.org/fr/module/v%C3%A9rification-des-cl%C3%A9s)
  - [Русский](https://ssd.eff.org/ru/module/%D0%B2%D0%B5%D1%80%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F-%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%B9)
  - [Türkçe](https://ssd.eff.org/tr/module/anahtar-do%C4%9Frulamas%C4%B1)
  - [Tiếng Việt](https://ssd.eff.org/vi/module/ki%E1%BB%83m-ch%E1%BB%A9ng-ch%C3%ACa-kh%C3%B3a)
  - [Português](https://ssd.eff.org/pt-br/module/verificacao-de-chaves)
  - [Mandarin](https://ssd.eff.org/zh-hans/module/fdabd489-f5e2-47fc-9163-7aba74f0c21f)
  - [Burmese](https://ssd.eff.org/my/module/%E1%80%85%E1%80%80%E1%80%AC%E1%80%B8%E1%80%9D%E1%80%BE%E1%80%80%E1%80%BA%E1%80%9E%E1%80%B1%E1%80%AC%E1%80%B7-%E1%80%85%E1%80%85%E1%80%BA%E1%80%86%E1%80%B1%E1%80%B8%E1%80%A1%E1%80%90%E1%80%8A%E1%80%BA%E1%80%95%E1%80%BC%E1%80%AF%E1%80%81%E1%80%BC%E1%80%84%E1%80%BA%E1%80%B8)
  - [پښتو](https://ssd.eff.org/ps/module/key-verification)
  - [ภาษาไทย](https://ssd.eff.org/th/module/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A2%E0%B8%B7%E0%B8%99%E0%B8%A2%E0%B8%B1%E0%B8%99%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%96%E0%B8%B9%E0%B8%81%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%B5%E0%B8%A2%E0%B9%8C)
  - [اردو](https://ssd.eff.org/ur/module/%DA%A9%D9%84%DB%8C%D8%AF%DB%8C-%D8%AA%D8%B5%D8%AF%DB%8C%D9%82)
  - [More Translations](https://ssd.eff.org/en/other-translations)
- [Index](https://ssd.eff.org/#index)
- KeywordsSearch

[×](https://ssd.eff.org/module/key-verification#)

# Key Verification

**Last Reviewed**: January 01, 2025

Read [Key Concepts in Encryption](https://ssd.eff.org/en/module/key-concepts-encryption) first if [encryption ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/encryption) keys are unfamiliar to you.

When you communicate online using [end-to-end encryption ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/end-to-end-encryption), each person you send a message to has their own unique public [key ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/key). You use this key to [encrypt ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/encrypt) messages to them, so that only they can decode them.

Suppose someone claiming to be your friend Esra’a sends you a chat request on an encrypted messenger application like WhatsApp or Signal. Even though you think your messenger is using Esra’a’s public key, you may be encrypting your messages using a key that came from a different person entirely—which means this fake Esra’a will be able to decode all your future messages.

To make sure you are using someone’s correct [encryption key ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/encryption-key) (and that others know that they are using the correct encryption key for you), it’s important to use verified keys. Today, there are different methods of verifying keys across different services and that are appropriate for different [security plans](https://ssd.eff.org/module/your-security-plan).

## How Key Transparency Works Behind the Scenes to Verify Keys [\#](https://ssd.eff.org/module/key-verification\#how-key-transparency-works-behind-the-scenes-to-verify-keys)

In most encrypted messaging apps, [key verification ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/key-verification) is done manually from a screen that displays a code that both parties bring up and compare, or a QR code to scan (we’ll get into this more below). When someone changes phones, they often change keys, and might have a key for each device they use. This makes verifying that someone is who they say they are tedious, especially in a group chat.

Key transparency, such as what’s [used by WhatsApp](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/) and on [iMessage](https://security.apple.com/blog/imessage-contact-key-verification/) (as an [opt-in](https://support.apple.com/en-us/118246) feature), hopes to solve this problem. With key transparency, the public key is kept on a server, which the app can check and verify. When a key change is recorded, it’s added to the record, and that record can be publicly audited to ensure the chat provider is doing what they say they are doing. This partially automates key verification, which can check that key against the published audit without you having to do so in person. While Apple Messages automatically uses key transparency to verify keys every time a contact's key changes, WhatsApp only provides it as an alternative to manual verification in the key verification screen.

Not every end-to-end communication app uses key transparency, nor does it remove the ability to verify keys manually when you need to. For example, key transparency adds a layer of security to group chats, where there are so many people in the chat it’s not feasible to verify the keys every single time one changes. It does not replace the need to verify for more high- [risk ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/risk-assessment) situations, like when a whistleblower reaches out to a journalist.

## When and How to Manually Verify Keys [\#](https://ssd.eff.org/module/key-verification\#when-and-how-to-manually-verify-keys)

Different secure messaging systems have different ways to manually verify keys, but all of them encourage you to check those keys outside of the messaging system itself. This is called “ [out-of-band verification ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/out-of-band-verification).” So in our example, you should find some other way to check that online Esra’a is the same as real life Esra’a. You can do this by calling Esra’a on the phone, or meeting Esra’a in person to verify the public encryption key or safety number that you’re seeing actually belongs to her.

Why use out-of-band verification?

- Without definitively knowing who a key came from, you can’t rely on a secure messaging system since it’s not completely secure yet.
- It’s often harder to fake someone’s communications in more than one service. For instance, if you ask to verify Signal fingerprints using a FaceTime video chat, the fake person would have to be able to both run a fake Signal account and a fake FaceTime account, and disguise themselves as your friend on video.
- When you ask for secret information within the channel itself (“in-band verification”), there’s a risk that an imposter might secretly be talking to both parties, called a “man-in-the-middle” or “machine-in-the-middle” [attack ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/attack). If that’s happening, asking for secret information like a [security question ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/security-question) or a [key fingerprint ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/key-fingerprint) won’t be enough (we’ll get into this more below). For example, if you ask something like, “What was I wearing last time we hung out?” an imposter could ask the person that question and immediately send you real answers. And if you ask for a key fingerprint, the attacker would just send their own [fingerprint ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/fingerprint), and you would never know.

You should verify keys when you use a new messaging tool to communicate, or when someone’s keys change. A person’s keys might change when they purchase a new phone or if they add a new device (like a tablet or computer).

### Verifying Keys Out-of-Band [\#](https://ssd.eff.org/module/key-verification\#verifying-keys-out-of-band)

Encryption keys are very long numbers, which makes them hard to read aloud and check manually. To make key verification easier, communication software can show you a “fingerprint” or “safety number” based on the key, which is shorter and easier to check. Fingerprints can be a smaller number, a set of common words, or even a graphic or image. Often, they are embedded in a QR code to make checking them even easier.

To verify keys, your contact can read or show you the fingerprint of their key, while you check it against the fingerprint of the key you have for them on your device. After you’ve verified your contact’s key, they can verify your key by asking you to read or show them your key fingerprint as they check it against the copy on their device. Once you both know you have the right keys, you can communicate more securely. It’s easiest and best to do this in person, but you can also do it through other tools, like video chat or another messaging app (though the latter has additional risks).

### Verifying Keys In Person [\#](https://ssd.eff.org/module/key-verification\#verifying-keys-in-person)

Verifying keys in person is the most ideal method because it is easier to confirm someone is who they say they are when you’re face-to-face with them.

In person, you have your public key fingerprint available and your friend confirms that it matches what’s on their device. The easiest way to do this is if the app makes a QR code available, in which case your friend can just scan your QR code and you’re good to go. For other apps, your friend will have to double-check that every single character from your public key fingerprint matches what they have for your public key fingerprint. It’s a little tedious, but it’s really worth doing. The in-person method might happen when people exchange business cards with their public key fingerprints, or when colleagues see each other at a meeting.

Each end-to-end encrypted messaging app is different and some provide alternative ways to check key fingerprints. Currently, there is no universal term for what the practice is called and how it is implemented.

Let’s imagine that An Ming meets her friend Ghassan at an event. They decide that it’s best to communicate with each other using an end-to-end encryption app on their smartphones, so they install Signal. While An Ming and Ghassan are together, they take advantage of these apps’ key verification capabilities by scanning each other’s [QR code to verify their safety numbers](https://ssd.eff.org/module/how-to-use-signal#verify-safety-numbers).

|     |
| --- |
| ![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1943/image-20250102103045-1.png) |
| _Two people hold up their smartphones with QR codes and a string of random letters and numbers visible on their screens. They verify each other’s key fingerprints by scanning the other person’s QR code with their phone cameras. Locks and green checkmarks float above their phones._ |

### Verifying keys over another medium [\#](https://ssd.eff.org/module/key-verification\#verifying-keys-over-another-medium)

If you can’t verify keys in person, you can contact your friend using a different way of communication—a way other than the one you’re using to verify keys.

For example, if you’re trying to verify Signal safety numbers with someone, you could use the telephone or video chat, or even another end-to-end encrypted communication app, like WhatsApp, to do so. It would be difficult for an [adversary ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/adversary) to intercept your messages from all these different mediums simultaneously, but not impossible for a sufficiently determined adversary. Using video chat makes impersonating you harder than using another text-based app; you’ll have to make a decision that trades off security for convenience based on your personal [threat model](https://ssd.eff.org/module/your-security-plan). A different encrypted app that you’ve already verified keys on is best, but not always possible.

Locating your key can vary by app, but the key verification methods remain approximately the same. You can either read your key’s fingerprint aloud (if you are face-to-face on video or using the telephone) or you can copy-and-paste it into a communications program. Whichever you choose, it is important that you check every single letter and number.

Lastly, many of these end-to-end encryption apps indicate if the keys change. It’s important to be on the lookout for when your friends’ keys change—be sure to confirm that this is an expected change with them, and re-verify their new keys. You can do so in person or over another medium.

Ready to give key verification a try for yourself with a friend? Here’s how to verify keys on [Signal](https://ssd.eff.org/module/how-to-use-signal#verify-safety-numbers), [WhatsApp](https://ssd.eff.org/module/how-to-use-whatsapp#using-whatsapp), or [Apple’s Messages](https://support.apple.com/en-us/118246).

For more information about public keys and how key verification works, check out our Surveillance Self-Defense guides on [Key Concepts in Encryption](https://ssd.eff.org/en/module/key-concepts-encryption), and [A Deep Dive on End-to-End Encryption](https://ssd.eff.org/en/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work).

- [Copyright (CC BY)](https://www.eff.org/copyright)
- [Privacy](https://www.eff.org/policy)