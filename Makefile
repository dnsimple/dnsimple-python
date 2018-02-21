.DEFAULT_GOAL := setup

test: setup
	test -f tests/.env || { echo "Set up your env file before running tests"; exit 1; }
	./env/bin/py.test tests

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || virtualenv env;	\
	./env/bin/pip install -r requirements.txt --upgrade;

dnsimple.egg-info/SOURCES.txt: env
	./env/bin/python setup.py develop

setup: dnsimple.egg-info/SOURCES.txt

ci: test
	py.test tests

deploy:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*
