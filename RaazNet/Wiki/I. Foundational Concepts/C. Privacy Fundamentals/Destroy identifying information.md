---
title: "Destroy Identifying Information from Photos, Videos, and Files"
tags: [privacy, metadata, anonymity, photo-security, video-security, digital-forensics]
category: "Digital Security"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, Human Rights Workers]
topics: ["Metadata Removal", "Photo Privacy", "Video Privacy", "Location Privacy", "Digital Anonymity"]
summary: "Guide to removing identifying information, metadata, and location data from photos, videos, and documents before sharing."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic smartphone or computer literacy", "Understanding of file sharing risks"]
estimated_read_time: "8 minutes"
---

# Destroy Identifying Information

Files can reveal far more about you than their visible content. This guide explains how to remove identifying details and hidden metadata from photos, videos, and documents before sharing them.

## Why This Matters

Pictures and videos can expose sensitive information about you and others:

- **Visible details**: Faces of protest participants, street signs revealing your location, identifiable landmarks
- **Hidden metadata**: GPS coordinates, timestamps, device information, and creator details embedded in files

Metadata is automatically added to photos, videos, PDFs, and many other files. While useful for organizing files, this information can reveal:

- Your exact location when a file was created
- The device used to capture it
- When and by whom it was made

Anyone accessing your files could use this data to track your movements or identify you.

## Remove Identifying Details from Pictures

Before publishing photos online, obscure faces and other identifying features using tools on your device—not social media platforms. Editing through Instagram, Facebook, or Snapchat means the platform retains your original, unedited image.

> **Important**: Check if your original images are automatically backed up. Disable backup for sensitive photos or delete originals from cloud storage after editing.

### Mobile Devices (Android & iOS)

**Signal** (Free, open-source)
- Use Signal's built-in camera to take photos and blur faces
- Learn more: [Blur tools for Signal](https://signal.org/blog/blur-tools/)
- Tip: Send edited photos to yourself via [Note to Self](https://support.signal.org/hc/en-us/articles/360043272451-Note-to-Self), then download for sharing elsewhere

### Android

**Obscuracam** (Recommended)
- Automatically blurs faces and removes camera/location metadata
- Free and open-source

**Built-in Photo App**
- Use the pen tool (not marker) to cover identifying details
- Apply at least two passes over sensitive areas for security

### iOS

**Photo App Markup**
- Add fully opaque shapes rather than using semi-transparent markers
- Black rectangles or emojis provide better coverage than blur effects
- Access Markup in Photos, Messages, Mail, Notes, and Books apps

### Desktop (Linux, Windows, macOS)

**GIMP** (Free, open-source)
- Use blur and smudge tools for face obscuring
- Reference: [GIMP Blur/Sharpen Tool Guide](https://docs.gimp.org/2.10/en/gimp-tool-convolve.html)

### Why Proper Blurring Matters

Simple blur or pixelation can sometimes be reversed using deobfuscation techniques. For secure redaction:

- Use solid color overlays instead of pixelation for text
- Apply multiple blur passes
- Use recommended tools like Obscuracam that implement secure blurring

Further reading:
- [Why You Should Never Use Pixelation To Hide Sensitive Text](https://dheera.net/posts/20140725-why-you-should-never-use-pixelation)
- [Redacting photos on the go: A field guide](https://freedom.press/training/redacting-photos-on-the-go/)

## Remove Identifying Details from Videos

### Android

- **Putmask**: Automatic face tracking and blurring ([Face track tutorial](https://putmask.com/face-track-tutorial))
- **YouTube Studio**: Blur specific video sections ([YouTube blurring guide](https://support.google.com/youtube/answer/9057652))

### iOS

- **Blur-Video**: Blur faces, logos, or background objects

### Desktop (Linux, Windows, macOS)

- **Shotcut** (Free, open-source): Video editing with blur capabilities ([Video tutorial](https://www.youtube.com/watch?v=k6eyh1UaRYI))

## Disable Geolocation on Your Device

Prevent location data from being embedded in files by disabling location services before capturing photos, videos, or audio.

### Android
- [Manage location settings](https://support.google.com/accounts/answer/3467281)
- [Security in a Box: Android location guide](https://securityinabox.org/en/phones-and-computers/android/#turn-off-location-and-wipe-history)

### iOS
- [Turn off Location Services](https://support.apple.com/en-us/102647)
- [Security in a Box: iOS location guide](https://securityinabox.org/en/phones-and-computers/ios/#turn-off-location-and-wipe-history)

### macOS
- [Disable Location Services](https://support.apple.com/guide/mac-help/allow-apps-to-detect-the-location-of-your-mac-mh35873/mac#apda5e7d8a845e64)
- [Security in a Box: macOS location guide](https://securityinabox.org/en/phones-and-computers/mac/#turn-off-location-and-wipe-history)

### Windows
- [Location service and privacy settings](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088)
- [Security in a Box: Windows location guide](https://securityinabox.org/en/phones-and-computers/windows/#turn-off-location-and-wipe-history)

### Linux
- Ubuntu: [Control location services](https://help.ubuntu.com/stable/ubuntu-help/privacy-location.html)
- GNOME: [Geolocation settings](https://help.gnome.org/users/empathy/stable/geolocation-turn.html.en)
- [Security in a Box: Linux location guide](https://securityinabox.org/en/phones-and-computers/linux/#turn-off-location-and-wipe-history)

### Review App Permissions

Regularly check which apps can access your location:
- [Android permissions](https://securityinabox.org/en/phones-and-computers/android/#check-your-app-permissions)
- [iOS permissions](https://securityinabox.org/en/phones-and-computers/ios/#check-your-app-permissions)
- [macOS permissions](https://securityinabox.org/en/phones-and-computers/mac/#check-your-app-permissions)
- [Windows permissions](https://securityinabox.org/en/phones-and-computers/windows/#check-your-app-permissions)
- [Linux permissions](https://securityinabox.org/en/phones-and-computers/linux/#check-your-app-permissions)

## Remove Metadata from Files

Strip hidden metadata from photos, videos, audio files, and documents before sharing.

> **Note**: On some operating systems, metadata removal is only available for images and videos, not all file types.

### Android

- **Scrambled Exif**: Remove metadata from photos
- **ExifTool for Android**: View, edit, and delete metadata in photos and videos

### iOS

- **MetaX**: Check, edit, and delete photo metadata
- **Photo & Video Metadata Remover**: Creates metadata-free copies (preserves originals)

### Desktop (Linux, Windows, macOS)

- **ExifCleaner**: Clean metadata from images, videos, PDFs, and other files

### Understanding Metadata

To view a file's metadata:
- **Windows**: Right-click → Properties
- **macOS**: Right-click → Get Info
- **Linux**: Right-click → Properties

For comprehensive information about media metadata, see [Everything you wanted to know about media metadata, but were afraid to ask](https://freedom.press/training/everything-you-wanted-know-about-media-metadata-were-afraid-ask/).

---

*Last updated: 20 March 2024*