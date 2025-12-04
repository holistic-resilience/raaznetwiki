---
title: "Obtaining Android Applications Privately"
tags: [android, privacy, app-stores, open-source, security]
category: "Android Privacy"
difficulty: "Intermediate"
audience: [Privacy-Conscious Users, Android Users, Security Enthusiasts]
topics: ["App Installation", "Privacy Protection", "Android Security"]
summary: "Guide to obtaining Android apps privately without Google Play Services, covering Obtainium, Aurora Store, F-Droid, and manual methods."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic Android knowledge", "Understanding of app installation"]
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

- **Safe:** Installing Signal from [Signal's APK landing page](https://signal.org/android/apk)
- **Risky:** Installing from third-party APK repositories like Aptoide or APKPure

> **Note:** The risk of installing a malicious update is lower because Android verifies that all app updates are signed by the same developer as the existing app on your phone.

## GrapheneOS App Store

GrapheneOS's app store is available on [GitHub](https://github.com/GrapheneOS/Apps/releases). It supports Android 12 and above and can update itself.

The store includes standalone applications built by the GrapheneOS project:
- **Auditor** - Device integrity verification
- **Camera** - Secure camera application
- **PDF Viewer** - Secure document viewer

These apps are signed with GrapheneOS's own signature that Google does not have access to, making this the preferred source over the Play Store.

## Aurora Store

The Google Play Store requires a Google account, which is problematic for privacy. Aurora Store provides an alternative.

**Aurora Store** is a Google Play Store client that does not require:
- A Google account
- Google Play Services
- microG

**Resources:**
- [Homepage](https://auroraoss.com/)
- [Downloads](https://gitlab.com/AuroraOSS/AuroraStore/-/releases)

### Limitations

- **Paid apps:** Cannot be downloaded with the anonymous account feature
- **Optional Google login:** You can log in to download purchased apps, but this gives Google access to your installed apps list. You still benefit from not requiring the full Google Play client on your device.

## Manual Installation with RSS Notifications

For apps released on platforms like GitHub and GitLab, you can add an RSS feed to your news aggregator to track new releases.

### GitHub RSS Feeds

Navigate to the releases page and append `.atom` to the URL:

```
https://github.com/GrapheneOS/Camera/releases.atom
```

### GitLab RSS Feeds

Navigate to the project repository and append `/-/tags?format=atom` to the URL:

```
https://gitlab.com/AuroraOSS/AuroraStore/-/tags?format=atom
```

### Verifying APK Fingerprints

When downloading APKs manually, verify their signature with the `apksigner` tool:

1. Install [Java JDK](https://oracle.com/java/technologies/downloads)

2. Download [Android Studio command line tools](https://developer.android.com/studio#command-tools)

3. Extract and install build tools:
   ```bash
   unzip commandlinetools-*.zip
   cd cmdline-tools
   ./bin/sdkmanager --sdk_root=./ "build-tools;29.0.3"
   ```

4. Verify the APK:
   ```bash
   ./build-tools/29.0.3/apksigner verify --print-certs ../Camera-37.apk
   ```

5. Compare the resulting hashes with another source. Some developers like [Signal](https://signal.org/android/apk) publish fingerprints on their website.

## F-Droid

**Recommendation:** Only use F-Droid for apps that cannot be obtained through the methods above.

F-Droid is often recommended as a Google Play alternative, particularly in the privacy community. It offers:
- Third-party repository support
- [Reproducible builds](https://f-droid.org/en/docs/Reproducible_Builds) for some applications
- Dedication to free and open-source software

### Security Concerns

However, there are security-related downsides:

1. **Delayed updates:** Apps in the official F-Droid repository often fall behind on updates
2. **Signing practices:** F-Droid maintainers reuse package IDs and sign apps with their own keys, giving the F-Droid team significant trust
3. **Inclusion standards:** Requirements are less strict than Google Play, resulting in older, unmaintained apps that may not meet [modern security standards](https://developer.android.com/google/play/requirements/target-sdk)

### IzzyOnDroid Repository

The [IzzyOnDroid](https://apt.izzysoft.de/fdroid) repository alleviates some concerns:

- Pulls builds directly from code forges (GitHub, GitLab)
- Offers [reproducible builds](https://android.izzysoft.de/articles/named/iod-rbs-mirrors-clients) for hundreds of applications
- Developers verify reproducibility of developer-signed APKs
- Conducts [additional security scans](https://android.izzysoft.de/articles/named/iod-scan-apkchecks) of apps

> **Tip:** Use F-Droid and IzzyOnDroid as discovery tools to find open-source apps, then download through other means such as the Play Store, Aurora Store, or directly from the developer.

### F-Droid Basic

In rare cases where an app is only distributed through F-Droid (e.g., Gadgetbridge), use [F-Droid Basic](https://f-droid.org/en/packages/org.fdroid.basic) instead of the original F-Droid app.

**Advantages:**
- Automatic background updates without privileged extension or root
- Reduced feature set (limiting attack surface)

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/android/obtaining-apps/)*