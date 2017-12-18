# Project Title
---
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
* Feature #1
* Feature #2
* Feature #3

### Getting Started
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository, create a new virtual environment, and install the repo's requirements into your VE. To accomplish this, execute these commands:

`$ git clone https://github.com/chelseadole/write-me.git`
`$ cd write-me`

Now now that you've cloned your repo and changed directories into the project, create a virtual environment, and download the project's requirements into your VE.

`$ python3 -m venv ENV`
`$ source ENV/bin/activate`
`$ pip install -r requirements.txt`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine. Once you have executed this command, open your browser, and go to `http://localhost:8000/`
`$ ./manage.py runserver`
### Test Suite
##### *Running Tests*
This application uses pytest as a testing suite. To run tests, run:

`$ pytest`

To view test coverage, run:

`$ pytest --cov`
