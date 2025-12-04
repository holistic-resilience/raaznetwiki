---
title: "Face Recognition Technology: A Comprehensive Guide to Street-Level Surveillance"
tags: [face-recognition, biometrics, surveillance, law-enforcement, privacy, civil-liberties]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Privacy Advocates, Activists, Legal Professionals, Journalists]
topics: ["Facial Recognition", "Biometric Surveillance", "Law Enforcement Technology", "Civil Liberties", "Privacy Rights"]
summary: "Comprehensive guide to face recognition technology, how law enforcement uses it, its accuracy problems, and the threats it poses to privacy and civil liberties."
source: "Electronic Frontier Foundation (EFF) - Street Level Surveillance"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of privacy concepts", "Familiarity with law enforcement practices"]
estimated_read_time: "20 minutes"
---

# Face Recognition Technology

Face recognition is a biometric technology that uses a face or the image of a face to identify or verify the identity of an individual in photos, video, or in real-time. It is commonly used by law enforcement and private businesses.

Face recognition systems depend on databases of individuals' images to train their underlying algorithms. The technology can be applied retroactively to video footage and photographs, used in coordination with other surveillance technologies and databases when creating profiles of individuals—including those who may never have been involved in a crime. It facilitates the tracking of individuals across video feeds and can be integrated into camera systems and other technologies, as seen at sporting events in the United States.

## Key Concerns

Face recognition poses significant risks:

- **Accuracy failures**: The technology can implicate people for crimes they haven't committed and make people into targets of unwarranted or dangerous retaliation
- **Demographic bias**: Facial recognition software is particularly bad at recognizing Black people and other ethnic minorities, women, young people, and transgender and nonbinary individuals
- **Disparate impact**: People in vulnerable demographic groups are especially at risk of being misidentified
- **Mass surveillance**: Contributes to surveillance of individuals, neighborhoods, and populations historically targeted by unfair policing practices
- **Targeting protected speech**: Has been used to target people engaging in protected speech and alienate perceived enemies

Hundreds of law enforcement agencies and a rapidly growing number of private entities use face recognition across the United States, with use in other countries also growing.

## How Face Recognition Works

Face recognition systems use computer algorithms to pick out specific, distinctive details about a person's face and make a judgment of its similarity to other faces.

### The Process

1. **Feature extraction**: Details such as distance between the eyes or shape of the chin are identified
2. **Mathematical representation**: Features are converted into a mathematical representation called a "face template"
3. **Comparison**: The template is compared to data on other faces in a face recognition database
4. **Matching**: The system attempts to find matches based on similarity scores

### Related Technologies

- **Face detection**: Identifying whether an image contains a face at all
- **Face analysis**: Assessment of certain traits like skin color and age based on the image of a face
- **Face verification**: Comparing an image of a known individual against another image to confirm both represent the same person
- **Face identification**: Comparing a sample image of an unknown individual against a collection of known faces to find a match

### Probability Matching

Some systems calculate a probability match score between an unknown person and specific face templates, offering several potential matches ranked by likelihood rather than returning a single result.

### Performance Variables

Face recognition systems vary in their ability to identify people under challenging conditions:
- Poor lighting
- Low quality image resolution
- Suboptimal angle of view (such as photographs taken from above)

### Error Types

| Error Type | Description | Example |
|------------|-------------|---------|
| **False Negative** | System fails to match a person's face to an image that is in the database | System returns zero results when the person is actually in the database |
| **False Positive** | System incorrectly matches a person's face to a different person in the database | Police submit image of "Joe" but system identifies them as "Jack" |

**Important trade-off**: There is almost always a trade-off between false positive and false negative rates:
- For phone unlocking, false negatives (failing to recognize you) are preferable to false positives (allowing others access)
- For criminal identification, false positives are particularly dangerous as they can lead to wrongful accusations

## How Law Enforcement Uses Face Recognition

Many local police agencies, state law enforcement, and federal agencies use face recognition in routine patrolling and policing.

### Database Access

- Scores of databases facilitate face recognition use at local, state, and federal levels
- Law enforcement may access systems through private platforms or government-designed systems
- Agencies can query databases to identify people in photos from:
  - Social media
  - Closed-circuit television (CCTV)
  - Traffic cameras
  - Photographs taken in the field

### Real-Time Monitoring

Faces may be compared in real-time against "hot lists" of people suspected of illegal activity.

### Federal Agency Use

According to a July 2021 Government Accountability Office (GAO) report:
- At least 20 of 42 federal agencies with policing powers use face recognition systems
- Agencies access one or more of 27 different federal face recognition databases
- Face recognition systems in 29 states are accessed by federal agencies
- At least 10 federal agencies don't track their use of non-federal face recognition technology

### Notable Uses

- **Post-George Floyd protests (2020)**: Federal agencies used face recognition to identify individuals during protests and civil unrest
- **January 6, 2021**: Three agencies admitted using the technology to identify individuals at the U.S. Capitol attack
- **Border and airport security**: TSA is integrating face recognition into airports; as of early 2023, TSA had introduced the technology to 16 major airports, and CBP had implemented it at 32 airports

### FBI Systems

**Next Generation Identification Database**:
- Contains more than 30 million face recognition records
- Provides "lights out" access to state and local agencies (no federal human oversight of individual searches)

**FACE Services** (Facial Analysis, Comparison and Evaluation):
- Dedicated FBI team for face recognition searches
- Access to more than 400 million non-criminal photos from state DMVs and the State Department
- At least 16 U.S. states allow FACE access to driver's license and ID photos
- As of 2019, nearly 400,000 searches had been conducted through FACE services

### State and Local Use

- Over a quarter of all state and local law enforcement agencies can run face recognition searches
- As of September 2023, EFF's Atlas of Surveillance cataloged nearly 900 municipal, county, and state agencies using face recognition
- The Pinellas County Sheriff's Office in Florida maintains one of the largest local databases with more than 38 million images accessible by 263 different agencies

### Mobile Face Recognition

Officers can use smartphones, tablets, or other portable devices to:
- Take photos of drivers or pedestrians in the field
- Immediately compare photos against face recognition databases
- Attempt real-time identification

### DMV Integration

- More than half of all adults in the United States have their likeness in at least one face recognition database
- At least 43 states have used face recognition with their DMV databases to detect fraud
- At least 26 states allow law enforcement to search driver license databases

## Who Sells Face Recognition

### Major Vendors

| Company | Notable Features |
|---------|------------------|
| **Clearview AI** | Database of 30+ million photos scraped from online sources; commonly used by law enforcement |
| **MorphoTrust/Idemia** | Designs systems for state DMVs, federal and state law enforcement, border control, airports, TSA PreCheck |
| **3M** | Face recognition and biometric solutions |
| **Cognitec** | Facial recognition algorithms and systems |
| **DataWorks Plus** | Law enforcement biometric solutions |
| **Dynamic Imaging Systems** | Facial recognition technology |
| **FaceFirst** | Commercial and law enforcement solutions |
| **NEC Global** | Biometric identification systems |

## Threats Posed By Face Recognition

### Privacy and Civil Liberties Concerns

**Data collection challenges**:
- Face recognition data is easy for law enforcement to collect
- Hard for members of the public to avoid
- Unlike passwords, people can't easily change their faces

**Expanding surveillance infrastructure**:
- Agencies increasingly share information across jurisdictions
- Cameras are becoming more powerful and ubiquitous
- More photographs and video are being stored for future analysis
- Images captured for one purpose are commonly used in face recognition systems

### Accuracy Problems

The FBI acknowledged in its privacy impact assessment that its system "may not be sufficiently reliable to accurately locate other photos of the same identity, resulting in an increased percentage of misidentifications."

**Key accuracy issues**:
- FBI system finds the true candidate in top 50 profiles only 85% of the time—and only when the candidate exists in the gallery
- If the candidate isn't in the gallery, the system may still produce false matches
- Accuracy decreases as database size increases due to similar-looking faces
- This shifts the burden of proof away from the government, forcing people to prove their innocence

### Demographic Bias

Face recognition systems are particularly bad at identifying:
- Black, Brown, and Asian individuals
- Women
- Young people
- Transgender and nonbinary individuals

**Compounding factors**:
- Criminal databases include disproportionate numbers of African Americans, Latinos, and immigrants due to racially-biased police practices
- Even when algorithms are updated for better accuracy, law enforcement may continue using flawed original systems

### Specific Threats

**Mugshot databases**:
- Photos taken upon arrest, before guilt or innocence is determined
- Often never removed from databases even if charges are never brought

**Targeting protected speech**:
- During protests after Freddie Gray's death, Baltimore Police used social media photos through face recognition to identify and arrest protesters
- Only one agency (Ohio Bureau of Criminal Investigation) has a policy expressly prohibiting use to track protected free speech

**Potential for abuse**:
- Few systems are audited for misuse
- Less than 10% of agencies have publicly-available use policies
- Only two agencies restrict purchases to systems meeting accuracy thresholds
- Only one agency (Michigan State Police) provides documentation of its audit process

### Human Review Limitations

Research shows that without specialized training, people make wrong decisions about whether a candidate photo is a match about half the time. Unfortunately, few systems have specialized personnel review matches.

### Legislative Landscape

Some cities have implemented bans, but these are frequently undermined:
- **Virginia**: Enacted complete ban in 2021, rolled back restrictions in 2022
- **California**: Three-year moratorium passed in 2019, restrictions not reinstated after expiration in 2023
- **New Orleans**: Replaced 2020 ban with regulated access for local police

## EFF's Position and Work

EFF supports meaningful restrictions on face recognition use by both government and private companies, including total bans. EFF believes that face recognition in all forms—including face scanning and real-time tracking—poses threats to civil liberties and individual privacy.

### Advocacy Efforts

- Called on federal government to ban face recognition by federal agencies
- Testified before Senate Subcommittee on Privacy, Technology, and the Law
- Testified before House Committee on Oversight and Government Reform
- Participated in NTIA face recognition multistakeholder process (walked out when companies wouldn't commit to meaningful restrictions)
- Supported local and state bans on facial recognition

### Legal Work

- Filed amicus brief in New Jersey supporting defendant's discovery rights to know face recognition algorithms used in their case (court agreed)
- Sued the FBI for access to face recognition records
- Filed public records requests to obtain secret information on face recognition systems
- Launched crowdsourcing campaign with MuckRock to request information on mobile biometric technologies
- Filed amicus brief with ACLU of Minnesota demanding release of emails regarding Hennepin County Sheriff Office's face recognition program

### Public Education

- Created "Who Has Your Face" project to help individuals learn about databases containing their images
- Provides resources to activists fighting face surveillance

## Legal Cases

- **State of New Jersey v. Arteaga**: Discovery rights for face recognition algorithms
- **EFF v. U.S. Department of Justice**: Access to face recognition records
- **Tony Webster v. Hennepin County and Hennepin County Sheriff's Office**: Release of biometric program documentation
- **Willie Allen Lynch v. State of Florida**: Rights when facial recognition is used for identification

## Additional Resources

- [Garbage In, Garbage Out](https://www.flawedfacedata.com/) - Georgetown Law, Center on Privacy and Technology
- [Face Off: Law Enforcement Use of Face Recognition Technology](https://www.eff.org/wp/law-enforcement-use-face-recognition) - EFF
- [The Perpetual Line-Up](https://www.law.georgetown.edu/privacy-technology-center/publications/the-perpetual-line-up/) - Georgetown Law Center on Privacy and Technology
- [Police Surveillance and Facial Recognition: Why Data Privacy Is Imperative for Communities of Color](https://www.brookings.edu/articles/police-surveillance-and-facial-recognition-why-data-privacy-is-an-imperative-for-communities-of-color/) - Brookings Institute
- [Face Recognition Technology: FBI Should Better Ensure Privacy and Accuracy](https://www.gao.gov/products/gao-16-267) - Government Accountability Office
- [Federal Agencies' Use and Related Privacy Protections](https://www.gao.gov/products/gao-22-106100) - Government Accountability Office
- [California Cops Are Using These Biometric Gadgets in the Field](https://www.eff.org/deeplinks/2015/11/how-california-cops-use-mobile-biometric-tech-field) - EFF
- [Face Recognition Performance Role of Demographic Information](https://ieeexplore.ieee.org/document/6327355) - IEEE
- [Privacy Impact Assessment for the Facial Analysis, Comparison, and Evaluation (FACE) Services Unit](https://www.fbi.gov/file-repository/pia-face-phase-2-system.pdf/view) - FBI

---

*Most recently updated September 5, 2023*