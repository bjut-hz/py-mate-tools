# -*- coding: utf-8 -*-
__author__ = 'hz'

from setuptools import setup, find_packages
import os

def walkdir(dirname):
    rec_files=[]
    for cur, _dirs, files in os.walk(dirname):
    	rec_files+=[(cur,map(lambda f: os.path.join(cur,f),files))]
    #print rec_files
    return rec_files

setup(
    name = "py-mate-tools",
    version = "1.0",
    author = "何震震",
    maintainer = "何震震",
    author_email = "936432896@qq.com",
    url = "https://github.com/bjut-hz/py-mate-tools",
    license = "Apache License, Version 2.0",
    keywords = ['SRL', 'semantic role labeling', 'NLP', 'natural language processing',
                'mate-tools', 'Tools for Natural Language Analysis'],
    description = "Python interface for mata tools written by Java",
    packages = ['py-mate-tools'],
    # ['*'] will cause bug when use --python setup.py bdist_egg command-- but  ['py-mate-tools/*'] not
    package_data = {'py-mate-tools' : ['py-mate-tools/*'] },
    install_requires = ['nltk>=3'],
    data_files = walkdir( 'py-mate-tools' ),
    classifiers = ['Programming Language :: Python :: 2.7']
)