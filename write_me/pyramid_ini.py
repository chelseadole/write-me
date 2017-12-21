"""Get app name from pyramid development.ini file."""
from write_me.list_files import get_dev_files

DEV_FILES = get_dev_files()


def get_dev_info():
    """Get app name from development.ini."""
    dev_info = {}

    for dev_file in DEV_FILES:
        with open(dev_file, 'r') as df:
            for line in df:
                if line.startswith("use = egg:"):
                    dont_need, need = line.split(':')
                    app_name = need.strip()
                    dev_info[dev_file] = app_name
                    break

    return dev_info


if __name__ == '__main__':  # pragma no cover
    res = get_dev_info()

    for f in res:
        print(f, ':', res[f])
