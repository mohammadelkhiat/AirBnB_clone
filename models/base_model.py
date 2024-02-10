#!/usr/bin/python3
'''Base model class'''

from uuid import uuid4
from datetime import datetime


class BaseModel:
    
    def __init__(self, *args, **kwargs):
        """BaseModel class that defines all 
        common attributes/methods for other classes
        
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        self.updated_at = datetime.now()
        
        
    def to_dict(self):
        dict_set = self.__dict__.copy()
        dict_set['__class__'] = self.__class__.__name__
        dict_set['created_at'] = self.created_at.isoformat()
        dict_set['updated_at'] = self.updated_at.isoformat()
        return dict_set