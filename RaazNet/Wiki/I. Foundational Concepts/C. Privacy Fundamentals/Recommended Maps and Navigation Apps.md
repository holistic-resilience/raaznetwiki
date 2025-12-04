```yaml
---
title: "Recommended Maps and Navigation Apps"
tags: [privacy, maps, navigation, open-source, offline-maps, location-privacy]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Mobile Users]
topics: ["Privacy Protection", "Mobile Apps", "Navigation", "Location Privacy"]
summary: "Privacy-respecting alternatives to Google Maps and Apple Maps that don't build advertising profiles from your location data."
source: "Privacy Guides"
content_type: "Reference"
security_level: "Informational"
language: "English"
prerequisites: ["Basic smartphone usage"]
estimated_read_time: "4 minutes"
---

# Maps and Navigation

Use a **map and navigation app** that doesn't build an advertising profile based on your searches and location history. Instead of using Google Maps, Apple Maps, or Waze, consider these privacy-respecting alternatives.

The recommendations here do not collect personally identifying information (PII) based on each application's privacy policy. There is **no guarantee** that these privacy policies are honored.

---

## Organic Maps

**Organic Maps** is an open-source, community-developed map display and navigation app for walkers, drivers, and cyclists. The app offers worldwide, offline maps based on OpenStreetMap data, and navigation with privacy—no location tracking, no data collection, and no ads. The app can be used completely offline.

### Features
- Cycling routes, hiking trails, and walking paths
- Turn-by-turn navigation with voice guidance
- Public transport route planning (only available in supported regions and cities)
- Completely offline functionality

### Downloads
- [Google Play](https://play.google.com/store/apps/details?id=app.organicmaps)
- [App Store](https://apps.apple.com/app/organic-maps/id1567437057)
- [GitHub](https://github.com/organicmaps/organicmaps/releases)
- [Linux (Flathub)](https://flathub.org/apps/app.organicmaps.desktop)

### Links
- [Homepage](https://organicmaps.app/)
- [Privacy Policy](https://organicmaps.app/privacy)
- [Source Code](https://github.com/organicmaps/organicmaps)

> **Note:** Organic Maps is a simple, basic app that lacks certain features many users might expect, such as satellite images, street view images, and real-time traffic information.

---

## OsmAnd

**OsmAnd** is an open-source, offline map and navigation application based on OpenStreetMap that offers turn-by-turn navigation for walking, cycling, driving, as well as public transport. See the [OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/OsmAnd#Features) for a detailed overview of supported features.

### Downloads
- [Google Play](https://play.google.com/store/apps/details?id=net.osmand)
- [App Store](https://apps.apple.com/us/app/id934850257)
- [Android APK](https://osmand.net/docs/versions/free-versions)

### Links
- [Homepage](https://osmand.net/)
- [Privacy Policy](https://osmand.net/docs/legal/privacy-policy)
- [Documentation](https://osmand.net/docs/intro)
- [Source Code](https://github.com/osmandapp)

### Privacy Configuration

#### Unique User Identifier (UUID)

OsmAnd generates a [unique user identifier](https://osmand.net/docs/legal/terms-of-use/#6-unique-user-indentifier) for each app install that rotates every three months. The UUID is sent to OsmAnd's servers when downloading maps.

**To disable on Android:**
1. From the home screen, go to **☰ Menu**
2. Select **⚙ Settings** → **⚙ OsmAnd settings** → **Identifiers**
3. Uncheck **Send Unique User Identifier (UUID)**

> This setting is not available on the iOS app.

#### Anonymous Usage Data

The app includes a setting for sharing anonymous data about downloaded maps and feature usage. This is disabled by default on Android but **enabled by default on iOS**.

**To disable on iOS:**
1. Tap **☰** on the home screen
2. Select **⚙ Settings** → **⚙ OsmAnd settings**
3. Uncheck **Send anonymous data**

#### External Data Overlays

OsmAnd allows you to overlay external map data, such as:
- Satellite images from Microsoft
- [Traffic data](https://themm.net/public/osmand_traffic) from Google (not used for automatic route planning)
- Street view images from [Mapillary](https://mapillary.com/) (optional integration)

---

## Selection Criteria

These recommendations are based on objective criteria independent of any affiliation with the projects.

### Minimum Requirements
- Must not collect PII per their privacy policy
- Must not require users to create an account
- Must not require location sharing; if opted in, data must be anonymized
- Must retain core functionality offline and allow map downloads for offline use

### Best-Case Features
- Open-source codebase
- Public transport route planning
- Real-time traffic information for route planning
- Advanced features: detailed POI information, reviews, topographic maps, satellite imagery, and street view

---

*Source: [Privacy Guides](https://www.privacyguides.org/en/maps/)*