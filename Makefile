pip-install:
	pip install -r requirements.txt

pip-reset:
	pip freeze > pkgs-to-rm.txt
	pip uninstall -y -r pkgs-to-rm.txt
	rm pkgs-to-rm.txt
	pip install -r requirements.txt

run:
	source venv/bin/activate; export FLASK_APP=app; export FLASK_ENV=development; flask run

lint:
	flake8 *.py

test:
	python3 -m unittest discover -v
