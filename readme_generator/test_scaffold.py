"""Test file for ensure scaffolding functionality."""
import os

from unittest import TestCase

from unittest.mock import patch

import pytest

from .make_scaffold import main, overwrite


class TestScaffold(TestCase):
    """Scaffold class for testing inputs and file creation."""

    def test_overwrite_input_no(self):
        """Test overwrite function if no entered."""
        with patch('builtins.input', side_effect=['n', 'no']):
            assert overwrite() == 'README.md.new'

    def test_overwrite_input_yes(self):
        """Test overwrite function if yes entered."""
        with patch('builtins.input', side_effect=['y', 'yes']):
            assert overwrite() == 'README.md'

    def test_main_returns_succcess_text(self):
        """Test success test returned when main is called."""
        with patch('builtins.input', side_effect='y'):
            assert main() == 'README generated.'
