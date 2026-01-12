# Contributing to DNSimple/Python

## Getting Started

### 1. Clone the repository

Clone the repository and move into it:

```shell
git clone git@github.com:dnsimple/dnsimple-python.git
cd dnsimple-python
```

### 2. Install dependencies

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

### 3. Testing

[Run the test suite](#testing) to check everything is working as expected and to install the project specific
dependencies (the first time you'll run the script all the dependencies will be installed for you).

To run the test suite:

```shell
make test
```

## Testing

Submit unit tests for your changes. You can test your changes on your machine by [running the test suite](#testing).

When you submit a PR, tests will also be run on the [continuous integration environment via GitHub Actions](https://github.com/dnsimple/dnsimple-python/actions).
