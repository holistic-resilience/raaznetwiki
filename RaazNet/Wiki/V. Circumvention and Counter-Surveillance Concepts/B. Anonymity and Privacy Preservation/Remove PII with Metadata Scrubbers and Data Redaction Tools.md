[Skip to content](https://www.privacyguides.org/en/data-redaction/#mat2)

![](https://www.privacyguides.org/en/assets/img/cover/data-redaction.webp)

# Data and Metadata Redaction

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/data-redaction.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Public Exposure](https://www.privacyguides.org/en/basics/common-threats/#limiting-public-information)

When sharing files, be sure to remove associated metadata. Image files commonly include [Exif](https://en.wikipedia.org/wiki/Exif) data. Photos sometimes even include GPS coordinates in the file metadata.

Warning

You should **never** use blur to redact [text in images](https://bishopfox.com/blog/unredacter-tool-never-pixelation). If you want to redact text in an image, you should draw a box over the text.

## MAT2

![MAT2 logo](https://www.privacyguides.org/en/assets/img/data-redaction/mat2.svg)

**MAT2** is free, cross-platform software which allows you to remove metadata from image, audio, torrent, and document file types. It provides both a command line tool and a graphical user interface via an extension for [Dolphin](https://github.com/jvoisin/mat2/tree/master/dolphin), the default file manager of [KDE](https://kde.org/).

[Repository](https://github.com/jvoisin/mat2#readme) [Documentation](https://github.com/jvoisin/mat2#how-to-use-mat2 "Documentation") [Source Code](https://github.com/jvoisin/mat2 "Source Code")

Downloads

- [Windows](https://pypi.org/project/mat2)
- [macOS](https://github.com/jvoisin/mat2#requirements-setup-on-macos-os-x-using-homebrew)
- [Linux](https://pypi.org/project/mat2)
- [Web](https://github.com/jvoisin/mat2#web-interface)

## ExifEraser (Android)

![ExifEraser logo](https://www.privacyguides.org/en/assets/img/data-redaction/exiferaser.svg)

**ExifEraser** is a modern, permissionless image metadata erasing application for Android.

It currently supports JPEG, PNG, and WebP files.

[Repository](https://github.com/Tommy-Geenexus/exif-eraser#readme) [Documentation](https://github.com/Tommy-Geenexus/exif-eraser#description "Documentation") [Source Code](https://github.com/Tommy-Geenexus/exif-eraser "Source Code")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.none.tom.exiferaser)
- [Accrescent](https://accrescent.app/app/com.none.tom.exiferaser)
- [GitHub](https://github.com/Tommy-Geenexus/exif-eraser/releases)

The metadata that is erased depends on the image's file type:

- **JPEG**: ICC Profile, Exif, Photoshop Image Resources and XMP/ExtendedXMP metadata will be erased if it exists.
- **PNG**: ICC Profile, Exif and XMP metadata will be erased if it exists.
- **WebP**: ICC Profile, Exif and XMP metadata will be erased if it exists.

After processing the images, ExifEraser provides you with a full report about what exactly was removed from each image.

The app offers multiple ways to erase metadata from images. Namely:

- You can share an image from another application with ExifEraser.
- Through the app itself, you can select a single image, multiple images at once, or even an entire directory.
- It features a "Camera" option, which uses your operating system's camera app to take a photo, and then it removes the metadata from it.
- It allows you to drag photos from another app into ExifEraser when they are both open in split-screen mode.
- Lastly, it allows you to paste an image from your clipboard.

## Shortcuts (iOS & macOS)

On iOS and macOS, you can remove image metadata without using any third-party apps by creating a [**shortcut**](https://apps.apple.com/app/id915249334) for this purpose. Here is an example shortcut you can download to use as is:

[Clean Image Metadata](https://icloud.com/shortcuts/fb774ddb7b5b4296871776c67ac0fff9)

You can also use it as a model for your own shortcut; just make sure that the **Preserve Metadata** option under the **Convert** action is unchecked. Once added, you can access the shortcut in the share sheet that appears when you select the  Share button. You can select multiple images and invoke the shortcut to remove their metadata all at once.

This shortcut removes metadata such as location, device model, lens model, and other camera information. It also sets the image creation date to the time the shortcut was used.

## ExifTool (CLI)

![ExifTool logo](https://www.privacyguides.org/en/assets/img/data-redaction/exiftool.png)

**ExifTool** is the original Perl library and command-line application for reading, writing, and editing meta information (Exif, IPTC, XMP, and more) in a wide variety of file formats (JPEG, TIFF, PNG, PDF, RAW, and more).

It is often a component of other Exif removal applications and in most Linux distribution repositories.

[Homepage](https://exiftool.org/) [Documentation](https://exiftool.org/faq.html "Documentation") [Source Code](https://github.com/exiftool/exiftool "Source Code") [Contribute](https://exiftool.org/#donate "Contribute")

Downloads

- [Windows](https://exiftool.org/)
- [macOS](https://exiftool.org/)
- [Linux](https://exiftool.org/)

Deleting data from a directory of files

```
exiftool -all= *.file_extension
```

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

- Apps developed for open-source operating systems must be open source.
- Apps must be free and should not include ads or other limitations.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).