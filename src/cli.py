import os
import sys
from src.library import Library

class Cli:

  def __init__(self, library: Library) -> None:
    self.lib = library
    self.cmd = "clear" if os.name == "posix" else "cls"


  def run(self) -> None:
    """
      Run the main loop.
    """
    os.system(self.cmd)
    self.show_menu()

    while True:
      user_input: str = input("> ").strip()
      self.match_input(user_input)


  def match_input(self, user_input: str) -> None:
    """
      Execute user commands.
    """
    os.system(self.cmd)
    match user_input:
      case "1":
        print("\tДобавить книгу")
        self.lib.add_book()
      case "2":
        print("\tУдалить книгу")
        self.lib.remove_book()
      case "3":
        print("\tПоиск")
        self.lib.search_book()
      case "4":
        print("\tПоказать все книги")
        self.lib.show_books()
      case "5":
        print("\tИзменить статус книги")
        self.lib.change_status()
      case "6":
        sys.exit(0)
      case _:
        self.show_menu()


  def show_menu(self) -> None:
    """
      Display the main menu.
    """
    print("Выберите действие (1-6):")
    print("1 Добавить книгу")
    print("2 Удалить книгу")
    print("3 Поиск")
    print("4 Показать все книги")
    print("5 Изменить статус книги")
    print("6 Выйти")
