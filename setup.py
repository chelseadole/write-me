"""Setup script for write-me Python package."""
from setuptools import setup, find_packages


setup(
    name='write_me',
    # package_dir={'': 'write_me', 'readme_generator': 'readme_generator'},
    # py_modules=['readme_generator', 'write_me'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['genreadme=readme_generator.make_scaffold:main'],
    },
    version='0.51',
    description='Python package to assist developers with constructing README as project evolves.',
    author=['Chelsea Dole',
            'Matt Favoino',
            'Darren Haynes',
            'Chris Closser',
            'Gabriel Meringolo'],
    author_email='chelseadole@gmail.com',
    url='https://github.com/chelseadole/write-me',
    download_url='https://github.com/chelseadole/write-me/archive/0.51.tar.gz',
    keywords=['Python', 'README', 'PyPi', 'pip'],
    classifiers=[],
    install_requires=[
        "markdown_generator",
    ],
)
