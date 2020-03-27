import os
import logging.config
from mint_firebase.mint_fetch import firebase_init
from mint_firebase.mint_fetch import get_config_data

config_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.yaml')

mint_fetch_config = get_config_data(config_filename)
firebase_config_file = mint_fetch_config["firebase"]["credentials"]

firebase_config_file_real = os.path.join(os.path.dirname(os.path.realpath(__file__)), firebase_config_file)

firebase_init(firebase_config_file_real)

# Disable Django's logging setup
LOGGING_CONFIG = None

LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        # console logs to stderr
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        # default for all undefined Python modules
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'root': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        'mint_fetch': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            # Avoid double logging because of root logger
            'propagate': False,
        },

        # Our application code
        'openapi_server': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            # Avoid double logging because of root logger
            'propagate': False,
        },
        # Prevent noisy modules from logging to Sentry
        'noisy_module': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
})
logger = logging.getLogger(__name__)