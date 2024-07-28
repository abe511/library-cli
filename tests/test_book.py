import unittest
import re
from src.book import Book, generate_id

class TestBook(unittest.TestCase):
  
  def setUp(self):
    self.book = Book(title="Название книги", author="Автор книги", year=1234)


  def test_book_initialization(self):
    self.assertEqual(self.book.title, "Название книги")
    self.assertEqual(self.book.author, "Автор книги")
    self.assertEqual(self.book.year, 1234)
    self.assertEqual(self.book.status, "в наличии")
    self.assertIsInstance(self.book.id, str)


  def test_str_representation(self):
    expected = f"{self.book.id}: 1234, Автор книги, Название книги - в наличии"
    self.assertEqual(str(self.book), expected)


  def test_change_status(self):
    self.assertEqual(self.book.status, "в наличии")
    self.book.change_status()
    self.assertEqual(self.book.status, "выдана")
    self.book.change_status()
    self.assertEqual(self.book.status, "в наличии")


  def test_generate_id(self):
    self.assertIsInstance(generate_id(), str)


  def test_id_length(self):
    id_string = generate_id(16)
    self.assertEqual(len(id_string), 16)


  def test_characters(self):
    pattern = re.compile(r"^[a-z0-9]+$")
    self.assertIsNotNone(pattern.match(generate_id()), "The generated string does not match the pattern")


if __name__ == "__main__":
  unittest.main()