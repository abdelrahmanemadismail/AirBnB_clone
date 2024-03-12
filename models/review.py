#!/usr/bin/python3
"""
Review module
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for Review class.
        """
        self.place_id = kwargs.pop('place_id', "")
        self.user_id = kwargs.pop('user_id', "")
        self.text = kwargs.pop('text', "")
        super().__init__(*args, **kwargs)
