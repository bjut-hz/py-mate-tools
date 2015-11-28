# -*- coding: utf-8 -*-
__author__ = 'hz'

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
files = ["PyMateTools/*"]
import os
def walkdir(dirname):
    rec_files=[]
    for cur, _dirs, files in os.walk(dirname):
        rec_files+=[(cur,map(lambda f: os.path.join(cur,f),files))]
    #print rec_files
    return rec_files

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup(name = "PyMateTools",
    version = "1.0",
    description = "Python interface for mate-tools written by Java.",
    author = "何震震",
    maintainer = "何震震",
    author_email = "936432896@qq.com",
    url = "https://github.com/bjut-hz/py-mate-tools",
    license = "Apache License, Version 2.0",
    install_requires = ['nltk>=3'],
    classifiers = ['Programming Language :: Python :: 2.7'],
    keywords = ['SRL', 'semantic role labeling', 'NLP', 'natural language processing',
                'mate-tools', 'Tools for Natural Language Analysis'],
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['PyMateTools'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'PyMateTools' : files },
    #'runner' is in the root.
    #scripts = ["runner.py"],
    long_description = """Practical Natural Language Processing for Humans.""",
    data_files = walkdir('PyMateTools'),
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []    
)