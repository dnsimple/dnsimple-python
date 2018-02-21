setup:
	test -d env || virtualenv env
	./env/bin/pip install -r requirements.txt --upgrade
	./env/bin/python setup.py develop

test: setup
	test -f tests/.env || { echo "Set up your env file before running tests"; exit 1; }
	./env/bin/py.test tests

ci-setup:
	pip install -r requirements.txt --upgrade

ci-test:
	py.test tests

deploy:
	rm dist/*
	python setup.py sdist
	twine upload dist/*

.PHONY: test
