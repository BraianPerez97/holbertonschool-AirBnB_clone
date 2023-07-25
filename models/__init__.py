#!/usr/bin/python3
"""This module creates an instance of FileStorage."""

# Import the FileStorage class
from models.engine.file_storage import FileStorage
storage = FileStorage()  # Create an instance of FileStorage
storage.reload()  # Load objects from the file
