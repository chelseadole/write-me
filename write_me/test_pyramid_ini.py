"""Test pyramid_ini file module."""
from write_me.pyramid_ini import get_dev_info


def test_get_dev_info_returns_dict():
    """Test that get dev info returns dict."""
    assert isinstance(get_dev_info(), dict)
