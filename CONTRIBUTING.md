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

## Releasing

The following instructions uses `$VERSION` as a placeholder, where `$VERSION` is a `MAJOR.MINOR.BUGFIX` release such as `1.2.0`.

1. Set the version in `./dnsimple/version.py` and `pyproject.toml`.

    ```python
    version = "$VERSION"
    ```

2. Run the test suite and ensure all tests pass: `make test`

3. Finalize the `## main` section in `CHANGELOG.md` assigning the version.

4. Commit and push the changes

    ```shell
    git commit -s -a -m "Release $VERSION"
    git push origin main
    ```

5. Wait for CI to complete.

6. Create a signed tag.

    ```shell
    git tag -a v$VERSION -s -m "Release $VERSION"
    git push origin --tags
    ```

## Testing

Submit unit tests for your changes. You can test your changes on your machine by [running the test suite](#testing).

When you submit a PR, tests will also be run on the [continuous integration environment via Travis](https://travis-ci.com/dnsimple/dnsimple-python).
