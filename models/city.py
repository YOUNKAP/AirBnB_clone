#!/usr/bin/python3
"""Module for City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City.
        Args:
            - state_id (str) : Id of state
            - name (str) : name of state
    """
    state_id = ""
    name = ""
