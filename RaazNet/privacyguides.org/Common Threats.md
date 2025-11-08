---
title: "Common Threats"
tags: [privacy, security, threat-modeling, surveillance, attacks]
category: "Privacy Basics"
difficulty: "Beginner"
audience: [General Public, Privacy-Conscious Users, Journalists]
topics:
  [
    "Threat Modeling",
    "Mass Surveillance",
    "Service Providers",
    "Supply Chain Attacks",
  ]
summary: "Overview of common digital privacy and security threats, including anonymity, targeted attacks, mass surveillance, and censorship."
source: "Privacy Guides"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic understanding of online activity"]
estimated_read_time: "12 minutes"
---

[Skip to content](https://www.privacyguides.org/en/basics/common-threats/#anonymity-vs-privacy)

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/basics/common-threats.md?plain=1 "Edit this page")

# Common Threats

Broadly speaking, we categorize our recommendations into the [threats](https://www.privacyguides.org/en/basics/threat-modeling/) or goals that apply to most people. You may be concerned with none, one, a few, or all of these possibilities, and the tools and services you use depend on what your goals are. You may have specific threats outside these categories as well, which is perfectly fine! The important part is developing an understanding of the benefits and shortcomings of the tools you choose to use, because virtually none of them will protect you from every threat.

**Anonymity**

Shielding your online activity from your real identity, protecting you from people who are trying to uncover _your_ identity specifically.

**Targeted Attacks**

Being protected from hackers or other malicious actors who are trying to gain access to _your_ data or devices specifically.

**Supply Chain Attacks**

Typically, a form of Targeted Attack that centers around a vulnerability or exploit introduced into otherwise good software either directly or through a dependency from a third party.

**Passive Attacks**

Being protected from things like malware, data breaches, and other attacks that are made against many people at once.

**Service Providers**

Protecting your data from service providers (e.g. with E2EE, which renders your data unreadable to the server).

**Mass Surveillance**

Protection from government agencies, organizations, websites, and services which work together to track your activities.

**Surveillance Capitalism**

Protecting yourself from big advertising networks, like Google and Facebook, as well as a myriad of other third-party data collectors.

**Public Exposure**

Limiting the information about you that is accessible online—to search engines or the public.

**Censorship**

Avoiding censored access to information or being censored yourself when speaking online.

Some of these threats may be more important to you than others, depending on your specific concerns. For example, a software developer with access to valuable or critical data may be primarily concerned with Supply Chain Attacks and Targeted Attacks. They will likely still want to protect their personal data from being swept up in Mass Surveillance programs. Similarly, many people may be primarily concerned with Public Exposure of their personal data, but they should still be wary of security-focused issues, such as Passive Attacks—like malware affecting their devices.

## Anonymity vs. Privacy

Anonymity

Anonymity is often confused with privacy, but they're distinct concepts. While privacy is a set of choices you make about how your data is used and shared, anonymity is the complete disassociation of your online activities from your real identity.

Whistleblowers and journalists, for example, can have a much more extreme threat model which requires total anonymity. That's not only hiding what they do, what data they have, and not getting hacked by malicious actors or governments, but also hiding who they are entirely. They will often sacrifice any kind of convenience if it means protecting their anonymity, privacy, or security, because their lives could depend on it. Most people don't need to go so far.

## Security and Privacy

Passive Attacks

Security and privacy are also often confused, because you need security to obtain any semblance of privacy: Using tools—even if they're private by design—is futile if they could be easily exploited by attackers who later release your data. However, the inverse isn't necessarily true: The most secure service in the world _isn't necessarily_ private. The best example of this is trusting data to Google who, given their scale, have had few security incidents by employing industry-leading security experts to secure their infrastructure. Even though Google provides very secure services, very few people would consider their data private in Google's free consumer products (Gmail, YouTube, etc.)

When it comes to application security, we generally don't (and sometimes can't) know if the software we use is malicious, or might one day become malicious. Even with the most trustworthy developers, there's generally no guarantee that their software doesn't have a serious vulnerability that could later be exploited.

To minimize the damage that a malicious piece of software _could_ do, you should employ security by compartmentalization. For example, this could come in the form of using different computers for different jobs, using virtual machines to separate different groups of related applications, or using a secure operating system with a strong focus on application sandboxing and mandatory access control.

Tip

Mobile operating systems generally have better application sandboxing than desktop operating systems: Apps can't obtain root access, and require permission for access to system resources.

Desktop operating systems generally lag behind on proper sandboxing. ChromeOS has similar sandboxing capabilities to Android, and macOS has full system permission control (and developers can opt in to sandboxing for applications). However, these operating systems do transmit identifying information to their respective OEMs. Linux tends to not submit information to system vendors, but it has poor protection against exploits and malicious apps. This can be mitigated somewhat with specialized distributions which make significant use of virtual machines or containers, such as [Qubes OS](https://www.privacyguides.org/en/desktop/#qubes-os).

## Attacks against Specific Individuals

Targeted Attacks

Targeted attacks against a specific person are more problematic to deal with. Common attacks include sending malicious documents via email, exploiting vulnerabilities (e.g. in browsers and operating systems), and physical attacks. If this is a concern for you, you should employ more advanced threat mitigation strategies.

Tip

By design, **web browsers**, **email clients**, and **office applications** typically run untrusted code, sent to you from third parties. Running multiple virtual machines—to separate applications like these from your host system, as well as each other—is one technique you can use to mitigate the chance of an exploit in these applications compromising the rest of your system. For example, technologies like Qubes OS or Microsoft Defender Application Guard on Windows provide convenient methods to do this.

If you are concerned about **physical attacks** you should use an operating system with a secure verified boot implementation, such as Android, iOS, macOS, or [Windows (with TPM)](https://learn.microsoft.com/windows/security/information-protection/secure-the-windows-10-boot-process). You should also make sure that your drive is encrypted, and that the operating system uses a TPM or Secure [Enclave](https://support.apple.com/guide/security/secure-enclave-sec59b0b31ff/1/web/1) or [Element](https://developers.google.com/android/security/android-ready-se) to rate limit attempts to enter the encryption passphrase. You should avoid sharing your computer with people you don't trust, because most desktop operating systems don't encrypt data separately per-user.

## Attacks against Certain Organizations

Supply Chain Attacks

Supply chain attacks are frequently a form of Targeted Attack towards businesses, governments, and activists, although they can end up compromising the public at large as well.

Example

A notable example of this occurred in 2017 when M.E.Doc, a popular accounting software in Ukraine, was infected with the _NotPetya_ virus, subsequently infecting people who downloaded that software with ransomware. NotPetya itself was a ransomware attack which impacted 2000+ companies in various countries, and was based on the _EternalBlue_ exploit developed by the NSA to attack Windows computers over the network.

There are few ways in which this type of attack might be carried out:

1. A contributor or employee might first work their way into a position of power within a project or organization, and then abuse that position by adding malicious code.
2. A developer may be coerced by an outside party to add malicious code.
3. An individual or group might identify a third party software dependency (also known as a library) and work to infiltrate it with the above two methods, knowing that it will be used by "downstream" software developers.

These sorts of attacks can require a lot of time and preparation to perform and are risky because they can be detected, particularly in open source projects if they are popular and have outside interest. Unfortunately they're also one of the most dangerous as they are very hard to mitigate entirely. We would encourage readers to only use software which has a good reputation and makes an effort to reduce risk by:

1. Only adopting popular software that has been around for a while. The more interest in a project, the greater likelihood that external parties will notice malicious changes. A malicious actor will also need to spend more time gaining community trust with meaningful contributions.
2. Finding software which releases binaries with widely-used, trusted build infrastructure platforms, as opposed to developer workstations or self-hosted servers. Some systems like GitHub Actions let you inspect the build script that runs publicly for extra confidence. This lessens the likelihood that malware on a developer's machine could infect their packages, and gives confidence that the balaunched binaries produced are in fact produced correctly.
3. Looking for code signing on individual source code commits and releases, which creates an auditable trail of who did what.
4. Checking whether the source code has meaningful commit messages (such as [conventional commits](https://conventionalcommits.org/)) which explain what each change is supposed to accomplish.
5. Noting the number of contributors or maintainers a program has.

## Privacy from Service Providers

Service Providers

We live in a world where almost everything is connected to the internet. Our "private" messages, emails, and social interactions are typically stored on a server, somewhere. Generally, when you send someone a message it's stored on a server, and when your friend wants to read the message the server will show it to them.

The obvious problem with this is that the service provider (or a hacker who has compromised the server) can access your conversations whenever and however they want, without you ever knowing. This applies to many common services, like SMS messaging, Telegram, and Discord.

Thankfully, E2EE can alleviate this issue by encrypting communications between you and your desired recipients before they are even sent to the server. The confidentiality of your messages is guaranteed, assuming the service provider doesn't have access to the private keys of either party.

Note on Web-based Encryption

In practice, the effectiveness of different E2EE implementations varies. Applications, such as [Signal](https://www.privacyguides.org/en/real-time-communication/#signal), run natively on your device, and every copy of the application is the same across different installations. If the service provider were to introduce a [backdoor](<https://en.wikipedia.org/wiki/Backdoor_(computing)>) in their application—in an attempt to steal your private keys—it could later be detected with [reverse engineering](https://en.wikipedia.org/wiki/Reverse_engineering).

On the other hand, web-based E2EE implementations, such as Proton Mail's web app or Bitwarden's _Web Vault_, rely on the server dynamically serving JavaScript code to the browser to handle cryptography. A malicious server can target you and send you malicious JavaScript code to steal your encryption key (and it would be extremely hard to notice). Because the server can choose to serve different web clients to different people—even if you noticed the attack—it would be incredibly hard to prove the provider's guilt.

Therefore, you should use native applications over web clients whenever possible.

Even with E2EE, service providers can still profile you based on **metadata**, which typically isn't protected. While the service provider can't read your messages, they can still observe important things, such as whom you're talking to, how often you message them, and when you're typically active. Protection of metadata is fairly uncommon, and—if it's within your [threat model](https://www.privacyguides.org/en/basics/threat-modeling/)—you should pay close attention to the technical documentation of the software you're using to see if there's any metadata minimization or protection at all.

## Mass Surveillance Programs

Mass Surveillance

Mass surveillance is the intricate effort to monitor the "behavior, many activities, or information" of an entire (or substantial fraction of a) population.[1](https://www.privacyguides.org/en/basics/common-threats/#fn:1) It often refers to government programs, such as the ones [disclosed by Edward Snowden in 2013](<https://en.wikipedia.org/wiki/Global_surveillance_disclosures_(2013%E2%80%93present)>). However, it can also be carried out by corporations, either on behalf of government agencies or by their own initiative.

Atlas of Surveillance

If you want to learn more about surveillance methods and how they're implemented in your city you can also take a look at the [Atlas of Surveillance](https://atlasofsurveillance.org/) by the [Electronic Frontier Foundation](https://eff.org/).

In France, you can take a look at the [Technopolice website](https://technopolice.fr/villes) maintained by the non-profit association La Quadrature du Net.

Governments often justify mass surveillance programs as necessary means to combat terrorism and prevent crime. However, as breaches of human rights, they're most often used to disproportionately target minority groups and political dissidents, among others.

ACLU: _[The Privacy Lesson of 9/11: Mass Surveillance is Not the Way Forward](https://aclu.org/news/national-security/the-privacy-lesson-of-9-11-mass-surveillance-is-not-the-way-forward)_

In the face of Edward Snowden's disclosures of government programs such as [PRISM](https://en.wikipedia.org/wiki/PRISM) and [Upstream](https://en.wikipedia.org/wiki/Upstream_collection), intelligence officials also admitted that the NSA had for years been secretly collecting records about virtually every American’s phone calls — who’s calling whom, when those calls are made, and how long they last.

## Surveillance as a Business Model

Surveillance Capitalism

> Surveillance capitalism is an economic system centered around the capture and commodification of personal data for the core purpose of profit-making.[5](https://www.privacyguides.org/en/basics/common-threats/#fn:3)

For many people, tracking and surveillance by private corporations is a growing concern.

## Limiting Public Information

Public Exposure

The best way to keep your data private is simply not making it public in the first place. Deleting unwanted information you find about yourself online is one of the best first steps you can take to regain your privacy.

## Avoiding Censorship

Censorship

Censorship online can be carried out (to varying degrees) by actors including totalitarian governments, network administrators, and service providers. These efforts to control communication and restrict access to information will always be incompatible with the human right to Freedom of Expression.

You must always consider the risks of trying to bypass censorship, the potential consequences, and how sophisticated your adversary may be.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
