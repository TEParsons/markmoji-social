from markmoji.tests import BaseHandlerTests
from markmoji_social.handlers import FacebookPostHandler, InstagramPostHandler, LinkedInPostHandler, TootHandler, TumblrPostHandler, TweetHandler


class TestFacebookPostHandler(BaseHandlerTests):
    handler = FacebookPostHandler


class TestInstagramPostHandler(BaseHandlerTests):
    handler = InstagramPostHandler


class TestLinkedInPostHandler(BaseHandlerTests):
    handler = LinkedInPostHandler


class TestTootHandler(BaseHandlerTests):
    handler = TootHandler


class TestTumblrPostHandler(BaseHandlerTests):
    handler = TumblrPostHandler


class TestTweetHandler(BaseHandlerTests):
    handler = TweetHandler
