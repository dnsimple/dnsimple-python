#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from dnsimple import dnsimple

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.markdown'), 'r') as readme_file:
    readme = readme_file.read()

setup(
    name='dnsimple',
    version=dnsimple.__version__,
    description=u' '.join(dnsimple.__doc__.splitlines()).strip(),
    long_description=readme,
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
