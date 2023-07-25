#!/usr/bin/python3
"""
This module contains the User class that inherits from BaseModel.
"""

from models.base_model import BaseModel  # Import BaseModel

# Define the User class that inherits from BaseModel


class User(BaseModel):
    """User class inheriting from BaseModel"""

    # Define class attributes with default values
    email = ""  # Public class attribute, should be a string
    password = ""  # Public class attribute, should be a string
    first_name = ""  # Public class attribute, should be a string
    last_name = ""  # Public class attribute, should be a string
