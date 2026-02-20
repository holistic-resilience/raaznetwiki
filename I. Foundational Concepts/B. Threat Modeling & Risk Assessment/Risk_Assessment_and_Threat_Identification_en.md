---
title: "Risk Assessment and Threat Identification"
tags:
  [
    risk-assessment,
    threat-modeling,
    digital-security,
    iran-context,
    surveillance,
    actor-mapping,
    operational-security,
  ]
category: "Foundational Concepts"
difficulty: "Intermediate"
audience: [Activists, Journalists, NGO Workers, General Iranian Public]
topics:
  [
    "Threat Modeling Fundamentals",
    "Context Analysis",
    "Asset Inventory",
    "Adversary Capabilities",
    "Risk Matrix",
  ]
summary: "A comprehensive guide to identifying digital and physical threats in the Iranian context. This document outlines how to create a personal or organizational threat model, map adversaries (such as state actors), and assess risks based on assets and vulnerabilities."
source: "Raaznet Aggregated Wiki"
content_type: "Core Guide"
security_level: "Essential"
language: "English"
prerequisites:
  [
    "Basic understanding of digital privacy",
    "Awareness of the Iranian socio-political context",
  ]
estimated_read_time: "12 minutes"
last_updated: "2026-02-19"
---

# Risk Assessment and Threat Identification

Security is not a product you buy; it is a process. For Iranian users—whether activists, journalists, or ordinary citizens avoiding censorship—understanding the specific landscape of threats is the first step toward safety. This guide consolidates frameworks for **Threat Modeling** and **Risk Assessment**, tailored to the realities of the Iranian internet landscape (Halal Net/National Information Network).

## 1. What is Threat Modeling?

Threat modeling is a structured approach to identifying what you have, who wants it, and how they might get it. It moves you away from "paranoid" general fear toward specific, actionable security plans.

To build a threat model, you must answer five fundamental questions:

1.  **What do I want to protect?** (Assets)
2.  **Who do I want to protect it from?** (Adversaries/Actors)
3.  **How likely is it that I will need to protect it?** (Likelihood)
4.  **How bad are the consequences if I fail?** (Impact)
5.  **How much trouble am I willing to go through to prevent potential consequences?** (Capacity/Effort)

---

## 2. Context Analysis: The Iranian Landscape

Before assessing personal risks, you must understand the environment. In Iran, the primary threat model differs from Western contexts; the adversary is often the state infrastructure itself, not just criminal hackers.

### The PESTLE Framework (Iranian Context)

Use this framework to analyze the current situation:

- **Political:** Changes in internet legislation (e.g., "Protection Bill"), upcoming elections, or periods of civil unrest (protests) which usually correlate with internet shutdowns or throttling.
- **Economic:** Forced migration to domestic apps due to the high cost of international bandwidth; reliance on precarious digital payments.
- **Social:** The use of social engineering (e.g., fake morality police warnings) to trick users; infiltration in activist groups.
- **Technological:** Deep Packet Inspection (DPI) by ISPs; blocks on encryption protocols (TLS/SSL); state-sponsored malware.
- **Legal:** Criminalization of VPN use; forced confessions; lack of data privacy laws protecting citizens from the state.
- **Environmental:** Physical internet infrastructure vulnerability; electricity blackouts affecting security systems.

---

## 3. Actor Mapping: Who is the Adversary?

In security planning, an **Adversary** (or Actor) is any entity that poses a threat to your assets. In Iran, actors generally fall into three categories:

### A. State-Sponsored Actors (High Capability / High Resource)

- **FATA (Cyber Police):** Monitors social media, phishing campaigns, and public internet usage.
- **IRGC Intelligence Organization:** Conducts targeted espionage, advanced malware deployment, and physical detention of high-value targets.
- **Ministry of Intelligence:** Focuses on surveillance of dissidents and infiltration of networks.
- **The Judiciary:** Issues summons often delivered via SMS (a major vector for phishing).

### B. Infrastructure Actors (Privileged Access)

- **ISPs (MCI, Irancell, TCI):** These entities are legally required to log traffic, facilitate Deep Packet Inspection, and assist in SMS interception or 2FA hijacking.
- **Domestic Platforms:** Local messaging apps (e.g., Eitaa, Soroush) and hosting providers that store data within Iran's borders, making it accessible to security agencies without a warrant.

### C. Opportunistic & Social Actors

- **Cybercriminals:** Seeking financial gain (banking trojans, phishing).
- **Infiltrators/Informants:** Individuals entering trusted circles to gather intelligence.
- **Social Circle:** Family members or colleagues who may inadvertently leak information due to poor security hygiene (e.g., clicking links).

---

## 4. Asset Inventory: What Are You Protecting?

You cannot protect everything equally. List your assets and classify them.

### Information Assets

- **Communications:** Signal/WhatsApp chats, emails, contact lists.
- **Identity:** Anonymity of your admin status on Telegram channels or Instagram pages.
- **Documentation:** Photos/Videos of protests, human rights violations, or sensitive documents.
- **Credentials:** Passwords, 2FA backup codes, recovery keys.

### Physical Assets

- **Devices:** Smartphones (primary target for location/contacts), laptops, hard drives.
- **Hardware Tokens:** YubiKeys or 2FA dongles.

### Intangible Assets

- **Reputation:** Protection against defamation or "cyber-bullying" campaigns.
- **Network Trust:** The safety of your colleagues or followers.

---

## 5. Threat Identification

Based on the actors and assets, specific threats in Iran include:

### Digital Threats

- **Phishing & Social Engineering:**
  - _The "Samaneh Sana" Tactic:_ Fake judicial SMS messages containing malware links.
  - _Fake VPNs:_ Malicious apps distributed on Telegram that function as spyware.
- **Network Surveillance:**
  - _DPI:_ Identification and blocking of VPN traffic.
  - _DNS Hijacking:_ Redirecting traffic to fake servers.
- **Account Takeover:**
  - _SIM Swapping/Interception:_ Intercepting SMS 2FA codes to hijack Telegram or Instagram accounts.
- **Malware:**
  - _Spyware:_ Tools like Pegasus (used rarely against high-profile targets) or generic commodity spyware used to track location and keylogs.

### Physical & Legal Threats

- **Device Seizure:** Confiscation of phones at checkpoints or during raids.
- **Coerced Access:** Being forced to unlock devices via biometrics (face/fingerprint) or under duress during interrogation.
- **Doxxing:** State media or "cyber armies" releasing private information to intimidate activists.

---

## 6. Risk Assessment Matrix

Once threats are identified, categorize them to prioritize your response.

- **Risk = Likelihood × Impact**

| Impact / Likelihood                             | **High Likelihood** (e.g., Phishing, VPN Blocking)                                    | **Low Likelihood** (e.g., Pegasus Infection, Targeted Raid)           |
| :---------------------------------------------- | :------------------------------------------------------------------------------------ | :-------------------------------------------------------------------- |
| **High Impact** (Arrest, Compromise of Network) | **CRITICAL:** Immediate mitigation required (e.g., Panic Button, Data Deletion Plan). | **HIGH:** Plan contingencies (e.g., Duress codes, Encrypted backups). |
| **Low Impact** (Spam, Temporary Internet Loss)  | **MEDIUM:** Implement standard hygiene (e.g., Spam filters, Offline maps).            | **LOW:** Monitor occasionally.                                        |

### Practical Example: Iranian Activist

1.  **Threat:** Device seizure at a protest.
2.  **Likelihood:** High.
3.  **Impact:** High (Arrest, exposure of contacts).
4.  **Risk Level:** **Critical.**
5.  **Mitigation:** Do not bring primary phone; use a "burner" phone; enable full disk encryption; disable biometrics (FaceID/TouchID) before leaving home.

---

## 7. Vulnerability Assessment (The "Gap" Analysis)

Analyze where your current defenses are weak.

- **Behavioral:** Do you click links in SMS? Do you reuse passwords?
- **Technical:** Is your phone OS outdated? Is your hard drive unencrypted? Do you use SMS for 2FA instead of an Authenticator App?
- **Organizational:** Does your team use insecure channels (SMS/calls) for sensitive discussions? Is there a lack of trust or clear protocols during an emergency?

### Common Vulnerabilities in Iran

- **Reliance on SMS 2FA:** Highly vulnerable to state interception.
- **Using Domestic Apps:** Vulnerable to direct monitoring.
- **VPN Leaks:** Using "Free VPNs" that log data or contain malware.
- **Lack of "Clean" Devices:** Crossing borders or attending protests with devices containing sensitive archives.

---

## 8. Strategy and Response Planning

Based on the assessment, you will develop strategies (covered in detail in the _Security Strategy_ section).

- **Protection:** Implementing encryption, using Tor/Orbot, switching to Signal, disabling link previews.
- **Deterrence:** Making it too costly or difficult for the adversary to access data (e.g., strong encryption that FATA cannot easily brute-force).
- **Acceptance:** Acknowledging certain risks (e.g., internet shutdown) and preparing offline communication methods (Mesh networks, Sneakernet).

### Emergency Response Indicators

Establish an **Early Alert System**. Monitor for:

- Sudden drop in internet speed or specific protocol blocking (indicates tightening censorship).
- Strange noises or battery drain on devices (potential malware).
- Unexpected login attempts on your accounts.
- Arrests of peers in your network (indicates potential compromise of shared groups).

## 9. Conclusion

Risk assessment is continuous. In the context of Iran, where the digital landscape shifts rapidly due to government intervention, you must revisit your threat model regularly—especially before attending public events, crossing borders, or engaging in sensitive online campaigns.

**Next Steps:**

- Proceed to **[Security Strategy and Response Planning]** to build defenses against these risks.
- Review **[Organizational Security and Group Dynamics]** if working in a team.
