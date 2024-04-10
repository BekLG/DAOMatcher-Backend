from decouple import config


TIMEOUT = 10

LIX_API_KEY = config("LIX_API_KEY")
LIX_BASE_URL = "https://api.lix-it.com/v1"

LINKEDIN_PAYLOAD = {}
LINKEDIN_HEADERS = {"Authorization": LIX_API_KEY}

TWITTER_TOKEN = config("TWITTER_TOKEN")
TWITTER_API_KEY = config("TWITTER_API_KEY")
TWITTER_API_SECRET = config("TWITTER_API_SECRET")
TWITTER_BASE_URL = "https://api.twitter.com/2"
TWITTER_HEADERS = {"Authorization": f"Bearer {TWITTER_TOKEN}"}
TWITTER_PAYLOAD = {}


MASTEDON_BASE_URL = "https://{server}/api/v1/accounts"
# SECOND_MASTEDON_BASE_URL = "https://mastodon.social/api/v1/accounts"
