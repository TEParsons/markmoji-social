import re
from markmoji import handlers 



class FacebookPostHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded post (from Facebook).

    ### Parameters
    label (str)
    :    Unused as embedded posts don't have alt text

    link (str)
    :    Link to the post to embed
    """
    # F in a square looks like the facebook logo
    emoji = "🅵"

    example = "🅵<https://www.facebook.com/TheXKCD/posts/pfbid0KZZoxocUJYYE8NnZUHtpDkmr7Jw1qpMBE4QpFKBNBMVJByNX9iPctUfpRCmCwCiMl>"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<iframe src='https://www.facebook.com/plugins/post.php?href={self.link}' class=facebook-embed{self.html_params}></iframe>"


class InstagramPostHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded Instagram post.

    ### Parameters
    label (str)
    :    Unused as embedded posts don't have alt text

    link (str)
    :    Link to the post to embed
    """

    emoji = "📷"
    requirements = "<script async src='//www.instagram.com/embed.js'></script>"

    example = "📷<https://www.instagram.com/p/CkYXXhlt5N7>"
    __author__ = "🦊"

    @property
    def html(self):
        _, _, post_id = re.match("(https?://)?(www\.)?instagram\.com/p/([\w\d]*)", self.link).groups()

        return f"<blockquote class='instagram-media' data-instgrm-captioned data-instgrm-permalink='https://www.instagram.com/p/{post_id}/?utm_source=ig_embed&amp;utm_campaign=loading' data-instgrm-version='14'{self.html_params}><a href='https://www.instagram.com/p/{post_id}/?utm_source=ig_embed&amp;utm_campaign=loading'>{self.label}</a></blockquote>"


class LinkedInPostHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded LinkedIn post.

    ### Parameters
    label (str)
    :    Hover text for the iframe

    link (str)
    :    Link to the post - either an embed link, direct link or URD value
    """
    # Rainy cloud emoji, as cloud would be too easily confused with cloud storage
    emoji = "📠"

    example = "📠[My body is ready for this great advice](linkedin.com/posts/reggie-fils-aime-nintendo_former-nintendo-of-america-exec-shares-the-activity-6957484429954945024-8q95)"
    __author__ = "🦊"

    @property
    def html(self):
        url = self.link

        if "linkedin.com/posts/" in url:
            # If it's a post link, parse it to get the URD
            url = re.search("-(\d*)-", url).group(1)
        
        if "linkedin.com/embed/feed/update/" not in url:
            # If it's not an embed link, make it one
            url = f"https://www.linkedin.com/embed/feed/update/urn:li:activity:{url}"
        
        return f"<iframe src='{url}' title='{self.label}'></iframe>"


class TootHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded toot (from Mastodon).

    ### Parameters
    label (str)
    :    Unused as embedded toots don't have alt text

    link (str)
    :    Link to the toot to embed
    """
    # Elephant emoji, like what everyone's got on their Twitter usernames
    emoji = "🐘"
    requirements = "<script src='https://toot.wales/embed.js' async='async'></script>"

    example = "🐘<https://universeodon.com/@TheTweetOfGod/109597493614530062>"
    __author__ = "🦊"

    @property
    def html(self):
        link = self.link
        # Make sure we're using the /embed link
        _, embed = re.match("(https?://)?[\w\d]*\.com/@[\w\d]*/\d*(/embed)?", link).groups()
        if embed is None:
            link += "/embed"
        # Construct iframe
        return f"<iframe src='{link}' class='mastodon-embed'{self.html_params}></iframe>"


class TumblrPostHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded Tumblr post

    ### Parameters
    label (str)
    :    Unused as embedded Tumblr posts don't have alt text

    link (str)
    :    Link to the post to embed (format should be `{username}.tumblr.com/post/{numeric id}/whatever-else-it-doesn't-matter`)
    """

    emoji = "ⓣ"
    requirements = "<script async src='https://assets.tumblr.com/post.js'></script>"

    example = "ⓣ<https://tinyleavesdream.tumblr.com/post/663071895596548096>"
    __author__ = "🦊"

    @property
    def html(self):
        # Get username and post id from link
        _, username, post_id, _ = re.match("(https?://)?([\w\d\-_]*)\.tumblr\.com/post/(\d*)(/.*)?", self.link).groups()
        # Construct holder
        return f"<div class='tumblr-post' data-href='https://embed.tumblr.com/embed/post/{username}/{post_id}'{self.html_params}><a href='{self.link}'></a></div>"


class TweetHandler(handlers.MarkmojiHandler):
    """
    Handler for an embedded tweet.

    ### Parameters
    label (str)
    :    Unused as embedded tweets don't have alt text

    link (str)
    :    Link to the tweet to embed
    """
    # Bird emoji... because Twitter...
    emoji = "🐦"
    requirements = "<script async src='https://platform.twitter.com/widgets.js' charset='utf-8'></script>"

    example = "🐦<https://twitter.com/edballs/status/63623585020915713>"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<blockquote class=twitter-tweet{self.html_params}><a href='{self.link}'></a></blockquote>"