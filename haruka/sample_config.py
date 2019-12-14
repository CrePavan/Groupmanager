if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR KEY HERE"
    OWNER_ID = "YOUR ID HERE"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "YOUR USERNAME HERE"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # Some API is required for more features
    MAPS_API = None
    CAT_API_KEY = None
    DOG_API_KEY = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    STRICT_GBAN = False
    STRICT_GMUTE = False
    ALLOW_EXCL = True  # Allow ! commands as well as /

    # MEMES
    DEEPFRY_TOKEN = None  # Used for facial recognition in the deepfry command


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
