import unittest
from models.base_model import BaseModel
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import os
from datetime import datetime
from time import sleep

class TestBaseModel(unittest.TestCase):
    """ Suite to test Base class """
    
    """ #1 ATTRIBUTES """
    
    def setUp(self):
        """Set up for all methods"""
        pass
    
    def test_creation(self):
        """Testing whether is created or not"""
        Attr122 = BaseModel()
        self.assertTrue(hasattr(Attr122, "id"))
        self.assertTrue(hasattr(Attr122, "created_at"))
        self.assertTrue(hasattr(Attr122, "updated_at"))

    def id_duplications(self):
        """Is it realy Universal Unique or is it just a name"""
        id11 = BaseModel()
        id22 = BaseModel()
        id33 = BaseModel()
        id45 = BaseModel()
        self.assertFalse(id11.id == id22.id)
        self.assertFalse(id11.id == id33.id)
        self.assertFalse(id11.id == id45.id)
        self.assertFalse(id22.id == id33.id)
        self.assertFalse(id22.id == id45.id)
        self.assertFalse(id45.id == id45.id)
        
    def test_our_types(self):
        """did we get the string and datetime Right"""
        Typo2 = BaseModel()
        self.assertEqual(type(Typo2.id, str))
        self.assertEqual(type(Typo2.created_at, datetime))
        self.assertEqual(type(Typo2.updated_at, datetime))
        
    """ #2 METHODS """
    
    def test_save(self):
        """Do we save the time or we go through black hole"""
        sa22 = BaseModel()
        creation_time = sa22.created_at
        updating_time = sa22.updated_at
        sleep(0.06)
        sa22.save()
        self.assertFalse(updating_time == sa22.updated_at)
        self.assertTrue(creation_time == sa22.created_at)
        
    def test_to_dict(self):
        """Is right conerted or not"""
        the_base22 = BaseModel()
        dic = the_base22.to_dict()
        self.assertEqual(dic['__class__'], "BaseModel")
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        
    def test_isoformat(self):
        """Did we get to ISO 8601"""
        the_base2 = BaseModel()
        crtdtime2 = datetime.now()
        updtdtime2 = datetime.now()
        the_base2.created_at = crtdtime2
        the_base2.updated_at = updtdtime2

        dic = the_base2.to_dict()
        self.assertEqual(dic["created_at"], crtdtime2.isoformat())
        self.assertEqual(dic["updated_at"], updtdtime2.isoformat())
