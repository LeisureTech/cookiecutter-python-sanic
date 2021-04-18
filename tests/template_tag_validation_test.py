import pytest

from hooks.template_tag_validation import (
    is_valid_module_name,
    is_valid_package_name,
)


project_slug_test_date = [
    ("lowercase", True),
    ("lower_with_underscores", True),
    ("lower_with_number_123", True),
    ("CAPITAL", False),
    ("lower-with-dashes", False),
    ("_start_with_underscore", False),
]


@pytest.mark.parametrize("project_slug, expected", project_slug_test_date)
def test_module_name_validity(project_slug, expected):

    assert is_valid_module_name(project_slug) == expected


package_name_test_date = [
    ("lowercase", True),
    ("lower-with-dashes", True),
    ("lower-with-number-123", True),
    ("CAPITAL", False),
    ("lower_with_underscores", False),
]


@pytest.mark.parametrize("package_name, expected", package_name_test_date)
def test_package_name_validity(package_name, expected):
    assert is_valid_package_name(package_name) == expected
