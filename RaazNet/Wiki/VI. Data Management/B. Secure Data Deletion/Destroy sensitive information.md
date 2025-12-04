\_\_('Table of Contents')

Files › Destroy sensitive information

# [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#destroy-sensitive-information) Destroy sensitive information

Updated 25 March 2024

## [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#table-of-contents) Table of Contents

- [Clean traces of your work off your device](https://securityinabox.org/en/files/destroy-sensitive-information/#clean-traces-of-your-work-off-your-device)
- [Wipe a whole device](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device)
- [Before you sell, give away or dispose of an old computer or phone](https://securityinabox.org/en/files/destroy-sensitive-information/#before-you-sell-give-away-or-dispose-of-an-old-computer-or-phone)

A phone or computer uses its memory like someone who works very hard to save paper: it writes in pencil, and piles up the files you tell it to delete (like temporary files or the files you remove from your device's Trash, or Recycle Bin). When it needs more space, it erases writing from paper in the "deleted" pile, and writes on that part of the paper again to add new files.

So when you drag a file to the Trash and then empty the dustbin, your phone or computer does not really delete that file. What happens is more like removing labels from a filing cabinet, but leaving the documents in it. When you "delete" a file you are only telling your phone or computer that it can use the space where the deleted file was saved for something else. Until your device saves another file in that space, the original file can still be seen by someone who has access to your device, and the right tools.

The tools we recommend in this chapter do more than just delete the file by erasing the words. They scribble over the top of every word with random nonsense several times so no trace of the original file is left behind. Security experts agree that "wiping" your phone's or computer's unused space in this way is effective enough to keep an intruder from reading your erased files.

**There is a big exception to this. In all phones, in newer computers and in external storage devices, there is a risk that solid-state drives, or SSDs, as well as USB sticks and SD cards will not fully erase their contents because of a technique called "wear leveling."** Learn more about the challenges of erasing SSDs in [the Surveillance Self-Defense guide on deleting data securely](https://ssd.eff.org/en/module/how-delete-your-data-securely-macos#SSDs). To make it harder to recover what you have erased from an SSD drive it is crucial to [encrypt these drives](https://securityinabox.org/en/files/secure-file-storage#consider-encrypting-your-external-storage-devices) as soon as possible, particularly if you are going to dispose of them. It is also important to encrypt drives before you re-use them.

Secure deletion tools will not erase files you have not deleted or specifically decided to wipe. Still, be careful with software like this. If it is your first time using these tools, carefully follow the steps detailed in this chapter in order to erase files safely and effectively. There are a few ways to wipe sensitive data from your devices. You can wipe the contents of your trash, the "empty" space on the drive, or the entire drive.

## [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#clean-traces-of-your-work-off-your-device) Clean traces of your work off your device

Set a regular schedule to wipe your device's unused memory securely. This will ensure that sensitive files do not remain on your devices, hard drives, USB sticks, removable memory cards (SD cards) from cameras, mobile phones or portable music players, and any other device where you store sensitive information.

**Android**

- Use [CCleaner for Android](https://www.ccleaner.com/ccleaner-android) to remove temporary and hidden files, like application cache, browser history, clipboard content and old call logs.

To run CCleaner for Android for the first time, see [their guide](https://support.ccleaner.com/s/article/running-ccleaner-for-android-for-the-first-time).

- After deleting temporary and hidden files with CCleaner for Android, use [Extirpater](https://f-droid.org/packages/us.spotco.extirpater/) to wipe free space in your device.

Note that Extirpater is not available in the Google Play store. [Install F-Droid's APK](https://f-droid.org/) first and install Extirpater through it. Use this app with care as it can permanently damage the memory of your device if you run it too often.


**iOS**

- Use [CCleaner for iOS](https://www.ccleaner.com/ccleaner-ios) to remove temporary and hidden files.

**Linux and Windows**

- Use [BleachBit](https://www.bleachbit.org/) to remove temporary and hidden files. See [their guide](https://docs.bleachbit.org/).

**macOS**

- Include the ["Custom files and folders" option](https://support.ccleaner.com/s/article/how-do-i-include-custom-files-for-cleaning) in [CCleaner for Mac](https://www.ccleaner.com/ccleaner-mac) to remove temporary and hidden files.

Learn why we recommend this

We recommend cleaning traces of your work to remove the history of your activity on a device, combat malware and help your device work better. These files are hard to find and remove safely. In the next few paragraphs, we will tell you more about these files.

Your web browser saves text, images, cookies, account information, the history of websites you have visited and personal data used to complete online forms. Our [guide on secure browsing](https://securityinabox.org/en/internet-connection/safer-browsing/) can tell you more about this data and how to delete it more often.

Your device and the apps on it also save temporary versions of files you are working on. This way, if a computer or phone crashes or there is a power outage, you don't lose all the work you have done. If you wipe the file you were working on, you remove the current version, but your device continues to store older temporary files in ways that are hard to find and remove without special tools. Apps and devices also save all sorts of other shortcuts to make our lives easier, including what you copy to the clipboard.

## [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#wipe-a-whole-device) Wipe a whole device

Before you proceed to wiping an entire device, create an encrypted backup of your important files, as discussed in our guide [Backup and recover from information loss](https://securityinabox.org/en/files/backup).

When you are sure you have backed up all important data, you can follow the instructions in this section.

### [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#all-devices) All devices

- Close down all apps you are not using.
- Disconnect from the internet, turning off wifi or unplugging the cable as needed.
- You may want to start by [clearing your browser's temporary files](https://securityinabox.org/en/internet-connection/safer-browsing/#delete-your-browsing-history).

### [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#mobile-devices) Mobile devices

- If possible, ensure [full-disk encryption is turned on](https://securityinabox.org/en/files/secure-file-storage#consider-encrypting-your-whole-device) before wiping your device.

#### Android

- To wipe the flash memory of your phone, [reset your device to factory settings](https://support.google.com/android/answer/6088915).

#### iOS

- Learn how to securely wipe your device in [the instructions on what to do before you sell, give away, or trade in your iPhone or iPad](https://support.apple.com/HT201351).

### [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#computers) Computers

- It is not possible for a device to thoroughly erase itself. You will need to start your computer from an external drive to do this.
  - One option is to physically remove the hard drive from your computer, treat it as an external drive, and erase it using another computer.
    - For instructions on how to remove your drive, [search for "remove hard drive" and the brand and model of your computer on iFixit](https://www.ifixit.com/Search?query=remove+hard+drive).
    - Put the drive you removed into an external USB "drive enclosure."
- If you need to wipe an HDD hard drive, consider using [ShredOS](https://github.com/PartialVolume/shredos.x86_64). This may take some time, and you will need to download ShredOS, write it to an empty USB stick and then run it from the USB device.
  - Note that while ShredOS can be used to wipe SSDs, these drives work in a way that makes it impossible for this tool to reliably wipe them completely. This is why it's always best to [fully encrypt](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-your-whole-device) SSDs with a strong password in order to make them impossible to read for anyone who doesn't have the decryption password.
- Once you have wiped the entire disk, be sure to set up full-disk encryption when reinstalling the operating system.
- Unfortunately, on newer computers that use an SSD, it is harder to guarantee that a drive is fully erased. However, you can take the steps described for each operating system in the following sections.
  - Encrypting your entire SSD with a strong password will also make the data impossible to read without your permission.

#### macOS

- To erase your macOS computer and reset it to factory settings, follow the steps in the [official documentation](https://support.apple.com/en-us/102664).
- On macOS computers with SSD drives, secure erase options are not available in Disk Utility. To protect the data stored in your SSD, [enable full-disk encryption](https://support.apple.com/HT204837) on the drive you want to erase. This ensures the contents of your hard drive look like random nonsense to anyone who does not have your device password.
- On older Mac computers that have Intel chips, you can erase your hard drive securely using [Disk Utility](https://support.apple.com/en-us/102639) or [Erase Assistant](https://support.apple.com/guide/mac-help/mchl7676b710/mac).

#### Windows

1. Extract the internal disk of your computer. For instructions on how to do this, [search for "remove hard drive" and the brand and model of your computer on iFixit](https://www.ifixit.com/Search?query=remove+hard+drive).
2. Put the drive you removed into an external USB "drive enclosure."
3. Plug the hard disk you want to erase into a computer with [Eraser](https://securityinabox.org/en/files/tools#eraser) installed.
4. Delete everything on the drive you have extracted.
5. Then use Eraser to wipe all of the drive's unallocated space. You might need to let this procedure run overnight, as it can be quite slow.

Learn why we recommend this

When you wipe an entire hard drive, you will need to run your computer's operating system off a different drive because a program like Eraser cannot thoroughly erase the device that is running it. This will require physically removing from your computer the drive you want to erase and essentially turning it into an external hard drive.

## [Anchor](https://securityinabox.org/en/files/destroy-sensitive-information/\#before-you-sell-give-away-or-dispose-of-an-old-computer-or-phone) Before you sell, give away or dispose of an old computer or phone

- If possible, when you are selling or giving away an old computer, do not give the new owner the hard drive; but if you must, be sure you have fully wiped it using the instructions in [Wipe a whole device](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device).
- If you are selling, giving away or disposing of a mobile device or an external storage device, wipe it fully using the instructions in [Wipe a whole device](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device).
- Remove USB drives, SD cards, SIM cards, dongles and other small devices that may be inserted or plugged into your device.
- If you are disposing of an old hard drive, consider destroying it physically as well as [wiping it](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device). You can do this by hammering nails through the drive, or with a drill. Do not burn or pour acid on a drive, and do not put it in the microwave. Physically destroying data storage is always the safest option.
- You can also keep a wiped drive that is in good condition to re-use it yourself, in a new device or as an external hard drive.
- Use the following instructions as an additional checklist when taking the steps we have listed in the section on [securely erasing your device](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device).

**Android**

- Follow the instructions in our guide on [securing the Google accounts connected with your device](https://securityinabox.org/en/phones-and-computers/android/#secure-the-google-accounts-connected-with-your-device) to remove this device from the list of devices associated with your Google accounts.
  - Follow the instructions for [wiping a whole device](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device).

**iOS**

- Follow the instructions in our guide on [securing the accounts connected with your device](https://securityinabox.org/en/phones-and-computers/ios#secure-the-accounts-connected-with-your-device) to remove this device from the list of devices associated with your online accounts.
- Follow the instructions in the official Apple documentation on [What to do before you sell, give away, or trade in your iPhone or iPad](https://support.apple.com/HT201351) to securely prepare your phone for disposal, including instructions for fully wiping a device securely.

**Linux**

- Follow the links in [removing unneeded accounts associated with your device](https://securityinabox.org/en/phones-and-computers/linux#remove-unneeded-accounts-associated-with-your-device) to remove this device from the list of devices associated with your online accounts.
  - Follow the instructions for [wiping a whole device](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device).

**macOS**

- Follow the instructions in our guide on [securing the accounts connected with your device](https://securityinabox.org/en/phones-and-computers/mac#secure-the-accounts-connected-with-your-device) to remove this device from the list of devices associated with your online accounts.
- Follow the instructions in the official Apple documentation on [What to do before you sell, give away, trade in, or recycle your Mac](https://support.apple.com/HT201065) to securely prepare your computer for disposal, including the instructions for fully wiping a device securely.

**Windows**

- Follow the instructions in our guide on [securing the accounts connected with your device](https://securityinabox.org/en/phones-and-computers/windows/#secure-the-accounts-connected-with-your-device) to remove this device from the list of devices associated with your online accounts.
- Follow the instructions in the official Microsoft documentation on [what to do before you sell or gift your Xbox or Windows pc](https://support.microsoft.com/account-billing/before-you-sell-or-gift-your-windows-10-device-or-xbox-one-78ee8071-c8ab-40c4-1d89-f708582062e4) to securely prepare your computer for disposal.
- Follow the instructions for [wiping a whole device](https://securityinabox.org/en/files/destroy-sensitive-information/#wipe-a-whole-device).

Learn why we recommend this

The process of wiping a drive may take quite some time. When you are giving a computer to someone else, it may be difficult to negotiate not giving them the hard drive. But when you are selling or otherwise disposing of a device, it is worth taking these precautions to ensure you are not accidentally giving away your sensitive files to someone else.