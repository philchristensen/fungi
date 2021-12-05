# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

# disables creation of .DS_Store files inside tarballs on Mac OS X
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

setup(
    name='fungi',
    version='0.1.0',
    url='https://github.com/philchristensen/pyfungi',
    author='Phil Christensen',
    author_email='phil@bubblehouse.org',
    packages=find_packages(),
    install_requires=[
        "click",
        "tabulate"
    ],
    entry_points='''
        [console_scripts]
        fungi=fungi.core:cli
    '''
)
