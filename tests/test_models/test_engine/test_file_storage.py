#!/usr/bin/python3
''' Testing our file_storage file '''


import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Testing the storage object"""
    
    def test_01storage_class(self):
        ''' Testing the storage object '''
        self.assertIsInstance(storage, FileStorage)
        
    """Tests for `__file_path`"""

    def test_02file_path_private(self):
        
        with self.assertRaises(AttributeError):
            storage.file_path
            storage._file_path
            storage.__file_path
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))

    def test_03file_path_type(self):
        
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_04file_path_value(self):
        
        self.assertGreater(len(storage._FileStorage__file_path), len(".json"))
        end_of_file_path = storage._FileStorage__file_path[(-len(".json")):]
        self.assertEqual(end_of_file_path, ".json")


    def test_05objects_private(self):
        
        with self.assertRaises(AttributeError):
            storage.objects
            storage._objects
            storage.__objects
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))

    def test_06objects_type(self):
        self.assertIsInstance(storage._FileStorage__objects, dict)

# Testing all() method in FileStorage class

    def test_08all_return_type(self):
        
        all_objs2 = storage.all()
        self.assertIsInstance(all_objs2, dict)

    def test_09all_return_value(self):
        
        all_objs2 = storage.all()
        self.assertIs(all_objs2, storage._FileStorage__objects)

    def test_10all_Nof_arguments(self):
        
        self.assertRaises(TypeError, storage.all(), "argument")

# Testing new() method in FileStorage class which is used by BaseModel __init__

    def test_11newObj_called_new(self):
       
        my_models = BaseModel()
        my_models.name = "My_First_Model"
        my_models.my_number = 89

        my_model_key = f"{my_models.__class__.__name__}.{my_models.id}"
        all_objs = storage.all()

        self.assertIn(my_model_key, all_objs.keys())

        self.assertTrue(hasattr(all_objs[my_model_key], 'id'))
        self.assertEqual(all_objs[my_model_key].id, my_models.id)

        self.assertTrue(hasattr(all_objs[my_model_key], 'name'))
        self.assertEqual(all_objs[my_model_key].name, my_models.name)

        self.assertTrue(hasattr(all_objs[my_model_key], 'my_number'))
        self.assertEqual(all_objs[my_model_key].my_number, my_models.my_number)


    def test_12save_return(self):
        
        my_models = BaseModel()
        self.assertIsNone(my_models.save())
        self.assertIsNone(storage.save())

    def test_13save_Nof_arguments(self):
        
        my_model1s = BaseModel()
        self.assertRaises(TypeError, storage.save(), "argument")
        self.assertRaises(TypeError, my_model1s.save(), "argument")

    def test_14save_file_exist(self):
        
        my_model = BaseModel()
        my_model.save()

        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        self.assertTrue(os.path.getsize(storage._FileStorage__file_path) > 0)

    def tearDownClass(cls):
        os.remove("file.json")

    def setUpClass(cls):
        os.remove("file.json")


if __name__ == "__main__":
    unittest.main()
