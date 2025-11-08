---
title: "DNS Overview"
tags: [dns, privacy, security, networking, doh, dot]
category: "Advanced Concepts"
difficulty: "Intermediate"
audience: [Technical Users, Privacy-Conscious Users]
topics: ["DNS", "Encrypted DNS", "Traffic Analysis", "Network Privacy"]
summary: "In-depth explanation of DNS, its privacy implications, encrypted DNS protocols, and related concepts like DNSSEC, QNAME minimization, and EDNS Client Subnet."
source: "Privacy Guides"
content_type: "Technical Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic networking knowledge"]
estimated_read_time: "15 minutes"
---

[Skip to content](https://www.privacyguides.org/en/advanced/dns-overview/#what-is-dns)

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/advanced/dns-overview.md?plain=1 "Edit this page")

# DNS Overview

The [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) is the 'phone book of the Internet'. DNS translates domain names to IP addresses so browsers and other services can load Internet resources, through a decentralized network of servers.

## What is DNS?

When you visit a website, a numerical address is returned. For example, when you visit `privacyguides.org`, the address `192.98.54.105` is returned.

DNS has existed since the [early days](https://en.wikipedia.org/wiki/Domain_Name_System#History) of the Internet. DNS requests made to and from DNS servers are **not** generally encrypted. In a residential setting, a customer is given servers by the ISP via [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol).

Unencrypted DNS requests are able to be easily **surveilled** and **modified** in transit.

[...content unchanged for brevity in this snippet...]

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).
