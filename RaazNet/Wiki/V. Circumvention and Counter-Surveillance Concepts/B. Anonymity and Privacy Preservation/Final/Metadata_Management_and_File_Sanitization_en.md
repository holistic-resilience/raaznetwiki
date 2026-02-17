---
title: "Metadata Management and File Sanitization"
tags:
  [
    metadata,
    exif,
    privacy,
    redaction,
    sanitization,
    dangerzone,
    digital-forensics,
    iran-security,
  ]
category: "Anonymity and Privacy"
difficulty: "Intermediate"
audience: [Activists, Journalists, Privacy-Conscious Users, General Public]
topics:
  [
    "Metadata Removal",
    "Document Sanitization",
    "Visual Redaction",
    "Anti-Forensics",
  ]
summary: "A comprehensive guide to removing invisible data (metadata) from files, safely redacting visual information, and sanitizing documents to neutralize tracking and malware."
source: "Raaznet Wiki"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  [
    "Basic understanding of file types",
    "Ability to install open-source software",
  ]
estimated_read_time: "10 minutes"
last_updated: "2026-02-17"
---

# Metadata Management and File Sanitization

What you **don't** see in a file is often more dangerous than what you do see. Every photo, video, and document you create contains hidden "data about data," known as **metadata**.

For Iranian activists and citizens, metadata can reveal the exact GPS location of a protest photo, the unique device ID of the photographer, the time a document was created, and the software used to edit it. Security agencies can use this data to identify and locate individuals even if they use a pseudonym online.

This guide covers how to scrub this invisible data, how to visually redact sensitive information securely, and how to sanitize documents to remove potential malware.

---

## 1. Understanding the Risk

### What is Metadata?

Metadata is information embedded within a file that describes its contents and origin.

- **Images (EXIF):** GPS coordinates, camera model, shutter speed, date/time, and sometimes the device's serial number.
- **Documents (PDF/DOCX):** Author name, editing time, revision history, and software version.
- **Audio/Video:** Location data, device model, and recording timestamps.

### The Threat in Iran

If you share a photo of a protest on Telegram or social media, and that file retains its metadata:

1.  **Geolocation:** Authorities can map exactly where the photo was taken.
2.  **Device Fingerprinting:** If your device is seized later, they can match the unique sensor noise or serial numbers in the metadata to files found on your phone.
3.  **Association:** Document metadata often defaults to the "User Name" of the computer (e.g., "Ali's MacBook"), linking anonymous files to real identities.

---

## 2. Visual Redaction (Blocking Faces and Text)

Before removing hidden data, you must ensure visible data (faces, license plates, sensitive text) is hidden securely.

### ⚠️ Never Use Pixelation or Swirls

**Do not** use standard pixelation (mosaic) or swirl effects to hide text or faces. Artificial Intelligence and de-obfuscation tools can often reverse these effects to reveal the original content.

### Recommended Method: Solid Opaque Blocks

The only secure way to redact information is to cover it with a solid, 100% opaque shape (usually a black box).

### Tools for Secure Redaction

#### Mobile (Android & iOS)

- **Signal (Recommended):** The Signal app has a built-in blur tool that is robust and easy to use.
  - _How to use:_ Open a chat (e.g., "Note to Self") > Tap Camera > Select Photo > Tap the Blur icon (checkered circle) > Toggle "Blur Faces" or draw to blur manually. Save the image without sending if needed.
- **Pocket Paint (Android):** Part of the Catrobat project. Use the "Brush" tool with solid color to paint over details.
- **iOS Markup:** Use the built-in photo editor. Add a shape (square/circle), set the color to black, and ensure the "Fill" is set to solid black (not transparent). **Do not use the highlighter tool.**

#### Desktop (Windows, Linux, macOS)

- **GIMP / Photoshop:** Use the selection tool to highlight the area and fill it with solid black bucket fill.
- **Drawing Tools:** Even MS Paint is effective _if_ you use a solid box. Do not use spray cans or semi-transparent brushes.

---

## 3. Removing Metadata (Scrubbing)

Once the image is visually redacted, you must strip the hidden code.

### Desktop Tools

#### MAT2 (Metadata Anonymisation Toolkit 2)

MAT2 is the gold standard for removing metadata without compromising file integrity. It removes metadata from images, audio, and documents.

- **Platform:** Linux (Native), Windows/macOS (via WSL or Command Line).
- **Features:** Heavily cleans files. Note that it may convert images/documents to varying formats to ensure deep cleaning.
- **Integration:** In Linux (e.g., Tails OS), you can right-click a file and select "Remove metadata."

#### ExifTool

A powerful command-line application for reading, writing, and editing meta information.

- **Platform:** Windows, macOS, Linux.
- **Command to strip all metadata:**
  ```bash
  exiftool -all= filename.jpg
  ```
  _(Note: This creates a backup of the original. Ensure you share the cleaned version.)_

### Mobile Tools

#### Android

- **ExifEraser:** A modern, permissionless app. It supports JPEG, PNG, and WebP. It creates a metadata-free copy of your image.
  - _Source:_ [F-Droid](https://f-droid.org/packages/com.none.tom.exiferaser/) | [Google Play](https://play.google.com/store/apps/details?id=com.none.tom.exiferaser)
- **Scrambled Exif:** An open-source tool. You "share" an image to this app, it scrubs the data, and then prompts you to share the clean image to your destination app (e.g., Telegram/Twitter).
  - _Source:_ [F-Droid](https://f-droid.org/en/packages/com.fasteyez.scrambledexif/)

#### iOS

- **Shortcuts:** You can create or download a privacy shortcut (e.g., "Metadata Stripper") that converts the image and strips metadata before sharing.
- **ViewExif / Metapho:** Apps that allow viewing and removing metadata directly from the Photos app extension.

---

## 4. Document Sanitization with Dangerzone

Journalists and activists often receive PDFs or Office documents that may contain hostile code (malware) designed to infect their computers or "phone home" to reveal the opener's IP address.

**Dangerzone** is a tool that takes a potentially dangerous document, converts it into a safe PDF, and ensures no malware survives.

### How It Works

1.  **Isolation:** It opens the document in a secure, isolated sandbox (a container).
2.  **Pixelation:** It converts the document pages into raw pixel data (images).
3.  **Reconstruction:** It turns those images back into a clean PDF.

Because the final file is reconstructed from visual data, any scripts, macros, or malware embedded in the original code are destroyed.

- **Download:** [dangerzone.rocks](https://dangerzone.rocks/)
- **Use Case:** Always process email attachments (PDF, Word, Excel) through Dangerzone before opening them on your main machine.

---

## 5. Sharing Considerations for Iranian Users

### Telegram: "Photo" vs. "File"

Telegram is the primary communication tool in Iran. You must understand the difference in upload methods:

- **Send as Photo (Default):** Telegram compresses the image. This **usually removes** EXIF metadata (GPS, camera model) as a side effect of compression.
- **Send as File:** Users often send photos as "Files" to preserve quality for evidence. **This preserves all metadata.**
  - **Risk:** If you send a protest photo as a "File" to a journalist or bot, and they are compromised, your GPS location is attached to that file.
  - **Solution:** Always scrub metadata using ExifEraser or MAT2 _before_ sending a photo as a "File."

### Social Media Uploads

Platforms like Instagram and X (Twitter) generally strip metadata when you upload a post publicly. However:

1.  They retain the original data on their servers (which can be subpoenaed).
2.  Direct Messages (DMs) on some platforms may _not_ strip metadata.
3.  **Best Practice:** Always scrub files locally on your device before uploading them anywhere.

---

## 6. Summary Checklist

1.  **Redact Visuals:** Use solid black boxes (Signal Blur or Markup) to hide faces and text. Never use pixelation.
2.  **Scrub Metadata:** Use **ExifEraser** (Android) or **MAT2** (Desktop) to remove GPS and device tags.
3.  **Sanitize Documents:** Run received PDFs/Docs through **Dangerzone** to neutralize malware.
4.  **Disable Geotagging:** Turn off "Location Tags" in your phone's main Camera app settings to prevent data collection at the source.
5.  **Verify:** Before sending a high-risk file, check its properties (Right-click > Properties > Details) to ensure fields like "Camera Maker" and "GPS" are empty.
