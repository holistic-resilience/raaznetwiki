---
title: "How to_ Use OTR for macOS"
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

[Skip to main content](https://ssd.eff.org/module/how-use-otr-macos#main-content)

- [About](https://ssd.eff.org/pages/about-surveillance-self-defense)
- [Language](https://ssd.eff.org/module/how-use-otr-macos#)  - [English](https://ssd.eff.org/module/how-use-otr-macos)
  - [አማርኛ](https://ssd.eff.org/am/module/%E1%88%88%E1%88%9B%E1%8A%AD-%E1%8B%A8otr-%E1%8A%A0%E1%8C%A0%E1%89%83%E1%89%80%E1%88%9D)
  - [العربية](https://ssd.eff.org/ar/module/%D8%AF%D9%84%D9%8A%D9%84-%D9%83%D9%8A%D9%81-%D8%AA%D8%B3%D8%AA%D8%AE%D8%AF%D9%85-otr-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D9%85%D8%A7%D9%83)
  - [Español](https://ssd.eff.org/es/module/c%C3%B3mo-usar-otr-para-mac)
  - [Français](https://ssd.eff.org/fr/module/guide-pratique-utiliser-le-protocole-otr-sous-macos)
  - [Русский](https://ssd.eff.org/ru/module/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-otr-%D0%B4%D0%BB%D1%8F-mac)
  - [Türkçe](https://ssd.eff.org/tr/module/nas%C4%B1l-mac-i%C3%A7in-otr-kullan%C4%B1m%C4%B1)
  - [Tiếng Việt](https://ssd.eff.org/vi/module/l%C3%A0m-th%E1%BA%BF-n%C3%A0o-s%E1%BB%AD-d%E1%BB%A5ng-otr-cho-mac)
  - [Português](https://ssd.eff.org/pt-br/module/como-utilizar-o-otr-para-mac)
  - [Mandarin](https://ssd.eff.org/zh-hans/module/how-use-otr-macos)
  - [Burmese](https://ssd.eff.org/my/module/how-use-otr-macos)
  - [پښتو](https://ssd.eff.org/ps/module/how-use-otr-macos)
  - [ภาษาไทย](https://ssd.eff.org/th/module/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3-%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B9%82%E0%B8%AD%E0%B8%97%E0%B8%B5%E0%B8%AD%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-mac)
  - [اردو](https://ssd.eff.org/ur/module/%DA%A9%D8%B3-%D8%B7%D8%B1%D8%AD-%DA%A9%D8%B1%DB%8C%DA%BA-otr-%D9%85%DB%8C%DA%A9-%DA%A9%DB%92-%D9%84%D8%A6%DB%92-%D8%A7%D8%B3%D8%AA%D8%B9%D9%85%D8%A7%D9%84-%DA%A9%D8%B1%DB%8C%DA%BA)
  - [More Translations](https://ssd.eff.org/en/other-translations)
- [Index](https://ssd.eff.org/#index)
- KeywordsSearch

[×](https://ssd.eff.org/module/how-use-otr-macos#)

# How to: Use OTR for macOS

**Last Reviewed**: January 18, 2017

**Download Location:** [https://adium.im/](https://adium.im/)

**Computer requirements** (Adium 1.5 or later): Mac OS X 10.6.8 or newer, an Apple-branded Macintosh computer.

**Version used in this guide:** Adium 1.5.9

**License:** GNU GPL

**Other reading:** [https://pressfreedomfoundation.org/encryption-works](https://pressfreedomfoundation.org/encryption-works); [https://adium.im/help/](https://adium.im/help/)

**Level:** Beginner-Intermediate

**Time required:** 15-20 minutes

**NOTE**: This guide is not being actively reviewed or updated, and is currently retired. If you would like to use Adium or another form of OTR messaging for macOS, please refer to those services’ websites and documentation for information on how to install and use them.

[Adium](https://adium.im/) is a free and open source instant messaging client for OS X that allows you to chat with individuals across multiple chat protocols, including Google Hangouts, Yahoo! Messenger, Windows Live Messenger, AIM, ICQ, and XMPP.

OTR ( [Off-the-record ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/off-the-record)) is a [protocol ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/protocol) that allows people to have confidential conversations using the messaging tools they’re already familiar with. This should not be confused with Google's “Off the record,” which merely disables chat logging, and does not have [encryption ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/encryption) or verification capabilities. For Mac users, OTR comes built-in with the Adium client.

OTR employs [end-to-end encryption ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/end-to-end-encryption). This means that you can use it to have conversations over services like Google Hangouts without those companies ever having access to the contents of the conversations.  However, the fact that you are having a conversation is visible to the provider.

## Why Should I Use Adium + OTR? [\#](https://ssd.eff.org/module/how-use-otr-macos\#why-should-i-use-adium-otr)

When you have a chat conversation using Google Hangouts on the Google website, that chat is encrypted using [HTTPS ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/https), which means the content of your chat is protected from hackers and other third parties while it’s in transit. It is _not_, however, protected from Google, which have the keys to your conversations and can hand them over to authorities or use them for marketing purposes.

After you have installed Adium, you can sign in to it using multiple accounts at the same time. For example, you could use Google Hangouts and XMPP simultaneously. Adium also allows you to chat using these tools without OTR. Since OTR _only works if both people are using it_, this means that even if the other person does not have it installed, you can still chat with them using Adium.

Adium also allows you to do [out-of-band verification ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/out-of-band-verification) to make sure that you’re talking to the person you think you’re talking to and you are not being subject to a [man-in-the-middle attack ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/man-in-the-middle-attack). For every conversation, there is an option that will show you the [key ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/key) fingerprints it has for you and the person with whom you are chatting. A " [key fingerprint ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/key-fingerprint)" is a string of characters like "342e 2309 bd20 0912 ff10 6c63 2192 1928,” that’s used to verify a longer public key. Exchange your fingerprints through another communications channel, such as Twitter DM or email, to make sure that no one is interfering with your conversation. If the keys don't match, you can't be sure you're talking to the right person. In practice, people often use multiple keys, or lose and have to recreate new keys, so don't be surprised if you have to re-check your keys with your friends occasionally.

## Limitations: When Should I Not Use Adium + OTR? [\#](https://ssd.eff.org/module/how-use-otr-macos\#limitations-when-should-i-not-use-adium-otr)

Technologists have a term to describe when a program or technology might be vulnerable to external [attack ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/attack): they say it has a large “attack surface.” Adium has a large attack surface. It is a complex program, which has not been written with security as a top priority. It almost certainly has bugs, some of which might be used by governments or even big companies to break into computers that are using it. Using Adium to [encrypt ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/encrypt) your conversations is a great defense against the kind of untargeted dragnet surveillance that is used to spy on everyone's Internet conversations, but if you think you will be personally targeted by a well-resourced attacker (like a nation-state), you should consider stronger precautions, such as [PGP ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/pgp)-encrypted email.

## Installing Adium + OTR On Your Mac [\#](https://ssd.eff.org/module/how-use-otr-macos\#installing-adium-otr-on-your-mac)

### Step 1: Install the program [\#](https://ssd.eff.org/module/how-use-otr-macos\#step-1-install-the-program)

First, go to [https://adium.im/](https://adium.im/) in your browser. Choose “Download Adium 1.5.9.” The file will download as a .dmg, or disk image, and will probably be saved to your “downloads” folder.

Double-click on the file; that will open up a window that looks like this:

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/16/content_adium_1.png)

Move the Adium icon into the “Applications” folder to install the program. Once the program is installed, look for it in your Applications folder and double-click to open it.

### Step 2: Set up your account(s) [\#](https://ssd.eff.org/module/how-use-otr-macos\#step-2-set-up-your-account-s)

First, you will need to decide what chat tools or protocols you want to use with Adium. The setup process is similar, but not identical, for each type of tool. You will need to know your account name for each tool or protocol, as well as your [password ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/password) for each account.

To set up an account, go to the Adium menu at the top of your screen and click “Adium” and then “Preferences.” This will open a window with another menu at the top. Select “Accounts,” then click the “+” sign at the bottom of the window. You will see a menu that looks like this:

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/17/content_adium_2.png)

Select the program that you wish to sign in to. From here, you will be prompted either to enter your username and password, or to use Adium’s authorization tool to sign in to your account. Follow Adium’s instructions carefully.

## How to Initiate an OTR Chat [\#](https://ssd.eff.org/module/how-use-otr-macos\#how-to-initiate-an-otr-chat)

Once you have signed in to one or more of your accounts, you can start using OTR.

Remember: In order to have a conversation using OTR, both people need to be using a chat program that supports OTR.

### Step 1: Initiate an OTR Chat [\#](https://ssd.eff.org/module/how-use-otr-macos\#step-1-initiate-an-otr-chat)

First, identify someone who is using OTR, and initiate a conversation with them in Adium by double-clicking on their name. Once you have opened the chat window, you will see a small, open lock in the upper left-hand corner of the chat window. Click on the lock and select “Initiate Encrypted OTR Chat.”

### Step 2: Verify Your Connection [\#](https://ssd.eff.org/module/how-use-otr-macos\#step-2-verify-your-connection)

Once you have initiated the chat and the other person has accepted the invitation, you will see the lock icon close; this is how you know that your chat is now encrypted (congratulations!) – But wait, there’s still another step!

At this time, you have initiated an unverified, encrypted chat. This means that while your communications are encrypted, you have not yet determined and verified the identity of the person you are chatting with. Unless you are in the same room and can see each other’s screens, it is important that you verify each other’s identities. For more information, read the module on [Key Verification](https://ssd.eff.org/en/module/key-verification#overlay=en/node/37/).

To verify another user’s identity using Adium, click again on the lock, and select “Verify.” You will be shown a window that displays both your key and the key of the other user. Some versions of Adium only support manual [fingerprint ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/fingerprint) verification. This means that, using some method, you and the person with whom you’re chatting will need to check to make sure that the keys that you are being shown by Adium match precisely.

The easiest way to do this is to read them aloud to one another in person, but that’s not always possible. There are different ways to accomplish this with varying degrees of trustworthiness. For example, you can read your keys aloud to one another on the phone if you recognize each other’s voices or send them using another verified method of communication such as PGP. Some people publicize their key on their website, Twitter account, or business card.

The most important thing is that you verify that every single letter and digit matches perfectly.

### Step 3: Disable Logging [\#](https://ssd.eff.org/module/how-use-otr-macos\#step-3-disable-logging)

Now that you have initiated an encrypted chat and verified your chat partner’s identity, there’s one more thing you need to do. Unfortunately, Adium logs your OTR-encrypted chats by default, saving them to your hard drive. This means that, despite the fact that they’re encrypted, they are being saved in plain text on your hard drive.

To disable logging, click “Adium” in the menu at the top of your screen, then “Preferences.” In the new window, select “General” and then disable “Log messages” and “Log OTR-secured chats.” Remember, though, that you do not have control over the person with whom you are chatting—she could be logging or taking screenshots of your conversation, even if you yourself have disabled logging.

Your settings should now look like this:

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/18/content_adium_3.png)

Also, when Adium displays notifications of new messages, the contents of those messages may be logged by the OS X Notification Center. This means that while Adium leaves no trace of your communications on your own computer or your correspondent's, either your or their computer's version of OS X may preserve a record. To prevent this, you may want to disable notifications.

To do this, select "Events" in the Preferences window, and look for any entries that say "Display a notification." For each entry, expand it by clicking the gray triangle, and then click the newly-exposed line that say "Display a notification," then click the minus icon ("-") at the lower left to remove that line." If you are worried about records left on your computer, you should also turn on full-disk encryption, which will help protect this [data ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/data) from being obtained by a third party without your password.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/19/content_sign_on_and_message_received_background.png)

- [Copyright (CC BY)](https://www.eff.org/copyright)
- [Privacy](https://www.eff.org/policy)