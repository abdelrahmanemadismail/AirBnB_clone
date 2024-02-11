#!/usr/bin/python3
"""Base module"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all other classes in the project.
    """

    def __init__(self):
        """
        Constructor for Base class.
        """

        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing all attributes of the object.
                  - '__class__': The name of the class
                  - 'created_at': The creation time in ISO format
                  - 'updated_at': The update time in ISO format
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
