import random
from typing import List, Optional

def generate_id(length: Optional[int] = 8) -> str:
  chars: str = "0123456789abcdefghijklmnopqrstuvwxyz"
  end: int = len(chars) - 1;
  id_string: List[str] = []
  for _ in range(length):
    random_char: str = chars[random.randint(0, end)]
    id_string.append(random_char)
  return "".join(id_string)
