

def match_input(user_input: str) -> None:
  match user_input:
    case "1":
      print("1 Добавить книгу")
    case "2":
      print("2 Удалить книгу")
    case "3":
      print("3 Поиск")
    case "4":
      print("4 Показать все книги")
    case "5":
      print("5 Изменить статус книги")
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
  is_running: bool = True

  show_menu()
  
  while is_running:
    user_input: str = input("Номер: ").strip()
    if user_input == "":
      continue
    
    if user_input == "6" or user_input == "exit":
      is_running = False

    match_input(user_input)


if __name__ == "__main__":
  main()