---
title: "Protect Your Data and Communications When Using Google Services"
tags: [google, privacy, security, gmail, google-drive, account-security, digital-rights]
category: "Account Security"
difficulty: "Intermediate"
audience: [General Public, Privacy-Conscious Users, Activists, Journalists]
topics: ["Google Account Security", "Privacy Protection", "Email Security", "Data Management"]
summary: "Comprehensive guide to securing your Google account, Gmail, Drive, Photos, and Maps with privacy-focused configurations and security best practices."
source: "Security in a Box"
content_type: "Educational Guide"
security_level: "Informational"
language: "English"
prerequisites: ["Basic computer literacy", "Active Google account"]
estimated_read_time: "25 minutes"
---

# Protect Your Data and Communications When Using Google Services

Read this guide to learn how to secure your Google account, including Gmail, Google Drive, Google Photos, and Google Maps.

> **Note:** Consider whether relying on commercial, corporate products is secure enough to protect your information. Commercial corporations might not share your values and may remove or filter content they believe violates their policies. They may also struggle to understand your local context, particularly if they don't operate in your language.

## Understanding Your Google Account

When you create a Gmail account or start using Google Drive, you automatically create a Google account that provides access to all of Google's services, including Google Workspace and YouTube. 

**Important considerations:**
- Logging into your Google account shares data about you and your internet usage, including non-Google services
- Log out of your Google account when you've finished using Google services
- Consider using a dedicated browser only for Google services
- Use an email client to read your Gmail instead of the web interface
- You can use Android devices without a Google account
- Consider using multiple Google accounts for different activities (see [multiple identity management](https://securityinabox.org/en/communication/multiple-identities))

## Google's Policies and Data Practices

### Understanding Terms of Service
- Review Google's terms on [Terms of Service; Didn't Read](https://tosdr.org/en/service/217)
- Read [Google's policies](https://policies.google.com/), including their [privacy policy](https://policies.google.com/privacy) and [terms of service](https://policies.google.com/terms)
- Install the [Terms of Service; Didn't Read browser extension](https://tosdr.org/en/sites/download) to see overviews for services you use

### Government and Law Enforcement Requests
- Search for "Google" and your country on [Lumen](https://lumendatabase.org/) to see takedown requests
- Review [Google's policy on law enforcement requests](https://policies.google.com/terms/information-requests)

Social media sites may provide your information to governments or law enforcement when requested, even information you tried to keep private.

## Creating a New Account

You can [create a Google account](https://support.google.com/accounts/answer/27441) for free. Google also offers [paid plans](https://support.google.com/a/answer/6043576) (free for [frontline workers](https://support.google.com/a/answer/10393656) and [educational institutions](https://support.google.com/a/answer/134628)).

### Identity Considerations

- Even with a fake name, you may be identifiable by your IP address unless you [use a VPN or Tor](https://securityinabox.org/en/communication/multiple-identities/#hide-your-ip-address)
- Consider separate accounts for different campaigns and activities
- Keep personal and work accounts separate

### Setting Up Without Linking Personal Information

To create an account without providing another email address:

1. Go to the [Google Account sign in page](https://accounts.google.com/signin)
2. Click **Create account** → **For my personal use**
3. Enter a name (doesn't need to be real) → **Next**
4. Enter birthday and gender (don't need to be real) → **Next**
5. Select **Create a Gmail address** → **Next**
6. Choose or create an email address → **Next**
7. Enter a strong, unique password twice → **Next**

**Don't associate your phone number:** Your phone number can easily identify you. Consider whether providing it increases your risk.

### Account Inheritance Planning

- Designate a trusted contact to receive an email if your account is unused for 3+ months
- For emergencies, share login information via [secure communication](https://securityinabox.org/en/communication/private-communication)
- If someone you know is arrested, see [Digital First Aid Kit: Someone I Know Has Been Arrested](https://digitalfirstaid.org/arrested/)

### Data Portability

Before storing data on any platform, test how to download your data from your Google Account. Assess what's provided, in what format, and how you can use it.

## Protecting Your Account

### Recovery Information
- [Check your recovery email](https://myaccount.google.com/recovery/email)
- [Check your recovery phone number](https://myaccount.google.com/signinoptions/rescuephone)
- Update immediately if you lose access to either

Secure your recovery email and phone number—an adversary could hack them to change your password.

### Strong Passwords
Use strong passwords for your accounts. See our guide on [creating and maintaining strong passwords](https://securityinabox.org/en/password/passwords).

### Two-Step Verification

Set up 2-step verification using:
- **Recommended:** Security key, authenticator app, or security codes
- **Avoid if possible:** SMS or phone calls (your mobile carrier has access, and these are easier to hack)

See our [guide on two-factor authentication](https://securityinabox.org/en/passwords/2fa).

### Backup Codes
- [Get backup codes](https://support.google.com/accounts/answer/1187538) for when you can't use your usual 2-step method
- [Use a Google security code on Android](https://support.google.com/accounts/answer/6046815)

### Advanced Protection Program

For high-risk individuals (journalists, human rights defenders):

- [Get started with Advanced Protection](https://landing.google.com/advancedprotection/#enroll-in-minutes)
- [Enable on mobile devices](https://support.google.com/accounts/answer/7519408)
- [Read the FAQ](https://landing.google.com/advancedprotection/faq/)

**Requirements:** A FIDO-compliant security key (Google Titan, Yubikey, Nitrokey, or Thetis) or passkey.

**Note:** This restricts normal usage—you'll need your security key for new device logins, and some apps requiring sensitive data access won't work.

### Regular Security Checkups
- Review [your Google Account security page](https://myaccount.google.com/security) regularly
- Run the [security checkup](https://myaccount.google.com/security-checkup)
- Complete the [privacy checkup](https://myaccount.google.com/privacycheckup)

### Lost or Stolen Devices
- [Find, lock, or erase a stolen Android device](https://support.google.com/accounts/answer/6160491)
- [Sign out from lost devices](https://support.google.com/accounts/answer/3067630#remove)
- See [Digital First Aid Kit: I lost my device](https://digitalfirstaid.org/topics/lost-device/)

### Phishing Awareness
- [View security events in your account](https://support.google.com/accounts/answer/6063333)
- Never click links in security emails—log in directly to verify

## Using Google Services Securely

### Gmail

Gmail is convenient but not primarily focused on privacy. For privacy-oriented alternatives, see our [communication tools section](https://securityinabox.org/en/communication/tools/#more-secure-email-providers).

#### Download Your Mail
Use an email client like [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) to download, organize, and delete email from the server.

- [Add Gmail to an email client](https://support.google.com/mail/answer/7126229)
- [Add Gmail to Thunderbird](https://support.mozilla.org/en-US/kb/automatic-account-configuration)

#### End-to-End Encryption

For standard Gmail accounts, use OpenPGP-compatible tools:
- [Thunderbird](https://securityinabox.org/en/communication/tools/#thunderbird) or [K-9 Mail](https://securityinabox.org/en/communication/tools/#k-9-mail) with [OpenKeychain](https://securityinabox.org/en/communication/tools/#openkeychain)
- Browser extensions: [Mailvelope](https://securityinabox.org/en/communication/tools/#mailvelope) or [FlowCrypt](https://flowcrypt.com/)

#### Check Forwarding Settings
In [Forwarding and POP/IMAP settings](https://mail.google.com/mail/#settings/fwdandpop):
- Ensure "Disable forwarding" is selected
- Delete unfamiliar email addresses
- Disable POP/IMAP if only using browser or mobile app

### Google Drive

#### Secure Sharing
- [Share with specific people](https://support.google.com/drive/answer/2494822)
- [Stop sharing a file](https://support.google.com/drive/answer/2494893/#7014631)
- [Limit sharing options](https://support.google.com/drive/answer/2494893/#restrict_sharing)
- [Transfer ownership](https://support.google.com/drive/answer/2494892)

### Google Maps

#### Disable Location Sharing
- [Manage your location in Google Search](https://support.google.com/websearch/answer/179386)
- [Stop apps from using your phone's location](https://support.google.com/accounts/answer/6179507)

Disabling location services also improves battery life.

### Google Photos

#### Safe Sharing Practices

**Never post images that include:**
- Personally identifying information
- Information revealing where you live (like photos of your house)

**Think carefully before posting:**
- Images that identify others without consent
- Location metadata

**Privacy settings:**
- [Manage face labeling and remove "me" labels](https://support.google.com/photos/answer/7378566)
- [Stop sharing](https://support.google.com/photos/answer/6280921)
- [Remove sharing partners you don't recognize](https://support.google.com/photos/answer/7378858)
- [Turn off contact sharing suggestions](https://support.google.com/photos/answer/7378859)
- [Review devices you're sharing to](https://support.google.com/photos/answer/9458709)
- [Remove metadata before posting](https://securityinabox.org/en/files/destroy-identifying-information/#remove-metadata-from-pictures-videos-and-other-files)

## Checking for Suspicious Access

### Review Sessions and Devices
- Check which devices have logged into your account
- If you see suspicious activity, immediately change your password to a new, random passphrase
- [Check devices with account access](https://support.google.com/accounts/answer/3067630)

### Login Notifications
[Google automatically sends notifications](https://support.google.com/accounts/answer/7305876) for logins from new devices.

### If Your Account Was Hacked
- Use the [Security Checkup tool](https://myaccount.google.com/security-checkup)
- Follow [Google's steps for compromised accounts](https://support.google.com/accounts/answer/6294825)
- See [Digital First Aid Kit: I lost access to my account](https://digitalfirstaid.org/topics/account-access-issues)

### Connected Apps and Sites
- Avoid using Google to log into other sites
- Use different passwords for every site
- Review connected apps in your account settings

## Managing Your Information

### Profile Information
Avoid sharing publicly:
- Personally identifying information
- Details about family members
- Sexual orientation or activities (depending on your threat assessment)

**Best practices:**
- Agree with your network on what to share for safety
- Consider what you reveal about friends
- Ask others to be sensitive about what they share about you

### Birthday
When registering, you can provide a fake birthday. Once added, you can't delete it but can control who sees it.

## Controlling Contact and Discovery

### Block Unwanted Contacts
[Block an email address](https://support.google.com/mail/answer/8151) to stop harassment in private messages.

### Disable Ad Personalization
[Turn off ad personalization](https://adssettings.google.com/)—governments or police may buy advertising data to target you.

## Leaving No Trace

### Public or Shared Devices
- Avoid accessing your Google account from shared devices
- Never save passwords on public machines
- Delete browsing history after use
- Change passwords of any accessed accounts as soon as possible

### Delete Search History
- [Clear Web & App Activity](https://myactivity.google.com/activitycontrols/webandapp)
- [Turn off activity tracking](https://myactivity.google.com/activitycontrols)
- [Delete activity from Google services](https://support.google.com/accounts/answer/465)

## Handling Abuse

### Reporting
- [Report abuse in Google Groups](https://support.google.com/groups/answer/81275)
- [Report Terms of Service violations](https://support.google.com/docs/answer/2463296)

### Doxxing and Personal Information Exposure
- [Remove sensitive information from Google searches](https://support.google.com/websearch/troubleshooter/3111061)
- [Request content removal from specific Google services](https://support.google.com/legal/troubleshooter/1114905)

### Botnets and Spam
- Use "(Send) Feedback" in most Google products
- [Report spam in Gmail](https://support.google.com/mail/answer/1366858)

### Impersonation
Google will [assist in removing fake pornography](https://support.google.com/websearch/answer/9116649) but generally won't remove parody impersonation.

### Content Filtering
- [SafeSearch blocks adult content](https://support.google.com/websearch/answer/510)
- [YouTube Restricted Mode blocks adult and violent content](https://support.google.com/youtube/answer/174084)

### Account Recovery
[Learn how to recover a disabled account](https://support.google.com/accounts/answer/40695). Human rights defenders have had accounts shut down for documenting abuses or being reported by adversaries.

### Taking a Break
[Set an automatic responder](https://support.google.com/mail/answer/25922) if you need time away or anticipate being unable to respond.