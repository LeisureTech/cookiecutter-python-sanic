# Cookiecutter Python Sanic

Cookiecutter python Sanic is a framework that is used for rapid development in
microservice infrastructure. It adopts many state-of-art technologies including
but not limited to:
- Pre-commit for code style formatting by Black and Linter by flake8.
- Building docker images and using docker containers for local development.
- Semantic version release.
- Alembic for db migration.
- Automatic PyTest in CI/CD.

---
### Why Sanic?

Sanic is web server framework that supports HTTP 2.0 which supports asynchrous
communication between services.

----
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

Now it's time to initialize your project, you just need to do.

```bash
# Create your repository
mkdir /your-repository
cookiecutter https://github.com/LeisureTech/python-project-generator
```
Following the steps and setting up a few template tags,
you will get your project instantly!

---
## Versioning
We suggest to use `python-semantic-release` to do semantic release.
```bash
pip install python-semantic-release
```
To release a new version,
```bash
semantic-release publish --minor/--patch/--major # bump version
```
