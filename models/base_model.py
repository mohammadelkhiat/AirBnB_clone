#!/usr/bin/python3
'''Base model class'''

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                    continue
                if key == '__class__':
                    continue
                if key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                    continue
                if key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                    continue

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_set = self.__dict__.copy()
        dict_set['__class__'] = self.__class__.__name__
        dict_set['created_at'] = self.created_at.isoformat()
        dict_set['updated_at'] = self.updated_at.isoformat()
        return dict_set
