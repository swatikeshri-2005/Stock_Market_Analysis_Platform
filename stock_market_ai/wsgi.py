"""
WSGI config for stock_market_ai project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_market_ai.settings')

application = get_wsgi_application()
