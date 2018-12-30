run:
	source venv/bin/activate; export FLASK_APP=app; export FLASK_ENV=development; flask run

lint:
	flake8 *.py

test:
	python3 -m unittest discover -v
