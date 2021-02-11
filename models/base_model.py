#!/usr/bin/python3
"""New class Basemodel"""

import uuid
import datetime
import time

class BaseModel():
    """New class Basemodel"""

    def __init__(self):
        """constructor class Basemodel"""
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    @property
    def id(self):
        return str(self.__id)

    @id.setter
    def id(self, value):
        self.__id = str(value)

    def __str__ (self):
        """ str representationf Basemodel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.__id,
                                        self.__dict__)

    def save(self):
        """ clss method that update the  Basemodel"""
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def to_dict(self):
        """ clss method that return the dictionary of a Basemodel"""
        new_dict = self.__dict__.copy()
        for old_key, value in self.__dict__.items():
            if "_BaseModel__" not in old_key:
                continue
            new_key = old_key.replace("_BaseModel__", "")
            new_dict[new_key] = self.__dict__[old_key]
            new_dict.pop(old_key)
            new_dict["__class__"] = self.__class__.__name__
        return new_dict
