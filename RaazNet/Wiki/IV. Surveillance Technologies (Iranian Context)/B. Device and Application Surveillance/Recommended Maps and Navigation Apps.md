---
title: "Recommended Maps and Navigation Apps"
tags: [privacy, maps, navigation, open-source, offline-maps, location-privacy]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Mobile Users]
topics: ["Digital Privacy", "Mobile Apps", "Navigation"]
summary: "Privacy-respecting alternatives to Google Maps and Apple Maps that don't track your location or build advertising profiles."
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

**Organic Maps** is an open-source, community-developed map display and navigation app for walkers, drivers, and cyclists. The app offers worldwide, offline maps based on OpenStreetMap data, and navigation with privacy—no location tracking, no data collection, and no ads.

### Key Features
- Completely offline functionality
- Cycling routes, hiking trails, and walking paths
- Turn-by-turn navigation with voice guidance
- Public transport route planning (supported regions only)

### Limitations
- No satellite imagery
- No street view images
- No real-time traffic information

### Download Links
- [Homepage](https://organicmaps.app/) | [Privacy Policy](https://organicmaps.app/privacy) | [Source Code](https://github.com/organicmaps/organicmaps)
- Available on: Google Play, App Store, GitHub, Linux (Flathub)

---

## OsmAnd

**OsmAnd** is an open-source, offline map and navigation application based on OpenStreetMap. It offers turn-by-turn navigation for walking, cycling, driving, and public transport.

For a detailed feature overview, see the [OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/OsmAnd#Features).

### Privacy Configuration

#### Disable Unique User Identifier (Android only)
OsmAnd generates a UUID for each install that rotates every three months, used for internal reports and sent when downloading maps.

**To disable:**
1. From home screen, go to ⚙ **Settings**
2. Select ⚙ **OsmAnd settings** → **Identifiers**
3. Uncheck **Send Unique User Identifier (UUID)**

*Note: This setting is not available on iOS.*

#### Disable Anonymous Data Sharing
This setting is disabled by default on Android but enabled by default on iOS.

**To disable on iOS:**
1. Tap the menu on the home screen
2. Go to ⚙ **Settings** → ⚙ **OsmAnd settings**
3. Uncheck **Send anonymous data**

### Additional Features
- Overlay external map data (satellite images from Microsoft, traffic data from Google)
- Optional Mapillary street view integration

### Download Links
- [Homepage](https://osmand.net/) | [Privacy Policy](https://osmand.net/docs/legal/privacy-policy) | [Documentation](https://osmand.net/docs/intro) | [Source Code](https://github.com/osmandapp)
- Available on: Google Play, App Store, Direct Android download

---

## Selection Criteria

### Minimum Requirements
- Must not collect PII per their privacy policy
- Must not require account creation
- Must not require location sharing; if opted in, data must be anonymized
- Must retain core functionality offline with downloadable maps

### Best-Case Features
- Open-source code
- Public transport route planning
- Real-time traffic information
- Advanced features: POI details/reviews, topographic maps, satellite and street view images