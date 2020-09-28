init:
	python3 -m venv ./venv

install_requirements: init
	pip install -r requirements.txt

test: install_requirements
	python -m unittest discover -p "*_test.py" -v

update_install_setuptools:
	python -m pip install --upgrade setuptools wheel

clean_package:
	rm -rf dist/*

package: update_install_setuptools
	python setup.py sdist bdist_wheel

test_package: package update_install_twine
	twine check dist/*

update_install_twine:
	python -m pip install --upgrade twine

upload_package: update_install_twine clean_package package
	python -m twine upload dist/*
