#!/usr/bin/python3

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
        Attr1 = BaseModel()
        self.assertTrue(hasattr(Attr1, "id"))
        self.assertTrue(hasattr(Attr1, "created_at"))
        self.assertTrue(hasattr(Attr1, "updated_at"))

    def id_duplications(self):
        """Is it realy Universal Unique or is it just a name"""
        id1 = BaseModel()
        id2 = BaseModel()
        id3 = BaseModel()
        id4 = BaseModel()
        self.assertFalse(id1.id == id2.id)
        self.assertFalse(id1.id == id3.id)
        self.assertFalse(id1.id == id4.id)
        self.assertFalse(id2.id == id3.id)
        self.assertFalse(id2.id == id4.id)
        self.assertFalse(id3.id == id4.id)
        
    def test_our_types(self):
        """did we get the string and datetime Right"""
        Typo = BaseModel()
        self.assertEqual(type(Typo.id, str))
        self.assertEqual(type(Typo.created_at, datetime))
        self.assertEqual(type(Typo.updated_at, datetime))
        
    """ #2 METHODS """
    
    def test_save(self):
        """Do we save the time or we go through black hole"""
        sa = BaseModel()
        creation_time = sa.created_at
        updating_time = sa.updated_at
        sleep(0.06)
        sa.save()
        self.assertFalse(updating_time == sa.updated_at)
        self.assertTrue(creation_time == sa.created_at)
        
    def test_to_dict(self):
        """Is right conerted or not"""
        the_base = BaseModel()
        dic = the_base.to_dict()
        self.assertEqual(dic['__class__'], "BaseModel")
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        
    def test_isoformat(self):
        """Did we get to ISO 8601"""
        the_base = BaseModel()
        crtdtime = datetime.now()
        updtdtime = datetime.now()
        the_base.created_at = crtdtime
        the_base.updated_at = updtdtime

        dic = the_base.to_dict()
        self.assertEqual(dic["created_at"], crtdtime.isoformat())
        self.assertEqual(dic["updated_at"], updtdtime.isoformat())
        