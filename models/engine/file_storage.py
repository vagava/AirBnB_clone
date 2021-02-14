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
        key=str(obj.__class__.__name__)+"."+str(obj.id)
        self.__objects[key]= obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        new_dict = self.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        with open("file.json", "a") as file:
            json.dump(new_dict, file, indent=4)


    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        dict_reload={}
        reload_obj = BaseModel()
        try:
            with open(FileStorage.__file_path) as file:
                dict_reload = json.load(file)
                self.__objects = reload_obj(dict_reload)
            return self.__objects
        except: pass
