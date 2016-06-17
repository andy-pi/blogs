#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#### SYSTEM FIXED SETTINGS####
LOAD_CONTENT_CACHE = False
# This sets the location of the pages - creating clean urls
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
AUTHOR_SAVE_AS = ''
# Puts the blog articles into reverse order, most recent first - default for blogs
REVERSE_ARTICLE_ORDER = True

# Enable pages in the menu
# Set clean urls for pages as well
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

DELETE_OUTPUT_DIRECTORY = False

# DISABLE ALL FEEDS
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#### USER DEFINED SETTINGS ####

#SITELOGO_SIZE=

AUTHOR = "Andy"
SITENAME = "AndyPi"
SITETITLE = SITENAME
TIMEZONE = 'Europe/London'
DEFAULT_PAGINATION = 100
LINKS = [('English', 'http://andypi.co.uk'),('github', 'https://github.com/andy-pi')]
DISQUS_SITENAME = 'andypi'
SITESUBTITLE = 'Raspberry Pi and Python'
SITELOGO = ''
FAVICON = ''
BANNER= ''

DIRECT_TEMPLATES = (('index', 'tags', 'archives')) #'categories',
PAGINATED_DIRECT_TEMPLATES = (('index'))
RELATIVE_URLS = True
THEME = 'themes/pelican-bootstrap3'
#OUTPUT_PATH='example-themes/tuxlite_tbs'
