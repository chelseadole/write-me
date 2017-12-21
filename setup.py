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
<<<<<<< HEAD
    version='0.5.3',
=======
    version='0.5.4',
>>>>>>> 79b4b6d70ad3e2c9c8cd98acc3b0e0060ef40bca
    description='Python package to assist developers with constructing README as project evolves.',
    author=['Chelsea Dole',
            'Matt Favoino',
            'Darren Haynes',
            'Chris Closser',
            'Gabriel Meringolo'],
    author_email='chelseadole@gmail.com',
    url='https://github.com/chelseadole/write-me',
<<<<<<< HEAD
    download_url='https://github.com/chelseadole/write-me/archive/0.5.3.tar.gz',
=======
    download_url='https://github.com/chelseadole/write-me/archive/0.5.4.tar.gz',
>>>>>>> 79b4b6d70ad3e2c9c8cd98acc3b0e0060ef40bca
    keywords=['Python', 'README', 'PyPi', 'pip'],
    classifiers=[],
    install_requires=[
        "markdown_generator",
    ],
)
