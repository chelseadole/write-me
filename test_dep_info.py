"""Test dep_info module."""
import pytest

from write_me.dep_info import local_modules, parse


def test_parse_func_returns_list():
    """Test if parse() returns list."""
    assert isinstance(parse(), list)


def test_local_modules_returns_list():
    """Test if local_modules() returns list."""
    assert isinstance(local_modules(), list)


def test_parse_returns_external_dependency():
    """Test parse returns external dependency."""
    assert 'markdown_generator' in parse()


def test_std_library_not_returned_by_parse():
    """Test a standard library module not returned by parse()."""
    assert 'os' not in parse()


def test_local_module_not_returned_by_parse():
    """Test local module not returned by parse()."""
    assert '.list_files' not in parse()
