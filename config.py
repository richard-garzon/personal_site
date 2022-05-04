import os

class Config(object):
    TWITTER_URL = os.environ.get('TWITTER_URL') or 'http//twitter.com'
    LINKEDIN_URL = os.environ.get('LINKEDIN_URL') or 'http://linkedin.com'
    GITHUB_URL = os.environ.get('GITHUB_URL') or 'http://github.com'
