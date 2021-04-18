import sys
import re


def is_valid_module_name(module_name):
    module_regex = r"^[a-z][_a-z0-9]+$"
    return re.match(module_regex, module_name) is not None


def is_valid_package_name(package_name):
    package_regex = r"^[a-z][-a-z0-9]+$"
    return re.match(package_regex, package_name) is not None


if not is_valid_module_name("{{ cookiecutter.project_slug }}"):
    print(
        """ERROR: The project module name ({{ cookiecutter.project_slug }}) is
        not a valid Python module name.
        Please use a short, all-lowercase name. Underscores (_) can be
        used in the module name if it improves readability."""
    )

    # Exit to cancel project
    sys.exit(1)

if not is_valid_package_name("{{ cookiecutter.package_name }}"):
    print(
        """ERROR: The project package name ({{ cookiecutter.package_name }})
        is not valid Python package.
        Please use a short, all-lowercase name. Dashes (-) can be used
        in the module name if it improves readability. """
    )

    # Exit to cancel project
    sys.exit(1)
