from typing import List, Dict, Union, Any
from .book import Book
from .csvdb import CSVdb

class Library:

  def __init__(self, db: CSVdb) -> None:
    self.books = db.get_all()
    self.db = db


  def get_user_input(self, prompt: str, msg: str, type: str = "text", optional: bool = False) -> Union[str, int]:
    """
      Get user input for text and number fields.
      Try only once if input is optional.
      Return validated input.
    """
    while True:
      user_input = input(prompt).strip() 
      prompt = msg
      try:
        if user_input == "":
          raise ValueError
        elif type == "number":
          value = int(user_input)
        else:
          value = user_input
        break
      except ValueError:
        if optional:
          return
        continue
    return value


  def get_id(self) -> Union[str, None]:
    """
      Get the `id` from user input and check it against the db.
      Return the `id`.
    """
    retry = 3
    is_found = False

    while retry:
      retry -= 1
      id: str = self.get_user_input("Идентификационный номер: ", "Пожалуйста, введите идентификационный номер книги: ")
      is_found = self.search_book_by_id(id)
      if not is_found and retry > 0:
        print("Неверный идентификационный номер. Попробуйте ещё раз")
      else:
        break

    if retry == 0 and not is_found:
      print("Неверный идентификационный номер. Пожалуйста, воспользуйтесь поиском")
      return
    return id


  def add_book(self) -> None:
    """
      Add a book to db. 
      Get user input for `title`, `author` and `year`.
      Construct the book and write to the db.
    """
    title = self.get_user_input("Название: ", "Пожалуйста, введите название: ")
    author = self.get_user_input("Автор: ", "Пожалуйста, введите полное имя автора: ")
    year = self.get_user_input("Год: ", "Пожалуйста, введите год издания: ", type="number")

    new_book = Book(title=title, author=author, year=year)
    response = self.db.add(new_book.__dict__)
    if response != "OK":
      print("Ошибка при записи")
      return
    print("Книга добавлена")


  def remove_book(self) -> None:
    """
      Remove the book from the db.
      Get the `id` from user and send a remove request.
    """
    id: str = self.get_id()
    if id:
      response = self.db.remove(id)
      if response:
        print(f"Книга удалена")
      else:
        print(f"Книга не найдена")


  def search_book(self) -> None:
    """
      Search books by `title`, `author` or `year`.
      Get optional user input and return matching records.
      Return empty list if no input provided. 
    """

    title = self.get_user_input("Название: ", "Пожалуйста, введите название: ", optional=True)
    author = self.get_user_input("Автор: ", "Пожалуйста, введите полное имя автора: ", optional=True)
    year = self.get_user_input("Год: ", "Пожалуйста, введите год издания: ", type="number", optional=True)

    if title == None and author == None and year == None:
      print("Нет результатов")
      return

    data = self.db.read()
    results = []
    if title is not None:
      title = title.lower()
    if author is not None:
      author = author.lower()

    for row in data:
      if (((title is None) or (title in row["title"].lower())) and
        ((author is None) or (author in row["author"].lower())) and
        ((year is None) or (int(row["year"]) == year))):
        results.append(row)
    if not results:
      print("Нет результатов")
      return
    self.show_books(results)


  def show_books(self, data: List[Book] = None) -> List[Book]:
    """
      Get the list of all books and print it in a nice format.
    """
    if not data:
      data = self.db.get_all()
    print(f"ID \tСтатус \tГод \tАвтор \tНазвание")
    for row in data:
      print(f'{row["id"]}  {row["status"]} \t{row["year"]} \t{row["author"]} \t{row["title"]}')


  def search_book_by_id(self, id: str) -> bool:
    """
      Check if the book with provided `id` exists.
    """
    data = self.db.get_all()
    for row in data:
      if row["id"] == id:
        return True
    return False


  def change_status(self) -> Union[Dict[Any, Any], Exception]:
    """
      Change book `status`.
      Get the `id` from user input and search the book.
      Get the `status` from user and modify it if the book is found.

      Statuses:
      * 1 - в наличии
      * 2 - выдана
    """
    id: str = self.get_id()
    new_status: str = self.get_user_input("Статус (1 - в наличии | 2 - выдана): ", "Пожалуйста, введите статус (1 - в наличии | 2 - выдана): ")

    if new_status not in ["1", "2", "в наличии", "выдана"]:
      print("Неверный статус")
      return

    status_codes = {"1": "в наличии", "2": "выдана"}
    if new_status in ["1", "2"]:
      new_status = status_codes[new_status]
    response = self.db.update(id, {"status": new_status})

    if response:
      print(f'Статус книги изменён на "{new_status}"')
    else:
      print(f'Не удалось сменить статус книги')
