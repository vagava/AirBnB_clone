#!/usr/bin/python3
""" Class Place"""

import uuid
import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place"""
    name = ""
    state_id = ""
    user_id = ""
