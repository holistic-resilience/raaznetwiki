---
title: "Cell-Site Simulators and IMSI Catchers"
tags: [surveillance, cell-site-simulators, imsi-catchers, stingrays, law-enforcement, mobile-security, privacy]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists, Legal Professionals]
topics: ["Mobile Surveillance", "Law Enforcement Technology", "Digital Privacy", "Fourth Amendment", "Cellular Networks"]
summary: "Comprehensive guide to cell-site simulators (Stingrays/IMSI catchers) - how they work, what data they collect, law enforcement use, and privacy implications."
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

These devices operate by conducting a general search of all cell phones within range, raising serious constitutional concerns. Law enforcement uses cell-site simulators to pinpoint phone locations with greater accuracy than phone companies can provide—and without involving the phone company at all. Cell-site simulators can also log IMSI numbers (International Mobile Subscriber Identifiers) unique to each SIM card for all mobile devices within a given area. Some advanced models can intercept communications.

---

## How Cell-Site Simulators Work

### Standard Cellular Communication

Cellular networks are distributed over geographic areas called "cells." Each cell is served by one transceiver (cell-site or base station). Your phone naturally connects to the closest base station to provide service as you move through various cells.

### Active Cell-Site Simulators

Active cell-site simulators—the type most commonly used by law enforcement—exploit how cellular devices are designed to connect to the nearby cell site with the strongest signal.

**How they exploit this behavior:**
- Broadcast signals stronger than legitimate cell sites nearby (or made to appear stronger)
- Cause devices within range to disconnect from legitimate cell sites
- Force devices to establish new connections with the cell-site simulator
- Exploit flaws in cellular protocols (2G/3G/4G/5G) to force disconnection from legitimate towers

### Detection Challenges

It is difficult for most people to know whether their phone has been accessed by an active cell-site simulator, and **impossible** to detect passive IMSI catchers.

**Detection tools (with limitations):**
- **SnoopSnitch app** - May not be verifiably accurate
- **SeaGlass** - System designed by University of Washington researchers to measure cell-site simulator use across Seattle
- **Crocodile Hunter** - Detection system designed by EFF researchers

---

## What Data Cell-Site Simulators Collect

Data collected can reveal intensely personal information about anyone carrying a phone, regardless of whether they've been suspected of a crime.

### Basic Data Collection
Once connected to a cell-site simulator, the device can:
- Determine your precise location
- Trigger your device to transmit its IMSI for later identification

### Advanced Capabilities (2G/GSM Downgrade)
If the simulator downgrades the connection to 2G/GSM, it can potentially:
- Intercept call metadata (numbers called, call duration)
- Capture unencrypted phone calls and text messages
- Monitor some types of data usage (websites visited)
- Divert calls and text messages
- Edit messages
- Spoof caller identity in texts and calls

---

## How Law Enforcement Uses Cell-Site Simulators

### Operational Methods

Police use cell-site simulators in two primary ways:
1. **Targeted tracking** - Locating a person when they already know the phone's identifying information
2. **Dragnet collection** - Gathering IMSI numbers of anyone in a specific area

**Deployment scale:**
- Some devices are small enough to fit in a police cruiser or on an officer's vest
- Officers can drive to multiple locations, capturing data from every mobile device in an area
- Some devices can capture up to **10,000 phones** at a time
- Searches include phones in traditionally protected spaces like homes and doctors' offices

### Documented Use Cases

**Local Law Enforcement:**
- Baltimore Police: Tracking kidnapper; locating a man who took his wife's phone during an argument
- Annapolis Police: Investigating a robbery involving $56 worth of food
- San Bernardino County Sheriff: Used cell-site simulator over 300 times in just over a year

**Federal Agencies:**
- ICE: Locating and arresting undocumented immigrants
- U.S. Marshals and FBI: Attached cell-site simulators to aircraft for tracking suspects
- Texas National Guard: Airborne cell-site simulators documented by Texas Observer

**Agencies Known to Use Cell-Site Simulators:**
- FBI, DEA, NSA, Secret Service, ICE
- U.S. Army, Navy, Marine Corps, National Guard
- Numerous state and local police departments

### Protest Surveillance

- Miami-Dade Police Department first purchased a cell-site simulator in 2003 to surveil protestors at a Free Trade of the Americas Agreement conference
- Suspected use during 2020 protests against police violence

### Compliance Issues

A 2023 report revealed that ICE, DHS, and the Secret Service have all used cell-site simulators many times **without following their own rules** on deployment or obtaining warrants.

---

## Manufacturers and Vendors

### Primary Vendors

**Harris Corporation** (most well-known):
- Stingray (original product, now a generic term)
- Hailstorm, ArrowHead, AmberJack, KingFish
- Has stopped selling to local law enforcement; still works with federal government

**Digital Receiver Technology** (Boeing division):
- Products commonly called "dirtboxes"

### Other Manufacturers
- Keyw, Octastic, Tactical Support Equipment
- Berkeley Varitronics, Cogynte, X-Surveillance
- Atos, Rayzone, Martone Radio Technology
- Septier Communication, PKI Electronic Intelligence
- Datong (Seven Technologies Group)
- Ability Computers and Software Industries
- Gamma Group, Rohde & Schwarz, Meganet Corporation

---

## Privacy and Constitutional Concerns

### Fourth Amendment Violations

Cell-site simulators conduct **general searches** that violate the Fourth Amendment requirement that warrants "particularly" describe who or what is to be searched. They invade the privacy of everyone within range, regardless of criminal suspicion.

### Government Secrecy

Law enforcement has extensively concealed cell-site simulator use:

**Deceptive Practices:**
- Obtaining "pen register" orders without explaining the true nature of surveillance
- Withholding information from defense attorneys and judges
- Signing non-disclosure agreements with Harris Corporation

**Obstruction of Justice:**
- Baltimore: Judge concluded law enforcement intentionally withheld information from defense
- Prosecutors have accepted plea deals to hide cell-site simulator use
- Cases have been dropped rather than reveal information about the technology
- U.S. Marshals drove files hundreds of miles to thwart public records requests
- FBI instructed police officers to "recreate evidence" from devices

### Disproportionate Impact

Cell-site simulators have been shown to disproportionately affect:
- Low-income communities
- Communities of color

In Baltimore, cell-site simulator use disproportionately impacted African-American communities, according to an FCC complaint overlaying police deployment data with census data.

### Emergency Service Disruption

Cell-site simulators can disrupt cell phone communications within up to a **500-meter radius**, including:
- Interrupting important communications
- Blocking emergency phone calls (911)

This makes them not only a privacy threat but a **public safety hazard**.

---

## EFF's Position and Recommendations

### Policy Recommendations

1. Law enforcement should obtain **individualized warrants based on probable cause**
2. Cell-site simulators should only be used for **serious, violent crimes**
3. Use should be limited to **identifying location of a particular phone**
4. Law enforcement must **minimize collection of data** from non-targets
5. Manufacturers must confirm their technology **does not disrupt emergency services**

### Legal Actions

**Freedom of Information:**
- Filed FOIA lawsuit to expose U.S. Marshals Service's use of cell-site simulators on planes

**Amicus Briefs:**
- First case where a judge threw out evidence from warrantless cell-site simulator use (with ACLU and ACLU of Maryland)
- U.S. vs. Damian Patrick: Pointed court to facts indicating Milwaukee Police secretly used cell-site simulator without a warrant

### Legislative Efforts

**California Electronic Communications Privacy Act (CalECPA):**
- Co-sponsored with ACLU and California Newspaper Publisher Association
- Requires California police to get a warrant before using cell-site simulators
- Evidence obtained without warrant is inadmissible in court

**S.B. 741:**
- Requires transparency measures regarding cell-site simulator use

### Technical Research

- **"Gotta Catch 'em All"** - Technical report on how cell-site simulators exploit cell networks
- **Crocodile Hunter** - Proof-of-concept detection system

---

## Related EFF Cases

- State of Maryland v. Kerron Andrews
- U.S. v. Damian Patrick
- EFF v. U.S. Department of Justice (U.S. Marshals Airborne IMSI Catchers)

---

## Additional Resources

- [Stingray Tracking Devices: Who's Got Them?](https://www.aclu.org/issues/privacy-technology/surveillance-technologies/stingray-tracking-devices-whos-got-them) (ACLU)
- [Your Secret Stingray's No Secret Anymore](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2437678) (Harvard Journal of Law and Technology)
- [Examining Law Enforcement Use of Cell Phone Tracking Devices](https://oversight.house.gov/hearing/examining-law-enforcement-use-of-cell-phone-tracking-devices/) (House Oversight Committee)
- [Department of Justice Policy Guidance: Use of Cell-Site Simulator Technology](https://www.justice.gov/opa/file/767321/download) (U.S. Department of Justice)
- [Long-Secret Stingray Manuals Detail How Police Can Spy on Phones](https://theintercept.com/2016/09/12/long-secret-stingray-manuals-detail-how-police-can-spy-on-phones/) (The Intercept)
- [A Secret Catalogue of Government Gear for Spying on Your Cellphone](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/) (The Intercept)