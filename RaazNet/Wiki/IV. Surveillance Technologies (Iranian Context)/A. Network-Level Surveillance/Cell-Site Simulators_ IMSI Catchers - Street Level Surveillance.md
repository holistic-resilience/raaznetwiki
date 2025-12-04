---
title: "Cell-Site Simulators / IMSI Catchers"
tags: [surveillance, imsi-catchers, stingray, law-enforcement, mobile-security, privacy, fourth-amendment]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Mobile Phone Surveillance", "Law Enforcement Technology", "Digital Privacy", "Constitutional Rights"]
summary: "Comprehensive guide on cell-site simulators (Stingrays/IMSI catchers) used by law enforcement to track phones and intercept communications."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of cellular networks", "Familiarity with privacy concepts"]
estimated_read_time: "12 minutes"
last_updated: "2023-03-29"
---

# Cell-Site Simulators / IMSI Catchers

Cell-site simulators, also known as **Stingrays** or **IMSI catchers**, are surveillance devices that [masquerade as legitimate cell-phone towers](https://www.eff.org/deeplinks/2015/01/2014-review-stingrays-go-mainstream), tricking phones within a certain radius into [connecting to the device rather than an actual tower](https://www.justice.gov/opa/file/767321/download).

These devices operate by conducting a general search of all cell phones within range, raising serious constitutional concerns. Law enforcement uses cell-site simulators to:

- Pinpoint phone locations with greater accuracy than phone companies
- Operate without involving the phone company
- Log IMSI numbers (International Mobile Subscriber Identifiers) unique to each SIM card
- Potentially intercept communications (with advanced features)

## How Cell-Site Simulators Work

### Standard Cellular Communication

Cellular networks are distributed over geographic areas called "cells." Each cell is served by one transceiver (cell-site or base station). Your phone naturally connects with the closest base station to provide service as you move through various cells.

![Phones connecting to cellular networks](https://sls.eff.org/files/sls/wysiwyg/pictures/42/content_CSS-2.png)

### Active Cell-Site Simulators

Active cell-site simulators are the most commonly used by law enforcement. They exploit how cellular devices are designed to connect to the nearby cell site with the strongest signal.

**How they work:**
- Broadcast signals stronger than legitimate cell sites (or made to appear stronger)
- Cause devices within range to disconnect from legitimate cell sites
- Force phones to establish new connections with the simulator
- Exploit flaws in cellular protocols (2G/3G/4G/5G) to force disconnections

### Detection Challenges

It is difficult for most people to know whether their phone's signals have been accessed by an active cell-site simulator, and **impossible** to detect passive IMSI catchers.

**Detection tools:**
- Apps like SnoopSnitch (may not be verifiably accurate)
- More advanced research tools, such as:
  - University of Washington's [SeaGlass system](https://seaglass.cs.washington.edu/) for measuring cell-site simulator use across Seattle
  - EFF's [Crocodile Hunter](https://github.com/EFForg/crocodilehunter/) detection system

## Data Collection Capabilities

Data collected by cell-site simulators can reveal intensely personal information about anyone who carries a phone, whether or not they have ever been suspected of a crime.

![Cell-site simulators tricking phones to connect to them](https://sls.eff.org/files/sls/wysiwyg/pictures/43/content_CSS-3.png)

### Basic Capabilities

Once connected to a cell-site simulator, the device can:
- Determine your location
- Trigger your device to transmit its IMSI for identification

### Advanced Capabilities (2G/GSM Downgrade)

If the simulator downgrades the connection to 2G/GSM, it can potentially:
- Intercept call metadata (numbers called, call duration)
- Capture [unencrypted phone calls and text messages](https://www.justice.gov/sites/default/files/criminal/legacy/2014/10/29/elec-sur-manual.pdf)
- Monitor some types of data usage (websites visited)
- [Divert calls and text messages](https://info.publicintelligence.net/Gamma-GSM.pdf)
- Edit messages
- Spoof caller identity in texts and calls

## Law Enforcement Usage

### Deployment Methods

- **Vehicle-mounted:** Small enough to fit in a police cruiser
- **Portable:** Can be worn on an officer's vest
- **Airborne:** Attached to [planes by U.S. Marshals and FBI](https://www.wsj.com/articles/americans-cellphones-targeted-in-secret-u-s-spy-program-1415917533)

These devices can capture data from [up to 10,000 phones](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/) at a time, including phones in traditionally protected private spaces like homes and doctors' offices.

### Federal Agencies Using Cell-Site Simulators

- FBI, DEA, NSA, Secret Service, ICE
- U.S. Army, Navy, Marine Corps, National Guard
- U.S. Marshals
- [Texas National Guard](https://www.texasobserver.org/texas-national-guard-spying-devices-surveillance/) (airborne use)

In 2023, it was revealed that ICE, DHS, and the Secret Service have [used cell-site simulators many times without following their own rules or obtaining warrants](https://www.eff.org/deeplinks/2023/03/report-ice-and-secret-service-conducted-illegal-surveillance-cell-phones).

### Types of Investigations

Cell-site simulators have been used for both major and minor crimes:

| Agency | Use Case |
|--------|----------|
| Baltimore Police | Wide variety: from tracking kidnappers to locating a man who took his wife's phone during an argument |
| Annapolis Police | [Investigated a robbery involving $56 worth of food](https://gizmodo.com/maryland-police-used-an-indiscriminate-cellphone-spy-to-1774831661) |
| ICE (Detroit) | [Located and arrested an undocumented immigrant](https://www.eff.org/deeplinks/2017/05/no-hunting-undocumented-immigrants-stingrays) |
| San Bernardino Sheriff | [Used over 300 times in approximately one year](https://arstechnica.com/tech-policy/2018/10/eff-sues-county-sheriff-claims-agency-wont-give-up-stingray-related-records/) |

### Use at Protests

- Miami-Dade Police Department [first purchased a cell-site simulator in 2003](http://cdn.arstechnica.net/wp-content/uploads/2013/09/miami-dade.pdf) for surveillance at a Free Trade of the Americas Agreement conference
- Suspected use [during 2020 protests against police violence](https://www.law.georgetown.edu/american-criminal-law-review/wp-content/uploads/sites/15/2022/02/59-1-Owsley-George_Floyd_General_Warrants.pdf)

## Manufacturers and Vendors

### Primary Suppliers

| Company | Products/Notes |
|---------|----------------|
| Harris Corporation | Stingray, Hailstorm, [ArrowHead](https://www.documentcloud.org/documents/3105805-Arrowhead-1-0-1-Release-Notes.html), [AmberJack, KingFish](https://www.documentcloud.org/documents/3105793-Gemini-3-3-Quick-Start-Guide.html) (no longer sells to local law enforcement) |
| Digital Receiver Technology (Boeing) | "[Dirtboxes](https://www.revealnews.org/article/chicago-and-los-angeles-have-used-dirt-box-surveillance-for-a-decade/)" |

### Other Manufacturers

Keyw, Octastic, Tactical Support Equipment, Berkeley Varitronics, Cogynte, X-Surveillance, Atos, Rayzone, Martone Radio Technology, Septier Communication, PKI Electronic Intelligence, Datong (Seven Technologies Group), Ability Computers and Software Industries, Gamma Group, Rohde & Schwarz, Meganet Corporation

**Technical Documentation:**
- [Septier product information](http://www.septier.com/law-enforcement/)
- [Gamma GSM capabilities](https://info.publicintelligence.net/Gamma-GSM.pdf)
- The Intercept's [secret internal U.S. government catalogue](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/)
- [Older cell-site simulator manual](https://theintercept.com/2016/09/12/long-secret-stingray-manuals-detail-how-police-can-spy-on-phones/) (obtained via FOIA)

## Privacy and Constitutional Concerns

### Fourth Amendment Violations

Cell-site simulators conduct [general searches](https://www.hoover.org/sites/default/files/research/docs/lynch_webreadypdf.pdf) that violate the Fourth Amendment requirement that warrants "particularly" describe who or what is to be searched. They invade the privacy of everyone within range, regardless of criminal suspicion.

### Government Secrecy

Law enforcement has employed extensive measures to conceal cell-site simulator use:

- **Deceptive court orders:** Obtaining "pen register" orders without explaining the true nature of surveillance
- **Withholding from defense:** In Baltimore, a judge concluded law enforcement [intentionally withheld information](https://www.aclu.org/other/state-v-andrews-stingray-june-4-2015-transcript?redirect=state-v-andrews-stingray-june-4-2015-transcript) from the defense
- **Non-disclosure agreements:** [With Harris Corporation](http://www.baltimoresun.com/news/maryland/baltimore-city/bs-md-ci-stingray-case-20150408-story.html)
- **Plea deals and dropped cases:** Prosecutors have [accepted plea deals](https://www.washingtonpost.com/world/national-security/secrecy-around-police-surveillance-equipment-proves-a-cases-undoing/2015/02/22/ce72308a-b7ac-11e4-aa05-1ce812b3fdd2_story.html) and [dropped cases](http://arstechnica.com/tech-policy/2015/04/fbi-would-rather-prosecutors-drop-cases-than-disclose-stingray-details/) to hide use
- **Evidence obstruction:** U.S. Marshals [drove files hundreds of miles](https://arstechnica.com/tech-policy/2014/06/us-marshals-step-in-thwart-efforts-to-learn-about-cell-tracking-devices/) to thwart public records requests
- **Evidence recreation:** [FBI instructed police officers to recreate evidence](https://theintercept.com/2016/05/05/fbi-told-cops-to-recreate-evidence-from-secret-cell-phone-trackers/) from the devices

### Public Safety Disruption

Cell-site simulators often disrupt cell phone communications within up to a [500-meter radius](http://www.theglobeandmail.com/news/national/rcmp-listening-tool-capable-of-knocking-out-911-calls-memoreveals/article29672075/), including [emergency phone calls](https://www.eff.org/deeplinks/2018/08/blog-post-wyden-911-disruption-css).

### Disproportionate Impact

In Baltimore, cell-site simulator use disproportionately impacted African-American communities, according to a map included in an [FCC complaint](https://www.eff.org/deeplinks/2016/08/civil-liberties-groups-file-fcc-complaint-arguing-baltimore-police-are-illegally) that overlaid deployment locations over census data.

## Legal Framework

### Current Status

- A [Congressional Oversight Committee report](https://www.eff.org/deeplinks/2017/02/bipartisan-congressional-oversight-committee-wants-probable-cause-warrants-0) called on Congress to pass laws requiring warrants before using cell-site simulators
- Some states, [such as California](https://www.eff.org/cases/californias-electronic-communications-privacy-act-calecpa), already require warrants except in emergencies

## EFF's Recommendations

1. Law enforcement should obtain **individualized warrants based on probable cause**
2. Cell-site simulators should only be used for **serious, violent crimes**
3. Cell-site simulators should only be used for **identifying location of a particular phone**
4. Law enforcement must **minimize collection of data** from non-targets
5. Manufacturers must confirm their technology **does not disrupt emergency services**

## EFF's Work on Cell-Site Simulators

### Litigation

- [FOIA lawsuit](https://www.eff.org/press/releases/eff-files-foia-suit-over-us-marshals-spy-planes) to expose U.S. Marshals Service's airborne cell-site simulator use
- [Amicus brief](https://www.eff.org/deeplinks/2015/12/eff-joins-aclu-amicus-brief-supporting-warrant-requirement-cell-site-simulators) (with ACLU) in the first case where a judge threw out evidence obtained without a warrant
- Amicus brief in *U.S. vs. Damian Patrick* regarding Milwaukee Police Department's warrantless use

### Legislation

- Co-sponsored the [California Electronic Communications Privacy Act (CalECPA)](https://www.eff.org/cases/californias-electronic-communications-privacy-act-calecpa) requiring warrants for cell-site simulator use
- Supported S.B. 741 requiring [transparency measures](https://www.eff.org/deeplinks/2016/04/here-are-79-policies-california-surveillance-tech-where-are-other-90)

### Research

- Published ["Gotta Catch 'em All"](https://www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catchers-exploit-cell-networks) technical report on cell-site simulator methods
- Developed [Crocodile Hunter](https://github.com/EFForg/crocodilehunter) proof-of-concept detection tool

## Related EFF Cases

- [State of Maryland v. Kerron Andrews](https://www.eff.org/cases/state-maryland-v-kerron-andrews)
- [U.S. v. Damian Patrick](https://www.eff.org/cases/us-v-damian-patrick)
- [EFF v. U.S. Department of Justice](https://www.eff.org/cases/us-marshals-airborne-imsi-catchers)

## Additional Reading

- [Stingray Tracking Devices: Who's Got Them?](https://www.aclu.org/issues/privacy-technology/surveillance-technologies/stingray-tracking-devices-whos-got-them) (ACLU)
- [Your Secret Stingray's No Secret Anymore](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2437678) (Harvard Journal of Law and Technology)
- [Examining Law Enforcement Use of Cell Phone Tracking Devices](https://oversight.house.gov/hearing/examining-law-enforcement-use-of-cell-phone-tracking-devices/) (House Oversight Committee)
- [The Relentless "Eye" Local Surveillance](http://centerformediajustice.org/resources/the-relentless-eye/) (Center for Media Justice)
- [Department of Justice Policy Guidance](https://www.justice.gov/opa/file/767321/download) (U.S. Department of Justice)
- [Long-Secret Stingray Manuals Detail How Police Can Spy on Phones](https://theintercept.com/2016/09/