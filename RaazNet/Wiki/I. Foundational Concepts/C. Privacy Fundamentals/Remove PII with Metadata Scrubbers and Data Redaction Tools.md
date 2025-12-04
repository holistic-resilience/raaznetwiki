---
title: "Remove PII with Metadata Scrubbers and Data Redaction Tools"
tags: [privacy, security, metadata, data-redaction, exif, digital-hygiene]
category: "Digital Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Digital Security", "Privacy Protection", "Metadata Removal", "File Sanitization"]
summary: "Guide to removing personally identifiable information and metadata from files using cross-platform tools like MAT2, ExifEraser, and ExifTool."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of file types"]
estimated_read_time: "6 minutes"
---

# Data and Metadata Redaction

When sharing files, be sure to remove associated metadata. Image files commonly include [Exif](https://en.wikipedia.org/wiki/Exif) data, which can contain sensitive information such as GPS coordinates, device information, and timestamps.

> [!warning] Text Redaction
> You should **never** use blur to redact [text in images](https://bishopfox.com/blog/unredacter-tool-never-pixelation). Blurred or pixelated text can often be recovered. If you want to redact text in an image, draw a solid opaque box over the text instead.

---

## Recommended Tools

### MAT2 (Cross-Platform)

![MAT2 logo](https://www.privacyguides.org/en/assets/img/data-redaction/mat2.svg)

**MAT2** is free, cross-platform software for removing metadata from image, audio, torrent, and document file types. It provides both a command-line tool and a graphical user interface via an extension for [Dolphin](https://github.com/jvoisin/mat2/tree/master/dolphin), the default file manager of [KDE](https://kde.org/).

**Downloads:** [Windows](https://pypi.org/project/mat2) | [macOS](https://github.com/jvoisin/mat2#requirements-setup-on-macos-os-x-using-homebrew) | [Linux](https://pypi.org/project/mat2) | [Web Interface](https://github.com/jvoisin/mat2#web-interface)

**Resources:** [Repository](https://github.com/jvoisin/mat2#readme) | [Documentation](https://github.com/jvoisin/mat2#how-to-use-mat2)

---

### ExifEraser (Android)

![ExifEraser logo](https://www.privacyguides.org/en/assets/img/data-redaction/exiferaser.svg)

**ExifEraser** is a modern, permissionless image metadata erasing application for Android supporting JPEG, PNG, and WebP files.

#### Supported Metadata Removal

| Format | Metadata Removed |
|--------|------------------|
| JPEG | ICC Profile, Exif, Photoshop Image Resources, XMP/ExtendedXMP |
| PNG | ICC Profile, Exif, XMP |
| WebP | ICC Profile, Exif, XMP |

#### Key Features

- Share images directly from other applications
- Process single images, multiple images, or entire directories
- Built-in camera option that automatically strips metadata from new photos
- Split-screen drag-and-drop support
- Clipboard paste functionality
- Detailed removal reports after processing

**Downloads:** [Google Play](https://play.google.com/store/apps/details?id=com.none.tom.exiferaser) | [Accrescent](https://accrescent.app/app/com.none.tom.exiferaser) | [GitHub](https://github.com/Tommy-Geenexus/exif-eraser/releases)

---

### Shortcuts (iOS & macOS)

On iOS and macOS, you can remove image metadata without third-party apps by creating a [Shortcut](https://apps.apple.com/app/id915249334).

**Download ready-to-use shortcut:** [Clean Image Metadata](https://icloud.com/shortcuts/fb774ddb7b5b4296871776c67ac0fff9)

#### Usage Instructions

1. Download and add the shortcut
2. Access it via the share sheet (Share button) when viewing images
3. Select multiple images to process them simultaneously

#### What It Removes

- Location data
- Device and lens model information
- Camera settings and information
- Sets image creation date to the time of processing

> [!tip] Custom Shortcuts
> You can use the provided shortcut as a template. Ensure the **Preserve Metadata** option under the **Convert** action is unchecked.

---

### ExifTool (CLI)

![ExifTool logo](https://www.privacyguides.org/en/assets/img/data-redaction/exiftool.png)

**ExifTool** is the original Perl library and command-line application for reading, writing, and editing metadata (Exif, IPTC, XMP, and more) across numerous file formats (JPEG, TIFF, PNG, PDF, RAW, and more).

ExifTool is often a component of other metadata removal applications and is available in most Linux distribution repositories.

**Downloads:** [Windows](https://exiftool.org/) | [macOS](https://exiftool.org/) | [Linux](https://exiftool.org/)

**Resources:** [Homepage](https://exiftool.org/) | [Documentation](https://exiftool.org/faq.html) | [Source Code](https://github.com/exiftool/exiftool)

#### Basic Usage

Delete metadata from all files of a specific type in a directory:

```bash
exiftool -all= *.file_extension
```

---

## Selection Criteria

The tools recommended in this guide meet the following criteria:

- **Open Source**: Apps developed for open-source operating systems must be open source
- **Free**: Apps must be free without ads or artificial limitations

---

## Related Topics

- [[encryption-basics|Encryption Basics]]
- [[secure-file-sharing|Secure File Sharing]]
- [[mobile-privacy|Mobile Privacy]]