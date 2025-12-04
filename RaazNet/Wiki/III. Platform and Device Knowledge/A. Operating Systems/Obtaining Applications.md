---
title: "Obtaining Android Applications Privately"
tags: [android, privacy, app-stores, security, open-source, google-play-alternatives]
category: "Android Security"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Android Users, Security Enthusiasts]
topics: ["Android Apps", "Privacy Protection", "App Installation", "Open Source Software"]
summary: "Guide to obtaining Android apps privately without Google Play Services, covering Obtainium, Aurora Store, GrapheneOS App Store, and F-Droid alternatives."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic Android knowledge", "Understanding of APK files"]
estimated_read_time: "8 minutes"
---

# Obtaining Android Applications Privately

There are many ways to obtain Android apps privately, even from the Play Store, without interacting with Google Play Services. This guide covers recommended methods for obtaining applications on Android, listed in order of preference.

## Obtainium

**Obtainium** is an app manager that allows you to install and update apps directly from the developer's own releases page (GitHub, GitLab, developer websites, etc.) rather than a centralized app store. It supports automatic background updates on Android 12 and higher.

**Resources:**
- [Repository & Documentation](https://github.com/ImranR98/Obtainium)
- [Downloads](https://github.com/ImranR98/Obtainium/releases)

### Security Considerations

Obtainium allows you to download APK installer files from various sources—it's your responsibility to ensure those sources and apps are legitimate. For example:

- **Safe**: Installing Signal from [Signal's official APK page](https://signal.org/android/apk)
- **Risky**: Installing from third-party repositories like Aptoide or APKPure

The risk of installing a malicious *update* is lower because Android verifies that all app updates are signed by the same developer as the existing app on your phone.

## GrapheneOS App Store

GrapheneOS's app store is available on [GitHub](https://github.com/GrapheneOS/Apps/releases). It supports Android 12 and above and can update itself.

The store includes standalone applications built by the GrapheneOS project:
- **Auditor** - Device integrity verification
- **Secure Camera** - Privacy-focused camera app
- **Secure PDF Viewer** - Safe document viewing

These apps are signed with GrapheneOS's own signature that Google cannot access, making this the preferred source over the Play Store for these applications.

## Aurora Store

The Google Play Store requires a Google account, which compromises privacy. Aurora Store provides an alternative.

**Aurora Store** is a Google Play Store client that does not require:
- A Google account
- Google Play Services
- microG

**Resources:**
- [Homepage](https://auroraoss.com/)
- [Downloads](https://gitlab.com/AuroraOSS/AuroraStore/-/releases)

### Limitations

- **Paid apps**: Cannot be downloaded with the anonymous account feature
- **Optional Google login**: You can log in to download purchased apps, but this exposes your installed app list to Google

The benefit remains: you don't need the full Google Play client, Google Play Services, or microG on your device.

## Manual Installation with RSS Notifications

For apps released on GitHub or GitLab, you can add RSS feeds to your news aggregator to track new releases.

### Creating RSS Feeds

**GitHub Example** (Secure Camera):
1. Navigate to the [releases page](https://github.com/GrapheneOS/Camera/releases)
2. Append `.atom` to the URL:
   ```
   https://github.com/GrapheneOS/Camera/releases.atom
   ```

**GitLab Example** (Aurora Store):
1. Navigate to the [project repository](https://gitlab.com/AuroraOSS/AuroraStore)
2. Append `/-/tags?format=atom` to the URL:
   ```
   https://gitlab.com/AuroraOSS/AuroraStore/-/tags?format=atom
   ```

### Verifying APK Fingerprints

When downloading APKs manually, verify their signature using the `apksigner` tool from Android build-tools.

**Setup:**
1. Install [Java JDK](https://oracle.com/java/technologies/downloads)
2. Download [Android Studio command line tools](https://developer.android.com/studio#command-tools)
3. Extract and install build-tools:
   ```bash
   unzip commandlinetools-*.zip
   cd cmdline-tools
   ./bin/sdkmanager --sdk_root=./ "build-tools;29.0.3"
   ```

**Verification:**
```bash
./build-tools/29.0.3/apksigner verify --print-certs ../Camera-37.apk
```

Compare the resulting hashes with another source. Some developers like [Signal publish fingerprints](https://signal.org/android/apk) on their websites.

## F-Droid

> **Recommendation**: Use F-Droid only for apps unavailable through the methods above.

F-Droid is often recommended as a Google Play alternative, offering third-party repositories and dedication to free and open-source software with [reproducible builds](https://f-droid.org/en/docs/Reproducible_Builds) for some applications.

### Security Concerns

However, F-Droid has notable security downsides:

- **Update delays**: Apps in the official repository often fall behind on updates
- **Key signing**: F-Droid maintainers reuse package IDs and sign apps with their own keys, requiring ultimate trust in the F-Droid team
- **Less strict requirements**: More apps that are older, unmaintained, or don't meet [modern security standards](https://developer.android.com/google/play/requirements/target-sdk)

### IzzyOnDroid Repository

The [IzzyOnDroid](https://apt.izzysoft.de/fdroid) repository addresses some concerns:

- Pulls builds directly from code forges (GitHub, GitLab)
- Offers [reproducible builds](https://android.izzysoft.de/articles/named/iod-rbs-mirrors-clients) for hundreds of applications
- Developers verify reproducibility of developer-signed APKs
- Conducts [additional security scans](https://android.izzysoft.de/articles/named/iod-scan-apkchecks)
- Works with developers on privacy improvements

Note: Apps may be [removed from IzzyOnDroid](https://gitlab.com/IzzyOnDroid/repo#are-apps-removed-from-the-repo--and-when-does-that-happen) under certain circumstances.

### Using F-Droid Effectively

The F-Droid and IzzyOnDroid repositories are useful for discovering open-source apps that you can then download through preferred methods (Play Store, Aurora Store, or directly from developers).

**Best practices:**
- Check how frequently apps are updated
- Avoid outdated apps that may rely on unsupported libraries
- Use your best judgment when evaluating new apps

### F-Droid Basic

For apps only distributed through F-Droid (like [Gadgetbridge](https://www.privacyguides.org/en/health-and-wellness/#gadgetbridge)), use [F-Droid Basic](https://f-droid.org/en/packages/org.fdroid.basic) instead of the original F-Droid app.

**Advantages:**
- Supports automatic background updates without privileged extension or root
- Reduced feature set (smaller attack surface)
- Newer, more secure client