---
title: "Destroy Identifying Information from Photos, Videos, and Files"
tags: [privacy, metadata, anonymity, photos, videos, geolocation]
category: "Digital Privacy"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users]
topics: ["Metadata Removal", "Photo Privacy", "Video Privacy", "Geolocation"]
summary: "Guide to removing identifying metadata and visual details from photos, videos, and files before sharing online."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic smartphone or computer usage", "Understanding of why privacy matters"]
estimated_read_time: "8 minutes"
---

# Destroy Identifying Information

Files and media you create contain hidden information that can reveal your identity, location, and device details. This guide explains how to remove both visible identifying details and hidden metadata from your photos, videos, and documents before sharing them.

## Why This Matters

Pictures and videos can reveal information about you and others in several ways:

- **Visible details**: Faces of demonstration participants, street signs showing your location, identifying landmarks
- **Hidden metadata**: GPS coordinates, timestamps, device information, and creator details embedded in files

This metadata can be useful for organizing your files, but it can also expose sensitive information to anyone who obtains the file—including your physical location at specific times.

---

## Remove Identifying Details from Pictures

Before publishing photos online, you may need to blur or obscure faces and other identifying details. 

> **Important**: Avoid using social media platform editing tools (Instagram, Facebook, Snapchat) for this purpose. These platforms receive your original unedited image first and may share it if requested. Edit locally on your device instead.

> **Backup Warning**: Original images may be automatically backed up to cloud services. Either disable photo backup or delete originals from your backup platform after editing.

### Mobile Devices

**Android and iOS**
- **[Signal](https://signal.org/)**: Use this privacy-focused messaging app to take photos and blur faces. See [Blur tools for Signal](https://signal.org/blog/blur-tools/) for instructions. You can send edited photos to yourself via [Note to Self](https://support.signal.org/hc/en-us/articles/360043272451-Note-to-Self), then download and share elsewhere.

**Android Only**
- **[Obscuracam](https://securityinabox.org/en/files/tools#obscuracam)**: Free, open-source app that blurs faces and removes camera/location metadata
- **Built-in Photo app**: Use the pen tool (not marker) and run it over identifying details at least twice to prevent deobfuscation

**iOS Only**
- **Photo app**: Use [Markup tools](https://support.apple.com/guide/iphone/edit-photos-and-videos-iphb08064d57/ios#iph1c7564dba) to add fully opaque shapes, black rectangles, or emojis over sensitive areas. Avoid semi-transparent marker tools.
- **Markup in other apps**: Available in Messages, Mail, Notes, and Books for editing photos, screenshots, and PDFs

### Desktop Computers

**Linux, Windows, macOS**
- **[GIMP](https://www.gimp.org/)**: Free, open-source photo editor. See the [official blur guide](https://docs.gimp.org/2.10/en/gimp-tool-convolve.html) for instructions.

### Why Proper Blurring Matters

Simple face blur or pixelation may not adequately protect identities. Some blurring techniques can be reversed using deobfuscation methods. 

**Resources:**
- [Why You Should Never Use Pixelation To Hide Sensitive Text](https://dheera.net/posts/20140725-why-you-should-never-use-pixelation)
- [Redacting photos on the go: A field guide](https://freedom.press/training/redacting-photos-on-the-go/)

---

## Remove Identifying Details from Videos

### Mobile Devices

**Android**
- **[Putmask](https://putmask.com/)**: Blur faces in videos with automatic face tracking. See their [face track tutorial](https://putmask.com/face-track-tutorial).

**iOS**
- **[Blur-Video](https://apps.apple.com/us/app/blur-video/id1555770514)**: Blur faces, logos, or background objects

### Desktop and Web

**All Platforms**
- **YouTube Studio**: Blur parts of videos before or after upload. See [YouTube's blurring guide](https://support.google.com/youtube/answer/9057652).
- **[Shotcut](https://shotcut.org/)**: Free, open-source video editor. Tutorial: [How To Blur Part Of Video in Shotcut](https://www.youtube.com/watch?v=k6eyh1UaRYI)

---

## Disable Geolocation on Your Devices

Prevention is easier than removal. Turn off location services before creating photos, videos, or audio files to avoid embedding GPS data.

### By Platform

| Platform | Instructions |
|----------|-------------|
| **Android** | [Manage location settings](https://support.google.com/accounts/answer/3467281) or see [Security in a Box Android guide](https://securityinabox.org/en/phones-and-computers/android/#turn-off-location-and-wipe-history) |
| **iOS** | [Turn off Location Services](https://support.apple.com/en-us/102647) or see [Security in a Box iOS guide](https://securityinabox.org/en/phones-and-computers/ios/#turn-off-location-and-wipe-history) |
| **macOS** | [Turn off Location Services](https://support.apple.com/guide/mac-help/allow-apps-to-detect-the-location-of-your-mac-mh35873/mac#apda5e7d8a845e64) or see [Security in a Box macOS guide](https://securityinabox.org/en/phones-and-computers/mac/#turn-off-location-and-wipe-history) |
| **Windows** | [Location service and privacy](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088) or see [Security in a Box Windows guide](https://securityinabox.org/en/phones-and-computers/windows/#turn-off-location-and-wipe-history) |
| **Linux (Ubuntu)** | [Control location services](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html) or see [Security in a Box Linux guide](https://securityinabox.org/en/phones-and-computers/linux/#turn-off-location-and-wipe-history) |
| **Linux (GNOME)** | [Activate/deactivate geolocation](https://help.gnome.org/users/empathy/stable/geolocation-turn.html.en) |

### Check App Permissions

Review which apps have location access on your device:
- [Android](https://securityinabox.org/en/phones-and-computers/android/#check-your-app-permissions)
- [iOS](https://securityinabox.org/en/phones-and-computers/ios/#check-your-app-permissions)
- [macOS](https://securityinabox.org/en/phones-and-computers/mac/#check-your-app-permissions)
- [Windows](https://securityinabox.org/en/phones-and-computers/windows/#check-your-app-permissions)
- [Linux](https://securityinabox.org/en/phones-and-computers/linux/#check-your-app-permissions)

---

## Remove Metadata from Files

Metadata removal tools vary by platform. Note that some operating systems only support editing metadata in images and videos, not all file types.

### Mobile Devices

**Android**
- **[Scrambled Exif](https://securityinabox.org/en/files/tools#scrambled-exif)**: Remove metadata from photos
- **[ExifTool for Android](https://play.google.com/store/apps/details?id=com.exiftool.free)**: View, edit, and delete metadata in photos and videos

**iOS**
- **[MetaX](https://securityinabox.org/en/files/tools#metax)**: Check, edit, and delete photo metadata
- **[Photo & Video Metadata Remover](https://apps.apple.com/us/app/photo-video-metadata-remover/id1079710135)**: Creates metadata-free copies (preserves originals)

### Desktop Computers

**Linux, Windows, macOS**
- **[ExifCleaner](https://securityinabox.org/en/files/tools#exifcleaner)**: Clean metadata from images, videos, PDFs, and other files

### Understanding Metadata

All files contain metadata about their creation—where, when, how, and by whom. You can view some metadata by right-clicking a file and selecting **Properties** (Windows) or **Get Info** (macOS).

**Further Reading**: [Everything you wanted to know about media metadata, but were afraid to ask](https://freedom.press/training/everything-you-wanted-know-about-media-metadata-were-afraid-ask/)

---

*Last updated: 20 March 2024*