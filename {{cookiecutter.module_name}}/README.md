# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

----
## Table of contents
- [Introduction]()
- [Get Started](#getstarted)
- [Init Git](#git)
- [How to run the project](#run)
- [Useful Commands](#commands)

----
## Introduction <a name="introduction"></a>
// TODO: To fill in

## Get Started <a name="getstarted"></a>

Before you can run this project, you need to have python installed.
You can use [pyenv](https://github.com/pyenv/pyenv) to create a virtual environment.

### Python >= 3.7:
Consider installing with [Homebrew](https://docs.brew.sh/):
```bash
brew update
# install pyenv by Homebrew
brew install pyenv
# confirm installation
pyenv --version  # pyenv 1.2.26
# create a python virtual env
pyenv virtualenv 3.8.9 python-starter-3.8.9
# activate the virtual env
pyenv activate python-starter-3.8.9
```

### Alembic for db migration
```bash
pip install alembic
# auto generate migration file
# run db migration
```

### Pre-commit
This project adopts pre-commit framework to maintain code readability and consistency.
Before you run hooks, you need to have pre-commit package manager installed.

```bash
pip install pre-commit
```


----
## Init Git <a name="git"></a>
Please install pre-commit git hook scripts so that it will run automatically on every commit.

```bash
pre-commit bash
```

----
### How to run the project <a name="run"></a>
Docker:
```bash
docker build -p
```

----
### Dev commands  <a name="commands"></a>

Automatically create requirements
```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

To run pre-commit against all files
```bash
pre-commit run --all-files
```
