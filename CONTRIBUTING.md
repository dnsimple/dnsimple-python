# Contributing to DNSimple/Python

## Getting Started

#### 1. Clone the repository

Clone the repository and move into it:

```shell
git clone git@github.com:dnsimple/dnsimple-python.git
cd dnsimple-python
```

#### 2. Install dependencies

Make sure you have Python (7.3 onwards) installed.

Make sure you have the required libraries installed:

```shell
pip install -r requirements.txt
```

(Optional) Install pyenv using *Homebrew* (on macOS) or following the instructions in the [pyenv project](https://github.com/pyenv/pyenv).

#### 3. Testing

[Run the test suite](#testing) to check everything is working as expected and to install the project specific 
dependencies (the first time you'll run the script it will install all the dependencies for you).

To run the test suite: 

```shell
make test
```

## Releasing

The following instructions uses `$VERSION` as a placeholder, where `$VERSION` is a `MAJOR.MINOR.BUGFIX` release such as `1.2.0`.

1. Run the test suite and ensure all the tests pass.
2. Set the version in `version.py` (located in `./dnsimple/version.py`).
    ```python
version = '$VERSION'
    ```
3. Run the test suite and ensure all tests pass: `make test`
4. Finalize the `## master` section in `CHANGELOG.md` assigning the version.
5. Commit and push the changes
    ```shell
    git commit -a -m "Release $VERSION"
    git push origin master
    ```
6. Wait for the CI to complete.
7. Create a signed tag.
    ```shell
    git tag -a v$VERSION -s -m "Release $VERSION"
    git push origin --tags
    ```

## Generating distribution packages

Make sure you have the latest versions of setuptools and wheel installed:

```shell
python3 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:

```shell
python3 setup.py sdist bdist_wheel
```

## Uploading the distribution packages

You'll have to install twine:

```shell
python3 -m pip install --user --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:

```shell
python3 -m twine upload --repository testpypi dist/*
```

You can also check if your distribution is ready to be uploaded like so:

```shell
twine check dist/*
```

## Testing

Submit unit tests for your changes. You can test your changes on your machine by [running the test suite](#testing).

When you submit a PR, tests will also be run on the [continuous integration environment via Travis](https://travis-ci.com/dnsimple/dnsimple-python).
