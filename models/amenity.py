#!/usr/bin/python3
"""Module for Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing a Amenity.
        Args:
            - name (str) : Amenity name
    """
    name = ""
