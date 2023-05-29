"""
WSGI config for inventrol project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
#from dj_static import Cling

path = '/home/zamenis/inventrol'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'inventrol.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


