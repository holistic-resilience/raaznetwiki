\_\_('Table of Contents')

# [Anchor](https://securityinabox.org/en/tools/signal/\#protect-yourself-and-your-communications-when-using-signal) Protect yourself and your communications when using Signal

Updated 23 September 2025

## [Anchor](https://securityinabox.org/en/tools/signal/\#table-of-contents) Table of Contents

- [The pros and cons of using Signal](https://securityinabox.org/en/tools/signal/#the-pros-and-cons-of-using-signal)
- [Before you start using Signal](https://securityinabox.org/en/tools/signal/#before-you-start-using-signal)
- [Install Signal](https://securityinabox.org/en/tools/signal/#install-signal)
- [Use a proxy if Signal is blocked in your country](https://securityinabox.org/en/tools/signal/#use-a-proxy-if-signal-is-blocked-in-your-country)
- [Create a new account](https://securityinabox.org/en/tools/signal/#create-a-new-account)
- [Protect your account](https://securityinabox.org/en/tools/signal/#protect-your-account)
- [Use Signal more safely](https://securityinabox.org/en/tools/signal/#use-signal-more-safely)
- [Secure your Signal communications](https://securityinabox.org/en/tools/signal/#secure-your-signal-communications)
- [Protect your groups](https://securityinabox.org/en/tools/signal/#protect-your-groups)
- [Check suspicious access](https://securityinabox.org/en/tools/signal/#check-suspicious-access)
- [Consider using Molly as an alternative client for Signal](https://securityinabox.org/en/tools/signal/#consider-using-molly-as-an-alternative-client-for-signal)
- [Resources](https://securityinabox.org/en/tools/signal/#resources)

- [![Project website](https://securityinabox.org/media/en/logos/signal-logo.png)](https://signal.org/)

[Project website](https://signal.org/)

**Signal** is a free and open-source messaging app that protects your communications using end-to-end encryption. It is developed by [the Signal Foundation](https://signalfoundation.org/) and is available for all major operating systems, but an account can only be created by installing it on a smartphone.

Read this guide to learn how to use Signal more safely and how to secure your account.

Also see [our guide on how to use messaging apps more securely](https://securityinabox.org/en/communication/secure-chat) to learn how to protect yourself when using chat tools for 1:1 and group communications.

## [Anchor](https://securityinabox.org/en/tools/signal/\#the-pros-and-cons-of-using-signal) The pros and cons of using Signal

We recommend Signal for 1:1 and group messaging and voice and video calls because:

- It is [free and open-source software](https://github.com/signalapp), so it's possible to submit its code to independent review.
- It protects your 1:1 and group messages and voice and video calls by default using [strong, modern and well-documented end-to-end encryption](https://github.com/signalapp/libsignal).
- It allows you to [verify the identity of your contacts](https://securityinabox.org/en/tools/signal/#verify-your-contacts-identities).
- It implements [forward secrecy](https://signal.org/blog/asynchronous-security/), so past conversations remain safe even if someone steals the encryption key used to protect a given message.
- It is asynchronous, so messages that were sent to you while you were offline will be waiting for you when you reconnect to the service.

However, it's important to bear the following in mind:

- Signal only encrypts messages that you exchange with other Signal users.
- While Signal prevents others from accessing the content of your messages and calls, it does not hide the fact that you are sending encrypted messages or making encrypted voice or video calls.
- In order to register with Signal, you must install the app in a phone (Android or iOS) and be willing and able to receive an SMS text message or a phone call from a number in the United States.
- Signal relies on Google’s Firebase Cloud Messaging and Apple Push Notification Service for push notifications. However, push notifications for Signal never contain sensitive unencrypted data and do not reveal the contents of any Signal messages or calls to anyone but you and the people you're talking to. In Signal, push notifications simply tell the app to wake up. They don't reveal who sent the message or who is calling. Notifications are processed entirely on your device, which is different from many other apps. If you're still worried about this feature, consider [using Molly as an alternative client](https://securityinabox.org/en/tools/signal/#consider-using-molly-as-an-alternative-client-for-signal).
- In some countries, encryption tools like Signal might attract attention or violate legal constraints. Consider whether encryption is illegal or suspicious in your jurisdiction. You can start this research by looking at the [Global Partners Digital World map of encryption laws and policies](https://www.gp-digital.org/world-map-of-encryption).
- [Certain countries](https://en.wikipedia.org/wiki/Signal_(software)#Blocking) completely block access to Signal. If Signal is blocked in your country, you can [use a proxy to get started with and continue using Signal](https://securityinabox.org/en/tools/signal/#use-a-proxy-if-signal-is-blocked-in-your-country).

## [Anchor](https://securityinabox.org/en/tools/signal/\#before-you-start-using-signal) Before you start using Signal

- Before you start using Signal, we recommend you make a communication plan based on the recommendations in our guide on [how to protect the privacy of your online communications](https://securityinabox.org/en/assess-plan/private-communication/) and read our general advice on [using messaging apps more securely](https://securityinabox.org/en/communication/secure-chat/).
- The security of your Signal account also depends on the security of your device. Review our recommendations to use your [Android](https://securityinabox.org/en/phones-and-computers/android) or [iOS](https://securityinabox.org/en/phones-and-computers/ios) device more securely.
  - Signal can also be linked to a desktop app. If you are planning to use this option, make sure your computer is secured by reviewing our guides on hot to use [Windows](https://securityinabox.org/en/phones-and-computers/windows), [Mac](https://securityinabox.org/en/phones-and-computers/mac) or [Linux](https://securityinabox.org/en/phones-and-computers/linux) more securely.

## [Anchor](https://securityinabox.org/en/tools/signal/\#install-signal) Install Signal

- Follow [the instructions in Signal's website to install Signal in your mobile device](https://support.signal.org/hc/en-us/articles/360008216551-Installing-Signal).
  - If you have an Android device and prefer not to use the Google Play Store, you can [download the Signal APK](https://signal.org/android/apk/) and use this file for the installation instead. Make sure to verify the certificate before installing Signal.
- Once you have installed Signal in your phone, you can connect it to a desktop app or to an iPad app.
  - Follow [the instructions in Signal's website to install the desktop app on Windows, macOS or Linux](https://support.signal.org/hc/en-us/articles/360008216551-Installing-Signal#install_desktop).

## [Anchor](https://securityinabox.org/en/tools/signal/\#use-a-proxy-if-signal-is-blocked-in-your-country) Use a proxy if Signal is blocked in your country

If Signal is [blocked in your country](https://en.wikipedia.org/wiki/Signal_(software)#Blocking), you can still create an account or continue using it by connecting through a proxy.

- [Learn how to find a proxy address](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#proxy_find).
- [Learn how to use a proxy on Signal for Android](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61MK3AQHE51VWFYGTC).
- [Learn how to use a proxy on Signal for iOS](https://support.signal.org/hc/en-us/articles/360056052052-Proxy-Support#h_01HDA8KS61PANY8JE6N8XXWQKM).
- If you are able to run a proxy server, follow [the instructions on how to set it up](https://github.com/signalapp/Signal-TLS-Proxy) to help make Signal's circumvention efforts as effective as possible.

## [Anchor](https://securityinabox.org/en/tools/signal/\#create-a-new-account) Create a new account

Learn how to register a new Signal account in [the support page on how to register a phone number](https://support.signal.org/hc/en-us/articles/360007318691-Register-a-phone-number).

### [Anchor](https://securityinabox.org/en/tools/signal/\#consider-registering-with-an-alternative-phone-number) Consider registering with an alternative phone number

- Find out [how to get a different phone number than the one you normally use](https://securityinabox.org/en/assess-plan/multiple-identities/#get-a-different-phone-number).
- Also [make sure your phone number is not visible in your profile](https://securityinabox.org/en/tools/signal/#keep-your-phone-number-private).

Learn why we recommend this

Your phone number may be connected to your official identity. You may not want to connect it to your messaging apps, especially if you would like to use this communication channel for sensitive activities that should not be traced back to your name and surname.

## [Anchor](https://securityinabox.org/en/tools/signal/\#protect-your-account) Protect your account

### [Anchor](https://securityinabox.org/en/tools/signal/\#set-a-registration-lock-pin-to-lock-your-phone-number) Set a registration lock PIN to lock your phone number

- To set a registration lock PIN, go to Settings > Account and turn on Registration Lock. You will be prompted to select a PIN. Make sure to store this PIN in a password manager as Signal cannot reset the PIN for you.
- Learn more on the registration lock in [the support page on the Signal PIN](https://support.signal.org/hc/en-us/articles/360007059792-Signal-PIN).

Learn why we recommend this

By setting a registration lock PIN, you'll stop others who do not know that PIN from registering a Signal account with your phone number.

## [Anchor](https://securityinabox.org/en/tools/signal/\#use-signal-more-safely) Use Signal more safely

This section contains recommendations on how to use Signal more safely. Also make sure to read [our guide on how to use messaging apps more securely](https://securityinabox.org/en/communication/secure-chat).

### [Anchor](https://securityinabox.org/en/tools/signal/\#keep-your-phone-number-private) Keep your phone number private

- To make sure your phone number is not visible in your profile, go to Settings > Privacy > Phone Number > Who can see my number and select Nobody.
  - Note that people who have your number saved in their phone contacts will still see your phone number, regardless of your settings, since they already know it.
- [Learn more on Signal's phone number privacy](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive).

Learn why we recommend this

By default, your phone number is not visible in your profile to people who don't already have it saved. You can change this setting to make it visible to everyone if you want to.

Since phone numbers are often connected to an official identity, we recommend keeping your phone number private, especially if you would like to use this communication channel for sensitive activities that should not be traced back to your name and surname.

### [Anchor](https://securityinabox.org/en/tools/signal/\#connect-with-others-without-sharing-your-phone-number) Connect with others without sharing your phone number

1. First create a username: go to Settings, tap your profile and enter your desired username.
   - Your username must be unique, and is formed by a name and at least 2 digits appended to the end. You can choose the numbers you see by default or change them.
   - [Learn more on Signal usernames](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive#usernames).
2. Go to Settings > Privacy > Phone Number > Who can find me by number and select Nobody. This will stop people from finding you by your phone number and will make sure that only people you've given your username to can connect with you on Signal.
   - [Learn more on Signal's phone number privacy and usernames](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive).

Learn why we recommend this

Your phone number may be connected to your official identity. You may not want to connect it to your messaging apps, especially if you would like to be found only by selected people or use this communication channel for sensitive activities that should not be traced back to your name and surname.

### [Anchor](https://securityinabox.org/en/tools/signal/\#back-up-your-messages) Back up your messages

Signal does not back up your chats by default, and only allows for your backups to be stored, in an encrypted form, on your mobile and on your computer if you have an Android device, and on your iPhone or iPad if you use iOS.

- [Learn how to back up and restore your Signal conversations](https://support.signal.org/hc/en-us/articles/360007059752-Backup-and-Restore-Messages).

### [Anchor](https://securityinabox.org/en/tools/signal/\#precautions-when-linking-devices) Precautions when linking devices

- [Learn how to link Signal Desktop or Signal iPad to your phone](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices).
- Consider that linking multiple devices will increase your attack surface, so try to reduce the number of linked devices to a minimum, ideally just one.
- Avoid linking your Signal account to shared devices (like on other people's devices or computers in public spaces).

### [Anchor](https://securityinabox.org/en/tools/signal/\#dont-share-contacts-and-call-history-with-ios) Don't share contacts and call history with iOS

- Go to Settings > Chats and disable Share Contacts with iOS and make sure this option is disabled to stop Signal from synchronizing your contacts with your phone app.
- Go to Settings > Privacy > Calling > Show Calls in Recents and make sure this option is disabled to stop Signal from synchronizing your call history with your phone app.

Learn why we recommend this

On iPhones and iPad, your call history may be synchronized with iCloud and your Signal contacts may be shared with iOS by default. To keep all your Signal activities and contacts restricted to the Signal app, make sure to disable the integrations described in this section.

### [Anchor](https://securityinabox.org/en/tools/signal/\#enable-incognito-keyboard-on-android) Enable Incognito Keyboard on Android

- Go to Settings > Privacy and enable the Incognito Keyboard option.
  - If you enable Incognito Keyboard, your keyboard may stop learning from the input you type and entries may not be remembered by your keyboard's dictionary to be used later for autocomplete or as a suggestion. This will decrease the risk of sharing the content you type with Google.
  - Note that if you enable this function, the autocorrect feature may not work.
  - It's important to consider that, depending on the device you use, this function may be ignored by your phone's keyboard and that Incognito Keyboard is by no means a protection against keyloggers and other spyware.
- [Read Signal's support page on Incognito Keyboard to learn more on this option](https://support.signal.org/hc/en-us/articles/360055276112-Incognito-Keyboard).

## [Anchor](https://securityinabox.org/en/tools/signal/\#secure-your-signal-communications) Secure your Signal communications

### [Anchor](https://securityinabox.org/en/tools/signal/\#verify-your-contacts-identities) Verify your contacts' identities

To confirm that you are exchanging encrypted messages with the right people, it's best to verify your contacts' safety number whenever possible. Once you have verified the safety number, mark your contact as verified by tapping the Mark as Verified or Clear Verification button.

- [Learn how to view a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#view).
- [Learn how to verify a safety number](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed#verify).

Learn why we recommend this

A Signal safety number is a long string of letters and numbers that uniquely identifies an account and its encryption key, allowing others to ensure that they are really communicating with the person they added as a contact. The identity verification described in this section helps you avoid impersonation attempts by third parties. If someone else tries to impersonate a contact you have verified, Signal will notice that the safety number has changed and you will see a safety number change alert.

### [Anchor](https://securityinabox.org/en/tools/signal/\#set-messages-to-automatically-disappear-or-delete-your-chat-history-regularly) Set messages to automatically disappear or delete your chat history regularly

- When sharing sensitive information, set messages in all conversations or in specific ones to disappear after a certain amount of time.
  - Consider how long you want messages to be visible before they expire. You can set messages to disappear after a custom time between few seconds and 4 weeks.
  - [Learn more about disappearing messages in Signal](https://support.signal.org/hc/en-us/articles/360007320771-Set-and-manage-disappearing-messages).
  - Disappearing messages do not guarantee that your messages will never be found! Someone could take a screenshot of the messages or take a photo of the screen using another camera. In any case, it's a good practice to also [disable screenshots of your messages](https://securityinabox.org/en/tools/signal/#enable-screen-security).
- If you haven't set automatic deletion for all your conversations, it's a good idea to regularly delete your chat history manually. Find the option in your app to [delete specific messages, single chats or all chats](https://support.signal.org/hc/en-us/articles/360007320491-Delete-messages-alerts-or-chats).

Learn why we recommend this

By default, chat apps keep a record of everything you and your contacts have written, said in voice messages or shared. Use the disappearing messages option to limit the amount of information Signal stores on your devices.

### [Anchor](https://securityinabox.org/en/tools/signal/\#enable-screen-security) Enable screen security

- To enable screen security, go to Settings > Privacy > Screen Security (Android) or Hide Screen in App Switcher (iOS).

Learn why we recommend this

Screen security blocks screenshots and also prevents previews of Signal messages from appearing in the app switcher on your phone.

Note that this feature won't stop message previews from appearing in your phone's notifications. To hide previews from message notifications, see instructions in our guides to secure your [Android](https://securityinabox.org/en/phones-and-computers/android/#control-what-can-be-seen-when-your-device-is-locked), [iOS](https://securityinabox.org/en/phones-and-computers/ios/#control-what-can-be-seen-when-your-device-is-locked), [Mac](https://securityinabox.org/en/phones-and-computers/mac/#control-what-can-be-seen-when-your-device-is-locked), [Linux](https://securityinabox.org/en/phones-and-computers/linux/#control-what-can-be-seen-when-your-device-is-locked) or [Windows](https://securityinabox.org/en/phones-and-computers/windows/#control-what-can-be-seen-when-your-device-is-locked) device.

### [Anchor](https://securityinabox.org/en/tools/signal/\#protect-your-ip-address-on-signal-calls) Protect your IP address on Signal calls

- Go to Settings > Privacy > Advanced and check the Always relay calls option.
  - If you activate this feature, you might find the call quality is reduced.
  - Note that this feature only protects your IP address during calls, not for other Signal activities like messaging or file sharing – by [using a VPN](https://securityinabox.org/en/internet-connection/circumvention/#choose-a-vpn-service) or [Tor](https://securityinabox.org/en/internet-connection/anonymity/#anonymize-all-your-connections), you can get a better protection against attempts at revealing your identity for everything you do online.

Learn why we recommend this

Apps that allow for 1:1 voice and video calls establish a direct connection between participants' devices to achieve a better call quality. This means that devices used for 1:1 voice and video calls need to exchange their IP addresses so that the call data can be delivered. But your IP address may reveal information like your broad geographical location or internet provider.

By always relaying calls, all your 1:1 calls will be relayed through Signal's servers, so the person you are talking to cannot see your IP address.

Note that your calls are end-to-end encrypted, so Signal cannot listen to them even if they go through Signal's servers. Also, all group calls go through Signal's servers, so your IP address is always protected when you talk to more than one person.

### [Anchor](https://securityinabox.org/en/tools/signal/\#disable-link-previews) Disable link previews

- Go to Settings > Chats and make sure Generate link previews is disabled.
- [Learn more on Signal Link Previews](https://support.signal.org/hc/en-us/articles/360022474332-Link-Previews).

Learn why we recommend this

If you keep link previews enabled, websites that link in your messages can obtain some information about you and your conversation. Note that this only applies to links you include in messages - other people sending links need to disable previews as well if they want to avoid sending information to the linked websites.

## [Anchor](https://securityinabox.org/en/tools/signal/\#protect-your-groups) Protect your groups

On Signal, you can create groups of up to 1000 members and organize group voice or video calls with up to 50 participants.

This section includes recommendations on how to secure your Signal groups.

- [Read more on Signal groups and how to start a group chat](https://support.signal.org/hc/en-us/articles/360007319331-Group-chats).
- [Read more on group voice and video calls](https://support.signal.org/hc/en-us/articles/360052977792-Group-Calling-Voice-or-Video).
- Also read [our tips on using group chats more safely in the guide on messaging apps](https://securityinabox.org/en/communication/secure-chat/#use-group-chats-more-safely).

### [Anchor](https://securityinabox.org/en/tools/signal/\#invite-only-people-you-know-and-trust) Invite only people you know and trust

- When creating a group, enable the option to control who can join your group, called Approve new members in Android or Require admin approval in iOS.
- [Learn how to add members to a group chat](https://support.signal.org/hc/en-us/articles/360050427692-Manage-a-group#add).
  - If you decide to create a shareable invite link, consider whether sharing the link publicly is too risky.
- To have a more fine-grained control on who joins your group, consider changing the default group permissions so only admins can add new members.

Learn why we recommend this

Group chats can be targeted by trolls who want to disrupt conversations or may be joined by someone who wants to surveil their members' activities. To reduce this risk, be careful not to share the invite link publicly. If your group deals with sensitive topics and is particularly at risk, make sure to only allow admins to add new members to the group.

When setting up a group also consider: what are members communicating about themselves by joining this group? For example, if it is an LGBTQI support group, will that affiliation bring dangers for members in your region? Consider the impact of visibility in your current moment. There may be times when it is valuable for your movement to be visible, and even at that moment people who want your support might need a way to connect with your group without being identified. Think strategically about the platforms where you create your groups, what you name them (would a coded name help, as it did the Mattachine Society or the Daughters of Bilitis gay and lesbian organizations in the 1950s?), and whether they are public or private.

### [Anchor](https://securityinabox.org/en/tools/signal/\#select-a-few-trusted-admins) Select a few trusted admins

- To give someone admin rights, go to the group members list, tap the name of the person you want to give admin rights to and then click Make admin.

Learn why we recommend this

When managing a group, especially a large one, moderating conversations and enforcing your community's guidelines can be particularly overwhelming. By giving admin rights to a few people you trust, you can create a more collaborative environment, reducing your stress level and ensuring a smoother communication within the group. Also, if a group is managed by more than one admin, you can rely on other people in case your account is blocked or you are unable to moderate or manage the group for other reasons.

### [Anchor](https://securityinabox.org/en/tools/signal/\#assign-some-privileges-only-to-admins) Assign some privileges only to admins

- In the Permissions section of every group, you can choose to restrict to admins only the permissions to add members, edit group info and send messages.
  - Make sure only admins can edit the group info, so unauthorized members cannot change the group's name, description and picture.

### [Anchor](https://securityinabox.org/en/tools/signal/\#moderate-the-conversation) Moderate the conversation

- Decide who can write to the group: if the main goal of your group is to share updates with many people, it is a good idea to only allow admins to send messages.
- If a member is violating your group's community standards, you can remove them by tapping their name and then Remove from group.

### [Anchor](https://securityinabox.org/en/tools/signal/\#set-messages-to-disappear) Set messages to disappear

- Set messages in your groups, or at least in the most sensitive ones, to disappear after a certain amount of time.
  - [Learn more about disappearing messages in Signal](https://support.signal.org/hc/en-us/articles/360007320771-Set-and-manage-disappearing-messages).

## [Anchor](https://securityinabox.org/en/tools/signal/\#check-suspicious-access) Check suspicious access

### [Anchor](https://securityinabox.org/en/tools/signal/\#check-your-linked-devices) Check your linked devices

- [Learn how to view the devices linked to your Signal account](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01JPNF3R6PAJQSQEFGVMMZ75TA).
- [Learn how to unlink any device you don't recognize](https://support.signal.org/hc/en-us/articles/360007320551-Linked-Devices#h_01K0YRHGSACMHVM8JYNSPNX157).
  - _Note that if you are using a VPN or Tor, which can conceal your location, your own device may appear as connecting from unexpected locations_.

Learn why we recommend this

Your adversaries may find ways to log in to your account from their devices. If they do so, it is possible you will be able to see this from the Linked devices section of your Signal app.

### [Anchor](https://securityinabox.org/en/tools/signal/\#if-your-device-is-lost-or-stolen) If your device is lost or stolen

- [Read Signal's support page on what to do if your phone is lost or stolen](https://support.signal.org/hc/en-us/articles/360007062452-What-do-I-do-if-my-phone-is-lost-or-stolen).

## [Anchor](https://securityinabox.org/en/tools/signal/\#consider-using-molly-as-an-alternative-client-for-signal) Consider using Molly as an alternative client for Signal

If you have an Android device, consider using [Molly](https://molly.im/) (or Molly-FOSS) if you would like to have additional features like:

- adding a layer of protection to your messaging app by encrypting your stored messages with a passphrase,
- having the same Signal account on multiple mobile devices,
- choosing how often you back up your conversations and how many backups you keep every time,
- relying on a system independent from Google for your phone to be notified about new messages (only possible on Molly-FOSS).

Learn why we recommend this

Molly is a secure, free and open-source messaging client with all the features of Signal, alongside some additional functionalities and security improvements.

- [Check out the full list of features that Molly adds to the Signal app in Molly's Github repository](https://github.com/mollyim/mollyim-android?tab=readme-ov-file#features).
- Watch [Techlore's video on Molly](https://www.youtube.com/watch?v=P-2z2c3XBkQ) (on YouTube) for more details on the differences between Molly and Signal and on who should consider using this app.

## [Anchor](https://securityinabox.org/en/tools/signal/\#resources) Resources

- [EFF Surveillance Self-Defense, How to: Use Signal](https://ssd.eff.org/module/how-to-use-signal) — _Last updated: March 26, 2025_
- [Techlore, Lock Down Signal Messenger: Ultimate Hardening Guide](https://www.youtube.com/watch?v=DPjg3651oJM) (YouTube video) — _Published: August 9, 2024_