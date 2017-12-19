# Project Title
---
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
* Feature #1
* Feature #2
* Feature #3

### Authors
---
* [Person1](www.github.com/chelseadole)
* [Person2](www.github.com/chelseadole)
* [Person3](www.github.com/chelseadole)

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository, create a new virtual environment, and install the repo requirements into your VE. To accomplish this, execute these commands:

`$ git clone https://github.com/chelseadole/write-me.git`
`$ cd write-me`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment, and download the project requirements into your VE.

`$ python3 -m venv ENV`
`$ source ENV/bin/activate`
`$ pip install -r requirements.txt`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `manage.py`:
`$ ./manage.py runserver`
Once you have executed this command, open your browser, and go to `localhost:8000/`.
### Test Suite
---
##### *Running Tests*
This application uses pytest as a testing suite. To run tests, run:

`$ pytest`

To view test coverage, run:

`$ pytest --cov`
##### *Test Files*
The testing files for this project are:
* `imager_images/tests.py`
* `imager_profiles/tests.py`
* `imager_api/tests.py`

### URLs
---
The URLs for this project are:

| URL | Description |
|:---:|:---:|
| `/images` | Library of all images |
| `/images/edit` | Edit view for a single image |
| `/images/add` | Add form for a new image |

### Development Tools
---
* Django
* Postgres
* Python
* MongoDB

### Contributions
---
If you wish to contribute to this project, please contact NAME1 or NAME2.
### License
---
This project is licensed under the MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Nicholas Hunt-Walker
* Coffee

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
