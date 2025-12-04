[Skip to content](https://www.privacyguides.org/en/android/general-apps/#shelter)

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/android/general-apps.md?plain=1 "Edit this page")

# General Apps

Protects against the following threat(s):

- [Passive Attacks](https://www.privacyguides.org/en/basics/common-threats/#security-and-privacy)

We recommend a wide variety of Android apps throughout this site. The apps listed here are Android-exclusive and specifically enhance or replace key system functionality.

### Shelter

If your device is on Android 15 or greater, we recommend using the native [Private Space](https://www.privacyguides.org/en/os/android-overview/#private-space) feature instead, which provides nearly the same functionality without needing to place trust in and grant powerful permissions to a third-party app.

![Shelter logo](https://www.privacyguides.org/en/assets/img/android/shelter.svg)

**Shelter** is an app that helps you leverage Android's Work Profile functionality to isolate or duplicate apps on your device.

Shelter supports blocking contact search cross profiles and sharing files across profiles via the default file manager ( [DocumentsUI](https://source.android.com/devices/architecture/modular-system/documentsui)).

[Repository](https://gitea.angry.im/PeterCxy/Shelter#shelter) [Source Code](https://gitea.angry.im/PeterCxy/Shelter "Source Code") [Contribute](https://patreon.com/PeterCxy "Contribute")

Warning

When using Shelter, you are placing complete trust in its developer, as Shelter acts as a [Device Admin](https://developer.android.com/guide/topics/admin/device-admin) to create the Work Profile, and it has extensive access to the data stored within the Work Profile.

Shelter is recommended over [Insular](https://secure-system.gitlab.io/Insular) and [Island](https://github.com/oasisfeng/island) as it supports [contact search blocking](https://secure-system.gitlab.io/Insular/faq.html).

### Secure Camera

Protects against the following threat(s):

- [Public Exposure](https://www.privacyguides.org/en/basics/common-threats/#limiting-public-information)

![Secure camera logo](https://www.privacyguides.org/en/assets/img/android/secure_camera.svg#only-light)![Secure camera logo](https://www.privacyguides.org/en/assets/img/android/secure_camera-dark.svg#only-dark)

**Secure Camera** is a camera app focused on privacy and security which can capture images, videos, and QR codes. CameraX vendor extensions (Portrait, HDR, Night Sight, Face Retouch, and Auto) are also supported on available devices.

[Repository](https://github.com/GrapheneOS/Camera#readme) [Documentation](https://grapheneos.org/usage#camera "Documentation") [Source Code](https://github.com/GrapheneOS/Camera "Source Code") [Contribute](https://grapheneos.org/donate "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=app.grapheneos.camera.play)
- [GitHub](https://github.com/GrapheneOS/Camera/releases)
- [GrapheneOS App Store](https://github.com/GrapheneOS/Apps/releases)

Main privacy features include:

- Auto removal of [Exif](https://en.wikipedia.org/wiki/Exif) metadata (enabled by default)
- Use of the new [Media](https://developer.android.com/training/data-storage/shared/media) API, therefore [storage permissions](https://developer.android.com/training/data-storage) are not required
- Microphone permission not required unless you want to record sound

Note

Metadata is not currently deleted from video files, but that is planned.

The image orientation metadata is not deleted. If you enable location (in Secure Camera) that **won't** be deleted either. If you want to delete that later you will need to use an external app such as [ExifEraser](https://www.privacyguides.org/en/data-redaction/#exiferaser-android).

### Secure PDF Viewer

Protects against the following threat(s):

- [Targeted Attacks](https://www.privacyguides.org/en/basics/common-threats/#attacks-against-specific-individuals)

![Secure PDF Viewer logo](https://www.privacyguides.org/en/assets/img/android/secure_pdf_viewer.svg#only-light)![Secure PDF Viewer logo](https://www.privacyguides.org/en/assets/img/android/secure_pdf_viewer-dark.svg#only-dark)

**Secure PDF Viewer** is a PDF viewer based on [pdf.js](https://en.wikipedia.org/wiki/PDF.js) that doesn't require any permissions. The PDF is fed into a [sandboxed](https://en.wikipedia.org/wiki/Sandbox_(software_development)) [WebView](https://developer.android.com/guide/webapps/webview). This means that it doesn't require permission directly to access content or files.

[Content-Security-Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) is used to enforce that the JavaScript and styling properties within the WebView are entirely static content.

[Repository](https://github.com/GrapheneOS/PdfViewer#readme) [Source Code](https://github.com/GrapheneOS/PdfViewer "Source Code") [Contribute](https://grapheneos.org/donate "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=app.grapheneos.pdfviewer.play)
- [GitHub](https://github.com/GrapheneOS/PdfViewer/releases)
- [GrapheneOS App Store](https://github.com/GrapheneOS/Apps/releases)

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

- Applications on this page must not be applicable to any other software category on the site.
- General applications should extend or replace core system functionality.
- Applications should receive regular updates and maintenance.

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).