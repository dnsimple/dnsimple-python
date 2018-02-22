VERSION := $(shell python setup.py --version)

setup:
	test -e env || virtualenv env
	./env/bin/pip install -r requirements.txt --upgrade
	./env/bin/python setup.py develop

test: setup
	test -f tests/.env || { echo "Set up your env file before running tests"; exit 1; }
	./env/bin/py.test tests

ci-setup:
	pip install -r requirements.txt --upgrade

ci-test:
	py.test tests

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
