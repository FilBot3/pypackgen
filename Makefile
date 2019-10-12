init:
	python -m pip install --upgrade pip
	python -m pip install -r python-3-requirements.txt

install:
	python setup.py install

develop:
	python setup.py develop

test:
	python setup.py pytest