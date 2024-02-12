#!/usr/bin/python3
'''review model class'''

from models.base_model import BaseModel
import models


class Review(BaseModel):
    """Review class that inherit from BaseModel classe"""
    place_id = ""
    user_id = ""
    text = ""
