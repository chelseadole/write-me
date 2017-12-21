"""Get django urls."""
from write_me.list_files import get_url_files

url_info = {}

URL_FILES = get_url_files()


def get_url_docstrings():
    """Get docstings from url files."""
    for url_file in URL_FILES:
        docstring = []
        with open(url_file, 'r') as tf:
            lines = tf.readlines()
            if lines and lines[0].startswith('"""'):
                if lines[0].endswith('"""\n'):
                    stripped = lines[0].strip()
                    docstring.append(stripped.strip('"""'))
                    url_info[url_file] = "".join(docstring)
                    continue
                for line in lines:
                    stripped = line.strip()
                    docstring.append(stripped.strip('"""'))
                    if line.endswith('"""\n'):
                        url_info[url_file] = "".join(docstring)
                        continue
            else:
                docstring.append("")
        url_info[url_file] = "".join(docstring)
    return url_info
