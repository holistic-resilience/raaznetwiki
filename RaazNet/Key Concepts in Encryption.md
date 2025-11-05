---
title: "Key Concepts in Encryption"
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

[Skip to main content](https://ssd.eff.org/module/key-concepts-encryption#main-content)

- [About](https://ssd.eff.org/pages/about-surveillance-self-defense)
- [Language](https://ssd.eff.org/module/key-concepts-encryption#)  - [English](https://ssd.eff.org/module/key-concepts-encryption)
  - [አማርኛ](https://ssd.eff.org/am/module/key-concepts-encryption)
  - [العربية](https://ssd.eff.org/ar/module/key-concepts-encryption)
  - [Español](https://ssd.eff.org/es/module/conceptos-claves-en-cifrado)
  - [Français](https://ssd.eff.org/fr/module/les-notions-essentielles-du-chiffrement)
  - [Русский](https://ssd.eff.org/ru/module/%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%B2%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D1%8F-%D0%B2-%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B8)
  - [Türkçe](https://ssd.eff.org/tr/module/key-concepts-encryption)
  - [Tiếng Việt](https://ssd.eff.org/vi/module/key-concepts-encryption)
  - [Português](https://ssd.eff.org/pt-br/module/conceitos-chave-na-criptografia)
  - [Mandarin](https://ssd.eff.org/zh-hans/module/daa4aad3-1638-4522-ac07-fc3af39c1a4b)
  - [Burmese](https://ssd.eff.org/my/module/%E1%80%80%E1%80%AF%E1%80%92%E1%80%BA%E1%80%96%E1%80%BC%E1%80%84%E1%80%B7%E1%80%BA-%E1%80%95%E1%80%BC%E1%80%B1%E1%80%AC%E1%80%84%E1%80%BA%E1%80%B8%E1%80%9C%E1%80%B2%E1%80%81%E1%80%BC%E1%80%84%E1%80%BA%E1%80%B8%E1%80%86%E1%80%AD%E1%80%AF%E1%80%84%E1%80%BA%E1%80%9B%E1%80%AC-%E1%80%A1%E1%80%81%E1%80%BC%E1%80%B1%E1%80%81%E1%80%B6%E1%80%A1%E1%80%9A%E1%80%B0%E1%80%A1%E1%80%86%E1%80%99%E1%80%BB%E1%80%AC%E1%80%B8)
  - [پښتو](https://ssd.eff.org/ps/module/key-concepts-encryption)
  - [ภาษาไทย](https://ssd.eff.org/th/module/key-concepts-encryption)
  - [اردو](https://ssd.eff.org/ur/module/key-concepts-encryption)
  - [More Translations](https://ssd.eff.org/en/other-translations)
- [Index](https://ssd.eff.org/#index)
- KeywordsSearch

[×](https://ssd.eff.org/module/key-concepts-encryption#)

# Key Concepts in Encryption

**Last Reviewed**: January 01, 2025

Under some circumstances, encryption can be fairly automatic and simple. But there are ways encryption can go wrong. The more you understand it, the safer you will be against such situations. Before we get into it, we recommend reading the “ [What Should I Know About Encryption?](https://ssd.eff.org/module/what-should-i-know-about-encryption)” guide first, if you haven’t already.

In this guide, we will look at five important concepts for understanding encryption in transit:

- Ciphers and keys
- Symmetric and asymmetric encryption
- Private and public keys
- Identity verification for people (public key fingerprints)
- Identity verification for websites (security certificates)

## Ciphers and Keys [\#](https://ssd.eff.org/module/key-concepts-encryption\#ciphers-and-keys)

First, let’s start with some glossary terms that we’ll be using:

**Encryption** is a mathematical process used to scramble information, so that it can only be unscrambled, or “decrypted”, with special knowledge. The process involves a cipher and a key.

A **cipher** is a set of rules (an algorithm) followed by a computer when encrypting and decrypting data. The same steps and rules used to encrypt data must be followed exactly to decrypt it.

A **key** is a piece of information that instructs the cipher in how to encrypt and decrypt. Keys are one of the most important concepts for understanding encryption.

## One Key or Many Keys? [\#](https://ssd.eff.org/module/key-concepts-encryption\#one-key-or-many-keys)

In **symmetric encryption**, there is one single key to both encrypt and decrypt information.

|     |
| --- |
| ![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1932/image-20250102100504-1.png) |
| _Older forms of encryption were symmetric. For the “Caesar cipher” used by Julius Caesar, the key to encrypt and decrypt a message was a shift of three. For example, “A” would be changed to “D.” So, using the key of three, the message “ENCRYPTION IS COOL” would be encrypted to “HQFUBSWLRQ LV FRRO.” That same key would be used to decrypt it back to the original message._ |

Symmetric encryption is still used today—it often comes in the form of “stream ciphers” and “block ciphers,” which rely on complex mathematical processes to make their encryption hard to crack. Nowadays, encryption includes many steps of scrambling data to make it hard to reveal the original content without the valid key. Modern symmetric encryption algorithms, such as the Advanced Encryption Standard (AES) algorithm, are strong and fast.

Symmetric encryption is widely used by computers for tasks like encrypting files, encrypting partitions on a computer, completely [encrypting devices and computers using full-disk encryption](https://ssd.eff.org/module/how-encrypt-your-windows-device), and encrypting databases like those of [password managers](https://ssd.eff.org/module/choosing-the-password-manager-that-s-right-for-you). To decrypt this symmetrically-encrypted information, you’ll often be prompted for a password. This is why we recommend [using strong passwords](https://ssd.eff.org/module/creating-strong-passwords).

Having a single key can be great if you are the only person who needs to access that information. But there’s a problem with having a single key: what if you wanted to share encrypted information with a friend far away? What if you couldn’t meet with your friend in person to share the key? How could you share the key with your friend securely over an open internet connection?

**Asymmetric encryption**, also known as **public key encryption**, addresses these problems. Asymmetric encryption involves two keys: a private key (for decryption) and a public key (for encryption).

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1931/image-20250102100504-2.png)

|     |     |
| --- | --- |
| **Symmetric Encryption** | **Asymmetric Encryption** |
| - Fast | - Slow |
| - Doesn’t require a lot of computing power | - Requires more computing power |
| - Useful for encrypting both large and small messages | - Best for encrypting small messages |
| - Requires sharing the key for encryption and decryption | - The decryption key does not need to be shared — only the “public key” for encryption is shared |
| - Cannot be used for verifying identities (authentication) | - Can be used for identity verification (authentication) |

Symmetric and asymmetric encryption are often used together for encrypting [data in transit](https://ssd.eff.org/module/what-should-i-know-about-encryption#encrypting-data-in-transit).

## Asymmetric Encryption: Private and Public Keys [\#](https://ssd.eff.org/module/key-concepts-encryption\#asymmetric-encryption-private-and-public-keys)

Private and public keys come in matched pairs, because the private key and public key are mathematically tied together. You can think of it like a rock that is split in half. When held back together, the two halves form the whole. No other rock-half will do. The public key and private key files are much the same, but are ultimately composed of computer-readable representations of very large numbers.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1939/image-20250102100504-3.png)

Although it is called a “public key,” it doesn’t quite serve the function of an actual, literal key to open things. Instead, it can be thought of as a lock for the data. For more in-depth information on public keys and private keys, see our [deep dive on public key cryptography](https://ssd.eff.org/module/deep-dive-end-end-encryption-how-do-public-key-encryption-systems-work).

|     |
| --- |
| ![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1937/image-20250102100504-4.png) |
| _A public key is a file that you can give to anyone or publish publicly. When someone wants to send you an end-to-end encrypted message, they’ll need your public key to do so. Nowadays, this happens automatically with most chat software that supports end-to-end encryption._ |

|     |
| --- |
| ![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1936/image-20250102100504-5.png) |
| _Your private key lets you decrypt this encrypted message. Because your private key allows you to read encrypted messages, it becomes very important to protect your private key. In addition, your private key can be used to sign documents so that others can verify that they really came from you._ |

Since the private key is a file on your device that requires protection, we encourage you to password protect and encrypt the devices where the private key is stored. We have guides for [strong passwords](https://ssd.eff.org/en/module/creating-strong-passwords) and [device encryption](https://ssd.eff.org/en/module/how-encrypt-your-iphone).

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1940/image-20250102100504-6.png)

|     |     |
| --- | --- |
| **Public Key** | **Private Key** |
| - A file that can be shared widely (can be shared over the internet easily) | - A file that must be kept safe and protected |
| - Sender needs the public key to encrypt information to the recipient | - Used to decrypt encrypted messages which use the corresponding public key |
| - Represented by a “public key fingerprint,” which is used for verifying identities (authentication) | - Used for digital signatures, allowing a way to verify a sender’s identity (authentication) |

In some ways, you can think of sending information in transit like sending a postcard. In the postcard illustration on the left (below), a sender writes: “HI! :-)” The sender addresses it to the message recipient. This message below on the left is unencrypted, and anyone passing the message along the way can read it.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1941/image-20250102100927-12.png)

On the right is that same postcard, with the message encrypted between the sender and receiver. The message still conveys the message “Hi! :-)” but now it looks like a block of encrypted gibberish to the rest of us.

How is this done? The sender has found the recipient’s public key. The sender addresses the message to the recipient’s public key, which encrypts the message. The sender has also included their signature to show that the encrypted message is really from them.

Note that the [metadata](https://ssd.eff.org/en/module/why-metadata-matters)—of who is sending and who is receiving the message, as well as additional information like time sent and received, where it passed through, and so on—is still visible. We can see that the sender and receiver are using encryption, we can tell that they are communicating, but we can’t read the content of their message.

## Who Are You Encrypting To? Are They Who They Really Say They Are? [\#](https://ssd.eff.org/module/key-concepts-encryption\#who-are-you-encrypting-to-are-they-who-they-really-say-they-are)

You might be wondering: “I get that my **public key** lets someone send me an encrypted message, and that my **private key** lets me read that encrypted message. But what if someone pretends to be me? What if they create a new public and private key, and impersonate me?”

This is where public key cryptography is especially useful: it lets you verify your identity and your recipient’s identity. Let’s look at the capabilities of the private key more closely.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1938/image-20250102100504-8.png)

In addition to letting you read encrypted messages that are sent to your public key, your private key lets you place unforgeable digital signatures on messages you send to other people, as though to say “Yes, this is really me writing this.”

Your recipient will see your digital signature along with your message and compare it with the information listed from your public key.

Let’s look at how this works in practice.

## Identity Verification for People: Public Key Fingerprints [\#](https://ssd.eff.org/module/key-concepts-encryption\#identity-verification-for-people-public-key-fingerprints)

When we send any kind of message, we rely on the good faith of people participating. For example, we don’t expect a mail delivery person to meddle with the contents of our mail. We also don’t expect someone to intercept a friend’s letter to us, open and modify it, and send it to us, as though nothing had been changed. But there’s a risk this could happen.

Encrypted messages have this same risk of being modified. However, public key cryptography allows us a way to check if information has been tampered with by checking someone’s digital identity with their real-life identity.

The public key is a giant block of text in a file. It is also represented in a human-readable shortcut called a key fingerprint.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1935/image-20250102100504-9.png)

The word “fingerprint” means lots of different things in the field of computer security.

One use of the term is a “key fingerprint,” a string of characters like “65834 02604 86283 29728 37069 98932 73120 14774 81777 73663 16574 23234” that should allow you to uniquely and securely check that someone on the internet is using the right private key.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1934/image-20250102100504-10.png)

In some apps, this information can be represented as a QR code that you and your friend scan off each other’s devices.

You can double-check that someone’s digital identity matches who they say they are through something called “fingerprint verification.” To get an idea of how this works in practice, try it out in [Signal](https://ssd.eff.org/module/how-to-use-signal#verify-safety-numbers) or [WhatsApp](https://ssd.eff.org/module/how-to-use-whatsapp#using-whatsapp).

Fingerprint verification is best done in real-life. If you’re able to meet with your friend in person, have your public key fingerprint available and let your friend double-check that every single character from your public key fingerprint matches what they have for your public key fingerprint. Checking a long string of characters like “342e 2309 bd20 0912 ff10 6c63 2192 1928” is tedious, but is a crucial step in securing your communications. If you’re not able to meet in person, you can make your fingerprint available through another secure channel, like another end-to-end encrypted messaging or chat system.

Verifying someone’s key fingerprint gives you a higher degree of certainty that it’s really them. But it’s not perfect. If the private keys are copied or stolen (say you have malware on your device, or someone physically accessed your device and copied the file), someone else would be able to use the same fingerprint. For this reason, if a private key is “stolen,” you will want to generate a new public and private key pair, and give your friends your new public key fingerprint.

## Summary: Public-Key Encryption Capabilities [\#](https://ssd.eff.org/module/key-concepts-encryption\#summary-public-key-encryption-capabilities)

In general, using public-key encryption can provide users:

**Confidentiality**: A message encrypted with public-key cryptography allows the sender to create a message that is secret, so that only the intended recipient can read it.

**Authenticity**: A recipient of a message signed with public-key cryptography can verify that the message was authentically crafted by the sender if they have the sender’s public key.

**Integrity**: A message signed or encrypted with public-key cryptography, in general, cannot be tampered with.The message will not decrypt or verify correctly. This means that even unintentional disruption of a message (e.g. because of a temporary network problem) will be detectable.

### Identity Verification for Websites and Services: Security Certificates [\#](https://ssd.eff.org/module/key-concepts-encryption\#identity-verification-for-websites-and-services-security-certificates)

You might wonder: “I can verify public key fingerprints, but what’s the equivalent for the web? How can I double-check that I’m using a website that really is the website that it says it is? How can I be sure that no one is interfering with my connection to a service?”

When using transport-layer encryption, your computer automatically checks to confirm whether a public key for a service is who it really says it is, and that it is encrypting to the intended service. This is called a “security certificate.”

Below, you can see an example of the security certificate for SSD from a generic web browser. This information is often accessible by clicking the HTTPS lock or options panel in your web browser and pulling up the certificate details.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1933/image-20250102100504-11.png)![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1942/image-20250102101115-13.png)

The web browser on your computer can make encrypted connections to sites using HTTPS. Websites often use security certificates to prove to your browser that you have a secure connection to the real site, and not to some other system that’s tampering with your connection. Web browsers examine certificates to check the public keys of domain names—(like [www.duckduckgo.com](http://www.duckduckgo.com/), [www.wikipedia.org](http://www.wikipedia.org/), or [ssd.eff.org](http://ssd.eff.org/)). Certificates are one way of trying to determine if you know the correct public key for a person or website, so that you can communicate securely with them.

But how does your computer know what the right public key is for sites you visit?

Modern browsers and operating systems include a list of trusted Certificate Authorities (CAs). The public keys for these CAs are pre-bundled when you download the browser or buy a computer. Certificate Authorities sign the public key of websites once they’ve validated them as legitimately operating a domain (such as [www.example.com](http://www.example.com/)). When your browser visits an HTTPS site, it verifies that the certificate the site delivered has actually been signed by a CA that it trusts. This means that a trusted third-party has verified that the site is who it is claiming to be.

Just because a site’s security certificate has been signed by a Certificate Authority, does not mean that the website is a secure site. There are limits to what a CA can verify—it can’t verify that a website is honest or trustworthy. For example, a website may be “secured” using HTTPS, but still host scams and malware. Be vigilant, and learn more by [reading our guide on malware and phishing.](https://ssd.eff.org/en/module/how-avoid-phishing-attacks)

From time to time, you will see certificate-related error messages on the web. Most commonly this is because a hotel or cafe network is trying to intercept your connection to a website in order to direct you to their login portal before accessing the web, or because of a bureaucratic mistake in the system of certificates. But occasionally it is because a hacker, thief, or police or spy agency is breaking the encrypted connection. Unfortunately, it is extremely difficult to tell the difference between these cases.

This means you should never click past a certificate warning if it relates to a site where you have an account or are reading any sensitive information.

### Putting It All Together: Symmetric Keys, Asymmetric Keys, & Public Key Fingerprints. [\#](https://ssd.eff.org/module/key-concepts-encryption\#putting-it-all-together-symmetric-keys-asymmetric-keys-public-key-fingerprints)

**The example of Transport-Layer Security Handshakes**

When using [transport-layer encryption](https://ssd.eff.org/module/what-should-i-know-about-encryption#transport-layer-encryption-or-end-to-end-encryption), your computer’s browser and the computer of the website you’re visiting both use symmetric algorithms and asymmetric algorithms.

Let’s examine a concrete example of how all these ideas work together: when you connect to this HTTPS website ( [https://ssd.eff.org/](https://ssd.eff.org/)), what happens?

When a website uses HTTPS, your browser and the website’s server have a very fast set of interactions called “the handshake.” Your browser—Google Chrome, Mozilla Firefox, Tor Browser, and so forth—is talking to the server hosting our website, [https://ssd.eff.org](https://ssd.eff.org/).

In the handshake, the browser and server first send each other notes to see if they have any shared preferences for encryption algorithms (these are known as “cipher suites”). You can think of it like your browser and our ssd.eff.org server having a quick conversation: they’re asking each other what encryption methods they both know and should communicate in, as well as which encryption methods they prefer.

It looks something like this: “Do we both know how to use an asymmetric algorithm like RSA in combination with a symmetric algorithm like AES? Yes, good. If this combination of encryption algorithms doesn’t work for us, what other encryption algorithms do we both know?”

Next, your browser uses asymmetric encryption: it sends a public key certificate to ssd.eff.org to prove that you are who you say you are. The site's server checks this public key certificate against your public key. This is to prevent a malicious computer from intercepting your connection.

Once your identity is confirmed, the site’s server uses symmetric encryption: it generates a new, symmetric, secret key file. It then asymmetrically encrypts your browser’s public key, and sends it to your browser. Your browser uses its private key to decrypt this file.

If this symmetric key works, your browser and website’s server use it to encrypt the rest of their communications. This set of interactions is the transport layer security (TLS) handshake. Thus, [if all goes right](https://www.moserware.com/2009/06/first-few-milliseconds-of-https.html) in the handshake, your connection to ssd.eff.org shows up as secure, with HTTPS before ssd.eff.org.

For a deeper dive on key verification [read this guide](https://ssd.eff.org/module/key-verification) next.

- [Copyright (CC BY)](https://www.eff.org/copyright)
- [Privacy](https://www.eff.org/policy)