import pytest


@pytest.fixture
def context():
    return {
        "package_name": "test-generator",
        "project_name": "Test Project",
        "project_short_description": "test",
        "module_name": "test_app",
        "app_name": "Test App",
        "full_name": "test",
        "version": "0.0.0",
        "github_username": "test",
        "email": "test@test.com",
        "port": 20000,
        "open_source_license": [
            "MIT license",
            "BSD license",
            "ISC license",
            "Apache Software License 2.0",
            "GNU General Public License v3",
            "Not open source"]
    }


def test_generation(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["module_name"]
    assert result.project.isdir()


def test_has_license(cookies, context):
    context["open_source_license"] = "MIT"
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.join('LICENSE').check(file=1)


def test_no_license(cookies, context):
    context["open_source_license"] = "Not open source"
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert not result.project.join('LICENSE').check(file=1)
