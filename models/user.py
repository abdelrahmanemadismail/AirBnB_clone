#!/usr/bin/python3
"""
User module
"""


from .base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for User class.
        """
        self.email = kwargs.pop('email', "")
        self.password = kwargs.pop('password', "")
        self.first_name = kwargs.pop('first_name', "")
        self.last_name = kwargs.pop('last_name', "")
        super().__init__(*args, **kwargs)
