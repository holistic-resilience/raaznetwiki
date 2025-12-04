---
title: "Why We Still Recommend Signal Over WhatsApp"
tags: [secure-messaging, encryption, privacy, signal, whatsapp, metadata]
category: "Secure Communications"
difficulty: "Beginner"
audience: [General Public, Activists, Privacy-Conscious Users]
topics: ["End-to-End Encryption", "Messaging Security", "Privacy Protection", "Metadata"]
summary: "Explains why Signal is recommended over WhatsApp despite both using the same encryption protocol, covering open source code, data storage, and business model differences."
source: "Security in a Box (Tactical Tech)"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of messaging apps"]
estimated_read_time: "6 minutes"
authors: ["Maria Xynou", "Chris Walker"]
date_published: "2016-05-23"
---

# Why We Still Recommend Signal Over WhatsApp

*Even though they both use end-to-end encryption*

WhatsApp's collaboration with Open Whisper Systems brought *end-to-end encryption* to a billion people around the world. When WhatsApp integrated the encryption protocol developed for Signal, many users began using end-to-end encryption without even realizing it.

This is an important development that helps protect user privacy globally. However, there are several reasons why we recommend Signal over WhatsApp, even though they both use the *same protocol* for end-to-end encryption.

## Source Code

WhatsApp deserves credit for adopting an open encryption protocol vetted by security experts rather than creating a proprietary encryption scheme with little external review.

However, cryptography is not the only aspect of security. The security of an app also depends on how an encryption protocol is integrated.

**Open source vs. closed source:**
- **Open source software** allows us to review the code, verify implementation, and confirm it contains no malicious code
- **Closed source software** requires trusting the developer's claims without verification

While WhatsApp relies on the Signal protocol (an open standard), the WhatsApp app itself is closed source. We trust Open Whisper Systems to have properly integrated the Signal protocol, but the closed source nature prevents us from identifying other aspects that could impact security.

**Signal is fully open source**, allowing verification that communications are properly encrypted and enabling review of the app's overall security.

## Secure Data Storage

The Signal protocol encrypts data *in transit*—it is a communications protocol. It does *not* automatically encrypt data stored on devices, such as messaging history.

| Feature | Signal | WhatsApp |
|---------|--------|----------|
| Data in transit | Encrypted | Encrypted |
| Local storage encryption | Optional passphrase protection | Not available |
| Protection from physical access | Yes (with passphrase) | No |

Signal allows users to encrypt messages stored on their phones with a passphrase, protecting those messages from anyone who gains physical access to the device.

## Verification Against Man-in-the-Middle Attacks

An essential component of digital security is verifying that we are communicating with the intended person. Without this verification, someone could intercept our communications through a *man-in-the-middle attack*—decrypting messages, recording them, re-encrypting them, and relaying them without detection.

Recognizing a correspondent's voice is not sufficient to guarantee proper encryption. Both apps provide cryptographic identity verification mechanisms, but Signal's implementation is more transparent due to its open source nature.

## Business Model

The organizations behind these apps have fundamentally different business models:

### WhatsApp (Facebook/Meta)
- Owned by Facebook
- Advertising-driven business model
- Fueled by user data collection across services

### Signal (Open Whisper Systems)
- Non-profit organization
- Grant-funded
- Mission: *"Advance the state of the art for secure communication, while simultaneously making it easy for everyone to use"*

## The Metadata Question

While the Signal protocol encrypts the *content* of communications, it does not encrypt *metadata*—information about who you contact, when, and from where.

**Why metadata matters:**
- Easier and cheaper to process than content
- Can be stored in large quantities
- Reveals information that is difficult to deny
- Enables mapping of political affiliation, interests, location, and habits
- Can be used for profiling and targeted advertising
- Research shows profiling can lead to discrimination

Given Facebook's willingness to implement end-to-end encryption (which prevents access to content), the value may have been in the metadata all along.

As Open Whisper Systems is not in the data business, Signal is more likely to protect metadata.

### A Note on Signal's Infrastructure

Signal's reliance on Google Cloud Messaging means Google has access to some metadata (such as IP addresses of devices receiving Signal messages). However, Signal's architecture minimizes this exposure. For those seeking to avoid Google entirely, alternatives like LibreSignal (available through F-Droid) allow using the Signal protocol independently from Google Play Services.

## Summary

| Consideration | Signal | WhatsApp |
|---------------|--------|----------|
| Encryption protocol | Signal Protocol | Signal Protocol |
| Source code | Open source | Closed source |
| Local storage encryption | Available | Not available |
| Business model | Non-profit | Advertising-driven |
| Metadata protection | Better | Uncertain |
| Independent verification | Possible | Not possible |

## Getting Started with Signal

For step-by-step instructions on installing and using Signal, see the [Security in a Box Signal guide](https://securityinabox.org/en/guide/signal/android).

---

*Original article published by Security in a Box (Tactical Tech)*