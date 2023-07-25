#!/usr/bin/python3
"""This module defines a class "FileStorage" that serializes and
deserializes instances to and from a JSON file."""

import json  # We need json to convert dictionary to JSON string and vice versa
import os    # import os module used for file path operations
from models.user import User  # Import the User class
from models.state import State  # Import the State class
from models.city import City  # Import the City class
from models.amenity import Amenity  # Import the Amenity class
from models.place import Place  # Import the Place class
from models.review import Review  # Import the Review class


class FileStorage:
    """A class to manage the storage of all our instances."""

    __file_path = "file.json"  # Where we'll store and load our data
    __objects = {}  # Here we will store all objects

    def all(self):
        """Returns all objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to our storage."""
        # Create the key as <class name>.<id>
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # Add object to dictionary
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes our objects and saves them to a file."""
        # Convert objects to dict representation
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        # Open file in write mode
        with open(self.__file_path, 'w') as f:
            # Write dictionary to file as JSON
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects
        """
        # Check if file exists
        if os.path.exists(self.__file_path):
            # Open file in read mode
            with open(self.__file_path, 'r') as f:
                # Load JSON file to dictionary
                obj_dict = json.load(f)
            # Import BaseModel here to avoid circular import
            from models.base_model import BaseModel
            # Convert dict to objects and add them to __objects
            class_map = {
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
            }
            for k, v in obj_dict.item():
                class_name = v['__class__']
                if class_name in class_map:
                    cls = class_map[class_name]
                    self.__objects[k] = cls(**v)