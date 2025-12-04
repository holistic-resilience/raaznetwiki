---
title: "Destroy Identifying Information from Photos, Videos, and Files"
tags: [privacy, metadata, digital-security, anonymity, photos, videos]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users]
topics: ["Metadata Removal", "Photo Privacy", "Video Privacy", "Digital Anonymity"]
summary: "Guide to removing identifying information and metadata from photos, videos, and documents to protect privacy when sharing files online."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file sharing risks"]
estimated_read_time: "8 minutes"
---

# Destroy Identifying Information

This guide explains how to remove identifying information from photos, videos, PDFs, and other files before sharing them online. Protecting this information helps safeguard your privacy and the privacy of others who may appear in your media.

## Why This Matters

Pictures and videos can reveal significant information about you and others:
- **Visual details**: Faces of participants at events, street signs revealing locations, identifying landmarks
- **Metadata**: Hidden information embedded in files including GPS coordinates, timestamps, device information, and creator details

Metadata can be useful for organizing files, but it can also expose sensitive information to anyone who accesses the file—potentially revealing your physical location, daily patterns, or the identities of people you're with.

---

## Remove Identifying Details from Pictures

When sharing photos, you may need to blur or obscure faces and other identifying details. **Avoid using social media platform editing tools** (Instagram, Facebook, Snapchat) for this purpose—these platforms receive your original, unedited image and may share it if requested.

> **Important**: Check if your original images are automatically backed up. Either disable backup for photos or delete originals from your backup service after editing.

### Mobile Devices (Android & iOS)

**Signal** (Free, open-source)
- Use Signal's built-in camera to take photos and blur faces
- Send edited photos to yourself via "Note to Self" for downloading
- Learn more: [Signal Blur Tools](https://signal.org/blog/blur-tools/)

### Android

**Obscuracam** (Free, open-source)
- Automatically detects and blurs faces
- Removes camera and location metadata
- [Download Obscuracam](https://securityinabox.org/en/files/tools#obscuracam)

**Built-in Photo App**
- Use the **pen tool** (not the marker) to obscure details
- Run the pen over identifying details at least twice
- [Google Photos editing guide](https://support.google.com/photos/answer/6128850)

### iOS

**Photos App Markup**
- Use fully opaque shapes rather than semi-transparent markers
- Add black rectangles or emojis over sensitive areas
- [Apple's photo editing guide](https://support.apple.com/guide/iphone/edit-photos-and-videos-iphb08064d57/ios)

**Markup in Other Apps**
- Available in Messages, Mail, Notes, and Books
- [Draw in apps with Markup](https://support.apple.com/guide/iphone/draw-in-apps-iph893c6f8bf/ios)

### Desktop (Linux, Windows, macOS)

**GIMP** (Free, open-source)
- Professional-grade photo editing
- [GIMP blur tool documentation](https://docs.gimp.org/2.10/en/gimp-tool-convolve.html)

> **Security Note**: Simple pixelation may be reversible through deobfuscation techniques. Use solid color overlays or proper blur tools designed for redaction. See [Why You Should Never Use Pixelation To Hide Sensitive Text](https://dheera.net/posts/20140725-why-you-should-never-use-pixelation) and [Redacting photos on the go: A field guide](https://freedom.press/training/redacting-photos-on-the-go/).

---

## Remove Identifying Details from Videos

### Android

**Putmask**
- Automatic face detection and blurring
- [Face track tutorial](https://putmask.com/face-track-tutorial)

**YouTube Studio**
- Blur faces or areas in uploaded videos
- [YouTube blurring guide](https://support.google.com/youtube/answer/9057652)

### iOS

**Blur-Video**
- Blur faces, logos, or background objects
- [Download from App Store](https://apps.apple.com/us/app/blur-video/id1555770514)

### Desktop (Linux, Windows, macOS)

**Shotcut** (Free, open-source)
- Full-featured video editor with blur capabilities
- [Video tutorial: How to blur in Shotcut](https://www.youtube.com/watch?v=k6eyh1UaRYI)

---

## Disable Geolocation on Your Device

The most effective approach is to prevent location data from being recorded in the first place. Disable location services before creating photos, videos, or audio files.

### By Platform

| Platform | Instructions |
|----------|-------------|
| **Android** | [Manage location settings](https://support.google.com/accounts/answer/3467281) • [Security in a Box guide](https://securityinabox.org/en/phones-and-computers/android/#turn-off-location-and-wipe-history) |
| **iOS** | [Turn off Location Services](https://support.apple.com/en-us/102647) • [Security in a Box guide](https://securityinabox.org/en/phones-and-computers/ios/#turn-off-location-and-wipe-history) |
| **macOS** | [Location Services settings](https://support.apple.com/guide/mac-help/allow-apps-to-detect-the-location-of-your-mac-mh35873/mac) • [Security in a Box guide](https://securityinabox.org/en/phones-and-computers/mac/#turn-off-location-and-wipe-history) |
| **Windows** | [Location service and privacy](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088) • [Security in a Box guide](https://securityinabox.org/en/phones-and-computers/windows/#turn-off-location-and-wipe-history) |
| **Linux (Ubuntu)** | [Ubuntu location services](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html) • [Security in a Box guide](https://securityinabox.org/en/phones-and-computers/linux/#turn-off-location-and-wipe-history) |
| **Linux (GNOME)** | [GNOME geolocation settings](https://help.gnome.org/users/empathy/stable/geolocation-turn.html.en) |

### Review App Permissions

Regularly check which apps have access to your location:
- [Android](https://securityinabox.org/en/phones-and-computers/android/#check-your-app-permissions)
- [iOS](https://securityinabox.org/en/phones-and-computers/ios/#check-your-app-permissions)
- [macOS](https://securityinabox.org/en/phones-and-computers/mac/#check-your-app-permissions)
- [Windows](https://securityinabox.org/en/phones-and-computers/windows/#check-your-app-permissions)
- [Linux](https://securityinabox.org/en/phones-and-computers/linux/#check-your-app-permissions)

---

## Remove Metadata from Files

Metadata removal tools can strip identifying information from photos, videos, audio files, and documents.

> **Tip**: View a file's metadata by right-clicking and selecting **Properties** (Windows/Linux) or **Get Info** (macOS).

### Android

| Tool | Purpose |
|------|---------|
| **[Scrambled Exif](https://securityinabox.org/en/files/tools#scrambled-exif)** | Remove metadata from photos |
| **[ExifTool for Android](https://play.google.com/store/apps/details?id=com.exiftool.free)** | View, edit, and delete metadata in photos and videos |

### iOS

| Tool | Purpose |
|------|---------|
| **[MetaX](https://securityinabox.org/en/files/tools#metax)** | Check, edit, and delete photo metadata |
| **[Photo & Video Metadata Remover](https://apps.apple.com/us/app/photo-video-metadata-remover/id1079710135)** | Creates metadata-free copies (preserves originals) |

### Desktop (Linux, Windows, macOS)

**[ExifCleaner](https://securityinabox.org/en/files/tools#exifcleaner)** (Free, open-source)
- Supports images, videos, PDFs, and other file types
- Batch processing capability

---

## Further Reading

- [Everything you wanted to know about media metadata, but were afraid to ask](https://freedom.press/training/everything-you-wanted-know-about-media-metadata-were-afraid-ask/) — Freedom of the Press Foundation
- [Redacting photos on the go: A field guide](https://freedom.press/training/redacting-photos-on-the-go/) — Freedom of the Press Foundation