"""Test project data module."""
from write_me.project_data import (get_project_name,
                                   get_project_url,
                                   get_user_name,
                                   get_user_profile_url)


def test_get_user_name():
    """Test username function for project url."""
    user = get_user_name('https://github.com/chelseadole/write-me')
    assert user == 'chelseadole'


def test_get_user_name_not_contributor():
    """Test username function does not return contributor to repo."""
    user = get_user_name('https://github.com/chelseadole/write-me')
    assert user != 'famavott'


def test_get_project_name():
    """Test to see if project name is grabbed from github."""
    project = get_project_name('https://github.com/chelseadole/write-me')
    assert project == 'write-me'


def test_get_user_profile_url():
    """Test to get user profile url associated with repo."""
    url = get_user_profile_url('famavott')
    assert url == 'https://github.com/famavott'


def test_get_project_url():
    """Test to ensure dict is returned."""
    assert type(get_project_url()) is dict


def test_keys_in_project_url():
    """Test project url keys."""
    project = get_project_url()
    assert project['project_user'] == 'chelseadole'
