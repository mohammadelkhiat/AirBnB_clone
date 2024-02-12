#!/usr/bin/python3
"""Building the user info"""

import cmd
import models.engine
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """Clerifaing"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
