# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Blockchain supported digital voting system, for final,'
    'year project (for BSc Computer & Information Security, Plymouth,'
    'University, 2017)',
    'author': 'Jack Tolley',
    'url': 'https://github.com/BadgerJack/verbose-octo-goggles',
    'download_url': 'Where to download it.',
    'author_email': 'jbadgerington@gmail.com',
    'version': '0.1',
    'install_requires': ['nose','paste'],
    'packages': ['heimdallr'],
    'scripts': [],
    'name': 'Project Heimdallr'
}

setup(**config)
