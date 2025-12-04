[Skip to content](https://www.privacyguides.org/en/android/obtaining-apps/#obtainium)

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/android/obtaining-apps.md?plain=1 "Edit this page")

# Obtaining Applications

There are many ways to obtain Android apps privately, even from the Play Store, without interacting with Google Play Services. We recommend the following methods of obtaining applications on Android, listed in order of preference.

## Obtainium

![Obtainium logo](https://www.privacyguides.org/en/assets/img/android/obtainium.svg)

**Obtainium** is an app manager which allows you to install and update apps directly from the developer's own releases page (i.e. GitHub, GitLab, the developer's website, etc.), rather than a centralized app store/repository. It supports automatic background updates on Android 12 and higher.

[Repository](https://github.com/ImranR98/Obtainium#readme) [Documentation](https://github.com/ImranR98/Obtainium/wiki "Documentation") [Source Code](https://github.com/ImranR98/Obtainium "Source Code") [Contribute](https://github.com/sponsors/ImranR98 "Contribute")

Downloads

- [GitHub](https://github.com/ImranR98/Obtainium/releases)

Obtainium allows you to download APK installer files from a wide variety of sources, and it is up to you to ensure those sources and apps are legitimate. For example, using Obtainium to install Signal from [Signal's APK landing page](https://signal.org/android/apk) should be fine, but installing from third-party APK repositories like Aptoide or APKPure may pose additional risks. The risk of installing a malicious _update_ is lower, because Android itself verifies that all app updates are signed by the same developer as the existing app on your phone before installing them.

## GrapheneOS App Store

GrapheneOS's app store is available on [GitHub](https://github.com/GrapheneOS/Apps/releases). It supports Android 12 and above and is capable of updating itself. The app store has standalone applications built by the GrapheneOS project such as the [Auditor](https://www.privacyguides.org/en/device-integrity/#auditor-android), [Camera](https://www.privacyguides.org/en/android/general-apps/#secure-camera), and [PDF Viewer](https://www.privacyguides.org/en/android/general-apps/#secure-pdf-viewer). If you are looking for these applications, we highly recommend that you get them from GrapheneOS's app store instead of the Play Store, as the apps on their store are signed by the GrapheneOS's project own signature that Google does not have access to.

## Aurora Store

The Google Play Store requires a Google account to log in, which is not great for privacy. You can get around this by using an alternative client, such as Aurora Store.

![Aurora Store logo](https://www.privacyguides.org/en/assets/img/android/aurora-store.webp)

**Aurora Store** is a Google Play Store client which does not require a Google account, Google Play Services, or microG to download apps.

[Homepage](https://auroraoss.com/) [Privacy Policy](https://gitlab.com/AuroraOSS/AuroraStore/-/blob/master/POLICY.md "Privacy Policy") [Source Code](https://gitlab.com/AuroraOSS/AuroraStore "Source Code")

Downloads

- [GitLab](https://gitlab.com/AuroraOSS/AuroraStore/-/releases)

Aurora Store does not allow you to download paid apps with their anonymous account feature. You can optionally log in with your Google account with Aurora Store to download apps you have purchased, which does give access to the list of apps you've installed to Google. However, you still benefit from not requiring the full Google Play client and Google Play Services or microG on your device.

## Manually with RSS Notifications

For apps that are released on platforms like GitHub and GitLab, you may be able to add an RSS feed to your [news aggregator](https://www.privacyguides.org/en/news-aggregators/) that will help you keep track of new releases.

![RSS APK](https://www.privacyguides.org/en/assets/img/android/rss-apk-light.png#only-light)![RSS APK](https://www.privacyguides.org/en/assets/img/android/rss-apk-dark.png#only-dark)![APK Changes](https://www.privacyguides.org/en/assets/img/android/rss-changes-light.png#only-light)![APK Changes](https://www.privacyguides.org/en/assets/img/android/rss-changes-dark.png#only-dark)

### GitHub

On GitHub, using [Secure Camera](https://www.privacyguides.org/en/android/general-apps/#secure-camera) as an example, you would navigate to its [releases page](https://github.com/GrapheneOS/Camera/releases) and append `.atom` to the URL:

`https://github.com/GrapheneOS/Camera/releases.atom`

### GitLab

On GitLab, using [Aurora Store](https://www.privacyguides.org/en/android/obtaining-apps/#aurora-store) as an example, you would navigate to its [project repository](https://gitlab.com/AuroraOSS/AuroraStore) and append `/-/tags?format=atom` to the URL:

`https://gitlab.com/AuroraOSS/AuroraStore/-/tags?format=atom`

### Verifying APK Fingerprints

If you download APK files to install manually, you can verify their signature with the [`apksigner`](https://developer.android.com/studio/command-line/apksigner) tool, which is a part of Android [build-tools](https://developer.android.com/studio/releases/build-tools).

1. Install [Java JDK](https://oracle.com/java/technologies/downloads).

2. Download the [Android Studio command line tools](https://developer.android.com/studio#command-tools).

3. Extract the downloaded archive:



```
unzip commandlinetools-*.zip
cd cmdline-tools
./bin/sdkmanager --sdk_root=./ "build-tools;29.0.3"
```

4. Run the signature verification command:



```
./build-tools/29.0.3/apksigner verify --print-certs ../Camera-37.apk
```

5. The resulting hashes can then be compared with another source. Some developers such as Signal [show the fingerprints](https://signal.org/android/apk) on their website.



```
Signer #1 certificate DN: CN=GrapheneOS
Signer #1 certificate SHA-256 digest: 6436b155b917c2f9a9ed1d15c4993a5968ffabc94947c13f2aeee14b7b27ed59
Signer #1 certificate SHA-1 digest: 23e108677a2e1b1d6e6b056f3bb951df7ad5570c
Signer #1 certificate MD5 digest: dbbcd0cac71bd6fa2102a0297c6e0dd3
```


## F-Droid

![F-Droid logo](https://www.privacyguides.org/en/assets/img/android/f-droid.svg)

We only recommend F-Droid as a way to obtain apps which cannot be obtained via the means above. F-Droid is often recommended as an alternative to Google Play, particularly within the privacy community. The option to add third-party repositories and not be confined to Google's walled garden has led to its popularity. F-Droid additionally has [reproducible builds](https://f-droid.org/en/docs/Reproducible_Builds) for some applications and is dedicated to free and open-source software. However, there are some security-related downsides to how F-Droid builds, signs, and delivers packages:

Due to their process of building apps, apps in the _official_ F-Droid repository often fall behind on updates. F-Droid maintainers also reuse package IDs while signing apps with their own keys, which is not ideal as it gives the F-Droid team ultimate trust. Additionally, the requirements for an app to be included in the official F-Droid repo are less strict than other app stores like Google Play, meaning that F-Droid tends to host a lot more apps which are older, unmaintained, or otherwise no longer meet [modern security standards](https://developer.android.com/google/play/requirements/target-sdk).

Other popular third-party repositories for F-Droid such as [IzzyOnDroid](https://apt.izzysoft.de/fdroid) alleviate some of these concerns. The IzzyOnDroid repository pulls builds directly from code forges (GitHub, GitLab, etc.) and is the next best thing to the developers' own repositories. They also offer [reproducible builds](https://android.izzysoft.de/articles/named/iod-rbs-mirrors-clients) for hundreds of applications and have developers who verify the reproducibility of developer-signed APKs. Furthermore, the IzzyOnDroid team conducts [additional security scans](https://android.izzysoft.de/articles/named/iod-scan-apkchecks) of apps housed in the repo, which usually result in [deliberations](https://github.com/gouravkhunger/QuotesApp/issues/22) between them and app developers toward privacy improvements in their apps. Note that apps may be removed from the IzzyOnDroid repo in [certain circumstances](https://gitlab.com/IzzyOnDroid/repo#are-apps-removed-from-the-repo--and-when-does-that-happen).

The [F-Droid](https://f-droid.org/en/packages) and [IzzyOnDroid](https://apt.izzysoft.de/fdroid) repositories are home to countless apps, so they can be useful places to search for and discover open-source apps that you can then download through other means such as the Play Store, Aurora Store, or by getting the APK directly from the developer. You should use your best judgment when looking for new apps via this method, and keep an eye on how frequently the app is updated. Outdated apps may rely on unsupported libraries, among other things, posing a potential security risk.

F-Droid Basic

In some rare cases, the developer of an app will only distribute it through F-Droid ( [Gadgetbridge](https://www.privacyguides.org/en/health-and-wellness/#gadgetbridge) is one example of this). If you really need an app like that, we recommend using the newer [F-Droid Basic](https://f-droid.org/en/packages/org.fdroid.basic) client instead of the original F-Droid app to obtain it. F-Droid Basic supports automatic background updates without privileged extension or root, and has a reduced feature set (limiting attack surface).

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).