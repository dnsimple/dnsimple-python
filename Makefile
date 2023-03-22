install_requirements: init
	poetry install

test: install_requirements
	poetry run python -m unittest discover -p "*_test.py" -v

update_install_setuptools: install_requirements
	poetry run python -m pip install --upgrade setuptools wheel

clean_package:
	rm -rf dist/*

package: update_install_setuptools
	poetry run python setup.py sdist bdist_wheel

test_package: package update_install_twine
	poetry run twine check dist/*

update_install_twine:
	poetry run python -m pip install --upgrade twine

test_upload_package: update_install_twine clean_package package
	poetry run python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload_package: update_install_twine clean_package package
	poetry run python -m twine upload dist/*
