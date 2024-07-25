import random
import string
from typing import Optional

def generate_id(length: Optional[int] = 8) -> str:
  return "".join(random.choices(string.digits + string.ascii_lowercase, k=length))