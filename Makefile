VENV_PATH='your preferred environment path'

environment_setup:
	@echo "Setting up python environment"
	python -m venv $(VENV_PATH)
	. $(VENV_PATH)/bin/activate

library_setup: environment_setup
	@echo "Installing libraries"
	python -m pip install --upgrade pip
	pip install -r requirements.txt

run:
	@echo "Running MM user claims entry program"
	$(VENV_PATH)/bin/python claims.py