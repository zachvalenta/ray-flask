help:
	@echo
	@echo "lint:   lint using flake8"
	@echo "pipfr:  freeze dependencies into requirements.txt"
	@echo "pipin:  install dependencies from requirements.txt"
	@echo "piprs:  remove any installed pkg *not* in requirements.txt"
	@echo "rf:     run Flask"
	@echo "rg:     run gunicorn"
	@echo "test:   exec unit tests"
	@echo

lint:
	flake8 *.py

pipfr:
	pip freeze > requirements.txt

pipin:
	pip install -r requirements.txt

piprs:
	pip freeze > pkgs-to-rm.txt
	pip uninstall -y -r pkgs-to-rm.txt
	rm pkgs-to-rm.txt
	pip install -r requirements.txt

rf:
	source venv/bin/activate; export FLASK_APP=app; export FLASK_ENV=development; flask run

rg:
	gunicorn app:app

test:
	python3 -m unittest discover -v
