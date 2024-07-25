from dataclasses import dataclass, field
from typing import Optional
from utils import generate_id

@dataclass
class Book:
  title: str
  author: str
  year: int
  book_id: str = field(default_factory=generate_id)
  status: str = field(default="в наличии")
  
  def __str__(self) -> str:
    return f"{self.book_id}: {self.year}, {self.author}, {self.title} - {self.status}"

  def change_status(self, status: Optional[str] = "выдана") -> None:
    self.status = status

