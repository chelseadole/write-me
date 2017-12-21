"""Test for files listed."""

from write_me.list_files import (LICENSE, MODEL_FILES, PIP_FILES,
                                 PY_FILES, README_FILES, SETUP_FILES,
                                 TEST_FILES, URL_FILES, YML_FILES, repo_fs)

import pytest

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
    assert './write_me/test/urls.py' in URL_FILES


def test_routes_dot_py_in_url_files():
    """Test routes.py in url files."""
    assert './write_me/test/routes.py' in URL_FILES


def test_setup_in_setup_files():
    """Test setup.py in setup files."""
    assert './setup.py' in SETUP_FILES


def test_license_in_license_list():
    """Test license in license list."""
    assert './LICENSE' in LICENSE


def test_models_in_model_files():
    """Test that models file in MODEL_FILES."""
    assert './write_me/test/models.py' in MODEL_FILES


@pytest.mark.parametrize('item', [item for item in PY_FILES])
def test_only_py_files(item):
    """Test only .py files end up in this list."""
    assert '.py' in item
