#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

setup(
    name="minc2.simple",
    version="0.1",
    description="MINC2 Simple interface using CFFI",
    long_description=open("README.md", "rt").read(),
    url="https://github.com/vfonov/minc2-simple",
    author="Vladimir S. FONOV",
    author_email="vladimir.fonov@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages(),
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=[
        "./minc2/build_minc2-simple.py:ffi",
    ],
)