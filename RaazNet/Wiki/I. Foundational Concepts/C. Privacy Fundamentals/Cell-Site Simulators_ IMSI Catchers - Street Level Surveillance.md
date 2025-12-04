---
title: "Cell-Site Simulators and IMSI Catchers"
tags: [cell-site-simulator, imsi-catcher, stingray, mobile-surveillance, law-enforcement, fourth-amendment]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Mobile Phone Surveillance", "Law Enforcement Technology", "Digital Privacy", "Constitutional Rights"]
summary: "Comprehensive guide to cell-site simulators (Stingrays/IMSI catchers) - how they work, what data they collect, and their legal implications."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Advanced"
language: "English"
prerequisites: ["Basic understanding of cellular networks", "Familiarity with privacy concepts"]
estimated_read_time: "15 minutes"
last_updated: "2023-03-29"
---

# Cell-Site Simulators and IMSI Catchers

Cell-site simulators, also known as **Stingrays** or **IMSI catchers**, are surveillance devices that masquerade as legitimate cell-phone towers, tricking phones within a certain radius into connecting to the device rather than an actual tower.

These devices operate by conducting a general search of all cell phones within range, raising significant constitutional concerns. Law enforcement uses cell-site simulators to:

- Pinpoint phone locations with greater accuracy than phone companies
- Operate without involving the phone company
- Log IMSI numbers (International Mobile Subscriber Identifiers) unique to each SIM card
- Potentially intercept communications (with advanced features)

## How Cell-Site Simulators Work

### Standard Cellular Communication

Cellular networks are distributed over geographic areas called "cells." Each cell is served by one transceiver (cell-site or base station). Your phone naturally connects with the closest base station to provide service as you move through various cells.

### Active Cell-Site Simulators

Active cell-site simulators are the type most commonly used by law enforcement. They exploit how cellular devices are designed to connect to the cell site with the strongest signal:

1. **Signal Strength Exploitation**: The simulator broadcasts signals stronger than legitimate cell sites (or makes signals appear stronger)
2. **Forced Disconnection**: Devices within range disconnect from legitimate cell sites
3. **Rogue Connection**: Phones establish new connections with the cell-site simulator
4. **Protocol Vulnerabilities**: Simulators exploit flaws in 2G/3G/4G/5G cellular protocols to force connections

### Detection Challenges

It is difficult for most people to know whether their phone's signals have been accessed by an active cell-site simulator, and impossible to detect passive IMSI catchers. While apps like SnoopSnitch exist, their accuracy is not verifiable. More advanced detection systems have been developed:

- **SeaGlass**: A system designed by University of Washington researchers to measure cell-site simulator use across Seattle
- **Crocodile Hunter**: A detection system developed by EFF researchers

## Data Collection Capabilities

Cell-site simulators can collect intensely personal information about anyone who carries a phone, regardless of whether they have been suspected of a crime.

### Basic Data Collection

Once a device connects to a cell-site simulator, it can:

- Determine your precise location
- Capture your device's IMSI for identification

### Advanced Capabilities (2G/GSM Downgrade)

If the simulator forces a downgrade to 2G/GSM, it can potentially:

- Intercept call metadata (numbers called, call duration)
- Capture unencrypted phone calls and text messages
- Monitor certain data usage (websites visited)
- Divert calls and text messages
- Edit messages
- Spoof caller identity in texts and calls

## Law Enforcement Usage

### Operational Methods

Police use cell-site simulators in various configurations:

- **Vehicle-mounted**: Small enough to fit in a police cruiser
- **Body-worn**: Can be worn on an officer's vest
- **Airborne**: Attached to aircraft (used by U.S. Marshals and FBI)

These devices can capture data from up to 10,000 phones at a time, including phones in private spaces like homes and doctors' offices.

### Documented Use Cases

Law enforcement has used cell-site simulators for investigations ranging from serious to trivial:

| Agency | Use Case |
|--------|----------|
| Baltimore Police | Tracking kidnapper; locating man who took wife's phone during argument |
| Annapolis Police | Investigating robbery of $56 worth of food |
| ICE (Detroit) | Locating and arresting undocumented immigrant |
| San Bernardino Sheriff | Over 300 deployments in approximately one year |
| Miami-Dade Police | Surveilling protesters at FTAA conference (2003) |

### Federal Agencies Using Cell-Site Simulators

- FBI, DEA, NSA, Secret Service, ICE
- U.S. Army, Navy, Marine Corps, National Guard
- U.S. Marshals
- Department of Homeland Security

A 2023 investigation revealed that ICE, DHS, and the Secret Service used cell-site simulators many times without following their own deployment rules or obtaining warrants.

## Manufacturers and Vendors

### Primary Manufacturers

**Harris Corporation** (most well-known):
- Stingray (original product, now synonymous with the technology)
- Hailstorm, ArrowHead, AmberJack, KingFish
- *Note: Harris has stopped selling to local law enforcement but continues federal government contracts*

**Digital Receiver Technology** (Boeing division):
- "Dirtboxes"

### Other Vendors

| Company | Company | Company |
|---------|---------|---------|
| Keyw | Octastic | Tactical Support Equipment |
| Berkeley Varitronics | Cogynte | X-Surveillance |
| Atos | Rayzone | Martone Radio Technology |
| Septier Communication | PKI Electronic Intelligence | Datong (Seven Technologies Group) |
| Ability Computers | Gamma Group | Rohde & Schwarz |
| Meganet Corporation | | |

## Legal and Constitutional Concerns

### Fourth Amendment Violations

Cell-site simulators conduct **general searches** that violate the Fourth Amendment requirement that warrants "particularly" describe who or what is to be searched. They invade the privacy of everyone within range, regardless of criminal suspicion.

### Government Secrecy

Law enforcement has engaged in extensive efforts to hide cell-site simulator use:

- Using deceptive "pen register" orders instead of proper warrants
- Withholding information from defense attorneys and judges
- Signing non-disclosure agreements with Harris Corporation
- Accepting plea deals to avoid disclosure
- Dropping cases rather than revealing technology use
- Physically relocating files to thwart public records requests
- FBI instructing officers to "recreate evidence" from the devices

### Documented Secrecy Incidents

- **Baltimore**: Judge concluded law enforcement intentionally withheld information from defense
- **Sarasota, FL; Tacoma, WA; Baltimore, MD; St. Louis, MO**: Police attempted to keep information secret
- **U.S. Marshals**: Drove files hundreds of miles to avoid public records requests

## Public Safety and Civil Rights Impacts

### Emergency Services Disruption

Cell-site simulators often disrupt cell phone communications within up to a **500-meter radius**, potentially interrupting:

- Emergency 911 calls
- Critical communications

### Disproportionate Impact

Studies show cell-site simulators disproportionately affect:

- Low-income communities
- Communities of color

In Baltimore, an FCC complaint demonstrated that cell-site simulator use disproportionately impacted African-American communities based on deployment locations overlaid with census data.

## EFF's Recommended Safeguards

1. **Warrant Requirement**: Law enforcement should obtain individualized warrants based on probable cause
2. **Serious Crimes Only**: Use should be limited to serious, violent crimes
3. **Location-Only Use**: Devices should only identify the location of a particular phone
4. **Data Minimization**: Law enforcement must minimize collection from non-targets
5. **Emergency Services Protection**: Manufacturers must confirm their technology does not disrupt emergency calls

## Legal Developments

### State Legislation

**California Electronic Communications Privacy Act (CalECPA)**:
- Requires California police to get a warrant before using cell-site simulators
- Evidence obtained without a warrant is inadmissible in court
- Co-sponsored by EFF, ACLU, and California Newspaper Publisher Association

### Federal Oversight

A Congressional Oversight Committee report called on Congress to pass laws requiring a warrant before using cell-site simulators.

## Additional Resources

### EFF Resources

- [Gotta Catch 'em All: Understanding How IMSI-Catchers Exploit Cell Networks](https://www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catchers-exploit-cell-networks) - Technical report
- [Crocodile Hunter](https://github.com/EFForg/crocodilehunter) - Detection proof of concept

### External Resources

- [Stingray Tracking Devices: Who's Got Them?](https://www.aclu.org/issues/privacy-technology/surveillance-technologies/stingray-tracking-devices-whos-got-them) (ACLU)
- [Department of Justice Policy Guidance: Use of Cell-Site Simulator Technology](https://www.justice.gov/opa/file/767321/download)
- [Long-Secret Stingray Manuals Detail How Police Can Spy on Phones](https://theintercept.com/2016/09/12/long-secret-stingray-manuals-detail-how-police-can-spy-on-phones/) (The Intercept)
- [A Secret Catalogue of Government Gear for Spying on Your Cellphone](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/) (The Intercept)

### Related EFF Legal Cases

- State of Maryland v. Kerron Andrews
- U.S. v. Damian Patrick
- EFF v. U.S. Department of Justice (U.S. Marshals Airborne IMSI Catchers)