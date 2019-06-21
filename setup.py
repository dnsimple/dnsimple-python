#!/usr/bin/env python

import os
from setuptools import setup, find_packages
import versioneer

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='dnsimple',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Python API client for Domain Management Automation with DNSimple https://developer.dnsimple.com',
    long_description=readme,
    long_description_content_type="text/markdown",
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['requests>=2.10.0,<3.0.0']
)
