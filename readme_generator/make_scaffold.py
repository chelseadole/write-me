"""Module to create README.md file with basic scaffold, using markdown_generator."""
import markdown_generator as mg
import os

# from gather_data import models, apps, tests, basic_data
# data necessary = ['Project Title']
os.system('rm README.md')
os.system('touch README.md')

if __name__ == '__main__':
    with open('README.md', 'w') as f:
        writer = mg.Writer(f)
        writer.write_heading('Project Title', 1)
        writer.write_hrule()

        # Description and Key Features
        writer.writeline('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        key_features = mg.List()
        key_features.append('Feature #1')
        key_features.append('Feature #2')
        key_features.append('Feature #3')
        writer.write(key_features)

        # Project Download/"Getting Started" Instructions
        writer.write_heading('Getting Started', 3)
        writer.write_heading('Installation', 4)
        writer.writeline('First, clone the project repo from Github. Then, change directories into the cloned repository, create a new virtual environment, and install the repo\'s requirements into your VE. To accomplish this, execute these commands:')
        writer.writeline()
        writer.writeline('`$ git clone https://github.com/chelseadole/write-me.git`')
        writer.writeline('`$ cd write-me`')
        writer.writeline('`$ python3 -m venv ENV`')
        writer.writeline('`$ source ENV/bin/activate`')
        writer.writeline('`$ pip install -r requirements.txt`')

        # Serving the App
        writer.write_heading('Serving Locally', 4)
        writer.writeline('Once you have cloned the application and installed the requirements, you can serve the project on your local machine. Once you have executed this command, open your browser, and go to `http://localhost:8000/`')
        writer.writeline('`$ ./manage.py runserver')
