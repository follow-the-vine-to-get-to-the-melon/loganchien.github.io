#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Logan'
SITENAME = u"Logan's Thought"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

LOCALE = ('en_US.utf-8',)

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Web', 'http://logan.tw'),
         ('Blog (Taiwan)', 'http://blog.logan.tw'),)

# Social widget
SOCIAL = (('facebook', 'http://facebook.com/loganchien'),
          ('google+', 'http://plus.google.com/+LoganChienTW'),
          ('github', 'http://github.com/loganchien'),
          ('linkedin', 'https://www.linkedin.com/in/loganchien'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Change homepage
INDEX_SAVE_AS = 'blog.html'

# Menu Item
MENUITEMS = (('home', '/'),
             ('blog', '/blog.html'),)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Theme
THEME = 'pelican-octopress-theme'

# Static URL
STATIC_PATHS = ['static/certs', 'static/images']
