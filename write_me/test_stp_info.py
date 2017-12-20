"""Test the setup.py parsing function."""

import pytest


from write_me.stp_info import parse_setup_py

setup_dict = parse_setup_py()


def test_dict_is_returned():
    """Function should return a dict."""
    assert type(setup_dict) is dict


def test_dict_not_empty():
    """Returned dict should have info from setup.py."""
    assert setup_dict


def test_dict_contains_name():
    """Test 'name' is key in dict."""
    assert 'name' in setup_dict


def test_dict_name_key_has_correct_value():
    """Test 'name' key has correct value."""
    assert setup_dict['name'] == "write_me"


def test_dict_contains_packages():
    """Test 'packages' is key in dict."""
    assert 'packages' in setup_dict


def test_dict_name_packages_has_correct_value():
    """Test 'name' key has correct value. Should be empty string."""
    assert setup_dict['packages'] == ""


def test_dict_contains_author():
    """Test 'author' is key in dict."""
    assert 'author' in setup_dict


def test_dict_name_author_value_is_a_list():
    """Test 'author' key's value is a list."""
    assert type(setup_dict['author']) is list


def test_dict_author_has_correct_authors():
    """Test 'author' key's value has correct authors."""
    authors = ['Chelsea Dole',
               'Matt Favoino',
               'Darren Haynes',
               'Chris Closser',
               'Gabriel Meringolo']

    assert setup_dict['author'] == authors
