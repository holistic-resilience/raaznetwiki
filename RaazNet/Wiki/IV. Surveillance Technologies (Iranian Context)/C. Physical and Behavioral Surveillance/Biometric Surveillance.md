---
title: "Biometric Surveillance"
tags: [biometrics, surveillance, privacy, law-enforcement, dna, facial-recognition, iris-scanning, tattoo-recognition]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Biometric Identification", "Law Enforcement Surveillance", "Privacy Rights", "Civil Liberties"]
summary: "Comprehensive guide to biometric surveillance methods including DNA collection, tattoo recognition, and iris scanning used by law enforcement."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of privacy concepts", "Familiarity with law enforcement practices"]
estimated_read_time: "25 minutes"
---

# Biometric Surveillance

Biometric surveillance encompasses a collection of methods for tracking individuals using physical or biological characteristics, ranging from fingerprint and DNA collection to gait recognition and heartbeat tracking.

These methods rely heavily on algorithms to identify certain characteristics from a sample, like the image of a face or the sound of a voice, and match it to one other particular sample or a group of samples.

## Fundamental Concerns

Biometric identification can be flawed due to:
- **Algorithm issues** - Errors in the underlying software
- **Training data gaps and biases** - Incomplete or prejudiced datasets
- **Sample quality problems** - Poor quality inputs leading to misidentification

For example, gait analysis (using walking patterns to identify a person) depends on movement that can vary based on fatigue level, footwear, environmental conditions, and health. Voice recognition depends on voiceprints, which can be mimicked by AI-generated spoofs.

Because biometric features are unique and irreplaceable, this type of surveillance is particularly concerning. A person cannot simply change their eyes or DNA in the way they can change a password or credit card. Tracking done in this way can be extremely and persistently intrusive. The black box nature of many biometric identification systems can perpetuate patterns of biased policing and result in errors that are difficult to defend against.

---

## DNA Collection and Searches

A DNA sample can reveal our entire genetic makeup, including deeply private and sensitive information such as:
- Ancestry
- Biological relationships
- Propensity for certain medical conditions

Although DNA has been used by law enforcement since the 1980s, technology and police methods have evolved significantly.

### Current State of DNA Collection

DNA collection has become mandatory for those convicted of or arrested for many crimes. In the United States, this information is entered into the **Combined DNA Index System (CODIS)**, maintained by the FBI. This database contains:
- Nearly **16 million offender profiles**
- **5 million arrestee profiles**

Previously, useful forensic samples could only be obtained from blood, semen, or other bodily fluids. Today, forensic investigators can detect, collect, and analyze trace amounts of DNA from objects a person merely touches.

### Forensic Genetic Genealogy (FGG) Searches

Forensic genetic genealogy searches differ from traditional criminal DNA searches in several key ways:

| Aspect | CODIS Database | Genetic Genealogy Databases |
|--------|---------------|----------------------------|
| **Maintenance** | Government-maintained | Privately maintained |
| **Data Source** | Mandatory collection from offenders/arrestees | Voluntarily submitted by consumers |
| **Regulation** | Subject to state and federal statutes | No specific laws governing collection and sharing |
| **Data Volume** | 13-20 loci (STR markers) | 500,000+ SNPs |
| **Information Revealed** | Limited identification | Family members, distant ancestors, disease propensity |

#### Risks of FGG Searches

Police have used FGG searches in high-profile cases, including ones implicating innocent people:

- **Golden State Killer case**: An earlier search pointed to a different person before the actual perpetrator was identified
- **2014 Idaho cold case**: A search led police to suspect an innocent man
- **2012 California case**: A man spent five months in jail after a database search linked his DNA to a murder victim—although he was hospitalized when the murder occurred. Paramedics may have transferred his DNA when they responded to the crime scene

EFF has filed briefs in multiple cases challenging DNA collection and FGG searches, and has advocated for legislative restrictions on how these searches are conducted. Maryland and Montana have passed the nation's first laws restricting law enforcement access to genetic genealogy databases.

### Probabilistic Genotyping Software

DNA samples used in criminal prosecutions are generally of low quality, making them complicated to analyze. Probabilistic genotyping software is often used to determine whether a suspect's DNA matches crime scene samples. However, this software has significant issues:

- **Accuracy concerns**
- **Human-inputted bias**
- **Opaque processes and algorithms**

When these results are used in criminal cases, defendants should have the right to evaluate any DNA analysis tool's source code. EFF has successfully argued in state and federal courts that information regarding probabilistic genotyping software must be provided to the defense.

---

## Tattoo Recognition

Tattoo recognition technology uses images of people's tattoos to:
- Identify individuals
- Reveal information about religion or political beliefs
- Associate people with others who have similar tattoos

This technology is being actively developed by private companies with support from federal agencies, state law enforcement, and universities. Researchers test and train the technology using photographs of incarcerated people or from social media, raising critical issues of ethics, privacy, and First Amendment rights.

### How Tattoo Recognition Works

1. An image of a tattoo is captured and submitted to the system
2. Image recognition software creates a mathematical representation
3. The system analyzes the image for specific details
4. Those details are matched against images in the database
5. Humans may tag images with metadata to further describe or categorize them

### Data Collection Methods

According to NIST's "Best Practices" for tattoo recognition:

- **Two photographs** of each tattoo: one close-up, one showing body location
- **Large tattoos**: Full photo plus photos of particular areas of interest
- **Detention environments**: Images may be collected from the entire body, including areas not publicly visible (upper legs, chest, genital areas)
- **Metadata tagging**: Position on body, ink color, and imagery categories (political symbols, sports icons, specific images like dragons or flags)

Law enforcement may also collect images:
- In the field during routine police stops
- From online websites and social media

### Law Enforcement Applications

Before automation, tattoo recognition involved maintaining binders of photographs, similar to mugshot books. In recent years, departments have digitized these images and added them to databases with tagged metadata.

NIST-identified uses for law enforcement include:
- Identifying a person by their tattoos
- Identifying suspects whose tattoos are partially visible on cameras
- Discerning the meaning of tattoos by matching to similar imagery
- Mapping connections between people with similar tattoos

**Real-world deployments:**

- **Gang Graffiti Automatic Recognition and Interpretation (GARI)**: A project between Purdue University and Indiana State Police allowing law enforcement nationwide to share photos of graffiti and gang tattoos with timestamps and GPS coordinates
- **Arizona Department of Public Safety**: Using tattoo recognition since 2022, built on more than one million images from criminal bookings

### Vendors

Companies selling tattoo recognition technology include:
- Idemia (formerly OT-Morpho or Safran)
- Face Forensics
- DataWorks
- Rank One Computing
- Neurotechnology

Universities involved in development:
- University of Michigan (with Idemia)
- Purdue University (with Indiana State Police)
- French Alternative Energies and Atomic Energy Commission
- Fraunhofer Institute
- MITRE Corporation

### Threats and Concerns

#### First Amendment Implications

Tattoos often represent personal beliefs and affiliations. Law enforcement could use this technology as a proxy to create lists of people based on:
- Religion
- Nationality
- Political ideologies
- Common interests

#### Misidentification Risks

Assumptions about tattoos can be wrong:
- A Jewish person with a Star of David tattoo could be affiliated with a Chicago street gang whose members also wear six-pointed star tattoos
- A person who obtained a gang-affiliated tattoo as a teenager may still be categorized as a gang member decades later

#### Immigration Enforcement

- An immigrant with DACA status was detained and fast-tracked for deportation because officials claimed he had a gang tattoo (he said it signified his place of birth)
- Immigrants have sought tattoo removal services to avoid deportation

### EFF's Work on Tattoo Recognition

Through FOIA and public records requests, EFF has exposed various tattoo recognition programs:

- Revealed that NIST scientists ignored ethical obligations for experiments with inmate images
- Successfully pressured NIST to overhaul privacy safeguards and redact sensitive images
- Filed a 2017 lawsuit against the U.S. Department of Commerce, Justice, and Homeland Security
- Won access to records revealing which agencies used the database
- Pushed institutions to cease use of the system—roughly a third deleted the problematic data or reported never receiving/using it

**Related Legal Case:** [EFF v. U.S. Department of Commerce, Department of Justice, Department of Homeland Security](https://www.eff.org/cases/nist-tattoo-recognition-technology-program-foia)

---

## Iris Recognition

Iris recognition (or iris scanning) uses visible and near-infrared light to photograph a person's iris. Advocates claim it allows law enforcement to compare iris images against existing databases to determine or confirm identity, and that iris scans are quicker and more reliable than fingerprints since it's easier to alter fingers than eyes.

### How Iris Recognition Works

1. **Illumination**: Infrared light illuminates the iris to reveal unique patterns invisible to the naked eye
2. **Detection**: Scanners detect and exclude eyelashes, eyelids, and reflections
3. **Extraction**: A set of pixels containing only the iris is isolated
4. **Analysis**: The pattern of lines and colors is analyzed to extract a bit pattern
5. **Comparison**: The digitized pattern is compared to stored templates for:
   - **Verification**: One-to-one matching
   - **Identification**: One-to-many matching

**Scanner types:**
- Wall-mounted or fixed location
- Handheld and portable
- Long-range scanners (researchers at Carnegie Mellon are developing scanners that could capture images surreptitiously from up to 40 feet away)

### Data Collected

- Approximately **240 biometric features** unique to every eye
- Digital representation stored in computer databases
- Sometimes used in conjunction with fingerprints and face recognition

### Vendors

Companies selling iris recognition technology include:
- Aware
- BioID
- Biometric Intelligence and Identification Technologies
- Crossmatch
- EyeCool
- EyeLock
- Gemalto
- Idemia
- Iridian Technologies
- Iris Guard
- Iris ID
- IriTech
- NEC
- Neurotechnology
- Panasonic
- SRI International
- Tascent
- Thales
- Unisys

### Law Enforcement Applications

#### Federal Level

- **FBI Next Generation Identification (NGI) System**: Added iris recognition in December 2020
  - Database of more than 1.3 million samples from federal, state, and local law enforcement
  - Texas Department of Criminal Justice contributed 110,000+ iris samples from incarcerated individuals

- **U.S. Military**: Used iris scanning devices to identify detainees in Iraq and Afghanistan
  - SEEK II handheld device takes iris scans, fingerprints, and face scans
  - Data ports back to FBI database in West Virginia in seconds

- **Department of Homeland Security**: HART (Homeland Advanced Recognition Technology) System
  - Primary biometric database accessible to DHS components, law enforcement partners, and international entities
  - Includes 1-to-Many iris database

- **Customs and Border Protection**: At least four iris scanners at checkpoints; recording iris scans for migrants

- **TSA**: Using iris scanners at some airports

#### State and Local Level

- **NYPD**: Among the first to use iris recognition (BI2 Technologies' MORIS system, fall 2010)
  - Reports of arrestees being held longer for declining iris photographs despite the "voluntary" program
  - Uses iris recognition for identity verification at arraignment

- **Border Sheriffs**: Iris recognition devices installed in every sheriff's department along the U.S.-Mexico border
  - BI2 offered free three-year trials of stationary iris capture devices
  - Scans added to BI2's private database (close to a million iris scans from 180+ jurisdictions)
  - Database housed by third-party vendor in San Antonio with three disaster backup facilities

- **Prisons**: Rhode Island Department of Corrections, Tennessee Bureau of Investigation

- **California**: Orange County and Los Angeles County sheriff offices had plans to implement iris scanning (2015)

- **Schools**: Some have tested iris recognition for access control

### Threats and Concerns

#### Mass Surveillance Risk

The biggest threat is a national database that can track people covertly, at a distance or in motion, without knowledge or consent. Long-range iris scanners could potentially identify people simply glancing in their rearview mirror after being pulled over.

#### Immigration Enforcement

Grave concerns exist about local law enforcement sharing biometric data with federal immigration agencies like ICE, which has direct access to many law enforcement databases.

#### Technical Limitations

No biometric is foolproof:

- **2009 study**: Patients with acute iris inflammation caused recognition systems to fail
- **2012 NIST report**: Iris recognition technology was inaccurate 1-10% of the time for crowd identification
- **Miss rates**: 2.5% to 20% or higher for single irises

Quality problems include:
- Poor subject presentation (closed eye, rotated iris, off-axis gaze)
- Capture environment issues (motion blur, reflections, lighting problems)
- Image processing problems (compression, corruption)
- Unusual individual characteristics (abnormal pupil shapes)

#### Security Vulnerabilities

It is possible to trick or bypass iris scanners:

- **2012**: Security researchers at Universidad Autonoma de Madrid recreated iris images from digital codes in security databases
- **2017**: Chaos Computer Club bypassed Samsung Galaxy S8 iris authentication using a night-mode photograph, a printer, and a contact lens

#### Data Security Risks

- Unclear what steps agencies take to secure biometric data
- Databases are honeypots for criminals
- Data breaches and hacks occur regularly
- Law enforcement can be careless—a military iris scanning device was sold on eBay with information still on it
- Biometric information cannot be revoked, canceled, or reissued if compromised
- Law enforcement often stores iris biometrics on vendor-operated databases, giving companies access to criminal justice data

---

## Additional Resources

### DNA and Genetic Genealogy
- [EFF: How Your DNA—Or Someone Else's—Can Send You to Jail](https://www.eff.org/deeplinks/2021/05/how-your-dna-or-someone-elses-can-send-you-jail)
- [EFF: Maryland and Montana Pass Nation's First Laws Restricting Law Enforcement Access](https://www.eff.org/deeplinks/2021/06/maryland-and-montana-pass-nations-first-laws-restricting-law-enforcement-access)

### Tattoo Recognition
- [EFF: 5 Ways Law Enforcement Will Use Tattoo Recognition Technology](https://www.eff.org/deeplinks/2016/05/5-ways-law-enforcement-will-use-tattoo-recognition-technology)
- [EFF: Tattoo Recognition Research Threatens Free Speech and Privacy](https://www.eff.org/deeplinks/2016/06/tattoo-recognition-research-threatens-free-speech-and-privacy)
- [NIST Tattoo Recognition Technology Program](https://www.nist.gov/programs-projects/tattoo-recognition-technology)

### Iris Recognition
- [The Intercept: The Biometric Frontier](https://theintercept.com/2017/07/08/border-sheriffs-iris-surveillance-biometrics/)
- [Cambridge University: How Iris Recognition Works](http://www.cl.cam.ac.uk/~jgd1000/irisrecog.pdf)
- [EFF: California Cops Are Using These Biometric Gadgets in the Field](https://www.eff.org/deeplinks/2015/11/how-california-cops-use-mobile-biometric-tech-field)
- [Policing Project: Iris Recognition Primer](https://www.policingproject.org/news-main/2019/9/20/policing-project-five-minute-primers-iris-recognition)
- [NIST: IREX 10 Identification Track](https