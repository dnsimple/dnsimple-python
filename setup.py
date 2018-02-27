#!/usr/bin/env python

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='dnsimple',
    version='1.0.2',
    description='Python API client for Domain Management Automation with DNSimple https://developer.dnsimple.com',
    long_description=readme,
    maintainer='David Aronsohn',
    maintainer_email='WagThatTail@Me.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/onlyhavecans/dnsimple-python/',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['requests>=2.10.0,<=2.18.4']
)
