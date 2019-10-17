setup:
	python -m pip install --upgrade pip
	python -m pip install -r python-3-requirements.txt

venv:
	# Once this has been completed, it can be sourced and then development can
	# happen out of this repository.
	python -m venv venv/pypackgen

install:
	python setup.py install

develop:
	python setup.py develop

test:
	python setup.py pytest
