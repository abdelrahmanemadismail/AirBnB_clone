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
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")