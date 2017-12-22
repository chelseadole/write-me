"""Get django settings."""
import ast
import re

from write_me.get_docstrings import get_docstrings
from write_me.list_files import get_settings_files


SETTINGS_FILES = get_settings_files()


def get_settings_info():
    """Get docstings from url files."""
    settings_info = {}

    if not any('settings.py' in f for f in SETTINGS_FILES):
        settings_info['/settings.py'] = "NO SETTINGS.PY FILE SO NO DOCSTRING"
        settings_info['INSTALLED_APPS'] = ["APPS NOT FOUND ADD, YOUR APPS HERE"]
        return settings_info

    for set_file in SETTINGS_FILES:
        docstring = get_docstrings(set_file)
        settings_info[set_file] = docstring

        with open(set_file, 'r') as sf:
            txt = sf.read()
            try:
                regex = re.compile(r'INSTALLED_APPS = (.*?\])', re.DOTALL)
                result = re.search(regex, txt)
                if result:
                    apps_list = ast.literal_eval(re.sub(r'\s*', '', result.group(1)))
                    settings_info['INSTALLED_APPS'] = apps_list
                else:
                    settings_info['INSTALLED_APPS'] = ["APPS NOT FOUND, ADD YOUR APPS HERE"]
            except:
                settings_info['INSTALLED_APPS'] = ["APPS NOT FOUND, ADD YOUR APPS HERE"]

    return settings_info


if __name__ == '__main__':  # pragma no cover
    res = get_settings_info()

    for f in res:
        print(f, ':', res[f])
