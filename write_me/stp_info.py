"""Transform setup.py into a python dictionary."""

import ast

setup_parsed = {}

setup_keys = ['name', 'version', 'description', 'author_email', 'url', 'packages', 'author=']


with open('../setup.py', 'r') as sf:
    # evaluated = ast.literal_eval(sf.read())
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
                            # import pdb; pdb.set_trace()
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


for keys in setup_parsed:
    print(keys, setup_parsed[keys])

print(type(setup_parsed['packages']))
