"""Setup script for write-me Python package."""
from setuptools import find_packages, setup


setup(
    name='write_me',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['genreadme=readme_generator.make_scaffold:main'],
    },
    version='0.6.6',
    description="Python package to assist developers with constructing README as project evolves.",
    author='The write-me team: Chelsea Chris Matt Darren Gabe',
    author_email='writeme.pypi@gmail.com',
    url='http://write-me.readthedocs.io/',
    download_url='https://github.com/chelseadole/write-me/archive/0.6.6.tar.gz',
    keywords=['Python', 'README', 'PyPi', 'pip'],
    license='MIT',
    classifiers=[],
    install_requires=[
        "markdown_generator",
    ],
)
