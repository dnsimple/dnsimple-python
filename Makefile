.DEFAULT_GOAL := setup

ci:
	py.test tests

test: setup
	./env/bin/py.test tests

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || virtualenv env;	\
	./env/bin/pip install -r requirements.txt --upgrade;

dnsimple.egg-info/SOURCES.txt: env
	./env/bin/python setup.py develop

setup: dnsimple.egg-info/SOURCES.txt

deploy:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

.PHONY: test
