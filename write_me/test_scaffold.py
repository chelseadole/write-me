# """Test file for ensure scaffolding functionality."""
# import os

# import tempfile

# from unittest import TestCase
# import markdown_generator as mg

# from unittest.mock import patch

# from readme_generator.make_scaffold import user_data, license, setup_dict, dependencies


# class TestScaffold(TestCase):
#     """Scaffold class for testing inputs and file creation."""

#     # def test_overwrite_input_no(self):
#     #     """Test overwrite function if no entered."""
#     #     with tempfile.TemporaryDirectory() as test_dir:
#     #         os.chdir(test_dir)
#     #         f = tempfile.NamedTemporaryFile()
#     #         f.name = 'README.md'
#     #         with patch('builtins.input', side_effect=['n', 'no']):
#     #             assert overwrite() == 'README.md.new'

#     # def test_overwrite_input_yes(self):
#     #     """Test overwrite function if yes entered."""
#     #     with tempfile.TemporaryDirectory() as test_dir:
#     #         os.chdir(test_dir)
#     #         f = tempfile.NamedTemporaryFile()
#     #         f.name = 'README.md'
#     #         with patch('builtins.input', side_effect=['y', 'yes']):
#     #             assert overwrite() == 'README.md'

#     # def test_main_returns_succcess_text(self):
#     #     """Test success test returned when main is called."""
#     #     with tempfile.TemporaryDirectory() as test_dir:
#     #         os.chdir(test_dir)
#     #         f = tempfile.NamedTemporaryFile()
#     #         f.name = 'README.md'
#     #         try:
#     #             with patch('builtins.input', return_value='y'):
#     #                 assert main() == 'README generated.'
#     #         except Exception as e:
#     #             return e

#     # def test_overwrite_user_prompt(self):
#     #     """Test overwrite prompts user with yes/no question."""
#     #     with tempfile.TemporaryDirectory() as test_dir:
#     #         os.chdir(test_dir)
#     #         f = tempfile.NamedTemporaryFile()
#     #         f.name = 'README.md'
#     #         assert overwrite('n') == 'README.md.new'

#     def test_user_data_populated_in_make_scaffold(self):
#         """Test that make_scaffold creates a populated user_data dict."""
#         assert len(user_data) > 0
#         assert "url" in user_data.keys()

#     def test_make_scaffold_creates_license(self):
#         """Test that make_scaffold creates a populated license."""
#         assert isinstance(license, str)
#         assert "license" in license

#     def test_make_scaffold_creates_setup_dict_and_contains_info(self):
#         """Test that setup_dict is created successfully in make_scaffold."""
#         assert isinstance(setup_dict, dict)
#         assert "version" in setup_dict.keys()
#         assert isinstance(setup_dict['author'], list)

#     def test_dependencies_are_gathered(self):
#         """Test that dependencies are gathered."""
#         assert isinstance(dependencies, list)
#         assert len(dependencies) > 0
