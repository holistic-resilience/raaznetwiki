\_\_('Table of Contents')

Communication › Secure your email communications

# [Anchor](https://securityinabox.org/en/communication/secure-email/\#secure-your-email-communications) Secure your email communications

Updated 10 October 2024

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#table-of-contents) Table of Contents

- [Choose an email provider](https://securityinabox.org/en/communication/secure-email/#choose-an-email-provider)
- [Secure your email account](https://securityinabox.org/en/communication/secure-email/#secure-your-email-account)
- [Consider using a disposable mail account](https://securityinabox.org/en/communication/secure-email/#consider-using-a-disposable-mail-account)
- [Consider using email aliases](https://securityinabox.org/en/communication/secure-email/#consider-using-email-aliases)
- [\[Optional\] Create an anonymous email](https://securityinabox.org/en/communication/secure-email/#optional-create-an-anonymous-email)
- [Decide how to access your mailbox](https://securityinabox.org/en/communication/secure-email/#decide-how-to-access-your-mailbox)
- [Consider regularly deleting mail stored on the server](https://securityinabox.org/en/communication/secure-email/#consider-regularly-deleting-mail-stored-on-the-server)
- [Organize your mailbox](https://securityinabox.org/en/communication/secure-email/#organize-your-mailbox)
- [Back up your mailbox](https://securityinabox.org/en/communication/secure-email/#back-up-your-mailbox)
- [Protect yourself from phishing and malware](https://securityinabox.org/en/communication/secure-email/#protect-yourself-from-phishing-and-malware)
- [\[Advanced\] Protect your email messages with end-to-end encryption](https://securityinabox.org/en/communication/secure-email/#advanced-protect-your-email-messages-with-end-to-end-encryption)
- [\[Advanced\] Beyond the body: learn to read an email header](https://securityinabox.org/en/communication/secure-email/#advanced-beyond-the-body-learn-to-read-an-email-header)

An email is a text message (which can be accompanied by file attachments) that you send through the browser or using a mail client app installed on your device (for example [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail)). When you click the Send button, your message reaches your email provider's servers, where it is stored (usually in your Sent folder) and can also be backed up. Your provider then forwards it to the server of the provider used by your recipients, where it is stored (and can be backed up again). Finally, the email is delivered to your recipients, who read it through their browsers or mail clients of choice. At this point recipients can decide to either keep the email stored online or download it to their devices and delete it from their provider's servers.

Nowadays many people use email only rarely, and prefer to use [encrypted chat apps](https://securityinabox.org/en/communication/secure-chat) or [video calls](https://securityinabox.org/en/communication/video-conference) for their everyday communications. However, we still use email for [many](https://www.reddit.com/r/sysadmin/comments/qyxzs2/is_email_being_replaced/) [different reasons](https://techcrunch.com/2016/06/28/you-cant-kill-email/), especially to create other online accounts and to organize our work and conversations based on different parameters.

By default, email is not the most secure method of online communication, since it is not encrypted, carries a lot of metadata, persists on the providers' servers and can expose you to phishing, [malware infections](https://securityinabox.org/en/phones-and-computers/malware/) and other attacks. Still, it is a resilient technology that will ensure the continuity of communications even if servers stop functioning for a while, and as explained in this guide, there are ways of making it more secure.

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#choose-an-email-provider) Choose an email provider

Ask yourself these questions to learn how to choose an email provider:

- Is it a mature platform? Is it actively maintained and developed? Does it have a large base of users?
- Where is the provider based? And where are the servers? Are they in a country that would comply with a request by authorities from your own country? And is that country enforcing human rights and consumer protection? It is important to know whether the email provider will respect your privacy and rights, and under what circumstances it will comply with requests to provide access to your information.
- Can you trust the owners of the servers both from a technical and an ethical point of view? What's their history and mission? Do they regularly publish transparency reports or canary statements? Have they been independently audited? Do they store information on their clients for a long time? If they ever received requests for information by state authorities, how did they respond?
- Do they use free and open-source software in their servers? If they offer a mobile app, is it also free and open-source?
- Do they encrypt email in transit with TLS? You can check if they do by [running a test on checktls.com](https://www.checktls.com/TestReceiver).
- Are individual mailboxes encrypted inside the server?
- Do they offer 2-factor authentication?
- Do they offer end-to-end encryption between their own users?
- Do they offer a way of encrypting emails in general through their app? Is this feature based on mature free and open-source software for end-to-end encryption like OpenPGP?
- Do they offer additional services like a calendar, a file storage platform or a VPN?
- Is it a paid service? If it's not paid, what's the provider's business model?

See [our list of email providers](https://securityinabox.org/en/communication/tools/#more-secure-email-providers) to decide where to create your new email account.

In some situations, you may choose to activate an email account on a mainstream server like Gmail, for example to avoid using an uncommon domain name that is mainly used by activists. If this is the case, take into account the risk that a commercial email provider may hand over your data to the authorities in case of an investigation and consider encrypting your email.

- If you decide to create a Gmail account, read [our guide on how to use Gmail more securely](https://securityinabox.org/en/tools/google).

Learn why we recommend this

Email was not built with a focus on security. It was developed in the 1970s, when it was used by a limited number of people who just needed to ensure that they could communicate with each other. Today, most email providers protect your messages with client-to-server encryption (using TLS) as they go from your device, through your local router and your ISP, to your email providers' servers. This stops anyone eavesdropping on your local network or on the wires that lead from your device to the email providers and to your recipient's devices from reading your messages. That's why we recommend email providers that, among other things, encrypt email in transit through TLS.

However, your messages remain unencrypted when they are stored on your device and on your email provider's servers as well as on the recipient's device and email provider's servers. This means someone with access to the servers or devices can read your email. Therefore we strongly recommend you to consider also [encrypting your messages](https://securityinabox.org/en/communication/secure-email/#advanced-protect-your-email-messages-with-end-to-end-encryption), especially if their content is particularly sensitive.

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#secure-your-email-account) Secure your email account

When creating a new email account, immediately secure it with a [strong password](https://securityinabox.org/en/passwords/passwords/) and, if possible, with [2-factor authentication](https://securityinabox.org/en/passwords/2fa/).

When setting your new password, you will probably also have to set one or more recovery questions. In these cases, it's always a good idea to provide fake replies. [Learn what kind of strategies you can apply in these cases in our guide on safe passwords](https://securityinabox.org/en/passwords/passwords/#set-safer-recovery-questions).

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#consider-using-a-disposable-mail-account) Consider using a disposable mail account

- If you need an email address only to receive emails for a short period of time, you can create a disposable mailbox on [Guerrilla Mail](https://www.guerrillamail.com/) or on [anonbox](https://anonbox.net/index.en.html).

Learn why we recommend this

If you need an email address in a one-off situation, for example to activate a service, you can use a disposable mailbox. This solution can help avoid exposing your main mailbox to spamming and other risks.

Note that you can use disposable emails to receive but not to send mails. If you would like to send messages that cannot be traced back to your main identity, read [the instructions on how to create an anonymous email](https://securityinabox.org/en/communication/secure-email/#optional-create-an-anonymous-email).

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#consider-using-email-aliases) Consider using email aliases

- Create an alternative address connected to your mailbox, for example to prevent spam.
  - Learn how to create an alias on [Proton Mail](https://proton.me/support/creating-aliases), [Riseup](https://riseup.net/en/email/settings/aliases#how-do-i-create-a-new-alias), [Autistici/Inventati](https://www.autistici.org/docs/userpanel#alias), [Disroot](https://howto.disroot.org/en/tutorials/email/webmail/settings/identities#creating-identities-alias), [Posteo](https://posteo.de/en/help/how-do-i-add-or-delete-an-email-alias) and [Mailfence](https://kb.mailfence.com/kb/what-is-the-difference-between-an-alias-and-a-mailbox/).
  - Learn how to configure [Thunderbird](https://support.mozilla.org/en-US/kb/using-identities) and [K-9 Mail](https://docs.k9mail.app/en/6.400/settings/account/#manage-identities) to send messages from an alias.

Learn why we recommend this

Most email services offer the possibility of creating an email alias or more. An alias is an additional email address for your mailbox. A message that is sent to an alias you have set up will be forwarded to your mailbox. You can also use an alias to send mail messages with a different sender name, but you have to configure this additional identity in your mail client or in the webmail. It's important to note that mail aliases are not anonymous: in most cases, they can be traced back to your main address by reading the headers of any message you send with your alias.

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#optional-create-an-anonymous-email)\[Optional\] Create an anonymous email

If you would like to create an email account that is not connected to your official identity and can't be traced back to you, follow [the instructions in our guide on anonymity to learn how to create and use an email account anonymously](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails).

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#decide-how-to-access-your-mailbox) Decide how to access your mailbox

- If the service you have chosen allows for it, use [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) on your computer.
  - [Learn how to set up an account in Thunderbird](https://support.mozilla.org/en-US/kb/automatic-account-configuration).
- If the service you have chosen does not offer a mobile app, use [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) on your mobile device or [Thunderbird](https://play.google.com/store/apps/dev?id=8696262544613553264) on Android.
  - [Learn how to set up an account in K-9 Mail](https://docs.k9mail.app/en/6.400/accounts/add/).
- If you have more than one email account, consider organizing all your mail in a mail client like [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) for computers and Android and [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) for mobile devices.
  - [Learn how to merge multiple mailboxes in a global inbox in Thunderbird](https://support.mozilla.org/en-US/kb/unify-your-pop-email-accounts-global-inbox).
  - [Add a second account in K-9 Mail](https://docs.k9mail.app/en/6.400/accounts/add_another/).

Learn why we recommend this

While all email providers offer a web interface and often also mobile apps to access your email, it can be convenient to organize all your email in one mail client like Thunderbird or K-9 Mail.

Mail clients also make it possible to decide whether you want to [download your mail to a secure device](https://securityinabox.org/en/communication/secure-email/#consider_regularly_deleting_mail_stored_on_the_server) or keep it in the server to be able to read it from different devices.

Read more on [Why Use a Mail Client vs Webmail in the Thunderbird blog](https://blog.thunderbird.net/2024/09/why-use-a-mail-client-vs-webmail/).

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#consider-regularly-deleting-mail-stored-on-the-server) Consider regularly deleting mail stored on the server

If you can, use a mail client like Thunderbird to download your email to a secure device and delete it from the server using POP3. If you need to access your messages from different devices (like your computer and your phone), you will not want to delete them from the server and it may be best to use IMAP instead.

Learn why we recommend this

You can find explanations on the difference between downloading email with POP3 (for example to delete your email from the server) or IMAP (to keep it on the server) in [the official Thunderbird documentation](https://support.mozilla.org/en-US/kb/difference-between-imap-and-pop3). Most email services provide instructions on how to set up an email client to receive your mail with POP3 or IMAP.

Consider that accessing your email through a mobile device is less secure than through a computer, since mobile devices can be easily lost and are generally harder to protect than computers.

If you decide to download all your email to a device, make sure that the device you use is [secure, regularly updated](https://securityinabox.org/en/phones-and-computers/) and [backed up](https://securityinabox.org/en/files/backup/).

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#organize-your-mailbox) Organize your mailbox

- Organize your email in Thunderbird:
  - Get to know the [Thunderbird interface](https://support.mozilla.org/en-US/kb/getting-started-thunderbird-main-window-supernova) and learn [how to organize your email through tags](https://support.mozilla.org/en-US/kb/message-tags) and [how to visualize tags together with folders](https://blog.thunderbird.net/2023/08/make-thunderbird-yours-how-to-get-the-thunderbird-115-supernova-look/).
  - [Search your email with Thunderbird's quick filter](https://support.mozilla.org/en-US/kb/quick-filter-toolbar).
  - Consider [organizing your email by using just 4 folders](https://blog.thunderbird.net/2024/06/chaotic-inbox-to-productivity-powerhouse/).
  - [Learn how to use filters in Thunderbird](https://support.mozilla.org/en-US/kb/organize-your-messages-using-filters).
  - [Learn how to train Thunderbird's spam filter](https://blog.thunderbird.net/2024/09/thunderbird-and-spam/).
  - [Organize conversations through message threading in Thunderbird](https://support.mozilla.org/en-US/kb/message-threading-thunderbird).
  - [Learn how to create templates in Thunderbird and avoid writing messages from scratch](https://blog.thunderbird.net/2024/08/maximize-your-day-templates-to-the-rescue/).
- Read [Cory Doctorow's tips on how to keep your inbox always empty](https://www.theguardian.com/technology/2008/apr/29/email.filter).

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#back-up-your-mailbox) Back up your mailbox

- Back up your email from your server to a secure device using [Thunderbird with POP3](https://securityinabox.org/en/communication/secure-email/#consider-regularly-deleting-mail-stored-on-the-server) (you can choose to [leave the mail on the server](https://support.mozilla.org/en-US/questions/1128358#answer-890862), if you need to access it from other devices).
- [Learn how to back up your Thunderbird profile](https://support.mozilla.org/en-US/kb/thunderbird-export), including accounts, messages, address books, and settings.
- [Learn how to restore the backup of your Thunderbird profile with the import tool](https://support.mozilla.org/en-US/kb/thunderbird-import).

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#protect-yourself-from-phishing-and-malware) Protect yourself from phishing and malware

- [Get in the habit of noticing when an email tries to pressure you to act quickly or appeal to your emotions](https://securityinabox.org/en/phones-and-computers/malware/#be-aware-that-malicious-actors-may-try-to-pressure-you-to-act-quickly-or-appeal-to-your-emotions), as it may be an attempt at making you open a malicious link, download an infected attachment or enter your login data in a phishing web page.

Learn why we recommend this

Security experts consider people's emotions and habits the most vulnerable part of digital security. When we are asked to take quick action, when we are curious, or when we feel threatened, we usually comply with the instructions we have received.

The stresses of human rights work can make us especially vulnerable to this kind of attacks. Many of us are convinced we could never be tricked, but thinking twice can stop attempts at installing malware in our devices and spy on us without us realizing what is going on.

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#advanced-protect-your-email-messages-with-end-to-end-encryption)\[Advanced\] Protect your email messages with end-to-end encryption

- Encrypt and sign your mail messages with OpenPGP using one of the following tools:
  - [Thunderbird](https://support.mozilla.org/en-US/kb/openpgp-thunderbird-howto-and-faq) (Windows, Linux, macOS, Android)
  - [K-9 Mail](https://k9mail.app/) and [OpenKeychain](https://www.openkeychain.org/) (Android)
    - Read [the guide in the K-9 Mail website](https://docs.k9mail.app/en/6.400/security/pgp/).
  - [Mailvelope](https://www.mailvelope.com/) (Chrome/Chromium, Firefox, Edge)
  - [FlowCrypt](https://flowcrypt.com/) (Android app for any email provider, iOS app for Gmail, browser extension/add-on for Gmail available for Firefox, Chrome/Chromium, Brave, Edge and Opera)
- Try email services that support encryption
  - [Proton Mail](https://proton.me/)
    - NOTE: Proton Mail does not automatically encrypt mail to someone whose address is not on Proton Mail. To encrypt to someone who does not use Proton Mail, you must [set a password the recipient can use to open the message](https://proton.me/support/password-protected-emails) or you may need to [exchange encryption public keys](https://proton.me/support/how-to-use-pgp).
  - [Mailfence](https://mailfence.com/en/)
    - NOTE: Mailfence does not automatically encrypt mail to someone whose address is not on Mailfence. To encrypt to someone who does not use Mailfence, you can [set a password the recipient can use to open the message](https://kb.mailfence.com/kb/how-to-use-symmetric-encryption/) or you can [exchange encryption public keys with your recipient](https://kb.mailfence.com/kb/how-to-send-an-openpgp-encrypted-and-signed-email/).

Learn why we recommend this

Email encryption uses complex mathematics to scramble the content of your files or messages so they can only be read by someone who has the "key" to decrypt it. Experts trust OpenPGP encryption because until now nobody managed to decrypt it without owning the necessary key.

Encrypting email is important. By default, your email is saved unencrypted on the servers of your own and your recipient's email provider, and may be saved, still unencrypted, on more than one of your recipient's devices, like their mobile and their computer. Anyone who has access to a server or device where your message is stored could potentially read its content. Encryption stops attackers from reading parts of the email that have been encrypted (e.g. body, attachments and in some cases the subject line), which will look to them like a sequence of nonsense characters.

It is worth noting, however, that encryption will not stop an attacker from learning where the message comes from, to whom it is addressed, when it was sent and other information contained in the [header of the email](https://securityinabox.org/en/communication/secure-email/#advanced-beyond-the-body-learn-to-read-an-email-header). This may or may not include the subject of the message (which sometimes is encrypted and sometimes isn't). An attacker could use this information to demonstrate that people are writing to each other, even without knowing what they are talking about.

## [Anchor](https://securityinabox.org/en/communication/secure-email/\#advanced-beyond-the-body-learn-to-read-an-email-header)\[Advanced\] Beyond the body: learn to read an email header

- Read [the guide on how to view and extract raw messages in common email clients on the website of the Computer Incident Response Center Luxembourg (CIRCL)](https://circl.lu/pub/tr-34/).
- Learn how to analyze email headers in the section on email headers of [Internews' Field Guide to incident response for civil society and media (2023, p. 60)](https://internews.org/wp-content/uploads/2023/11/Field-Guide-to-Threat-Labs.pdf).

Learn why we recommend this

Like a letter, an email consists of the body of the message and of additional information necessary, for example, for the message to reach its destination and for the recipient to know when the message was sent. This information usually includes the time and date when the email was sent, the sender's name, email address and IP address, the recipient's name and email address, the subject of the email and the time and date when the email was received by each computer on the route between the sender and the recipient. A header will also provide information on whether an email has been sent from an authorized system, so being able to read it can help you confirm that it is not spam and that the email of the alleged sender isn't spoofed. That's why in case of doubt (for example if you suspect the sender of an email is not who they say they are), it is important to be able to visualize the header and analyze it or send it to experts that can analyze it for you.