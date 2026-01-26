---
title: "SIM Swapping Attacks"
tags:
  [
    sim-swapping,
    mobile-security,
    two-factor-authentication,
    account-security,
    social-engineering,
  ]
category: "Mobile Security"
difficulty: "Intermediate"
audience:
  [General Public, Activists, Privacy-Conscious Users, Cryptocurrency Users]
topics: ["Mobile Security", "Account Protection", "Authentication Methods"]
summary: "راهنمای جامع درباره حملات تعویض سیم‌کارت، نحوه عملکرد آن‌ها و روش‌های مقابله برای محافظت از حساب‌های آنلاین"
source: "Certfa (سرتفا)"
content_type: "Educational Guide"
security_level: "Advanced"
language: "Persian"
prerequisites:
  ["آشنایی با مفاهیم پایه امنیت دیجیتال", "آشنایی با احراز هویت دو مرحله‌ای"]
estimated_read_time: "8 minutes"
---

# SIM Swapping Attacks (SIM Swapping)

## Introduction

The SIM swapping attack is one of the old and well-known problems in the mobile network infrastructure. These attacks allow hackers to steal ownership of your SIM card using fake methods and gain access to your online accounts.

## How the Attack Works

### Step One: Information Gathering

Hackers gather your identity information from websites and various sources.

### Step Two: Deceiving the Operator

Using this information, they convince the mobile operator to transfer your SIM card number to a new SIM card.

### Step Three: Accessing Accounts

After the number transfer:

- All calls and SMS messages are sent to the new SIM card
- Two-factor authentication codes reach the hackers
- Hackers can gain access to social networks, emails, and bank accounts

## Why is this attack dangerous?

SIM swapping attacks are one of the most effective hybrid hacking methods for stealing user accounts. Known victims include:

- Jack Dorsey (Twitter CEO)
- Singers and actors
- Cryptocurrency investors
- Executives of large companies

> **Real example:** In one case, hackers stole $23.8 million from the accounts of Michael Terpin, a famous cryptocurrency investor.

## Countermeasures

### 1. Activating SIM PIN

PIN and PUK codes are 4 or 8 digit passwords for physical and identity protection of the SIM card.

**Why is it important?**
Without knowing the PIN code, attackers cannot transfer your phone number to another operator.

**Recommendation:** Make sure to keep your SIM PIN activated.

### 2. Choosing a Reliable Mobile Operator

- Contact your operator
- Ask about security layers for SIM swapping
- If not supported, change the operator

### 3. Using Secure Authentication Methods

**Insecure methods (avoid):**

- SMS codes (SMS)

**Secure methods (recommended):**

- **Time-based One-Time Passwords (TOTP):** Using apps such as:
  - Google Authenticator
  - Authy
- **Hardware security keys:** Such as YubiKey

### 4. Account Recovery Settings

In many services, a phone number is requested for account recovery.

**Recommendation for Google:**

- Use the "Recovery email" option
- Avoid the "Recovery phone" option

## Further Resources

- [Hackers Hit Twitter C.E.O. Jack Dorsey in a 'SIM Swap.' You're at Risk, Too](https://www.nytimes.com/2019/09/05/technology/sim-swap-jack-dorsey-hack.html)
- [How to Protect Yourself Against a SIM Swap Attack](https://www.wired.com/story/sim-swap-attack-defend-phone/)

---

**Related Topics:** Multi-factor Authentication | Mobile Security | Social Networks
