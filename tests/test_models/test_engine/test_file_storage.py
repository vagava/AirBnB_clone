#!/usr/bin/python3
"""
test Class FileStorage
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import inspect
import pep8
import models
from datetime import datetime as datetime
import os

new_dict = {'id': '1128',
            'created_at': '2021-02-28T21:03:32.012328',
            '__class__': 'BaseModel', 'my_number': 89,
            'updated_at': '2021-02-28T21:03:54.052343',
            'name': 'Vanessa'}


class Test_FileStorage(unittest.TestCase):
    """Unitest for check the project at the class model"""
    def test_docs(self):
        """Tests docstring for module"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_class_docs(self):
        """Tests doc for class  FileStorage"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_methods_docs(self):
        """Tests docs for method FileStorage"""
        m = inspect.getmembers(FileStorage, predicate=inspect.ismethod)
        for name, func in m:
            self.assertTrue(len(func.__doc__) > 0)
        m = inspect.getmembers(FileStorage, predicate=inspect.isfunction)
        for name, func in m:
            self.assertTrue(len(func.__doc__) > 0)

    def test_storage_isinstance(self):
        """Tests if storage is an instance of FileStorage"""
        prueba = FileStorage()
        self.assertIsInstance(prueba, FileStorage)

    def test_file_json(self):
        """Tests for path existence"""
        prueba = BaseModel()
        prueba.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_method(self):
        """Checks if reload method is working"""
        self.assertTrue(models.storage.reload() is None)

    def tearDown(self):
        """Cleans the enviroment for tests"""
        if os.path.exists('file.json'):
            os.remove("file.json")
