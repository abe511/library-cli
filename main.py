import sys
import os
from src.cli import Cli
from src.library import Library
from src.csvdb import CSVdb


def main() -> None:
  """
    Run the library app.\\
    Default db file name is used if no argument is provided.
  """
  filename = sys.argv[1] if len(sys.argv) >= 2 else "db.csv"
  fields = ["id", "title", "author", "year", "status"]

  db = CSVdb(filename=filename, fields=fields)

  library = Library(db=db)
  
  cli = Cli(library=library)
  
  cli.run()


if __name__ == "__main__":
  main()