---
title: "Android General Apps for Privacy and Security"
tags: [android, privacy, security, apps, grapheneos, work-profile]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Android Users, Security Enthusiasts]
topics: ["Android Apps", "Privacy Protection", "App Isolation", "Metadata Removal"]
summary: "Privacy-focused Android apps that enhance system functionality, including work profile isolation, secure camera, and PDF viewing."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Basic"
language: "English"
prerequisites: ["Basic Android knowledge", "Understanding of app permissions"]
estimated_read_time: "4 minutes"
---

# Android General Apps for Privacy and Security

This guide covers Android-exclusive applications that enhance or replace key system functionality with privacy and security in mind.

## Shelter - Work Profile Isolation

> **Note:** If your device runs Android 15 or later, consider using the native [Private Space](https://www.privacyguides.org/en/os/android-overview/#private-space) feature instead, which provides similar functionality without requiring third-party app permissions.

**Shelter** leverages Android's Work Profile functionality to isolate or duplicate apps on your device.

### Key Features
- Block contact search across profiles
- Share files across profiles via the default file manager (DocumentsUI)
- Supports contact search blocking (advantage over alternatives like Insular and Island)

### Important Considerations
- Shelter acts as a [Device Admin](https://developer.android.com/guide/topics/admin/device-admin) to create the Work Profile
- The developer has extensive access to data stored within the Work Profile
- Requires placing complete trust in the developer

**Links:** [Repository](https://gitea.angry.im/PeterCxy/Shelter#shelter) | [Source Code](https://gitea.angry.im/PeterCxy/Shelter) | [Support](https://patreon.com/PeterCxy)

---

## Secure Camera

**Secure Camera** is a privacy-focused camera app from GrapheneOS that captures images, videos, and QR codes.

### Key Features
- **Automatic Exif metadata removal** (enabled by default)
- Uses modern Media API—no storage permissions required
- Microphone permission only needed for audio recording
- CameraX vendor extensions supported (Portrait, HDR, Night Sight, Face Retouch, Auto)

### Current Limitations
- Metadata is not yet deleted from video files (planned feature)
- Image orientation metadata is not removed
- Location data (if enabled) is preserved—use [ExifEraser](https://www.privacyguides.org/en/data-redaction/#exiferaser-android) for removal

**Downloads:** [Google Play](https://play.google.com/store/apps/details?id=app.grapheneos.camera.play) | [GitHub](https://github.com/GrapheneOS/Camera/releases) | [GrapheneOS App Store](https://github.com/GrapheneOS/Apps/releases)

**Links:** [Repository](https://github.com/GrapheneOS/Camera#readme) | [Documentation](https://grapheneos.org/usage#camera)

---

## Secure PDF Viewer

**Secure PDF Viewer** is a permission-free PDF viewer based on [pdf.js](https://en.wikipedia.org/wiki/PDF.js) from GrapheneOS.

### Security Architecture
- PDFs are rendered in a [sandboxed](https://en.wikipedia.org/wiki/Sandbox_(software_development)) [WebView](https://developer.android.com/guide/webapps/webview)
- No direct file access permissions required
- [Content-Security-Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) enforces static JavaScript and styling

**Downloads:** [Google Play](https://play.google.com/store/apps/details?id=app.grapheneos.pdfviewer.play) | [GitHub](https://github.com/GrapheneOS/PdfViewer/releases) | [GrapheneOS App Store](https://github.com/GrapheneOS/Apps/releases)

**Links:** [Repository](https://github.com/GrapheneOS/PdfViewer#readme) | [Source Code](https://github.com/GrapheneOS/PdfViewer)

---

## Selection Criteria

These recommendations follow Privacy Guides' [standard criteria](https://www.privacyguides.org/en/about/criteria/):

- Must extend or replace core system functionality
- Not applicable to other software categories on the site
- Must receive regular updates and maintenance