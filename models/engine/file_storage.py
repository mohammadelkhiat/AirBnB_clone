#!/usr/bin/python3
'''File Storage class'''

import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """class that serializes instances to
    a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        class_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[class_key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as outfile:
            json.dump(new_dict, outfile)

    def reload(self):
        obb = {"User": User, "State": State, "BaseModel": BaseModel,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as outfile:
                new_obj = json.load(outfile)
            for k, value in new_obj.items():
               clas = value["__class__"]
               obj = eval(clas + "(**value)")
               FileStorage.__objects[k] = obj
