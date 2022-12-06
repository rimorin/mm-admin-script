# ministry-mapper-admin
MM Admin tool for user access control

## How to use

To run this project locally,

1. [Retrieve Firebase service account key](https://firebase.google.com/docs/admin/setup).

2. Setup python 3 environment using Make. 

```sh
make VENV_PATH=preferred_python_env_path library-setup
```

3. Run management program depending on your needs
```sh
make VENV_PATH=preferred_python_env_path manage_claims
make VENV_PATH=preferred_python_env_path manage_pass
make VENV_PATH=preferred_python_env_path create_user
make VENV_PATH=preferred_python_env_path delete_user
```
