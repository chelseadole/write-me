"""Test file system search."""
import os


def repo_fs():
    """Dir listing of current repo."""
    for root, dirs, files in os.walk("."):
        # import pdb; pdb.set_trace()
        if not dirs.startswith('ENV'):
            for file in files:
                if file.endswith(".py"):
                    print('py file found: ', os.path.join(root, file))
                if file.endswith(".yml"):
                    print('.yml file found: ', os.path.join(root, file))
                if file.endswith(".pip"):
                    print('pip file found: ', os.path.join(root, file))


if __name__ == '__main__':
    print(repo_fs())
