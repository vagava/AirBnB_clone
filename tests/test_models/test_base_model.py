#!/usr/bin/python3
"""
test Class BaseModel
"""
import unittest
from models.base_model import BaseModel
import inspect
import pep8
import models
from datetime import datetime as datetime


class Test_BaseModel(unittest.TestCase):
    """Unitest for check the project at the class model"""
    def test_docs(self):
        """Tests docstring for module"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_class_docs(self):
        """Tests doc for class  basemodel"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_methods_docs(self):
        """Tests docs for method basemodel"""
        m = inspect.getmembers(BaseModel, predicate=inspect.ismethod)
        for name, func in m:
            self.assertTrue(len(func.__doc__) > 0)
        m = inspect.getmembers(BaseModel, predicate=inspect.isfunction)
        for name, func in m:
            self.assertTrue(len(func.__doc__) > 0)

    def test_docstring_for_test(self):
        """Tests docstring for this test"""
        self.assertTrue(len(__doc__) > 0)

    def test_pep8(self):
        """
        Tests for PEP-8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_base_init(self):
        """
        Testing a class BaseModel
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(issubclass(type(instance), BaseModel))
        self.assertIs(type(instance), BaseModel)

        instance.name = "Holberton"
        instance.my_number = 89
        self.assertEqual(instance.name, "Holberton")
        self.assertEqual(instance.my_number, 89)

    def test_none(self):
        """Check if a new instance is not none"""
        basemodel1 = BaseModel()
        self.assertIsNotNone(basemodel1)

    def test_uuid(self):
        """Check ids in the created instances"""
        basemodel1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(hasattr(basemodel1, "id"))
        self.assertNotEqual(basemodel1.id, bm2.id)

    def test_created_at(self):
        """Check if the instance has created_at Atttibute"""
        basemodel1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(basemodel1, "created_at")
        self.assertTrue(bm2, "created_at")

    def test_updated_at(self):
        """Check if the instance has created_at Atttibute"""
        basemodel1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(basemodel1, "updated_at")
        self.assertTrue(bm2, "updated_at")

    def test__str__(self):
        """Check the string of an created instance"""
        basemodel1 = BaseModel()
        printed = "[{}] ({}) {}".format(
            basemodel1.__class__.__name__, basemodel1.id, basemodel1.__dict__)
        self.assertEqual(str(basemodel1), printed)

    def test_to_dict(self):
        """Test the to_dict method from BaseModel"""
        basemodel1 = BaseModel()
        basemodel1_dict = basemodel1.to_dict()
        self.assertIsInstance(basemodel1_dict, dict)
        self.assertEqual(basemodel1_dict["__class__"], "BaseModel")
        self.assertEqual(str(basemodel1.id), basemodel1_dict["id"])
        self.assertIsInstance(basemodel1_dict["created_at"], str)
        self.assertIsInstance(basemodel1_dict["updated_at"], str)

    def test_save(self):
        """Test to check each update in the storage"""
        basemodel1 = BaseModel()
        self.assertTrue(hasattr(basemodel1, "updated_at"))
        basemodel1.save()
        self.assertTrue(hasattr(basemodel1, "updated_at"))
        t_arg = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                 'create_at': datetime(2017, 9, 28, 21, 5, 54, 119427),
                 'updated_at': datetime(2017, 9, 28, 21, 5, 54, 119572),
                 'name': 'basemodel1'}
        bm2 = BaseModel(t_arg)
        bm2.save()
        last_time = bm2.updated_at
        bm2.save()
        self.assertNotEqual(last_time, bm2.updated_at)

    def test_init_from_dict(self):
        """test to check a new instance witk Kwargs"""
        my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298',
                   '__class__': 'BaseModel', 'my_number': 89,
                   'updated_at': '2017-09-28T21:03:54.052302',
                   'name': 'Holberton'}
        basemodel1 = BaseModel(**my_dict)
        self.assertIsInstance(basemodel1, BaseModel)
        self.assertIsInstance(basemodel1.id, str)
        self.assertEqual(basemodel1.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsInstance(basemodel1.created_at, datetime)
        self.assertIsInstance(basemodel1.updated_at, datetime)
        self.assertIsInstance(basemodel1.name, str)
        self.assertEqual(basemodel1.name, 'Holberton')

    def test_new_attributte(self):
        """test to check if new attribute  can be added"""
        basemodel1 = BaseModel()
        basemodel1.name = "Betty"
        self.assertEqual(basemodel1.name, "Betty")
