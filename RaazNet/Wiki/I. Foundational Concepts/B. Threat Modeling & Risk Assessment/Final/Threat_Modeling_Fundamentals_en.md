---
title: "Threat Modeling Fundamentals"
tags:
  [
    threat-modeling,
    risk-assessment,
    digital-security,
    holistic-security,
    privacy,
    iran-context,
    security-strategy,
  ]
category: "Foundational Concepts"
difficulty: "Beginner"
audience: [Activists, Journalists, Human Rights Defenders, General Public]
topics:
  [
    "Security Planning",
    "Risk Management",
    "Context Analysis",
    "Adversary Mapping",
  ]
summary: "A comprehensive guide to understanding and applying threat modeling in the Iranian context. This document consolidates frameworks for identifying assets, mapping adversaries, assessing risks, and developing holistic security strategies."
source: "Raaznet Wiki (Consolidated from Tactical Tech, EFF, Privacy Guides, and Certfa)"
content_type: "Core Guide"
security_level: "Essential"
language: "English"
prerequisites: ["None"]
estimated_read_time: "15 minutes"
last_updated: "2026-02-19"
---

# Threat Modeling Fundamentals

## Introduction

Security is not a product you buy; it is a process you practice. For Iranian users facing a complex landscape of state surveillance, censorship, and cybercrime, relying on generic advice can be dangerous. **Threat Modeling** is the systematic process of identifying what you have of value, who wants it, and how to protect it.

At **Raaznet**, we advocate for a **Holistic Security** approach. This means we do not view digital security in a vacuum. We recognize that your physical safety, your psychosocial well-being (stress levels), and your digital footprint are deeply interconnected. A breach in one area often leads to vulnerabilities in the others.

---

## 1. The Core Framework: Five Questions

To build an effective security plan, you must answer five fundamental questions. This framework prevents "security fatigue"—the exhaustion that comes from trying to protect everything against everyone all the time.

### Question 1: What do I want to protect? (Assets)

An **asset** is anything you value. In the context of Iran, assets often include:

- **Information:** Contact lists (activist networks), chat logs (Telegram/Signal), photos/videos of protests, location history.
- **Physical Devices:** Mobile phones, laptops, hard drives, cameras.
- **Intangibles:** Your reputation, your physical freedom, the safety of your family, your mental health.
- **Access:** Admin access to channels or websites.

### Question 2: Who do I want to protect it from? (Adversaries)

An **adversary** is any person or entity that poses a threat to your assets. You must be specific.

- **State Actors:** Ministry of Intelligence, IRGC Intelligence Organization, FATA (Cyber Police).
- **Telecommunications:** ISPs (Irancell, MCI, TCI) that log metadata and enforce censorship.
- **Local Threats:** Workplace informants, abusive family members, politically motivated neighbors (Basij).
- **Cybercriminals:** Phishing gangs, ransomware operators.

### Question 3: How likely is it that I will need to protect it? (Risk)

Risk is the intersection of **Likelihood** and **Impact**.

- _Is the threat mass surveillance?_ (High likelihood, variable impact).
- _Is the threat a targeted arrest?_ (Lower likelihood for the general public, Very High for high-profile activists).

### Question 4: How bad are the consequences if I fail? (Impact)

- **Low Impact:** Spam emails, temporary loss of internet access.
- **Medium Impact:** Doxxing, loss of social media accounts, financial theft.
- **High Impact:** Arrest, interrogation, torture, long-term imprisonment, physical harm to self or family.

### Question 5: How much trouble am I willing to go through? (Capacity)

Security measures usually reduce convenience.

- Are you willing to leave your phone at home during a gathering?
- Can you memorize a 20-character password?
- Are you willing to switch from WhatsApp to Signal despite your family not using it?

---

## 2. Contextual Analysis and Actor Mapping

Before choosing tools (like VPNs or encryption), you must understand the environment you operate in.

### PESTLE Analysis (Iranian Context)

Systematically scan the environment using these factors:

- **Political:** New legislation regarding internet criminalization (e.g., "Protection Bill" variants).
- **Technological:** New capabilities of the National Information Network (SHOMA), domestic root certificates, new filtering techniques.
- **Social:** Public sentiment, levels of trust within your network.
- **Legal:** Current enforcement trends regarding satellite internet or VPN usage.

### Visual Actor Mapping

Create a map of the entities around you to visualize relationships.

1.  **Center:** Place yourself/your organization.
2.  **Allies:** People/groups who actively support you (trusted colleagues, secure tech support).
3.  **Neutral Parties:** ISPs, hardware vendors, neighbors. _Note: In Iran, neutral parties (ISPs) are often compelled by law to act as adversaries._
4.  **Adversaries:** Entities actively trying to harm you.

> **Critical Note:** Do not assume "neutral" actors are safe. In Iran, platform providers (like domestic messaging apps) are legally required to store data and share it with security services upon request.

---

## 3. Risk Assessment Matrix

Once you have identified threats, prioritize them. You cannot defend against everything equally. Use a **Likelihood vs. Impact** matrix.

| Risk Level          | Low Impact                                                                                | High Impact                                                                                                    |
| :------------------ | :---------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **High Likelihood** | **Manage/Mitigate**<br>_(e.g., Internet throttling. Solution: Have backup VPNs/bridges)._ | **CRITICAL PRIORITY**<br>_(e.g., Device seizure upon arrest. Solution: Full Disk Encryption, Hidden Volumes)._ |
| **Low Likelihood**  | **Accept**<br>_(e.g., Someone reading your public blog)._                                 | **Plan Contingencies**<br>_(e.g., Office raid. Solution: Remote wipe capabilities, legal support plan)._       |

- **Green (Low/Low):** Ignore or accept.
- **Yellow (High Likelihood/Low Impact):** Automate defenses (e.g., ad blockers).
- **Red (High Impact):** Requires immediate behavioral changes and strict protocols.

---

## 4. Holistic Security: The Human Element

Digital security fails when the human operator is compromised. Stress, trauma, and exhaustion degrade your ability to make safe decisions.

### The Stress Table

Security incidents often happen when we are tired or panicked. Monitor your stress levels:

- **Green (Manageable):** You are creative and engaged.
- **Yellow (Unpleasant):** You feel "wired," hyper-alert, or physically tense. _Action:_ Take a break, step back from sensitive tasks.
- **Red (Critical):** You are overwhelmed, anxious, or engaging in unhealthy coping mechanisms. _Action:_ Stop all high-risk activity immediately. You are a security liability to yourself and your network.

### Security Indicators

Establish a "baseline" of normality so you can detect anomalies.

- **Digital:** Is your battery draining unusually fast? Are you receiving unexpected 2FA codes (sign of account hijacking attempts)?
- **Physical:** Are there unfamiliar cars parked on your street? Are you seeing repeated "coincidental" meetings with strangers?
- **Psychosocial:** Is the team arguing more than usual? (This can be a sign of infiltration or extreme burnout).

---

## 5. Building a Security Strategy

Based on your assessment, adopt specific strategies.

### Capacity vs. Vulnerability

- **Vulnerability:** A weakness that increases risk (e.g., using SMS for 2FA in Iran, where operators allow interception).
- **Capacity:** A strength that reduces risk (e.g., using hardware security keys or knowledge of Tor bridges).
- **Goal:** Reduce vulnerabilities and build capacities.

### Strategic Approaches

1.  **Protection:** Hardening defenses.
    - _Example:_ Enabling Lockdown Mode on iPhone, using Signal with disappearing messages, using distinct identities for online activities.
2.  **Deterrence:** Raising the cost of the attack.
    - _Example:_ Making data harder to decrypt (strong passwords) so that lower-level investigators might give up.
3.  **Acceptance:** Building allies to reduce threat.
    - _Example:_ Publicizing your work internationally so that an arrest draws diplomatic condemnation (use with caution; can sometimes escalate risk).

---

## 6. Practical Application: The "Do No Harm" Principle

When implementing security in a group or organization:

- **Inclusivity:** Security measures should not exclude less tech-savvy members. If a tool is too hard to use, people will bypass it.
- **Resource Allocation:** Do not hoard security resources (e.g., paid VPNs) for leadership only. This creates resentment and weak links.
- **Do No Harm:** Ensure your security measures do not endanger others. For example, leaving a shared Signal group without warning might panic other members.

## Summary Checklist for Iranian Users

1.  [ ] **Define your assets:** What data on your phone would put you in Evin prison?
2.  [ ] **Map your actors:** Who has the technical capability to access that data (FATA, ISPs)?
3.  [ ] **Check your stress:** Are you calm enough to make security decisions?
4.  [ ] **Prioritize:** Focus on High Impact/High Likelihood threats first.
5.  [ ] **Monitor:** Watch for changes in your environment (internet blocks, physical surveillance) and adapt.

---

### Related Resources

- **Tactical Tech:** _Holistic Security Guide_
- **EFF:** _Surveillance Self-Defense_
- **Raaznet Wiki:** _[Contextual Analysis and Actor Mapping]_ (Coming Soon)
- **Raaznet Wiki:** _[Risk Assessment and Threat Identification]_ (Coming Soon)
