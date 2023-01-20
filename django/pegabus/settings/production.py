"""Production extension settings."""
import os

from pegabus.settings.main import *  # noqa pylint: disable=W0614,W0401
from pegabus.settings.jazzmin import *  # noqa pylint: disable=W0614,W0401

DEBUG = False

ALLOWED_HOSTS = ['*']

COMPRESS_OFFLINE = True

STATIC_ROOT = os.getenv('STATIC_ROOT')
MEDIA_ROOT = os.getenv('MEDIA_ROOT')
