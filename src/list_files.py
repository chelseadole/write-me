"""Test file system search."""
import os

PY_FILES = []
YML_FILES = []
PIP_FILES = []
README_FILES = []
TEST_FILES = []


def repo_fs():
    """File listing of current repo broken up into lists."""
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if '.' not in d and 'ENV' not in d and '__' not in d]
        for f in files:
            if f.endswith(".py"):
                PY_FILES.append(os.path.join(root, f))
            if f.endswith(".yml"):
                YML_FILES.append(os.path.join(root, f))
            if f.startswith("requirements"):
                PIP_FILES.append(os.path.join(root, f))
            if f.startswith("README.md"):
                README_FILES.append(os.path.join(root, f))
    if PY_FILES:
        parse_test_files()


def parse_test_files():
    """Remove test files into seperate list."""
    for f in PY_FILES:
        if 'test' in f:
            TEST_FILES.append(f)
            PY_FILES.remove(f)


if __name__ == '__main__':  # pragma no cover
    repo_fs()
    print('.py files:\n', PY_FILES,
          '\n.yml files:\n', YML_FILES,
          '\nrequirements:\n', PIP_FILES,
          '\nREADME.md files:\n', README_FILES,
          '\ntest files:\n', TEST_FILES
          )
