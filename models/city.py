#!/usr/bin/python3
'''city model class'''

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherit from BaseModel classe"""
    state_id = ""
    name = ""
