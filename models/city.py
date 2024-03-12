#!/usr/bin/python3
"""
City module
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for City class.
        """
        self.state_id = kwargs.pop('state_id', "")
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
