"""Get the gihub url of a project."""

import re


def get_user_name(url):
    """Extract user name from the project url."""
    regex = re.compile(r'github\.com/(.+?)/')
    result = re.search(regex, url)
    return result.group(1)


def get_project_name(url):
    """Extract project name from the project url."""
    regex = re.compile(r'https://github.com/.+?/(.+$)')
    result = re.search(regex, url)
    return result.group(1)


def get_user_profile_url(user):
    """Return project user's github profile url."""
    return 'https://github.com/{}'.format(user)


def get_project_url():
    """Open .git/config file and git the url from it."""
    project_info = {}
    with open('./.git/config', 'r') as git_config:
        for line in git_config:
            if "url = git@" in line:
                dont_need, need = line.split(' = ')
            if "url = git@" in line:
                dont_need, need = line.split('@')
                url = need.strip()
                url = url.replace(':', '/')
                url = url.rstrip('.git')
                url = url.replace(url, 'https://' + url)
                project_info['url'] = url
                break
            elif "url = https://github.com" in line:
                dont_need, need = line.split(' = ')
                url = need.rstrip(".git")
                project_info['url'] = url
                break

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
