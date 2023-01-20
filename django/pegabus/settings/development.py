"""Development extension settings."""
from pegabus.settings.main import *  # noqa pylint: disable=W0614,W0401
from pegabus.settings.jazzmin import *  # noqa pylint: disable=W0614,W0401


DEBUG = True

ALLOWED_HOSTS = ['*']

COMPRESS_OFFLINE = False
