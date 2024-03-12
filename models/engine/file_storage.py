#!/usr/bin/python3
"""
File Storage
"""


import json


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

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }

        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = classes[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
