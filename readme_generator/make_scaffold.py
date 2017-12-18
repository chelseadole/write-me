"""Module to create README.md file with basic scaffold, using markdown_generator."""
import markdown_generator as mg
import os

from scaffold_options import test_options, serving_options

os.system('rm README.md')
os.system('touch README.md')

if __name__ == '__main__':
    with open('README.md', 'w') as f:
        w = mg.Writer(f)
        w.write_heading('Project Title', 1)
        w.write_hrule()

        # Description and Key Features
        w.writeline('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        key_features = mg.List()
        key_features.append('Feature #1')
        key_features.append('Feature #2')
        key_features.append('Feature #3')
        w.write(key_features)

        # AUTHORS
        w.write_heading('Authors', 3)
        w.write_hrule()
        authors = mg.List()
        authors.append(mg.link('www.github.com/chelseadole', 'Person1'))
        authors.append(mg.link('www.github.com/chelseadole', 'Person2'))
        authors.append(mg.link('www.github.com/chelseadole', 'Person3'))
        w.write(authors)

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
        w.writeline('First, clone the project repo from Github. Then, change directories into the cloned repository, create a new virtual environment, and install the repo requirements into your VE. To accomplish this, execute these commands:')
        w.writeline()
        w.writeline('`$ git clone https://github.com/chelseadole/write-me.git`')
        w.writeline('`$ cd write-me`')
        w.writeline()
        w.writeline('Now now that you have cloned your repo and changed directories into the project, create a virtual environment, and download the project requirements into your VE.')
        w.writeline()
        w.writeline('`$ python3 -m venv ENV`')
        w.writeline('`$ source ENV/bin/activate`')
        w.writeline('`$ pip install -r requirements.txt`')

        # GETTING STARTED: Serving the App
        w.write_heading(mg.emphasis('Serving Locally'), 5)
        w.writeline('Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `manage.py`:')
        w.writeline('`$ ./manage.py runserver`')
        w.writeline('Once you have executed this command, open your browser, and go to `localhost:8000/`.')

        # TESTS: Running & Files
        w.write_heading('Test Suite', 3)
        w.write_hrule()
        w.write_heading(mg.emphasis('Running Tests'), 5)
        w.writeline('This application uses pytest as a testing suite. To run tests, run:')
        w.writeline()
        w.writeline('`$ pytest`')
        w.writeline()
        w.writeline('To view test coverage, run:')
        w.writeline()
        w.writeline('`$ pytest --cov`')

        w.write_heading(mg.emphasis('Test Files'), 5)
        w.writeline('The testing files for this project are:')
        test_files = mg.List()
        test_files.append('`imager_images/tests.py`')
        test_files.append('`imager_profiles/tests.py`')
        test_files.append('`imager_api/tests.py`')
        w.write(test_files)

        # URLS - table
        w.write_heading('URLs', 3)
        w.write_hrule()
        w.writeline('The URLs for this project are:')
        w.writeline()
        urls_table = mg.Table()
        urls_table.add_column('URL', mg.Alignment.CENTER)
        urls_table.add_column('Description', mg.Alignment.CENTER)
        urls_table.append('`/images`', 'Library of all images')
        urls_table.append('`/images/edit`', 'Edit view for a single image')
        urls_table.append('`/images/add`', 'Add form for a new image')
        w.write(urls_table)

        # TOOLS
        w.write_heading('Built With', 3)
        w.write_hrule()
        tools_list = mg.List()
        tools_list.append('Django')
        tools_list.append('Postgres')
        tools_list.append('Python')
        tools_list.append('MongoDB')
        w.write(tools_list)

        # CONTRIBUTIONS
        w.write_heading('Contributions', 3)
        w.write_hrule()
        w.writeline('If you wish to contribute to this project, please contact NAME1 or NAME2.')

        # LICENSE
        w.write_heading('License', 3)
        w.write_hrule()
        w.writeline('This project is licensed under the MIT License - see the LICENSE.md file for details.')

        # ACKNOWLEDGEMENTS
        w.write_heading('Acknowledgements', 3)
        w.write_hrule()
        shoutouts = mg.List()
        shoutouts.append('Nicholas Hunt-Walker')
        shoutouts.append('Coffee')
        w.write(shoutouts)
