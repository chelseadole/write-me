"""Gather all dependencies not in standard library and return as list."""
import re

from .list_files import get_all_py_files, get_py_files

DEP_LIST = []

PY_FILES = get_py_files()

ALL_PY = get_all_py_files()


STD_LIST = ['__future__', '__main__', '_dummy_thread', '_thread', 'abc',
            'aifc', 'argparse', 'array', 'ast', 'asynchat', 'asyncio',
            'asyncore', 'atexit', 'audioop', 'base64', 'bdb', 'binascii',
            'binhex', 'bisect', 'builtins', 'bz2', 'cProfile', 'calendar',
            'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs',
            'codeop', 'collections', 'collections.abc', 'colorsys',
            'compileall', 'concurrent.futures', 'configparser', 'contextlib',
            'copy', 'copyreg', 'crypt', 'csv', 'ctypes', 'curses',
            'curses.ascii', 'curses.panel', 'curses.textpad', 'datetime',
            'dbm', 'dbm.dumb', 'dbm.gnu', 'dbm.ndbm', 'decimal', 'difflib',
            'dis', 'distutils', 'distutils.archive_util',
            'distutils.bcppcompiler', 'distutils.ccompiler',
            'distutils.cmd', 'distutils.command',
            'distutils.command.bdist', 'distutils.command.bdist_dumb',
            'distutils.command.bdist_msi', 'distutils.command.bdist_packager',
            'distutils.command.bdist_rpm', 'distutils.command.bdist_wininst',
            'distutils.command.build', 'distutils.command.build_clib',
            'distutils.command.build_ext', 'distutils.command.build_py',
            'distutils.command.build_scripts', 'distutils.command.check',
            'distutils.command.clean', 'distutils.command.config',
            'distutils.command.install', 'distutils.command.install_data',
            'distutils.command.install_headers',
            'distutils.command.install_lib',
            'distutils.command.install_scripts', 'distutils.command.register',
            'distutils.command.sdist', 'distutils.core',
            'distutils.cygwinccompiler',
            'distutils.debug', 'distutils.dep_util', 'distutils.dir_util',
            'distutils.dist', 'distutils.errors', 'distutils.extension',
            'distutils.fancy_getopt', 'distutils.file_util',
            'distutils.filelist',
            'distutils.log', 'distutils.msvccompiler', 'distutils.spawn',
            'distutils.sysconfig', 'distutils.text_file',
            'distutils.unixccompiler', 'distutils.util', 'distutils.version',
            'doctest', 'dummy_threading', 'email', 'email.charset',
            'email.contentmanager', 'email.encoders', 'email.errors',
            'email.generator', 'email.header', 'email.headerregistry',
            'email.iterators', 'email.message', 'email.mime',
            'email.parser', 'email.policy', 'email.utils',
            'encodings.idna', 'encodings.mbcs', 'encodings.utf_8_sig',
            'ensurepip', 'enum', 'errno',
            'faulthandler', 'fcntl', 'filecmp',
            'fileinput', 'fnmatch', 'formatter',
            'fpectl', 'fractions', 'ftplib',
            'functools', 'gc', 'getopt',
            'getpass', 'gettext', 'glob',
            'grp', 'gzip', 'hashlib',
            'heapq', 'hmac', 'html',
            'html.entities', 'html.parser', 'http',
            'http.client', 'http.cookiejar', 'http.cookies',
            'http.server', 'imaplib', 'imghdr',
            'imp', 'importlib', 'importlib.abc',
            'importlib.machinery', 'importlib.util', 'inspect',
            'io', 'ipaddress', 'itertools',
            'json', 'json.tool', 'keyword',
            'lib2to3', 'linecache', 'locale',
            'logging', 'logging.config', 'logging.handlers',
            'lzma', 'macpath', 'mailbox',
            'mailcap', 'marshal', 'math',
            'mimetypes', 'mmap', 'modulefinder',
            'msilib', 'msvcrt', 'multiprocessing',
            'multiprocessing.connection', 'multiprocessing.dummy',
            'multiprocessing.managers', 'multiprocessing.pool',
            'multiprocessing.sharedctypes', 'netrc', 'nis',
            'nntplib', 'numbers', 'operator',
            'optparse', 'os', 'os.path',
            'ossaudiodev', 'parser', 'pathlib',
            'pdb', 'pickle', 'pickletools',
            'pipes', 'pkgutil', 'platform',
            'plistlib', 'poplib', 'posix',
            'pprint', 'profile', 'pstats',
            'pty', 'pwd', 'py_compile',
            'pyclbr', 'pydoc', 'queue',
            'quopri', 'random', 're',
            'readline', 'reprlib', 'resource',
            'rlcompleter', 'runpy', 'sched',
            'secrets', 'select', 'selectors',
            'shelve', 'shlex', 'shutil',
            'signal', 'site', 'smtpd',
            'smtplib', 'sndhdr', 'socket',
            'socketserver', 'spwd', 'sqlite3',
            'ssl', 'stat', 'statistics', 'string',
            'stringprep', 'struct', 'subprocess',
            'sunau', 'symbol', 'symtable',
            'sys', 'sysconfig', 'syslog', 'tabnanny',
            'tarfile', 'telnetlib', 'tempfile', 'termios',
            'test', 'test.support', 'textwrap',
            'threading', 'time', 'timeit',
            'tkinter', 'tkinter.scrolledtext', 'tkinter.tix',
            'tkinter.ttk', 'token', 'tokenize',
            'trace', 'traceback', 'tracemalloc',
            'tty', 'turtle', 'turtledemo',
            'types', 'typing', 'unicodedata',
            'unittest', 'unittest.mock', 'urllib',
            'urllib.error', 'urllib.parse', 'urllib.request',
            'urllib.response', 'urllib.robotparser', 'uu',
            'uuid', 'venv', 'warnings',
            'wave', 'weakref', 'webbrowser',
            'winreg', 'winsound', 'wsgiref',
            'wsgiref.handlers', 'wsgiref.headers', 'wsgiref.simple_server',
            'wsgiref.util', 'wsgiref.validate', 'xdrlib',
            'xml', 'xml.dom', 'xml.dom.minidom',
            'xml.dom.pulldom', 'xml.etree.ElementTree', 'xml.parsers.expat',
            'xml.parsers.expat.errors', 'xml.parsers.expat.model', 'xml.sax',
            'xml.sax.handler', 'xml.sax.saxutils', 'xml.sax.xmlreader',
            'xmlrpc.client', 'xmlrpc.server', 'zipapp',
            'zipfile', 'zipimport', 'zlib'
            ]


def local_modules():
    """Strip local file path to use in parse function below."""
    holder = []
    for path in ALL_PY:
        holder.append(path.rsplit('/')[-1].split('.py')[0])
    return holder


def parse(files=PY_FILES):
    """Parse import statements, compare to std library."""
    libbies = []
    reg_pat = re.compile(r'(.*import.*)', re.M)
    for py_file in files:
        with open(py_file) as file_obj:
            words = file_obj.read()
            if len(words) > 0:
                x = re.findall(reg_pat, words)
                for ret in x:
                    if ret.startswith('import'):
                        libbies.append(ret.split('import')[1].strip())
                    if ret.startswith('from'):
                        libbies.append(ret.split('import')[0].split('from ')[-1].strip())
    for lib in libbies:
        if ' as ' in lib:
            libbies.append(lib.split(' as ')[0])
            libbies.remove(lib)
        if ', ' in lib:
            libbies.extend(lib.split(', '))
            libbies.remove(lib)
    libbies = {lib for lib in libbies if lib not in STD_LIST}
    final = []
    for lib in libbies:
        if '.' in lib:
            final.append(lib.split('.')[-1])
        else:
            final.append(lib)
    return [x for x in final if x not in local_modules()]
