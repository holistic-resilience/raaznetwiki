---
title: "Contextual Analysis and Actor Mapping"
tags:
  [
    context-analysis,
    actor-mapping,
    situational-awareness,
    pestle,
    risk-assessment,
    iran-security,
    operational-security,
  ]
category: "Foundational Concepts"
difficulty: "Intermediate"
audience: [Activists, Journalists, NGO Workers, General Public]
topics:
  [
    "Security Strategy",
    "Threat Assessment",
    "Stakeholder Analysis",
    "Iranian Digital Landscape",
  ]
summary: "A comprehensive guide to analyzing the operational environment and mapping actors (allies, adversaries, and neutrals) within the Iranian context to build effective security strategies."
source: "Raaznet Wiki Aggregation"
content_type: "Guide & Framework"
security_level: "Essential"
language: "English"
prerequisites: ["Basic understanding of digital surveillance"]
estimated_read_time: "10 minutes"
---

# Contextual Analysis and Actor Mapping

Security does not exist in a vacuum. A tool or tactic that is safe in one country may be dangerous in another. For Iranian users, understanding the specific **context**—the political, technological, and social environment—is the first line of defense.

This guide provides a framework for analyzing your environment and mapping the people and institutions (actors) that impact your security. By understanding _where_ you are and _who_ surrounds you, you can move from generic paranoia to calculated risk management.

---

## I. The Importance of Context Analysis

Context analysis is the systematic study of the environment in which you operate. For activists and citizens in Iran, relying on general security advice without considering the local context can lead to "unrecognized threats" (dangers you don't see) or "unfounded fears" (wasting energy on things that aren't threats).

### The PESTLE Framework (Iranian Context)

To analyze your security context, we use the **PESTLE** framework. Below is an adaptation of this framework specifically for the Iranian landscape.

#### 1. Political

- **Factional Dynamics:** Understand which security agency typically targets your line of work (e.g., is it the Ministry of Intelligence (VAJA) or the IRGC Intelligence Organization (SAS)?).
- **Cycles of Unrest:** Security posture must tighten during anniversaries of protests (e.g., Aban 98, Woman Life Freedom) or election periods when state sensitivity is heightened.
- **State Narrative:** How does the state currently frame your activity? (e.g., "acting against national security," "cooperating with hostile states").

#### 2. Economic

- **Hardware Cost:** Inflation and sanctions make replacing seized devices difficult. Data backup strategies must account for the inability to easily buy new hardware.
- **Payment Trails:** Use of domestic banking apps or payment gateways creates a permanent, traceable financial record linked to your national ID.

#### 3. Social

- **Trust Deficit:** The extensive use of informants (local Basij bases, workplace monitoring) creates an environment of paranoia.
- **Cultural Pressure:** Social engineering attacks often exploit cultural norms, such as respect for authority or family emergencies.
- **Gender Dynamics:** Female activists face distinct threats, including gender-based harassment online and specific leverage used by interrogators regarding "honor" or family reputation.

#### 4. Technological

- **National Information Network (SHOMA):** Iran operates a dual-layer internet. Domestic traffic is cheaper, faster, and heavily monitored. International traffic is throttled and filtered.
- **Infrastructure Ownership:** ISPs in Iran are not neutral; they are legally required to log data and often owned by state-affiliated entities.
- **Platform Dominance:** The push to move users to domestic platforms (e.g., Eitaa, Rubika, Soroush) serves to centralize surveillance.

#### 5. Legal

- **Criminalization:** Laws such as the "User Protection Bill" (Tarh-e Sianat) or computerized crimes laws function to criminalize encryption and VPN use.
- **Lack of Due Process:** In the context of the Islamic Republic, legal frameworks are often weaponized. "Evidence" is frequently digital data extracted from seized devices.

#### 6. Environmental

- **Physical Infrastructure:** Internet shutdowns often correlate with specific geographic locations of unrest. Understanding the physical layout of your city’s connectivity (cellular towers, ISP hubs) is part of situational awareness.

---

## II. Actor Mapping

Actor mapping is the process of visualizing relationships. It helps you identify who can help you, who might hurt you, and who might unintentionally compromise you.

### 1. Categorizing Actors

In the Iranian security landscape, actors generally fall into four categories:

| Category               | Definition                                                                          | Iranian Context Examples                                                                                                                 |
| :--------------------- | :---------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Adversaries**        | Entities actively trying to stop, surveil, or harm you.                             | **FATA** (Cyber Police), **IRGC** (Sepah) Cyber Army, **Basij** cyber battalions, state-sponsored hacker groups (e.g., Charming Kitten). |
| **Allies**             | People or groups who share your goals and support you.                              | Trusted colleagues, secure technology providers (e.g., Tor Project), international human rights orgs, legal aid networks.                |
| **Neutral Parties**    | Entities with no specific agenda regarding your work, but who hold power or data.   | Landlords, neighbors, hardware repair shops, non-political family members.                                                               |
| **Incidental Threats** | Entities that pose a risk not through malice, but through compliance or negligence. | **ISPs** (Irancell, Hamrah Aval), domestic cloud providers (Arvan Cloud), domestic app developers.                                       |

### 2. Mapping Relationships & Intensity

Visualizing these connections helps identify weak points.

- **Direct Connections:** Who do you talk to daily? (e.g., Your team). If one is compromised, you are at immediate risk.
- **Indirect Connections:** Who talks to your team? (e.g., The family member of a colleague). If a colleague's family is pressured by security forces, that pressure transmits to your colleague, and then to you.
- **Data Connections:** Who holds your data? In Iran, if you use a domestic messenger, the server host is an actor with direct access to your metadata and potentially your content.

> **Critical Warning:** In Iran, the line between a "Neutral Party" (like an ISP) and an "Adversary" is non-existent. Legally, all ISPs must cooperate with security forces. Treat all infrastructure providers as potential adversaries.

---

## III. The Information Ecosystem

Beyond people, you must map your **Information Ecosystem**. This involves cataloging what data you have, where it lives, and who controls the container.

### 1. Information at Rest (Storage)

- **Physical:** Paper notes, hard drives, USB sticks.
  - _Risk:_ Physical raids (home/office).
- **Digital (Local):** Files on laptops/phones.
  - _Risk:_ Seizure at checkpoints; theft; coercion to unlock devices.
- **Digital (Cloud):**
  - _Domestic Cloud:_ Files stored on Iranian services (PersianGig, CafeBazaar, Aparat) are vulnerable to immediate state access without a warrant.
  - _International Cloud:_ Files on Google Drive/Dropbox. Secure from direct seizure, but vulnerable if account credentials are phished or 2FA is intercepted via SMS.

### 2. Information in Motion (Transfer)

- **Domestic Traffic:** Traffic routing through SHOMA (internal network) allows for Deep Packet Inspection (DPI).
- **International Traffic:** Traffic leaving Iran through the telecommunications gateway (TIC) is heavily filtered.

### 3. Actor-Information Overlap

When mapping, ask: _Which actor controls the infrastructure where my information lives?_

- If you send an SMS, the **Mobile Network Operator (MNO)** is the actor holding that data.
- If you use a VPN, the **VPN Provider** is the actor holding your traffic data.

---

## IV. The "Do No Harm" Approach

Security measures aimed at protection can sometimes cause backlash if they ignore the social context. This is the "Do No Harm" framework.

### 1. Avoid Creating Suspicion

In a neighborhood where "everyone knows everyone," sudden extreme secrecy can attract attention.

- **Example:** If you suddenly install CCTV cameras and reinforced locks on your home door in a quiet residential building, neighbors (or the local mosque/Basij) may become suspicious.
- **Strategy:** Blend in. Your physical security should match the baseline of your environment.

### 2. Managing Family and Peers

Implementing strict security protocols (e.g., "everyone must use Signal," "no phones in meetings") can create tension or fear within a group or family.

- **Risk:** If family members feel excluded or scared, they may inadvertently talk to others about your "strange behavior."
- **Strategy:** Explain security measures as "good digital hygiene" rather than "anti-regime secrecy." Frame it as protecting privacy from hackers and criminals, which is a universally understood concern.

### 3. Resource Allocation

Allocating security resources (e.g., buying VPN licenses or iPhones for some staff but not others) can create internal resentment.

- **Strategy:** Ensure security is collective. The security of the group is only as strong as the least secure member.

---

## V. Practical Exercises

To apply this knowledge, conduct the following exercises with your team or for yourself.

### Exercise 1: Visual Actor Map

1.  **Center:** Place yourself/organization in the center of a paper.
2.  **Layer 1 (Direct):** Plot people/groups you contact daily.
3.  **Layer 2 (Indirect):** Plot people who influence Layer 1.
4.  **Layer 3 (Infrastructure):** Plot the ISPs, apps, and platforms holding your data.
5.  **Color Code:** Red for Adversaries, Green for Allies, Yellow for Neutrals.
6.  **Analyze:** Look for Red actors that have direct lines to your Green actors (e.g., An ISP connecting to your team member).

### Exercise 2: The Stress Test (Scenario Planning)

Select a realistic scenario based on your PESTLE analysis (e.g., "Internet Shutdown" or "Arrest of a Colleague").

1.  How does the map change?
2.  Which "Neutrals" might become "Adversaries" under pressure?
3.  Which communication channels (Information Ecosystem) will fail?

## Summary

Contextual analysis is not a one-time task; it is a mindset. In Iran, where the digital and physical security landscape shifts rapidly, you must regularly update your map. Know your environment, know your actors, and know where your data lives.
