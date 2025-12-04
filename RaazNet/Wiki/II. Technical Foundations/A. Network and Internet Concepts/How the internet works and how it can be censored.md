\_\_('Table of Contents')

Internet Connection › How the internet works and how it can be censored

# [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#how-the-internet-works-and-how-it-can-be-censored) How the internet works and how it can be censored

Updated 20 August 2024

## [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#table-of-contents) Table of Contents

- [How the internet works, and how some countries and other entities block or censor websites and online services](https://securityinabox.org/en/internet-connection/how-the-internet-works/#how-the-internet-works-and-how-some-countries-and-other-entities-block-or-censor-websites-and-online-services)
- [Understanding how websites and online services can be blocked](https://securityinabox.org/en/internet-connection/how-the-internet-works/#understanding-how-websites-and-online-services-can-be-blocked)
- [Your internet connection](https://securityinabox.org/en/internet-connection/how-the-internet-works/#your-internet-connection)
- [How websites are blocked](https://securityinabox.org/en/internet-connection/how-the-internet-works/#how-websites-are-blocked)
- [How tools get around blocks](https://securityinabox.org/en/internet-connection/how-the-internet-works/#how-tools-get-around-blocks)
- [Further Reading](https://securityinabox.org/en/internet-connection/how-the-internet-works/#further-reading)

## [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#how-the-internet-works-and-how-some-countries-and-other-entities-block-or-censor-websites-and-online-services) How the internet works, and how some countries and other entities block or censor websites and online services

The internet is an international public resource, made up of computers, phones, servers, routers and other devices connected to each other. It was designed to continue providing service even if part of the network was destroyed.

> No one person, company, organization or government runs the internet.
>
> [_Wikipedia page on internet governance_](https://en.wikipedia.org/wiki/Internet_governance)

However, national and international bodies have some control over the infrastructure of the internet in their jurisdiction. Many countries prevent internet users within their borders from accessing certain websites or online services. Businesses, schools, libraries and other institutions may rely on similar filters to "protect" their employees, students and customers from material they consider harmful or distracting.

Internet filtering can be based on different technologies. Some filters block sites based on their IP addresses (identifying numbers that may be shaped like `172.105.249.143` or `2a01:7e01::f03c:92ff:fecd:7e45` and are assigned to every phone, computer, router and website to deliver internet content to those who have requested it). Others block particular domain names (the web addresses you may be more familiar with, like `google.com` or this website, `securityinabox.org`). Some filters block all addresses except an official list of allowed sites defined by the authority that have devised those filters. Other filters search through unencrypted internet traffic and cause the internet infrastructure to ignore requests that include specific keywords (for example, searches that include "human rights violations" or names of opposition leaders).

You can often bypass these filters by installing software that uses intermediary servers, located in other countries, to pass content between the blocked content or service you are trying to reach and your device. Learn more about these tools in [the guide on how to circumvent internet blockages and monitoring](https://securityinabox.org/en/internet-connection/circumvention).

## [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#understanding-how-websites-and-online-services-can-be-blocked) Understanding how websites and online services can be blocked

Research carried out by organisations like the [Open Observatory of Network Interference (OONI)](https://ooni.org/) and [Reporters Without Borders (RSF)](https://rsf.org/en/recherche?text=censorship) indicates that many countries filter a wide variety of social, political and "national security" content, but rarely publish lists of what they block. Governments that wish to control their citizens' access to the internet also block VPNs and proxies they are aware of, as well as websites that offer tools and instructions to help people get around filters.

Article 19 of the Universal Declaration of Human Rights guarantees free access to information. Despite this, the number of countries censoring the internet continues to increase. As this practice spreads throughout the world, however, so does access to anti-blocking tools that have been created, deployed and publicised by activists, programmers and volunteers, with funding from the United States, Canada, the European Union, NGOs and other bodies concerned with free speech.

## [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#your-internet-connection) Your internet connection

![](https://securityinabox.org/media/en/anonymity-and-circumvention/internet_connection.png)

When you ask your computer to access a website, or your phone to use an app, your request and the content you see in response both go through a number of network devices. Your phone or computer first uses its wired, wireless or mobile data connection to reach your internet service provider (ISP). If you are home and using your own wifi, this ISP may be the company you pay for internet service. If you are using mobile data, the ISP you are connecting to is probably your mobile service provider. If you are working from an office, school, internet cafe or some other public space, it may be difficult to determine what ISP you are connecting to.

Your ISP relies on the network infrastructure in your country to connect its users with the rest of the world. The ISP assigns an IP address to the local network or device you are using to connect, whether it is your home wifi, your mobile phone or the network of the internet cafe, school or hotspot you are using. Your ISP will use this address to send content to your device. On the other end of your connection, the website or internet service you are accessing will have received its own IP address from an ISP in its own country.

Online services can use this address to send you the web pages you are trying to view and other data you request. (Your device has its own IP address, which is how your router sends everybody on your network their own traffic. It is only used on your local network.)

Anyone who knows your IP address can figure out what city or region you are in. Certain entities can determine your precise location even more precisely:

- **Your mobile provider** knows the precise physical location of your phone while your device is on, by triangulating your location among its cell towers.
- **Your ISP** will likely know what building you are in.
- **An internet cafe, library or business** where you are accessing the internet will know which of their computers you were using at any given time. And if you are using your own device, they will know which local IP address was assigned to your device on their local network, thus associating all your activities to your device.
- **Government agencies** may know all of the above. And even if they do not, they can often use their influence to find out.

Internet communication is somewhat more complex than the description above, but even this simplified model can help you figure out what risks you face when connecting to the internet and what institution or entity could be blocking a website you're trying to connect to.

## [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#how-websites-are-blocked) How websites are blocked

When you view a web page, your device connects to a domain name service (DNS) to look up the IP address associated with the website's domain name — for example, it could ask what's the IP address of `securityinabox.org` and receive the answer `172.105.249.143`. It then asks your ISP to send a request to the ISP in charge of `172.105.249.143` to ask the web server at `172.105.249.143` for the contents of securityinabox.org.

If you are in a country that censors securityinabox.org, your request will not succeed at some point of this process: when your device tries to look up the IP address, when it requests the content, or as the content is being sent to your device. In some countries, ISPs are required to consult a national blacklist of sites they must not show you. These blocklists can contain domain names, IP addresses, keywords or a mix of all of these. Keyword filters scan both unencrypted requests and the results a website or service returns to you.

You might not always know when you have requested a blocked webpage, content or service. Sometimes you may receive a response that explains why a particular content or service has been censored. But most of the times you will see a misleading error message, saying for example that the page or service could not be found or the address may be misspelled.

Each blocking technique has strengths and weaknesses. When attempting to get around internet blocks, it is easier to assume the worst than to figure out what techniques are being used in your country. You might as well assume:

- that blocking is implemented nationally, at the ISP level _and_ on your local network,
- that DNS lookups _and_ content requests are blocked,
- that blocklists are maintained for both domain names and IP addresses,
- that your unencrypted internet traffic is monitored for keywords, and
- that no indication or reason will be given for the blocking.

The safest and most effective anti-blocking tools should work regardless of the type of block you are facing.

## [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#how-tools-get-around-blocks) How tools get around blocks

![](https://securityinabox.org/media/en/anonymity-and-circumvention/proxies.png)

Circumvention tools like Tor and VPNs apply encryption to your traffic, thus protecting the secrecy of the requested data, including the IP address of the requested service. They hide the address until your request arrives at a proxy server in another country. The proxy then decrypts that address, sends your request to see the content, accepts the response from the page or service, encrypts it again and sends it back to your device. We sometimes use "tunnels" as a metaphor for this: your traffic is still passing through infrastructure controlled by the ISP, government or other institutions that wants to block your access, but their filters are unable to read the content of your request or determine exactly where you're trying to go when you leave the tunnel. All they know is that you are interacting with a proxy and that encryption is being used to prevent them from seeing the information you're requesting.

- [Learn how to choose the censorship circumvention tool that is right for you](https://securityinabox.org/en/internet-connection/circumvention).

### [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#blocking-resistance) Blocking resistance

Of course, the government agency in charge of internet filters — or the company that provides your government with blocking software — might eventually identify that unknown computer as a proxy, and add it to their blocklist. This is why VPNs and other tools sometimes stop working.

However, it usually takes time for those blocking the internet to discover proxies. Tools for visiting blocked websites use one or more of the following techniques:

- **Hidden proxies** can be distributed to users in a way that prevents censors from finding them all at once.
- **Private proxies** limit the number of people who know about and can access them, making it harder for authorities to find and block them. You can create a private proxy using for example [Outline](https://securityinabox.org/en/internet-connection/tools/#outline-vpn) or [Algo](https://securityinabox.org/en/internet-connection/tools/#algo-vpn).
- **Disposable proxies** can be replaced more quickly than they can be blocked.
- **Obfuscation** disguises proxy traffic as normal internet traffic thus keeping censors from identifying unknown proxies.
- **Domain fronting** makes it harder to block a web address as this blockage would also block access to other useful, popular services (such as Google).

## [Anchor](https://securityinabox.org/en/internet-connection/how-the-internet-works/\#further-reading) Further Reading

- Surveillance Self-Defense, [How to: Understand and Circumvent Network Censorship](https://ssd.eff.org/module/understanding-and-circumventing-network-censorship)
- [Security in a box guide on accessing blocked websites](https://securityinabox.org/en/internet-connection/circumvention).