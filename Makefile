install_requirements:
	poetry install

test: install_requirements
	poetry run python -m unittest discover -p "*_test.py" -v

clean_package:
	rm -rf dist/*

package:
	poetry build

test_upload_package: clean_package package
	poetry publish --repository testpypi
