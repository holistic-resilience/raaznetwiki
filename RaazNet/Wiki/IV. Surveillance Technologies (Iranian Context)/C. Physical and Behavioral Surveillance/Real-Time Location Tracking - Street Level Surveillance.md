---
title: "Real-Time Location Tracking"
tags: [location-tracking, mobile-surveillance, data-brokers, fourth-amendment, law-enforcement, privacy]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Digital Surveillance", "Privacy Rights", "Law Enforcement Technology", "Data Brokers"]
summary: "EFF guide explaining how law enforcement purchases mobile location data from brokers to track individuals, bypassing warrant requirements."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of mobile devices", "Familiarity with privacy concepts"]
estimated_read_time: "8 minutes"
---

# Real-Time Location Tracking

[Real-time mobile location tracking](https://www.eff.org/issues/location-data-brokers) is one of the ways law enforcement tracks individuals across time. Many people carry cell phones and other mobile devices that capture location information through applications and the advertising ecosystem. In recent years, law enforcement has gained access to this information by [purchasing it from data brokers](https://apnews.com/article/technology-police-government-surveillance-d395409ef5a8c6c3f6cdab5b1d0e27ef), giving them access—often in real-time—to the locations of millions of individuals who have had nothing to do with crimes.

## How It Works

[To advertise to you online](https://www.eff.org/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech), companies need to know who you are and what you like. Your online behavior and location are linked to you, then regularly collected, bought, and sold by advertisers and private companies. Weather apps, navigation apps, coupon apps, and "family safety" apps often request location access to enable key features. Once an app has location access, it can share that data with just about anyone—including the police.

### The Data Collection Process

Data brokers entice app developers with cash-for-data deals, often paying per user for direct access to their device. Developers add bits of code called **software development kits (SDKs)** from location brokers into their apps. Once installed, a broker's SDK gathers data whenever the app has access to it:

- **Foreground access**: Location data collected when the app is open
- **Background access**: Data collected whenever the phone is on, even if the app is closed

Applications typically require users to grant "permission" to access and collect location data. [This information is associated with your Ad-ID](https://www.eff.org/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech)—a way of identifying you, your online behavior, and location across devices, applications, and websites.

This sensitive information is regularly sold and shared beyond the original application, and [law enforcement has begun purchasing](https://www.eff.org/deeplinks/2022/08/how-ad-tech-became-cop-spy-tech) it from data brokers.

## How Law Enforcement Uses It

Real-time mobile location data is now used by federal agencies and small, local police departments alike.

### Federal and Military Use

Military and foreign intelligence agencies have used location data in numerous instances. [In one unclassified project](https://www.wsj.com/articles/academic-project-used-marketing-data-to-monitor-russian-military-sites-11595073601), researchers at Mississippi State University used Locate X data to track movements around Russian missile test sites, including those of high-level diplomats. The U.S. Army funded the project and said it showed "good potential use" of the data. The Army claimed the collection was consistent with policy as long as no "personal characteristics" were collected—though detailed movements of individuals are inherently personal characteristics.

### State and Local Law Enforcement

State and local law enforcement [use purchased location data](https://www.eff.org/press/releases/data-broker-helps-police-see-everywhere-youve-been-click-mouse-eff-investigation) to track individuals who may or may not be involved in crimes. They can:

- **Track specific devices**: Identify a device of interest and follow its location through time and space
- **Area searches**: Specify an area of interest to identify all devices (and individuals) within that area

Law enforcement can effectively "geofence" an area—drawing a virtual fence around a real-world location—then collect digital information from everyone present. This can be applied to any location, including protests, places of worship, or reproductive health clinics.

## Who Sells It

Location data can be [purchased from numerous data brokers](https://www.eff.org/deeplinks/2022/06/how-federal-government-buys-our-cell-phone-location-data), which either collect information directly from applications via SDKs or from other data brokers.

### Key Data Brokers

**[Fog Data Science](https://www.eff.org/deeplinks/2022/06/what-fog-data-science-why-surveillance-company-so-dangerous)**: Specializes in selling location data to law enforcement. Agencies claim it's the only company providing this type of access without requiring purchase of other platforms or services.

**Venntel**: A subsidiary of Gravy Analytics that appears to provide the data underlying Fog Data's services. [Venntel's U.S. government clients](https://www.wired.com/story/dhs-surveillance-phone-tracking-data/) include:
- Internal Revenue Service (IRS)
- Department of Homeland Security (DHS)
- Immigration and Customs Enforcement (ICE)
- Customs and Border Protection (CBP)
- Drug Enforcement Administration (DEA)
- Federal Bureau of Investigation (FBI)

Gravy Analytics acquires all data indirectly through other data brokers rather than embedding SDKs directly.

**Other vendors**: [Locate X](https://www.protocol.com/government-buying-location-data), [Veraset](https://www.eff.org/deeplinks/2021/11/data-broker-veraset-gave-bulk-device-level-gps-data-dc-government), and [Cobwebs Technologies](https://cobwebs.com/en/law-enforcement/) (which [integrates real-time mobile location data](https://theintercept.com/2023/07/26/texas-phone-tracking-border-surveillance/) into broader intelligence analysis platforms).

## Threats to Privacy and Constitutional Rights

The purchase and use of mobile location data [undermines Fourth Amendment rights](https://www.eff.org/deeplinks/2020/12/law-enforcement-purchasing-commercially-available-geolocation-data) and circumvents regulations on government surveillance.

### The Carpenter Precedent

The Fourth Amendment generally requires police to obtain a warrant before searching a particular location or person. In 2018, the Supreme Court ruled in *[Carpenter v. United States](https://www.eff.org/cases/carpenter-v-united-states)* that police must get a warrant before obtaining historical location data from cell carriers—known as "cell site location information" (CSLI). The court wrote that historical CSLI creates a "detailed chronicle of a person's physical presence compiled every day, every moment over years."

### How Data Brokers Enable Constitutional Violations

With access to commercial location data, federal agencies can:

- Query data about millions or billions of identifiable people at once
- Look forwards or backwards at location histories of hundreds of devices simultaneously
- Learn where device owners live, work, and travel
- Make extraordinarily broad queries spanning entire states or countries
- Filter resulting data however they see fit

This stretches the Fourth Amendment's particularity requirement far beyond the breaking point.

### Scale of Surveillance

Fog's "device search" feature provides chronicles of people's lives often more detailed than the CSLI in *Carpenter*. In that case, carriers provided 12,898 data points spanning 127 days for one individual. Records show that Missouri officials acquired **47,394 signals spanning 163 days** for a single phone using Fog's data.

Records from [Iowa Department of Public Safety](https://www.documentcloud.org/documents/22187960-iowa-dps_20210312_ad-id-lookup) and [Broward County, Florida](https://www.documentcloud.org/documents/22187525-broward-county_20190621_purchase-order) show Fog commonly helps customers perform device searches on known advertising IDs. Fog's "Reveal" feature executes dragnet searches equivalent to geofence warrants—courts have invalidated such warrants as too broad to be constitutional.

### The Constitutional Problem

The Fourth Amendment prohibits unreasonable searches and requires particularity in warrants. The government cannot do an end-run around [these basic Fourth Amendment rules](https://www.eff.org/deeplinks/2020/12/law-enforcement-purchasing-commercially-available-geolocation-data) by writing checks to location data brokers—yet that is exactly what's happening.

## EFF's Work on This Issue

EFF has been investigating law enforcement's use of mobile phone location tracking.

In summer 2022, [EFF published an investigation](https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police), [together with the Associated Press](https://apnews.com/article/technology-police-government-surveillance-d395409ef5a8c6c3f6cdab5b1d0e27ef), into Fog Data Science—previously unknown in the mobile location broker landscape.

EFF continues working to advance knowledge of law enforcement's use of mobile location data and supports legislation like [the Fourth Amendment is Not For Sale Act](https://www.eff.org/deeplinks/2021/04/tell-congress-support-fourth-amendment-not-sale-act), which limits government agencies' ability to purchase information on individuals.

## Additional Reading

- [US v Ellis](https://www.courtlistener.com/opinion/7327015/united-states-v-ellis/) (Court Opinion)
- [Inside Fog Data Science, the Secretive Company Selling Mass Surveillance to Local Police](https://www.eff.org/deeplinks/2022/08/inside-fog-data-science-secretive-company-selling-mass-surveillance-local-police) (EFF)
- [Tech tool offers police 'mass surveillance on a budget'](https://apnews.com/article/technology-police-government-surveillance-d395409ef5a8c6c3f6cdab5b1d0e27ef) (Associated Press)
- [Carpenter v. United States decision](https://www.supremecourt.gov/opinions/17pdf/16-402_new_o75q.pdf) (Supreme Court)
- [New Records Detail DHS Purchase and Use of Vast Quantities of Cell Phone Location Data](https://www.aclu.org/news/privacy-technology/new-records-detail-dhs-purchase-and-use-of-vast-quantities-of-cell-phone-location-data) (ACLU)