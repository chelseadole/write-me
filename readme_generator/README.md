# write_me
---
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

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository, create a new virtual environment, and install the repo requirements into your VE. To accomplish this, execute these commands:

`$ git clone https://github.com/chelseadole/write-me.git`
`$ cd write_me`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment, and download the project requirements into your VE.

`$ python3 -m venv ENV`
`$ source ENV/bin/activate`
`$ pip install -r requirements.txt`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `manage.py`.
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

| File Name | Description |
|:---:|:---:|
| `./test_scaffold.py` | Test file for ensure scaffolding functionality. |

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
### Contributions
---
If you wish to contribute to this project, please contact chelseadole@gmail.com.
### License
---
This project is licensed under the MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Nicholas Hunt-Walker
* Coffee

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
