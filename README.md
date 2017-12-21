# write-me
---
### Description
[![Build Status](https://travis-ci.org/chelseadole/write-me.svg?branch=staging)](https://travis-ci.org/chelseadole/write-me) [![Coverage Status](https://coveralls.io/repos/github/chelseadole/write-me/badge.svg)](https://coveralls.io/github/chelseadole/write-me)[![PyPI version](https://badge.fury.io/py/write-me.svg)](https://badge.fury.io/py/write-me)

Version: *0.5.4*

Python package to assist developers with constructing README as project evolves.
* Feature #1
* Feature #2
* Feature #3

### Authors
---
* [Chelsea Dole](https://github.com/chelseadole/write-me)
* [Matt Favoino](https://github.com/chelseadole/write-me)
* [Darren Haynes](https://github.com/chelseadole/write-me)
* [Chris Closser](https://github.com/chelseadole/write-me)
* [Gabriel Meringolo](https://github.com/chelseadole/write-me)

### Dependencies
---
* markdown_generator

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/chelseadole/write-me.git`

`$ cd write-me`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -r requirements.txt`
### Test Suite
---
##### *Running Tests*
This application uses [pytest](https://docs.pytest.org/en/latest/) as a testing suite. To run tests, run:

``$ pytest``

To view test coverage, run:

``$ pytest --cov``
##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./test_dep_info.py` | Test dep_info module. |
| `./readme_generator/test_scaffold.py` |  |
| `./write_me/test_django_setings_info.py` | Test django settings module. |
| `./write_me/test_list_files.py` | Test for files listed. |
| `./write_me/test_project_data.py` | Test project data module. |
| `./write_me/test_pyramid_ini.py` | Test pyramid_ini file module. |
| `./write_me/test_scaffold.py` |  |
| `./write_me/test_stp_info.py` | Test the setup.py parsing function. |
| `./write_me/test_travis_badge.py` | Test travis badge. |
| `./write_me/test_tsting_info.py` | Test test info dict. |
| `./write_me/test_uri_info.py` | Test url and route dictionary. |
| `./write_me/test/test_scaffold.py` | Tests for scaffold of README generator. |

### Development Tools
---
* *python* - programming language

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Coffee

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
