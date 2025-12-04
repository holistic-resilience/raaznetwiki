---
title: "Obtaining Android Applications Privately"
tags: [android, privacy, app-stores, security, open-source]
category: "Mobile Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Android Users, Security Enthusiasts]
topics: ["Android Security", "App Installation", "Privacy Protection", "Open Source Software"]
summary: "Guide to obtaining Android apps privately without Google Play Services, covering Obtainium, Aurora Store, GrapheneOS App Store, and F-Droid alternatives."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic Android knowledge", "Understanding of APK installation"]
estimated_read_time: "8 minutes"
---

# Obtaining Android Applications Privately

There are many ways to obtain Android apps privately, even from the Play Store, without interacting with Google Play Services. The following methods are listed in order of preference.

## Obtainium

**Obtainium** is an app manager that allows you to install and update apps directly from the developer's own releases page (GitHub, GitLab, developer websites, etc.) rather than a centralized app store. It supports automatic background updates on Android 12 and higher.

**Resources:**
- [Repository & Documentation](https://github.com/ImranR98/Obtainium)
- [Downloads](https://github.com/ImranR98/Obtainium/releases)

### Security Considerations

Obtainium downloads APK installer files from various sources—it's your responsibility to ensure those sources and apps are legitimate. For example:

- **Safe:** Installing Signal from [Signal's official APK page](https://signal.org/android/apk)
- **Risky:** Installing from third-party APK repositories like Aptoide or APKPure

The risk of installing a malicious *update* is lower because Android verifies that all app updates are signed by the same developer as the existing app on your phone.

## GrapheneOS App Store

GrapheneOS's app store is available on [GitHub](https://github.com/GrapheneOS/Apps/releases). It supports Android 12 and above and can update itself.

The store contains standalone applications built by the GrapheneOS project:
- **Auditor** - Device integrity verification
- **Camera** - Secure camera application
- **PDF Viewer** - Secure document viewer

These apps are signed with GrapheneOS's own signature that Google does not have access to, making it preferable to the Play Store for these specific applications.

## Aurora Store

The Google Play Store requires a Google account, which is not ideal for privacy. Aurora Store provides an alternative.

**Aurora Store** is a Google Play Store client that does not require a Google account, Google Play Services, or microG to download apps.

**Resources:**
- [Homepage](https://auroraoss.com/)
- [Privacy Policy](https://gitlab.com/AuroraOSS/AuroraStore/-/blob/master/POLICY.md)
- [Downloads](https://gitlab.com/AuroraOSS/AuroraStore/-/releases)

### Limitations

- **Paid apps:** Cannot be downloaded with the anonymous account feature
- **Optional Google login:** You can log in with your Google account to access purchased apps, which gives Google access to your installed apps list—but you still avoid requiring full Google Play Services on your device

## Manual Installation with RSS Notifications

For apps released on platforms like GitHub and GitLab, you can add an RSS feed to your news aggregator to track new releases.

### GitHub RSS Feeds

Navigate to the app's releases page and append `.atom` to the URL:

```
https://github.com/GrapheneOS/Camera/releases.atom
```

### GitLab RSS Feeds

Navigate to the project repository and append `/-/tags?format=atom` to the URL:

```
https://gitlab.com/AuroraOSS/AuroraStore/-/tags?format=atom
```

### Verifying APK Fingerprints

When downloading APKs manually, verify their signature with the `apksigner` tool from Android build-tools:

1. Install [Java JDK](https://oracle.com/java/technologies/downloads)

2. Download the [Android Studio command line tools](https://developer.android.com/studio#command-tools)

3. Extract and install build-tools:
   ```bash
   unzip commandlinetools-*.zip
   cd cmdline-tools
   ./bin/sdkmanager --sdk_root=./ "build-tools;29.0.3"
   ```

4. Verify the APK:
   ```bash
   ./build-tools/29.0.3/apksigner verify --print-certs ../Camera-37.apk
   ```

5. Compare the resulting hashes with another source. Some developers like Signal [publish fingerprints](https://signal.org/android/apk) on their website.

## F-Droid

F-Droid is recommended only when apps cannot be obtained through the methods above.

While F-Droid is popular in the privacy community for its third-party repository support and dedication to free and open-source software, there are security-related downsides:

### Concerns with Official F-Droid Repository

- **Delayed updates:** Apps often fall behind on updates due to the build process
- **Key management:** F-Droid maintainers reuse package IDs while signing apps with their own keys, giving the F-Droid team significant trust
- **Less strict requirements:** The repository tends to host older, unmaintained apps that may not meet modern security standards

### IzzyOnDroid Repository

The [IzzyOnDroid](https://apt.izzysoft.de/fdroid) repository addresses some concerns:

- Pulls builds directly from code forges (GitHub, GitLab)
- Offers [reproducible builds](https://android.izzysoft.de/articles/named/iod-rbs-mirrors-clients) for hundreds of applications
- Conducts [additional security scans](https://android.izzysoft.de/articles/named/iod-scan-apkchecks)
- Works with developers to improve app privacy

### Using F-Droid Wisely

Both F-Droid and IzzyOnDroid repositories can be useful for:
- **Discovery:** Finding open-source apps to then download through other means (Play Store, Aurora Store, or directly from developers)
- **Research:** Identifying alternatives to proprietary applications

When evaluating apps, check how frequently they're updated. Outdated apps may rely on unsupported libraries, posing security risks.

### F-Droid Basic

For apps distributed exclusively through F-Droid (like Gadgetbridge), use [F-Droid Basic](https://f-droid.org/en/packages/org.fdroid.basic) instead of the original F-Droid app:

- Supports automatic background updates without privileged extension or root
- Reduced feature set limits attack surface
- Better security posture than the full F-Droid client