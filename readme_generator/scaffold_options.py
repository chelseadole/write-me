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
    "flask": {
        "instructions": "Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this cmmand at the same level of your `app.py`.",
        "serve_command": "`$ python app.py`",
        "hosting": "Once you have executed this command, open your brower, and go to `localhost:5000`."
    }
}

built_with_opts = {
    "frameworks": {
        "opts": ['django', 'pyramid', 'flask', 'tornado', 'falcon', 'hug', 'sanic', 'cherrypy'],
        "description": " - web framework"
    },
    "dbms": {
        "opts": ["postgres", "mysql", "mongodb", "sqlite", "oracle"],
        "description": " - database management system"
    },
    "languages": {
        "opts": ["python", "javascript", "react", "node", "java", "swift", "c#", "c++", "c", "php", "ruby on rails", "haskell", "coffeescript", "html", "css"],
        "description": " - programming language"
    }
}
