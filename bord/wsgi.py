"""WSGI config for BORD."""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bord.settings")

application = get_wsgi_application()
