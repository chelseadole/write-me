"""Test file system search."""
import os

PY_FILES = []
YML_FILES = []
PIP_FILES = []


def repo_fs():
    """Dir listing of current repo."""
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if '.' not in d and 'ENV' not in d and '__' not in d]
        for file in files:
            if file.endswith(".py"):
                PY_FILES.append(os.path.join(root, file))
            if file.endswith(".yml"):
                YML_FILES.append(os.path.join(root, file))
            if file.startswith("requirements"):
                PIP_FILES.append(os.path.join(root, file))

    # import pdb; pdb.set_trace()
if __name__ == '__main__':
    print(repo_fs())
