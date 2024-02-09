import unittest
from models.base_model import BaseModel
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import os


class TestBaseModel(unittest.TestCase):
    """ Suite to test Base class """
