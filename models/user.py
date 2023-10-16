#!/usr/bin/python3
"""Module for User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User.
        Args:
            - email (str) : user email
            - password (str) : user pwd
            - first_name (str): user first name
            - last_name (str): user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
