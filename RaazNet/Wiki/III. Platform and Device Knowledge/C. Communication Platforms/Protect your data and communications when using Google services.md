---
title: "Protect Your Data and Communications When Using Google Services"
tags: [google, gmail, google-drive, account-security, privacy, two-factor-authentication]
category: "Account Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, Human Rights Defenders]
topics: ["Digital Security", "Privacy Protection", "Account Management", "Email Security"]
summary: "Comprehensive guide to securing your Google account, Gmail, Google Drive, Photos, and Maps with privacy-focused best practices."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Active Google account"]
estimated_read_time: "25 minutes"
---

# Protect Your Data and Communications When Using Google Services

*Updated 5 December 2024*

Read this guide to learn how to secure your Google account, including your usage of Gmail, Google Drive, Google Photos, and Google Maps.

**Related guides:**
- [YouTube security guide](https://securityinabox.org/en/tools/youtube) for privacy when sharing and viewing videos
- [Android guide](https://securityinabox.org/en/phones-and-computers/android/) for using Google's mobile operating system securely

> **Important consideration:** Before relying on commercial, corporate products, evaluate whether they can adequately protect your information. Commercial corporations might not share your values, may remove or filter content that they believe violates their policies, and may struggle to understand your local context—particularly if they do not operate in your language.

---

## Table of Contents

1. [Understanding Your Google Account](#understanding-your-google-account)
2. [Google's Policies and Data Usage](#googles-policies-and-data-usage)
3. [Creating a New Account](#creating-a-new-account)
4. [Protecting Your Account](#protecting-your-account)
5. [Using Google Services Securely](#using-google-services-securely)
6. [Checking for Suspicious Access](#checking-for-suspicious-access)
7. [Managing Shared Information](#managing-shared-information)
8. [Controlling Who Can Find or Contact You](#controlling-who-can-find-or-contact-you)
9. [Leaving No Trace](#leaving-no-trace)
10. [Handling Abuse](#handling-abuse)

---

## Understanding Your Google Account

When you create a Gmail account or start using Google Drive, you automatically create a Google account that provides access to all Google services, including Google Workspace and YouTube.

**Key privacy consideration:** When logged into your Google account while using your browser or Android device, you may share data about yourself and your internet usage—including activity on non-Google services. Log out of your Google account when you've finished using Google services.

**Alternative approaches:**
- Use a dedicated browser exclusively for Google services
- [Use an email client](https://securityinabox.org/en/tools/google/#download-your-mail) to read Gmail
- [Use Android devices without a Google account](https://securityinabox.org/en/phones-and-computers/android/#advanced-use-android-without-a-google-account)
- Maintain multiple Google accounts for different activities (see [multiple identity management](https://securityinabox.org/en/communication/multiple-identities))

---

## Google's Policies and Data Usage

### Understanding Terms of Service

- Review clarified terms on [Terms of Service; Didn't Read](https://tosdr.org/en/service/217)
- Read [Google's policies](https://policies.google.com/), including their [privacy policy](https://policies.google.com/privacy) and [terms of service](https://policies.google.com/terms)
- Install the [Terms of Service; Didn't Read browser extension](https://tosdr.org/en/sites/download) for quick policy overviews

**Why this matters:** Online service providers often have unclear policies about data handling. Your data might be combined with other information to make inferences about you, or sold to other companies. Understanding these policies helps you make informed decisions.

### Government and Law Enforcement Requests

- Search for "Google" and your country on [Lumen](https://lumendatabase.org/) to see content removal requests
- Review [Google's policy on law enforcement requests](https://policies.google.com/terms/information-requests)

**Why this matters:** Social media sites may provide your information—including private data—to governments or law enforcement when requested. Understanding these conditions helps you assess your risk.

---

## Creating a New Account

You can [create a Google account](https://support.google.com/accounts/answer/27441) for free (personal, organizational, business, or child accounts). [Paid plans](https://support.google.com/a/answer/6043576) offer additional features, with free options for [frontline workers](https://support.google.com/a/answer/10393656) and [educational institutions](https://support.google.com/a/answer/134628).

### Identity Considerations

**Using real vs. fake names:**
- Even with a fake name, you may be identifiable by your network connection and IP address unless you [use a VPN or Tor](https://securityinabox.org/en/communication/multiple-identities/#hide-your-ip-address)
- Consider separate accounts for different campaigns and activities
- At minimum, keep personal and work accounts separate

### Account Setup Process

Create a new Google account without providing another email address:

1. Go to the [Google Account sign in page](https://accounts.google.com/signin)
2. Click **Create account** → **For my personal use**
3. Enter your first and last name (they don't need to be real) → **Next**
4. Enter birthday and gender (they don't need to be real) → **Next**
5. Select **Create a Gmail address** → **Next**
6. Choose or create an email address → **Next**
7. Enter a strong, unique password twice → **Next**

**Why create without linking:** If you need to hide your identity, start fresh without connecting to existing accounts or email addresses tied to your name. For maximum anonymity, also [avoid connecting to your phone or IP](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails).

### Phone Number Considerations

**Recommendation:** Do not enter your phone number when setting up a new account if possible.

**Why:** Your phone number can easily be used to identify you. Consider whether local law enforcement could request information from service providers using your phone number, or whether someone seeking to harass or locate you might exploit it.

### Designating an Account Manager

- Choose a [trusted contact](https://support.google.com/accounts/answer/3036546) to receive an email if your account is unused for 3+ months, who can then download specified data
- For emergency access needs, share login information via [secure communication](https://securityinabox.org/en/communication/private-communication)
- If someone you know has been arrested, see the [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/arrested/)

**Why this matters:** Designating someone ensures others are notified of your situation and prevents malicious actors from defacing, hacking, or exploiting your account and contacts.

### Data Portability

Test how to [download your data](https://support.google.com/accounts/answer/3024190) from your Google Account. Start the download, review what data is provided, assess the format, and understand how you can use it.

**Why this matters:** Before storing data on any large platform, understand what it takes to migrate elsewhere. Complete deletion from servers may also take considerable time.

---

## Protecting Your Account

### Recovery Information

- [Check your recovery email](https://myaccount.google.com/recovery/email)
- [Check your recovery phone number](https://myaccount.google.com/signinoptions/rescuephone)
- Update immediately if you lose access to either

**Why this matters:** Recovery information helps you regain access and receives security notifications. An attacker could change these to gain future control. Secure your recovery email and phone—an adversary could hack them to change your password.

### Strong Passwords

Use strong passwords to protect your accounts. Access to your Google account means access to extensive information about you and your contacts.

See: [How to create and maintain strong passwords](https://securityinabox.org/en/password/passwords)

### Two-Step Verification

**Recommended methods (in order of security):**
1. Security key
2. Authenticator app
3. Security codes

**Avoid if possible:** SMS or phone calls—your mobile provider has full access to these communications, and they're easier to compromise. This is especially important if your official name isn't associated with your account.

See: [Guide on two-factor authentication](https://securityinabox.org/en/passwords/2fa)

### Backup Codes

- [Get backup codes](https://support.google.com/accounts/answer/1187538) for signing in without your usual 2-step method
- [Use Google security codes on Android devices](https://support.google.com/accounts/answer/6046815)

**Why this matters:** Safely stored backup codes provide another way to access your account if you lose your 2-step verification method.

### Advanced Protection Program

For users at high risk of digital attacks (human rights defenders, journalists):

- [Get started with Advanced Protection](https://landing.google.com/advancedprotection/#enroll-in-minutes)
- [Enable on mobile devices](https://support.google.com/accounts/answer/7519408)
- [Watch the explainer video](https://youtu.be/Twe0qlqyTfo)
- [Read the FAQ](https://landing.google.com/advancedprotection/faq/)

**Requirements:** A FIDO-compliant security key ([Google Titan](https://cloud.google.com/security/products/titan-security-key?hl=en), [Yubikey](https://www.yubico.com/products/), [Nitrokey](https://www.nitrokey.com/products/nitrokeys), or [Thetis](https://thetis.io/)), or a passkey (see [passkey security recommendations](https://securityinabox.org/en/passwords/passwords/#consider-how-and-when-to-use-passkeys)).

**Trade-offs:** You'll need your security key or passkey to sign in on new devices, and some apps requiring access to sensitive data (emails, Google Drive) won't work.

### Regular Security Reviews

- Review [your Google Account security page](https://myaccount.google.com/security) regularly
- Run the [security checkup](https://myaccount.google.com/security-checkup)
- Complete the [privacy check-up](https://myaccount.google.com/privacycheckup)

### Lost or Stolen Devices

- [Find, lock, or erase a stolen Android device](https://support.google.com/accounts/answer/6160491)
- [Sign out from lost/stolen devices](https://support.google.com/accounts/answer/3067630#remove)
- See the [Digital First Aid Kit: I lost my device](https://digitalfirstaid.org/topics/lost-device/)

### Phishing Awareness

[View security events in your account](https://support.google.com/accounts/answer/6063333) to verify legitimate communications.

**Important:** If you receive a security email or text claiming to be from Google, don't click links or provide your password. Instead, log in directly to your account and check the security page.

---

## Using Google Services Securely

### Gmail

While Gmail offers an intuitive interface, reliable service, and substantial storage, it's a commercial service not primarily focused on privacy protection.

**For privacy-focused alternatives:** See the [communication tools section](https://securityinabox.org/en/communication/tools/#more-secure-email-providers) and [email provider selection criteria](https://securityinabox.org/en/communication/secure-email/#choose-an-email-provider).

**Essential reading:** [Guide on securing email communications](https://securityinabox.org/en/communication/secure-email)

#### Downloading Your Mail

- [Add Gmail to an email client](https://support.google.com/mail/answer/7126229)
- [Add Gmail to Thunderbird](https://support.mozilla.org/en-US/kb/automatic-account-configuration)
- [Configure Thunderbird for Gmail](https://support.mozilla.org/en-US/kb/thunderbird-and-gmail)

**Recommended clients:** [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) to download email, delete from server, and organize locally.

#### End-to-End Encryption

**For Google Workspace Enterprise/Education Plus users:** Your administrator may have enabled [server-side S/MIME encryption](https://support.google.com/mail/answer/13317990).

**For standard Gmail accounts:** Use [OpenPGP-compatible tools](https://securityinabox.org/en/communication/tools/#email-applications-that-support-end-to-end-encryption):

- **Desktop:** [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird)
- **Mobile:** [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) with [OpenKeychain](https://securityinabox.org/en/communication/tools/#openkeychain)
- **Browser:** [Mailvelope](https://securityinabox.org/en/communication/tools/#mailvelope) or [FlowCrypt](https://flowcrypt.com/) ([setup guide](https://flowcrypt.com/docs))

#### Forwarding Settings

Check the [Forwarding and POP/IMAP settings](https://mail.google.com/mail/#settings/fwdandpop):

- Ensure **Disable forwarding** is selected
- Delete any email addresses you don't own or trust
- Disable POP/IMAP if you only use browser/mobile app; keep enabled if using an email client

**Why this matters:** Auto-forwarding is an easy way for attackers to access your email after compromising your account. Check this setting [especially if you suspect compromise](https://securityinabox.org/en/tools/google/#if-you-think-your-account-has-been-hacked).

### Google Drive

#### Secure Sharing

- Share with [specific persons](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-with-specific-people), [groups](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-with-a-group-of-specific-people), [anyone with the link](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Callow-general-access-to-the-file), or [publicly](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-a-file-publicly)
- [Stop sharing a file](https://support.google.com/drive/answer/2494893/#7014631)
- [Limit how files are shared](https://support.google.com/drive/answer/2494893/#restrict_sharing)
- [Transfer file ownership](https://support.google.com/drive/answer/2494892)

### Google Maps

#### Location Privacy

- [Manage your location when searching on Google](https://support.google.com/websearch/answer/179386)
- On Android: [Stop apps from using your phone's location](https://support.google.com/accounts/answer/6179507)

**Why this matters:** Stopping location storage protects against someone finding your current or past location. Disabling location services also improves battery life.

### Google Photos

#### Safe Photo Sharing

**Never post images that include:**
- Personally identifying information (full names, ID numbers, addresses)
- Information revealing where you live (pictures of your house)

**Consider carefully before posting:**
- Details about family members
- Information on sexual orientation or activities
- Images that could identify others without their consent

**Privacy settings:**
- [Manage face labeling and remove "me" labels](https://support.google.com/photos/answer/7378566)
- [Stop sharing with others](https://support.google