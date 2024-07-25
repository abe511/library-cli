import unittest
import re
from src.utils import generate_id

class TestGenerateId(unittest.TestCase):
  
  def test_generate_id(self):
    self.assertIsInstance(generate_id(), str)
  
  def test_id_length(self):
    lengthyId = generate_id(16)
    self.assertEqual(len(lengthyId), 16)

  def test_characters(self):
    pattern = re.compile(r"^[a-z0-9]+$")
    self.assertIsNotNone(pattern.match(generate_id()), "The generated string does not match the pattern")