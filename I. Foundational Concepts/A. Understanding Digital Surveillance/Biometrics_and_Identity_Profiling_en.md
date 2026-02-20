---
title: "Biometrics and Identity Profiling"
tags:
  [
    biometrics,
    facial-recognition,
    identity-profiling,
    surveillance,
    iran-national-id,
    privacy,
    digital-security,
  ]
category: "Surveillance Technologies"
difficulty: "Intermediate"
audience: [General Public, Activists, Journalists, Privacy-Conscious Users]
topics: ["Biometric Surveillance", "Identity Management", "State Surveillance"]
summary: "Overview of biometric technologies (facial recognition, iris, DNA) and identity profiling methods used for surveillance, with a specific focus on the Iranian context including National ID cards and hijab enforcement."
source: "Raaznet Aggregated Data"
content_type: "Wiki Article"
security_level: "Informational"
language: "English"
prerequisites: ["Understanding Digital Surveillance", "Basic Privacy Concepts"]
estimated_read_time: "15 minutes"
---

# Biometrics and Identity Profiling

**Biometric surveillance** is the automated recognition of individuals based on their biological and behavioral characteristics. Unlike a password or a key, biometrics—such as your face, fingerprint, iris, or walking gait—are intrinsic to who you are. You cannot easily change them, making biometric tracking a persistent and invasive form of surveillance.

In the context of Iran, biometric data is not just used for authentication (like unlocking a phone) but is central to a state-level apparatus of control, linking physical identity with digital activity through centralized databases like the National Smart Card (_Kart-e Melli Hooshmand_) and SIM card registries.

## Key Biometric Technologies

### 1. Facial Recognition

Facial recognition technology uses algorithms to map facial features from a photograph or video frame and compare them against a database of known faces.

- **How it works:** The system analyzes the geometry of the face (distance between eyes, nose width, jawline) to create a unique "face template."
- **Iranian Context:**
  - **Hijab Enforcement:** The Iranian government utilizes facial recognition in public spaces, including the **Tehran Metro** and major intersections, to identify women violating mandatory hijab laws.
  - **Traffic Surveillance:** While initially for traffic control, cameras are now integrated with police databases to identify drivers and passengers.
  - **University Access:** Universities (e.g., Amirkabir University) have installed facial recognition systems at gates to control student access and enforce dress codes.
  - **The "Hybrid" Approach:** Often, the state combines facial recognition with other data points. For example, a traffic camera captures a license plate (ALPR), queries the vehicle owner's database, finds the registered mobile number, and sends a warning SMS—all without necessarily performing a real-time biometric face match of the driver, though capability for the latter is expanding.

### 2. Fingerprint and Iris Scanning

Fingerprint and iris patterns are highly unique and stable over time.

- **National Smart Card (_Kart-e Melli Hooshmand_):** This card contains a chip storing the holder's biometric data, including fingerprints and a high-resolution photograph. This creates a centralized national biometric database accessible by various state agencies (NAJA, FATA, Intelligence).
- **Border Control:** Iran has deployed biometric systems (fingerprint, face, and iris) at borders (e.g., Dogharoun) to catalog Afghan refugees and monitor cross-border movement.
- **Mobile Devices:** Many users voluntarily store fingerprints on their phones for convenience. If a device is seized, security forces often attempt to force the user to unlock the device using their fingerprint.

### 3. DNA and Genetic Profiling

DNA reveals not only individual identity but also familial relationships, ancestry, and medical propensity.

- **Forensic Use:** DNA is collected from arrestees and crime scenes.
- **Familial Searching:** Even if a target has not provided DNA, they can be identified if a relative has. In an authoritarian context, this allows for the tracking of political dissidents through their family members.

### 4. Behavioral Biometrics

This involves identifying individuals based on _how_ they act rather than _what_ they look like.

- **Gait Analysis:** Identifying a person by their walking style. This can be used to identify masked protesters.
- **Keystroke Dynamics:** Analyzing typing rhythm to identify a user behind a pseudonym.
- **Voice Recognition:** Used in telecommunications monitoring to identify speakers on phone calls, even if they switch SIM cards.

## Identity Profiling and Data Aggregation

Biometrics are most dangerous when combined with other data. **Identity Profiling** is the creation of a comprehensive dossier on an individual by aggregating data from multiple sources.

### The Iranian "Data Backbone"

The Islamic Republic relies on cross-referencing databases to maintain control. The lack of a single "super-AI" is compensated by bureaucratic integration:

1.  **Civil Registry (National ID):** The core identity (Name, Face, Fingerprint, Family links).
2.  **Shahkar System:** Links every SIM card to a National ID. This ensures that online activity (tied to a phone number) can be instantly traced to a physical person.
3.  **Hamta Registry:** Registers mobile device IMEIs to SIM cards. This links the _hardware_ to the _person_.
4.  **Banking & Services:** Access to banking, subsidies, and administrative services requires the National ID, creating a timestamped trail of an individual's physical locations and activities.

### The "Nazer" System and Crowdsourcing

The **Nazer** (Observer) app allows regime loyalists to report "violations" (such as removing hijab) by uploading photos, license plates, and locations. This crowdsourced surveillance feeds directly into the police profiling system, turning citizens into extensions of the surveillance state.

## Risks to Privacy and Safety

- **Loss of Anonymity:** In a biometrically surveyed society, "being a face in the crowd" is impossible. Attendance at a protest or a private gathering can be logged automatically.
- **False Positives:** Biometric algorithms often have higher error rates for women and ethnic minorities. In a legal system lacking due process, a machine error can lead to wrongful arrest or fines.
- **Chilling Effect:** The _knowledge_ of surveillance causes people to self-censor, avoiding public spaces or political expression.
- **Targeted Harassment:** Automated systems allow for the efficient harassment of thousands of people simultaneously (e.g., mass SMS warnings for hijab violations) without the need for equivalent human police manpower.

## Countermeasures and Protection

While bypassing state-level biometric surveillance is difficult, specific measures can reduce risk:

### 1. Digital Hygiene

- **Disable Biometric Unlock:** On your smartphone, **disable Face ID and Fingerprint unlock**. Use a strong, alphanumeric passphrase. In a seizure situation, you cannot be physically forced to "think" of your password, but your finger can be forced onto a sensor.
- **Metadata Scrubbing:** Before posting photos online, remove Exif metadata (location, device type) using tools like _ObscuraCam_ or _Scrambled Exif_.
- **Social Media Discipline:** Avoid posting high-resolution photos of your face or the faces of others at sensitive events.

### 2. Physical Obfuscation

- **Masking:** While cameras are improving, standard medical masks, sunglasses, and hats still disrupt facial recognition.
- **CV Dazzle:** Avant-garde makeup and hair styling designed to break facial recognition algorithms (though often conspicuous and impractical in daily Iranian life).
- **Gait Alteration:** Being aware of unique walking patterns or clothing (shoes/backpacks) that make you identifiable even when masked.

### 3. Identity Compartmentalization

- **Separate Identities:** Maintain a strict separation between your "Legal Identity" (SIM linked to ID, bank apps) and your "Activist Identity" (Foreign SIM, burner device, Tor-based communication).
- **Avoid "Nazer" Triggers:** Be aware of zones with high camera density or regime loyalist presence when engaging in civil disobedience.

## Conclusion

Biometric surveillance in Iran is rapidly evolving from a forensic tool into a mechanism of social control. The integration of the National Smart Card, Shahkar system, and street-level cameras creates a dragnet that requires users to be vigilant about both their physical presence and their digital footprint.

---

**Related Topics:**

- [[The_Mechanisms_of_Digital_Surveillance]]
- [[The_Surveillance_Economy_and_Data_Brokers]]
- [[Mobile_Device_Security]]
