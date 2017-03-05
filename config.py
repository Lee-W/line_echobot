import os
import sys


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Error occurs when setting env variable "{}"'.format(var_name)
        print(error_msg)
        sys.exit(1)


try:
    from config_secret import *
except ImportError:
    LINE_CHANNEL_ACCESS_TOKEN = get_env_variable('LINE_CHANNEL_ACCESS_TOKEN')
    LINE_CHANNEL_SECRET = get_env_variable('LINE_CHANNEL_SECRET')


MUST_HAVE_SETUPS = [
    'LINE_CHANNEL_ACCESS_TOKEN',
    'LINE_CHANNEL_SECRET'
]

for key in MUST_HAVE_SETUPS:
    if key not in globals():
        print('{key} must be set'.format(key=key))
        sys.exit(1)
