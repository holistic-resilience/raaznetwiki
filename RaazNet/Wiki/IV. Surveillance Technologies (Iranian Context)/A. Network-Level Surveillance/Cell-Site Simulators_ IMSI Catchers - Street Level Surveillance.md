Cell-Site Simulators/ IMSI Catchers \| Street Level Surveillance [Skip to main content](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers#main-content)

- [Technologies](https://sls.eff.org/)
- [About](https://sls.eff.org/?class=scrolly#about)
- [News](https://sls.eff.org/articles)
- Resources
  - [Atlas of Surveillance](https://atlasofsurveillance.org/)
  - [Spot the Surveillance](https://eff.org/spot)
  - [Surveillance Self Defense](https://ssd.eff.org/)

* * *

Follow Us


- [Facebook](https://www.facebook.com/eff)
- [X](https://twitter.com/eff)
- [RSS](https://www.eff.org/rss)
- [Subscribe](https://www.eff.org/effector)

Share


- [Facebook](https://www.facebook.com/share.php?u=https%3A//sls.eff.org&title=EFF%27s%20Street-Level%20Surveillance%20page%20is%20an%20accessible%20resources%20when%20you%20need%20a%20field%20guide%20to%20the%20technology%20used%20by%20police,%20how%20it%20works,%20and%20why%20it%27s%20dangerous.%20Learn%20more%20about%20surveillance%20cameras,%20license%20plate%20readers,%20and%20more. "Share on Facebook")
- [X](https://twitter.com/intent/tweet?text=EFF%27s%20Street-Level%20Surveillance%20page%20is%20an%20accessible%20resources%20when%20you%20need%20a%20field%20guide%20to%20the%20technology%20used%20by%20police,%20how%20it%20works,%20and%20why%20it%27s%20dangerous.%20Learn%20more%20about%20surveillance%20cameras,%20license%20plate%20readers,%20and%20more.&url=https%3A//sls.eff.org&via=eff&related=eff "Share on Twitter")
- Copy Link

[×](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers#)

[≡](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers#mobile-nav)

[![Electronic Frontier Foundation](https://sls.eff.org/assets/eff-monogram-white-82e096a984dc1f116f80dbea3f0f704d2e1a7407a359a616057f4e7917cd7a26.svg)](https://eff.org/)

![globe](https://sls.eff.org/assets/globe-54ce3b0c3b43065e07a53826025a3b07657c141b646dc37047e18a7d4622854e.svg)

- [English](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers)
- [Español](https://sls.eff.org/es/technologies/cell-site-simulators-imsi-catchers)

![](https://sls.eff.org/files/sls/technology/banner_attachment/file/29/SLS-cellsite-2023.png)

## Cell-site simulators/ imsi catchers

Cell-site simulators, also known as Stingrays or IMSI catchers, are devices that [masquerade as legitimate cell-phone towers](https://www.eff.org/deeplinks/2015/01/2014-review-stingrays-go-mainstream), tricking phones within a certain radius into [connecting to the device rather than a tower](https://www.justice.gov/opa/file/767321/download).

Cell-site simulators operate by conducting a general search of all cell phones within the device’s radius, in violation of basic constitutional protections. Law enforcement use cell-site simulators to pinpoint the location of phones with greater accuracy than phone companies and without needing to involve the phone company at all. Cell-site simulators can also log IMSI numbers, (International Mobile Subscriber Identifiers) unique to each SIM card, of all of the mobile devices within a given area. Some cell-site simulators may have advanced features allowing law enforcement to intercept communications.

### How Cell-Site Simulators Work

#### Standard Communication

Cellular networks are distributed over geographic areas called "cells." Each cell is served by one transceiver, also known as a cell-site or base station. Your phone naturally connects with the closest base station to provide you service as you move through various cells.

![Phones connecting to cellular networks](https://sls.eff.org/files/sls/wysiwyg/pictures/42/content_CSS-2.png)

Source: EFF

Generally, there are two types of device used by law enforcement that are often referred to interchangeably: passive devices (which we will call IMSI catchers), and active devices (which we will call cell-site simulators.) Passive devices, as a rule, do not transmit any signals. They work by plucking cellular transmissions out of the air, the same way an FM radio works. They then decode (and sometimes decrypt) those signals to find the IMSI of the mobile device and track it.

Active cell-site simulators are much more commonly used by law enforcement, and work very differently from their passive cousins. Cellular devices are designed to connect to the cell site nearby with the strongest signal. To exploit this, cell-site simulators broadcast signals that are either stronger than the legitimate cell sites around them, or are made to appear stronger. This causes devices within range to disconnect from their service providers’ legitimate cell sites and to instead establish a new connection with the cell-site simulator. Cell-site simulators can also take advantage of flaws in the design of cellular protocols (such as 2G/3G/4G/5G) to cause phones to disconnect from a legitimate cell-site and connect to the cell-site simulator instead.  For the purposes of this article we will focus on active cell-site simulators.

It is difficult for most people to know whether or not their phone’s signals have been accessed by an active cell-site simulator, and it is impossible for anyone to know if their phone’s signals have been accessed by a passive IMSI catcher. Apps for identifying the use of cell-site simulators, such as SnoopSnitch, may not be verifiably accurate. Some more advanced tools have been built, which may be more accurate. For instance, security researchers at the University of Washington have [designed a system to measure the use of cell-site simulators across Seattle](https://seaglass.cs.washington.edu/), and EFF researchers [have designed a similar system](https://github.com/EFForg/crocodilehunter/).

### What Kinds of Data Cell-Site Simulators Collect

Data collected by cell-site simulators can reveal intensely personal information about anyone who carries a phone, whether or not they have ever been suspected of a crime.

![Cell-site simulators tricking phones to connect to them. ](https://sls.eff.org/files/sls/wysiwyg/pictures/43/content_CSS-3.png)

Source: EFF

Cell-site simulator surveillance: Cell-site simulators trick your phone into thinking they are base stations.

Once your cellular device has connected to a cell-site simulator, the cell-site simulator can determine your location and trigger your device to transmit its  IMSI for later identification. If the cell-site simulator is able to downgrade the cellular connection to a 2G/GSM connection then it can potentially perform much more intrusive acts such as intercepting call metadata (what numbers were called or called the phone and the amount of time on each call), [the content of unencrypted phone calls and text messages](https://www.justice.gov/sites/default/files/criminal/legacy/2014/10/29/elec-sur-manual.pdf) and some types of data usage (such as websites visited).  Additionally, marketing materials produced by the manufacturers of cell-site simulators indicate that they [can be configured](https://info.publicintelligence.net/Gamma-GSM.pdf) to divert calls and text messages, edit messages, and even spoof the identity of a caller in text messages and calls on a 2G/GSM network.

### How Law Enforcement Uses Cell-Site Simulators

Police can use cell-site simulators to try to locate a person when they already know their phone’s identifying information, or to gather the IMSI (and later the identity) of anyone in a specific area. Some cell-site simulators are small enough to fit in a police cruiser, or even on the vest of an officer, allowing law enforcement officers to drive to multiple locations, capturing from every mobile device in a given area—in some cases [up to 10,000 phones](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/) at a time. These indiscriminate, dragnet searches include phones located in traditionally protected private spaces, such as homes and doctors’ offices.

Law enforcement officers have used information from cell-site simulators to investigate major and minor crimes and civil offenses. [Baltimore Police, for example,](https://www.usatoday.com/story/news/2015/08/23/baltimore-police-stingray-cell-surveillance/31994181/) have used their devices for a wide variety of purposes, ranging from tracking a kidnapper to trying to locate a man who took his wife’s phone during an argument (and later returned it to her). [In one case](https://gizmodo.com/maryland-police-used-an-indiscriminate-cellphone-spy-to-1774831661), Annapolis Police used a cell-site simulator to investigate a robbery involving $56 worth of submarine sandwiches and chicken wings. In Detroit, [U.S. Immigration and Customs Enforcement used a cell-site simulator](https://www.eff.org/deeplinks/2017/05/no-hunting-undocumented-immigrants-stingrays) to locate and arrest an undocumented immigrant. In California, the San Bernardino county sheriff's office [used their cell-site simulator over 300 times in a little over a year](https://arstechnica.com/tech-policy/2018/10/eff-sues-county-sheriff-claims-agency-wont-give-up-stingray-related-records/).

Police may have deployed cell-site simulators at protests. The Miami-Dade Police Department apparently [first purchased a cell-site simulator in 2003 to surveil protestors at a Free Trade of the Americas Agreement conference](http://cdn.arstechnica.net/wp-content/uploads/2013/09/miami-dade.pdf). And it is suspected that they have been used [more recently than that](https://www.law.georgetown.edu/american-criminal-law-review/wp-content/uploads/sites/15/2022/02/59-1-Owsley-George_Floyd_General_Warrants.pdf) during protests against police violence in 2020.

Cell-site simulators [are used](http://www.vocativ.com/389656/stingray-devices-in-trumps-america/) by the FBI, DEA, NSA, Secret Service, and ICE, as well as the U.S. Army, Navy, Marine Corps, and National Guard. U.S. Marshals and the FBI [have attached cell-site simulators to airplanes](https://www.wsj.com/articles/americans-cellphones-targeted-in-secret-u-s-spy-program-1415917533) to track suspects, gathering massive amounts of data about many innocent people in the process. The [Texas Observer](https://www.texasobserver.org/texas-national-guard-spying-devices-surveillance/) also uncovered airborne cell-site simulators in use by the Texas National Guard. In 2023 it was revealed that ICE, DHS, and the Secret Service have all [used cell-site simulators many times without following their own rules on deployment or getting a warrant](https://www.eff.org/deeplinks/2023/03/report-ice-and-secret-service-conducted-illegal-surveillance-cell-phones).

A [recent Congressional Oversight Committee report](https://www.eff.org/deeplinks/2017/02/bipartisan-congressional-oversight-committee-wants-probable-cause-warrants-0) called on Congress to pass laws requiring a warrant before using cell-site simulators. Some states, [such as California](https://www.eff.org/cases/californias-electronic-communications-privacy-act-calecpa), already require a warrant, except in emergency situations.

### Who Sells Cell-site Simulators

Harris Corporation is the most well known company providing cell-site simulators to law enforcement. Their Stingray product has become the catchphrase for these devices, but they have subsequently introduced other models, such as Hailstorm, [ArrowHead](https://www.documentcloud.org/documents/3105805-Arrowhead-1-0-1-Release-Notes.html), [AmberJack, and KingFish](https://www.documentcloud.org/documents/3105793-Gemini-3-3-Quick-Start-Guide.html). Harris has stopped selling cell-site simulator technology to local law enforcement agencies but still works with the federal government. Digital Receiver Technology, a division of Boeing, is also a common supplier of the technology, often referred to as “ [dirtboxes](https://www.revealnews.org/article/chicago-and-los-angeles-have-used-dirt-box-surveillance-for-a-decade/).”

Other sellers of cell-site simulators include Keyw, Octastic, Tactical Support Equipment, Berkeley Varitronics, Cogynte, X-Surveillance, Atos, Rayzone, Martone Radio Technology, Septier Communication, PKI Electronic Intelligence, Datong (Seven Technologies Group), Ability Computers and Software Industries, Gamma Group, Rohde & Schwarz, Meganet Corporation. Manufacturers [Septier](http://www.septier.com/law-enforcement/) and [Gamma GSM](https://info.publicintelligence.net/Gamma-GSM.pdf) both provide information on what the devices can capture. The Intercept published a [secret, internal U.S. government catalogue](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/) of various cellphone surveillance devices, as well as an [older cell-site simulator manual](https://theintercept.com/2016/09/12/long-secret-stingray-manuals-detail-how-police-can-spy-on-phones/) made available through a Freedom of Information Act request.

### Threats Posed by Cell-Site Simulators

Cell-site simulators invade the privacy of everyone who happens to be in a given area, regardless of the fact that the vast majority have not been accused of committing a crime. These are [general searches](https://www.hoover.org/sites/default/files/research/docs/lynch_webreadypdf.pdf) that violate the Fourth Amendment requirement that warrants “particularly” describe who or what is to be searched.

The use of cell-site simulators have been shrouded in government secrecy. Police have used cell-site simulators to track location data without a warrant, by deceptively obtaining “pen register” orders from courts without explaining the true nature of the surveillance. In Baltimore, a judge concluded that law enforcement had [intentionally withheld the information](https://www.aclu.org/other/state-v-andrews-stingray-june-4-2015-transcript?redirect=state-v-andrews-stingray-june-4-2015-transcript) from the defense, in violation of their legal disclosure obligations. For a while, police departments tried to keep the use of cell-site simulators secret from not just the public but also the court system, withholding information from defense attorneys and judges—likely due in part to [non-disclosure agreements](http://www.baltimoresun.com/news/maryland/baltimore-city/bs-md-ci-stingray-case-20150408-story.html) with Harris Corporation. Prosecutors have [accepted plea deals](https://www.washingtonpost.com/world/national-security/secrecy-around-police-surveillance-equipment-proves-a-cases-undoing/2015/02/22/ce72308a-b7ac-11e4-aa05-1ce812b3fdd2_story.html) to hide their use of cell-site simulators and have even [dropped cases](http://arstechnica.com/tech-policy/2015/04/fbi-would-rather-prosecutors-drop-cases-than-disclose-stingray-details/) rather than revealing information about their use of the technology. U.S. Marshalls have [driven files hundreds of miles](https://arstechnica.com/tech-policy/2014/06/us-marshals-step-in-thwart-efforts-to-learn-about-cell-tracking-devices/) to thwart public records requests. Police have [tried to keep information secret](https://www.eff.org/deeplinks/2015/01/2014-review-stingrays-go-mainstream) in Sarasota, Florida, Tacoma, Washington, [Baltimore, Maryland](https://arstechnica.com/tech-policy/2014/11/prosecutors-drop-key-evidence-at-trial-to-avoid-explaining-stingray-use/), and St. Louis, Missouri.

To preserve this secrecy, the [FBI told police officers to recreate evidence](https://theintercept.com/2016/05/05/fbi-told-cops-to-recreate-evidence-from-secret-cell-phone-trackers/) from the devices, according to a document obtained by the nonprofit investigative journalism outlet Oklahoma Watch.

Cell-site simulators often disrupt cell phone communications within as much as a [500-meter radius](http://www.theglobeandmail.com/news/national/rcmp-listening-tool-capable-of-knocking-out-911-calls-memoreveals/article29672075/) of the device, interrupting important communications and even [emergency phone calls](http://www.theglobeandmail.com/news/national/rcmp-listening-tool-capable-of-knocking-out-911-calls-memoreveals/article29672075/).  Cell-site simulators have been shown to disproportionately affect low-income communities and communities of color. In Baltimore, the use of cell-site simulators disproportionately impacted African-American communities, according to a map included in an [FCC complaint](https://www.eff.org/deeplinks/2016/08/civil-liberties-groups-file-fcc-complaint-arguing-baltimore-police-are-illegally) that overlaid where Baltimore Police were using stingrays over census data on the city’s black population.

[Cell-site simulators can also disrupt emergency calls](https://www.eff.org/deeplinks/2018/08/blog-post-wyden-911-disruption-css), such as 911 in the US, making them not only a menace to privacy but to public safety as well.

Cell-site simulators rely on vulnerabilities in our communications system that the government should help fix rather than exploit.

### EFF’s Work on Cell-Site Simulators

For the reasons above, EFF opposes police use of cell site simulators. Insofar as law enforcement agencies are using cell-site simulators in criminal investigations, EFF argues that use should be limited in the following ways:

1. Law enforcement should obtain individualized warrants based on probable cause;
2. Cell-site simulators should only be used for serious, violent crimes;
3. Cell-site simulators should only be used for identifying location of a particular phone;
4. Law enforcement must minimize the collection of data from people who are not the targets of the investigation.
5. Companies making cell-site simulators must confirm that their technology does not disrupt calls to emergency services.

#### Litigation

We [filed a Freedom of Information Act lawsuit](https://www.eff.org/press/releases/eff-files-foia-suit-over-us-marshals-spy-planes) to expose and shine light on the U.S. Marshals Service’s use of cell-site simulators on planes.

Along with the ACLU and ACLU of Maryland, we [filed an amicus brief](https://www.eff.org/deeplinks/2015/12/eff-joins-aclu-amicus-brief-supporting-warrant-requirement-cell-site-simulators) in the first case in the country where a judge threw out evidence obtained as a result of using a cell-site simulator without a warrant.

We filed an amicus brief, along with the ACLU, pointing a court to facts indicating that the Milwaukee Police Department secretly used a cell-site simulator to locate a defendant through his cell phone without a warrant in U.S. vs. Damian Patrick. (The government then [admitted](https://www.eff.org/document/us-v-patrick-government-letter-admitting-stingray-use) to having used it.)

#### Legislation

We were original co-sponsors of the [California Electronic Communications Privacy Act (CalECPA)](https://www.eff.org/cases/californias-electronic-communications-privacy-act-calecpa), along with the ACLU and the California Newspaper Publisher Association. This law requires California police to get a warrant before using a cell-site simulator. Any evidence obtained from a cell-site simulator without a warrant is inadmissible in court.

EFF supported S.B. 741, which requires transparency measures regarding the use of cell-site simulators. We [collected many of these policies](https://www.eff.org/deeplinks/2016/04/here-are-79-policies-california-surveillance-tech-where-are-other-90).

#### Further Research

We have written a report on the [technical means possibly used by cell-site simulators called “Gotta Catch ‘em All”](https://www.eff.org/wp/gotta-catch-em-all-understanding-how-imsi-catchers-exploit-cell-networks), and we have developed a proof of concept technical means of [detecting cell-site simulators called Crocodile Hunter](https://github.com/EFForg/crocodilehunter).

### EFF Cases

[State of Maryland v. Kerron Andrews](https://www.eff.org/cases/state-maryland-v-kerron-andrews)

[U.S. v. Damian Patrick](https://www.eff.org/cases/us-v-damian-patrick)

[EFF v. U.S. Department of Justice](https://www.eff.org/cases/us-marshals-airborne-imsi-catchers)

### **Suggested Additional Reading**

[Stingray Tracking Devices: Who's Got Them?](https://www.aclu.org/issues/privacy-technology/surveillance-technologies/stingray-tracking-devices-whos-got-them) (ACLU)

[Your Secret Stingray's No Secret Anymore: The Vanishing Government Monopoly over Cell Phone Surveillance and Its Impact on National Security and Consumer Privacy](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2437678)(Harvard Journal of Law and Technology)

[Examining Law Enforcement Use of Cell Phone Tracking Devices](https://oversight.house.gov/hearing/examining-law-enforcement-use-of-cell-phone-tracking-devices/) (House Oversight Committee)

[The Relentless “Eye” Local Surveillance: Its Impact on Human Rights and Its Relationship to National and International Surveillance](http://centerformediajustice.org/resources/the-relentless-eye/)(Center for Media Justice and others)

[Department of Justice Policy Guidance: Use of Cell-Site Simulator Technology](https://www.justice.gov/opa/file/767321/download) (U.S. Department of Justice)

[Long-Secret Stingray Manuals Detail How Police Can Spy on Phones](https://theintercept.com/2016/09/12/long-secret-stingray-manuals-detail-how-police-can-spy-on-phones/)  (The Intercept)

[A Secret Catalogue of Government Gear for Spying on Your Cellphone](https://theintercept.com/2015/12/17/a-secret-catalogue-of-government-gear-for-spying-on-your-cellphone/) (The Intercept)

[Cops Turn to Canadian Phone-Tracking Firm After Infamous 'Stingrays' Become 'Obsolete'](https://gizmodo.com/american-cops-turns-to-canadian-phone-tracking-firm-aft-1845442778) (Gizmodo)

_Most recently updated March 29th, 2023_

[Technologies](https://sls.eff.org/)