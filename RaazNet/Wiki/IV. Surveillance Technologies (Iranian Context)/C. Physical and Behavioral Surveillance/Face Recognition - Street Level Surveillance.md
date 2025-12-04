---
title: "Face Recognition - Street Level Surveillance"
tags: [face-recognition, biometrics, surveillance, law-enforcement, privacy, civil-liberties]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Legal Professionals]
topics: ["Biometric Surveillance", "Law Enforcement Technology", "Privacy Rights", "Civil Liberties"]
summary: "Comprehensive EFF guide on face recognition technology, how law enforcement uses it, its threats to privacy and civil liberties, and advocacy efforts to restrict its use."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of digital privacy concepts", "Familiarity with law enforcement practices"]
estimated_read_time: "18 minutes"
---

# Face Recognition

Face recognition is a biometric technology that uses a face or the image of a face to identify or verify the identity of an individual in photos, video, or in real-time. It is commonly used by law enforcement and private businesses. Face recognition systems depend on databases of individuals' images to train their underlying algorithms.

Face recognition can be applied retroactively to video footage and photographs, and it can be used in coordination with other surveillance technologies and databases when creating profiles of individuals—including those who may never have been involved in a crime. It facilitates the tracking of individuals across video feeds and can be integrated into camera systems and other technologies, as we have seen at sporting events in the United States.

## Key Concerns

Face recognition can be prone to failures in its design and in its use, which can implicate people for crimes they haven't committed and make people into targets of unwarranted or dangerous retaliation.

**Disproportionate Impact:** Facial recognition software is particularly bad at recognizing:
- Black people and other ethnic minorities
- Women
- Young people
- Transgender and nonbinary individuals

People in these demographic groups are especially at risk of being misidentified by this technology and are disparately impacted by its use. Face recognition contributes to the mass surveillance of individuals, neighborhoods, and populations that have historically been targeted by unfair policing practices, and it has been used to target people engaging in protected speech.

Hundreds of law enforcement agencies and a rapidly growing number of private entities use face recognition across the United States. Its use in other countries is also growing.

## How Face Recognition Works

Face recognition systems use computer algorithms to pick out specific, distinctive details about a person's face and make a judgment of its similarity to other faces. Details such as distance between the eyes or shape of the chin are converted into a mathematical representation and compared to data on other faces collected in a face recognition database.

### Key Terminology

- **Face template:** Data about a particular face designed to only include certain details that can be used to distinguish one face from another (distinct from a photograph)
- **Face detection:** Identifying whether an image contains a face at all
- **Face analysis:** Assessment of certain traits (like skin color and age) based on the image of a face
- **Face verification:** Comparing the image of a known individual against another image to confirm both represent the same person
- **Face identification:** Comparing a sample image of an unknown individual against a collection of known faces to find a match

Some face recognition systems calculate a probability match score between an unknown person and specific face templates stored in the database, offering several potential matches ranked by likelihood rather than returning a single result.

### Accuracy Challenges

Face recognition systems vary in their ability to identify people under challenging conditions such as:
- Poor lighting
- Low quality image resolution
- Suboptimal angle of view

**Error Types:**
- **False negative:** The system fails to match a person's face to an image that is actually in the database, erroneously returning zero results
- **False positive:** The system matches a person's face to an incorrect image in the database (e.g., submitting an image of "Joe" but the system identifies them as "Jack")

When researching a face recognition system, it is important to examine both rates, as there is almost always a trade-off. If the result of a misidentification is that an innocent person goes to jail, the system should be designed to minimize false positives.

## How Law Enforcement Uses Face Recognition

Many local police agencies, state law enforcement, and federal agencies use face recognition in routine patrolling and policing. Scores of databases facilitate face recognition use at local, state, and federal levels.

### Access and Capabilities

Law enforcement may access face recognition systems through:
- Private platforms
- Systems designed internally
- Systems developed by other government agencies

These databases can query images from:
- Social media
- Closed-circuit television (CCTV)
- Traffic cameras
- Photographs taken by officers in the field

Faces may also be compared in real-time against "hot lists" of people suspected of illegal activity.

### Federal Use

The use of face recognition by federal law enforcement agencies is widespread. Agencies use it to:
- Generate investigative leads
- Access devices
- Get authorization to enter physical locations

**Key Statistics (July 2021 GAO Report):**
- At least 20 of 42 federal agencies with policing powers have their own or use another government agency's face recognition system
- Agencies reported accessing one or more of 27 different federal face recognition databases
- Face recognition systems in 29 states are accessed by federal law enforcement
- At least 10 federal agencies do not track their use of non-federal face recognition technology

### Border and Airport Use

Law enforcement increasingly uses face recognition to verify identities of individuals crossing the border or flying through U.S. airports:
- **TSA:** Introduced technology to 16 major airports as of early 2023
- **CBP:** Implemented face recognition at 32 airports for passengers leaving and entering the United States

### FBI Systems

**Next Generation Identification Database:**
- Contains more than 30 million face recognition records
- Allows state and local agencies "lights out" access (no federal human review of individual searches)
- States reciprocally allow FBI access to their criminal face recognition databases

**Facial Analysis, Comparison and Evaluation (FACE) Services:**
- Dedicated FBI team for face recognition searches
- Can access more than 400 million non-criminal photos from state DMVs and the State Department
- At least 16 U.S. states allow FACE access to driver's license and ID photos
- As of 2019, conducted nearly 400,000 searches

### State and Local Use

**Prevalence:**
- Over a quarter of all state and local law enforcement agencies can run face recognition searches
- As of September 2023, EFF's Atlas of Surveillance cataloged nearly 900 municipal, county, and state agencies using face recognition

**Mobile Face Recognition:**
Officers can use smartphones, tablets, or other portable devices to photograph individuals in the field and immediately compare against databases.

**DMV Integration:**
- More than half of all U.S. adults have their likeness in at least one face recognition database (Georgetown University research)
- At least 43 states have used face recognition with DMV databases to detect fraud
- At least 26 states allow law enforcement to search driver license databases

### Notable Examples

- **Pinellas County Sheriff's Office (Florida):** Maintains one of the largest local databases with more than 38 million images (as of June 2022), accessible by 263 different agencies
- **Post-George Floyd Protests (2020):** Federal agencies used face recognition to identify individuals
- **January 6, 2021 Capitol Attack:** Three agencies admitted using the technology to identify individuals present

## Who Sells Face Recognition

Law enforcement agencies now commonly purchase access to commercial face recognition products rather than developing systems internally.

### Major Vendors

**Clearview AI:**
- Database of more than 30 million photos
- Images scraped from online and public locations
- One of the most extensive databases known to be used by law enforcement

**MorphoTrust (Idemia subsidiary):**
- Designs systems for state DMVs, federal and state law enforcement, border control, airports (including TSA PreCheck), and the State Department

**Other Common Vendors:**
- 3M
- Cognitec
- DataWorks Plus
- Dynamic Imaging Systems
- FaceFirst
- NEC Global

## Threats Posed By Face Recognition

### Privacy and Civil Liberties Concerns

**Unavoidable Collection:**
- Face recognition data is easy for law enforcement to collect
- Hard for members of the public to avoid
- Unlike passwords, people cannot easily change their faces

**Expanding Infrastructure:**
- Agencies increasingly share information across jurisdictions
- Cameras are becoming more powerful and ubiquitous
- More photographs and video are being stored for future analysis
- Images captured for one purpose are commonly used in face recognition systems

### Accuracy Problems

**FBI Admission:** The FBI acknowledged in its privacy impact assessment that its system "may not be sufficiently reliable to accurately locate other photos of the same identity, resulting in an increased percentage of misidentifications."

**Database Size Issues:**
- Face recognition accuracy decreases as database size increases
- More people in the database means higher likelihood of similar faces
- FBI system finds the true candidate in top 50 profiles only 85% of the time—and only when the candidate exists in the gallery

**Burden Shifting:** Inaccurate systems shift the traditional burden of proof away from the government, forcing people to prove their innocence.

### Demographic Bias

Face recognition systems perform worse at identifying:
- Black, Brown, and Asian individuals
- Non-gender conforming individuals
- Ethnic minorities
- Young people
- Women

**Compounding Factors:**
- Criminal databases include disproportionate numbers of African Americans, Latinos, and immigrants due to racially-biased police practices
- Even when algorithms are updated for accuracy, law enforcement may continue using original flawed systems

### Persistent Data

- Face recognition data often derived from publicly-available photos, social media, and mugshot images
- Mugshots taken upon arrest—before guilt or innocence is determined
- Mugshot photos often never removed from databases, even without charges

### Chilling Effect on Free Speech

Face recognition can target people engaging in protected speech:
- **Baltimore (Freddie Gray protests):** Police ran social media photos through face recognition to identify and arrest protesters
- Of 52 agencies analyzed by Georgetown Center on Privacy and Technology, only one (Ohio Bureau of Criminal Investigation) has a policy expressly prohibiting use to track individuals engaged in protected free speech

### Lack of Oversight

**Limited Safeguards:**
- Few systems are audited for misuse
- Less than 10% of agencies have publicly-available use policies
- Only two agencies (San Francisco PD and South Sound 911) restrict purchases to technology meeting accuracy thresholds
- Only Michigan State Police provides documentation of its audit process
- Agencies generally do not require warrants
- Many do not require suspicion of a crime before using face recognition

**Human Backup Limitations:**
Research shows that people without specialized training make wrong decisions about candidate photo matches about half the time. Few systems have specialized personnel review potential matches.

### Regulatory Landscape

**Bans and Rollbacks:**
- Some cities have implemented bans on face recognition use
- These restrictions are constantly being undermined at law enforcement's behest

**Examples:**
- **Virginia:** Enacted complete ban in 2021, rolled back restrictions in 2022
- **California:** Three-year moratorium passed in 2019, restrictions not reinstated after expiration in 2023
- **New Orleans:** Replaced 2020 ban with regulated access for local police

**Limited Private Sector Regulation:**
- Illinois Biometric Information Privacy Act requires notice and consent before private use of face recognition
- This only applies to companies, not law enforcement agencies

## EFF's Work on Face Recognition

EFF supports meaningful restrictions on face recognition use by both government and private companies, including total bans. EFF believes face recognition in all forms—including face scanning and real-time tracking—poses threats to civil liberties and individual privacy.

### Advocacy Efforts

**Federal Level:**
- Called on federal government to ban face recognition use by federal agencies
- Testified before Senate Subcommittee on Privacy, Technology, and the Law
- Testified before House Committee on Oversight and Government Reform
- Participated in NTIA face recognition multistakeholder process (walked out with other NGOs when companies wouldn't commit to meaningful restrictions)

**State and Local Level:**
- Supported local and state bans on facial recognition
- Opposes efforts to expand its use

### Legal Actions

**Court Cases:**
- Filed amicus brief in New Jersey (with EPIC and NACDL) supporting defendant's discovery rights to know face recognition algorithms used in their case—court agreed
- Sued FBI for access to face recognition records
- Filed amicus brief (with ACLU of Minnesota) demanding release of Hennepin County Sheriff Office face recognition program emails

**Public Records:**
- Filed public records requests for secret information on face recognition systems
- Pushed back when cities haven't properly complied with requests
- 2015: Launched crowdsourcing campaign with MuckRock to request information on mobile biometric technologies

### Public Education

- "Who Has Your Face" project helps individuals learn about databases containing their image
- Provides resources to activists fighting face surveillance

## EFF Legal Cases

- [State of New Jersey v. Arteaga](https://www.eff.org/document/state-new-jersey-v-francisco-arteaga)
- EFF v. U.S. Department of Justice
- [Tony Webster v. Hennepin County and Hennepin County Sheriff's Office](https://www.eff.org/deeplinks/2017/07/eff-minnesota-supreme-court-sheriff-must-release-emails-documenting-biometric)
- [Willie Allen Lynch v. State of Florida](https://www.eff.org/deeplinks/2019/03/when-facial-recognition-used-identify-defendants-they-have-right-obtain)

## Additional Reading

- [Garbage In, Garbage Out (Georgetown Law, Center on Privacy and Technology)](https://www.flawedfacedata.com/)
- [Face Off: Law Enforcement Use of Face Recognition Technology (EFF)](https://www.eff.org/wp/law-enforcement-use-face-recognition)
- [The Perpetual Line-Up (Georgetown Law Center on Privacy and Technology)](https://www.law.georgetown.edu/privacy-technology-center/publications/the-perpetual-line-up/)
- [Police Surveillance and Facial Recognition: Why Data Privacy Is Imperative for Communities of Color (Brookings Institute)](https://www.brookings.edu/articles/police-surveillance-and-facial-recognition-why-data-privacy-is-an-imperative-for-communities-of-color/)
- [Face Recognition Technology: FBI Should Better Ensure Privacy and Accuracy (Government Accountability Office)](https://www.gao.gov/products/gao-16-267)
- [Federal Agencies' Use and Related Privacy Protections (Government Accountability Office)](https://www.gao.gov/products/gao-22-106100)
- [California Cops Are Using These Biometric Gadgets in the Field (EFF)](https://www.eff.org/deeplinks/2015/11/how-california-cops-use-mobile-biometric-tech-field)
- [Face Recognition Performance Role of Demographic Information (IEEE)](https://ieeexplore.ieee.org/document/6327355)
- [Privacy Impact Assessment for the Facial Analysis, Comparison, and Evaluation (FACE) Services Unit (FBI)](https://www.fbi.gov/file-repository/pia-face-phase-2-system.pdf/view)

---

*Most recently updated September 5, 2023*