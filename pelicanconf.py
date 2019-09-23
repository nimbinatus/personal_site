#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Laura Santamaria'
SITENAME = 'Accidental DevOpsAdv'
SITEURL = ''
SITESRC = 'https://github.com/nimbinatus/nimbinatus.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Biography
BIO = "Developer Advocate @LogDNA. Pythonista. DevOps Advocate."
PROFILE_IMAGE = 'avatar.png'

# Social widget
SOCIAL = (
    ('email', 'laura@nimbinatus.com'),
    ('linkedin', 'https://www.linkedin.com/in/lauraasantamaria'),
    ('twitter', 'https://twitter.com/nimbinatus'),
    ('github', 'https://github.com/nimbinatus')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Theme
THEME = 'theme/pelican-themes/twitchy'

# Plugins
# PLUGIN_PATHS = [ 'plugins' ]
# PLUGINS = ['assets']

# static files
STATIC_PATHS = [
    'favicon.ico'
]
