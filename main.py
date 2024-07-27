from src.library import Library
from src.csvdb import CSVdb


# def match_input(user_input: str) -> None:
def match_input(user_input: str, library: Library) -> None:
  match user_input:
    case "1":
      print("\tДобавить книгу")
      library.add_book()
    case "2":
      print("\tУдалить книгу")
      library.remove_book()
    case "3":
      print("\tПоиск")
      library.search_book()
    case "4":
      print("\tПоказать все книги")
      library.show_books()
    case "5":
      print("\tИзменить статус книги")
      library.change_status()
    case "6":
      print("👋")
    case _:
      show_menu()


def show_menu() -> None:
  print("Выберите действие (1-6):")
  print("1 Добавить книгу")
  print("2 Удалить книгу")
  print("3 Поиск")
  print("4 Показать все книги")
  print("5 Изменить статус книги")
  print("6 Выйти")


def main() -> None:
  
  filename = "db.csv"
  fields = ["id", "title", "author", "year", "status"]

  db = CSVdb(filename=filename, fields=fields)

  library = Library(db)
  
  show_menu()
  
  while True:
    user_input: str = input("> ").strip()
    if user_input == "":
      continue
    
    if user_input == "6" or user_input == "exit":
      break

    match_input(user_input, library)


if __name__ == "__main__":
  main()