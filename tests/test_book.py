import unittest
from src.book import Book

class TestBook(unittest.TestCase):
  
  def setUp(self):
    self.book = Book(title="Название книги", author="Автор книги", year=1234)
  
  def test_book_initialization(self):
    self.assertEqual(self.book.title, "Название книги")
    self.assertEqual(self.book.author, "Автор книги")
    self.assertEqual(self.book.year, 1234)
    self.assertEqual(self.book.status, "в наличии")
    self.assertIsInstance(self.book.book_id, str)
  
  def test_str_representation(self):
    expected = f"{self.book.book_id}: 1234, Автор книги, Название книги - в наличии"
    self.assertEqual(str(self.book), expected)
    
  def test_change_status(self):
    self.assertEqual(self.book.status, "в наличии")
    
    self.book.change_status()
    self.assertEqual(self.book.status, "выдана")
    
    self.book.change_status()
    self.assertEqual(self.book.status, "в наличии")


if __name__ == "__main__":
  unittest.main()