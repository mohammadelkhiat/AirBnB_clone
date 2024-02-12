#!/usr/bin/env python3
"""Verifying Class City"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class Test_City(unittest.TestCase):
    """Verifying Class city"""

    model = City()

    def test_inhertance(self):
        """Verifying Is Instance"""
        self.assertIsInstance(self.model, City)
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Verifying has attrinutes type"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))

    def test_attribute_a(self):
        """Verifying has attribute type"""
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertTrue(hasattr(self.model, "name"))

    def test_attribute_type(self):
        """Verifying Type of Attributes type"""
        self.assertIsInstance(self.model.state_id, str)
        self.assertIsInstance(self.model.name, str)

    def test_addattr(self):
        """Verifying add attribute type"""
        self.model.some = "some"
        self.assertTrue(hasattr(self.model, "some"))


if __name__ == "__main__":
    unittest.main()
