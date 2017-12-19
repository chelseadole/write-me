"""Test test info dict."""

import pytest

from tsting_info import get_docstrings


@pytest.fixture
def tfd():
    """Get test info dict."""
    return get_docstrings()


def test_non_mpty_dict(tfd):
    """Test dictionary is not mpty."""
    assert tfd


def test_a_key_in_dict(tfd):
    """Test dictionary has file path as keys."""
    tkeys = tfd.keys()
    assert './src/test_tsting_info.py' in tkeys


def test_a_keys_val_in_dict(tfd):
    """Test dictionary has this docstring."""
    tval = tfd.get('./src/test_tsting_info.py')
    assert 'Test test info dict.' in tval


def test_b_key_in_dict(tfd):
    """Test dictionary has file path as keys."""
    tkeys = tfd.keys()
    assert './src/test_list_files.py' in tkeys


def test_b_keys_val_in_dict(tfd):
    """Test dictionary has another docstring."""
    tval = tfd.get('./src/test_list_files.py')
    assert 'Test for files listed.' in tval
