"""Get license type from github license file."""

from list_files import get_license

LICENSE = get_license()


def get_license_type():
    """Get app name from development.ini."""
    if LICENSE:
        with open(LICENSE[0], 'r') as lf:
            lines = lf.readline()
            return lines.strip()


if __name__ == '__main__':  # pragma no cover
    res = get_license_type()

    print(res)