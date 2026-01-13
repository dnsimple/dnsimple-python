# Contributing to DNSimple/Python

## Getting Started

Clone the repository and move into it:

```shell
git clone git@github.com:dnsimple/dnsimple-python.git
cd dnsimple-python
```

[Poetry](https://python-poetry.org/) is used by this library, so ensure you have it installed.

Make sure you have Python installed.

Init the project

```shell
poetry install
```

To start a shell in the virtual environment:

```shell
poetry shell
```

## Testing

Submit unit tests for your changes. You can test your changes on your machine by running the test suite.

To run the test suite:

```shell
make test
```

When you submit a PR, tests will also be run on the [continuous integration environment via GitHub Actions](https://github.com/dnsimple/dnsimple-python/actions).

## Changelog

We follow the [Common Changelog](https://common-changelog.org/) format for changelog entries.
