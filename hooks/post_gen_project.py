import os
import logging

logger = logging.getLogger(__name__)

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        logger.info("Project {{cookiecutter.module_name}} is not open source")
        remove_file('LICENSE')
