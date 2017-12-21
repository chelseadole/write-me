"""Get docstring from test_files."""

from write_me.get_docstrings import get_docstrings
from write_me.list_files import get_test_files

test_info = {}

TEST_FILES = get_test_files()


def get_test_docstrings():
    """Get docstings from test files."""
    for test_file in TEST_FILES:
        docstring = get_docstrings(test_file)
        test_info[test_file] = docstring

    return test_info


if __name__ == '__main__':  # pragma no cover
    get_test_docstrings()
