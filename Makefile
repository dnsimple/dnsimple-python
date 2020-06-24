init:
	pip install -r requirements.txt

test:
	python -m unittest discover -p "*_test.py" -v
