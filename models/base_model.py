#!/usr/bin/python3
"""
This module contains the BaseModel class which will be the base class for
other classes.
"""

# We import the uuid module to generate unique IDs
import uuid
# We import the datetime module to manage dates and times
from datetime import datetime
import models


class BaseModel:
    """
    A base class that defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        This method is called when a new instance of the class is created.
        If kwargs is not empty, assigns attributes based on kwargs.
        Otherwise, assigns unique id and the current date/time.
        """
        # Generate a unique ID for the instance
        self.id = str(uuid.uuid4())
        # Get the current date and time for created_at
        self.created_at = datetime.now()
        # updated_at is the same as created_at when the instance is created
        self.updated_at = self.created_at

        if kwargs:  # Instance is created from dictionary
            # Iterate through dictionary items
            for key, value in kwargs.items():
                # Convert string to datetime for these keys
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # Ignore the __class__ key
                if key != '__class__':
                    # Set attribute on instance with key-value pair.
                    setattr(self, key, value)

        else:
            # Import storage and add the new object to it
            models.storage.new(self)

    def __str__(self):
        """
        This method returns a string representation of the instance.
        """
        # Return a formatted string containing the class name, the ID,
        # and the dictionary of the instance attributes.
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the 'updated_at' attribute with the current date
        and time.
        """
        # Update the updated_at attribute
        self.updated_at = datetime.now()
        # Save the instance to storage
        models.storage.save()

    def to_dict(self):
        """
        This method returns a dictionary containing all keys/values of the
        instance's __dict__.
        """

        # Make a copy of the __dict__ dictionary
        dict_copy = self.__dict__.copy()

        # Add the class name to the dictionary
        dict_copy["__class__"] = self.__class__.__name__

        # Convert 'created_at' and 'updated_at' to strings in ISO format
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        # Return the dictionary
        return dict_copy
