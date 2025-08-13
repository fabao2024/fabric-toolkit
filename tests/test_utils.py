import unittest
from unittest.mock import patch, mock_open
from toolkit import utils

class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_load_translation_success(self, mock_file):
        # Arrange
        lang = "en"

        # Act
        data = utils.load_translation(lang)

        # Assert
        mock_file.assert_called_once_with(f"toolkit/locales/{lang}.json", "r", encoding="utf-8")
        self.assertEqual(data, {"key": "value"})

    @patch("builtins.open", side_effect=[FileNotFoundError, mock_open(read_data='{"default": "value"}').return_value])
    def test_load_translation_fallback(self, mock_file):
        # Arrange
        lang = "fr" # A language that doesn't exist

        # Act
        data = utils.load_translation(lang)

        # Assert
        self.assertEqual(mock_file.call_count, 2)
        mock_file.assert_any_call("toolkit/locales/fr.json", "r", encoding="utf-8")
        mock_file.assert_any_call("toolkit/locales/en.json", "r", encoding="utf-8")
        self.assertEqual(data, {"default": "value"})

if __name__ == '__main__':
    unittest.main()
