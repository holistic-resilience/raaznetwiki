[Skip to content](https://www.privacyguides.org/en/news-aggregators/#aggregator-clients)

![](https://www.privacyguides.org/en/assets/img/cover/news-aggregators.webp)

# News Aggregators

[Edit this page](https://github.com/privacyguides/privacyguides.org/blob/main/docs/news-aggregators.md?plain=1 "Edit this page")

Protects against the following threat(s):

- [Service Providers](https://www.privacyguides.org/en/basics/common-threats/#privacy-from-service-providers)

A **news aggregator** is software which aggregates digital content from online newspapers, blogs, podcasts, and other resources to one location for easy viewing. Using one can be a great way to keep up with your favorite content.

## Aggregator clients

### Akregator

![Akregator logo](https://www.privacyguides.org/en/assets/img/news-aggregators/akregator.svg)

**Akregator** is a news feed reader that is a part of the [KDE](https://kde.org/) project. It comes with a fast search, advanced archiving functionality, and an internal browser for easy news reading.

[Homepage](https://apps.kde.org/akregator) [Privacy Policy](https://kde.org/privacypolicy-apps "Privacy Policy") [Documentation](https://docs.kde.org/?application=akregator "Documentation") [Source Code](https://invent.kde.org/pim/akregator "Source Code") [Contribute](https://kde.org/community/donations "Contribute")

Downloads

- [Flathub](https://flathub.org/apps/details/org.kde.akregator)

### NewsFlash

![NewsFlash logo](https://www.privacyguides.org/en/assets/img/news-aggregators/newsflash.png)

**NewsFlash** is an open-source, modern, and easy-to-use news feed reader for Linux. It can be used offline or with services like [Inoreader](https://inoreader.com/) or [Nextcloud News](https://apps.nextcloud.com/apps/news). It has a search feature and a pre-defined list of sources that you can add directly.

[Repository](https://gitlab.com/news-flash/news_flash_gtk#newsflash) [Source Code](https://gitlab.com/news-flash/news_flash_gtk "Source Code")

Downloads

- [Flathub](https://flathub.org/apps/io.gitlab.news_flash.NewsFlash)

### Feeder

![Feeder logo](https://www.privacyguides.org/en/assets/img/news-aggregators/feeder.png)

**Feeder** is a modern RSS client for Android that has many [features](https://github.com/spacecowboy/Feeder#features) and works well with folders of RSS feeds.

It supports [RSS](https://en.wikipedia.org/wiki/RSS), [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard)), [RDF](https://en.wikipedia.org/wiki/RDF%2FXML), and [JSON Feed](https://en.wikipedia.org/wiki/JSON_Feed).

[Repository](https://github.com/spacecowboy/Feeder#readme) [Source Code](https://github.com/spacecowboy/Feeder "Source Code") [Contribute](https://ko-fi.com/spacecowboy "Contribute")

Downloads

- [Google Play](https://play.google.com/store/apps/details?id=com.nononsenseapps.feeder.play)
- [GitHub](https://github.com/spacecowboy/Feeder/releases)

### Miniflux

![Miniflux logo](https://www.privacyguides.org/en/assets/img/news-aggregators/miniflux.svg#only-light)![Miniflux logo](https://www.privacyguides.org/en/assets/img/news-aggregators/miniflux-dark.svg#only-dark)

**Miniflux** is a web-based news aggregator that you can self-host.

It supports [RSS](https://en.wikipedia.org/wiki/RSS), [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard)), [RDF](https://en.wikipedia.org/wiki/RDF%2FXML), and [JSON Feed](https://en.wikipedia.org/wiki/JSON_Feed).

[Homepage](https://miniflux.app/) [Documentation](https://miniflux.app/docs/index#user-guide "Documentation") [Source Code](https://github.com/miniflux/v2 "Source Code") [Contribute](https://miniflux.app/#donations "Contribute")

### NetNewsWire

![NetNewsWire logo](https://www.privacyguides.org/en/assets/img/news-aggregators/netnewswire.png)

**NetNewsWire** is a free and open-source feed reader for macOS and iOS with a focus on a native design and feature set.

It supports conventional feed formats and includes built-in support for Reddit feeds.

[Homepage](https://netnewswire.com/) [Privacy Policy](https://netnewswire.com/privacypolicy "Privacy Policy") [Documentation](https://netnewswire.com/help "Documentation") [Source Code](https://github.com/Ranchero-Software/NetNewsWire "Source Code")

Downloads

- [App Store](https://apps.apple.com/app/id1480640210)
- [macOS](https://netnewswire.com/)

### Newsboat

![Newsboat logo](https://www.privacyguides.org/en/assets/img/news-aggregators/newsboat.svg)

**Newsboat** is an RSS/Atom feed reader for the text console. It's an actively maintained fork of [Newsbeuter](https://en.wikipedia.org/wiki/Newsbeuter). It is very lightweight and ideal for use over [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell).

[Homepage](https://newsboat.org/) [Documentation](https://newsboat.org/releases/2.38/docs/newsboat.html "Documentation") [Source Code](https://github.com/newsboat/newsboat "Source Code")

## Criteria

**Please note we are not affiliated with any of the projects we recommend.** In addition to [our standard criteria](https://www.privacyguides.org/en/about/criteria/), we have developed a clear set of requirements to allow us to provide objective recommendations. We suggest you familiarize yourself with this list before choosing to use a project, and conduct your own research to ensure it's the right choice for you.

- Must be open-source software.
- Must operate locally, i.e. must not be a cloud service.

## Social Media RSS Support

Some social media services also support RSS, although it's not often advertised.

### Reddit

Reddit allows you to subscribe to Subreddits via RSS.

Example

Replace `[SUBREDDIT]` with the Subreddit you wish to subscribe to.

```
https://reddit.com/r/[SUBREDDIT]/new/.rss
```

### YouTube

You can subscribe to YouTube channels without logging in and associating usage information with your Google account.

Example

To subscribe to a YouTube channel with an RSS client, first look for its [channel code](https://support.google.com/youtube/answer/6180214). The channel code can be found in the expanded description (i.e., the "About" section) of the YouTube channel you wish to subscribe to: **About** → **Share channel** → **Copy channel ID**. Replace `[CHANNEL ID]` below:

```
https://youtube.com/feeds/videos.xml?channel_id=[CHANNEL ID]
```

Was this page helpful?











Thanks for your feedback!











Thanks for your feedback! If you want to let us know more, please leave a post on our [forum](https://discuss.privacyguides.net/c/site-development/7).