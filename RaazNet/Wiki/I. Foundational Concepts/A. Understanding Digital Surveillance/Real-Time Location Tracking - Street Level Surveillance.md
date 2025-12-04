---
title: "Real-Time Location Tracking"
tags: [location-tracking, surveillance, data-brokers, fourth-amendment, mobile-privacy, law-enforcement]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Digital Surveillance", "Privacy Protection", "Civil Liberties", "Law Enforcement Technology"]
summary: "EFF guide explaining how law enforcement purchases mobile location data from brokers to track individuals, bypassing warrant requirements."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of mobile devices", "Familiarity with privacy concepts"]
estimated_read_time: "10 minutes"
---

# Real-Time Location Tracking

[Real-time mobile location tracking](https://www.eff.org/issues/location-data-brokers) enables law enforcement to monitor individuals' movements over time. Most people carry cell phones that capture location information through apps and the advertising ecosystem. In recent years, law enforcement has gained access to this data by [purchasing it from data brokers](https://apnews.com/article/technology-police-government-surveillance-d395409ef5a8c6c3f6cdab5b1d0e27ef), providing often real-time access to millions of individuals' locations—including those with no connection to criminal activity.

## How It Works

### The Advertising-to-Surveillance Pipeline

[Online advertising](https://www.eff.org/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech) requires companies to know who you are and what you like. Your online behavior and location become linked to your identity through regular collection, purchase, and sale by advertisers and private companies.

Common apps that request location access include:
- Weather apps
- Navigation apps
- Coupon apps
- "Family safety" apps

Once an app gains location access, it can share that data with virtually anyone—including police.

### Software Development Kits (SDKs)

Data brokers incentivize app developers with cash-for-data deals, often paying per user for direct device access. Developers integrate location broker SDKs into their apps, which then gather data whenever the app has access:

- **Foreground access**: Data collected when the app is open
- **Background access**: Data collected whenever the phone is on, even with the app closed

### Ad-ID Tracking

Applications typically require users to grant "permission" for location and data collection. [This information links to your Ad-ID](https://www.eff.org/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech)—a unique identifier connecting you, your online behavior, and location across devices, applications, and websites.

This sensitive information is regularly sold to entities beyond the original application, and [law enforcement now purchases it](https://www.eff.org/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech) from data brokers.

## How Law Enforcement Uses It

Real-time mobile location data serves both federal agencies and local police departments.

### Federal and Military Use

Military and foreign intelligence agencies have deployed location data in multiple instances:

- [In one unclassified project](https://www.wsj.com/articles/academic-project-used-marketing-data-to-monitor-russian-military-sites-11595073601), Mississippi State University researchers used Locate X data to track movements around Russian missile test sites, including high-level diplomats
- The U.S. Army funded the project, noting "good potential use" while claiming consistency with Army policy as long as no "personal characteristics" were collected—despite detailed movement data being inherently personal

### State and Local Use

State and local law enforcement [use purchased location data](https://www.eff.org/press/releases/data-broker-helps-police-see-everywhere-youve-been-click-mouse-eff-investigation) through two primary methods:

1. **Device tracking**: Identifying a specific device and following its location through time and space
2. **Geofencing**: Drawing a virtual "fence" around a real-world area to identify all devices (and individuals) within it

Geofencing can target any location law enforcement deems relevant, including:
- Protests
- Places of worship
- Reproductive health clinics

## Who Sells It

Location data comes from [numerous data brokers](https://www.eff.org/deeplinks/2022/06/how-federal-government-buys-our-cell-phone-location-data) that either collect information directly via SDKs or acquire it from other brokers and applications.

### Key Vendors

**Fog Data Science**
- Specializes in selling location data to law enforcement
- Claims to be the only company providing this access without requiring additional platform purchases

**Venntel**
- Subsidiary of Gravy Analytics
- Appears to provide data underlying Fog Data's services
- [Known government clients](https://www.wired.com/story/dhs-surveillance-phone-tracking-data/) include:
  - Internal Revenue Service (IRS)
  - Department of Homeland Security (DHS)
  - Immigration and Customs Enforcement (ICE)
  - Customs and Border Protection (CBP)
  - Drug Enforcement Administration (DEA)
  - Federal Bureau of Investigation (FBI)
- Acquires all data indirectly through other brokers rather than embedding SDKs directly

**Other Vendors**
- [Locate X](https://www.protocol.com/government-buying-location-data)
- [Veraset](https://www.eff.org/deeplinks/2021/11/data-broker-veraset-gave-bulk-device-level-gps-data-dc-government)
- [Cobwebs Technologies](https://cobwebs.com/en/law-enforcement/) – [integrates real-time location data](https://theintercept.com/2023/07/26/texas-phone-tracking-border-surveillance/) with intelligence analysis for police operations

## Constitutional and Privacy Threats

### Fourth Amendment Concerns

Purchasing mobile location data [undermines Fourth Amendment rights](https://www.eff.org/deeplinks/2020/12/law-enforcement-purchasing-commercially-available-geolocation-data) and circumvents regulations on government tracking.

The Fourth Amendment generally requires police to obtain a warrant before searching a location or person. In 2018, the Supreme Court ruled in *[Carpenter v. United States](https://www.eff.org/cases/carpenter-v-united-states)* that police must get a warrant before obtaining historical cell site location information (CSLI), which creates "a detailed chronicle of a person's physical presence compiled every day, every moment over years."

### How Data Broker Access Exceeds Warrant Scope

With commercial data broker access, federal agencies can:
- Query data about millions or billions of identifiable people simultaneously
- Access data without limitation to a single area or time slice
- Start from one time and place, then look forwards or backwards at hundreds of devices' location histories
- Learn where device owners live, work, and travel
- Make extraordinarily broad queries spanning entire states or countries
- Filter resulting data however they choose

This appears to match the DHS's 2018 Venntel deal, stretching the Fourth Amendment's particularity requirement beyond recognition.

### Comparison to Carpenter

Fog's "device search" feature often provides more detailed chronicles than the CSLI in *Carpenter v. United States*:

| Case | Data Points | Time Span |
|------|-------------|-----------|
| *Carpenter* (MetroPCS/Sprint) | 12,898 | 127 days |
| Missouri case (Fog Data) | 47,394 | 163 days |

Records from [Iowa Department of Public Safety](https://www.documentcloud.org/documents/22187960-iowa-dps_20210312_ad-id-lookup) and [Broward County, Florida](https://www.documentcloud.org/documents/22187525-broward-county_20190621_purchase-order) show Fog commonly helps customers perform device searches on known advertising IDs.

### Geofence-Style Searches

Fog's "Reveal" feature enables dragnet searches equivalent to "geofence warrants"—requests to Google for information about every device in a particular area at a particular time. Police can use Fog Reveal "area searches" to:
1. Identify all devices within a geofence and time frame
2. Perform "pattern-of-life analysis" on each device
3. Attempt to identify device owners

Courts have invalidated geofence warrants as too broad to be constitutional.

### The Core Problem

The Fourth Amendment prohibits unreasonable searches and requires particularity in warrants. If the government wants specific location data about a specific person, it must first obtain a warrant based on probable cause. Dragnet surveillance of millions of identifiable people for law enforcement purposes constitutes a forbidden general search.

The government cannot circumvent [these Fourth Amendment rules](https://www.eff.org/deeplinks/2020/12/law-enforcement-purchasing-commercially-available-geolocation-data) by purchasing data from location brokers—yet that is precisely what occurs with mobile location data purchases.

## EFF's Work

EFF investigates law enforcement use of mobile phone location tracking:

- In summer 2022, EFF published an [investigation into Fog Data Science](https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police) with the [Associated Press](https://apnews.com/article/technology-police-government-surveillance-d395409ef5a8c6c3f6cdab5b1d0e27ef), exposing a previously unknown player in the mobile location broker landscape
- EFF continues advancing public knowledge of law enforcement's location data use
- EFF supports legislation like the [Fourth Amendment is Not For Sale Act](https://www.eff.org/deeplinks/2021/04/tell-congress-support-fourth-amendment-not-sale-act) to limit government data purchases

## Additional Reading

- [US v. Ellis](https://www.courtlistener.com/opinion/7327015/united-states-v-ellis/) (Court Opinion)
- [Inside Fog Data Science, the Secretive Company Selling Mass Surveillance to Local Police](https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police) (EFF)
- [Tech tool offers police 'mass surveillance on a budget'](https://apnews.com/article/technology-police-government-surveillance-d395409ef5a8c6c3f6cdab5b1d0e27ef) (Associated Press)
- [Carpenter v. United States decision](https://www.supremecourt.gov/opinions/17pdf/16-402_new_o75q.pdf) (Supreme Court)
- [New Records Detail DHS Purchase and Use of Vast Quantities of Cell Phone Location Data](https://www.aclu.org/news/privacy-technology/new-records-detail-dhs-purchase-and-use-of-vast-quantities-of-cell-phone-location-data) (ACLU)