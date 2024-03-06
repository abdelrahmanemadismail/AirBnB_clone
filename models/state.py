#!/usr/bin/python3
"""
State module
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for State class.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
