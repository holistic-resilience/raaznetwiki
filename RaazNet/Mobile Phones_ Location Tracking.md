---
title: "Mobile Phones_ Location Tracking"
tags: [privacy, security, digital-rights, mobile-security, surveillance, communications]
category: "Mobile Security"
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

[Skip to main content](https://ssd.eff.org/module/mobile-phones-location-tracking#main-content)

- [About](https://ssd.eff.org/pages/about-surveillance-self-defense)
- [Language](https://ssd.eff.org/module/mobile-phones-location-tracking#)  - [English](https://ssd.eff.org/module/mobile-phones-location-tracking)
  - [አማርኛ](https://ssd.eff.org/am/module/mobile-phones-location-tracking)
  - [العربية](https://ssd.eff.org/ar/module/4c8d927f-9c2c-4622-b8f2-d29571705483)
  - [Español](https://ssd.eff.org/es/module/tel%C3%A9fonos-m%C3%B3viles-seguimiento-de-la-ubicaci%C3%B3n)
  - [Français](https://ssd.eff.org/fr/module/telephones-portables-suivi-de-la-localisation)
  - [Русский](https://ssd.eff.org/ru/module/%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D1%8B-%D0%BE%D1%82%D1%81%D0%BB%D0%B5%D0%B6%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BC%D0%B5%D1%81%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
  - [Türkçe](https://ssd.eff.org/tr/module/cep-telefonlar%C4%B1-konum-takibi)
  - [Tiếng Việt](https://ssd.eff.org/vi/module/mobile-phones-location-tracking)
  - [Português](https://ssd.eff.org/pt-br/module/telefones-celulares-rastreamento-de-localizacao)
  - [Mandarin](https://ssd.eff.org/zh-hans/module/22cba6d5-aab9-46e1-b5f3-71df662f8666)
  - [Burmese](https://ssd.eff.org/my/module/mobile-phones-location-tracking)
  - [پښتو](https://ssd.eff.org/ps/module/mobile-phones-location-tracking)
  - [ภาษาไทย](https://ssd.eff.org/th/module/mobile-phones-location-tracking)
  - [اردو](https://ssd.eff.org/ur/module/mobile-phones-location-tracking)
  - [More Translations](https://ssd.eff.org/en/other-translations)
- [Index](https://ssd.eff.org/#index)
- KeywordsSearch

[×](https://ssd.eff.org/module/mobile-phones-location-tracking#)

# Mobile Phones: Location Tracking

**Last Reviewed**: November 05, 2024

## Location Tracking [\#](https://ssd.eff.org/module/mobile-phones-location-tracking\#location-tracking)

The deepest privacy [threat ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/threat) from mobile phones—yet one that is often completely invisible—is the way that they announce your whereabouts through the signals they broadcast. There are at least four ways that an individual phone's location can be tracked by others:

- Mobile Signal Tracking from Towers
- Mobile Signal Tracking from Cell Site Simulators
- Wi-Fi and Bluetooth Tracking
- Location Information Leaks from Apps and Web Browsing

### Mobile Signal Tracking — Towers [\#](https://ssd.eff.org/module/mobile-phones-location-tracking\#mobile-signal-tracking-towers)

In all modern mobile networks, the cellular provider can calculate where a particular subscriber's phone is located whenever the phone is powered on and registered with the network. The ability to do this results from the way the mobile network is built with cellular towers, and is commonly called “triangulation.” If you’ve ever watched a modern day crime thriller, you’ve probably heard triangulation mentioned.

![Three cell phone towers have different ranges, represented by overlapping circles. A phone is shown in the area where all towers’ signal ranges meet.](https://ssd.eff.org/files/ssd/wysiwyg/pictures/740/content_mobilephones-triangulation.jpg)

One way the mobile phone company uses triangulation is to observe the signal strength that different towers receive from a particular subscriber's mobile phone, and then calculate where that phone must be located. This is done with “Angle of Arrival” measurements.

The accuracy of these measurements to figure out a subscriber's location varies depending on many factors, including the technology the provider uses and how many cell towers they have in an area. Usually, with at least three cell towers, the provider can get down to 3/4 of a mile or 1km. For modern cell phones and networks [trilateration](https://www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catchers-exploit-cell-networks#OverviewAttacks) is also used where a feature called “locationInfo-r10” is supported. This feature returns a report that contains the phone’s exact GPS coordinates, which is far more accurate than triangulation.

There is no way to hide from this kind of tracking as long as your mobile phone is powered on, with a registered [SIM card ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/sim-card), and transmitting signals to an operator's network.

Although normally only the mobile operator itself can perform this kind of tracking, a government could force the operator to turn over location [data ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/data) about a user (in real-time or as a matter of historical record). In 2010, a German privacy advocate named Malte Spitz used privacy laws to get his mobile operator to turn over the records that it had about his location. He also [published them as an educational resource](http://www.zeit.de/digital/datenschutz/2011-03/data-protection-malte-spitz) so that other people could understand how mobile operators monitor its customers this way. The possibility of government access to this sort of data is not theoretical: it is widely used by law enforcement agencies, including in the United States. In 2018, the Supreme Court ruled in [Carpenter vs. United States](https://www.eff.org/cases/carpenter-v-united-states) that under the Fourth Amendment, police must get a warrant before obtaining this type of historical location data derived from cell carriers—known as “cell site location information,” or CSLI. Historical CSLI, the court wrote, creates a “detailed chronicle of a person’s physical presence compiled every day, every moment over years.”

A related kind of government request is called a “tower dump.’ Here, a government asks a mobile operator for a list of all the mobile devices that were present in a certain area at a certain time. This could be used to investigate a crime, or to find out who was present at a particular protest. EFF has [asked courts](https://www.eff.org/deeplinks/2022/05/massachusetts-highest-court-upholds-cell-tower-dump-warrant) to find tower dumps unconstitutional because they are overbroad and lack probable cause under the Fourth Amendment.

Carriers also exchange data with one another about a device location. This data is less precise than tracking data that aggregates multiple towers' observations, but it can still be used as the basis for services that track an individual device—including commercial services that query these records to find where an individual phone is currently connecting to the mobile network. This tracking does not involve forcing carriers to turn over user data; instead, this technique uses location data available on a commercial basis.

**What you can do about it**: Since this is handled by your cellular provider, there’s not much you can do to prevent this from happening beyond not carrying your cell phone with you. If your carrier informs you that law enforcement has demanded your data through a court order or warrant, you can contact [EFF's legal assistance intake](https://www.eff.org/pages/legal-assistance) to see if we can help.

### Mobile Signal Tracking — Cell Site Simulator [\#](https://ssd.eff.org/module/mobile-phones-location-tracking\#mobile-signal-tracking-cell-site-simulator)

A government or a technically sophisticated organization can also collect location data directly, such as with a cell site simulator, also sometimes called an [IMSI Catcher](https://www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catchers-exploit-cell-networks#BasicIMSICatcher) or Stingray. These are portable, fake cell phone towers that pretend to be a real one, in order to “catch” particular users' mobile phones, and detect their physical presence, and spy on their communications. IMSI refers to the International Mobile Subscriber Identity number that identifies a particular subscriber's SIM card, though an IMSI catcher may target a device using other properties of the device as well.

![An animation: a phone connects to a cell phone tower’s weak network connection: the tower requests the ID of the phone, and the phone responds with its International Mobile Subscriber Identity (IMSI) number. A cell-site simulator — presented here as a device within a mobile vehicle — appears, providing a stronger network connection. The phone connects to the cell-site simulator’s signal. The cell-site simulator requests the ID of the phone, and the phone responds with its IMSI number.  ](https://ssd.eff.org/files/ssd/wysiwyg/pictures/741/content_cssmobilephone.gif)

The IMSI catcher needs to be taken to a particular location in order to find or monitor devices at that location. IMSI traffic interception by law enforcement requires a warrant (and [in many cases](https://www.dhs.gov/sites/default/files/publications/mgmt/law-enforcement/mgmt-dir_047-02-dept-policy-regarding-use-cell-site-simulator-technology.pdf), an additional pen register order and other protections are required). However, a “rogue” CSS, (not set up by law enforcement) would be operating outside of those legal parameters.

**What you can do**: Currently there are some defenses against IMSI catchers. On Android, you [can disable 2G connections](https://ssd.eff.org/module/attending-protest#prevent-cell-site-simulators-from-tracking-your-phone), which many IMSI catchers use. You can disable 2G on an iPhone by [enabling “Lockdown Mode,”](https://ssd.eff.org/module/how-to-enable-lockdown-mode-on-iphone) though that also disables many other features. Additionally, it’s helpful to use encrypted messaging such as [Signal](https://ssd.eff.org/module/how-to-use-signal), [WhatsApp](https://ssd.eff.org/module/how-to-use-whatsapp), or iMessage to ensure the content of your communications can’t be intercepted.

### Wi-Fi and Bluetooth Tracking [\#](https://ssd.eff.org/module/mobile-phones-location-tracking\#wi-fi-and-bluetooth-tracking)

Modern smartphones have other radio transmitters in addition to the mobile network interface. They also have Wi-Fi and Bluetooth support. These signals are transmitted with less power than a mobile signal and can normally be received only within a short range (such as within the same room or the same building), although someone using a sophisticated antenna could detect these signals from unexpectedly long distances. For example, in 2007, an expert in Venezuela received a Wi-Fi signal at a distance of 382 km or 237 mi, under rural conditions with little radio interference. However, this scenario of such a wide range is unlikely.

![A phone connects to bluetooth identifiers and wi-fi routers, sharing its MAC address as an identifiable number.](https://ssd.eff.org/files/ssd/wysiwyg/pictures/742/content_mobilephones-macaddress.jpg)

Both Bluetooth and Wi-Fi signals include a unique serial number for the device, called a MAC address, which can be seen by anybody who can receive the signal. Whenever Wi-Fi is turned on, a typical smartphone will transmit occasional “probe requests” that include the MAC address and will let others nearby recognize that this device is present. Bluetooth devices do something similar. These identifiers have traditionally been valuable tools for [passive trackers in retail stores and coffee shops](https://www.nytimes.com/interactive/2019/06/14/opinion/bluetooth-wireless-tracking-privacy.html) to gather data about how devices, and people, move around the world. Bluetooth surveillance has also been used on the U.S. border, [using devices that allegedly can capture](https://www.eff.org/deeplinks/2024/05/add-bluetooth-long-list-border-surveillance-technologies) Bluetooth MAC addresses.

However, on modern versions of iOS and Android, the MAC address included in probe requests is randomized by default, which makes this kind of tracking much more difficult. Since MAC randomization is software based, [it is fallible and the default MAC address has the potential to be leaked](https://telefonicatech.com/en/blog/privacy-breach-apple-devices-sending-real-mac-of-the-device-along-random-one). Moreover, some Android devices [may not implement MAC randomization properly](https://www.nctatechnicalpapers.com/Paper/2019/2019-mac-randomization-in-mobile-devices/download) (PDF download).

Although modern phones usually randomize the addresses they share in probe requests, many phones still share a stable MAC address with networks that they actually join, like when you connect to a pair of wireless headphones. This means that network operators can recognize particular devices over time, and tell whether you are the same person who joined the network in the past. This can happen even if you don't type your name or e-mail address anywhere or sign in to any services.

**What you can do**: Modern mobile operating systems use randomized MAC addresses on Wi-Fi. But, this is a complex issue, as many systems have a legitimate need for a stable MAC address. For example, if you sign into a hotel network, it keeps track of your authorization via your MAC address. When you get a new MAC address, that network sees your device as a new device. iOS 18 and newer [rotate the device’s MAC address](https://purple.ai/blogs/apples-ios-18-macos-15-the-impact-on-public-wifi-how-purple-can-help/) about every two weeks. On Android, a similar feature is called “ [Randomized MAC address](https://support.google.com/android/answer/9654714?hl=en#zippy=%2Cchange-more-wi-fi-settings%2Cprivate-dns%2Cfind-your-phones-mac-address).” If you are in a situation where you are concerned about this sort of surveillance, you can turn Wi-Fi or Bluetooth off on your phone temporarily.

### Location Information Leaks From Apps and Web Browsing [\#](https://ssd.eff.org/module/mobile-phones-location-tracking\#location-information-leaks-from-apps-and-web-browsing)

Modern smartphones provide ways for the phone to determine its own location, often using GPS, but also sometimes using other services provided by location companies (which usually ask the company to guess the phone's location based on a list of cell phone towers or Wi-Fi networks that the phone can see from where it is). This is packaged into a feature both Apple and Google call “Location Services.” Apps can ask the phone for this location information and use it to provide services that are based on location, such as maps that display your location on the map.

![A “location services”-like settings menu on an illustrated phone.](https://ssd.eff.org/files/ssd/wysiwyg/pictures/743/content_mobilephones-locationservices.jpg)

Some of these apps will then transmit your location over the network to a service provider. This could provide a way for the application and third parties the service provider shares with to track you. The app developers might not intend to track users, but they might still end up with the ability to do that, and they might end up revealing location information about their users to governments or a [data breach ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/glossary/data-breach).

In each case, location tracking is not only about finding where someone is right now, like in an exciting movie chase scene where agents are pursuing someone through the streets. It can reveal historical activities and also suggest information about their beliefs, participation in events, and personal relationships. For example, location tracking could be used to suggest when people are in a romantic relationship by following who they visit during certain times of day, to find out who attended a particular meeting, who was at a particular protest, or to try to identify a journalist's confidential source.

The [location data collected in these apps has been purchased](https://www.eff.org/issues/location-data-brokers) by law enforcement without a warrant, as [we’ve](https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police) [seen](https://www.eff.org/deeplinks/2022/06/how-federal-government-buys-our-cell-phone-location-data) [numerous](https://www.eff.org/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech) [times](https://www.eff.org/deeplinks/2022/08/how-law-enforcement-around-country-buys-cell-phone-location-data-wholesale). This [can include](https://sls.eff.org/technologies/real-time-location-tracking) both historical and real-time location data.

**What you can do**: Cut access to your location in as many of your apps as possible, or only provide apps with “course” or “approximate” location when you can. Both Android and iPhone allow you to choose whether an app can access your location, and how much data it can access if so. Think about whether an app needs your location to function. For example, a navigation app for driving directions will need your exact location when you’re using the app. But does your weather app need to know exactly where you are or would manually typing in your zip code suffice? Does that game you downloaded need your location at all? Revoke access any time you’re not sure. You can always change your mind.

On iPhone, [follow these directions](https://support.apple.com/en-us/102647) to review the apps you’ve given location access to. On Android, review the apps you’ve given location access to [by following these instructions](https://support.google.com/android/answer/3467281?hl=en-GB&sjid=4808572162827578581-NC).

### Behavioral Data Collection and Mobile Advertising Identifiers [\#](https://ssd.eff.org/module/mobile-phones-location-tracking\#behavioral-data-collection-and-mobile-advertising-identifiers)

In addition to the location data collected by some apps and websites, many apps share information about more basic interactions, such as app installs, opens, usage, and other activity. This information is often shared with dozens of third-party companies throughout the advertising ecosystem enabled by real-time bidding (RTB). Despite the mundane nature of the individual data points, in aggregate this behavioral data can still be very revealing.

Advertising technology companies convince app developers to install pieces of code in software development kit (SDK) documentation in order to serve ads in their apps. These pieces of code collect data about how each user interacts with the app, then share that data with the third-party tracking company. The tracker may then re-share that information with dozens of other advertisers, advertising service providers, and data brokers. This whole process takes just milliseconds.

![Underneath a full-screen mobile ad: code for Software Development Kits (SDKs). The phone sends a packet of user data, like number of installs, opens, gender, activity and location, to a remote server.  ](https://ssd.eff.org/files/ssd/wysiwyg/pictures/744/content_sdk.jpg)

This data becomes meaningful thanks to the mobile advertising identifier (MAID), a unique random number that identifies a single device. Each packet of information shared during an RTB auction is usually associated with a MAID. Advertisers and data brokers can pool together data collected from many different apps using the MAID, and therefore build a profile of how each user identified by a MAID behaves. MAIDs do not themselves encode information about a user’s real identity, but it’s often trivial for data brokers or advertisers to associate a MAID with a real identity. They have several tactics for doing this, like collecting a name or email address within an app.

Mobile ad IDs are built into both Android and iOS, as well as a number of other devices like game consoles, tablets, and TV set top boxes. On Android, every app, and every third-party installed in those apps, has access to the MAID by default. In the latest versions of iOS, apps need to ask permission before collecting and using the phone’s mobile ad ID. On Android, you can remove the ad ID, but you’ll have to dig into the settings.

Behavioral data collected from mobile apps is used primarily by advertising companies and data brokers, usually to do behavioral targeting for commercial or political ads. But [governments have been known to piggyback](https://www.wired.com/story/how-pentagon-learned-targeted-ads-to-find-targets-and-vladimir-putin/) on the surveillance done by private companies.

**​​What you can do**: Both iOS and Android offer ways to disable app’s access to the ad ID, or just disable the feature entirely. On Android, [follow Google’s directions here](https://support.google.com/android/answer/13720755?hl=en). On iPhone, [don’t allow apps to ask to track](https://support.apple.com/guide/iphone/control-app-tracking-permissions-iph4f4cbd242/ios) you.

- [Copyright (CC BY)](https://www.eff.org/copyright)
- [Privacy](https://www.eff.org/policy)