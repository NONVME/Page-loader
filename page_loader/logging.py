import logging.config
import os

BASE_LOG_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.logs')
FILE_NAME = os.path.join(BASE_LOG_DIR, f'{__name__}.log')
FORMAT = '%(asctime)s:[%(module)s:%(lineno)s] %(levelname)s %(message)s'
LOG_LEVEL = 'INFO'

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stderr'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': FILE_NAME,
            'maxBytes': 1048576,
            'backupCount': 3
        }
    },

    'loggers': {
        'base_file': {
            'handlers': ['file'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        'base_console': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
        'page_loader.engine': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': False
        }
    }
}


if not os.path.exists(BASE_LOG_DIR):
    os.mkdir(BASE_LOG_DIR)
logging.config.dictConfig(LOGGING_CONFIG)
