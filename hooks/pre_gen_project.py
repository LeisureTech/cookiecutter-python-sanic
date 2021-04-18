import sys

from hooks.template_tag_validation import (
    is_valid_module_name,
    is_valid_package_name,
)


if not is_valid_module_name("{{ cookiecutter.project_slug }}"):
    print(
        """ERROR: The project module name ({{ cookiecutter.project_slug }}) is
        not a valid Python module name.
        Please use a short, all-lowercase name. Underscores (_) can be
        used in the module name if it improves readability."""
    )

    # Exit to cancel project
    sys.exit(1)

if not is_valid_package_name("{{ cookiecutter.package-name }}"):
    print(
        """ERROR: The project package name ({{ cookiecutter.package-name }})
        is not valid Python package.
        Please use a short, all-lowercase name. Dashes (-) can be used
        in the module name if it improves readability. """
    )

    # Exit to cancel project
    sys.exit(1)
