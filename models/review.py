#!/usr/bin/python3
"""Module containing the Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from BaseModel """
    place_id = ""  # It will be the Place.id
    user_id = ""  # It will be the User.id
    text = ""
