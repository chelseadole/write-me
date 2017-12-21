# """Test file for ensure scaffolding functionality."""
# import os

# import tempfile

# from unittest import TestCase

# from unittest.mock import patch

# from readme_generator.make_scaffold import main, overwrite


# class TestScaffold(TestCase):
#     """Scaffold class for testing inputs and file creation."""

#     def test_overwrite_input_no(self):
#         """Test overwrite function if no entered."""
#         with tempfile.TemporaryDirectory() as test_dir:
#             os.chdir(test_dir)
#             f = tempfile.NamedTemporaryFile()
#             f.name = 'README.md'
#             with patch('builtins.input', side_effect=['n', 'no']):
#                 assert overwrite() == 'README.md.new'

#     def test_overwrite_input_yes(self):
#         """Test overwrite function if yes entered."""
#         with tempfile.TemporaryDirectory() as test_dir:
#             os.chdir(test_dir)
#             f = tempfile.NamedTemporaryFile()
#             f.name = 'README.md'
#             with patch('builtins.input', side_effect=['y', 'yes']):
#                 assert overwrite() == 'README.md'

#     def test_main_returns_succcess_text(self):
#         """Test success test returned when main is called."""
#         with tempfile.TemporaryDirectory() as test_dir:
#             os.chdir(test_dir)
#             f = tempfile.NamedTemporaryFile()
#             f.name = 'README.md'
#             try:
#                 with patch('builtins.input', return_value='y'):
#                     assert main() == 'README generated.'
#             except Exception as e:
#                 return e

#     def test_overwrite_user_prompt(self):
#         """Test overwrite prompts user with yes/no question."""
#         with tempfile.TemporaryDirectory() as test_dir:
#             os.chdir(test_dir)
#             f = tempfile.NamedTemporaryFile()
#             f.name = 'README.md'
#             assert overwrite('n') == 'README.md.new'
