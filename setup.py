#!/usr/bin/env python

import os
from setuptools import setup, find_packages

setup(
    name='dnsimple-python',
    version=__import__('dnsimple').__version__,
    description=u' '.join(
        __import__('dnsimple').__doc__.splitlines()).strip(),
    long_description=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'README.markdown'),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/ixc/dnsimple-python/',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
