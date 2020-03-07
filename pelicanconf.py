#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


from minchin.pelican.themes import minchindotca

THEME = minchindotca.get_path()
BOOTSTRAP_THEME = 'minchindotca'

IMAGE_PROCESS = {
  'article-feature': ["scale_in 848 848 True"],
  'index-feature': ["scale_in 263 263 True"],
}

# Jijna2 filters
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)


def article_date(value):
    """Converts a date to the format we want it displayed on the article
       template.
    """
    return value.strftime('%A, %B %-d, %Y')


def breaking_spaces(value):
    """Converts non-breaking spaces to regular spaces."""
    return value.replace('\u00A0', ' ')


JINJA_FILTERS = {
  'datetimefilter': datetimefilter,
  'article_date':   article_date,
  'breaking_spaces': breaking_spaces,
}


AUTHOR = 'Real Alchemist'
SITENAME = 'Real Alchemy'
SITEURL = 'srisivac.realalchemu.in/blog'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
