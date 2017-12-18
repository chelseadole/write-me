"""Setup script for write-me Python package."""
from setuptools import setup


setup(
    name='write_me',
    packages=['write_me'],
    entry_points={
        'console_scripts': []
    },
    version='0.1',
    description='Python package to assist developers with constructing README as project evolves.',
    author=['Chelsea Dole',
            'Matty Favoino',
            'Darren Haynes',
            'Chris Closser',
            'Gabriel Meringolo'],
    author_email=['chelseadole@gmail.com',
                  'mattfavoino@gmail.com',
                  'darrenhaynes@zoho.com',
                  'moredrums@comcast.net',
                  'gabriel.meringolo@gmail.com'],
    url='https://github.com/chelseadole/write-me',
    download_url='',
    keywords=['Python', 'README', 'PyPi', 'pip', 'Matty Favoino'],
    classifiers=[],
)
