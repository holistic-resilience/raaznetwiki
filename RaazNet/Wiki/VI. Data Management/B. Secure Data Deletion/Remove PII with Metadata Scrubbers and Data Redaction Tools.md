---
title: "Data and Metadata Redaction Tools"
tags: [privacy, security, metadata, exif, data-redaction, file-management]
category: "Privacy Tools"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Activists, Journalists, General Public]
topics: ["Digital Security", "Privacy Protection", "Metadata Removal"]
summary: "Guide to removing personally identifiable metadata from files using cross-platform tools like MAT2, ExifEraser, and ExifTool."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file types"]
estimated_read_time: "4 minutes"
---

# Data and Metadata Redaction

When sharing files, be sure to remove associated metadata. Image files commonly include [Exif](https://en.wikipedia.org/wiki/Exif) data, which can contain sensitive information. Photos sometimes even include GPS coordinates in the file metadata.

> [!warning]
> You should **never** use blur to redact [text in images](https://bishopfox.com/blog/unredacter-tool-never-pixelation). If you want to redact text in an image, you should draw a box over the text.

---

## MAT2

**MAT2** is free, cross-platform software for removing metadata from image, audio, torrent, and document file types. It provides both a command line tool and a graphical user interface via an extension for [Dolphin](https://github.com/jvoisin/mat2/tree/master/dolphin), the default file manager of [KDE](https://kde.org/).

**Platforms:** Windows, macOS, Linux, Web

**Resources:**
- [Repository & Documentation](https://github.com/jvoisin/mat2#readme)
- [Download (PyPI)](https://pypi.org/project/mat2)

---

## ExifEraser (Android)

**ExifEraser** is a modern, permissionless image metadata erasing application for Android. It currently supports JPEG, PNG, and WebP files.

### Supported Metadata Removal

| Format | Metadata Removed |
|--------|------------------|
| JPEG | ICC Profile, Exif, Photoshop Image Resources, XMP/ExtendedXMP |
| PNG | ICC Profile, Exif, XMP |
| WebP | ICC Profile, Exif, XMP |

### Key Features

- Share images directly from other applications
- Process single images, multiple images, or entire directories
- Built-in camera option that automatically strips metadata from new photos
- Split-screen drag-and-drop support
- Clipboard paste functionality
- Detailed report of removed metadata after processing

**Download:** [Google Play](https://play.google.com/store/apps/details?id=com.none.tom.exiferaser) | [Accrescent](https://accrescent.app/app/com.none.tom.exiferaser) | [GitHub](https://github.com/Tommy-Geenexus/exif-eraser/releases)

---

## Shortcuts (iOS & macOS)

On iOS and macOS, you can remove image metadata without third-party apps by creating a [Shortcut](https://apps.apple.com/app/id915249334).

**Download example shortcut:** [Clean Image Metadata](https://icloud.com/shortcuts/fb774ddb7b5b4296871776c67ac0fff9)

### How to Use

1. Download and add the shortcut
2. Access it via the Share button when selecting images
3. Select multiple images to process them simultaneously

### What It Removes

- Location data
- Device and lens model information
- Other camera metadata
- Resets image creation date to processing time

> [!tip]
> When creating your own shortcut, ensure the **Preserve Metadata** option under the **Convert** action is unchecked.

---

## ExifTool (CLI)

**ExifTool** is the original Perl library and command-line application for reading, writing, and editing meta information (Exif, IPTC, XMP, and more) in a wide variety of file formats (JPEG, TIFF, PNG, PDF, RAW, and more).

It is often a component of other Exif removal applications and is available in most Linux distribution repositories.

**Platforms:** Windows, macOS, Linux

**Resources:**
- [Homepage](https://exiftool.org/)
- [Documentation](https://exiftool.org/faq.html)
- [Source Code](https://github.com/exiftool/exiftool)

### Basic Usage

Delete metadata from all files of a specific type in a directory:

```bash
exiftool -all= *.file_extension
```

---

## Selection Criteria

These tools were selected based on the following requirements:

- Apps developed for open-source operating systems must be open source
- Apps must be free and should not include ads or other limitations