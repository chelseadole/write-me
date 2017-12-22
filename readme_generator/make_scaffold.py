"""Module to create README.md file with basic scaffold."""
import argparse
import os
import shutil

import markdown_generator as mg

from readme_generator.scaffold_options import (dbms, frameworks,
                                               serving_options, test_options,)

from write_me.dep_info import parse
from write_me.django_setings_info import get_settings_info
from write_me.django_uri_info import get_url_docstrings
from write_me.get_license import get_license_type
from write_me.list_files import get_all_py_files
from write_me.project_data import get_project_url
from write_me.pyramid_ini import get_dev_info
from write_me.stp_info import parse_setup_py
from write_me.travis_badge import get_travis_badge
from write_me.tsting_info import get_test_docstrings

settings_dict = get_settings_info()
url_dict = get_url_docstrings()
setup_dict = parse_setup_py()
dependencies = parse()
license = get_license_type()
test_dict = get_test_docstrings()
get_all_py = get_all_py_files()
user_data = get_project_url()
pyramid_info = get_dev_info()
badge = get_travis_badge()

testing_lst = parse(get_all_py)
testing_mod = ''
for i in testing_lst:
    if i == "pytest" or i == "nose":
        testing_mod = i
if not testing_mod:
    testing_mod = "unittest"

parser = argparse.ArgumentParser()  # pragma: no cover
parser.add_argument('-v', '--verbose',
                    help='create verbose readme',
                    action='store_true')
parser.add_argument('-d', '--django',
                    help='Django readme scaffolding',
                    action='store_true')
parser.add_argument('-p', '--pyramid',
                    help='Pyramid readme scaffolding',
                    action='store_true')
parser.add_argument('-f', '--flask',
                    help='Flask readme scaffolding',
                    action='store_true')
args = parser.parse_args()


def overwrite(answer=None):
    """Check if user wants to overwrite existing README.md."""
    prompt_txt = """
    Do you want to overwrite your present README file?
    Don't worry, if you overwrite your present README
    it will be backed up to README.md.old

    Yes or no?
    """
    poss_answers = ['n', 'no', 'y', 'yes']

    if not answer:
        answer = input(prompt_txt).lower()
        while answer not in poss_answers:
            answer = input(prompt_txt).lower()

    if answer == 'yes' or answer == 'y':
        if os.path.isfile('README.md'):
            shutil.move('README.md', 'README.md.old')
        return 'README.md'
    elif answer == 'no' or answer == 'n':
        return 'README.md.new'


def main():
    """Create README."""
    if os.path.isfile('README.md'):
        readme = overwrite()
    else:
        readme = 'README.md'

    with open(readme, 'w') as f:
        w = mg.Writer(f)
        w.write_heading(user_data['project_name'], 1)
        w.write_hrule()

        # Description and Key Features
        w.write_heading('Description', 3)
        if badge:
            w.writeline(badge)
            w.writeline()
        w.writeline('Version: ' + mg.emphasis(setup_dict['version']))
        w.writeline()
        w.writeline(setup_dict['description'])
        key_features = mg.List()
        key_features.append('Feature #1')
        key_features.append('Feature #2')
        key_features.append('Feature #3')
        w.write(key_features)

        # AUTHORS
        w.write_heading('Authors', 3)
        w.write_hrule()
        authors = mg.List()
        for i in range(len(setup_dict['author'])):
            authors.append(mg.link(user_data['url'], setup_dict['author'][i]))
        w.write(authors)

        if len(dependencies) > 0:
            # DEPENDENCIES
            w.write_heading('Dependencies', 3)
            w.write_hrule()
            deps = mg.List()
            for dep in dependencies:
                deps.append(dep)
            if args.django and "django" not in dependencies:
                deps.append("Django")
            elif args.pyramid and "pyramid" not in dependencies:
                deps.append("Pyramid")
            elif args.flask and "flask" not in dependencies:
                deps.append("Flask")
            w.write(deps)

        if args.verbose:
            # DOCS
            w.write_heading('Documentation', 3)
            w.write_hrule()
            w.writeline('Additional documentation can be found at: YOUR DOC SITE HERE')

        w.write_heading('Getting Started', 3)
        w.write_hrule()

        # GETTING STARTED: Installation requirements
        w.write_heading(mg.emphasis('Prerequisites'), 5)
        prereqs = mg.List()
        prereqs.append(mg.link('https://www.python.org/downloads/', 'python (3.6+)'))
        prereqs.append(mg.link('https://pip.pypa.io/en/stable/', 'pip'))
        prereqs.append(mg.link('https://git-scm.com/', 'git'))
        w.write(prereqs)

        # GETTING STARTED: Cloning/VE Instructions
        w.write_heading(mg.emphasis('Installation'), 5)
        w.writeline('First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:')
        w.writeline()
        w.writeline('`$ git clone {}.git`'.format(user_data['url']))
        w.writeline()
        w.writeline('`$ cd {}`'.format(user_data['project_name']))
        w.writeline()
        w.writeline('Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.')
        w.writeline()
        w.writeline('`$ python3 -m venv ENV`')
        w.writeline()
        w.writeline('`$ source ENV/bin/activate`')
        w.writeline()
        w.writeline('`$ pip install -r requirements.txt`')

        if os.path.isfile('requirements.txt'):
            with open('requirements.txt', 'r') as f:
                reqs = []
                for line in f:
                    line = line.strip()
                    reqs.append(line)
            reqs = [i.split('==')[0] for i in reqs]

            if args.django and "psycopg2" in reqs:
                # Additional Django setup requirements using PostgreSQL
                w.writeline()
                w.writeline('Open PostgreSQL using the `psql` command from your Terminal.')
                w.writeline('Create a PostgreSQL Database, called YOUR DBNAME HERE, using following command:')
                w.writeline()
                w.writeline('`USER=# CREATE DATABASE ~YOUR DB NAME HERE~;`')
                w.writeline()
                w.writeline('Now that your database exists, you can migrate this project\'s data into it. Outside of the PostgreSQL commandline, on the same level as your `manage.py` file, run:')
                w.writeline('`$ ./manage.py migrate`')
                w.writeline()

            elif args.django and "mymssql" in reqs:
                # Additional Django setup requirements using MySQL
                w.writeline()
                w.writeline('Open MySQL using the `psql` command from your Terminal, with your personal user data.')
                w.writeline('Create a PostgreSQL Database, called YOUR DBNAME HERE, using following command:')
                w.writeline()
                w.writeline('`USER=# CREATE DATABASE ~YOUR DB NAME HERE~;`')
                w.writeline()
                w.writeline('Now that your database exists, you can migrate this project\'s data into it. Outside of the MySQL commandline, on the same level as your `manage.py` file, run:')
                w.writeline('`$ ./manage.py migrate`')
                w.writeline()

            elif args.django and "cx_Oracle" in reqs:
                # Additional Django setup requirements using Oracle
                w.writeline()
                w.writeline('Open Oracle using the `sqlplus` command from your Terminal.')
                w.writeline('Create an Oracle Database, called YOUR DBNAME HERE, using following command:')
                w.writeline()
                w.writeline('`USER=# CREATE DATABASE ~YOUR DB NAME HERE~;`')
                w.writeline()
                w.writeline('Now that your database exists, you can migrate this project\'s data into it. Outside of the Oracle commandline, on the same level as your `manage.py` file, run:')
                w.writeline('`$ ./manage.py migrate`')
                w.writeline()

        if args.django:
            # GETTING STARTED: Serving the App (Django)
            w.write_heading(mg.emphasis('Serving Locally'), 5)
            w.writeline(serving_options['django']['instructions'])
            w.writeline(serving_options['django']['serve_command'])
            w.writeline(serving_options['django']['hosting'])

        elif args.pyramid:
            # GETTING STARTED: Serving the App (Pyramid)
            w.write_heading(mg.emphasis('Serving Locally'), 5)
            w.writeline(serving_options['pyramid']['instructions'])
            w.writeline(serving_options['pyramid']['serve_command'])
            w.writeline(serving_options['pyramid']['hosting'])

        elif args.flask:
            # GETTING STARTED: Serving the App (Flask)
            w.write_heading(mg.emphasis('Serving Locally'), 5)
            w.writeline(serving_options['flask']['instructions'])
            w.writeline(serving_options['flask']['serve_command'])
            w.writeline(serving_options['flask']['hosting'])

        # TESTS: Running & Files
        w.write_heading('Test Suite', 3)
        w.write_hrule()
        if len(test_dict.keys()) > 0:
            w.write_heading(mg.emphasis('Running Tests'), 5)
            if args.django:
                w.writeline('This is a Django application, and therefore to run tests, run the following command at the same level as `./manage.py`.')
                w.writeline()
                w.writeline('`./manage.py test`')
            else:
                w.writeline('This application uses {} as a testing suite. To run tests, run:'.format(mg.link(test_options[testing_mod][0], testing_mod)))
                w.writeline()
                w.writeline('`{}`'.format(test_options[testing_mod][1]))
                w.writeline()
                w.writeline('To view test coverage, run:')
                w.writeline()
                w.writeline('`{}`'.format(test_options[testing_mod][2]))

            w.write_heading(mg.emphasis('Test Files'), 5)
            w.writeline('The testing files for this project are:')
            w.writeline()
            test_table = mg.Table()
            test_table.add_column('File Name', mg.Alignment.CENTER)
            test_table.add_column('Description', mg.Alignment.CENTER)
            for key, val in test_dict.items():
                test_table.append('`{}`'.format(key), val)
            w.write(test_table)
        else:
            w.writeline('This repository contains no tests.')

        # URLS - table
        if args.django or args.pyramid or args.flask:
            w.write_heading('URLs', 3)
            w.write_hrule()
            w.writeline('The URLS for this project can be found in the following modules:')
            w.writeline()
            urls_table = mg.Table()
            urls_table.add_column('URL module', mg.Alignment.CENTER)
            urls_table.add_column('Description', mg.Alignment.CENTER)
            for key, val in url_dict.items():
                urls_table.append(key, val)
            w.write(urls_table)

        # APPLICATIONS (Django) -v
        if args.django and args.verbose:
            w.write_heading('Django Apps', 3)
            w.write_hrule()
            models_list = mg.List()
            for model in settings_dict['INSTALLED_APPS']:
                if "django.contrib" not in model and "storages" not in model:
                    models_list.append(model)
            w.write(models_list)

        # APPLICATIONS (Pyramid)
        if args.pyramid:
            w.write_heading('Pyramid Development Files', 3)
            w.write_hrule()
            w.writeline('Development files specific to the Pyramid web framework can be found in the following files:')
            pyr_table = mg.List()
            for key, val in pyramid_info.items():
                pyr_table.append(key)
            w.write(pyr_table)

        # TOOLS
        w.write_heading('Development Tools', 3)
        w.write_hrule()
        tools_list = mg.List()
        tools_list.append('{} - programming language'.format(mg.emphasis('python')))
        if os.path.isfile('requirements.txt'):
            with open('requirements.txt', 'r') as f:
                reqs = []
                for line in f:
                    line = line.strip()
                    reqs.append(line)
            reqs = [i.split('==')[0] for i in reqs]
            for package in reqs:
                if package.lower() in frameworks:
                    tools_list.append('{} - web framework'.format(mg.emphasis(package.lower())))
                elif package.lower() in dbms:
                    tools_list.append('{} - DB management system'.format(mg.emphasis(package.lower())))
        w.write(tools_list)

        if args.verbose:
            # CONTRIBUTIONS
            w.write_heading('Contributions', 3)
            w.write_hrule()
            w.writeline('If you wish to contribute to this project, please contact {}.'.format(setup_dict['author_email']))

        # LICENSE
        w.write_heading('License', 3)
        w.write_hrule()
        w.writeline(license)

        # ACKNOWLEDGEMENTS
        w.write_heading('Acknowledgements', 3)
        w.write_hrule()
        shoutouts = mg.List()
        shoutouts.append('Coffee')
        w.write(shoutouts)

        w.writeline(mg.emphasis('This README was generated using ' + mg.link('https://github.com/chelseadole/write-me', 'writeme.')))
    print("""

        README generated.

        User TODOs:
            * Add application highlights to bullet-point "Features" section
            * Add correct contributor Github URL links to "Authors" section
            * Populate "Acknowledgements" section

        Please review your new README, and complete any sections that require additional user input.

        """)
if __name__ == "__main__":
    main()
