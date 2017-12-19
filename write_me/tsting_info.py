"""Get docstring from test_files."""

from write_me.list_files import get_test_files

test_info = {}

TEST_FILES = get_test_files()


def get_docstrings():
    """Get docstings from test files."""
    for test_file in TEST_FILES:
        docstring = []
        with open(test_file, 'r') as tf:
            lines = tf.readlines()
            if lines[0].startswith('"""'):
                if lines[0].endswith('"""\n'):
                    stripped = lines[0].strip()
                    docstring.append(stripped.strip('"""'))
                    test_info[test_file] = "".join(docstring)
                    continue
                for line in lines:
                    stripped = line.strip()
                    docstring.append(stripped.strip('"""'))
                    if line.endswith('"""\n'):
                        test_info[test_file] = "".join(docstring)
                        continue
            else:
                docstring.append("")
        test_info[test_file] = "".join(docstring)
    return test_info

if __name__ == '__main__':
    get_docstrings()
