from typing import List, Dict
from book import Book

class Library:

  def __init__(self, db: List[Book]) -> None:
    self.books = db.get_all()

  def add_book(self, book: Book) -> None:
    db.add(book)

  def remove_book(self, id: str) -> None:
    db.remove(id)

  def search_book(self, term: str) -> List[Book]:
    res = db.search(term)
    return res

  def show_books(self) -> List[Book]:
    return self.books

  def change_status(self, id: str, new_status: str) -> bool:
    res = db.update(id, {"status": new_status})
    return res
