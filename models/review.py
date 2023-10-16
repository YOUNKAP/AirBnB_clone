#!/usr/bin/python3
"""Module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review.
        Args:
            - place_id (str) :
            - user_id (str) :
            - text (str) :
    """
    place_id = ""
    user_id = ""
    text = ""
