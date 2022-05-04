import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Config(object):
    TWITTER_URL = os.environ.get('TWITTER_URL') or 'http//twitter.com'
    LINKEDIN_URL = os.environ.get('LINKEDIN_URL') or 'http://linkedin.com'
    GITHUB_URL = os.environ.get('GITHUB_URL') or 'http://github.com'
