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
        self.name = kwargs.pop('name', "")
        super().__init__(*args, **kwargs)
