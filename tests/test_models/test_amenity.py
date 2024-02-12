#!/usr/bin/env python3
"""Verifying Class Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class Test_Amenity(unittest.TestCase):
    """Verifying Class Amenity"""

    model = Amenity()

    def test_inhertance(self):
        """Verifying inheritance and instance types"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, Amenity)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Verifying model properties"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "__init__"))

    def test_attribute_a(self):
        """Verifying attribute existence"""
        self.assertTrue(hasattr(self.model, "name"))

    def test_attribute_type(self):
        """Verifying attribute types"""
        self.assertIsInstance(self.model.name, str)

    def test_addattr(self):
        """Verifying attribute addition"""
        self.model.some = "some"
        self.assertTrue(hasattr(self.model, "some"))


if __name__ == "__main__":
    unittest.main()
