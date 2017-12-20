"""Get doc strings."""


import re


def get_docstrings(_file):
    """Get our first docstring."""
    docstring = ''
    with open(_file, 'r') as lfile:
        txt = lfile.read()
        if txt.startswith('"""'):
            regex = re.compile(r'""".+?"""', re.DOTALL)
            res = re.match(regex, txt)
            docstring = res.group().replace('"""', '').strip()
            return docstring
