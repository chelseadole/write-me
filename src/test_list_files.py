"""Test for files listed."""

import pytest
from list_files import (repo_fs, PY_FILES, YML_FILES,
                        PIP_FILES, README_FILES, TEST_FILES,
                        URL_FILES)


repo_fs()


def test_readme_files_list():
    """Test found README.md files."""
    assert 'README.md' in README_FILES[0]


def test_py_files_list():
    """Test found .py files."""
    assert './readme_generator/test_scaffold.py' in TEST_FILES


def test_py_files_list_only_py():
    """Test not found .py files."""
    assert './LICENSE' not in PY_FILES


def test_yml_files_list():
    """Test found .yml files."""
    assert './.travis.yml' in YML_FILES


def test_pip_files_list():
    """Test found requirements files."""
    assert './requirements.pip' in PIP_FILES


def test_url_dot_py_in_url_files():
    """Test url.py in url files."""
    assert './src/urls.py' in URL_FILES


def test_routes_dot_py_in_url_files():
    """Test routes.py in url files."""
    assert './src/routes.py' in URL_FILES


@pytest.mark.parametrize('item', [item for item in PY_FILES])
def test_only_py_files(item):
    """Test only .py files end up in this list."""
    assert '.py' in item
