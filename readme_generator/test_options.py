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
