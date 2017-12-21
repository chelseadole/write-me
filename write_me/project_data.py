"""Get the gihub url of a project."""

import re


def get_user_name(url):
    """Extract user name from the project url."""
    regex = re.compile(r':(.+?)/')
    result = re.search(regex, url)
    return result.group(1)


def get_project_name(url):
    """Extract project name from the project url."""
    regex = re.compile(r'/(.+?)\.')
    result = re.search(regex, url)
    return result.group(1)


def get_user_profile_url(user):
    """Return project user's github profile url."""
    return 'http://github.com/{}'.format(user)


def get_project_url():
    """Open .git/config file and git the url from it."""
    project_info = {}

    with open('./.git/config', 'r') as git_config:
        for line in git_config:
            # import pdb; pdb.set_trace()
            if "url = git@" in line or "url = https" in line:
                dont_need, need = line.split(' = ')
                url = need.strip()
                project_info['url'] = url

    project_user = get_user_name(url)
    project_info['project_user'] = project_user
    project_name = get_project_name(url)
    project_info['project_name'] = project_name
    project_user_profile_url = get_user_profile_url(project_user)
    project_info['project_user_profile_url'] = project_user_profile_url

    return project_info


if __name__ == '__main__':
    info = get_project_url()
    for i in info:
        print(i, info[i])
