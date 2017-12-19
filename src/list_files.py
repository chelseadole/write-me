"""Test file system search."""
import os

PY_FILES = []
YML_FILES = []
PIP_FILES = []
README_FILES = []
TEST_FILES = []
LICENSE = []
URL_FILES = []
CONTRIBUTIONS = []
SETUP_FILES = []


def repo_fs():
    """File listing of current repo broken up into lists."""
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if '.' not in d and 'ENV' not in d and '__' not in d]
        for f in files:
            if f.endswith(".py"):
                if not f.startswith('__'):
                    PY_FILES.append(os.path.join(root, f))
            if f.endswith(".yml"):
                YML_FILES.append(os.path.join(root, f))
            if f.startswith("requirements"):
                PIP_FILES.append(os.path.join(root, f))
            if f.startswith("README.md"):
                README_FILES.append(os.path.join(root, f))
            if f.startswith("LICENSE"):
                LICENSE.append(os.path.join(root, f))
            if f.startswith("CONTRIBUTIONS"):
                CONTRIBUTIONS.append(os.path.join(root, f))
    parse_files()


def parse_files():
    """Parse all the files."""
    if PY_FILES:
        parse_setup_files()
        if PY_FILES:
            parse_settings_files()
            if PY_FILES:
                parse_test_files()
                if PY_FILES:
                    parse_url_files()
                    if PY_FILES:
                        parse_route_files()


def parse_setup_files():
    """Remove setup files into seperate lists."""
    for f in PY_FILES:
        if 'setup' in f:
            SETUP_FILES.append(f)
            PY_FILES.remove(f)


def parse_settings_files():
    """Remove settings files into seperate lists."""
    for f in PY_FILES:
        if 'settings' in f:
            SETUP_FILES.append(f)
            PY_FILES.remove(f)


def parse_test_files():
    """Remove test files into seperate list."""
    for f in PY_FILES:
        if 'test' in f:
            TEST_FILES.append(f)
            PY_FILES.remove(f)


def parse_url_files():
    """Remove url files into seperate lists."""
    for f in PY_FILES:
        if 'urls' in f:
            URL_FILES.append(f)
            PY_FILES.remove(f)


def parse_route_files():
    """Remove route files into seperate lists."""
    for f in PY_FILES:
        if 'routes' in f:
            URL_FILES.append(f)
            PY_FILES.remove(f)


if __name__ == '__main__':  # pragma no cover
    repo_fs()
    print('.py files:\n', PY_FILES,
          '\n.yml files:\n', YML_FILES,
          '\nrequirements:\n', PIP_FILES,
          '\nREADME.md files:\n', README_FILES,
          '\ntest files:\n', TEST_FILES,
          '\nLICENSE:\n', LICENSE,
          '\nURL_FILES:\n', URL_FILES,
          '\nCONTRIBUTIONS:\n', CONTRIBUTIONS,
          '\nCONTRIBUTIONS:\n', CONTRIBUTIONS,
          '\nsetup_files:\n', SETUP_FILES,
          )
