import os

from src.config.common import *

APP_ENV = os.getenv('APP_ENV', 'dev')

if APP_ENV == 'dev':
    from src.config.dev import *
