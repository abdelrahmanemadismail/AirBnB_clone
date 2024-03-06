#!/usr/bin/python3
"""
File Storage
"""


import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    This class handles the serialization and deserialization of instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves the dictionary of all objects stored.
        
        Returns:
            dict: A dictionary containing all objects stored.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to the JSON file.
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to objects if it exists.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
