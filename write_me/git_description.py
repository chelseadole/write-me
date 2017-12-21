"""Retrieve .git description if not in setup.py."""


def get_git_description():
    """Open .git/description and determine if description exists."""
    try:
        with open('./.git/description', 'r') as git_desc:
            for line in git_desc:
                if line.startswith('Unnamed repository;'):
                    return 'YOUR PROJECT DESCRIPTION HERE'
                else:
                    return git_desc.read()
    except FileNotFoundError:
        return 'YOUR PROJECT DESCRIPTION HERE'

if __name__ == '__main__':  # pragma no cover
    print(get_git_description())
