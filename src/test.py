"""Test file system search."""
import os


def repo_fs():
    """Dir listing of current repo."""
    for root, dirs, files in os.walk("./"):
        for file in files:
            if file.endswith(".py"):
                print(os.path.join(root, file))


if __name__ == '__main__':
    print(repo_fs())
