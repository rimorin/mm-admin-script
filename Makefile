include .env
export

environment_setup:
	@echo "Setting up python environment"
	python -m venv $(VENV_PATH)
	. $(VENV_PATH)/bin/activate

library_setup: environment_setup
	@echo "Installing libraries"
	python -m pip install --upgrade pip
	pip install -r requirements.txt

format_code:
	@echo "Formatting python files"
	black .

# Update user access lvl
manage_claims:
	@echo "Running MM user claims entry program"
	$(VENV_PATH)/bin/python user/claims.py

# Update user details
manage_details:
	@echo "Running MM user details program"
	$(VENV_PATH)/bin/python user/details.py

# Update user password
manage_pass:
	@echo "Running MM user password program"
	$(VENV_PATH)/bin/python user/password.py

# Create new user
create_user:
	@echo "Running MM user creation program"
	$(VENV_PATH)/bin/python user/create.py

# delete user
delete_user:
	@echo "Running MM user deletion program"
	$(VENV_PATH)/bin/python user/delete.py

# manage congregation
create_congregation:
	@echo "Running MM cong creation program"
	$(VENV_PATH)/bin/python congregation/create.py

update_congregation:
	@echo "Running MM cong modification program"
	$(VENV_PATH)/bin/python congregation/update.py