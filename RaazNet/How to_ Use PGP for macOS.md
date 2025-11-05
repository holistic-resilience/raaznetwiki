---
title: "How to_ Use PGP for macOS"
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

[Skip to main content](https://ssd.eff.org/module/how-use-pgp-mac-os-x#main-content)

- [About](https://ssd.eff.org/pages/about-surveillance-self-defense)
- [Language](https://ssd.eff.org/module/how-use-pgp-mac-os-x#)  - [English](https://ssd.eff.org/module/how-use-pgp-mac-os-x)
  - [አማርኛ](https://ssd.eff.org/am/module/%E1%88%88%E1%88%9B%E1%8A%AD-os-x-%E1%8B%A8pgp-%E1%8A%A0%E1%8C%A0%E1%89%83%E1%89%80%E1%88%9D)
  - [العربية](https://ssd.eff.org/ar/module/%D9%83%D9%8A%D9%81%D9%8A%D8%A9-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-pgp-%D8%B9%D9%84%D9%89-%D8%A3%D8%AC%D9%87%D8%B2%D8%A9-%D9%85%D8%A7%D9%83)
  - [Español](https://ssd.eff.org/es/module/c%C3%B3mo-usar-pgp-para-mac-os-x)
  - [Français](https://ssd.eff.org/fr/module/guide-pratique-utiliser-pgp-pour-macos)
  - [Русский](https://ssd.eff.org/ru/module/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-pgp-%D0%B4%D0%BB%D1%8F-mac)
  - [Türkçe](https://ssd.eff.org/tr/module/nas%C4%B1l-mac-os-x-i%C3%A7in-pgp-kullan%C4%B1m%C4%B1)
  - [Tiếng Việt](https://ssd.eff.org/vi/module/l%C3%A0m-th%E1%BA%BF-n%C3%A0o-s%E1%BB%AD-d%E1%BB%A5ng-pgp-tr%C3%AAn-mac-os-x)
  - [Português](https://ssd.eff.org/pt-br/module/como-utilizar-pgp-para-mac-os-x)
  - [Mandarin](https://ssd.eff.org/zh-hans/module/how-use-pgp-mac-os-x)
  - [Burmese](https://ssd.eff.org/my/module/how-use-pgp-mac-os-x)
  - [پښتو](https://ssd.eff.org/ps/module/how-use-pgp-mac-os-x)
  - [ภาษาไทย](https://ssd.eff.org/th/module/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3-%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99-pgp-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-mac-os-x)
  - [اردو](https://ssd.eff.org/ur/module/%DA%A9%D8%B3-%D8%B7%D8%B1%D8%AD-%DA%A9%D8%B1%DB%8C%DA%BA-mac-os-x-%DA%A9%DB%92-%D9%84%DB%8C%DB%92-pgp-%DA%A9%D8%A7-%D8%A7%D8%B3%D8%AA%D8%B9%D9%85%D8%A7%D9%84)
  - [More Translations](https://ssd.eff.org/en/other-translations)
- [Index](https://ssd.eff.org/#index)
- KeywordsSearch

[×](https://ssd.eff.org/module/how-use-pgp-mac-os-x#)

# How to: Use PGP for macOS

**Last Reviewed**: June 17, 2018

**NOTE**: This guide is not being actively reviewed or updated, and is currently retired. If you would like to use [PGP ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/pgp) via GnuPG, or Thunderbird with Enigmail, please refer to those services’ websites and documentation for information on how to install and use them.

To use PGP to exchange secure emails you have to bring together three programs: GnuPG, Mozilla Thunderbird and Enigmail. GnuPG is the program that actually encrypts and decrypts the content of your mail, Mozilla Thunderbird is an email client that allows you to read and write emails without using a browser, and Enigmail is an [add-on ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/add-on) to Mozilla Thunderbird that ties it all together.

What this guide teaches is how to use PGP with Mozilla Thunderbird, an email client program that performs a similar function to Outlook. You may have your own favorite email software program (or use a web mail service like Gmail or Outlook.com). This guide won't tell you how to use PGP with these programs. You can choose either to install Thunderbird and experiment with PGP with a new email client, or you can investigate other solutions to use PGP with your customary software. We have still not found a satisfactory solution for these other programs.

Using PGP doesn't completely [encrypt ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/ps/glossary/encrypt) all aspects of your email: the sender and receiver information is unencrypted. Encrypting the sender and receiver information would break email. For similar reasons, PGP does not encrypt the subject line of your emails so you may want to use a generic subject line when sending encrypted emails. What using Mozilla Thunderbird with the Enigmail add-on gives you is an easy way to encrypt the body of your email.

You will first download all the software needed, install it, and then end with configuration and how to use the result.

**Computer requirements**: An internet connection, a computer running Mac OS X, an email account

**Download Location**:

- [Enigmail](https://www.enigmail.net/home/index.php)
- [GnuPG](https://gnupg.org/)
- [Mozilla Thunderbird](https://www.mozilla.org/en-US/thunderbird/)

**Versions used in this guide**: Mac OS X: 10.11; Mozilla Thunderbird 45.2.0; Enigmail 1.9; GnuPG 2.1.11

**License**: Free Software; mix of Free Software licenses

**Other reading**:

- [An Introduction to Public Key Cryptography and PGP Key Verification](https://ssd.eff.org/en/module/introduction-public-key-cryptography-and-pgp)
- [Creating Strong Passwords](https://ssd.eff.org/en/module/creating-strong-passwords)
- [Animated Overview: How to Make a Super-Secure Password Using Dice](https://ssd.eff.org/en/module/animated-overview-how-make-super-secure-password-using-dice)
- [Animated Overview: Using Password Managers to Stay Safe Online](https://ssd.eff.org/en/module/animated-overview-using-password-managers-stay-safe-online)

**Level**: Beginner-Intermediate

**Time required**: 30-60 minutes

Pretty Good Privacy ( [PGP ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/pgp)) is a way to help protect your email communications from being read by anyone except their intended recipients. And, to a lesser extent, it can save your emails from being read if the computer on which they are stored is stolen or broken into.

It can also be used to prove that an email came from a particular person, instead of being a fake message sent by another sender (it is otherwise very easy for email to be fabricated). Both of these are important defenses if you're being targeted for surveillance or misinformation.

To use PGP, you will need to install some extra software that will work with your current email program. You will also need to create a private [key ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/key), which you will keep private. The private key is what you will use to [decrypt ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/decrypt) emails sent to you, and to digitally sign emails that you send to show they truly came from you. Finally, you'll learn how to distribute your public key—a small chunk of information that others will need to know before they can send you encrypted mail, and that they can use to verify emails you send.

## Getting and Installing GnuPG [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#getting-and-installing-gnupg)

You can get GnuPG (also known as GPG) on Mac OS X by downloading the small installer from the [GnuPG download page](https://gnupg.org/download/index.html#sec-1-2)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/311/content_00.png)

_Click on GnuPG for OS X_ next to “Simple installer for GnuPG modern” which will download the GPG installer.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/312/content_01a.png)

You’ll get redirected to the SourceForge download website.

## Getting Mozilla Thunderbird [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#getting-mozilla-thunderbird)

Go to the [Mozilla Thunderbird website](https://www.mozilla.org/en-US/thunderbird/)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/313/content_01.png)

_Click on the green button labeled “Free Download.”_ The Mozilla Thunderbird website will have detected your preferred language. If you want to use Thunderbird in another language click on the “Systems & Languages” link and make your selection from there.

## Installing GnuPG [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#installing-gnupg)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/314/content_02.png)

_Click the Download icon_ in the Dock and then _click the GnuPG-2.11-002.dmg file_.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/315/content_03.png)

A window will open, indicating your progress.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/316/content_04.png)

A window will open, giving you an overview of the Installation file and some other files. _Click the “_ _Install.pkg_ _”_ _icon_ _._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/317/content_05.png)

Next, a window will open starting the guided installation. _C_ _lick the “_ _Continue_ _” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/318/content_06.png)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/319/content_07.png)

GnuPG is installed as a system package and requires your username and [password ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/password) to install. _Enter your password and click “Install Software.”_

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/320/content_08.png)

You will see a window that will say “The installation was successful.” C _lick the “_ _Close_ _” button_.

## Installing Mozilla Thunderbird [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#installing-mozilla-thunderbird)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/314/content_02.png)

_Click the Download icon_ in the Dock and then _click the_ _Thunderbird 45.2.0_ _.dmg file_.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/321/content_09.png)

A window will open indicating your progress.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/322/content_10.png)

A window will open with the Thunderbird icon and a link to your Applications folder. Drag Thunderbird to the Applications folder.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/323/content_11.png)

A window with a progress bar will open, when it is done, it will close.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/324/content_12.png)

Make sure to eject the mounted DMG files.

## Preparation for Enigmail installation [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#preparation-for-enigmail-installation)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/325/content_13.png)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/326/content_14.png)

When Mozilla Thunderbird launches for the first time, Mac OS X will ask you if you are sure you want to open it. Mozilla Thunderbird was downloaded from mozilla.org and should be safe, _click the “Open” button_.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/327/content_15.png)

Mozilla Thunderbird can integrate with the Mac OS X address book, we leave this choice to you.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/328/content_16.png)

When Mozilla Thunderbird launches for the first time, you will see this small confirmation window asking about some default settings. _We recommend clicking the “Set as Default” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/329/content_17.png)

When Mozilla Thunderbird launches for the first time, you will be asked whether you would like a new email address _. Click the “Skip this and use my existing email” button_. Now you will configure Mozilla Thunderbird to be able to receive and send email. If you are used to only reading and sending email through gmail.com, outlook.com, or yahoo.com, Mozilla Thunderbird will be a new experience, but it isn't that different overall.

## Adding a mail account to Mozilla Thunderbird [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#adding-a-mail-account-to-mozilla-thunderbird)

A new window will open:

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/330/content_18.png)

Enter your name, your email address, and the password to your email account. Mozilla doesn't have access to your password or your email account. _Click the “Continue” button._

In many cases Mozilla Thunderbird will automatically detect the necessary settings.

In some cases Mozilla Thunderbird doesn't have complete information and you'll need to enter it yourself. Here is an example of the instructions Google provides for Gmail:

- Incoming Mail (IMAP) Server - Requires SSL
  - imap.gmail.com
  - Port: 993
  - Requires SSL: Yes
- Outgoing Mail (SMTP) Server - Requires TLS
  - smtp.gmail.com
  - Port: 465 or 587
  - Requires SSL: Yes
  - Requires authentication: Yes
  - Use same settings as incoming mail server
-  Full Name or Display Name: \[your name or [pseudonym ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/pseudonym)\]
- Account Name or User Name: your full Gmail address ( [username@gmail.com](mailto:username@gmail.com)). Google Apps users, please enter [username@your\_domain.com](mailto:username@your_domain.com)
- Email address: your full Gmail address ( [username@gmail.com](mailto:username@gmail.com)) Google Apps users, please enter [username@your\_domain.com](mailto:username@your_domain.com)
- Password: your Gmail password

If you use [two-factor authentication ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/two-factor-authentication) with Google (and depending on your [threat model ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/threat-model) you probably should!) you cannot use your standard Gmail password with Thunderbird. Instead, you will need to create a new application-specific password for Thunderbird to access your Gmail account. See [Google's own guide](https://support.google.com/mail/answer/185833?hl=en&rd=1) for doing this.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/331/content_19.png)

When all the information is entered correctly, _click the “Done” button._

Mozilla Thunderbird will start downloading copies of your email to your computer. _Try sending_ _a test email to your_ _friends._

## Installing Enigmail [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#installing-enigmail)

Enigmail is installed in a different way from Mozilla Thunderbird and GnuPG. As mentioned before, Enigmail is an [Add-on ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/add-on) for Mozilla Thunderbird. _Click the “Menu button,” also called the Hamburger button and select “Add Ons.”_

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/332/content_21.png)

You'll be taken to an Add-ons Manager tab. Enter "Enigmail" into the Add-on search field to look for Enigmail on the Mozilla Add-on site.![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/333/content_23.png)

Enigmail will be the first option. _Click the "Install" button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/334/content_24.png)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/335/content_25.png)

After the Enigmail add-on is installed Mozilla Thunderbird will ask to restart the browser to activate Enigmail. _Click the “Restart Now” button and Mozilla Thunderbird will restart_.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/336/content_26.png)

When Mozilla Thunderbird restarts an additional window will open up that will start the process of setting up the Enigmail add-on. _Keep the “Start setup now” button selected and click the “Continue” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/337/content_27.png)

## Required Configuration Steps [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#required-configuration-steps)

In May 2018 researchers [revealed](https://efail.de/) several vulnerabilities in PGP (including GPG) for email, and theorized many more which others could build upon.

Thunderbird and Enigmail’s developers have been working on ways to protect against the EFAIL vulnerabilities. As of [version 2.0.6](https://sourceforge.net/p/enigmail/forum/announce/thread/5772757e/) (released May 27, 2018), Enigmail has released patches that defend against all known exploits described in the EFAIL paper, along with some new ones in the same class that other researchers were [able to devise](https://twitter.com/hanno/status/997138771194859521), which beat earlier Enigmail fixes. Each new fix made it a little harder for an attacker to get through Enigmail’s defenses. We feel confident that, if you update to this version of Enigmail (and keep updating!), Thunderbird users can turn their PGP back on.

But, while Enigmail now defends against most known attacks even with HTML on, the EFAIL [vulnerability ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/vulnerability) demonstrated just how dangerous HTML in email is for security. Thus, we recommend that Enigmail users also turn off HTML by going to View > Message Body As > Plain Text.

1\. First click on the Thunderbird **hamburger menu** (the three horizontal lines).

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/84/content_1-revised.png)

2. Select “ **View**” from the right side of the menu that appears.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/85/content_2.png)

3. Select “ **Message Body As**” from the menu that appears, then select the “ **Plain Text**” radio option.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/86/content_3.png)

Viewing all email in plaintext can be hard, and not just because many services send only HTML emails. Turning off HTML mail can pose some usability problems, such as [some attachments failing to show up](https://twitter.com/micahflee/status/998984671995166721). Thunderbird users shouldn't have to make this trade-off between usability and security, so we hope that Thunderbird will take a closer look at supporting their plaintext community from now on. As the software is now, however, users will need to decide for themselves whether to take the risk of using HTML mail; the most vulnerable users should probably not take that risk, but the right choice for your community is a judgment call [based on your situation](https://ssd.eff.org/en/module/assessing-your-risks).

Now you will start creating your private key and public key. Learn more about keys, and what they are, in our [Introduction to Public Key Cryptography and PGP guide](https://ssd.eff.org/en/module/introduction-public-key-cryptography-and-pgp#1).

## Creating a Public Key and Private Key [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#creating-a-public-key-and-private-key)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/338/content_28.png)

Unless you have already configured more than one email account, Enigmail will choose the email account you've already configured. The first thing you'll need to do is come up with a [strong passphrase](https://ssd.eff.org/en/module/creating-strong-passwords) for your private key.

_Click the "Continue" button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/339/content_29.png)

Your key will expire at a certain time; when that happens, other people will stop using it entirely for new emails to you, though you might not get any warning or explanation about why. So, you may want to mark your calendar and pay attention to this issue a month or so before the expiration date.

It's possible to extend the lifetime of an existing key by giving it a new, later expiration date, or it's possible to replace it with a new key by creating a fresh one from scratch. Both processes might require contacting people who email you and making sure that they get the updated key; current software isn't very good at automating this. So make a reminder for yourself; if you don't think you'll be able to manage it, you can consider setting the key so that it never expires, though in that case other people might try to use it when contacting you far in the future even if you no longer have the private key or no longer use PGP.

To check your key's expiration date in Thunderbird, click the Enigmail menu and select "Key Management." Search for your key in the Enigmail Key Management window and double click on it. A new window will open and your key's expiration date will be displayed in the field called "Expiry." To set a new expiration date, click the "Change" button next to your key's current expiration date. Remember to send your updated public key to your contacts or publish it to a keyserver if you update your key's expiration date.

Enigmail will generate the key and when it is complete, a small window will open asking you to generate a [revocation certificate ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/revocation-certificate). This revocation certificate is important to have as it allows you to make the private key and public key invalid in the event you lose your private key or it gets stolen. For this reason, store your revocation certificate separately from your private key; burn it to a CD or put it on a USB drive and keep it somewhere safe. Publishing the revocation certificate to a keyserver will let other PGP users know not to use or trust that public key. It is important to note that merely deleting the private key does not invalidate the public key and may lead others to sending you encrypted mail that you can't decrypt. _Click the “Generate Certificate” button_.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/340/content_30.png)

First you will be asked to provide the [passphrase ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/passphrase) you used when you created the PGP key. _Click the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/341/content_31.png)

A window will open to provide you a place to save the revocation certificate. While you can save the file to your computer we recommend saving the file to a USB drive that you are using for nothing else and storing the drive in a safe space. We also recommend removing the revocation certificate from the computer with the keys, just to avoid unintentional revocation. Even better, save this file on an encrypted disk. Choose the location where you are saving this file and _click the “Save” button_.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/342/content_32.png)

Now Enigmail will give you further information about saving the revocation certificate file again. _Click the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/343/content_33.png)

Finally, you are done with generating the private key and public key. _Click the “Done” button._

## Optional configuration steps [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#optional-configuration-steps)

### Display Fingerprints and Key Validity [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#display-fingerprints-and-key-validity)

The next steps are completely optional but they can be helpful when using OpenPGP and Enigmail. Briefly, the Key ID is a small part of the [fingerprint ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/fingerprint). When it comes to verifying that a public key belongs to a particular person the fingerprint is the best way. Changing the default display makes it easier to read the fingerprints of the certificates you know about. _Click the configuration button, then the Enigmail option, then Key Management._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/344/content_34.png)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/345/content_35.png)

A window will open showing two columns: Name and Key ID.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/346/content_36.png)![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/347/content_36a.png)

On the far right there is a small button. _Click that button to configure the columns._ _Unclick the Key ID option and click the Fingerprint option and the Key Validity option._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/348/content_37.png)

Now there will be three columns: Name, Key Validity, and Fingerprint.

## Finding Other People Who Are Using PGP [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#finding-other-people-who-are-using-pgp)

### Getting a Public Key by Email [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#getting-a-public-key-by-email)

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/349/content_38.png)

You might get a public key sent to you as an email attachment. _Click on the "Import Key"_ button.

### ![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/350/content_39.png)[\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#)

A small window will open asking you to confirm importing the PGP key. _Click the "Yes" button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/351/content_40.png)

A new window will open with the results of the import. _Click the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/352/content_41.png)

If you reload the original email you’ll see that the bar over the email has changed.

If you open up the Enigmail key management window again, you can check the result. Your PGP key is in bold because you have both the private key and the public key. The public key you just imported is not bold because it doesn't contain the private key.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/353/content_41a.png)

### Getting a Public Key as a File [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#getting-a-public-key-as-a-file)

It's possible that you get a public key by downloading it from a website or someone might have sent it through chat software. In a case like this, we will assume you downloaded the file to the Downloads folder.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/348/content_37.png)

Open the Enigmail Key Manager.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/354/content_42.png)

_Click on the “File” menu. Select “Import Keys from File.”_

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/355/content_43.png)

Select the public key, it might have very different file name endings such as .asc, .pgp, or .gpg. _Click the “Open” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/350/content_39.png)

A small window will open asking you to confirm importing the PGP key. _Click the “Yes” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/351/content_40.png)

A new window will open with the results of the import. _Click the “OK” button._

### Getting a Public Key From a URL [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#getting-a-public-key-from-a-url)

It's possible to get a public key by downloading it directly from a URL

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/356/content_48.png)

Open the Enigmail Key Manager and _click on the “Edit” menu. Select “Import Keys from URL.”_

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/357/content_49.png)

Enter the URL. The URL can have several forms. Most often it is likely a [domain name ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/domain-name) ending in a file.

Once you have the right URL, _click the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/350/content_39.png)

A small window will open asking you to confirm importing the PGP key. _Click the "Yes" button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/351/content_40.png)

A new window will open with the results of the import. _Click the "OK" button._

If you look at [https://www.eff.org/about/staff](https://www.eff.org/about/staff) you will notice a “PGP Key” link under the staff pictures. Danny O'Brien's PGP key, for example, can be found at: [https://www.eff.org/files/pubkeydanny.txt](https://www.eff.org/files/pubkeydanny.txt).

### Getting a public key from a key server [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#getting-a-public-key-from-a-key-server)

Keyservers can be a very useful way of getting public key. Try looking for a public key.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/358/content_50.png)

From the Key Management interface _click the “Keyserver”_ menu and _select “Search for Keys.”_

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/359/content_51.png)

A small window will pop up with a search field. You can search by a complete email address, a partial email address, or a name. In this case, you will search for keys containing “ [samir@samirnassar.com](mailto:samir@samirnassar.com)”. _Click the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/360/content_52.png)

A larger window will pop up with many options. If you scroll down you'll notice some keys are italicized and grayed out. These are keys that have either been revoked or expired on their own.

We have several PGP keys for Samir Nassar and we don’t yet know which one to choose. One key is in grey italics which means that it has been revoked. Because we don’t know which one we want yet, we will import them all. _Select the keys by clicking the box on the left then press the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/361/content_53.png)

A small notification window will pop up letting you know if you succeeded. _Click the “OK” button._

The Enigmail Key Manager will now show you the added keys:

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/362/content_54.png)

Note that of the three imported keys, one is expired, one is revoked, and one is currently a valid key.

## Letting others know you are using PGP [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#letting-others-know-you-are-using-pgp)

Now that you have PGP, you want to let others know that you are using it so they can also send you encrypted messages using PGP.

Using PGP doesn't completely [encrypt ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/zh-hans/glossary/encrypt) your email: the sender and receiver information is unencrypted. Encrypting the sender and receiver information would break email. Using Thunderbird with the Enigmail add-on gives you an easy way to encrypt and decrypt the content of your email.

Let's look at three different ways you can let people know you are using PGP.

### Let people know you are using PGP with an email [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#let-people-know-you-are-using-pgp-with-an-email)

You can easily email your public key to another person by sending them a copy as an attachment.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/363/content_55.png)

_Click the "Write" button in Mozilla Thunderbird._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/364/content_56.png)

Fill in an address and a subject, perhaps something my “my public key,” click the “Attach My Public Key” button. If you have already imported a PGP key for the person you are sending the PGP key to, the Lock icon in the Enigmail bar will be highlighted. As an additional option, you can also click the Pencil icon to sign the email, giving the recipient a way to verify the authenticity of the email later.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/365/content_57.png)

A window will pop open asking you if you forgot to add an attachment. This is a bug in the interaction between Enigmail and Mozilla Thunderbird, but don’t worry, your public key will be attached. _Click the “No, Send Now” button._

### Let people know you are using PGP on your website [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#let-people-know-you-are-using-pgp-on-your-website)

In addition to letting people know via email, you can post your public key on your website. The easiest way is to upload the file and link to it. This guide won't go into how to do those things, but you should know how to export the key as a file to use in the future.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/348/content_37.png)

_Click the configuration button, then the Enigmail option, then Key Management._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/366/content_58.png)

_Highlight the key in bold, then right-click to bring up the menu and select Export keys to file._

## ![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/367/content_59.png)[\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#)

A small window will pop up with three buttons. _Click the “Export Public Keys Only” button_.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/368/content_60.png)

Now a window will open so you can save the file. In order to make it easier to find in the future please save the file to the Documents folder. Now you can use this file as you wish.

Make sure you don't click the “Export Secret Keys” button because exporting the secret key could allow others to impersonate you if they are able to guess your password.

### Uploading to a keyserver [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#uploading-to-a-keyserver)

Keyservers make it easier to search for and download public keys of others. Most modern keyservers are synchronizing, meaning that a public key uploaded to one server will eventually reach all servers.

Although uploading your public key to a keyserver might be a convenient way of letting people know that you have a public PGP certificate, you should know that due to the nature of how keyservers work there is no way to delete public keys once they are uploaded.

Before uploading your public key to a keyserver, it is good to take a moment to consider whether you want the whole world to know that you have a public certificate without the ability to remove this information at a later time.

If you choose to upload your public key to keyservers, you will go back to the Enigmail Key Management window.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/366/content_58.png)

Right-click your PGP key and select the Upload Public Keys to Keyserver option.

## Sending PGP Encrypted Mail [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#sending-pgp-encrypted-mail)

Now you will send your first encrypted email to a recipient.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/363/content_55.png)

In the main Mozilla Thunderbird window _click the “Write” button_. A new window will open.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/369/content_63a.png)

Write your message, and enter a recipient. For this test, select a recipient whose public key you already have. Enigmail will detect this and automatically encrypt the email.

The subject line won't be encrypted, so choose something innocuous, like "hello."

The body of the email was encrypted and transformed. For example the text above will be transformed into something like this:![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/122/content_290pgpmessage.png)

## Receiving PGP Encrypted Mail [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#receiving-pgp-encrypted-mail)

Let's go through what happens when you receive encrypted email.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/370/content_63.png)

Notice that Mozilla Thunderbird is letting you know you have new mail. _Click on the message._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/371/content_64.png)

A small window opens asking you for the password to the PGP key. Remember: Don't enter your email password. _Click the "OK" button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/372/content_65.png)

Now the message will show up decrypted.

## Revoking the PGP Key [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#revoking-the-pgp-key)

### Revoking Your PGP Key Through the Enigmail Interface [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#revoking-your-pgp-key-through-the-enigmail-interface)

The PGP keys generated by Enigmail automatically expire after five years. So if you lose all your files, you can hope that people will know to ask you for another key once the key has expired.

You might have a good reason to disable the PGP key before it expires. Perhaps you want to generate a new, stronger PGP key. The easiest way to revoke your own PGP key in Enigmail is through the Enigmail Key Manager.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/348/content_37.png)

Right click on your PGP key, it's in bold, and _select the "Revoke Key" option._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/373/content_66.png)

A window will pop up letting you know what happens and asking for your confirmation. _Click the “Revoke Key” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/371/content_64.png)

The password window opens, enter your password for the PGP key and _click to "OK" button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/374/content_69.png)

Now a new window will open up letting you know you succeeded. _Click the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/375/content_68.png)

When you go back to the Enigmail Key Management window you'll notice a change to your PGP key. It is now grayed out and italicized.

### Revoking a PGP Key with a Revocation Certificate [\#](https://ssd.eff.org/module/how-use-pgp-mac-os-x\#revoking-a-pgp-key-with-a-revocation-certificate)

Like we mentioned before, you might have a good reason to disable the PGP key before it expires. Similarly, others might have good reasons to revoke an existing key. In the previous section you might have noticed that Enigmail generates and imports a revocation certificate internally when you use the Enigmail Key Manager to revoke a key.

You might get sent revocation certificates from friends as a notice that they want to revoke their key. Since you already have a revocation certificate, you will use the one you generated earlier to revoke your own key.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/354/content_42.png)

Start with the Enigmail Key Manager and _click the “File” menu and select “Import Keys from File.”_

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/376/content_67.png)

A window will open up so you can select the revocation certificate. _Click on the file, and click the “Open” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/374/content_69.png)

You'll get a notification that the certificate was imported successfully and that a key was revoked. _Click the “OK” button._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/375/content_68.png)

When you go back to the Enigmail Key Management window you'll notice a change to your PGP key. It is now grayed out and italicized.

Now that you have all the proper tools, try sending your own PGP-encrypted email.

- [Copyright (CC BY)](https://www.eff.org/copyright)
- [Privacy](https://www.eff.org/policy)