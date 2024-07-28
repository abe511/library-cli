from typing import List, Dict, Optional, Union, Any
import csv
import os

class CSVdb:

  def __init__(self, filename: str, fields: List[str]) -> None:
    self.db_file = filename
    self.fields = fields


  def read(self) -> Union[List[Any], Exception]:
    """
      Read the db file and return an object with data.
    """
    try:
      if os.path.exists(self.db_file):
        with open(self.db_file, "r", newline="") as csv_file:
          reader = csv.DictReader(csv_file)
          data = list(reader)
        return data
    except Exception as e:
      return e
    return []


  def write(self, data: List[Dict[Any, Any]], mode: Optional[str] = "a") -> Union[str, Exception]:
    """
      Write the headers and provided data to a db.\\
      Create a db file if it does not exist.\\
      Headers are not written to existing file.\\
      Append new records to a db file. (default mode)
    """
    try:
      file_exists = os.path.isfile(self.db_file)
      with open(self.db_file, mode, newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=self.fields)
        if not file_exists or mode == "w":
          writer.writeheader()
        writer.writerows(data)
        return "OK"
    except Exception as e:
      return e


  def add(self, new_data: Dict[Any, Any]) -> Union[str, Exception]:
    """
      Add a single object to db.
    """
    return self.write([new_data])


  def get_all(self) -> List[Any]:
    """
      Retrieve a list of all db records.
    """
    return self.read()


  def update(self, id: str, update_data: Dict[Any, Any]) -> Union[Dict[Any, Any], Exception]:
    """
      Update a db record with provided data.\\
      Find the record with matching `id` and create an object with updated fields.\\
      Write the updated object to db.
    """
    data = self.read()
    updated_record = {}
    for row in data:
      if row["id"] == id:
        for k, v in update_data.items():
          row[k] = v
        updated_record = row
    response = self.write(data, "w")
    if response == "OK":
      return updated_record
    return response


  def remove(self, id: str) -> bool:
    """
      Remove the record with matching `id`.\\
      Write modified data to db.
    """
    data = self.read()
    filtered_data = [row for row in data if row["id"] != id]
    if len(filtered_data) < len(data):
      self.write(filtered_data, "w")
      return True
    return False
