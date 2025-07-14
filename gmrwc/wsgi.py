#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gmrwc.settings')

application = get_wsgi_application()

