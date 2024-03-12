#!/usr/bin/python3
"""
Place module
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for Place class.
        """
        self.city_id = kwargs.pop('city_id', "")
        self.user_id = kwargs.pop('user_id', "")
        self.name = kwargs.pop('name', "")
        self.description = kwargs.pop('description', "")
        self.number_rooms = kwargs.pop('number_rooms', 0)
        self.number_bathrooms = kwargs.pop('number_bathrooms', 0)
        self.max_guest = kwargs.pop('max_guest', 0)
        self.price_by_night = kwargs.pop('price_by_night', 0)
        self.latitude = kwargs.pop('latitude', 0.0)
        self.longitude = kwargs.pop('longitude', 0.0)
        self.amenity_ids = kwargs.pop('amenity_ids', [])
        super().__init__(*args, **kwargs)
