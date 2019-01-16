help:
	@echo "lint:    lint using flake8"
	@echo "pip-in:  install dependencies from requirements.txt"
	@echo "pip-rs:  remove any installed pkg *not* in requirements.txt"
	@echo "runf:   run Flask"
	@echo "rung:   run gunicorn"
	@echo "test:    exec unit tests"

lint:
	flake8 *.py

pip-in:
	pip install -r requirements.txt

pip-rs:
	pip freeze > pkgs-to-rm.txt
	pip uninstall -y -r pkgs-to-rm.txt
	rm pkgs-to-rm.txt
	pip install -r requirements.txt

runf:
	source venv/bin/activate; export FLASK_APP=app; export FLASK_ENV=development; flask run

rung:
	gunicorn app:app

test:
	python3 -m unittest discover -v
