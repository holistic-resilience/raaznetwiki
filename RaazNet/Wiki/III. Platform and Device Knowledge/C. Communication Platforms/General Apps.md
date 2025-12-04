```yaml
---
title: "General Android Apps for Privacy and Security"
tags: [android, privacy, security, apps, grapheneos, work-profile]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Android Users, Security Enthusiasts]
topics: ["Android Apps", "Privacy Protection", "Mobile Security"]
summary: "Recommended Android apps that enhance privacy and security by replacing or extending core system functionality."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic Android knowledge", "Understanding of app permissions"]
estimated_read_time: "4 minutes"
---
```

# General Android Apps for Privacy and Security

This guide covers Android-exclusive apps that enhance or replace key system functionality with a focus on privacy and security.

## Shelter (Work Profile Manager)

> **Note:** If your device runs Android 15 or later, consider using the native [Private Space](https://www.privacyguides.org/en/os/android-overview/#private-space) feature instead, which provides similar functionality without requiring third-party app permissions.

**Shelter** helps you leverage Android's Work Profile functionality to isolate or duplicate apps on your device.

### Key Features
- Blocks contact search across profiles
- Enables file sharing between profiles via the default file manager ([DocumentsUI](https://source.android.com/devices/architecture/modular-system/documentsui))
- Supports [contact search blocking](https://secure-system.gitlab.io/Insular/faq.html)

### Important Consideration

> ⚠️ **Warning:** Shelter acts as a [Device Admin](https://developer.android.com/guide/topics/admin/device-admin) to create the Work Profile, giving it extensive access to data stored within the Work Profile. Only use if you trust the developer.

Shelter is recommended over alternatives like [Insular](https://secure-system.gitlab.io/Insular) and [Island](https://github.com/oasisfeng/island) due to its contact search blocking support.

**Links:** [Repository](https://gitea.angry.im/PeterCxy/Shelter#shelter) | [Source Code](https://gitea.angry.im/PeterCxy/Shelter) | [Contribute](https://patreon.com/PeterCxy)

---

## Secure Camera

A privacy-focused camera app that captures images, videos, and QR codes with enhanced security features.

### Key Features
- **Auto Exif removal** (enabled by default) - automatically strips metadata from images
- Uses the modern [Media API](https://developer.android.com/training/data-storage/shared/media), eliminating storage permission requirements
- Microphone permission only required for audio recording
- Supports CameraX vendor extensions (Portrait, HDR, Night Sight, Face Retouch, Auto) on compatible devices

### Limitations
- Video metadata removal is not yet implemented (planned feature)
- Image orientation metadata is retained
- Location data (if enabled) is not automatically removed - use [ExifEraser](https://www.privacyguides.org/en/data-redaction/#exiferaser-android) for manual removal

### Downloads
- [Google Play](https://play.google.com/store/apps/details?id=app.grapheneos.camera.play)
- [GitHub Releases](https://github.com/GrapheneOS/Camera/releases)
- [GrapheneOS App Store](https://github.com/GrapheneOS/Apps/releases)

**Links:** [Repository](https://github.com/GrapheneOS/Camera#readme) | [Documentation](https://grapheneos.org/usage#camera) | [Contribute](https://grapheneos.org/donate)

---

## Secure PDF Viewer

A security-focused PDF viewer based on [pdf.js](https://en.wikipedia.org/wiki/PDF.js) designed to minimize attack surface.

### Security Features
- **No permissions required** - doesn't need direct access to content or files
- PDFs are rendered in a [sandboxed](https://en.wikipedia.org/wiki/Sandbox_(software_development)) [WebView](https://developer.android.com/guide/webapps/webview)
- [Content-Security-Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) enforces static JavaScript and styling properties

### Downloads
- [Google Play](https://play.google.com/store/apps/details?id=app.grapheneos.pdfviewer.play)
- [GitHub Releases](https://github.com/GrapheneOS/PdfViewer/releases)
- [GrapheneOS App Store](https://github.com/GrapheneOS/Apps/releases)

**Links:** [Repository](https://github.com/GrapheneOS/PdfViewer#readme) | [Source Code](https://github.com/GrapheneOS/PdfViewer) | [Contribute](https://grapheneos.org/donate)

---

## Selection Criteria

These apps are recommended based on the following criteria:

- Must extend or replace core Android system functionality
- Not applicable to other software categories on Privacy Guides
- Receives regular updates and active maintenance
- Meets Privacy Guides' [standard criteria](https://www.privacyguides.org/en/about/criteria/)