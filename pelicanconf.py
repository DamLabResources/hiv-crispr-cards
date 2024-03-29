#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from utils import pelican_yaml_reader

AUTHOR = 'Will Dampier'
SITENAME = 'HIV CRISPR Cards'
SITEURL = 'https://damlabresources.github.io/hiv-crispr-cards/'
THEME_STATIC_DIR = 'theme'
CSS_FILE = 'main.css'
AUTORELOAD_IGNORE_CACHE = True

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
RELATIVE_URLS = True

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

#TEMPLATE_PAGES = {'guide.html': 'docs/theme/templates/guide.html',
#                  }

PLUGINS = [pelican_yaml_reader]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True