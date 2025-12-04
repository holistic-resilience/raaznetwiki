---
title: "Protect Your Data and Communications When Using Google Services"
tags: [google, privacy, security, email-security, account-protection, data-protection]
category: "Digital Security"
difficulty: "Intermediate"
audience: [General Public, Activists, Privacy-Conscious Users, IT Administrators]
topics: ["Account Security", "Privacy Protection", "Google Services", "Email Security"]
summary: "Comprehensive guide to securing your Google account, Gmail, Drive, Photos, and Maps with privacy-focused best practices."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Basic"
language: "English"
prerequisites: ["Basic computer literacy", "Active Google account"]
estimated_read_time: "25 minutes"
---

# Protect Your Data and Communications When Using Google Services

*Updated 5 December 2024*

This guide covers how to secure your Google account, including Gmail, Google Drive, Google Photos, and Google Maps. For related guides, see [YouTube security](https://securityinabox.org/en/tools/youtube) and [Android security](https://securityinabox.org/en/phones-and-computers/android/).

> **Important Consideration**: Commercial corporate products may not share your values and could remove or filter content based on their policies. They may also struggle to understand your local context, particularly if they don't operate in your language.

---

## Table of Contents

1. [Understanding Your Google Account](#understanding-your-google-account)
2. [Google's Policies and Data Practices](#googles-policies-and-data-practices)
3. [Creating a New Account](#creating-a-new-account)
4. [Protecting Your Account](#protecting-your-account)
5. [Using Google Services Securely](#using-google-services-securely)
6. [Checking for Suspicious Access](#checking-for-suspicious-access)
7. [Managing Your Information and Privacy](#managing-your-information-and-privacy)
8. [Handling Abuse and Harassment](#handling-abuse-and-harassment)

---

## Understanding Your Google Account

When you create a Gmail account or start using Google Drive, you automatically create a Google account that provides access to all Google services, including Google Workspace and YouTube.

### Key Privacy Considerations

- **Data sharing**: When logged into your Google account, you may share data about your internet usage, including non-Google services
- **Best practice**: Log out of your Google account when finished using Google services
- **Alternative approaches**:
  - Use a dedicated browser exclusively for Google services
  - [Use an email client](https://securityinabox.org/en/tools/google/#download-your-mail) to access Gmail
  - [Use Android without a Google account](https://securityinabox.org/en/phones-and-computers/android/#advanced-use-android-without-a-google-account)
  - Maintain [multiple accounts for different activities](https://securityinabox.org/en/communication/multiple-identities)

---

## Google's Policies and Data Practices

### Understanding Terms of Service

- Review simplified explanations at [Terms of Service; Didn't Read](https://tosdr.org/en/service/217)
- Read [Google's policies](https://policies.google.com/), including their [privacy policy](https://policies.google.com/privacy) and [terms of service](https://policies.google.com/terms)
- Install the [Terms of Service; Didn't Read browser extension](https://tosdr.org/en/sites/download) for quick overviews

> **Why this matters**: It's often unclear what service providers do with your information—whether it's combined with other data, sold to other companies, or shared without your consent.

### Government and Law Enforcement Requests

- Search for "Google" and your country on [Lumen](https://lumendatabase.org/) to see takedown requests
- Review [Google's law enforcement request policy](https://policies.google.com/terms/information-requests)

> **Why this matters**: Social media sites may provide your information to governments or law enforcement upon request, even information you intended to keep private.

---

## Creating a New Account

You can [create a Google account](https://support.google.com/accounts/answer/27441) for free. [Paid plans](https://support.google.com/a/answer/6043576) offer additional features, with free options for [frontline workers](https://support.google.com/a/answer/10393656) and [educational institutions](https://support.google.com/a/answer/134628).

### Identity Considerations

**Using Real vs. Fake Names**:
- Even with a fake name, you may be identifiable by your IP address unless you [use a VPN or Tor](https://securityinabox.org/en/communication/multiple-identities/#hide-your-ip-address)
- Consider separate accounts for different campaigns and activities
- At minimum, keep personal and work accounts separate

### Account Setup Process

1. Go to the [Google Account sign in page](https://accounts.google.com/signin)
2. Click **Create account** → **For my personal use**
3. Enter name (doesn't need to be real) → **Next**
4. Enter birthday and gender (doesn't need to be real) → **Next**
5. Select **Create a Gmail address** → **Next**
6. Choose or create an email address → **Next**
7. Enter a strong, unique password twice → **Next**

> **Privacy tip**: Create Gmail accounts without connecting them to existing email addresses if you need to hide your identity. For maximum anonymity, also [avoid connecting to your phone or IP](https://securityinabox.org/en/internet-connection/anonymity/#exchange-anonymous-emails).

### Phone Number Considerations

**Recommendation**: Don't associate your phone number with your account if possible.

> **Why**: Phone numbers can easily identify you. Consider whether local law enforcement could use your phone number to find activities associated with you, or whether someone seeking to harass you might use it.

### Emergency Access Planning

- Set up a [trusted contact](https://support.google.com/accounts/answer/3036546) who receives email if your account is unused for 3+ months
- Share login information via [secure communication](https://securityinabox.org/en/communication/private-communication) for emergencies
- If someone is arrested, consult the [Digital First Aid Kit troubleshooter](https://digitalfirstaid.org/arrested/)

### Data Portability

Test [downloading your data](https://support.google.com/accounts/answer/3024190) before storing significant information. Understand what formats are provided and how to use exported data.

---

## Protecting Your Account

### Recovery Information

- [Check your recovery email](https://myaccount.google.com/recovery/email)
- [Check your recovery phone](https://myaccount.google.com/signinoptions/rescuephone)
- Update immediately if you lose access to either

> **Security note**: Secure your recovery email and phone—attackers may compromise these to gain control of your main account.

### Password Security

Use strong, unique passwords. See the guide on [creating and maintaining strong passwords](https://securityinabox.org/en/password/passwords).

### Two-Step Verification

**Recommended methods** (in order of preference):
1. Security key
2. Authenticator app
3. Security codes

**Avoid if possible**: SMS or phone calls—mobile carriers have full access to these communications and they're easier to compromise.

See the [two-factor authentication guide](https://securityinabox.org/en/passwords/2fa) for setup instructions.

### Backup Codes

- [Get backup codes](https://support.google.com/accounts/answer/1187538) for account recovery
- [Use Google security codes on Android](https://support.google.com/accounts/answer/6046815)

### Advanced Protection Program

For high-risk users (journalists, human rights defenders), consider [Google's Advanced Protection Program](https://landing.google.com/advancedprotection/):

**Requirements**:
- FIDO-compliant security key ([Google Titan](https://cloud.google.com/security/products/titan-security-key), [Yubikey](https://www.yubico.com/products/), [Nitrokey](https://www.nitrokey.com/products/nitrokeys), or [Thetis](https://thetis.io/))
- Or a passkey (see [passkey security recommendations](https://securityinabox.org/en/passwords/passwords/#consider-how-and-when-to-use-passkeys))

**Trade-offs**:
- Requires security key/passkey for new device sign-ins
- Some apps requiring sensitive data access won't work

**Resources**:
- [Getting started guide](https://landing.google.com/advancedprotection/#enroll-in-minutes)
- [Mobile device setup](https://support.google.com/accounts/answer/7519408)
- [Explainer video](https://youtu.be/Twe0qlqyTfo)
- [FAQ](https://landing.google.com/advancedprotection/faq/)

### Regular Security Maintenance

- Review your [Google Account security page](https://myaccount.google.com/security) regularly
- Run the [security checkup](https://myaccount.google.com/security-checkup)
- Complete the [privacy checkup](https://myaccount.google.com/privacycheckup)

### Lost or Stolen Devices

- [Find, lock, or erase Android devices](https://support.google.com/accounts/answer/6160491)
- [Sign out from lost devices](https://support.google.com/accounts/answer/3067630#remove)
- Follow the [Digital First Aid Kit lost device guide](https://digitalfirstaid.org/topics/lost-device/)

### Phishing Protection

- [View security events](https://support.google.com/accounts/answer/6063333) to verify legitimate alerts
- Never click links in security emails—log in directly to verify

---

## Using Google Services Securely

### Gmail

While Gmail offers reliable service and large storage, it's a commercial service not primarily focused on privacy. Consider [more privacy-oriented providers](https://securityinabox.org/en/communication/tools/#more-secure-email-providers) and review [email provider selection criteria](https://securityinabox.org/en/communication/secure-email/#choose-an-email-provider).

#### Download Your Email

Use an email client like [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) to:
- Download and organize email locally
- Delete messages from Google's servers
- Maintain control over your data

**Setup guides**:
- [Add Gmail to an email client](https://support.google.com/mail/answer/7126229)
- [Add Gmail to Thunderbird](https://support.mozilla.org/en-US/kb/automatic-account-configuration)
- [Configure Thunderbird for Gmail](https://support.mozilla.org/en-US/kb/thunderbird-and-gmail)

#### End-to-End Encryption

**For Google Workspace Enterprise/Education users**: Your administrator may have enabled [client-side encryption via S/MIME](https://support.google.com/mail/answer/13317990).

**For standard Gmail accounts**:
- Use [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) with [OpenKeychain](https://securityinabox.org/en/communication/tools/#openkeychain)
- Install browser extensions: [Mailvelope](https://securityinabox.org/en/communication/tools/#mailvelope) or [FlowCrypt](https://flowcrypt.com/)

#### Check Forwarding Settings

Go to [Forwarding and POP/IMAP settings](https://mail.google.com/mail/#settings/fwdandpop):
- Ensure **Disable forwarding** is selected
- Remove unrecognized email addresses
- Disable POP/IMAP if only using browser/mobile app

> **Why**: Auto-forwarding is an easy way for attackers to maintain access after compromising your account.

### Google Drive

#### Secure Document Sharing

- Share with [specific people](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-with-specific-people), [groups](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-with-a-group-of-specific-people), [link holders](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Callow-general-access-to-the-file), or [publicly](https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cshare-a-file-publicly)
- [Stop sharing files](https://support.google.com/drive/answer/2494893/#7014631)
- [Limit sharing options](https://support.google.com/drive/answer/2494893/#restrict_sharing)
- [Transfer file ownership](https://support.google.com/drive/answer/2494892)

### Google Maps

#### Location Privacy

- [Manage location settings for Google Search](https://support.google.com/websearch/answer/179386)
- [Stop apps from using your location on Android](https://support.google.com/accounts/answer/6179507)

> **Benefits**: Prevents location tracking and extends battery life.

### Google Photos

#### Safe Photo Sharing

**Never post images showing**:
- Personally identifying information
- Information revealing where you live (e.g., pictures of your house)

**Think carefully before posting**:
- Images that could identify others
- Content others haven't consented to share

**Privacy settings**:
- [Manage face recognition and "me" labels](https://support.google.com/photos/answer/7378566)
- [Stop sharing with others](https://support.google.com/photos/answer/6280921)
- [Remove sharing partners](https://support.google.com/photos/answer/7378858)
- [Turn off contact sharing suggestions](https://support.google.com/photos/answer/7378859)
- [Review devices displaying your photos](https://support.google.com/photos/answer/9458709)
- [Remove metadata before posting](https://securityinabox.org/en/files/destroy-identifying-information/#remove-metadata-from-pictures-videos-and-other-files)

---

## Checking for Suspicious Access

### Review Sessions and Devices

- Check [devices with account access](https://support.google.com/accounts/answer/3067630)
- If suspicious activity appears, immediately change to a [new, strong passphrase](https://securityinabox.org/en/passwords/passwords)
- Save new passwords in your [password manager](https://securityinabox.org/en/passwords/password-managers)

### Login Notifications

[Google automatically sends notifications](https://support.google.com/accounts/answer/7305876) for logins from new devices.

### If Your Account Was Hacked

1. Use the [Security Checkup tool](https://myaccount.google.com/security-checkup)
2. Follow [Google's account recovery steps](https://support.google.com/accounts/answer/6294825)
3. If unsuccessful, consult the [Digital First Aid Kit account access troubleshooter](https://digitalfirstaid.org/topics/account-access-issues)

### Connected Apps and Sites

**Best practice**: Avoid using Google to log into other sites—this creates additional attack vectors and leaves more evidence of your online activity.

Review connected services:
- [Third-party apps with account access](https://myaccount.google.com/permissions)
- [Sites where you use Sign in with Google](https://myaccount.google.com/connections)

---

## Managing Your Information and Privacy

### Profile Information

**Avoid sharing**:
- Personally identifying information
- Location details
- Information about family members
- Sexual orientation or activities (depending on your threat model)

**Best practices**:
- Get consent before posting about others
- Establish sharing guidelines with colleagues
- Remember that content can easily