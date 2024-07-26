from dataclasses import dataclass, field
try:
    from utils import generate_id
except ImportError:
    from .utils import generate_id


@dataclass
class Book:
  title: str
  author: str
  year: int
  id: str = field(default_factory=generate_id)
  status: str = field(default="в наличии")
  
  def __str__(self) -> str:
    return f"{self.id}: {self.year}, {self.author}, {self.title} - {self.status}"

  def change_status(self) -> None:
    if self.status == "выдана":
      self.status = "в наличии"
      return
    self.status = "выдана"

