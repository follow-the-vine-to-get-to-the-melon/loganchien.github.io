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

# URL configuration
INDEX_SAVE_AS = 'blog/index.html'  # Move article index page

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'category/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tag/index.html'

AUTHORS_SAVE_AS = 'authors/index.html'

# Menu item
MENUITEMS = (('home', '/'),
             ('blog', '/blog'),)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Theme
THEME = 'pelican-octopress-theme'

# Static URL
STATIC_PATHS = ['static/certs', 'static/images']
