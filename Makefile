.PHONY: test

help:
	@echo
	@echo "🍶  FLASK"
	@echo
	@echo "flask:     	run dev server"
	@echo "guni:     	run gunicorn"
	@echo "reset:     	drop db and recreate blank"
	@echo
	@echo "🛠  TOOLING"
	@echo
	@echo "fmt:     	auto format code using Black"
	@echo "lint:    	lint using flake8"
	@echo "repl:    	debug using bpython"
	@echo "secure:  	security check using Bandit"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "freeze:   	freeze dependencies into requirements.txt"
	@echo "install:   	install dependencies from requirements.txt"
	@echo "purge:   	remove any installed pkg *not* in requirements.txt"
	@echo

guni:
	gunicorn app:app

flask:
	source venv/bin/activate; flask run

reset:
	qing local.db; touch local.db

fmt:
	black app.py test_app.py

lint:
	flake8 *.py

repl:
	bpython

test:
	python3 -m pytest -v

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

purge:
	@echo "🔍 - DISCOVERING UNSAVED PACKAGES\n"
	pip freeze > pkgs-to-rm.txt
	@echo
	@echo "📦 - UNINSTALL ALL PACKAGES\n"
	pip uninstall -y -r pkgs-to-rm.txt
	@echo
	@echo "♻️  - REINSTALL SAVED PACKAGES\n"
	pip install -r requirements.txt
	@echo
	@echo "🗑  - UNSAVED PACKAGES REMOVED\n"
	diff pkgs-to-rm.txt requirements.txt | grep '<'
	@echo
	rm pkgs-to-rm.txt
	@echo

