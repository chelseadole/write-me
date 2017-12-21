"""Test dep_info module."""
from write_me.dep_info import STD_LIST, local_modules, parse


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


def test_parse_has_no_as_alias():
    """Test parse function doesn't return import alias."""
    assert 'markdown_generator as mg' not in parse()


def test_parse_doesnt_return_commas():
    """Test parse function doesn't return commas."""
    assert ', ' not in parse()


def test_tweepy_not_in_list_of_standard_lib():
    """Test non standard lib not in standard lib list."""
    assert 'tweepy' not in STD_LIST


def test_os_in_list_of_standard_lib():
    """Test standard lib in standard lib list."""
    assert 'os' in STD_LIST


def test_parse_removes_all_the_whites():
    """Test parse function removes extra white space."""
    assert ' markdown_generator' not in parse()
