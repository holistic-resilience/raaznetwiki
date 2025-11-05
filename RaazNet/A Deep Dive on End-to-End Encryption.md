---
title: "A Deep Dive on End-to-End Encryption"
tags: [privacy, security, digital-rights, encryption, cryptography, privacy]
category: "Encryption"
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

[Skip to main content](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work#main-content)

- [About](https://ssd.eff.org/pages/about-surveillance-self-defense)
- [Language](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work#)  - [English](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work)
  - [አማርኛ](https://ssd.eff.org/am/module/%E1%8B%A8%E1%8A%A0%E1%8B%B0%E1%89%A3%E1%89%A3%E1%8B%AD-%E1%89%81%E1%88%8D%E1%8D%8D-%E1%88%B5%E1%8A%90-%E1%88%98%E1%88%B0%E1%8B%8D%E1%88%AD-%E1%8A%A5%E1%8A%93-pgp-%E1%88%98%E1%8C%8D%E1%89%A2%E1%8B%AB)
  - [العربية](https://ssd.eff.org/ar/module/%D9%85%D9%82%D8%AF%D9%85%D8%A9-%D8%A5%D9%84%D9%8A-%D8%A7%D9%84%D8%AA%D8%B9%D9%85%D9%8A%D8%A9-%D9%88%D8%A8%D9%8A-%D8%AC%D9%8A-%D8%A8%D9%8A)
  - [Español](https://ssd.eff.org/es/module/una-mirada-en-profundidad-al-cifrado-de-extremo-extremo-%C2%BFc%C3%B3mo-funcionan-los-sistemas-de)
  - [Français](https://ssd.eff.org/fr/module/une-pr%C3%A9sentation-approfondie-du-chiffrement-de-bout-en-bout-comment-les-syst%C3%A8mes-de)
  - [Русский](https://ssd.eff.org/ru/module/%D0%B3%D0%BB%D1%83%D0%B1%D0%BE%D0%BA%D0%BE%D0%B5-%D0%BF%D0%BE%D0%B3%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D0%BC%D0%B8%D1%80-%D1%81%D0%BA%D0%B2%D0%BE%D0%B7%D0%BD%D0%BE%D0%B3%D0%BE-%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC-%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8-%D1%81-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D0%BC)
  - [Türkçe](https://ssd.eff.org/tr/module/a%C3%A7%C4%B1k-anahtar-kriptografisi-ve-pgpye-giri%C5%9F)
  - [Tiếng Việt](https://ssd.eff.org/vi/module/gi%E1%BB%9Bi-thi%E1%BB%87u-v%E1%BB%81-m%E1%BA%ADt-m%C3%A3-kh%C3%B3a-c%C3%B4ng-khai-v%C3%A0-pgp)
  - [Português](https://ssd.eff.org/pt-br/module/uma-introducao-criptografia-de-chave-publica-e-pgp)
  - [Mandarin](https://ssd.eff.org/zh-hans/module/08d874d3-0e44-487b-b5ae-34299cb418f9)
  - [Burmese](https://ssd.eff.org/my/module/%E1%80%A1%E1%80%85-%E1%80%A1%E1%80%86%E1%80%AF%E1%80%B6%E1%80%B8%E1%80%80%E1%80%AF%E1%80%92%E1%80%BA%E1%80%96%E1%80%BC%E1%80%84%E1%80%B7%E1%80%BA%E1%80%95%E1%80%BC%E1%80%B1%E1%80%AC%E1%80%84%E1%80%BA%E1%80%B8%E1%80%9C%E1%80%B2%E1%80%81%E1%80%BC%E1%80%84%E1%80%BA%E1%80%B8%E1%80%A1%E1%80%AC%E1%80%B8-%E1%80%91%E1%80%B2%E1%80%91%E1%80%B2%E1%80%9D%E1%80%84%E1%80%BA%E1%80%9D%E1%80%84%E1%80%BA%E1%80%9C%E1%80%B1%E1%80%B7%E1%80%9C%E1%80%AC%E1%80%81%E1%80%BC%E1%80%84%E1%80%BA%E1%80%B8-%E1%80%A1%E1%80%99%E1%80%BB%E1%80%AC%E1%80%B8%E1%80%9E%E1%80%AF%E1%80%B6%E1%80%B8-%E1%80%85%E1%80%80%E1%80%AC%E1%80%B8%E1%80%9D%E1%80%BE%E1%80%80%E1%80%BA%E1%80%9E%E1%80%B1%E1%80%AC%E1%80%B7%E1%80%96%E1%80%BC%E1%80%84%E1%80%B7%E1%80%BA-%E1%80%80%E1%80%AF%E1%80%92%E1%80%BA)
  - [پښتو](https://ssd.eff.org/ps/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work)
  - [ภาษาไทย](https://ssd.eff.org/th/module/%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%9A%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%95%E0%B9%89%E0%B8%99%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A3%E0%B8%AB%E0%B8%B1%E0%B8%AA%E0%B8%84%E0%B8%B5%E0%B8%A2%E0%B9%8C%E0%B8%AA%E0%B8%B2%E0%B8%98%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B8%B0-public-key-cryptography-%E0%B9%81%E0%B8%A5%E0%B8%B0-pgp)
  - [اردو](https://ssd.eff.org/ur/module/%D8%B9%D9%88%D8%A7%D9%85%DB%8C-%DA%A9%D9%84%DB%8C%D8%AF%DB%8C-%D8%B1%D9%85%D8%B2-%D9%86%DA%AF%D8%A7%D8%B1%DB%8C-%D8%A7%D9%88%D8%B1-%D9%BE%DB%8C%DB%94%D8%AC%DB%8C%DB%94%D9%BE%DB%8C-%DA%A9%D8%A7-%D8%A7%DB%8C%DA%A9-%D8%AA%D8%B9%D8%A7%D8%B1%D9%81)
  - [More Translations](https://ssd.eff.org/en/other-translations)
- [Index](https://ssd.eff.org/#index)
- KeywordsSearch

[×](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work#)

# A Deep Dive on End-to-End Encryption: How Do Public Key Encryption Systems Work?

**Last Reviewed**: January 01, 2025

If you haven’t yet, we recommend reading a few guides before this one, to help cement some of the concepts discussed here: [What Should I Know About Encryption?](https://ssd.eff.org/module/what-should-i-know-about-encryption), [Key Concepts of Encryption](https://ssd.eff.org/module/key-concepts-encryption), and [Key Verification](https://ssd.eff.org/module/key-verification).

If used correctly, [end-to-end encryption ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/end-to-end-encryption) can help protect the contents of your messages, text, and files from being read by anyone except their intended recipients. End-to-end encryption tools make messages unreadable to eavesdroppers on the network, as well as to service providers themselves. They can also prove a message came from a specific person and was not altered.

Once complicated to set up, end-to-end encryption tools are far more usable than they used to be. A secure messaging tool like [Signal](https://ssd.eff.org/module/how-to-use-signal) is a good example of an app that uses end-to-end encryption to [encrypt ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/encrypt) messages between the sender and intended recipient while remaining easy to use. Even the largest platforms, like WhatsApp and Facebook Messenger support end-to-end encryption without you needing to do any sort of set-up ahead of time.

The type of [encryption ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/encryption) we’re talking about in this guide, which end-to-end encryption tools rely on, is called public [key ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/key) [cryptography ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/cryptography) (sometimes referred to as [public key encryption ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/public-key-encryption)).

Understanding the underlying principles of public key cryptography will help you to use these tools safely. There are limits to what public key cryptography can and can’t do, and it’s helpful to understand those limits

## What Does Encryption Do? [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#what-does-encryption-do)

Here’s how encryption works when sending a secret message:

1. A clearly readable message is first encrypted into a scrambled message that is incomprehensible to anyone looking at it (“hello mum” turns into “OhsieW5ge+osh1aehah6”).
2. The encrypted message is sent over the internet, where, if they’re watching, eavesdroppers would only see the scrambled message (“OhsieW5ge+osh1aehah6”).
3. When it arrives at its destination, the intended recipient, and only the intended recipient, has some way of decrypting it back into the original message (“OhsieW5ge+osh1aehah6” is turned back into “hello mum”).

## Symmetric Encryption: A Story of Passing Secret Notes with a Single Key [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#symmetric-encryption-a-story-of-passing-secret-notes-with-a-single-key)

Let’s start with an example from history: the Caesar cipher.

Julia wants to send her friend César a note saying: “Meet me in the garden.” But she doesn’t want her classmates to see it.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1955/image-20250102104755-1.png)

If Julia passes the note along as-is, it gets passed through a bunch of intermediary classmates before reaching César. Although neutral, the intermediaries are still nosy, and can sneak a peek at the message before passing it on. They can also make copies of the message before passing it on and record the time Julia sends her message to César.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1946/image-20250102104755-2.png)

So, to protect the privacy of the conversation, Julia could decide to encrypt her message with a "key of three," shifting the letters down the alphabet by three. For example, A would be D, B would be E, and so on.

If Julia and César use a simple key of three to encrypt, and a key of three to [decrypt ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/decrypt), then their gibberish encrypted message might be enough to fool their classmates—but is still easy to crack. Any of their classmates could “ [brute force ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/brute-force)” the key by trying all the possible combinations until they figured out a word or two. In other words, they can persistently guess until they get the answer to decrypt the message.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1944/image-20250102104755-3.png)

The method of shifting the alphabet by three characters is a historic example of encryption used by Julius Caesar, hence, _the Caesar cipher_. When there is one key to both encrypt and decrypt, like in this example, it is called symmetric cryptography.

The Caesar cipher is a weak form of [symmetric cryptography](https://ssd.eff.org/module/key-concepts-encryption#one-key-or-many-keys). Thankfully, encryption has come a long way since then. Instead of just shifting the letters of a message by a few characters, keys can now use math and the help of computers to create a long string of numbers that’s much harder to decode.

Symmetric cryptography has many practical purposes, but doesn’t address the following issues: What if someone can eavesdrop and wait for Julia and César to share the key, then steal the key to decrypt their messages? What if they wait for Julia and César to reveal somehow that the secret for decrypting their messages was the key of three?

_How can César and Julia get around this problem?_

The best answer today is public key cryptography. In public key cryptography, encryption and decryption keys are different, and it’s perfectly safe to share the public key as long as the private key is kept private.

## Public Key Cryptography: A Tale of Two Keys [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#public-key-cryptography-a-tale-of-two-keys)

Let’s look at the problem more closely: How does the sender send the symmetric key to the recipient without someone spying on that conversation too?

Public-key cryptography (also known as asymmetric cryptography) has a neat solution for this. It allows each person in a conversation to create two keys: a public key and a private key. The two keys are connected and, despite the name, aren’t “keys” so much as they’re very large numbers with certain mathematical properties. If you encode a message using a person’s public key, they can decode it using their matching private key.

Now, Julia and César have moved past sending paper notes in class and are using their computers to send encrypted messages using public key cryptography. All the classmates who were passing the notes in the previous example are replaced with the computers that act as the intermediaries between Julia and César: Julia and César’s respective Wi-Fi points, internet service providers, and their email servers. In reality, it may be hundreds of computers between Julia and César that facilitate this conversation, and just like the nosy classmates, these intermediaries make and store copies of Julia and César’s messages each time they pass through.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1947/image-20250102104755-4.png)

They don’t mind that the intermediaries can see them communicating, but they want the _contents_ of their messages to remain private.

First, Julia needs César’s public key. César sends his public key over an insecure channel, like unencrypted email. (Good news: modern communication apps will do this on César’s behalf, removing the manual step, but the manual steps are still a good example of how this works.)

César doesn’t mind if the intermediaries get access to it because the public key is something that he can share freely (the key metaphor breaks down around here; it’s not quite right to think of the public key as a literal key; again: it's a very large number with certain mathematical properties, often encoded as a string of characters). To be safe, César sends his public key over multiple channels, an email and a text message, so it’s harder for intermediaries to send one of their own public keys on to Julia instead.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1945/image-20250102104755-5.png)

Julia receives César’s public key file. Now, Julia can encrypt a message to him. She writes, “Meet me in the garden.”

She sends the encrypted message. It is encrypted only to César.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1953/image-20250102104755-6.png)

Both Julia and César can understand the message, but it looks like gibberish to anyone else who tries to read it. But the intermediaries can still see _[metadata ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/metadata)_, like the subject line, dates, sender, and the recipient.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1957/image-20250102104755-7.png)

Because the message is encrypted to César’s public key, it is only intended for César and the sender (Julia) to unlock and read the contents of the message.

César can read the message using his private key.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1959/image-20250102104755-8.png)

To recap:

- Public key cryptography allows someone to send their public key in an open, insecure channel. Nowadays, communication apps handle this step for you.
- Having a friend’s public key allows you to encrypt messages to them.
- Your private key is used to decrypt encrypted messages meant for you.
- Intermediaries such as the email service providers, internet service providers, and those on their networks are able to see metadata this whole time. This includes details like who is sending what to whom, what time it’s received, what the subject line is, that the message is encrypted, and so on.

## Another Problem: What About Impersonation? [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#another-problem-what-about-impersonation)

In the example with Julia and César, the intermediaries are able to see metadata this whole time.

But let’s say that one of the intermediaries is a bad actor. By bad actor, we mean someone who intends to harm you by trying to steal or interfere with your information. This bad actor wants to spy on Julia’s message to César.

Let’s say this bad actor is able to trick Julia into grabbing the wrong public key file for César. Julia doesn’t notice that this isn’t actually César’s public key. So instead of César, the bad actor actually receives Julia’s message, peeks at it, then passes it along to César.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1954/image-20250102104755-9.png)

The bad actor could decide to change the contents of the file before passing it along to César. For example, they could change "Meet me in the garden," to "Meet me in the cafeteria."

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1956/image-20250102104755-10.png)

But most of the time, the bad actor decides to leave the contents unmodified. So, the bad actor forwards Julia’s message to César as though nothing happened, César knows to meet Julia in the garden, and _gasp_, to their surprise, the bad actor is there too!

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1958/image-20250102104756-11.png)

This is known as a " [man-in-the-middle attack ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/man-in-the-middle-attack)" or a "machine-in-the-middle [attack ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/attack)."

Luckily, public key cryptography has a method for preventing man-in-the-middle attacks through something called “ [fingerprint verification](https://ssd.eff.org/module/key-verification#verifying-keys-out-of-band).” This is best done in real life when possible. You’d have your public [key fingerprint ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/key-fingerprint) available, and your friend double-checks that every single character from your public key fingerprint matches what they have for your public key fingerprint. It’s a little tedious, but it’s worth doing.

Different end-to-end encrypted apps also have a way to check for fingerprints, though there are variations on what the practice is called and how it is implemented. In some instances, you’ll read each character of the [fingerprint ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/fingerprint) carefully and ensure it matches what you see on your screen versus what your friend sees on their screen. In others, you might scan a QR code on another person’s phone to “verify” their device.” In the example below, Julia and César are able to meet in person to verify their phone fingerprints by scanning each other’s QR codes using their phone’s camera.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1951/image-20250102104756-12.png)

For an example of what this method looks like in practice, [check out Signal's](https://ssd.eff.org/module/how-to-use-signal#verify-safety-numbers) "Verify safety number" option or [WhatsApp's "Verify security code" feature](https://ssd.eff.org/module/how-to-use-whatsapp#using-whatsapp).

If you don’t have the luxury of meeting in person, you can share your fingerprint through another secure channel, like another end-to-end encrypted messaging app or on a video call.

In the example below, César sends his public key fingerprint to Julia using a different end-to-end encrypted app on his smartphone.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1950/image-20250102104756-13.png)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1948/image-20250102104756-14.png)

To review:

- A man-in-the-middle attack is when someone intercepts your message to someone else. The attacker can alter the message and pass it along or choose to simply eavesdrop.
- Public key cryptography lets you address man-in-the-middle attacks by providing ways to verify the recipient and sender’s identities. This is done through "fingerprint verification."
- In addition to being used to encrypt a message to your friend, your friend’s public key also comes with a “public key fingerprint.” You can use the fingerprint to verify your friend’s identity.
- The private key is used to encrypt messages, as well as to digitally sign messages as being from you (more on this below).

## Signatures [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#signatures)

We know that if you encrypt a message with a certain public key, it can only be decrypted by the matching private key. The opposite is also true: if you encrypt a message with a certain private key, it can only be decrypted by its matching public key.

Why would this be useful? Suppose you wrote a message that said: “I promise to pay Aazul $100,” and then turned it into a secret message using your private key. Anyone could decrypt that message. But only one person could have written it: the person who has your private key. And if you’ve done a good job keeping your private key safe, that means you, and only you, could’ve written it. By encrypting the message with your private key, you’ve ensured it could only come from you.

In other words, you’ve done the same thing with this digital message as we do when we sign a message in the real world, which is why this process is known as “signing” a message.

Signing is also one of several methods that can make messages tamper-proof. If someone tried to change your message from “I promise to pay Aazul $100” to “I promise to pay Ming $100,” they would not be able to re-sign it using your private key. A signed message guarantees it originated from the correct source and wasn't messed with in transit.

## In Review: Using Public Key Cryptography [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#in-review-using-public-key-cryptography)

Let’s review. Public key cryptography lets you encrypt and send messages safely to anyone whose public key you know.

If others know your public key:

- They can send you secret messages that only you can decode using your matching private key.
- You can sign your messages with your private key so the recipients know the messages could only have come from you.
- Nowadays, messaging apps handle your public and private keys and have a more user-friendly mechanism for verifying those keys, making it easy for anyone to use public key cryptography without even realizing they’re using it.

And if you know someone else’s public key:

- You can decode a message they signed and know it truly came from them.

Public key cryptography becomes more useful when more people know your public key. You can share your public key with anyone who wants to communicate with you, it doesn’t matter who sees it.

The public key comes paired with a file called a private key. You can think of the private key like an actual key that you should protect and keep safe. Your private key is used to both encrypt and decrypt messages.

If your private key is accidentally deleted from your device, you won’t be able to decrypt your encrypted messages. If someone copies your private key (whether by physical access to your computer, [malware ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/malware) on your device, or if you accidentally share your private key), then others can read your encrypted messages. They can pretend to be you and sign messages claiming they were written by you.

It’s not unheard of for governments to steal private keys from important people's computers (by taking the computers away or by installing malware on them using physical access or [phishing ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/phishing) attacks). This undoes the protection private key cryptography offers.

This is like saying you have an unpickable lock on your door, but somebody can pickpocket your key, copy it, and then sneak it back into your pocket. Then, they’d be able to get into your house without picking the lock.

This goes back to your security plan: determine what your risks are and address them appropriately. If you feel like someone would go through great trouble to try to get your private key, you may not want to use an in-browser solution to end-to-end encryption. Instead, you may choose to store your private key on your own computer or phone, rather than someone else’s computer (like in the cloud or on a server).

## Public Key Cryptography in Practice [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#public-key-cryptography-in-practice)

We went over symmetric encryption and public key encryption as separate explanations, but public key encryption uses symmetric encryption as well. Public key encryption encrypts a symmetric key, which is then used to decrypt the actual message.

Pretty Good Privacy ( [PGP ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/pgp)) is rarely used anymore, but remains an example of a [protocol ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/protocol) that uses both symmetric cryptography and public key cryptography (asymmetric). Using end-to-end encryption tools like PGP will make you very aware of public key cryptography practices, because you have to do several steps manually. Most of what PGP does is hidden from the user in modern communication tools, but since PGP requires so many manual steps, it’s still helpful to explain how end-to-end encryption works.

### What Exactly Are Keys, And How Are Keys Tied Together? [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#what-exactly-are-keys-and-how-are-keys-tied-together)

Public key cryptography is based on the premise that there are two keys: one key for encrypting, and one key for decrypting. You can send a public key over an insecure channel, like the internet. You can post this public key everywhere, in very public places, and not compromise the security of your encrypted messages.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1952/image-20250102104756-15.png)

The public key comes paired with a file called a private key. You can think of the private key like an actual key that you have to protect and keep safe. Your private key is used to both encrypt and decrypt messages.

Let's take a look at how this works in a commonly-used public key cryptography algorithm called RSA (Rivest–Shamir–Adleman). RSA is often used to generate key pairs for PGP-encrypted emails.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1960/image-20250102104756-16.png)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1961/image-20250102104756-17.png)

The public key and private key are generated and tied together. Both rely on the same secret prime numbers. The private key represents two secret prime numbers.

Metaphorically, the public key is the product number: it is made up of the same two very large prime numbers used to make the private key. It’s very hard to figure out which two large prime numbers created the public key.

This problem is known as "prime factoring," and some implementations of public key cryptography take advantage of this difficulty for computers to solve what the component prime numbers are. Modern cryptography allows us to use randomly chosen, ridiculously gigantic, prime numbers that are hard to guess for both humans and computers.

The strength here is that people can share their public keys over insecure channels to let them encrypt to each other. In the process, they never reveal what their private key (secret prime numbers) is because they never have to send their private key to decrypt messages in the first place.

For public key cryptography to work, the sender and the recipient need each other’s public keys.

Another way you can think of it is that the public key and private key are generated together, like a yin-yang symbol. They are intertwined.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1949/image-20250102104756-18.png)

The public key is searchable and shareable. You can distribute it to whoever. You can post it on your social media (if you don’t mind that it reveals the existence of your email address). You can put it on your personal website.

The private key needs to be kept safe and close. You just have one. You don’t want to lose it,  share it, or make copies of it that can float around since it makes it harder to keep your private messages private.

### Modern Public Key Encryption in Practice: Signal’s Double Ratchet [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#modern-public-key-encryption-in-practice-signal-s-double-ratchet)

Over time, messaging protocols have evolved to offer additional properties to improve security and usability. This has changed how we all engage with encryption over the years, going from a transparent but clunky experience to something that happens in the background without us noticing it. One example of this is Signal’s “Double ratchet algorithm.” To best understand how this works, we should start by reviewing some key specifics from previous protocols.

#### Pretty Good Privacy (PGP)

As explained above, PGP is a single application of asymmetric encryption and symmetric encryption, and is typically used for encrypting email in a messaging context. With PGP, asymmetric encryption is used to encrypt a symmetric key, which is then used to encrypt a message. PGP allows asynchronous communication, but a one-time key compromise would reveal the contents of all messages, past and future. So, if someone gained access to your key, they would gain access to every message you’ve ever sent (or will send).

PGP isn’t as popular as it used to be, but some messaging apps use a similar type of encryption. These apps typically still have the break-in recovery and break-in archival secrecy problems that the email version has.

#### Off the Record (OTR)

OTR was once a popular [add-on ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/add-on) to early messaging chat clients, like Pidgin, and was used for communicating on services like Google Hangouts. For OTR to work, both parties must be online to set up a session, which limits its use.

With OTR, every back-and-forth message is a “session.” This means that if a single key is leaked, only messages from that session are compromised, not anything before or after. If multiple messages were sent from one user in a row, one key leak would reveal all of them, but not anything before or after. The key exchange is tacked onto the messages, so new keys are constantly being re-derived.

From a security perspective, this is great because if an attacker somehow accessed that key, they’d only get access to a single message. But the usability of OTR isn’t great. Since both parties need to be online, it’s not good for asynchronous messaging even after setup because the new key is only switched after both parties have messaged. This means that key material has to be kept around until the other party responds. Also, out-of-order message tracking—the feature of messaging clients that keeps messages in linear order based on the time they’re sent and received—becomes complicated. The order of messages isn’t just important for the legibility of the conversation, it’s also crucial for the encryption to actually work. If a message is sent out of order, the receiver’s app may not know which key to use to decrypt the message.

#### Silent Circle Instant Messaging Protocol (SCIMP)

SCIMP was an interim protocol that pioneered the use of a “double ratchet.” A double ratchet is when each sender has their own personal chain of keys, each is derived from the previous one. This means that key material can be safely discarded once a message is sent.

Picture a ratchet. Each time you turn the ratchet, it creates a new key for each message. If an attacker gets access to that key somehow, they can no longer read any previous message because once the message is sent, the ratchet spins again to create a new key. But they could use that key to make a copy of the ratchet, allowing them to read all future messages. Both people in a conversation have a personal ratchet that turns with each message. This is designed to prevent an attacker from scrolling back up in a conversation to read the previous messages, even if a person has sent multiple messages in a row.

SCIMP provides “ [forward secrecy ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/forward-secrecy),” meaning that a key compromise wouldn’t reveal past messages (this is confusingly named, but this prevents older messages from being read even if a key is compromised in the future). But SCIMP doesn’t provide any “future secrecy” or “break-in recovery” (used to prevent messages sent after a key is compromised from being read). Plus, expecting out-of-order messages means holding onto that key material for some length of time.

#### Signal’s Double Ratchet Algorithm

Signal uses a combination of OTR and SCIMP to support asynchronous messaging. [On its blog](https://signal.org/blog/advanced-ratcheting/), Signal explains the design philosophy like so: “We wanted a ratchet that combines the best of both worlds: the optimal _forward_ secrecy that a hash iteration ratchet like SCIMP provides, as well as the nice _future_ secrecy properties that a DH ratchet like OTR provides, with as little of the negatives of both as possible.”

In Signal, each person has a personal SCIMP-style ratchet that they turn when they send a new message (but the other person hasn’t responded). But each time messages are exchanged back and forth, a new session is created, as we saw in OTR.

By integrating both technologies, an attacker would need to decrypt almost every message individually. Technically, if user A has a long stream of posts without the other person B responding, and the key is leaked, the attacker will be able to see every new message sent by A until B responds and the session is advanced.

Signal’s double ratchet algorithm takes the idea of SCIMP key chains—which protect each individual message even if a user is “double texting”—and makes them mini-chains hanging off each step in an OTR ratchet. This ensures that the conversation gets a new key each time a new user responds. Additionally, it reduces the back-and-forths required by introducing a third “root key” chain.

One of Signal’s big innovations was being able to start conversations asynchronously using an offline key exchange. Since setting up the next message [encryption key ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/encryption-key) only requires two steps and not three, one of those steps can be prepared ahead of time and saved on Signal’s server. Relevant secret keys won’t be created until someone uses that material to perform a computation and derive their shared key information, so it’s safe to pre-publish. Signal calls these “prekeys.” For a less simplified version, see [here](https://signal.org/docs/specifications/x3dh/) or [here](https://signal.org/docs/specifications/pqxdh/) for the post-quantum version.

## Metadata: What Public Key Encryption Can't Do [\#](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work\#metadata-what-public-key-encryption-can-t-do)

Public key encryption is all about making sure the contents of a message are secret, genuine, and untampered with. But that's not the only privacy concern you might have. As we've noted, information about your messages— [the metadata](https://ssd.eff.org/module/why-metadata-matters)—can be as revealing as their contents.

If you exchange encrypted messages with a known dissident in your country, you may be in danger for simply communicating with them, even if those messages aren’t decoded. In some countries, you can face imprisonment for refusing to decode encrypted messages. Every encrypted messaging tool collects a different amount of metadata. For example, WhatsApp is also end-to-end encrypted, but collects more metadata than Signal.

Now that you’ve learned about public key cryptography, try out using an end-to-end encryption tool like [Signal](https://ssd.eff.org/module/how-to-use-signal).

- [Copyright (CC BY)](https://www.eff.org/copyright)
- [Privacy](https://www.eff.org/policy)