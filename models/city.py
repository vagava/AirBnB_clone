#!/usr/bin/python3
""" Class city"""

import uuid
import datetime
from models.base_model import BaseModel


class City(BaseModel):
    """Class city"""
    name = ""
    state_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = 0.0
