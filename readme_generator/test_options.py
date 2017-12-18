"""Testing module options for README, with varying syntax for running tests."""


test_options = {
    "nose_testing": {
        "name": "nose",
        "url": "http://nose.readthedocs.io/en/latest/",
        "run_tests": "`$ nosetests`",
        "run_cov": "`$ nosetests --with-coverage`"
    },
    "pytest_testing": {
        "name": "pytest",
        "url": "https://docs.pytest.org/en/latest/",
        "run_tests": "`$ pytest`",
        "run_cov": "`$ pytest --cov`"
    },
    "unittest_testing": {
        "name": "unittest",
        "url": "https://docs.python.org/3/library/unittest.html",
        "run_tests": "`$ python3 -m unittest`",
        "run_cov": "`$ coverage report -m`"
    }
}

serving_options = {
    "django": {
        "instructions": "Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `manage.py`:",
        "serve_command": "`$ ./manage.py runserver`",
        "hosting": "Once you have executed this command, open your browser, and go to `localhost:8000/`."
    },
    "pyramid": {
        "instructions": "Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command at the root level of your application, at the same level as `development.ini` and `production.ini`.",
        "serve_command": "`$ pserve development.ini`",
        "hosting": "Once you have executed this command, open your browser, and go to `localhost:6543/ `."
    },
    ""
}
