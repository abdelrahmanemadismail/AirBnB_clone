#!/usr/bin/python3
"""
Amenity module
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for Amenity class.
        """
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
