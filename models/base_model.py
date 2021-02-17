#!/usr/bin/python3
""" Metodo basemodel"""

import uuid
import datetime
import models


class BaseModel():
    """New class Basemodel"""

    def __init__(self, *args, **kwargs):
        """constructor class Basemodel"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ str representationf Basemodel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id,
                                        self.__dict__)

    def save(self):
        """ clss method that update the  Basemodel"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()
        return self.updated_at

    def to_dict(self):
        """ clss method that return the dictionary of a Basemodel"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict
