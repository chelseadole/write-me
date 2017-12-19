"""Test test info dict."""

import pytest

from write_me.tsting_info import get_docstrings


tfd = get_docstrings()


def test_non_mpty_dict():
    """Test dictionary is not mpty."""
    assert tfd


def test_a_key_in_dict():
    """Test dictionary has file path as keys."""
    tkeys = tfd.keys()
    assert './write_me/test_tsting_info.py' in tkeys


def test_a_keys_val_in_dict():
    """Test dictionary has this docstring."""
    tval = tfd.get('./write_me/test_tsting_info.py')
    assert 'Test test info dict.' in tval


def test_b_key_in_dict():
    """Test dictionary has file path as keys."""
    tkeys = tfd.keys()
    assert './write_me/test_list_files.py' in tkeys


def test_b_keys_val_in_dict():
    """Test dictionary has another docstring."""
    tval = tfd.get('./write_me/test_list_files.py')
    assert 'Test for files listed.' in tval
