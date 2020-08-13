# Contributing to DNSimple/Python

## Getting Started

#### 1. Clone the repository

Clone the repository and move into it:

```shell
git clone git@github.com:dnsimple/dnsimple-python.git
cd dnsimple-python
```

#### 2. Install dependencies

Make sure you have Python (3.8 onwards) installed.

Init the project

```shell
make init
```

This will install a virtual python environment `venv`. Once you have run the command
you can start using the virtual environment like so:

```shell
source ./venv/bin/activate
```

#### 3. Testing

[Run the test suite](#testing) to check everything is working as expected and to install the project specific
dependencies (the first time you'll run the script all the dependencies will be installed for you).

To run the test suite:

```shell
make test
```

## Releasing

The following instructions uses `$VERSION` as a placeholder, where `$VERSION` is a `MAJOR.MINOR.BUGFIX` release such as `1.2.0`.

1. Set the version in `./dnsimple/version.py`.

    ```python
    version = '$VERSION'
    ```

2. Run the test suite and ensure all tests pass: `make test`

3. Finalize the `## master` section in `CHANGELOG.md` assigning the version.

4. Commit and push the changes

    ```shell
    git commit -a -m "Release $VERSION"
    git push origin master
    ```

5. Wait for CI to complete.

6. Create a signed tag.

    ```shell
    git tag -a v$VERSION -s -m "Release $VERSION"
    git push origin --tags
    ```

## Generating distribution packages

```shell
make package
```

You can also check if your distribution is ready to be uploaded like so:

```shell
make test_package
```

## Uploading the distribution packages (to testpypi)

Run

```shell
make upload_package
```

and follow the instructions. This will upload the package to the testpypi environment.


## Testing

Submit unit tests for your changes. You can test your changes on your machine by [running the test suite](#testing).

When you submit a PR, tests will also be run on the [continuous integration environment via Travis](https://travis-ci.com/dnsimple/dnsimple-python).
