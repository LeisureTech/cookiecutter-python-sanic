# Python Project Generator

A simple project template for a micro service. Based on Sanic framework.

Use alembic for dbmigration.

Dockerized project.

- Cookiecutter documentation: https://cookiecutter.readthedocs.io

## Get Started

Generating your startup Sanic project is fairly simple. You are only a few
commands away.
But before you do that, you need to have `cookiecutter`installed.

For Homebrew, you can do:
```bash
brew install cookiecutter
```
Alternative installations can be found here:
https://cookiecutter.readthedocs.io/en/1.7.2/installation.html

To make sure you have the dependency, you can do:
```bash
cookiecutter -V # Cookiecutter 1.7.2
```

Now it's time to initialize your project, you just need to do.

```bash
# Create your repository
mkdir /your-repository
# Create project from the template
cookiecutter https://github.com/LeisureTech/python-project-generator
# For the sake of brevity, repos on GitHub can just use the 'gh' prefix
cookiecutter gh:LeisureTech/python-project-generator
```
Following the steps and setting up a few template tags,
you will get your project instantly!

---
## Versioning
We use `python-semantic-release` to do semantic version release.
```bash
pip install python-semantic-release
```
