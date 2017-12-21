"""Test django settings module."""
from write_me.django_setings_info import get_settings_info


def test_django_settings_info_returns_dict():
    """Test that get settings info returns dict."""
    assert isinstance(get_settings_info(), dict)


def test_django_settings_returns_installed_apps():
    """Test that get settings info has INSTALLED_APPS key."""
    assert 'INSTALLED_APPS' in get_settings_info()


def test_django_settings_returns_installed_apps_as_list():
    """Test that installed apps are in a list."""
    info = get_settings_info()
    assert isinstance(info['INSTALLED_APPS'], list)


def test_django_settings_installed_apps_as_contains_write_me():
    """Test that installed apps has write_me app."""
    info = get_settings_info()
    assert 'write_me' in info['INSTALLED_APPS']


def test_django_settings_installed_apps_has_app_data():
    """Test that get settings info has installed apps as value."""
    info = get_settings_info()
    assert info['INSTALLED_APPS'] == ['django.contrib.admin',
                                      'django.contrib.auth',
                                      'django.contrib.contenttypes',
                                      'django.contrib.sessions',
                                      'django.contrib.messages',
                                      'django.contrib.staticfiles',
                                      'bootstrap3', 'django_write', 'write_me',
                                      'multiselectfield', 'sorl.thumbnail',
                                      'dj_database_url', 'storages'
                                      ]
