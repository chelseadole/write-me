"""Test file system search."""
import os

ALL_PY_FILES = []
PY_FILES = []
YML_FILES = []
PIP_FILES = []
README_FILES = []
TEST_FILES = []
LICENSE = []
URL_FILES = []
CONTRIBUTIONS = []
SETUP_FILES = []
MODEL_FILES = []
SETTINGS_FILES = []
DEV_FILES = []


def repo_fs():
    """File listing of current repo broken up into lists."""
    for root, dirs, files in os.walk("."):
        dirs[:] = [  # add any extra dirs to ignore #
                   d for d in dirs
                   if '.' not in d
                   and 'ENV' not in d
                   and '__' not in d
                   and 'build' not in d
                   ]

        for f in files:
            if f.endswith(".py"):
                if not f.startswith('__'):
                    ALL_PY_FILES.append(os.path.join(root, f))
                    PY_FILES.append(os.path.join(root, f))
            if f.endswith(".yml"):
                YML_FILES.append(os.path.join(root, f))
            if f.startswith("requirements"):
                PIP_FILES.append(os.path.join(root, f))
            if f.startswith("development"):
                DEV_FILES.append(os.path.join(root, f))
            if f.startswith("README.md"):
                README_FILES.append(os.path.join(root, f))
            if f.startswith("LICENSE"):
                LICENSE.append(os.path.join(root, f))
            if f.startswith("CONTRIBUTIONS"):
                CONTRIBUTIONS.append(os.path.join(root, f))

    if PY_FILES:
        parse_files()

    return {  # dictionary with all lists of file path/names #
            'PY_FILES': PY_FILES,
            'YML_FILES': YML_FILES,
            'PIP_FILES': PIP_FILES,
            'README_FILES': README_FILES,
            'TEST_FILES': TEST_FILES,
            'LICENSE': LICENSE,
            'URL_FILES': URL_FILES,
            'CONTRIBUTIONS': CONTRIBUTIONS,
            'SETUP_FILES': SETUP_FILES,
            'MODEL_FILES': MODEL_FILES,
            'SETTINGS_FILES': SETTINGS_FILES,
            'DEV_FILES': DEV_FILES,
            }


def get_test_files():
    """Return list of all test files in project."""
    repo_fs()
    return TEST_FILES


def get_yml_files():
    """Return list of all test files in project."""
    repo_fs()
    return YML_FILES


def get_license():
    """Return license file path."""
    repo_fs()
    return LICENSE


def get_setup_file():
    """Return list of all setup.py files in project."""
    repo_fs()
    return SETUP_FILES


def get_requirements():
    """."""
    repo_fs()
    return PIP_FILES


def get_settings_files():
    """."""
    repo_fs()
    return SETTINGS_FILES


def get_dev_files():
    """."""
    repo_fs()
    return DEV_FILES


def get_py_files():
    """."""
    repo_fs()
    return PY_FILES


def get_all_py_files():
    """."""
    repo_fs()
    return ALL_PY_FILES


def get_url_files():
    """."""
    repo_fs()
    return URL_FILES


def parse_files():
    """Parse all the files."""
    pfuncs = [  # parse py files : add #
              parse_test_files,
              parse_model_files,
              parse_url_files,
              parse_route_files,
              parse_settings_files,
              parse_setup_files,
              ]

    while PY_FILES:
        for _ in range(len(pfuncs)):
            a_func = pfuncs.pop()
            a_func()
        break


def parse_model_files():
    """Remove model files into seperate lists."""
    a_copy = PY_FILES[::]
    for f in a_copy:
        if 'model' in f:
            MODEL_FILES.append(f)
            PY_FILES.remove(f)


def parse_setup_files():
    """Remove setup files into seperate lists."""
    a_copy = PY_FILES[::]
    for f in a_copy:
        if 'setup' in f:
            SETUP_FILES.append(f)
            PY_FILES.remove(f)


def parse_settings_files():
    """Remove settings files into seperate lists."""
    a_copy = PY_FILES[::]
    for f in a_copy:
        if 'settings' in f:
            SETTINGS_FILES.append(f)
            PY_FILES.remove(f)


def parse_test_files():
    """Remove test files into seperate list."""
    a_copy = PY_FILES[::]
    for f in a_copy:
        if 'test' in f:
            TEST_FILES.append(f)
            PY_FILES.remove(f)


def parse_url_files():
    """Remove url files into seperate lists."""
    a_copy = PY_FILES[::]
    for f in a_copy:
        if 'urls' in f:
            URL_FILES.append(f)
            PY_FILES.remove(f)


def parse_route_files():
    """Remove route files into seperate lists."""
    a_copy = PY_FILES[::]
    for f in a_copy:
        if 'routes' in f:
            URL_FILES.append(f)
            PY_FILES.remove(f)


if __name__ == '__main__':  # pragma no cover
    repo_fs()
    print(  # lists all files we are looking at if run from terminal #
          '.PY FILES:\n', PY_FILES,
          '\n.YML FILES:\n', YML_FILES,
          '\nREQUIREMENTS:\n', PIP_FILES,
          '\nREADME.md files:\n', README_FILES,
          '\nTEST FILES:\n', TEST_FILES,
          '\nLICENSE:\n', LICENSE,
          '\nURL_FILES:\n', URL_FILES,
          '\nCONTRIBUTIONS:\n', CONTRIBUTIONS,
          '\nSETUP_FILES:\n', SETUP_FILES,
          '\nMODEL_FILES:\n', MODEL_FILES,
          '\nSETTINGS_FILES:\n', SETTINGS_FILES,
          '\nDEV_FILES:\n', DEV_FILES,
          )
