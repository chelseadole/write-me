"""Transform setup.py into a python dictionary."""

import ast
from write_me.list_files import get_setup_file
from write_me.git_description import get_git_description
from write_me.project_data import get_project_url

setup_parsed = {}

setup_keys = [
              'version',
              'description',
              'author_email',
              'packages',
              'author=']


def parse_setup_py():
    """Convert needed info from setup.py into dict."""

    setup_files = get_setup_file()
    if not setup_files:
        project_dict = get_project_url()
        setup_parsed['version'] = "YOUR VERSION HERE"
        setup_parsed['description'] = get_git_description()
        setup_parsed['author_email'] = "YOUR EMAIL HERE"
        setup_parsed['packages'] = "YOUR PACKAGES HERE"
        setup_parsed['author'] = [project_dict['project_user']]
        return

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

    if not setup_parsed['author']:
        # get from author from setup_data dict instead.
        setup_parsed['author'] = [project_dict['project_user']]

    if not setup_parsed['author_email']:
        setup_parsed['author_email'] = "YOUR EMAIL HERE"

    if not setup_parsed['version']:
        setup_parsed['version'] = "YOUR VERSION HERE"

    if not setup_parsed['description']:
        setup_parsed['description'] = get_git_description()

    if not setup_parsed['packages']:
        setup_parsed['packages'] = "YOUR PACKAGES HERE"

    return setup_parsed


if __name__ == '__main__':  # pragma no cover
    print(parse_setup_py())
