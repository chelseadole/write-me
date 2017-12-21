"""Get django settings."""

import ast
import re

from write_me.list_files import get_settings_files

from write_me.get_docstrings import get_docstrings

SETTINGS_FILES = get_settings_files()


def get_settings_info():
    """Get docstings from url files."""
    settings_info = {}
    for set_file in SETTINGS_FILES:
        docstring = get_docstrings(set_file)
        settings_info[set_file] = docstring

        with open(set_file, 'r') as sf:
            txt = sf.read()
            regex = re.compile(r'INSTALLED_APPS = (.*?\])', re.DOTALL)
            result = re.search(regex, txt)
            apps_list = ast.literal_eval(re.sub(r'\s*', '', result.group(1)))
            settings_info['INSTALLED_APPS'] = apps_list

    return settings_info


if __name__ == '__main__':  # pragma no cover
    res = get_settings_info()

    for f in res:
        print(f, ':', res[f])
