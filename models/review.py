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
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")
