#!/usr/bin/python3
"""New class file_storage"""

from models.base_model import BaseModel
import os
import json



class FileStorage:
    """New class file_storage"""
    __file_path = "file.json"
    #guarda todos los objetos en formato diccionario
    #diccionario de diccionarios
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        __objects.append(obj.to_dict)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        import json
        with open("__file_path", "a") as file:
            json.dump(self._objects, file, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        pass



