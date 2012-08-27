#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from dnsimple import dnsimple

setup(
    name='dnsimple-python',
    version=dnsimple.__version__,
    description=u' '.join(dnsimple.__doc__.splitlines()).strip(),
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
