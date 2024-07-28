import os
import unittest
from typing import List, Any
from src.csvdb import CSVdb
from src.book import Book

class TestCSVdb(unittest.TestCase):

  def setUp(self) -> None:
    self.db_file = "test_db.csv"
    self.fields = ["id", "title", "author", "year", "status"]
    self.db = CSVdb(filename=self.db_file, fields=self.fields)


  def tearDown(self) -> None:
    if os.path.exists(self.db_file):
      os.remove(self.db_file)


  def add_data(self) -> List[Any]:
    row = Book(title="Test Title", author="Test Author",year=2024, status="test status")
    self.db.add(row.__dict__)
    data = self.db.get_all()
    return data


  def test_write(self):
    self.assertEqual(os.path.exists(self.db_file), False)
    book = Book(title="Test Title", author="Test Author",year=2024, status="test status")
    new_row = [book.__dict__]
    self.db.write(new_row)
    self.assertEqual(os.path.exists(self.db_file), True)
    data = self.db.get_all()
    self.assertEqual(len(data), 1)


  def test_write_multiple_rows(self):
    self.assertEqual(os.path.exists(self.db_file), False)
    book1 = Book(title="Test Title1", author="Test Author1",year=2024, status="test status1")
    book2 = Book(title="Test Title2", author="Test Author2",year=2024, status="test status2")
    new_data = [book1.__dict__, book2.__dict__]
    self.db.write(new_data)
    self.assertEqual(os.path.exists(self.db_file), True)
    data = self.db.get_all()
    self.assertEqual(len(data), 2)


  def test_read(self) -> None:
    self.assertEqual(os.path.exists(self.db_file), False)
    row = Book(title="Test Title", author="Test Author",year=2024, status="test status")
    self.db.add(row.__dict__)
    data = self.db.read()
    self.assertEqual(os.path.exists(self.db_file), True)
    self.assertEqual(len(data), 1)


  def test_read_empty(self) -> None:
    data = self.db.get_all()
    self.assertEqual(data, [])


  def test_add(self) -> None:
    row = Book(title="Test Title", author="Test Author",year=2024, status="test status")
    self.db.add(row.__dict__)
    data = self.db.get_all()
    self.assertEqual(len(data), 1)
    test_row = row.__dict__
    self.assertEqual(data[0]["title"], test_row["title"])


  def test_update(self) -> None:
    data = self.add_data()
    self.assertEqual(len(data), 1)
    row = data[0]
    update_data = {"title": "Updated Title", "author": "Updated Author", "status": "updated status"}
    self.db.update(row["id"], update_data)
    data = self.db.get_all()
    row = data[0]
    self.assertEqual(row["title"], "Updated Title")
    self.assertEqual(row["author"], "Updated Author")
    self.assertEqual(row["status"], "updated status")


  def test_remove(self) -> None:
    data = self.add_data()
    self.assertEqual(len(data), 1)
    row = data[0]
    self.db.remove(row["id"])
    data = self.db.get_all()
    self.assertEqual(len(data), 0)


if __name__ == "__main__":
  unittest.main()