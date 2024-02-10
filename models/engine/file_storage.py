#!/usr/bin/python3
'''File Storage class'''


class FileStorage:
    """class that serializes instances to
    a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    