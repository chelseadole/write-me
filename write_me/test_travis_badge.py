"""Test travis badge."""
from write_me.travis_badge import get_travis_badge


def test_travis_badge_returns_str():
    """Test get_travis_badge returns str."""
    res = get_travis_badge()
    assert isinstance(res, str)
