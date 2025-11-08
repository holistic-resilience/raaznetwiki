---
title: "How to_ Detect Bluetooth Trackers"
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

[Skip to main content](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#main-content)

- [About](https://ssd.eff.org/pages/about-surveillance-self-defense)
- [Language](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#)  - [English](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers)
  - [አማርኛ](https://ssd.eff.org/am/module/how-to-detect-bluetooth-trackers)
  - [العربية](https://ssd.eff.org/ar/module/how-to-detect-bluetooth-trackers)
  - [Español](https://ssd.eff.org/es/module/how-to-detect-bluetooth-trackers)
  - [Français](https://ssd.eff.org/fr/module/how-to-detect-bluetooth-trackers)
  - [Русский](https://ssd.eff.org/ru/module/how-to-detect-bluetooth-trackers)
  - [Türkçe](https://ssd.eff.org/tr/module/how-to-detect-bluetooth-trackers)
  - [Tiếng Việt](https://ssd.eff.org/vi/module/how-to-detect-bluetooth-trackers)
  - [Português](https://ssd.eff.org/pt-br/module/how-to-detect-bluetooth-trackers)
  - [Mandarin](https://ssd.eff.org/zh-hans/module/how-to-detect-bluetooth-trackers)
  - [Burmese](https://ssd.eff.org/my/module/how-to-detect-bluetooth-trackers)
  - [پښتو](https://ssd.eff.org/ps/module/how-to-detect-bluetooth-trackers)
  - [ภาษาไทย](https://ssd.eff.org/th/module/how-to-detect-bluetooth-trackers)
  - [اردو](https://ssd.eff.org/ur/module/how-to-detect-bluetooth-trackers)
  - [More Translations](https://ssd.eff.org/en/other-translations)
- [Index](https://ssd.eff.org/#index)
- KeywordsSearch

[×](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#)

# How to: Detect Bluetooth Trackers

**Last Reviewed**: July 15, 2024

On May 13, 2024, both [Apple](https://www.apple.com/newsroom/2024/05/apple-and-google-deliver-support-for-unwanted-tracking-alerts-in-ios-and-android/) and [Google](https://security.googleblog.com/2024/05/google-and-apple-deliver-support-for.html) announced they’d start supporting cross-platform operating system-level notifications for some third-party trackers, similar to the AirTag detection warnings. In theory, this means your phone may detect some Bluetooth trackers without a third-party app. In our testing, we’ve found these new models aren’t always detected. For now, we still recommend using AirGuard to locate non-supported trackers. Legitimate operating system-level notifications from Apple and Google look like this: “(Device name) detected near you,” or “Unknown items detected with you.” You can follow the on-screen instructions on your phone, just as you would in the AirTag sections below.

#### Table of contents

- [What's a Bluetooth Tracker?](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-s-a-bluetooth-tracker)  - [What Common Bluetooth Trackers Look Like](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-common-bluetooth-trackers-look-like)
- [What it Looks Like When Your Phone Automatically Finds a Tracker](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-it-looks-like-when-your-phone-automatically-finds-a-tracker)  - [On Android Devices](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#on-android-devices)
  - [On iPhones](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#on-iphones)
- [How to Manually Search for a Bluetooth Tracker](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#how-to-manually-search-for-a-bluetooth-tracker)  - [Manual Search on Android Devices](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#manual-search-on-android-devices)
  - [Manual Search on iPhones](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#manual-search-on-iphones)
- [What to Do If You Find an Unknown Tracker](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker)

Bluetooth location trackers such as AirTags, Tile, and Samsung SmartTags are marketed as a way to keep track of luggage or a misplaced wallet, but they can also be easily slipped surreptitiously into a bag or car, allowing stalkers and abusers unprecedented access to a person’s location without their knowledge. These devices are small enough to fit inside wallets or on a keychain, which makes them difficult to find, especially if you don't know what you're looking for.

If you have an Android device or iPhone, you can search for Bluetooth location trackers that might have been placed on you, in your bag or on a car. Your phone may also send you an alert if it detects one of these trackers traveling with you, though the timing of that alert may vary, and you may only get a [notification for specific brands of Bluetooth trackers](https://www.eff.org/deeplinks/2023/05/victory-apple-and-google-collaborate-detecting-unwanted-location-trackers).

This guide will detail what your phone can detect on its own, and which trackers you need a third-party app to detect. Keep in mind that the reliability of detection apps isn't perfect and you should not rely on them entirely.

## What's a Bluetooth Tracker? [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#what-s-a-bluetooth-tracker)

Bluetooth trackers are small battery-powered devices meant to track property. They use Bluetooth to communicate with other devices, usually phones, to piggyback on a cell or Wi-Fi connection to send their location to the owner of the tracker. The reliability and accuracy of these trackers is dependent on the network they're attached to. For example, Apple's AirTags can piggyback on every iPhone within Bluetooth range (about 30 feet), meaning in most cities and towns they'll be very accurate. Other brands work similarly, but on their own networks. Bluetooth trackers do not have GPS built into them and aren't as accurate as GPS. In order to use a Bluetooth tracker, the owner must register the tracker to an account, which typically also links the tracker to some combination of a name, username, or phone number.

Most Bluetooth trackers allow the owner to "share" the tracker's location with others. For example, an AirTag owner [can share the location](https://support.apple.com/guide/iphone/share-airtag-item-find-iphone-iph419cc5f28/ios) of an AirTag with up to three other people. Users of Life360’s Tile [can share with an unlimited number](https://support.thetileapp.com/hc/en-us/articles/205332837-Sharing-a-Tile) of people. If an AirTag is shared with you or someone you are with, you will not get "unknown tracker" alerts. Also, if you scan an AirTag to find its owner, it will not indicate that it's being shared with someone else.

It works like this: let's say you place a Bluetooth tracker on a bicycle, and your bicycle is then lost. The tracker will constantly ping nearby phones telling the phones where it is. If those phones are set up to work with the tracker (like all iPhones are by default with AirTags, or like a Tile tracker will do with other Tile users and with Amazon’s Sidewalk network), the phone sends the approximate location of that tracker to the manufacturer, so you, the owner of the tracker, can then see where the tracker is. From the perspective of the owner, it will look something like this:

![On the left is a screenshot from Apple's Find My app on iPhone, on the right is Tile's app, also on iPhone.](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1214/image-20240312080308-76.jpeg)_On the left is a screenshot from Apple's Find My app on iPhone, on the right is Tile's app, also on iPhone._

While device manufacturers repeatedly suggest these are meant only for tracking physical property, it is very easy for someone to place one of these trackers on a person. To combat stalking, some Bluetooth trackers provide a means for non-owners to locate a tracker if it is near you, either through phone apps or by making a sound. We'll get into how those apps do and don't work below, but first it's good to get an idea of what you're looking for.

### What Common Bluetooth Trackers Look Like [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#what-common-bluetooth-trackers-look-like)

Some brands, like Tile and Chipolo, make a handful of different designs, so it's worth looking at the product pages to familiarize yourself with each offering so you know what to look for. Here are some of the most popular trackers:

- [Apple AirTags](https://www.apple.com/airtag/)
- [Life360 Tile](https://www.tile.com/products)
- [Samsung SmartTags](https://www.samsung.com/us/mobile/mobile-accessories/phones/?category_names=Phones&accessories_type=SmartThings)
- [Chipolo](https://chipolo.net/en/pages/chipolo-collection)

Currently, only Apple AirTags alert you with a sound effect when they are traveling with you and not with the owner, and even those can take up to 24 hours before they'll start emitting noises. [This video](https://www.youtube.com/watch?v=c0TVHPHRjXg) details what sound an AirTag makes.

If you do not own a smartphone, the AirTag's beeping sounds are likely the only clue you'll have that someone has placed a tracker on you. However, know that it's possible for someone to disable that sound effect.

## What it Looks Like When Your Phone Automatically Finds a Tracker [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#what-it-looks-like-when-your-phone-automatically-finds-a-tracker)

Both Android and iOS can automatically detect when an unknown AirTag is traveling with you. "Unknown" means the tracker has been paired with someone else's phone, but is not currently connected to their phone. For example, if you are with a friend who has an AirTag attached to their keys, you will not get a notification about that Bluetooth tracker. However, if that person lends you their keys for the day and you are not physically together with your friend for the day, you should get a notification about an "unknown" tracker.

Your phone will not detect the tracker immediately and it can take up to 24 hours before you get a notification. This feature currently only works with AirTags without needing to download an extra app, though [both Android and Apple have announced plans](https://www.eff.org/deeplinks/2023/08/industry-discussion-about-standards-bluetooth-enabled-physical-trackers-finally) to support other Bluetooth trackers, like those made by Life360 and Samsung. Other Apple Bluetooth devices that use the company's "Find My" network, like wireless headphones, can also trigger these alerts.

In order for detection to work, you need to enable [certain services](https://ssd.eff.org/playlist/privacy-breakdown-of-mobile-phones) on your phone, including Bluetooth, some location services, and notifications. Most of these are enabled by default when you first set up your phone, but depending on [your security plan](https://ssd.eff.org/module/your-security-plan), you may have disabled them. Here are directions for checking they're enabled for [Android](https://support.google.com/android/answer/13658562?hl=en#zippy=%2Candroid-location-settings-privacy) and [iPhone](https://support.apple.com/en-us/HT212227).

If you get an unknown tracker notification, that means there is a Bluetooth tracker that your phone has detected moving with you. Before you panic, remember that these notifications can still show up for a legitimately used tracker, like the example above when a friend gave you their keys with an AirTag attached to them.

But an unknown tracker notification can also mean someone placed a Bluetooth tracker on you or something you own, without your knowledge. It's important to know what these notifications look like, and what to do about them if you get one.

Once you get a notification, search anywhere you think an object about the size of a U.S. Quarter (or 1 Euro) could be hidden, including any pockets or the lining of bags or jackets, or underneath a car. We most commonly hear of them being hidden inside bags and on cars, including behind the license plate.

### On Android Devices [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#on-android-devices)

#### **AirTag Notifications on Android 14+**

As long as your phone can run Android 14 or newer (you can check which [operating system ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/th/glossary/dfa3cea7-5d21-4bc3-9aea-6b5398edf727) you have installed under _**Settings**_ \> _**About Phone**_ \> _**Android Version**_), it can detect AirTags (but not other Bluetooth trackers) natively without downloading any extra apps. This feature is enabled by default, but if you want to double-check, then open _**Settings**_ \> _**Safety & emergency**_ \> _**Unknown tracker alerts**_ and make sure "Allow alerts" is enabled.

These settings may vary depending on which version of Android you have and which phone you have. Refer to your phone's manufacturer's website if these directions do not work.

If your phone detects an AirTag, you will get a notification that looks like this:

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1202/image-20240312080308-77.jpeg)_A notification for an unknown AirTag on Android 14._

Tap the notification, and you'll see a map along with the time and date that shows roughly when your phone noticed the tracker. Even though a map is displayed, that doesn't mean the owner of the AirTag was viewing your location at that time. The AirTag's owner cannot see a history of the AirTag's movement, just the current location when they open the "Find My" app on an Apple device. This is not always the case with other trackers, like Tile and Samsung SmartTags, which may provide a history to the owner (we'll get to [how to detect those below](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#Automatic%20AirGuard)).

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1207/image-20240312080308-78.jpeg)_Android's "Unknown AirTag" search screen._

If you tap "Play sound" it should trigger the AirTags beeping sound to help you find it (this doesn't always work and you may end up with an error message, even if an AirTag is nearby, so don't rely on it). Once you find the tracker, hold the AirTag to the back of your phone to get more information about it, including the last four digits of the phone number of the registered owner, and the serial number which can be useful to confirm any suspicions you may have, or if you decide to contact law enforcement. Keep in mind this can be a [burner phone ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/th/glossary/b541da06-4197-4880-88e4-3342258d7f92) or a secondary phone number. Likewise, this screen will not display any indication that an owner of an AirTag shared the AirTag's location with others. After you find the AirTag, proceed down to the [what to do if you find a tracker section](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker) below.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1197/image-20240312080308-79.jpeg)_After scanning an AirTag, you're shown information about the owner, including the last four digits of the phone number they used on their Apple account._

#### **Other Unknown Tracker Notifications with AirGuard**

If you cannot update to Android 14 on your phone, or you want automatic tracker detection for more than just AirTags, then you'll need to use a third-party app. There are a number of apps that can search for trackers, but we've found [AirGuard](https://github.com/seemoo-lab/AirGuard) useful at detecting the most popular trackers. But in our testing for this guide, the app was not perfect and on a couple occasions took longer than expected to register an unwanted tracker.

Download [AirGuard](https://play.google.com/store/apps/details?id=de.seemoo.at_tracking_detection.release) from the Google Play Store and open the app. You'll be asked to allow a few permissions that are required for the app to work: location, nearby devices, and notifications. If you're concerned about enabling the location permission, the app can still work without access to location, but will not include a location history of where the app found the tracker. Here is AirGuard’s [privacy policy.](https://tpe.seemoo.tu-darmstadt.de/privacy-policy.html)

Once you get through the permissions, you'll be taken to the app's main screen.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1203/image-20240312080308-80.jpeg)_AirGuard's dashboard on Android._

There are a number of settings in AirGuard you can change to fit your needs, but the default settings are enough to send you a notification when the app detects an unknown tracker following you. When AirGuard detects a tracker that's been following you, you will get a notification that looks like this.

Tap the notification, and it'll open AirGuard. If you enabled the location permission, you will see a map of where your phone first noticed the tracker, and a number of options for what to do next.

If this is a tracker you know of, you can tap "Ignore Device" to stop getting notifications about it. While not likely due to Bluetooth's short range, there might be false detections of trackers. If you are somewhere that you know for certain no tracker is with you, you can tap "False Alarm."

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1212/image-20240312080308-81.jpeg)_An AirGuard notification on Android._

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1209/image-20240312080308-82.jpeg)_AirGuard's map screen on Android._

If you have not already found where the Bluetooth tracker was hidden, tap "Detailed Scan." This shows a screen with a percentage number on it. The number is how strong the signal between your phone and the tracker is, and works sort of like radar. Walk around with your phone to see if the percentage gets stronger. This indicates you're getting closer to the Bluetooth tracker. If the percentage goes down, it means the signal is weaker, which means you're moving in the wrong direction.

Once it's around 90% or above, you should be very close to the tracker. After you find it, proceed down to the [what to do if you find a tracker section](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker) below.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1208/image-20240312080308-83.jpeg)_Airguard's tracker search screen on Android._

### On iPhones [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#on-iphones)

#### **AirTag Notifications with iOS 14.5+**

Any iPhone running iOS 14.5 or newer will automatically detect an unknown AirTag that's following you and send you an alert (You can check which version of the operating system you are running by opening **_Settings_** \> _**General**_ \> _**About**_ \> _**iOS Version**_). You can double-check that this setting is enabled by opening up _**Settings**_ \> _**Notifications**_ \> _**Tracking Notifications**_ and make sure "Allow Notifications" is enabled.

If your phone detects an unknown AirTag traveling with you, the notification will look like this:

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1195/image-20240312080308-84.jpeg)_Apple's unknown AirTag notification on an iPhone._

Tap the notification, and you will see a history of everywhere you've been since your phone first noticed the AirTag. Even though a map is displayed, that doesn't mean the owner of the AirTag was viewing your location at that time. The AirTag's owner cannot see a history of the AirTag's movement, just the current location when they open the "Find My" app. This is not always the case with other trackers, like Tile and Samsung SmartTags, which may provide a history to the owner (we'll get to how to detect those [below](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#iPhone%20Airtags)).

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1213/image-20240312080308-85.jpeg)_Apple's "Find My" iPhone app showing the history of an AirTag._

If this is an AirTag you know about, like in the above example where you've borrowed a friend's keys and they have an AirTag attached to them, you can tap "Pause Tracking Notifications" to disable notifications for that specific AirTag.

Otherwise, you have a couple options to help in your search for an unknown AirTag if you do not know where it is. Tap the "Play Sound" option to make the AirTag play a beeping sound to help you locate it. If that does not help you locate the AirTag, tap the "Find" option. If you're close enough, you will see a screen that attempts to guide you to the exact location of the AirTag with arrows. Follow the directions on screen to find it.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1190/image-20240312080308-86.jpeg)_Apple's search for an AirTag screen on iPhone._

Once you locate the AirTag, and confirm it's unknown to you, scroll down and tap "Learn About This AirTag." This will open your [web browser ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/th/glossary/a7381d1e-9ca0-438f-acd4-58c35201e542) and take you to a website that lists the serial number and the last four digits of the phone number that's registered to that AirTag, which can be useful to confirm any suspicions you may have or if you decide to contact law enforcement. Keep in mind this could link to a burner phone or a secondary phone number. Likewise, this screen will not display any indication that an owner of an AirTag shared the AirTag's location with others. After you find the AirTag, proceed down to the [what to do if you find a tracker section](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker) below.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1193/image-20240312080308-87.jpeg)_After scanning an AirTag, you're shown information about the owner, including the last four digits of the phone number they used on their Apple account._

#### **Other Unknown Tracker Notifications with AirGuard**

If you need to search for more than just AirTags, then you'll need a third-party app. There are a number of apps that can search for trackers, but we've found [AirGuard](https://github.com/seemoo-lab/AirGuard-iOS) useful at detecting several types of trackers. But in our testing for this guide, the app was not perfect and on a couple occasions took longer than expected to register an unwanted tracker.

Download and then open the [AirGuard](https://apps.apple.com/us/app/airguard-tracking-protection/id1659427454) app from the Apple App Store. You'll be asked to allow a few permissions that are required for the app to work: location, nearby devices, and notifications. If you're concerned about enabling the location permission, the app can still work without access to location, but will not include a location history of where the app found the tracker. Here is AirGuard’s [privacy policy](https://tpe.seemoo.tu-darmstadt.de/privacy-policy.html).

If AirGuard detects a tracker, you will get a notification that looks like this.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1198/image-20240312080308-88.jpeg)_An example of a notification from AirGuard on iPhone._

Tap the notification, and AirGuard will open up to this screen, showing a map and history of where your phone first noticed the tracker.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1200/image-20240312080308-89.jpeg)_Airguard's iPhone app showing some of the history of when a tracker was detected._

You have a few options on this screen: "Locate Tracker," which we'll get to shortly, "Observe Tracker," and "Ignore Tracker." The "Observe Tracker" option allows you to set a timer that will send you another notification in an hour if the tracker is still following you, which is useful if it's still not clear if this is an "unknown" tracker. Tap "Ignore Tracker" if you know what the Bluetooth tracker is and do not want to get notifications about it anymore.

If you do not know who owns the tracker or where it is, tap the "Locate Tracker" option. This shows a screen with a percentage on it. This number is how strong the signal between your phone and the tracker is, and works sort of like radar. Walk around with your phone to see if the percentage gets stronger. This indicates you're getting closer. If the percentage goes down, it means the signal is weaker, which means you're moving in the wrong direction.

Once it's around 90% or above, you should be very close to the tracker. After you find it, proceed down to the [what to do if you find a tracker section](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker) below.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1205/image-20240312080308-90.jpeg)_Airguard for iPhone's search feature._

## How to Manually Search for a Bluetooth Tracker [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#how-to-manually-search-for-a-bluetooth-tracker)

Since phones only detect AirTags and only alert you after a certain amount of time has passed, you should also know how to search for Bluetooth trackers manually. This way, if you suspect a tracker was placed on you but you cannot physically find it, you can use the app to help you immediately.

### Manual Search on Android Devices [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#manual-search-on-android-devices)

#### **Search for AirTags with Android 14+**

You can manually search for AirTags without the need to download a third-party app as long as your phone can run Android 14 or newer.

To do so, open _**Settings**_ \> _**Safety & emergency**_ \> _**Unknown tracker**_ alerts, then tap the "Scan now" button to initiate the scan. If an AirTag is found, you'll see this screen.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1194/image-20240312080308-91.jpeg)_Android's "Manual Scan" screen for Bluetooth trackers._

Tap the tracker icon, and you're taken to the same screen that appears if an unknown tracker is automatically detected. Here, you have the option to "Play sound." This should initiate a beeping sound to help you find the AirTag, though we found it doesn't always work reliably.![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1199/image-20240312080308-92.jpeg)_Android's screen for showing a found AirTag._

Once you find the AirTag, you can hold the white side of it to the back of your phone to open up a browser window that displays the serial number and the last four digits of the owner's phone number. You may need to hold it up to your phone for a few seconds before this works. If you still do not know who owns the AirTag, take a screenshot to save the information, and proceed down to the [what to do if you find a tracker section](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker) below. Keep in mind this can be a burner phone or a secondary phone number. Likewise, this screen will not display any indication that an owner of an AirTag shared the AirTag's location with others.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1196/image-20240312080308-93.jpeg)_After scanning an AirTag, you're shown information about the owner, including the last four digits of the phone number they used on their Apple account._

#### Search for Other Trackers with AirGuard

If you cannot update to Android 14 on your phone, or you want to search for more than just AirTags, then you'll need to use [AirGuard](https://play.google.com/store/apps/details?id=de.seemoo.at_tracking_detection.release) here as well. If you haven't already downloaded the app and enabled the permissions, do so now. You'll be asked to allow a few permissions that are required for the app to work: location, nearby devices, and notifications. If you're concerned about enabling the location permission, the app can still work without access to location, but will not include a location history of where the app found the tracker.

Open AirGuard and tap the "Scan" button with a radar icon at the bottom of the screen. After a brief animation, you'll be shown any Bluetooth trackers the app detects nearby. This type of manual scan works best when you're somewhere away from other people, as the results may include trackers you purchased yourself or any trackers owned by someone nearby. For example, if you initiate this scan in a parking lot or in an apartment building, you will likely see a bunch of results, most of which are not being used to track you.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1211/image-20240312080308-94.jpeg)_AirGuard's scan screen, showing a number of results, on Android._

Tap any tracker you do not recognize, and you're taken to a screen with more information about the tracker.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1191/image-20240312080308-95.jpeg)_AirGuard's device screen after you tap a specific tracker on Android._

For AirTags, you are given the option to play a sound to help you locate it, though this doesn't always work very well and may not always initiate a sound. If that is not an option or doesn't work, you can use a radar-like search feature. Tap the "Detailed Scan" button, where you will see a screen with a signal strength meter. Walk around, and if the signal gets stronger, keep walking in that direction. If it gets weaker, try another direction.

Once it's around 90% or above, you should be very close to the tracker. Proceed down to the [what to do if you find a tracker section](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker) below.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1204/image-20240312080308-96.jpeg)_AirGuard's scan screen on Android._

### Manual Search on iPhones [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#manual-search-on-iphones)

You cannot manually search for AirTags from an iPhone without downloading a separate app, like AirGuard. Searching for Bluetooth trackers with AirGuard is straightforward, though your options for what you can do to find Tiles and SmartTags are more limited than what's possible with AirTags.

Download and then open [AirGuard](https://apps.apple.com/us/app/airguard-tracking-protection/id1659427454) if you haven't already done so. You will need to allow several permissions for the app to work, including your location, notifications, and Bluetooth.

Tap the "Manual Scan" button in the bottom menu bar.

![AirGuard's home screen, on iPhone.](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1201/image-20240312080308-97.jpeg)_AirGuard's home screen, on iPhone._

The next screen will display any trackers the app detects. This type of manual scan works best when you're somewhere away from other people, as the results may include trackers you purchased yourself or just any legitimate trackers from someone nearby. For example, if you initiate this scan in a parking lot or in an apartment building, you will likely see a bunch of results, most of which are not being used to track you.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1210/image-20240312080308-98.jpeg)_AirGuard's "Scan" screen, on iPhone._

If you see an unknown tracker, tap the name of the tracker, then on the next screen tap "Locate Tracker." You will see a screen with a signal strength meter.

Walk around, and if the signal gets stronger, keep walking in that direction. If it gets weaker, try another direction. Some trackers, like AirTags, will have the option to "Play Sound," which you can tap to trigger a sound effect if the tracker has a speaker. If you get an alert that says "Playback Failed," that means the tracker is still connected to the owner's phone, meaning they are nearby. It is also possible to physically damage and disable an AirTag’s speaker, so you may not hear a sound even though the signal is getting stronger.

This can mean a couple different things: it may indicate that it's a nearby stranger's AirTag who isn't tracking you, or it can mean that the AirTag hasn't been disconnected from the owner long enough to be marked as "unknown" yet. This is why it's important to do this test far away from other people when you can. If you find an unknown tracker, proceed to the [what to do if you find a tracker section](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers#what-to-do-if-you-find-an-unknown-tracker) below.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1192/image-20240312080308-99.jpeg)_AirGuard search function, on iPhone._

## What to Do If You Find an Unknown Tracker [\#](https://ssd.eff.org/module/how-to-detect-bluetooth-trackers\#what-to-do-if-you-find-an-unknown-tracker)

If you find an unknown Bluetooth tracker, it's important to consider your next steps carefully. What's best for you will depend on your situation, but here are a couple factors to keep in mind.

[A safety plan](https://www.thehotline.org/plan-for-safety/create-your-personal-safety-plan/) is an important step to take before you do anything else. If you are in a relationship with an abusive person, that abusive person may be the owner of the device and could be using it to track you. If you disable the device and the abusive person can’t track your location anymore, they may make other abusive choices and engage in behavior that is more dangerous to you. Before letting that abusive person know that you are aware of their tracking, develop a plan to do that in a safe way. A local advocate for victims of domestic violence can help you create that plan. If you live in the United States, you can find a local advocate through the [National Domestic Violence Hotline](https://www.thehotline.org/) by calling 1-800-799-7233, or by texting “Start” to 88788.

If you believe that disabling an unknown tracker is a safe thing for you to do, you can disable any tracker by removing its battery. Some, like AirTags, show you how to disable it in the app when it's detected. Others, like those made by Samsung and Tile, may require a special tool—like a paperclip—to remove the battery. If you disable a Bluetooth tracker this way, whoever put it there will be alerted and will likely assume you found it.

![](https://ssd.eff.org/files/ssd/wysiwyg/pictures/1206/image-20240312080308-100.jpeg)_Directions for how to disable an AirTag on an iPhone._

You can sometimes learn additional information about who owns a Bluetooth tracker after you find it, though only AirTags provide much [data ![](https://ssd.eff.org/assets/efforg/info-7ae1fb29e1e734b20023f3e3470316c82b84a7e4b9f1d1e2f49e399f1f8de2d3.png)](https://ssd.eff.org/th/glossary/308108ca-6f5b-40fe-90ce-69fea66c19de). If you hold an AirTag to the back of your phone, you'll be taken to a website that lists the serial number and the last four digits of the owner's phone number. Tile, Samsung SmartTags, and Chipolo do not have a similar feature, though some Chipolo models will work with Apple's "Find My" app to display similar info to what you get with AirTags.

If you feel like your safety is at risk, you may wish to contact law enforcement or a trusted friend before taking any action with the tracker itself. It's very likely that if you disable the tracker, the owner will know you found it. Depending on the maker of the Bluetooth tracker, law enforcement can sometimes request information from the manufacturer. Be sure to take screenshots of any information you found, being sure to include the serial number of the tracker if it's available.

- [Copyright (CC BY)](https://www.eff.org/copyright)
- [Privacy](https://www.eff.org/policy)