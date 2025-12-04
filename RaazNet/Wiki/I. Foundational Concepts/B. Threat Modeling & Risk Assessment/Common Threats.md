---
title: "Common Threats to Digital Privacy and Security"
tags: [privacy, security, threat-modeling, surveillance, anonymity, encryption]
category: "Digital Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Journalists]
topics: ["Threat Modeling", "Privacy Protection", "Digital Security", "Surveillance"]
summary: "Comprehensive guide to understanding common digital threats including mass surveillance, targeted attacks, supply chain vulnerabilities, and strategies for protection."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Understanding of internet basics"]
estimated_read_time: "15 minutes"
---

# Common Threats to Digital Privacy and Security

We categorize privacy and security recommendations based on the threats or goals that apply to most people. You may be concerned with none, one, a few, or all of these possibilities. The tools and services you use depend on what your goals are. The important part is developing an understanding of the benefits and shortcomings of the tools you choose, because virtually none of them will protect you from every threat.

## Overview of Threat Categories

| Threat | Description |
|--------|-------------|
| **Anonymity** | Shielding your online activity from your real identity, protecting you from people trying to uncover *your* identity specifically |
| **Targeted Attacks** | Being protected from hackers or malicious actors trying to gain access to *your* data or devices specifically |
| **Supply Chain Attacks** | A form of targeted attack centering on vulnerabilities introduced into otherwise good software through a dependency or third party |
| **Passive Attacks** | Being protected from malware, data breaches, and other attacks made against many people at once |
| **Service Providers** | Protecting your data from service providers (e.g., with E2EE, which renders your data unreadable to the server) |
| **Mass Surveillance** | Protection from government agencies, organizations, websites, and services which work together to track your activities |
| **Surveillance Capitalism** | Protecting yourself from big advertising networks like Google and Facebook, as well as third-party data collectors |
| **Public Exposure** | Limiting the information about you that is accessible online—to search engines or the public |
| **Censorship** | Avoiding censored access to information or being censored yourself when speaking online |

Some threats may be more important to you than others depending on your specific concerns. For example, a software developer with access to valuable data may be primarily concerned with supply chain attacks and targeted attacks, while still wanting protection from mass surveillance programs.

---

## Anonymity vs. Privacy

Anonymity is often confused with privacy, but they're distinct concepts:

- **Privacy**: A set of choices you make about how your data is used and shared
- **Anonymity**: The complete disassociation of your online activities from your real identity

Whistleblowers and journalists, for example, may require total anonymity. That means not only hiding what they do and what data they have, but also hiding who they are entirely. They will often sacrifice convenience to protect their anonymity, privacy, or security, because their lives could depend on it. Most people don't need to go this far.

---

## Security and Privacy: Passive Attacks

When it comes to application security, we generally don't know if the software we use is malicious or might become malicious. Even with trustworthy developers, there's no guarantee their software doesn't have a serious vulnerability that could later be exploited.

### Mitigation Strategy: Security by Compartmentalization

To minimize damage from malicious software:

- Use different computers for different tasks
- Use virtual machines to separate groups of related applications
- Use a secure operating system with strong application sandboxing and mandatory access control

### Operating System Comparison

| OS | Sandboxing | Privacy Considerations |
|----|------------|----------------------|
| **ChromeOS** | Similar capabilities to Android | Transmits identifying information to Google |
| **macOS** | Full system permission control; developers can opt into sandboxing | Transmits identifying information to Apple |
| **Linux** | Poor protection against exploits and malicious apps by default | Does not submit information to system vendors |
| **Qubes OS** | Significant use of virtual machines/containers | Specialized distribution for security |

---

## Targeted Attacks Against Specific Individuals

Targeted attacks against a specific person are more problematic to deal with. Common attacks include:

- Sending malicious documents via email
- Exploiting vulnerabilities in browsers and operating systems
- Physical attacks

### Mitigation Strategies

**For digital attacks:**
Web browsers, email clients, and office applications typically run untrusted code from third parties. Running multiple virtual machines to separate these applications from your host system and each other can mitigate the chance of an exploit compromising your entire system. Technologies like Qubes OS or Microsoft Defender Application Guard provide convenient methods to do this.

**For physical attacks:**
- Use an operating system with secure verified boot implementation (Android, iOS, macOS, or Windows with TPM)
- Ensure your drive is encrypted
- Use a TPM, Secure Enclave, or Secure Element to rate-limit encryption passphrase attempts
- Avoid sharing your computer with untrusted individuals (most desktop operating systems don't encrypt data separately per-user)

---

## Supply Chain Attacks

Supply chain attacks frequently target businesses, governments, and activists, but can compromise the public at large.

### Notable Example: NotPetya (2017)

M.E.Doc, a popular accounting software in Ukraine, was infected with the NotPetya virus. This subsequently infected users who downloaded the software with ransomware, impacting 2,000+ companies across various countries. NotPetya was based on the EternalBlue exploit developed by the NSA.

### How Supply Chain Attacks Occur

1. A contributor or employee works their way into a position of power within a project, then abuses that position by adding malicious code
2. A developer is coerced by an outside party to add malicious code
3. An attacker infiltrates a third-party software dependency (library), knowing it will be used by downstream software developers

### Mitigation Strategies

1. **Adopt popular, established software** — More interest in a project means greater likelihood that external parties will notice malicious changes
2. **Use software with trusted build infrastructure** — Prefer releases built on platforms like GitHub Actions over developer workstations or self-hosted servers
3. **Check for meaningful commit messages** — Clear messages (such as [conventional commits](https://conventionalcommits.org/)) make it easier to verify, audit, and find bugs
4. **Note the number of contributors** — A lone developer may be more susceptible to coercion or negligence than software with multiple maintainers and scrutiny

---

## Privacy from Service Providers

Almost everything is connected to the internet. Our "private" messages, emails, and social interactions are typically stored on servers. When you send a message, it's stored on a server, and when your recipient wants to read it, the server shows it to them.

The problem: the service provider (or a hacker who has compromised the server) can access your conversations whenever they want, without you knowing. This applies to SMS messaging, Telegram, Discord, and many other services.

### Solution: End-to-End Encryption (E2EE)

E2EE encrypts communications between you and your recipients before they're sent to the server. The confidentiality of your messages is guaranteed, assuming the service provider doesn't have access to either party's private keys.

### Native Apps vs. Web-Based E2EE

| Implementation | Security Characteristics |
|----------------|-------------------------|
| **Native applications** (e.g., Signal) | Every copy is the same across installations; backdoors can be detected through reverse engineering |
| **Web-based E2EE** (e.g., Proton Mail web app, Bitwarden Web Vault) | Server dynamically serves JavaScript; a malicious server could send you malicious code to steal your encryption key; extremely hard to detect or prove |

**Recommendation:** Use native applications over web clients whenever possible.

### Metadata Concerns

Even with E2EE, service providers can still profile you based on **metadata**, which typically isn't protected:

- Whom you're talking to
- How often you message them
- When you're typically active

Protection of metadata is fairly uncommon. If it's within your threat model, pay close attention to the technical documentation of your software to see if there's any metadata minimization or protection.

---

## Mass Surveillance Programs

Mass surveillance is the effort to monitor the behavior, activities, or information of an entire (or substantial fraction of a) population. It often refers to government programs, such as those disclosed by Edward Snowden in 2013, but can also be carried out by corporations.

### Resources

- [Atlas of Surveillance](https://atlasofsurveillance.org/) by the Electronic Frontier Foundation
- [Technopolice](https://technopolice.fr/villes) (France) by La Quadrature du Net

### The Reality of Mass Surveillance

Governments often justify mass surveillance as necessary to combat terrorism and prevent crime. However, as breaches of human rights, they're most often used to disproportionately target minority groups and political dissidents.

The NSA had for years been secretly collecting records about virtually every American's phone calls—who's calling whom, when calls are made, and how long they last. This information can reveal incredibly sensitive details about people's lives: whether they've called a pastor, an abortion provider, an addiction counselor, or a suicide hotline.

Despite growing mass surveillance in the United States, the government has found that mass surveillance programs like Section 215 have had "little unique value" with respect to stopping actual crimes or terrorist plots.

### What Can Be Tracked

- Your IP address
- Browser cookies
- Data you submit to websites
- Your browser or device fingerprint
- Payment method correlation

### Mitigation Strategies

- Compartmentalize your online identities
- Blend in with other users
- Avoid giving out identifying information whenever possible

---

## Surveillance Capitalism

> Surveillance capitalism is an economic system centered around the capture and commodification of personal data for the core purpose of profit-making.

Tracking and surveillance by private corporations is a growing concern. Pervasive ad networks, such as those operated by Google and Facebook, span the internet far beyond the sites they control, tracking your actions along the way.

### Mitigation Strategies

- Use content blockers to limit network requests to tracking servers
- Read privacy policies of services you use
- Encrypt or obfuscate your data whenever possible to make it difficult for providers to correlate data and build a profile

### Beyond AdTech

Companies outside the AdTech or tracking industry can share your information with data brokers (Cambridge Analytica, Experian, Datalogix). Don't assume your data is safe just because a service doesn't fall within the typical tracking business model.

---

## Limiting Public Information (Public Exposure)

The best way to keep your data private is simply not making it public in the first place. Deleting unwanted information you find about yourself online is one of the best first steps to regain your privacy.

### Strategies

- Review and delete old accounts ([account deletion guide](https://www.privacyguides.org/en/basics/account-deletion/))
- If you've already submitted real information to sites that shouldn't have it, consider using disinformation tactics—submit fictitious information related to that online identity to make your real information indistinguishable from false information

---

## Avoiding Censorship

Censorship online can be carried out by totalitarian governments, network administrators, and service providers. These efforts to control communication and restrict access to information are incompatible with the human right to Freedom of Expression (United Nations Universal Declaration of Human Rights).

### Corporate Censorship

Censorship on corporate platforms is increasingly common as platforms like Twitter and Facebook respond to public demand, market pressures, and government pressures. Government pressures can be covert (requests to businesses) or overt (China requiring companies to adhere to strict censorship regimes).

### Circumvention Tools

- **Tor** for bypassing censorship
- **Matrix** for censorship-resistant communication (no centralized account authority)

### Important Considerations

While evading censorship itself can be easy, hiding the fact that you're doing it can be problematic.

| Method | What It Hides | What It Doesn't Hide |
|--------|---------------|---------------------|
| **Encrypted DNS** | DNS queries | What you're visiting from your ISP |
| **VPN or Tor** | What you're visiting from network administrators | That you're using those networks |
| **Pluggable transports** (Obfs4proxy, Meek, Shadowsocks) | Common VPN/Tor protocols from firewalls | Can still be detected by probing or deep packet inspection |

**Warning:** Always consider the risks of bypassing censorship, potential consequences, and how sophisticated your adversary may be. Be cautious with software selection and have a backup plan in case you are caught.

---

## References

1. Wikipedia: [Mass Surveillance](https://en.wikipedia.org/wiki/Mass_surveillance) and [Surveillance](https://en.wikipedia.org/wiki/Surveillance)
2. United States Privacy and Civil Liberties Oversight Board: [Report on the Telephone Records Program Conducted under Section 215](https://documents.pclob.gov/prod/Documents/OversightReport/ec542143-1079-424a-84b3-acc354698560/215-Report_on_the_Telephone_Records_Program.pdf)
3. "[Enumerating badness](https://ranum.com/security/computer_security/editorials/dumb)" — Content blockers and antivirus programs that list known bad things fail to adequately protect against new and unknown threats
4. United Nations: [Universal Declaration of Human Rights](https://un.org/en/about-us/universal-declaration-of-human-rights)
5. Wikipedia: [Surveillance capitalism](https://en.wikipedia.org/wiki/Surveillance_capitalism)