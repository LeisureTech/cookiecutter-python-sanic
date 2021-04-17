from setuptools import setup

__version__ = "{{cookiecutter.version}}"

setup(
    name="{{cookiecutter.package_name}}",
    version=__version__,
    description="{{cookiecutter.project_short_description}}",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    license="{{cookiecutter.open_source_license}}",
    python_requires=">=3.7",
)
