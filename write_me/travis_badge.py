"""Get the code for the Travis Badge."""


from write_me.list_files import get_yml_files
from write_me.project_data import get_project_url

YAMALS = get_yml_files()

BADGE = "[![Build Status](https://travis-ci.org/{0}/{1}.svg?branch=master)](https://travis-ci.org/{0}/{1})"
COVERALLS = "[![Coverage Status](https://coveralls.io/repos/github/{0}/{1}/badge.svg)](https://coveralls.io/github/{0}/{1})"


def get_travis_file():
    """Return 'travis.yml' file if its in the list of yml files."""
    for yamal in YAMALS:
        if 'travis.yml' in yamal:
            return yamal


def get_travis_badge():
    """Get app name from development.ini."""
    travis_file = get_travis_file()

    coveralls = False
    if travis_file:
        with open(travis_file, 'r') as tf:
            for line in tf:
                if "- coveralls" in line:
                    coveralls = True

        project_info = get_project_url()
        user = project_info['project_user']
        name = project_info['project_name']
        badge = BADGE.format(user, name)

        if coveralls:
            badge_with_coverall = COVERALLS.format(user, name)
            badge = badge + " " + badge_with_coverall
        return badge
    return

if __name__ == '__main__':  # pragma no cover
    res = get_travis_badge()
    print(res)
