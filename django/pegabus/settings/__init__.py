'''
Base definition of settings import
'''
# pytlint: disable=wildcard-import
# flake8: noqa
import os

if os.getenv('MODE') == 'production':
    from pegabus.settings.production import *  # pylint: disable=W0614,W0401
else:
    from pegabus.settings.development import *  # pylint: disable=W0614,W0401
