import re


def is_valid_module_name(module_name):
    module_regex = r"^[a-z][_a-z0-9]+$"
    return re.match(module_regex, module_name) is not None


def is_valid_package_name(package_name):
    package_regex = r"^[a-z][-a-z0-9]+$"
    return re.match(package_regex, package_name) is not None
