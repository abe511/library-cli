import os
import unittest
from unittest.mock import patch
from typing import List, Any
from src.csvdb import CSVdb
from src.library import Library
from src.book import Book

class TestLibrary(unittest.TestCase):

  def setUp(self) -> None:
    self.db_file = "test_db.csv"
    self.fields = ["id", "title", "author", "year", "status"]
    self.db = CSVdb(filename=self.db_file, fields=self.fields)
    self.lib = Library(db=self.db)


  def tearDown(self) -> None:
    if os.path.exists(self.db_file):
      os.remove(self.db_file)


  @patch("builtins.input", return_value="test input")
  def test_get_user_input_text(self, mock_input) -> None:
    value = self.lib.get_user_input("prompt 1: ", "prompt2: ")
    self.assertEqual(value, "test input")


  @patch("builtins.input", return_value="1234")
  def test_get_user_input_number(self, mock_input) -> None:
    value = self.lib.get_user_input("prompt 1: ", "prompt2: ", type="number")
    self.assertEqual(value, 1234)


  @patch("builtins.input", return_value="")
  def test_get_user_input_optional(self, mock_input) -> None:
    value = self.lib.get_user_input("prompt 1: ", "prompt2: ", optional=True)
    self.assertEqual(value, None)


if __name__ == "__main__":
  unittest.main()