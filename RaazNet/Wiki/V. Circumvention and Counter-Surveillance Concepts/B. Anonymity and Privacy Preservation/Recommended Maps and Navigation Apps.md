```yaml
---
title: "Recommended Maps and Navigation Apps"
tags: [privacy, maps, navigation, open-source, offline-maps, location-privacy]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Mobile Users]
topics: ["Digital Privacy", "Mobile Applications", "Location Privacy"]
summary: "Privacy-respecting alternatives to Google Maps and Apple Maps that don't track your location or build advertising profiles."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic smartphone usage"]
estimated_read_time: "4 minutes"
---
```

# Maps and Navigation

Use a **map and navigation app** that doesn't build an advertising profile based on your searches and location history. Instead of using Google Maps, Apple Maps, or Waze, consider these privacy-respecting alternatives.

The recommendations here do not collect personally identifying information (PII) based on each application's privacy policy. There is **no guarantee** that these privacy policies are honored.

---

## Organic Maps

**Organic Maps** is an open-source, community-developed map display and navigation app for walkers, drivers, and cyclists. The app offers worldwide, offline maps based on OpenStreetMap data, with no location tracking, no data collection, and no ads.

### Key Features

- Offline maps for worldwide use
- Cycling routes, hiking trails, and walking paths
- Turn-by-turn navigation with voice guidance
- Public transport route planning (available in supported regions)
- Completely usable offline

### Limitations

Organic Maps is a simple, basic app that lacks certain features many users might expect, such as:
- Satellite images
- Street view images
- Real-time traffic information

### Download Links

- [Google Play](https://play.google.com/store/apps/details?id=app.organicmaps)
- [App Store](https://apps.apple.com/app/organic-maps/id1567437057)
- [GitHub Releases](https://github.com/organicmaps/organicmaps/releases)
- [Linux (Flathub)](https://flathub.org/apps/app.organicmaps.desktop)

**Resources:** [Homepage](https://organicmaps.app/) | [Privacy Policy](https://organicmaps.app/privacy) | [Source Code](https://github.com/organicmaps/organicmaps)

---

## OsmAnd

**OsmAnd** is an open-source, offline map and navigation application based on OpenStreetMap. It offers turn-by-turn navigation for walking, cycling, driving, and public transport.

For a detailed overview of features, see the [OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/OsmAnd#Features).

### Privacy Configuration

#### Disable Unique User Identifier (Android Only)

OsmAnd generates a [unique user identifier (UUID)](https://osmand.net/docs/legal/terms-of-use/#6-unique-user-indentifier) that rotates every three months. On Android, you can disable sending this UUID:

1. Open the app and tap the menu icon
2. Go to **Settings** → **OsmAnd settings** → **Identifiers**
3. Uncheck **Send Unique User Identifier (UUID)**

> **Note:** This setting is not available on iOS.

#### Disable Anonymous Data Sharing

The app includes a setting for sharing anonymous data about downloaded maps and feature usage. This is disabled by default on Android but **enabled by default on iOS**.

**To disable on iOS:**
1. Tap the menu on the home screen
2. Go to **Settings** → **OsmAnd settings**
3. Uncheck **Send anonymous data**

### Additional Features

OsmAnd allows you to overlay external map data, including:
- Satellite images from Microsoft
- [Traffic data](https://themm.net/public/osmand_traffic) from Google (not used in automatic route planning)
- Street view images via [Mapillary](https://mapillary.com/) integration

### Download Links

- [Google Play](https://play.google.com/store/apps/details?id=net.osmand)
- [App Store](https://apps.apple.com/us/app/id934850257)
- [Android APK](https://osmand.net/docs/versions/free-versions)

**Resources:** [Homepage](https://osmand.net/) | [Privacy Policy](https://osmand.net/docs/legal/privacy-policy) | [Documentation](https://osmand.net/docs/intro) | [Source Code](https://github.com/osmandapp)

---

## Selection Criteria

### Minimum Requirements

- Must not collect PII per their privacy policy
- Must not require users to create an account
- Must not require location sharing; if opted in, data must be anonymized
- Must retain core functionality offline and allow map downloads

### Best-Case Features

- Open source
- Public transport route planning
- Real-time traffic information
- Advanced features: POI information, reviews, topographic maps, satellite/street view images