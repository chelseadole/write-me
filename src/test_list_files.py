"""Test for files listed."""

import pytest
from list_files import repo_fs, PY_FILES, YML_FILES, PIP_FILES, README_FILES, TEST_FILES


repo_fs()


def test_readme_files_list():
    """Test found README.md files."""
    assert './readme_generator/README.md' in README_FILES


def test_py_files_list():
    """Test found .py files."""
    assert './src/test/test_class.py' in TEST_FILES


def test_py_files_list_only_py():
    """Test not found .py files."""
    assert './LICENSE' not in PY_FILES


def test_yml_files_list():
    """Test found .yml files."""
    assert './.travis.yml' in YML_FILES


def test_pip_files_list():
    """Test found requirements files."""
    assert './requirements.pip' in PIP_FILES


@pytest.mark.parametrize('item', [item for item in PY_FILES])
def test_only_py_files(item):
    """Test only .py files end up in this list."""
    assert '.py' in item
