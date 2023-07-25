#!/usr/bin/python3
"""Module containing the Place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits from BaseModel """
    city_id = ""  # It will be the City.id
    user_id = ""  # It will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]  # It will be the list of Amenity.id later
