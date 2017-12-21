"""Test url and route dictionary."""

from write_me.django_uri_info import get_url_docstrings


def test_get_url_docstring_returns_dict():
    """Test_get_url_docstring_returns_dict."""
    assert type(get_url_docstrings()) is dict


def test_get_correct_docstring():
    """Test_get_correct_docstring."""
    res = get_url_docstrings()
    assert res['./write_me/test/routes.py'] == ''


def test_multi_line_docstring():
    """Test_multi_line_docstring."""
    res = get_url_docstrings()
    assert res['./write_me/test/main_urls.py'] == 'A multi line string.with a line space.'
