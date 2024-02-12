#!/usr/bin/python3
"""Building the user info"""

from models.base_model import BaseModel


class User(BaseModel):
    """Clerifaing"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
