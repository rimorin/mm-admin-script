VENV_PATH='your preferred environment path'

environment_setup:
	@echo "Setting up python environment"
	python -m venv $(VENV_PATH)
	. $(VENV_PATH)/bin/activate

library_setup: environment_setup
	@echo "Installing libraries"
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Update user access lvl
manage_claims:
	@echo "Running MM user claims entry program"
	$(VENV_PATH)/bin/python claims.py

# Update user password
manage_pass:
	@echo "Running MM user password program"
	$(VENV_PATH)/bin/python password.py

# Create new user
create_user:
	@echo "Running MM user creation program"
	$(VENV_PATH)/bin/python create.py

# delete user
delete_user:
	@echo "Running MM user deletion program"
	$(VENV_PATH)/bin/python delete.py