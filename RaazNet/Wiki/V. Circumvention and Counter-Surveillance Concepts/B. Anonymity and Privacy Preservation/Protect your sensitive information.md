\_\_('Table of Contents')

Files › Protect your sensitive information

# [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#protect-your-sensitive-information) Protect your sensitive information

Updated 13 March 2024

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#table-of-contents) Table of Contents

- [Consider deleting old data instead of storing it](https://securityinabox.org/en/files/secure-file-storage/#consider-deleting-old-data-instead-of-storing-it)
- [Consider whether encryption is illegal or suspicious in your jurisdiction](https://securityinabox.org/en/files/secure-file-storage/#consider-whether-encryption-is-illegal-or-suspicious-in-your-jurisdiction)
- [If encryption is illegal in your country, consider the following alternatives](https://securityinabox.org/en/files/secure-file-storage/#if-encryption-is-illegal-in-your-country-consider-the-following-alternatives)
- [Consider encrypting your whole device](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-your-whole-device)
- [Consider encrypting your external storage devices](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-your-external-storage-devices)
- [Consider encrypting just some sensitive files](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-just-some-sensitive-files)
- [Protect your encrypted folder or volume](https://securityinabox.org/en/files/secure-file-storage/#protect-your-encrypted-folder-or-volume)
- [Use trusted dealers and repair shops](https://securityinabox.org/en/files/secure-file-storage/#use-trusted-dealers-and-repair-shops)

Intruders may be able to read or modify your data if they manage to get hold of your device. It is always best to have several layers of defence against this possibility. Encrypting your entire devices as well as individual files is one important form of protection.

Encryption is a way for software to scramble your information using advanced mathematics, leaving you and only you with the key to unscramble it (in the form of a password, passphrase, or encryption key). So encrypting your device is like keeping your information in a locked safe with a combination that only you know.

Take the following steps to protect data stored on your devices.

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#consider-deleting-old-data-instead-of-storing-it) Consider deleting old data instead of storing it

Learn why we recommend this

Storing confidential data can be a risk for you and for the people you work with. Encryption reduces this risk but does not eliminate it. The first step to protecting sensitive information is to reduce how much of it you keep around. Unless you have a good reason to store a particular file, or a particular category of information within a file, you should simply delete it (see [How to destroy sensitive information](https://securityinabox.org/en/files/destroy-sensitive-information) to learn how to do this securely).

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#consider-whether-encryption-is-illegal-or-suspicious-in-your-jurisdiction) Consider whether encryption is illegal or suspicious in your jurisdiction

Learn why we recommend this

Encryption is illegal in some countries. If it is illegal in your country, downloading, installing or using encryption software might be considered a crime. Police, military, or intelligence services might take your use of encryption software as a pretext to investigate your activities or persecute your organization. Regardless of what is actually inside your encrypted volumes, and regardless of whether or not this information is legal in your area, the usage of encryption might cast suspicion on you.

So investigate how law enforcement has treated encryption in your country, and think carefully about whether tools whose sole purpose is encrypting your data are appropriate for your situation.

You can start researching the legal status of encryption in your country in the [Global Partners Digital World map of encryption laws and policies](https://www.gp-digital.org/world-map-of-encryption).

If encryption is not illegal in your country or in the countries you're travelling to, you can skip directly to [Consider encrypting your whole device](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-your-whole-device).

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#if-encryption-is-illegal-in-your-country-consider-the-following-alternatives) If encryption is illegal in your country, consider the following alternatives

### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#store-only-non-sensitive-information) Store only non-sensitive information

- See [Consider deleting old data instead of storing it](https://securityinabox.org/en/files/secure-file-storage/#consider-deleting-old-data-instead-of-storing-it) to learn why it's a good idea to delete data that you don't need.
- See [Destroy sensitive information](https://securityinabox.org/en/files/destroy-sensitive-information) to learn how to do this securely.

### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#store-to-an-encrypted-cloud-account) Store to an encrypted cloud account

- Consider whether making use of an encrypted cloud service would be wise given the threats you face. While these services protect your data using encryption, and store your data on servers that might be harder for your adversary to get to, if your adversaries do have access to those servers, they will have more time to try to break into your data, and may be able to do it without you detecting the break in.

### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#use-a-system-of-code-words) Use a system of code words

- Store your files normally, but use code words to label sensitive names, locations, activities, etc.

### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#store-to-an-encrypted-removable-drive) Store to an encrypted removable drive

- You can keep sensitive information off of your computer by storing it on an encrypted USB memory stick or portable hard drive. To learn how to encrypt your entire storage device, see [Consider encrypting your external storage devices](https://securityinabox.org/en/files/secure-file-storage/#consider-encrypting-your-external-storage-devices) below.

- Be aware that external devices are typically even more vulnerable than computers to loss and confiscation, so carrying around sensitive information on them can be risky. When encrypting them, make sure to use a strong password that is harder to guess or crack. See [Create and maintain strong passwords](https://securityinabox.org/en/passwords/passwords) to learn how to create a strong password.


## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#consider-encrypting-your-whole-device) Consider encrypting your whole device

- Be aware that full-disk encryption (FDE) only works fully if your device is powered all the way off, not in the sleep mode (also known as "suspend" or "hibernate"). If your device is not switched off, someone who has physical access to it may be able to read or modify your files and communications.

**Android**

- Most devices with Android 10 and higher are required to use file-based encryption, which means that any device running on Android 10 or higher should be encrypted by default.

If you would like to make sure that file-based encryption is indeed enabled in your device, navigate to **Settings** \> **Security** \> **Encryption & credentials** and look for **Encryption** or **Encrypt phone**. Please note that these options may differ on your device.


**iOS**

- iOS devices are encrypted by default when you [set a passcode to access them](https://support.apple.com/en-us/HT204060).

**Linux**

- You can only activate full-disk encryption when you are installing Linux, so you will need to re-install if FDE is not enabled in your computer. Before you do so:

  - [Back up all your data](https://securityinabox.org/en/files/backup). The installation process will replace all data stored on your previous operating system.
  - Plug your computer into a power source so that it does not switch off during the installation process.
  - Stay connected to the internet through a cable so that you can get the latest updates while you install Linux. If you are not connected to the internet through a cable you will be asked to select a wireless network, if available.
- To install Ubuntu, read the [installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop) in Ubuntu's official documentation.

- For the installation you will also need to create a bootable USB stick.

  - See Ubuntu's guide for the device you are using to create the bootable USB stick:
    - [Create a bootable USB stick on Windows](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows)
    - [Create a bootable USB stick on macOS](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos)
    - [Create a bootable USB stick on Ubuntu](https://www.ubuntu.com/download/desktop/create-a-usb-stick-on-ubuntu)

**macOS**

- [Turn FileVault on to encrypt the disk of your computer](https://support.apple.com/en-us/HT204837).

**Windows**

You can encrypt your entire Windows computer using BitLocker, the built-in device encryption system available on devices running Windows 10 or 11 Pro, Enterprise, or Education.

- To encrypt your Windows computer using BitLocker, see [the official Windows documentation](https://support.microsoft.com/en-us/windows/device-encryption-in-windows-ad5dcf4b-dbe0-2331-228f-7925c2a3012d)
  - For additional security, [enable a pre-boot PIN](https://www.howtogeek.com/262720/how-to-enable-a-pre-boot-bitlocker-pin-on-windows/).
- [Encrypt older devices](https://support.microsoft.com/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838)
  - If you encounter an error message saying "This device can't use a Trusted Platform Module," this means that your computer does not have a Trusted Platform Module (TPM) chip that is used for encryption. However, with the following configuration adjustments, BitLocker can still be used on computers without a TPM chip:
    1. Press Start. Type gpedit.msc and press Enter. In the new window, double-click **Operating System Drives**.
    2. In the right-hand panel of this window, double-click **Require additional authentication at startup**, which opens a new window. (Note: there is also a "Require additional authentication at startup (Windows Server 2008 and Windows Vista)" option; that is _NOT_ the one you want.)
    3. Select **Enabled**. Ensure that **Allow BitLocker without a compatible TPM (Requires a password or a startup key on a USB flash drive)** is enabled. Click OK.
    4. Close the Local Group Policy Editor window.
    5. At the end of this procedure you can [turn on device encryption](https://support.microsoft.com/windows/turn-on-device-encryption-0c453637-bc88-5f74-5105-741561aae838).

Learn why we recommend this

If your device is lost, stolen, or seized by people who want to access your files and communications, you will need protection to stop them. Encrypting your whole device with a strong password or code offers this kind of protection.

If your computer does not support full-disk encryption or if you prefer to use a free and open-source tool to enable disk encryption, you can use [VeraCrypt](https://veracrypt.io/) to [encrypt your whole device](https://veracrypt.io/en/System%20Encryption.html).

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#consider-encrypting-your-external-storage-devices) Consider encrypting your external storage devices

- Storing sensitive information in an encrypted storage device like a USB stick or portable hard drive may protect your most important data from adversaries who search your computer.
- Be aware that external devices are usually even more vulnerable than computers to loss and confiscation, so make sure to encrypt them with a strong password that is harder to guess or crack. See [Create and maintain strong passwords](https://securityinabox.org/en/passwords/passwords) to learn how to create a strong password.
- On desktops and laptops, your device may have built-in encryption options for external storage devices. Alternatively, you can use [VeraCrypt](https://veracrypt.io/) to encrypt external storage devices.

**Linux, macOS and Windows**

Whatever OS you run in your computer, you can use VeraCrypt to protect sensitive files in an external storage device. You can either create an encrypted volume within your external device or encrypt the entire storage device.

- [Download VeraCrypt](https://veracrypt.io/en/Downloads.html)
- [How to use VeraCrypt](https://veracrypt.io/en/Beginner%27s%20Tutorial.html)
- To learn how to encrypt an entire external storage device with VeraCrypt, see [Lifewire's post on how to encrypt a flash drive](https://www.lifewire.com/how-to-encrypt-a-flash-drive-4628341)
- Consider using VeraCrypt in [portable mode](https://veracrypt.io/en/Portable%20Mode.html) so anyone who searches your computer can't see you're using VeraCrypt in the first place.

**macOS**

On macOS, you can use the built-in Disk Utility to encrypt your external storage devices. Be aware that if you choose this solution you will only be able to access your encrypted devices on macOS systems.

- Learn how to [Encrypt and protect a storage device with a password in Disk Utility](https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac).

**Windows**

On Windows, you can use the built-in Bitlocker - available on Windows 10 and Windows 11 Pro, Enterprise or Education - to encrypt your external storage devices. Be aware that if you choose this solution you will only be able to access your encrypted devices on Windows systems.

- Learn [how to encrypt an external storage device with Bitlocker](https://www.microsoft.com/en-us/microsoft-365-life-hacks/privacy-and-safety/how-and-why-to-encrypt-usb-flash-drive).

**Tails**

Tails is an operating system that runs off a USB drive plugged into your machine. It protects all of your internet connections by using Tor at all times and erases your history when you shut it down, leaving no traces either in your computer or in the USB where the system is running. Furthermore, you can optionally create an encrypted volume inside the USB stick to store sensitive information that cannot be accessed by intruders who get access to your Tails stick in case you lose it or it is confiscated.

- Learn more about [Tails](https://tails.net/about/index.en.html).
- Learn about the [Tails persistent storage](https://tails.net/doc/persistent_storage/index.en.html).

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#consider-encrypting-just-some-sensitive-files) Consider encrypting just some sensitive files

On desktops and laptops, your device may have built-in encryption options that offer additional protection for specific files. Alternatively, you can use [Cryptomator](https://cryptomator.org/) to activate this additional layer of protection on any operating system, including mobile devices. Another option to encrypt your sensitive data on computers is [VeraCrypt](https://veracrypt.io/), which also makes it possible to [hide your encrypted folder](https://securityinabox.org/en/files/secure-file-storage/#consider-whether-to-store-your-files-in-a-hidden-volume).

Learn why we recommend this

You might find it useful to leave non-sensitive files on your device un-encrypted, so that if your device is searched it does not look suspicious because it contains ordinary, everyday files and communications. In this case, you can encrypt just some of your files.

**Windows, macOS, Linux, Android, iOS**

Whether you need to encrypt files in a computer or in a mobile device, you can use [Cryptomator](https://cryptomator.org/), a free and open-source application that was created specifically to protect the files you keep on online file storage platforms but can also be used to encrypt files you save in your device.

To learn how to use Cryptomator, see [their documentation](https://docs.cryptomator.org/en/latest/), especially the [Getting Started guide for computers](https://docs.cryptomator.org/en/latest/desktop/getting-started/).

**Windows**

- [How to encrypt a file in Windows 10](https://support.microsoft.com/en-us/windows/how-to-encrypt-a-file-1131805c-47b8-2e3e-a705-807e13c10da7)
- [How to encrypt a file in Windows 11](https://www.microsoft.com/en-us/windows/learning-center/how-to-encrypt-file)

**macOS**

- On macOS computers you can protect individual files by storing them in [a secure disk image created through the built-in Disk Utility](https://support.apple.com/et-ee/guide/disk-utility/dskutl11888/mac#dsku7bb3d28c).

**Linux, macOS and Windows**

- With VeraCrypt, you can protect individual files by storing them within an encrypted file container.

- [Download VeraCrypt](https://veracrypt.io/en/Downloads.html)

- [How to use VeraCrypt](https://veracrypt.io/en/Beginner's%20Tutorial.html)


### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#consider-whether-to-store-your-files-in-a-hidden-volume) Consider whether to store your files in a hidden volume

Learn why we recommend this

When you encrypt your information, nobody else may be able to read it, but someone might still be able to see that the encrypted data is there, and that you have taken steps to protect it. That adversary might then try to intimidate, blackmail, interrogate, or torture you to get you to unlock that encryption.

[VeraCrypt](https://veracrypt.io/) gives you the opportunity to avoid this risk by [creating a "hidden volume."](https://veracrypt.io/en/Hidden%20Volume.html) To open a hidden volume, you just need to enter a different password from the one you set for the standard volume. So if an intruder becomes suspicious about your encrypted files, they will be unable to prove hidden ones exist.

VeraCrypt disguises your encrypted information as other, less sensitive, hidden data (like music files or ordinary documents), so it does not look unusual. It is generally considered impossible to tell from analysis whether or not an encrypted volume contains a hidden volume. So if an intruder takes you to court or intimidates you into giving up your password, you can give them the passphrase for your standard volume and they will find convincing "decoy" material, but not the information you are protecting.

A hidden volume is like a "false bottom" in a locked safe: only you know that your safe has a secret compartment. This allows you to deny that you are keeping any secrets beyond what you already gave your adversary, and might help protect you in situations where you must reveal a password. So a hidden volume gives you a chance to escape a potentially dangerous situation. Remember, however, that this is less useful if using encryption is illegal in your country or if the fact that you are using it can raise suspicion.

Be warned that your adversary might know that VeraCrypt can hide information in this way; there is no guarantee they will give up if you reveal your decoy password, even if plenty of people use VeraCrypt without hidden volumes.

You must also make sure you do not accidentally reveal your hidden volume by leaving it open or allowing other applications to create shortcuts to the files it contains.

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#protect-your-encrypted-folder-or-volume) Protect your encrypted folder or volume

### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#unmount-and-disconnect-the-encrypted-folder-or-volume) Unmount and disconnect the encrypted folder or volume

- When your encrypted folder or volume is mounted - in other words, whenever you can access the contents yourself - your data may be vulnerable. Keep it unmounted when you are not actively reading or modifying the files inside it.
- If you keep an encrypted volume or folder on a USB stick or external hard drive, remember that just disconnecting the external storage device may not immediately make the volume disappear from the system. Simply disconnecting may corrupt the file on the external drive. You need to unmount the volume or folder first, then eject the drive from your operating system before you can physically disconnect the device from your computer. Note that to unmount a volume all accessed files need to be closed. So if you are editing a document or looking at a photo, you need to close those files or quit the programs before you can unmount. Practice this workflow until you can do it easily, so you will be ready in case of emergency.

Make sure to unmount and disconnect the encrypted folder or volume in all the following cases:

- Before you walk away from your device for any length of time. This ensures you do not leave your sensitive files accessible to physical or remote intruders while you are gone.
- Before you put your computer to sleep (also known as "suspend" or "hibernate"), either by selecting that option or by closing a laptop.
- Before allowing someone else to handle your computer. When taking a laptop through a security checkpoint or border crossing, it is important that you disconnect all encrypted volumes and shut your computer down completely.
- Before inserting an untrusted USB memory stick or other external storage device, including those belonging to friends or colleagues.

### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#protect-your-device-against-malware) Protect your device against malware

Encryption can only protect your files if nobody can spy on you, for example, when you enter the password to decrypt them. Malicious software like spyware and other forms of malware can reduce the effectiveness of any steps you take to protect your files and communications, so try to keep your device healthy by following the recommendations in the [Security in a Box guide on how to protect against malware](https://securityinabox.org/en/phones-and-computers/malware/).

### [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#dont-access-your-encrypted-folder-or-volume-on-a-device-you-dont-trust) Don’t access your encrypted folder or volume on a device you don’t trust

- An adversary may have installed malware to snoop on a device that is not in your control, like a shared computer at a net cafe. They might use this to steal your passwords and get access to your encrypted drive or other sensitive material on your device.

Learn why we recommend this

Following the "locked safe" metaphor, no matter how sturdy your safe is, it won't do you a whole lot of good if you leave the door open or someone can watch you as you enter the combination to open it.

## [Anchor](https://securityinabox.org/en/files/secure-file-storage/\#use-trusted-dealers-and-repair-shops) Use trusted dealers and repair shops

- If you buy a pre-owned device, have someone you trust wipe it clean and check it for malware.
- If you think someone might have the access, resources, or motivation to target you by pre-installing malware on your device before you buy it, carefully think about how to find a dealer you can trust.
- If you need your device to be repaired, be sure you trust the repair shop or the person you hand it over to.

Learn why we recommend this

When you get a pre-owned device, or send your device to be repaired, it offers adversaries an opportunity to look at your files. Pre-owned devices may unfortunately carry malware or spyware so, if possible, it might be better to buy a new one. Repair shops have sometimes been known to spy on devices or copy and sell their data. Be sure to choose a repair shop you trust.

If you are a well-known public figure, it is a good idea not to directly interact with repair providers and, instead, to ask someone you trust to get in touch with the shop so as to raise less curiosity regarding what your device may contain.