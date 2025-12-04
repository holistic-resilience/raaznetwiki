---
title: "Cell-Site Simulators (IMSI Catchers)"
tags: [surveillance, cell-site-simulators, imsi-catchers, stingrays, law-enforcement, mobile-security, privacy]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Mobile Surveillance", "Law Enforcement Technology", "Digital Privacy", "Fourth Amendment"]
summary: "Comprehensive guide to cell-site simulators (Stingrays/IMSI catchers), how they intercept mobile communications, law enforcement use, and privacy implications."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of cellular networks", "Familiarity with privacy concepts"]
estimated_read_time: "12 minutes"
---

# Cell-Site Simulators / IMSI Catchers

Cell-site simulators, also known as **Stingrays** or **IMSI catchers**, are surveillance devices that masquerade as legitimate cell-phone towers, tricking phones within a certain radius into connecting to the device rather than an actual tower.

These devices operate by conducting a general search of all cell phones within range, raising significant constitutional concerns. Law enforcement uses cell-site simulators to pinpoint phone locations with greater accuracy than phone companies can provide—and without involving the phone company at all. Cell-site simulators can also log IMSI numbers (International Mobile Subscriber Identifiers), unique identifiers for each SIM card, of all mobile devices within a given area. Some advanced models can intercept communications.

## How Cell-Site Simulators Work

### Standard Cellular Communication

Cellular networks are distributed over geographic areas called "cells." Each cell is served by one transceiver, known as a cell-site or base station. Your phone naturally connects with the closest base station to provide service as you move through various cells.

### Active Cell-Site Simulators

Active cell-site simulators are the type most commonly used by law enforcement. Cellular devices are designed to connect to the cell site with the strongest signal. Cell-site simulators exploit this by:

- Broadcasting signals stronger than legitimate cell sites
- Making signals appear stronger than they actually are
- Exploiting flaws in cellular protocols (2G/3G/4G/5G) to force disconnection from legitimate towers

This causes devices within range to disconnect from their service providers' legitimate cell sites and establish a new connection with the cell-site simulator.

### Detection Challenges

It is difficult for most people to know whether their phone has been accessed by an active cell-site simulator, and **impossible** to know if accessed by a passive IMSI catcher. While apps like SnoopSnitch exist for detection, their accuracy is not verifiable. More advanced tools have been developed by security researchers, including:

- A system by University of Washington researchers to measure cell-site simulator use across Seattle
- EFF's Crocodile Hunter detection system

## Data Collection Capabilities

Cell-site simulators can reveal intensely personal information about anyone carrying a phone, regardless of whether they have been suspected of a crime.

### Basic Capabilities

Once a device connects to a cell-site simulator, the simulator can:
- Determine precise location
- Capture the device's IMSI for identification

### Advanced Capabilities (2G/GSM Downgrade)

If the simulator can downgrade the connection to 2G/GSM, it can potentially:
- Intercept call metadata (numbers called, call duration)
- Access content of unencrypted phone calls and text messages
- Monitor some data usage (websites visited)
- Divert calls and text messages
- Edit messages
- Spoof caller identity in texts and calls

## Law Enforcement Applications

### Deployment Methods

Cell-site simulators come in various sizes:
- Vehicle-mounted units (police cruisers)
- Wearable units (officer vests)
- Airborne units (attached to aircraft)

Some devices can capture data from up to 10,000 phones at a time, including phones in traditionally protected private spaces like homes and doctors' offices.

### Documented Use Cases

Law enforcement has used cell-site simulators for both serious and minor offenses:

| Agency | Use Case |
|--------|----------|
| Baltimore Police | Wide variety—from tracking kidnappers to locating a man who took his wife's phone during an argument |
| Annapolis Police | Investigating a robbery involving $56 worth of food |
| ICE (Detroit) | Locating and arresting an undocumented immigrant |
| San Bernardino Sheriff | Over 300 uses in approximately one year |
| Miami-Dade Police | Surveillance of protestors (2003 FTAA conference) |

### Federal Usage

Cell-site simulators are used by:
- FBI, DEA, NSA, Secret Service, ICE
- U.S. Army, Navy, Marine Corps, National Guard
- U.S. Marshals (including airborne deployment)

A 2023 investigation revealed that ICE, DHS, and the Secret Service have all used cell-site simulators without following their own deployment rules or obtaining warrants.

## Manufacturers and Vendors

### Primary Vendors

**Harris Corporation** is the most well-known supplier, producing:
- Stingray (original model)
- Hailstorm
- ArrowHead
- AmberJack
- KingFish

*Note: Harris has stopped selling to local law enforcement but continues working with the federal government.*

**Digital Receiver Technology** (Boeing division) produces devices commonly called "dirtboxes."

### Other Manufacturers

- Keyw, Octastic, Tactical Support Equipment
- Berkeley Varitronics, Cogynte, X-Surveillance
- Atos, Rayzone, Martone Radio Technology
- Septier Communication, PKI Electronic Intelligence
- Datong (Seven Technologies Group)
- Ability Computers and Software Industries
- Gamma Group, Rohde & Schwarz, Meganet Corporation

## Privacy and Civil Liberties Concerns

### Constitutional Issues

Cell-site simulators conduct **general searches** that potentially violate the Fourth Amendment requirement that warrants "particularly" describe who or what is to be searched. They invade the privacy of everyone in a given area, regardless of criminal suspicion.

### Government Secrecy

Law enforcement has systematically concealed cell-site simulator use:

- Obtaining deceptive "pen register" orders without explaining the surveillance's true nature
- Withholding information from defense attorneys and judges
- Signing non-disclosure agreements with manufacturers
- Accepting plea deals or dropping cases rather than revealing use
- Physically relocating files to thwart public records requests

In Baltimore, a judge found that law enforcement **intentionally withheld information** from the defense, violating legal disclosure obligations. The FBI has instructed police officers to "recreate evidence" from the devices to preserve secrecy.

### Disproportionate Impact

Cell-site simulators have been shown to disproportionately affect:
- Low-income communities
- Communities of color

In Baltimore, an FCC complaint demonstrated that cell-site simulator use disproportionately impacted African-American communities.

### Public Safety Risks

Cell-site simulators can disrupt cell phone communications within a 500-meter radius, potentially interrupting:
- Normal communications
- Emergency phone calls (911)

## EFF's Recommendations

1. **Warrant requirement**: Law enforcement should obtain individualized warrants based on probable cause
2. **Serious crimes only**: Use should be limited to serious, violent crimes
3. **Location-only use**: Simulators should only identify the location of a particular phone
4. **Data minimization**: Law enforcement must minimize collection of data from non-targets
5. **Emergency call protection**: Manufacturers must confirm their technology does not disrupt emergency services

## Legal Developments

### Legislation

- **California Electronic Communications Privacy Act (CalECPA)**: Requires California police to obtain a warrant before using cell-site simulators; evidence obtained without a warrant is inadmissible
- **S.B. 741**: Requires transparency measures regarding cell-site simulator use

### Key Cases

- *State of Maryland v. Kerron Andrews*
- *U.S. v. Damian Patrick*
- *EFF v. U.S. Department of Justice*

A Congressional Oversight Committee report has called on Congress to pass laws requiring warrants before cell-site simulator use.

## Additional Resources

- [Stingray Tracking Devices: Who's Got Them?](https://www.aclu.org/issues/privacy-technology/surveillance-technologies/stingray-tracking-devices-whos-got-them) (ACLU)
- [Department of Justice Policy Guidance: Use of Cell-Site Simulator Technology](https://www.justice.gov/opa/file/767321/download) (DOJ)
- [Long-Secret Stingray Manuals Detail How Police Can Spy on Phones](https://theintercept.com/2016/09/12/long-secret-stingray-manuals-detail-how-police-can-spy-on-phones/) (The Intercept)
- [A Secret Catalogue of Government Gear for Spying on Your Cellphone](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/) (The Intercept)
- [EFF's Gotta Catch 'em All Report](https://www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catchers-exploit-cell-networks)
- [Crocodile Hunter Detection Tool](https://github.com/EFForg/crocodilehunter) (GitHub)

---

*Last updated: March 29, 2023*