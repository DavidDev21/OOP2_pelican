#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Z'
SITENAME = u'OOP2_pelican'
SITEURL = ''

PATH = 'content'
THEME="themes/OOP2_theme"
TIMEZONE = 'UTC'

OUTPUT_PATH='docs'

# Enforce article ordering
ARTICLE_ORDER_BY = 'article_num'

DEFAULT_LANG = u'en'

# Static_path starts from the "content" folder
# This is to tell pelican where the static content folder is and dont do processing on it
# Adds straight to the root of the site or the path relative to the root given by 'path'
STATIC_PATHS= ['extra']
# path: I am assuming this is where the file would go in the output dir
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True