#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# -*- mode: python -*-
from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
from numpy.distutils.core import setup, Extension
import os,sys

setup(
    name = 'dlab',
    version = "1.0.0",  
    packages= find_packages(exclude=["*test*"]),
    ext_package = 'dlab',
    ext_modules = [Extension('convolve',sources=['src/convolve.pyf','src/convolve.c'])],
    
    scripts = ['scripts/compress_toelis.py','scripts/merge_cells.py'],

    install_requires = ["numpy>=1.3", "tables>=2.1", "arf>=1.0",
                        "matplotlib>=0.99","scipy>=0.7"],

    description = "A python package with various functions I use frequently",
    
    author = "CD Meliza",
    maintainer = "CD Meliza",
    maintainer_email = "dmeliza@uchicago.edu",
)


# Variables:
# End: