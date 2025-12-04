---
title: "Destroy Identifying Information from Files"
tags: [privacy, metadata, anonymity, photo-security, digital-forensics]
category: "Digital Privacy"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users]
topics: ["Metadata Removal", "Photo Privacy", "Video Privacy", "Geolocation"]
summary: "Guide to removing identifying information, metadata, and location data from photos, videos, and other files before sharing."
source: "Security in a Box"
content_type: "Tutorial"
security_level: "Basic"
language: "English"
prerequisites: ["Basic smartphone or computer literacy", "Understanding of file sharing risks"]
estimated_read_time: "8 minutes"
---

# Destroy Identifying Information

Files such as photos, videos, and documents can reveal sensitive information about you and others. This guide explains how to remove identifying details and metadata before sharing files.

## Why This Matters

Pictures and videos can reveal significant information:
- **Visible details**: Faces of participants at events, street signs showing your location, identifying landmarks
- **Hidden metadata**: GPS coordinates, timestamps, device information, and creator details embedded in files

This metadata can be useful for organizing files but poses privacy risks when sharing. Someone analyzing your files could determine your physical location, daily patterns, or the device you use.

## Remove Identifying Details from Pictures

Before publishing photos online, remove or obscure identifying details using tools on your device rather than social media platforms. Platform-based editing uploads the original image first, which the platform retains.

> **Important**: Check if your original images are automatically backed up. Either disable backup for photos or delete originals from your backup service after editing.

### Android and iOS

**Signal** (free, open-source)
- Use Signal's built-in camera to take photos and blur faces
- Send edited photos to yourself via "Note to Self," then download and share elsewhere
- See [Signal's blur tools guide](https://signal.org/blog/blur-tools/)

### Android Only

**Obscuracam** (free, open-source)
- Blurs faces automatically
- Removes camera and location metadata
- Recommended for secure face blurring

**Built-in Photo App**
- Use the pen tool (not marker) for redaction
- Run over identifying details at least twice
- The marker tool is semi-transparent and less secure

### iOS Only

**Photo App Markup**
- Add fully opaque shapes rather than using marker tools
- Black rectangles or emojis provide better coverage than semi-transparent markers
- Available in Messages, Mail, Notes, and Books apps for photos, screenshots, and PDFs

### Desktop (Linux, Windows, macOS)

**GIMP** (free, open-source)
- Professional-grade photo editing
- Use the blur/smudge tool for obscuring details
- See [GIMP's convolve tool documentation](https://docs.gimp.org/2.10/en/gimp-tool-convolve.html)

### Why Blurring Method Matters

Some blurring techniques can be reversed through deobfuscation. Pixelation is particularly vulnerable—avoid using it for sensitive text. For detailed guidance, see:
- [Why You Should Never Use Pixelation To Hide Sensitive Text](https://dheera.net/posts/20140725-why-you-should-never-use-pixelation)
- [Redacting photos on the go: A field guide](https://freedom.press/training/redacting-photos-on-the-go/)

## Remove Identifying Details from Videos

### Android

- **Putmask**: Automatic face tracking and blurring ([face track tutorial](https://putmask.com/face-track-tutorial))
- **YouTube Studio**: Blur portions of videos before or after upload

### iOS

- **Blur-Video**: Blur faces, logos, or background objects

### Desktop (Linux, Windows, macOS)

- **Shotcut** (free, open-source): Full-featured video editor with blur capabilities

## Disable Geolocation on Your Devices

Preventing location data from being recorded is easier than removing it afterward. Disable location services before creating photos, videos, or audio files.

### By Platform

| Platform | Action |
|----------|--------|
| **Android** | Settings → Location → Turn off |
| **iOS** | Settings → Privacy → Location Services → Turn off |
| **macOS** | System Preferences → Security & Privacy → Privacy → Location Services |
| **Windows** | Settings → Privacy → Location → Turn off |
| **Linux (Ubuntu/GNOME)** | Settings → Privacy → Location Services → Turn off |

Also review which apps have location permissions and revoke access where unnecessary.

## Remove Metadata from Files

Use these tools to strip metadata from photos, videos, audio files, and PDFs.

### Android

- **Scrambled Exif**: Removes metadata from photos
- **ExifTool for Android**: View, edit, and delete metadata in photos and videos

### iOS

- **MetaX**: Check, edit, and delete photo metadata
- **Photo & Video Metadata Remover**: Creates metadata-free copies (preserves originals)

### Desktop (Linux, Windows, macOS)

- **ExifCleaner**: Batch clean metadata from images, videos, PDFs, and other files

### Understanding Metadata

To view basic metadata on a computer:
- **Windows**: Right-click file → Properties → Details
- **macOS**: Right-click file → Get Info
- **Linux**: Right-click file → Properties

For comprehensive information about media metadata, see [Everything you wanted to know about media metadata](https://freedom.press/training/everything-you-wanted-know-about-media-metadata-were-afraid-ask/).

---

*Last updated: March 2024*