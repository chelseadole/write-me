"""Transform setup.py into a python dictionary."""

import ast
from .list_files import get_setup_file

setup_parsed = {}

setup_keys = ['name',
              'version',
              'description',
              'author_email',
              'url',
              'packages',
              'author=']


def parse_setup_py():
    """Covert needed info from setup.py into dict."""
    setup_files = get_setup_file()
    if not setup_files:
        raise FileNotFoundError("No setup.py file found in root directory")

    with open(setup_files[0], 'r') as sf:
        create_list = []
        appending = False
        for line in sf:
            line = line.strip()
            line = line.rstrip(',')
            if not appending:
                for key in setup_keys:
                    if line.startswith(key):
                        k, v = line.split('=')
                        if v.startswith('['):
                            if v.endswith(']'):
                                v = ast.literal_eval(v)
                                setup_parsed[k] = v
                                continue
                            else:
                                appending = True
                                v = v.lstrip('[')
                                create_list.append(v.strip("'"))
                                continue
                        else:
                            setup_parsed[k] = v.strip("'")
                            continue
                    else:
                        continue

            else:
                if line.endswith(']'):
                    appending = False
                    line = line.rstrip(']')
                    create_list.append(line.strip("'"))
                    if key == "author=":
                        key = key.replace("=", "")
                    setup_parsed[key] = create_list
                else:
                    create_list.append(line.strip("'"))

    if 'packages' in setup_parsed:
        if setup_parsed['packages'] == 'find_packages()':
            setup_parsed['packages'] = ''

    return setup_parsed


if __name__ == '__main__':  # pragma no cover
    parse_setup_py()
