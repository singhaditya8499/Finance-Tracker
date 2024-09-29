# Makefile for Flask application

# Variables
VENV_PATH = venv
PYTHON = $(VENV_PATH)/bin/python
venv_creation=python3 -m venv venv
PIP = $(VENV_PATH)/bin/pip

activate_venv = . $(VENV_PATH)/bin/activate &&

.PHONY: install
install:
install:
	$(venv_creation)
	$(activate_venv) $(PIP) install -r requirements.txt

.PHONY: makevenv
makevenv:
makevenv:
	$(venv_creation)
	$(activate_venv) pip install --upgrade pip
	$(DONE)

.PHONY: run
run:
run:
	$(activate_venv) $(PYTHON) app.py

.PHONY: install-run
install-run:
install-run:
	$(activate_venv) $(PIP) install -r requirements.txt
	$(PYTHON) app.py

.PHONY: clean
clean:
clean:
	rm -rf $(VENV_PATH)