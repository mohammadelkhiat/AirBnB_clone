#!/usr/bin/python3
'''File Storage class'''

import json
import os
from models.base_model import BaseModel
import user


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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as outfile:
                new_obj = json.load(outfile)
            for value in new_obj.values():
                class_val = value["__class__"]
                self.new(eval(class_val)(**value))
