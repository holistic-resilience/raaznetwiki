---
title: "Metadata Scrubbing and Media Redaction"
tags:
  [
    privacy,
    metadata,
    exif,
    redaction,
    anonymity,
    protests,
    digital-security,
    iran-security,
  ]
category: "Data Management"
difficulty: "Intermediate"
audience: [Activists, Journalists, Protesters, General Public]
topics:
  [
    "Metadata Removal",
    "Visual Redaction",
    "Digital Anonymity",
    "Protest Safety",
  ]
summary: "A comprehensive guide to removing invisible metadata and securely obscuring visual identifiers in photos and videos to protect identities in Iran."
source: "Raaznet Aggregation"
content_type: "Guide"
security_level: "High"
language: "English"
prerequisites:
  ["Basic understanding of file types", "Access to F-Droid or App Store"]
estimated_read_time: "12 minutes"
---

# Metadata Scrubbing and Media Redaction

Sharing a photo or video is never just about the visual content. Every digital file carries hidden data called **metadata** (EXIF data) that can reveal your exact GPS location, device model, time of capture, and unique device ID. Furthermore, visual details—faces, tattoos, street signs—can be used by security forces to identify protesters and activists.

This guide details how to rigorously "scrub" (remove) this hidden data and "redact" (obscure) visual identifiers before sharing any media.

## Part 1: Visual Redaction (Obscuring Faces & Identifiers)

Simply cropping a photo is often insufficient. Security agencies use advanced reconstruction techniques and cross-referencing to identify individuals.

### ⚠️ The Danger of Pixelation and Blurring

**Do not use standard "blur" or "pixelate" filters found in basic editors.**
AI tools can often "de-pixelate" or reverse-engineer these effects to reveal the original image.

- **Bad:** Pixelation, semi-transparent highlighters, standard blurs.
- **Good:** Solid opaque shapes (black boxes), stickers, or specialized cryptographic blurring tools.

### Recommended Tools

#### 1. Signal Messenger (Android & iOS)

The safest and most accessible tool for quick redaction in the field.

- **How to use:** Open Signal > Tap Camera icon > Take or select photo > Tap the **Blur** tool (checkered circle icon).
- **Features:** "Blur Faces" toggle (automatic) and manual swipe to blur.
- **Workflow:** Edit the photo in Signal, save it to your device, and _then_ share it. Do not rely on the app's transport encryption alone if you plan to export the file later.

#### 2. PutMask (Android)

Ideal for videos. Manually blurring moving faces in a video frame-by-frame is difficult; PutMask automates this.

- **Features:** Automatically detects and tracks faces in videos to apply a secure blur.
- **Download:** Available on [Google Play](https://play.google.com/store/apps/details?id=com.putmask.facefilter) or via **Aurora Store** (for anonymous download in Iran).

#### 3. ObscuraCam (Android - Legacy)

Developed by the Guardian Project. While older, it remains a valid offline tool for "crowd blurring."

- **Download:** [F-Droid](https://f-droid.org/packages/org.witness.sscphase1/).

#### 4. Built-in "Markup" (iOS)

If you cannot install apps, use the native iOS editor **carefully**.

- **Method:** Open Photo > Edit > Markup (pen tip icon) > Plus (+) symbol > Square/Circle.
- **Critical Step:** Tap the shape icon (bottom left) to make it a **solid, filled shape** (not just an outline). Place this solid shape over faces/tattoos. **Never** use the "highlighter" or "pen" tool to scribble over text; it is transparent and can be adjusted to reveal the content.

#### 5. Shotcut (Desktop - Windows/Linux/macOS)

For high-quality video redaction (e.g., blurring a license plate or face in a long clip).

- **Download:** [Shotcut.org](https://shotcut.org/)
- **Technique:** Use the "Blur: Pad" or "Mosaic" filter with keyframes to track moving subjects.

---

## Part 2: Metadata Scrubbing (Removing Invisible Data)

Metadata allows authorities to map your network. A photo taken at a protest in Tehran contains GPS coordinates that place you at the scene, even if your face is covered.

### Android Tools

#### 1. Scrambled Exif (Recommended)

Free, open-source (FOSS), and lightweight. It requires no interface; it works via the "Share" menu.

- **Download:** [F-Droid](https://f-droid.org/packages/com.jarsilio.android.scrambledeggsif/).
- **Workflow:**
  1.  Go to your Gallery.
  2.  Select the photo(s).
  3.  Tap **Share** and select **Scrambled Exif**.
  4.  The app scrubs the data and immediately opens the "Share" menu again for you to send the _clean_ file to Telegram, Signal, or save it.

#### 2. ExifEraser

A robust alternative that supports JPEG, PNG, and WebP.

- **Download:** [Google Play](https://play.google.com/store/apps/details?id=com.none.tom.exiferaser) or Aurora Store.
- **Features:** Detailed reports on exactly what data was removed (ICC Profile, Photoshop resources, GPS).

### iOS Tools

#### 1. iOS Shortcuts (Built-in)

You can create or download a "Shortcut" to strip metadata without third-party apps.

- **Setup:** Open the "Shortcuts" app > Create New > Add Action "Convert Image" (set to JPEG, uncheck "Preserve Metadata") > Add Action "Save to Photo Album".
- **Download:** Pre-made shortcuts like "Metadata Remover" are often available in the Gallery.

#### 2. ViewExif

Allows you to view metadata directly in the Photos app and share a version without it.

### Desktop Tools (Windows / Linux / macOS)

#### 1. MAT2 (The Gold Standard)

**MAT2** (Metadata Anonymisation Toolkit 2) is the industry standard for removing metadata from a wide range of files (images, audio, office documents).

- **Platform:** Linux (CLI/GUI), installable on Windows via WSL.
- **Usage (CLI):** `mat2 --inplace file.jpg`
- **Note:** MAT2 is superior because it scrubs deeper than standard tools, handling watermarks and obscure tags.

#### 2. ExifCleaner

A user-friendly graphical interface (GUI) for desktop users.

- **Download:** [ExifCleaner GitHub](https://github.com/szlldm/ExifCleaner).
- **Usage:** Drag and drop files into the window. It supports batch processing for hundreds of photos at once.

#### 3. ExifTool (Advanced)

The most powerful command-line tool for reading and writing metadata.

- **Command:** `exiftool -all= *.jpg` (Deletes all metadata from all JPGs in the folder).

---

## Part 3: Operational Security for Iranian Users

### The "Capture vs. Share" Strategy

In high-risk environments like protests (e.g., Valiasr Square, Tehran University), your device is evidence.

1.  **Prevention:**
    - **Disable GPS:** Turn off "Location Tags" in your camera settings _before_ leaving home.
    - **Use a "Burner" Camera App:** Use [Open Camera](https://f-droid.org/packages/net.sourceforge.opencamera/) (from F-Droid) and explicitly ensure all metadata saving options are disabled.

2.  **The "Runner" Workflow:**
    - If recording sensitive footage, do not keep it on your primary phone.
    - Use a device with a removable SD card.
    - Pass the SD card to a "runner" (someone not on the front lines) to take it to a safe location for scrubbing and uploading.

3.  **Social Media Hygiene:**
    - **Warning:** While platforms like Instagram and Telegram often strip metadata from _displayed_ images, they may retain the original file with full data on their servers. If the platform cooperates with authorities or is breached, your data is exposed.
    - **Rule:** Always scrub metadata locally on your device _before_ uploading to any cloud or social platform.

4.  **SSDs and Wear Leveling:**
    - If you are scrubbing files on a computer with an SSD (Solid State Drive), simply deleting the metadata and saving the file _might_ leave the original version in the drive's memory due to "wear leveling."
    - **Solution:** Scrub the file, save it to a veracrypt-encrypted container or a RAM disk, and then securely wipe the free space of the drive if possible. For most users, using **Scrambled Exif** on Android before saving to disk is the safest mobile workflow.

### Quick Reference Checklist

| Task                | Recommended Tool (Mobile) | Recommended Tool (Desktop)     |
| :------------------ | :------------------------ | :----------------------------- |
| **Blur Faces**      | Signal (Blur Tool)        | Shotcut (Video) / GIMP (Photo) |
| **Remove GPS/Exif** | Scrambled Exif (Android)  | MAT2 or ExifCleaner            |
| **Verify Removal**  | ExifTool (Android Port)   | ExifTool (CLI)                 |
| **App Source**      | F-Droid / Aurora Store    | Official GitHub Repos          |
