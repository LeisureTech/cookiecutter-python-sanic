# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}


###

Create a new virtual env
```bash
pyenv virtualenv 3.8.9 python-starter-3.8.9
```

Activate env
```bash
pyenv activate python-starter-3.8.9
```

Automatically create requirements
```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```
