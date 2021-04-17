from cookiecutter.main import cookiecutter


def upgrade_project():
    # Create project from the cookiecutter-pypackage.git repo template
    cookiecutter('gh:LeisureTech/python-project-generator', replay=True)


if __name__ == '__main__':
    upgrade_project()
