"""
WSGI config for observability_workflows project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

# OLD CONFIG
# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'observability_workflows.settings')
# application = get_wsgi_application()

# Apache compatible config
import os
import sys
from django.core.wsgi import get_wsgi_application


path = '/var/www/html/observability_workflows/observability_workflows'

if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"]="observability_workflows.settings"

application = get_wsgi_application()