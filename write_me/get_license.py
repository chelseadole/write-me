"""Get license type from github license file."""

from write_me.list_files import get_license

LICENSE = get_license()


def get_license_type():
    """Get app name from development.ini."""
    if LICENSE:
        with open(LICENSE[0], 'r') as lf:
            lines = lf.readline()
            license = lines.strip()
            return 'This project is licensed under {} - see the LICENSE.md file for details.'.format(license)
    return 'This package does not have a license.'


if __name__ == '__main__':  # pragma no cover
    res = get_license_type()

    print(res)
