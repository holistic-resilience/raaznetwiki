---
title: "Biometric Surveillance: A Comprehensive Guide"
tags: [biometrics, surveillance, privacy, law-enforcement, dna, facial-recognition, iris-scanning, tattoo-recognition]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy Advocates, Legal Professionals]
topics: ["Digital Security", "Privacy Protection", "Civil Liberties", "Law Enforcement Technology"]
summary: "Comprehensive guide to biometric surveillance technologies including DNA collection, tattoo recognition, and iris scanning—how they work, who uses them, and their threats to privacy."
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

## Why Biometric Surveillance Is Concerning

Biometric identification can be flawed due to:
- Issues in the algorithm
- Gaps and biases in the training data
- Problems with the samples used

For example, **gait analysis** (using walking patterns to identify a person) depends on movement that can vary based on fatigue level, footwear, environmental conditions, and health. **Voice recognition** depends on voiceprints, which can be mimicked by AI-generated spoofs.

Because biometric features are unique and irreplaceable, this type of surveillance is particularly concerning. A person cannot simply change their eyes or DNA in the way they can change a password or credit card. Tracking done in this way can be extremely and persistently intrusive. Further, the black box nature of many types of biometric identification can perpetuate patterns of biased policing and result in errors that can be difficult to defend against.

---

## DNA Collection and Searches

A DNA sample can reveal our entire genetic makeup, including deeply private and sensitive information such as:
- Ancestry
- Biological relationships
- Propensity for certain medical conditions

Although DNA has been used by law enforcement since the 1980s, the technology and police methods have evolved significantly.

### Current DNA Collection Practices

DNA collection has become mandatory for those convicted of or even arrested for many crimes. In the United States, this information is entered into the national **Combined DNA Index System (CODIS)** database, maintained by the FBI. This database contains:
- Nearly **16 million offender profiles**
- **5 million arrestee profiles**

Previously, a useful forensic sample could only be obtained from blood, semen, or other bodily fluids. Today, forensic investigators can detect, collect, and analyze trace amounts of DNA from objects a person merely touches.

### Genetic Genealogy Searches

Forensic genetic genealogy (FGG) searches differ from traditional criminal DNA searches in several key respects:

| Aspect | CODIS Database | Genetic Genealogy Databases |
|--------|----------------|----------------------------|
| **Maintenance** | Government-maintained | Privately maintained |
| **Data Source** | Mandatory collection | Voluntarily submitted by consumers |
| **Regulation** | Subject to state and federal statutes | No specific laws governing collection, handling, or sharing |
| **Data Scope** | 13-20 loci (non-coding regions) | 500,000+ SNPs (can reveal health traits) |
| **Relationship Detection** | Some biological familial relationships | Distant and indirect familial relationships |

#### High-Profile Cases and Concerns

Police have used FGG searches in high-profile cases, including ones implicating innocent people:

- **Golden State Killer Case**: While ultimately successful, an earlier search pointed to a different person as the likely perpetrator
- **Idaho Cold Case (2014)**: A similar search led police to suspect an innocent man
- **California DNA Match (2012)**: A man spent five months in jail after a database search linked his DNA to a murder victim's fingernails—despite being hospitalized when the murder occurred. Prosecutors believe paramedics may have transferred his DNA to the victim.

EFF has filed briefs in multiple cases challenging DNA collection and FGG searches, and has advocated for legislative restrictions on how FGG searches are conducted.

### Probabilistic Genotyping Software

DNA samples used in criminal prosecutions are generally of low quality, making them particularly complicated to analyze. A new generation of **probabilistic genotyping software** is often used to determine whether a suspect's DNA matches samples found at a crime scene.

**Key Issues:**
- Accuracy concerns
- Human-inputted bias
- Opaque processes and algorithms

When these results are used in criminal cases, defendants should have the right to evaluate any DNA analysis tool's source code. EFF has successfully argued in state and federal courts that information regarding probabilistic genotyping software must be provided to the defense.

---

## Tattoo Recognition

Tattoo recognition technology uses images of people's tattoos to:
- Identify individuals
- Reveal information about their religion or political beliefs
- Associate them with people who have similar tattoos

The technology is actively developed by private companies with support from federal agencies, state law enforcement, and universities.

### How Tattoo Recognition Works

Tattoo recognition functions similarly to face recognition:

1. An image of a tattoo is captured and submitted to the system
2. Image recognition software creates a mathematical representation
3. The system analyzes the image for specific details
4. Those details are matched against images already in the database
5. Humans can tag images with metadata to further describe or categorize them

### Data Collection Practices

The National Institute of Standards and Technology (NIST) has developed "Best Practices" for capturing tattoo images:

- Two photographs of each tattoo (one close-up, one showing body location)
- Full photos of large tattoos plus photos of areas of interest
- In detention environments, images may be collected from the entire body, including non-publicly visible areas

**Metadata Tagging:**
The ANSI/NIST-ITL Standard has dozens of codes to categorize imagery, from general categories (political symbols, sports icons) to specific images (dragon, American flag).

Law enforcement may also collect images:
- In the field during routine police stops
- From websites or social media

### Law Enforcement Applications

NIST identified several uses for tattoo recognition technology:

1. Identifying a person by their tattoos
2. Identifying suspects whose tattoos are partially caught on cameras
3. Discerning the meaning of tattoos by matching to similar imagery
4. Mapping connections between people with similar tattoos

**Real-World Deployments:**

- **Gang Graffiti Automatic Recognition and Interpretation (GARI)**: A collaboration between Purdue University and Indiana State Police allowing law enforcement nationwide to share photos of graffiti and gang tattoos with timestamps and GPS coordinates

- **Arizona Department of Public Safety**: Using tattoo recognition since 2022, built on more than a million images from criminal bookings

### Vendors

Major vendors include:
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

**First Amendment Implications:**
Tattoos often represent religious beliefs, political ideologies, or cultural affiliations. Using this technology, law enforcement could create lists of people based on their religion, nationality, political beliefs, or common interests.

**Misidentification Risks:**
- A Jewish person with a Star of David tattoo could be affiliated with a Chicago street gang whose members also wear six-pointed star tattoos
- A person who obtained a gang-affiliated tattoo as a teenager may still be categorized as a gang member decades later

**Immigration Enforcement:**
- An immigrant with DACA status was detained and fast-tracked for deportation because officials claimed he had a gang tattoo (he said it represented his place of birth)
- Immigrants are seeking tattoo removal services to avoid deportation

### EFF's Work on Tattoo Recognition

Through FOIA and public records requests, EFF has exposed various tattoo recognition programs:

- Revealed that NIST scientists ignored ethical obligations for experiments with images taken from inmates
- Successfully pressured NIST to overhaul privacy safeguards
- Filed a lawsuit (November 2017) against Commerce, Justice, and Homeland Security departments
- Won access to records revealing agencies using the database
- Approximately one-third of institutions that requested problematic data deleted it or reported never receiving/using it

---

## Iris Recognition

Iris recognition or iris scanning uses visible and near-infrared light to take a high-contrast photograph of a person's iris. It is a form of biometric technology in the same category as face recognition and fingerprinting.

### How Iris Recognition Works

1. Iris scanners illuminate the iris with invisible infrared light
2. The system picks up unique patterns not visible to the naked eye
3. Eyelashes, eyelids, and reflections are detected and excluded
4. The pattern of lines and colors is analyzed to extract a bit pattern
5. This pattern is digitized and compared to stored templates

**Scanner Types:**
- Wall-mounted or fixed location
- Handheld and portable
- Long-range scanners (researchers at Carnegie Mellon are developing scanners that could capture images from up to 40 feet away)

### Data Collection

Iris scanners collect around **240 biometric features**, the combination of which is unique to every eye. The numeric representation is stored in computer databases.

Iris scanning is sometimes used in conjunction with other biometrics, such as fingerprints and face recognition.

### Law Enforcement Applications

**Federal Level:**
- FBI added iris recognition to its Next Generation Identification (NGI) System in December 2020
- Database contains more than 1.3 million samples from federal, state, and local law enforcement
- Texas Department of Criminal Justice contributed more than 110,000 iris samples from incarcerated individuals

**Military Use:**
- U.S. military used iris scanning devices to identify detainees in Iraq and Afghanistan
- SEEK II handheld device takes iris scans, fingerprints, and face scans and ports data to FBI database in seconds

**Local Police:**
- NYPD was among the first to use iris recognition (fall 2010)
- Reports of arrestees being held longer for declining iris photographs
- NYPD uses iris recognition for identity verification at arraignment

**Border and Immigration:**
- Department of Homeland Security uses the Homeland Advanced Recognition Technology (HART) System
- Customs and Border Protection employs at least four iris scanners at checkpoints
- TSA has begun using iris scanners at some airports

**Private Sector:**
- BI2 Technologies offered free three-year trials to border sheriffs
- BI2's private database has close to a million iris scans from over 180 law enforcement jurisdictions
- Database housed by third-party vendor in San Antonio with three disaster backup facilities

### Vendors

Major vendors include:
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

### Threats and Concerns

**Covert Mass Surveillance:**
The biggest threat is a national database that can track people covertly, at a distance or in motion, without their knowledge or consent. Law enforcement could potentially use long-range scanners on people simply glancing in their rear-view mirror after being pulled over.

**Immigration Enforcement:**
Local law enforcement sharing biometric data with federal agencies like ICE raises grave concerns.

**Accuracy Issues:**

| Study/Report | Finding |
|--------------|---------|
| 2009 Research Study | Patients with acute iris inflammation caused systems to fail |
| 2012 NIST Report | Iris recognition was inaccurate 1-10% of the time for crowd identification |
| Single Iris Miss Rates | Ranged from 2.5% to 20% or higher |

**Quality Problems Include:**
- Poor subject presentation (closed eye, rotated iris, off-axis gaze)
- Capture environment issues (motion blur, defocus, reflections, broken LEDs)
- Image processing problems (compression, corruption)
- Unusual individual characteristics (abnormal pupil shapes)

**Security Vulnerabilities:**

- **2012**: Researchers at Universidad Autonoma de Madrid recreated iris images from digital codes in security databases
- **2017**: Chaos Computer Club hackers bypassed Samsung Galaxy S8 iris authentication using a printed photograph with a contact lens superimposed
- **Data Breaches**: A military device used to scan irises was sold on eBay with information still on it

**Data Security Concerns:**
- Unclear what steps agencies take to secure biometric data
- Biometric databases are honeypots for criminals
- Biometric information cannot be revoked, canceled, or reissued if compromised
- Law enforcement often stores data on databases operated by vendors and private third parties

---

## Additional Resources

### EFF Legal Cases
- [EFF v. U.S. Department of Commerce, Department of Justice, Department of Homeland Security](https://www.eff.org/cases/nist-tattoo-recognition-technology-program-foia)

### Further Reading

**Tattoo Recognition:**
- [5 Ways Law Enforcement Will Use Tattoo Recognition Technology](https://www.eff.org/deeplinks/2016/05/5-ways-law-enforcement-will-use-tattoo-recognition-technology) (EFF)
- [Tattoo Recognition Research Threatens Free Speech and Privacy](https://www.eff.org/deeplinks/2016/06/tattoo-recognition-research-threatens-free-speech-and-privacy) (EFF)
- [NIST Tattoo Recognition Technology Program](https://www.nist.gov/programs-projects/tattoo-recognition-technology)

**Iris Recognition:**
- [The Biometric Frontier: Border Sheriffs Expand Iris Surveillance](https://theintercept.com/2017/07/08/border-sheriffs-iris-surveillance-biometrics/) (The Intercept)
- [How Iris Recognition Works](http://www.cl.cam.ac.uk/~jgd1000/irisrecog.pdf) (Cambridge University)
- [California Cops Are Using These Biometric Gadgets in the Field](https://www.eff.org/deeplinks/2015/11/how-california-cops-use-mobile-biometric-tech-field) (EFF)
- [Five Minutes Primers: Iris Recognition](https://www.policingproject.org/news-main/2019/9/20/policing-project-five-minute-primers-iris-recognition) (Policing Project)
- [IREX 10: Identification Track](https://pages.nist.gov/IREX10/) (NIST)

---

*Most recently updated October 1, 2023*

*Source: Electronic Frontier Foundation - Street Level Surveillance*