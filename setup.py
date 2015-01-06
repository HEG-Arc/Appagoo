#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import appagoo
version = appagoo.__version__

setup(
    name='Appagoo',
    version=version,
    author='',
    author_email='alessio.desanto@he-arc.ch',
    packages=[
        'appagoo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['appagoo/manage.py'],
)