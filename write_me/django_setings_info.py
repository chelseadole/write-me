"""Get django settings."""


from list_files import get_settings_files

from get_docstrings import get_docstrings

SETTINGS_FILES = get_settings_files()


def get_settings_info():
    """Get docstings from url files."""
    settings_info = {}
    for set_file in SETTINGS_FILES:
        docstring = get_docstrings(set_file)
        settings_info[set_file] = docstring
    return settings_info


if __name__ == '__main__':  # pragma no cover
    res = get_settings_info()

    for f in res:
        print(f, ':',  res[f])
