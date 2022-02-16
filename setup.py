# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from dnsimple.version import version

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="dnsimple",
    version=version,
    description="DNSimple API service for python",
    long_description_content_type="text/markdown",
    long_description=readme,
    author="Enrique Comba Riepenhausen",
    author_email="enrique@ecomba.pro",
    url="https://github.com/dnsimple/dnsimple-python",
    license="MIT",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    install_requires=["requests", "omitempty"],
    python_requires='>=3.8'
)
