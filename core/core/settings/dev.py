from core.settings.base import *


DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
]
# Override base.py settings here

try:
    from core.settings.local import *
except:
    pass