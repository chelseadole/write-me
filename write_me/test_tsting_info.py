"""Test test info dict."""

import pytest

from write_me.tsting_info import get_test_docstrings


tfd = get_test_docstrings()


def test_non_mpty_dict():
    """Test dictionary is not mpty."""
    assert tfd


def test_a_key_in_dict():
    """Test dictionary has file path as keys."""
    tkey = tfd.keys()
    assert './write_me/test_tsting_info.py' in tkey


def test_a_keys_val_in_dict():
    """Test dictionary has this docstring."""
    tval = tfd.get('./write_me/test_tsting_info.py')
    assert 'Test test info dict.' in tval


def test_b_key_in_dict():
    """Test dictionary has file path as keys."""
    tkey = tfd.keys()
    assert './write_me/test_list_files.py' in tkey


def test_b_keys_val_in_dict():
    """Test dictionary has another docstring."""
    tval = tfd.get('./write_me/test_list_files.py')
    assert 'Test for files listed.' in tval


def test_is_dict():
    """The get_docstrings() function should return a dict."""
    assert type(tfd) is dict


@pytest.mark.parametrize('fname', [fname for fname in get_test_docstrings()])
def test_filenames_should_be_test_files(fname):
    """All filenames should have string 'test' in them."""
    assert 'test' in fname


def test_file_test_scaffold_has_correct_docstring():
    """The 'test_scaffold.py' file gets correct docstring."""
    docstring = 'Tests for scaffold of README generator.'
    assert tfd['./write_me/test/test_scaffold.py'] == docstring


# def test_fivle_test_scaffold_has_correct_docstring():
#     """The."""
#     docstring = "Test file for ensure scaffolding functionality."
#     assert tfd['./readme_generator/test_scaffold.py'] == docstring
