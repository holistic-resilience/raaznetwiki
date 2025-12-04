\_\_('Table of Contents')

Internet Connection › Circumvent internet blockages and monitoring

# [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#circumvent-internet-blockages-and-monitoring) Circumvent internet blockages and monitoring

Updated 1 October 2025

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#table-of-contents) Table of Contents

- [Check if the website or service you can't reach is really blocked](https://securityinabox.org/en/internet-connection/circumvention/#check-if-the-website-or-service-you-cant-reach-is-really-blocked)
- [Encrypt your connections and your DNS](https://securityinabox.org/en/internet-connection/circumvention/#encrypt-your-connections-and-your-dns)
- [Consider whether you really need a VPN service](https://securityinabox.org/en/internet-connection/circumvention/#consider-whether-you-really-need-a-vpn-service)
- [Consider what a VPN service can do for you](https://securityinabox.org/en/internet-connection/circumvention/#consider-what-a-vpn-service-can-do-for-you)
- [Learn how to choose a VPN service](https://securityinabox.org/en/internet-connection/circumvention/#learn-how-to-choose-a-vpn-service)
- [Choose a VPN service](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service)
- [Check if it works](https://securityinabox.org/en/internet-connection/circumvention/#check-if-it-works)
- [Consider alternatives to regular VPN services](https://securityinabox.org/en/internet-connection/circumvention/#consider-alternatives-to-regular-vpn-services)
- [Try Tor](https://securityinabox.org/en/internet-connection/circumvention/#try-tor)
- [Consider accessing and sharing content on decentralized networks](https://securityinabox.org/en/internet-connection/circumvention/#consider-accessing-and-sharing-content-on-decentralized-networks)
- [Install software that isn't accessible in your country](https://securityinabox.org/en/internet-connection/circumvention/#install-software-that-isnt-accessible-in-your-country)
- [Ask these questions about other tools to visit blocked websites](https://securityinabox.org/en/internet-connection/circumvention/#ask-these-questions-about-other-tools-to-visit-blocked-websites)
- [Advanced: Partner with OONI](https://securityinabox.org/en/internet-connection/circumvention/#advanced-partner-with-ooni)
- [Further Reading](https://securityinabox.org/en/internet-connection/circumvention/#further-reading)

If you are not able to access websites or services that are important for your activities, this might be due to blockages implemented in your local network, by your ISP or by your government. These blockages are often a form of censorship, but in most cases you can reach the blocked websites by using several tools and techniques.

[_Learn more about how the internet works and how websites can be blocked_](https://securityinabox.org/en/internet-connection/how-the-internet-works).

This guide offers a series of recommendations on:

- how to access websites and services that are blocked or censored in your country or in the local network you are connecting from (like your library, workplace, hotel, etc.);
- how to avoid that the owners or managers of the websites and services you access know where you are;
- how to avoid monitoring by your local internet provider or somebody in your local network.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#check-if-the-website-or-service-you-cant-reach-is-really-blocked) Check if the website or service you can't reach is really blocked

- Enter the address of the website or service you can't access in [the search bar of Down for everyone or just me](https://downforeveryoneorjustme.com/). Alternatively, you could ask a trusted person living in another country to try and access the website or service you would like to visit or use and let you know if they can access it.
- If the site or service is up but you can't access it, this doesn't necessarily mean it has been blocked in your country or institution. If it's a website, try accessing it with a different browser to make sure it is not failing to load due to some settings or plugins installed in your main browser. If it's a service, try using a different app or device.
- If you still can't access the website or service after these tests, try one of the tools below to circumvent a possible blockage.

Learn why we recommend this

Sometimes you may not be able to access a website or service due to reasons that are not related to censorship. The website or service may be down for technical reasons, the cache of your browser may not be updating, an extension you have installed in your browser may stop the site from working properly, your app may be outdated, etc. Especially if you have been able to access this website or service until recently, it is worth following the steps in this section to troubleshoot your issue.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#encrypt-your-connections-and-your-dns) Encrypt your connections and your DNS

- Make sure that HTTPS-only mode is enabled in your browser and check that you are accessing the HTTPS version of the web pages you want to visit.
  - [Learn how to enable HTTPS-only mode in Firefox](https://support.mozilla.org/en-US/kb/https-only-prefs#w_enabledisable-https-only-mode).
    - [Turn on Always use secure connections in Chrome/Chromium](https://support.google.com/chrome/answer/10468685?hl=en&co=GENIE.Platform%3DDesktop&oco=0#zippy=%2Csafe-browsing-protection-levels%2Cturn-on-always-use-secure-connections).
    - Read the [Security planner guide on how to set up HTTPS-Only mode in other browsers](https://securityplanner.consumerreports.org/tool/install-https-everywhere).
- Switch to a different DNS provider than the one you use now. Choose one that is based outside of your country and that supports encrypted DNS queries.
  - Learn how to change your DNS provider in [the Google guide on how to configure the network settings of any operating system to use Google Public DNS](https://developers.google.com/speed/public-dns/docs/using).
  - You can find lists of privacy-friendly DNS providers in the [Awesome Privacy page on DNS providers](https://awesome-privacy.xyz/networking/dns-providers) and in the [Mozilla policy on DNS over HTTPS providers](https://wiki.mozilla.org/Security/DOH-resolver-policy#Conforming_Resolvers).
- Encrypt your DNS traffic.
  - [Configure DNS over HTTPS in Firefox](https://support.mozilla.org/en-US/kb/dns-over-https).
  - [Use secure connections for DNS traffic in Chrome/Chromium](https://support.google.com/chrome/answer/10468685?hl=en&co=GENIE.Platform%3DAndroid#zippy=%2Cuse-a-secure-connection-to-look-up-a-sites-ip-address).
  - [Set up secure DNS in Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/privacy-whitepaper/#secure-dns).
  - By default, Android devices use Private DNS with all networks that allow for this option. To check whether Private DNS is enabled in your device, follow the instructions in the [official guide on managing advanced network settings in Android phones](https://support.google.com/android/answer/9654714?hl=en&sjid=16136785382195371122-NA#zippy=%2Cprivate-dns).
  - In iOS and macOS, DNS over HTTPS is supported but not enabled by default.

Learn why we recommend this

Sometimes web requests are blocked based on a list of unauthorized keywords applied to the page address or content. However, this form of censorship can only be applied to unencrypted web communications. By using HTTPS only mode, you will encrypt your browser's communications with the website, so that only you and the website can know what pages you are viewing and what is their content.

In other cases, censorship is applied at the level of DNS queries: what is blocked or altered is how requests to translate certain web addresses into IP addresses work. By using trusted DNS servers outside of your country and by encrypting your DNS traffic, you can avoid this censorship. On the other hand, the entity that is filtering your internet connection can see that you are using a foreign DNS provider that supports encryption and might start blocking access to it.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#consider-whether-you-really-need-a-vpn-service) Consider whether you really need a VPN service

Before you proceed to installing a VPN, ask yourself what you need exactly.

You should try using a VPN, following the instructions in the sections below, in these cases:

- if you need to hide your IP address from the websites you visit or other services you use,
- if you need to hide which websites or services you use from your local internet provider or somebody in your local network,
- if you need to circumvent internet blockages implemented in your country or in the local network you are connecting from (like your library, workplace, hotel, etc.).

But there are other cases where your need may be addressed through different solutions, for example:

- If you need to stop someone on your local network or ISP from seeing sensitive data you enter in a website, you can make sure that your connection is encrypted by enabling [HTTPS-only mode in your browser](https://securityinabox.org/en/internet-connection/circumvention/#encrypt-your-connections-and-your-dns).
- If you want to protect yourself from commercial tracking, stopping third-party cookies in your browser settings and installing [free and open-source privacy extensions in your browser](https://securityinabox.org/en/communication/tools/#firefox-add-ons-for-general-privacy-and-security) might be enough for you.
- If, on the other hand, you need to be sure your traffic cannot be traced back to you in any way, consider using the [Tor Browser](https://securityinabox.org/en/internet-connection/tools/#tor-browser) and read [our guide on anonymity to learn about other tools you can use to reliably anonymize your connections](https://securityinabox.org/en/internet-connection/anonymity).

Learn why we recommend this

A VPN service can hide your IP address from the websites you visit and can help you circumvent internet blockages, but if you need to protect yourself from snooping at the level of your local network and to avoid being profiled and tracked by your ISP and by commercial websites, a VPN will not be enough: to address these needs, you should at least make sure that [enhanced privacy settings are enabled in your browser](https://securityinabox.org/en/internet-connection/safer-browsing) and you should install addons to prevent tracking.

If you are considering using a VPN to protect your online activities from someone on your local network, a VPN may not be your best solution, as (at the moment of writing this guide) VPNs have a vulnerability called [TunnelVision](https://www.eff.org/deeplinks/2024/05/wider-view-tunnelvision-and-vpn-advice) that can allow an attacker to route your connections through their computer instead of your VPN so they can spy on your traffic.

In the most sensitive cases where you really need [to hide your IP](https://securityinabox.org/en/internet-connection/anonymity) a VPN service is not enough to achieve online anonymity because the VPN provider can see all your traffic.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#consider-what-a-vpn-service-can-do-for-you) Consider what a VPN service can do for you

VPN services offer you a connection that can make it look like you are located in a different country than you actually are, and can give your ISP the impression that you are visiting a website or using a service different than the one you are actually accessing.

Some VPN services rely on functionalities that are built into the Windows, macOS, Linux, Android and iOS operating systems. Others require you to install and configure additional software (like OpenVPN or WireGuard). Some VPN providers will offer a customised installer that handles everything for you.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#learn-how-to-choose-a-vpn-service) Learn how to choose a VPN service

Ask yourself these questions to learn how to choose a VPN service:

- **Will it work for you?** – Do you know other people in your situation who are using this VPN service? Have you confirmed with them that it does its job? If this is not the case, does the VPN offer a free trial so you can make sure it will work for you before you sign a contract? Especially if you are planning to use specific tools with your VPN (like for example peer-to-peer file sharing software), it's a good idea to check whether the VPN will work with that tool.

- **Are VPN services legal in your country?** – in some countries, VPNs are illegal and you might risk heavy fines or even imprisonment for using them. If VPNs are illegal in your country, you may want to look for a VPN service that offers obfuscated servers or for [a different censorship circumvention tool](https://securityinabox.org/en/internet-connection/circumvention/#consider-alternatives-to-regular-vpn-services).

- **Is it trustworthy?** – The most important question is whether you can trust the company or organization providing the service. When using a VPN, you are moving your point of trust from your local network and internet service provider to the VPN provider. Ask yourself if changing who can see your traffic really reduces your risks. The VPN provider will now be potentially able to observe your internet traffic instead, so you will want to ensure that you can trust them by considering the points below.

  - **What's the VPN provider's mission?** – To be sure a VPN service is trustworthy, the first thing you should research is its mission or business model: what are the goals of the people managing it? Is the VPN managed by activists who want to fight surveillance or by a company? And if it is a company, who founded it? Does it have a public face, and what background do the founders have?

  - **Does it keep logs?** – Another important feature to consider is whether the VPN service keeps logs – sooner or later, state authorities will ask a VPN provider to hand over data on one of its users for some investigation. Especially if the VPN is managed by a commercial company, it will be bound to collaborate with the investigators if it wants to stay in business. In such cases, the only way a VPN provider can avoid handing over data and breaching its users' trust is by just keeping on its servers as little information as possible on your connections. Check the privacy policy and terms of service of a VPN to figure out whether they keep logs or not. Also check the VPN's history: did it already receive requests for information by state authorities? How did it respond?

  - **Has it been audited?** – A way of making sure that a VPN is willing to protect its users as it promises to do is by checking whether it undergoes regular audits by reputable and independent third parties. Since the protection granted by a VPN service relies on the way its infrastructure is set up and managed, the only possible way to check whether it is really secure is by submitting to regular tests. Check whether it undergoes audits, when it was last audited and whether the servers where audited too. If they only had their apps audited and not the backend infrastructure, you can't be sure what they do with your data when it goes through their servers.

  - **Where is it based?** – Are the company's headquarters in a country that would comply with a request by authorities from your country? And is that country enforcing human rights and consumer protection? It is important to know whether the VPN provider will respect your privacy and rights, and whether it will be forced to collaborate with your country's authorities, especially if you are using the VPN service to secure activities that your country severely cracks down upon.

     Read more on how to find out where a VPN is based in the "How to find out where your VPN is from" section of [Paul Bischoff's _A deeper dive into the China and Russia-linked VPNs on iOS and Android_](https://www.comparitech.com/news/a-deeper-dive-into-the-china-and-russia-linked-vpns-on-ios-and-android/).
- **How large is the network?** – How many servers does the VPN have, and in how many locations? The larger the network, the more reliable your connection will be. It's also important to check whether the VPN has servers close to your region, as connections will probably be faster if you can use servers closer to you.

- **What technology does it use?** – Does the VPN use a reliable protocol and modern encryption technology? Look for services that provide at least 256-bit encryption and a modern VPN protocol like the open-source WireGuard or OpenVPN protocols.

- **Does it include a kill switch feature?** – In case of connectivity issues, the VPN might disconnect and your connection could become suddenly insecure without you knowing. To avoid this risk the best VPN services feature a kill switch that will automatically stop all connections whenever you have a connectivity issue. Note that some operating systems (like [Android](https://support.google.com/android/answer/9089766?hl=en#zippy=%2Cstay-connected-all-the-time)) provide a similar feature in their own settings.

- [Also learn about the criteria we recommend to follow when choosing a tool](https://securityinabox.org/en/about/how/#how-we-develop-the-protection-strategies-we-recommend).


## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#choose-a-vpn-service) Choose a VPN service

- See [our list of tools to protect connections](https://securityinabox.org/en/internet-connection/tools/#visit-blocked-websites) for some recommended VPN services. These include options for running your own VPN.
- Once you have identified the VPNs that work best for you, consider installing at least a couple so that you have an alternatives in case one of them doesn't work.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#check-if-it-works) Check if it works

Once you have chosen a service that could work for you, follow the steps listed in this section to check that it really works and doesn't leak your IP address.

If possible run these tests while you have good access to the internet and don't need to circumvent wide-spread censorship.

### [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#check-if-there-are-any-ip-leaks) Check if there are any IP leaks

1. Look up your current IP address. You can visit a site like [IPLocation](https://www.iplocation.net/) or [WhatIsMyIP](https://www.whatismyip.com/), or even just enter the "what is my IP?" query in the Google search bar.
   - The address will be something like `172.105.249.143` or `2a01:7e01::f03c:92ff:fecd:7e45`.
2. On that same device, turn on the VPN or other app you want to use to get around internet blockages.
3. Go back to the IP address lookup page you used in step 1 and refresh it.
   - Confirm that it now shows you a different IP address.
   - If you see the same IP address as before, the app you are using is not working as it should.
4. If the tool you're using leaks your IP address try the following steps to see if you can solve this issue:
   - Restart your device.
   - Check that your app is connecting to the VPN server.
   - Temporarily disable your firewall and your antivirus. If your IP doesn't leak after this step, check the documentation of your firewall or antivirus to make sure they don't disable the functionality of your VPN.

### [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#check-if-there-are-any-dns-leaks) Check if there are any DNS leaks

1. With your VPN turned off, open the [DNS leak test page on BrowserLeaks](https://browserleaks.com/dns). Write down the domains that show up.
2. Start your VPN and reload the [DNS leak test page](https://browserleaks.com/dns). The IP addresses you see now should be different from the one you saw in step 1. If they haven't changed, your VPN is probably leaking your DNS.

### [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#check-if-there-are-any-webrtc-leaks) Check if there are any WebRTC leaks

1. With your VPN turned off, open the [WebRTC leak test page on BrowserLeaks](https://browserleaks.com/webrtc). You should see your IP address in the Public IP Address field.
2. Start your VPN and reload the [WebRTC leak test page](https://browserleaks.com/webrtc). The IP address you see now should be different from the one you saw in step 1. If it hasn't changed, you probably have a WebRTC leak.
3. To fix this issue you can try disabling WebRTC in your browser, but consider that this will also disable video call functionalities.
   - [Learn how to disable WebRTC in your browser](https://github.com/K3V1991/How-to-disable-WebRTC-in-Chrome-Firefox-Safari-Opera-and-Edge).

Learn why we recommend this

Most VPN providers advertise their services as effective, but you should check that they work and they don't leak your IP address.

It is important to test that the VPN service you use actually works and protects you so that you are ready for when you need it (e.g. when a website you need to visit or a service you need to use is blocked). It is more difficult to ensure you are using a tool correctly in an emergency, and in critical situations even the websites where those tools can be downloaded could be blocked.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#consider-alternatives-to-regular-vpn-services) Consider alternatives to regular VPN services

If VPN services are blocked in your country or institution, you can try out alternative censorship circumvention tools to access the websites you would like to visit.

### [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#install-your-own-vpn) Install your own VPN

- Join forces with someone who lives in a different country to set up your own VPN using tools like [Outline](https://securityinabox.org/en/internet-connection/tools/#outline-vpn), [Algo](https://securityinabox.org/en/internet-connection/tools/#algo-vpn) or [Amnezia VPN](https://amnezia.org/en/self-hosted).

### [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#try-a-dedicated-censorship-circumvention-tool) Try a dedicated censorship circumvention tool

- Try [Lantern](https://lantern.io/) for [Android](https://lantern.io/download?os=android), [iOS](https://lantern.io/download?os=ios), [Linux](https://lantern.io/download?os=linux), [macOS](https://lantern.io/download?os=mac), or [Windows](https://lantern.io/download?os=windows).
- Try [Psiphon](https://psiphon.ca/) for Android (download from the [Playstore](https://play.google.com/store/apps/details?id=com.psiphon3.subscription) or [directly from Psiphon's website](https://psiphon.ca/PsiphonAndroid.apk)), [iOS](https://apps.apple.com/app/psiphon-browser/id1193362444) (requires iOS 12.0 or later), [macOS](https://apps.apple.com/us/app/psiphon/id1276263909) (requires macOS 11.0 or later and a Mac with Apple M1 chip or later), or [Windows](https://psiphon.ca/psiphon3.exe).
  - If the download pages for Psiphon are blocked, you can email [get@psiphon3.com](mailto:get@psiphon3.com) to receive an email with an alternative download link that may work.
  - Be aware that Psiphon's direct download link for Android requires you to [allow your device to install unknown apps](https://www.androidauthority.com/how-to-install-apks-31494/#1). Turning that permission on may make your device vulnerable to malware, so it's best to grant this permission only temporarily and to revoke it as soon as the installation is completed.

Learn why we recommend this

VPNs don't always work. In some countries and institutions they may be blocked as much as the web pages you would like to access.
In such cases there are alternative solutions you can use, like setting up your own VPN, which will have an IP address that isn't known to the authorities of your country, or using specific tools that use technologies designed to go around internet filters.

Algo, Outline and Amnezia VPN are open-source applications that make it easier for individuals and organizations to administer their own secure VPN service. By using these tools, people enjoying free access to the internet can set up a VPN to give access to blocked websites to people who live in countries where VPNs are filtered by their IP addresses.

Psiphon is a free and open-source censorship circumvention tool that provides uncensored access to online content by using an obfuscation layer to defend against blockages based on filters that recognize VPNs. Psiphon gets its funding from advertisers who pay to reach users with their ads.

Lantern is a censorship circumvention tool that uses a set of open-source protocols to blend in with regular internet traffic, keeping its connections unblocked and undetected.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#try-tor) Try Tor

- See our [guide on anonymity tools](https://securityinabox.org/en/internet-connection/anonymity).
- Just like websites and other resources, also the Tor network may be inaccessible in your country. In such cases, you can use a [Tor Bridge](https://bridges.torproject.org/).

Learn why we recommend this

Using free and open-source anonymity tools like the [Tor Browser](https://securityinabox.org/en/internet-connection/tools/#tor-browser) can be particularly helpful if your main concern is not only internet censorship, but also state surveillance – that is if you would like to avoid being identified as a user of censored resources because visiting certain websites or doing certain activities online is illegal and sanctioned in your country.

Tor doesn't just route your internet traffic through one service provider as a VPN would do. instead, it bounces your connections through a distributed network of relays run by volunteers all around the world, encrypting your web requests and passing them through at least three servers before reaching their destination. This way, it prevents somebody watching your internet connection from learning what sites you visit, and it prevents the sites you visit from learning your physical location.

If Tor is blocked or unsafe to use in your country, you can use [Tor Bridges](https://bridges.torproject.org/) – Tor relays that are not listed in the public Tor directory and are therefore harder to identify for ISPs or governments trying to block access to the Tor network.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#consider-accessing-and-sharing-content-on-decentralized-networks) Consider accessing and sharing content on decentralized networks

- Try [I2P](https://geti2p.net/en/).
- Try [Ceno Browser](https://censorship.no/).

Learn why we recommend this

In particularly oppressive regimes, most censorship circumvention tools may be inaccessible or risky to use. Tools based on decentralized networks of peers like I2P and Ceno Browser have been developed specifically for these cases. The idea is that if a network is not centralized, it becomes more resilient to censorship as there is not one point of failure and content can be shared and accessed on each of its nodes.

I2P is one of these anonymous, resilient networks, so you cannot be identified if you use it.

Ceno Browser is a browser that makes it possible to access censored web content. It encourages and enables the sharing of web content among users, creating a decentralized network of peers helping each other.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#install-software-that-isnt-accessible-in-your-country) Install software that isn't accessible in your country

- Download censorship circumvention apps through [Paskoocheh](https://asl19.org/en/projects/paskoocheh).

Learn why we recommend this

If you live in an oppressive regime where it is particularly hard to download censorship circumvention apps, consider getting the tools you would like to install through Paskoocheh's censorship-resilient channels – the Paskoocheh website, Android app, email bot and Telegram bot.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#ask-these-questions-about-other-tools-to-visit-blocked-websites) Ask these questions about other tools to visit blocked websites

In this guide, we have provided a number of tools you can use to stay connected to the internet despite blockages.

You may encounter other tools, recommended by friends or colleagues, and wonder whether they are safe and effective to use.

- You can find a list of censorship circumvention tools in the [Awesome anti-censorship git repository](https://github.com/danoctavian/awesome-anti-censorship).
- To decide what tools are suitable for your needs, have a look at [the criteria we use to choose tools for Security in a Box](https://securityinabox.org/en/about/#how-we-choose-the-tools-we-recommend). Also ask yourself whether the service you are planning to use [works for you](https://securityinabox.org/en/internet-connection/circumvention/#work-for-you), [is legal in your country](https://securityinabox.org/en/internet-connection/circumvention/#legal) and [can be trusted](https://securityinabox.org/en/internet-connection/circumvention/#trustworthy).

### [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#is-it-a-web-based-proxy-another-kind-of-proxy-or-standalone-software-that-must-be-installed) Is it a web-based proxy, another kind of proxy or standalone software that must be installed?

Web-based proxies can be convenient if you can't install software on a computer you do not control, or when doing so might put you at risk. However, note that reputable apps that work outside of your browser are both more secure and more reliable than web-based proxies.

If you must use a proxy through your browser, do not enter passwords or exchange sensitive information. Never use a web-based proxy with an address that begins with HTTP instead of HTTPS, as it will leave your web requests and data you enter exposed to view of the proxy owners.

Also consider that some proxies (called SOCKS proxies) are not web-based but will route all your traffic through their servers. This can help you access services that are filtered in your country or institution (for example messaging apps), but it won't encrypt your connections.

### [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#is-it-public-or-private) Is it public or private?

Public proxies can be used by anyone, free-of-charge. However, if you do not know who is providing the proxy or why, it may possibly be provided with malicious intent. Public proxies also tend to become overcrowded more quickly. This slows them down and increases the likelihood that they will be blocked. Private proxies limit access in some way, often by charging a monthly or yearly fee.

If you are able to get an account on a reliable, secure and trusted private proxy, it will probably continue working longer than a public proxy.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#advanced-partner-with-ooni) Advanced: Partner with OONI

If websites or services are blocked when accessing the internet in your region, the [Open Observatory of Network Interference (OONI)](https://ooni.org/), which collects data from these situations around the world, would love to hear from you.

If you decide to collaborate with OONI, consider that anyone monitoring your internet activity will be able to see that you are running OONI Probe. So if you are on the radar of an oppressive regime it's best to [learn more about the potential risks of running tests for OONI](https://ooni.org/about/risks/) before you begin.

## [Anchor](https://securityinabox.org/en/internet-connection/circumvention/\#further-reading) Further Reading

- Surveillance Self-Defense, [How to: Understand and Circumvent Network Censorship](https://ssd.eff.org/module/understanding-and-circumventing-network-censorship)
- [Security in a box guide on how the internet works and how it can be censored](https://securityinabox.org/en/internet-connection/how-the-internet-works)
- [Security in a box guide on anonymity tools](https://securityinabox.org/en/internet-connection/anonymity)
- [Paul Bischoff, _A deeper dive into the China and Russia-linked VPNs on iOS and Android_, comparitech, August 21, 2025](https://www.comparitech.com/news/a-deeper-dive-into-the-china-and-russia-linked-vpns-on-ios-and-android/)