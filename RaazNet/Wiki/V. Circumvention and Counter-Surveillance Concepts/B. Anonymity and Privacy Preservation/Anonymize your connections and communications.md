\_\_('Table of Contents')

Internet Connection › Anonymize your connections and communications

# [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#anonymize-your-connections-and-communications) Anonymize your connections and communications

Updated 17 September 2024

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#table-of-contents) Table of Contents

- [Consider whether you really need anonymity tools](https://securityinabox.org/en/internet-connection/anonymity/#consider-whether-you-really-need-anonymity-tools)
- [Get ready](https://securityinabox.org/en/internet-connection/anonymity/#get-ready)
- [Browse the web anonymously](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously)
- [Use Tor securely by avoiding common mistakes](https://securityinabox.org/en/internet-connection/anonymity/#use-tor-securely-by-avoiding-common-mistakes)
- [Anonymize all your connections](https://securityinabox.org/en/internet-connection/anonymity/#anonymize-all-your-connections)
- [Chat anonymously](https://securityinabox.org/en/internet-connection/anonymity/#chat-anonymously)
- [Exchange anonymous emails](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails)
- [Send and receive files anonymously](https://securityinabox.org/en/internet-connection/anonymity/#send-and-receive-files-anonymously)
- [Use Tor Bridges if you can't connect to Tor automatically](https://securityinabox.org/en/internet-connection/anonymity/#use-tor-bridges-if-you-cant-connect-to-tor-automatically)
- [\[Advanced\] Set up a whistleblowing platform to receive files anonymously](https://securityinabox.org/en/internet-connection/anonymity/#advanced-set-up-a-whistleblowing-platform-to-receive-files-anonymously)

_“ Encryption and anonymity, today’s leading vehicles for online security, provide individuals with a means to protect their privacy, empowering them to browse, read, develop and share opinions and information without interference and enabling journalists, civil society organizations, members of ethnic or religious groups, those persecuted because of their sexual orientation or gender identity, activists, scholars, artists and others to exercise the rights to freedom of opinion and expression.”_ ( [Report of the Special Rapporteur on the promotion and protection of the right to freedom of opinion and expression, David Kaye, to the U.N. General Assembly, 22 May 2015](https://documents.un.org/doc/undoc/gen/g15/095/85/pdf/g1509585.pdf))

This guide explains how to anonymize connections and communications to achieve a specific goal without leaving any traces. This strategy is particularly helpful in high-risk situations where your activities cannot be connected to your identity as this would compromise your freedom and wellbeing.

If you need an alternative identity for a longer-lasting project (for example to keep your official name separated from your activities as a human rights defender), also read [our recommendations on how to manage and secure multiple online identities](https://securityinabox.org/en/communication/multiple-identities).

If you are thinking of using anonymity tools, consider that in some countries some of these are illegal or can be interpreted as a sign that you are doing something wrong. In such cases ask yourself if you could find other ways of reaching your goals, for example by using methods that don't require accessing the internet.

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#consider-whether-you-really-need-anonymity-tools) Consider whether you really need anonymity tools

We strongly recommend to use anonymizing tools based on Tor and to follow the instructions in the sections below, in these situations:

- if you need to make sure that nobody can trace back some specific activities you are going to undertake to your official identity;
- if censorship circumvention tools like VPNs are blocked in your country.

In other cases, you may have needs that could be addressed through different, and probably simpler, solutions, for example:

- If you need to stop someone on your local network or ISP from seeing sensitive data you enter in a website, you can make sure that your connection is encrypted by enabling [HTTPS-only mode in your browser](https://securityinabox.org/en/internet-connection/safer-browsing/#secure-your-connections).
- If you want to protect yourself from commercial tracking, [stopping third-party cookies in your browser settings](https://securityinabox.org/en/internet-connection/safer-browsing/#enable-tracking-protection-settings) and installing [free and open-source privacy extensions in your browser](https://securityinabox.org/en/internet-connection/safer-browsing/#use-protective-browser-add-onsextensions) might be enough for you.
- You can try using a VPN if you need to:
  - access websites or services that are blocked or censored in your country or in the local network you are connecting from (like your library, workplace, hotel, etc.),
  - avoid that the owners or managers of the websites and services you access know where you are, or
  - avoid monitoring by your local internet provider or somebody in your local network.
  - In all these cases we recommend you to read [our guide on how to circumvent internet blockages](https://securityinabox.org/en/internet-connection/circumvention) first.

Learn why we recommend this

Tor will make it almost impossible to anyone to spy on your online activities and trace them back to you as it encrypts and anonymizes all your connections (see an explanation of how this works in [Browse the web anonymously](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously) below). However, if you need to protect yourself from snooping at the level of your local network and to avoid being profiled and tracked by your ISP and by commercial websites, there are other ways. In most cases your [standard browser includes privacy settings](https://securityinabox.org/en/internet-connection/safer-browsing) that can address your basic privacy needs, and you can install addons to prevent tracking.

If you would like to access blocked websites, hide your IP from the websites and services you access or avoid monitoring at the level of your ISP or local network, in most cases [a VPN](https://securityinabox.org/en/internet-connection/circumvention) will address these needs.

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#get-ready) Get ready

- [Create an alternative identity and make sure nobody can connect it to you](https://securityinabox.org/en/communication/multiple-identities/#create-and-secure-an-alternative-identity). In particular, follow the instructions for some crucial steps:
  - [Get a different phone number](https://securityinabox.org/en/communication/multiple-identities/#get-a-different-phone-number) \- if you are planning to register a new phone number through an online calling service, use the [Tor Browser](https://securityinabox.org/en/internet-connection/anonymity/#browse_the_web_anonymously) to register it.
  - [Create a new email account](https://securityinabox.org/en/internet-connection/anonymity/#Exchange_anonymous_emails) using the [Tor Browser](https://securityinabox.org/en/internet-connection/anonymity/#browse_the_web_anonymously) and the separate phone number you have obtained for your anonymous identity. Even better, try to [find an email provider](https://securityinabox.org/en/communication/tools/#more-secure-email-providers) that doesn't require a phone number for opening an account.
  - [Separate your anonymous identity using a different device or virtual environment](https://securityinabox.org/en/communication/multiple-identities/#compartmentalize-each-identity-using-different-devices-profiles-or-virtual-environments).
  - Reflect on what kind of online services and messaging apps you will need to achieve your goal and register new accounts using [Tor](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously) and the separate phone number you have obtained for your anonymous identity.
  - [Learn how to keep your new identity really separate from your usual online presence](https://securityinabox.org/en/communication/multiple-identities/#keep-your-identities-separate).
- Make sure [the devices you want to use for your anonymous activities are secure, updated and protected against malware](https://securityinabox.org/en/phones-and-computers).
- [Learn how to protect sensitive information and familiarize yourself with file and device encryption](https://securityinabox.org/en/files/secure-file-storage).

Learn why we recommend this

If you want to make it as difficult as possible for anyone to trace your online activities back to you, consider that this requires thorough planning. Besides [choosing a different name](https://securityinabox.org/en/communication/multiple-identities/#choose-a-name) and [creating an alternative identity](https://securityinabox.org/en/communication/multiple-identities/#create-and-secure-an-alternative-identity) (even if for a limited time span), you will need separate accounts, which can only be created through a phone number and an email address that cannot be connected to your official identity. You will also need devices that are secure and protected from malware and you should learn how to protect your sensitive data and what strategies you can use to keep your anonymous identity separated from your official one.

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#browse-the-web-anonymously) Browse the web anonymously

- Install the [Tor Browser](https://www.torproject.org/download/) (for Windows, macOS, Linux and Android).
- Install the [Onion Browser](https://onionbrowser.com/) (for iOS).
- [Watch the YouTube video by the Tor Project on how Tor Browser protects your privacy and identity online](https://youtu.be/JWII85UlzKw).
- [Watch the YouTube video by the Tor Project on how to use the Tor Browser securely](https://www.youtube.com/watch?v=qYcErJc9N3o).
- Read [the Tor Project overview on how Tor works](https://2019.www.torproject.org/about/overview.html.en).

Learn why we recommend this

Tor is a network that protects and anonymizes your connections by encrypting your traffic and sending it through at least three random servers (or nodes) in the Tor network. The last node in the circuit (called "exit node" or "exit relay") then sends the traffic out onto the public Internet. There are thousands of Tor servers, and they are run by volunteers around the world.

The way most people use Tor is through the Tor Browser, which is a version of Firefox enhanced for better privacy. Tor Browser is free and open-source software.

The Tor network does not keep logs about your connections or IP address. When you use Tor, your ISP can only see your connections to the first node in the Tor network and the websites or online services you visit only see that you are connecting from Tor and don't know who you are unless you reveal your identity, for example by logging in to a platform with your usual account. Read the following section of this guide to learn how to avoid common mistakes that could reveal your identity to the websites and services you access.

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#use-tor-securely-by-avoiding-common-mistakes) Use Tor securely by avoiding common mistakes

- Control what information you provide online, such as logging in to personal accounts or providing personal information.
- Make sure any files you're sharing don't include metadata, such as dates, location or device information. Learn how to remove this data in [our guide on how to destroy identifying information](https://securityinabox.org/en/files/destroy-identifying-information/).
- Don't use the same Tor circuit for more than one identity at a time. [Learn more on managing identities in the Tor documentation](https://tb-manual.torproject.org/managing-identities/).
- Don't connect through untrusted devices that could be infected with malware and make sure your device is secure and protected. Learn how to avoid possible infections in [our guide on malware](https://securityinabox.org/en/phones-and-computers/malware).
- Don't torrent over Tor as your torrent client might reveal your IP. Read more on this risk in [the Tor Project blog post on why Bittorrent over Tor isn't a good idea](https://blog.torproject.org/bittorrent-over-tor-isnt-good-idea/).
- Don't enable or install browser plugins: Tor Browser already comes installed with one add-on — [NoScript](https://securityinabox.org/en/communication/tools/#noscript) — and adding anything else could deanonymize you.
- Make sure you use the [HTTPS versions of websites](https://securityinabox.org/en/internet-connection/safer-browsing/#secure-your-connections) and be cautious when visiting websites you don't know as they might be malicious.
- Be mindful when opening documents downloaded or received through the Tor Browser as these documents may contain malicious scripts that could deanonymize you. You can convert such documents to safe form using [DangerZone](https://dangerzone.rocks/).
- Be aware of [physical security risks like shoulder surfing or cameras recording your screen](https://securityinabox.org/en/phones-and-computers/physical-security/#consider-what-can-be-seen), try to share about your anonymous activities only with very trusted people and [reflect on how to separate your everyday life from the physical activities of your anonymous identity, for example when attending an event](https://securityinabox.org/en/communication/multiple-identities/#reflect-on-how-to-manage-your-multiple-identities-in-physical-spaces).

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#anonymize-all-your-connections) Anonymize all your connections

- [Install Tails](https://tails.net/install/index.en.html) (requires a computer).
  - [Learn how Tails works](https://tails.net/about/index.en.html).
  - [Read the Tails documentation to get started](https://tails.net/doc/index.en.html).
- If you prefer to anonymize just some of your connections, you can [install Whonix](https://www.whonix.org/wiki/Download).
  - Watch [What is Whonix? — Your Internet Privacy Super Tool](https://www.youtube.com/watch?v=sRJTHWgbMvc) (on YouTube).
  - Learn how to use Whonix in [the official documentation](https://www.whonix.org/wiki/Documentation).
- On mobile devices, you can anonymize all your connections with [Orbot](https://orbot.app/en/).
  - Read [Hudsonwillis' guide on how to set up Orbot](https://medium.com/@hudson234willis/how-to-use-orbot-vpn-5085d775d352).

Learn why we recommend this

The Tor Browser only anonymizes what you do through the Tor Browser, like visiting websites or using online platforms that can be reached through a web page. If you want to anonymize activities that require different tools, like for example messaging apps or an email client, you need to anonymize all the connections coming out of a certain device, so you will need to use one of the tools listed in this section.

[Tails](https://securityinabox.org/en/internet-connection/tools/#tails) is a free and open-source operating system that runs from a USB stick, connects to the internet over Tor and leaves no trace on your computer.

[Whonix](https://whonix.org/) is an anonymous operating system that runs like an app in Windows, macOS, Linux and [Qubes OS](https://securityinabox.org/en/phones-and-computers/tools/#qubes-os) and routes all internet traffic generated inside its workstation through the Tor network.

[Orbot](https://orbot.app/en/) is a free and open-source application for mobile devices that routes internet traffic through the Tor network. With Orbot, you can anonymize all your connections or only certain apps.

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#chat-anonymously) Chat anonymously

- Read [our guide on how to chat securely](https://securityinabox.org/en/communication/secure-chat) to choose a chat service that works for you. Ideally, choose a tool that offers end-to-end encryption and that allows to use a username rather than a phone number to connect with other people.
- If a phone number is required to create an account on the chat app you have chosen, [get a new phone number](https://securityinabox.org/en/communication/multiple-identities/#get-a-different-phone-number) for your anonymous identity. If you need to get the phone number from an online service, [use Tor](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously) to connect to that service.
- If the chat service requires an email address to register, [get a new email account](https://securityinabox.org/en/internet-connection/anonymity/#exchange_anonymous_emails) [over Tor](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously). Read [our guide on safe email](https://securityinabox.org/en/communication/secure-email) to choose a secure email provider.
- Only connect to the chat service through Tor, either by using a web-based chat through the [Tor Browser](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously) or by using a chat app on a device that makes it possible to [anonymize all your connections](https://securityinabox.org/en/internet-connection/anonymity/#anonymize-all-your-connections).

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#exchange-anonymous-emails) Exchange anonymous emails

- Read [our guide on secure email](https://securityinabox.org/en/communication/secure-email) to choose an email provider that works for you. Request a new email account on the server you have chosen using the [Tor Browser](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously) or [another tool that anonymizes all your connections](https://securityinabox.org/en/internet-connection/anonymity/#anonymize-all-your-connections).
  - If you only want to send one or few emails and don't need to keep the same email address for a longer period of time, consider using a disposable email service like [anonbox](https://anonbox.net/index.en.html) or [Guerrilla Mail](https://www.guerrillamail.com/).
- Only connect to the email service through Tor, either by using a webmail interface through the [Tor Browser](https://securityinabox.org/en/internet-connection/anonymity/#browse-the-web-anonymously) or by using a mail client like [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) on a device that makes it possible to [anonymize all your connections](https://securityinabox.org/en/internet-connection/anonymity/#anonymize-all-your-connections).

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#send-and-receive-files-anonymously) Send and receive files anonymously

- If you need to send files securely and anonymously, or to allow someone to send you files without revealing their identity to anyone, you can use [OnionShare](https://onionshare.org/), an open-source tool that lets you securely and anonymously share files, host websites and chat with friends using the Tor network.
  - Install [OnionShare](https://docs.onionshare.org/2.6.2/en/install.html) (for Linux, Windows, macOS, Android and iOS).
  - [Send files anonymously with OnionShare](https://docs.onionshare.org/2.6.2/en/features.html#share-files).
  - [Use OnionShare to let people anonymously submit files and messages directly to your computer](https://docs.onionshare.org/2.6.2/en/features.html#receive-files-and-messages).
  - You can also use OnionShare to [set up an anonymous chat room](https://docs.onionshare.org/2.6.2/en/features.html#chat-anonymously) and even to [host a website](https://docs.onionshare.org/2.6.2/en/features.html#host-a-website).
  - When sharing files through OnionShare, you will need to send an address and a private key — make sure to use a [secure chat over Tor](https://securityinabox.org/en/internet-connection/anonymity/#chat-anonymously) to preserve your anonymity when sharing this information.
- If you need to quickly share a file, you can use a temporary file sharing service, opening it with the Tor Browser.
  - If the file you want to share is not heavier then 2GB you can use the [Disroot file uploader](https://disroot.org/en/services/upload) based on [free and open source software called Lufi](https://framagit.org/fiat-tux/hat-softwares/lufi).
  - If the file you want to share is not heavier than 50MB, you can use [share.riseup.net](https://share.riseup.net/): click the upload button, wait for the file to upload and share the link you get with your recipient. Remember that the file will be deleted after 12 hours.
- You can also send and receive files anonymously through an anonymous end-to-end encrypted [chat app](https://securityinabox.org/en/communication/secure-chat) or by sending [an email encrypted with OpenPGP](https://securityinabox.org/en/communication/secure-email/#advanced-protect-your-email-messages-with-end-to-end-encryption). Make sure to use a secure [email](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails) or [chat](https://securityinabox.org/en/internet-connection/anonymity/#chat-anonymously) account that you have set up anonymously to begin with.

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#use-tor-bridges-if-you-cant-connect-to-tor-automatically) Use Tor Bridges if you can't connect to Tor automatically

- Tor may be blocked or illegal to use in some countries. If Tor is blocked or unsafe to use in your country, you can use a [Tor "Bridge"](https://bridges.torproject.org/).
  - [Learn how to connect to Tor from China](https://support.torproject.org/censorship/#censorship_connecting-from-china).
  - [Learn how to connect to Tor from Russia](https://support.torproject.org/censorship/connecting-from-russia/).

## [Anchor](https://securityinabox.org/en/internet-connection/anonymity/\#advanced-set-up-a-whistleblowing-platform-to-receive-files-anonymously)\[Advanced\] Set up a whistleblowing platform to receive files anonymously

- Consider using [SecureDrop](https://securedrop.org/overview/).
- Consider using [GlobaLeaks](https://www.globaleaks.org/).

Learn why we recommend this

If you are planning to set up a whistleblowing platform to receive anonymous submissions, for example for an investigative journalism project, you can consider free and open-source software like SecureDrop or GlobaLeaks.

SecureDrop is an open-source whistleblower submission system focused on security. The installation procedure for SecureDrop can be complicated, but the SecureDrop team offers support to the organizations interested in using it.

GlobaLeaks is free and open-source software. It is easier to install and manage, but focused more on usability than high security, so it's recommended for organizations that don't have dedicated technical support and need an auditing, survey or file submission platform.