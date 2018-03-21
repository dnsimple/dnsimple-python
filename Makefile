VERSION := $(shell python setup.py --version)

test: setup
	tox

ci-setup:
	pip install -r requirements.txt --upgrade

ci-test:
	pytest tests

venv:
	test -e env || python3 -m venv env
	./env/bin/pip install --upgrade tox
	./env/bin/pip install -r requirements.txt --upgrade
	./env/bin/python setup.py develop

setup: venv
	pyenv install --skip-existing 2.7.14
	pyenv install --skip-existing 3.6.4
	pyenv local 3.6.4 2.7.14
	pip install --upgrade tox tox-pyenv

deploy: setup
	git diff-index --quiet HEAD -- || git stash
	git checkout master
	git pull origin master
	git pull origin master --tags
	gem install github_changelog_generator
	github_changelog_generator --future-release=$(VERSION)
	git add CHANGELOG.md
	git commit -m "Deploy Version $(VERSION)"
	git tag $(VERSION)
	git push
	git push --tags
	rm dist/*
	./env/bin/python setup.py sdist
	gpg --detach-sign -a dist/dnsimple-$(VERSION).tar.gz
	./env/bin/pip install twine --upgrade
	./env/bin/twine upload dist/*

.PHONY: test
