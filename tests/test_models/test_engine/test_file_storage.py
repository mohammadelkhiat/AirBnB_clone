#!/usr/bin/python3
''' TestSuite for file_storage engine '''


import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''TestSuite for FileStorage class'''

# Testing the storage object

    def test_01storage_class(self):
        ''' Testing the storage object '''
        self.assertIsInstance(storage, FileStorage)

# Test the class attribute of storage

    # Tests for `__file_path`

    def test_02file_path_private(self):
        ''' Test the __file_path is a private class attribute '''
        with self.assertRaises(AttributeError):
            storage.file_path
            storage._file_path
            storage.__file_path
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))

    def test_03file_path_type(self):
        ''' Test the type of __file_path is a str '''
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_04file_path_value(self):
        ''' Test __file_path is a path of JSON file '''
        self.assertGreater(len(storage._FileStorage__file_path), len(".json"))
        end_of_file_path = storage._FileStorage__file_path[(-len(".json")):]
        self.assertEqual(end_of_file_path, ".json")

    # Tests for __objects:

    def test_05objects_private(self):
        ''' Test the __objects is a private class attribute '''
        with self.assertRaises(AttributeError):
            storage.objects
            storage._objects
            storage.__objects
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))

    def test_06objects_type(self):
        ''' Test the type of __objects is a dict '''
        self.assertIsInstance(storage._FileStorage__objects, dict)

# Testing all() method in FileStorage class

    def test_08all_return_type(self):
        ''' Test the return type of the all() method '''
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_09all_return_value(self):
        ''' Test the return value of the all() method '''
        all_objs = storage.all()
        self.assertIs(all_objs, storage._FileStorage__objects)

    def test_10all_Nof_arguments(self):
        ''' Test number of arguments all() can accept is 0 '''
        self.assertRaises(TypeError, storage.all(), "argument")

# Testing new() method in FileStorage class which is used by BaseModel __init__

    def test_11newObj_called_new(self):
        ''' Test that when a new BaseModel object created
        the new() method is called'''
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_key = f"{my_model.__class__.__name__}.{my_model.id}"
        all_objs = storage.all()

        self.assertIn(my_model_key, all_objs.keys())

        self.assertTrue(hasattr(all_objs[my_model_key], 'id'))
        self.assertEqual(all_objs[my_model_key].id, my_model.id)

        self.assertTrue(hasattr(all_objs[my_model_key], 'name'))
        self.assertEqual(all_objs[my_model_key].name, my_model.name)

        self.assertTrue(hasattr(all_objs[my_model_key], 'my_number'))
        self.assertEqual(all_objs[my_model_key].my_number, my_model.my_number)

# Testing save() method in FileStorage class

    def test_12save_return(self):
        ''' Test the return value of the save() method is None '''
        my_model = BaseModel()
        self.assertIsNone(my_model.save())
        self.assertIsNone(storage.save())

    def test_13save_Nof_arguments(self):
        ''' Test number of arguments save() can accept is 0 '''
        my_model = BaseModel()
        self.assertRaises(TypeError, storage.save(), "argument")
        self.assertRaises(TypeError, my_model.save(), "argument")

    def test_14save_file_exist(self):
        ''' Test the file saved in __file_path
        exists and not empty after save() '''
        my_model = BaseModel()
        my_model.save()

        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        self.assertTrue(os.path.getsize(storage._FileStorage__file_path) > 0)

    @classmethod
    def tearDownClass(cls):
        '''This removes file.json which is created in the test'''
        os.remove("file.json")

    @classmethod
    def setUpClass(cls):
        '''This removes file.json which is created in the test'''
        os.remove("file.json")
# Testing reload() method in FileStorage class which is used by models/__init__
# This part should be devided into 2 part one in the top and one in the end


# nothing for now but will continue later


if __name__ == "__main__":
    unittest.main()
