---
title: "Dangerzone: Document Sanitization Tool"
tags: [document-security, malware-protection, pdf-sanitization, open-source, privacy-tools]
category: "Privacy Tools"
difficulty: "Beginner"
audience: [Journalists, Activists, Security Professionals, General Users]
topics: ["Document Security", "Malware Protection", "Privacy Tools"]
summary: "A free open-source tool that converts potentially dangerous documents into safe PDFs by removing malware and metadata in a secure sandbox."
source: "Freedom of the Press Foundation"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer skills", "Understanding of document security risks"]
estimated_read_time: "5 minutes"
---

![](https://dangerzone.rocks/assets/img/logo.png)

# Dangerzone

Take potentially dangerous PDFs, office documents, or images and convert them
to safe PDFs.

[Download](https://dangerzone.rocks/#downloads) [Learn More](https://dangerzone.rocks/about/)

🦠 Removes malware

Dangerzone destroys malware by rendering your document into pixels in a secure sandbox and reconstructing it locally as a PDF.

🗋 Supports many file types

Dangerzone supports more than 20 file types, including PDFs, all major office-suite formats, and the most common image types.

🔌 Avoids network access

Documents are sanitized in a sandbox with no network access, so if a malicious document can compromise one, it can't let anyone know.

🫴 Provides a public good

Dangerzone is a free and open source project, maintained by [Freedom of the Press Foundation](https://freedom.press/) (FPF), a nonprofit organization that protects and defends press freedom.

## Download Dangerzone 0.9.1

🔍 [How to verify](https://github.com/freedomofpress/dangerzone/blob/v0.9.1/INSTALL.md#verifying-pgp-signatures)

![Apple Logo](https://dangerzone.rocks/assets/img/apple-logo.png)

MacOS

[Intel chip](https://github.com/freedomofpress/dangerzone/releases/download/v0.9.1/Dangerzone-0.9.1-i686.dmg) [Apple Silicon chip](https://github.com/freedomofpress/dangerzone/releases/download/v0.9.1/Dangerzone-0.9.1-arm64.dmg)

ℹ️
[Which one do I have?](https://support.apple.com/en-us/HT211814)

![Windows Logo](https://dangerzone.rocks/assets/img/windows-logo.png)

Windows

[Download for\\
Windows](https://github.com/freedomofpress/dangerzone/releases/download/v0.9.1/Dangerzone-0.9.1.msi)

️

![Ubuntu Logo](https://dangerzone.rocks/assets/img/ubuntu-logo.png)

Ubuntu / Debian

[Install](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md#ubuntu-debian)

![Fedora Logo](https://dangerzone.rocks/assets/img/fedora-logo.png)

Fedora

[Install](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md#fedora)

![Tails Logo](https://dangerzone.rocks/assets/img/tails-logo.svg)

Tails

[Install](https://tails.net/doc/persistent_storage/additional_software/dangerzone/index.en.html)

![Linux Logo](https://dangerzone.rocks/assets/img/linux-logo.png)

Other Linux

[Build from Source](https://github.com/freedomofpress/dangerzone/blob/main/BUILD.md)

![Qubes OS Logo](https://dangerzone.rocks/assets/img/qubes-os-logo.png)

Qubes OS (Beta)

[Install](https://github.com/freedomofpress/dangerzone/blob/main/INSTALL.md#qubes-os)

## How It Works

Dangerzone works like this: You give it a document that you don't know
if you can trust (for example, an email attachment). Inside of a sandbox,
Dangerzone converts the document to a PDF (if it isn't already one), and
then converts the PDF into raw pixel data: a huge list of of RGB color
values for each page. Then, Dangerzone takes this pixel data and converts
it back into a PDF.

[Learn more](https://dangerzone.rocks/about/)