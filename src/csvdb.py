from typing import List, Dict, Optional, Any
import csv
import os

class CSVdb:

  def __init__(self, filename: str, fields: List[str]) -> None:
    self.db_file = filename
    self.fields = fields

  # read file to object
  # return data or empty object
  def read(self) -> List[Any]:
    if os.path.exists(self.db_file):
      with open(self.db_file, "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
      return data
    return []

  # write header if no such file or file opened in "w" mode
  # append data by default
  def write(self, data: List[Dict[Any, Any]], mode: Optional[str] = "a") -> None:
    file_exists = os.path.isfile(self.db_file)
    with open(self.db_file, mode, newline="") as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames=self.fields)
      if not file_exists or mode == "w":
        writer.writeheader()
      writer.writerows(data)

  # read file
  # if id not found add new record
  # write to file
  def add(self, new_data: Dict[Any, Any]) -> bool:
    data = self.read()
    for row in data:
      if row["id"] == new_data["id"]:
        return False
    self.write([new_data])
    return True

  def get_all(self) -> List[Any]:
    return self.read()

  # read file
  # find the record by id
  # update necessary fields
  # write to file
  # return the updated record
  def update(self, id: str, update_data: Dict[Any, Any]) -> Dict[Any, Any]:
    data = self.read()
    updated_record = {}
    for row in data:
      if row["id"] == id:
        for k, v in update_data.items():
          row[k] = v
        updated_record = row
    self.write(data, "w")
    return updated_record

  # read file
  # filter data
  # write to file
  # return status
  def remove(self, id: str) -> bool:
    data = self.read()
    filtered_data = [row for row in data if row["id"] == id]
    if len(filtered_data) < len(data):
      self.write(filtered_data, "w")
      return True
    return False
