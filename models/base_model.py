#!/usr/bin/python3
"""Module for Base class
defines all common attributes/methods for other classes.
"""

from datetime import datetime
import uuid


class BaseModel():

    """Class for base model of objects."""

    def __init__(self, *args, **kwargs):
        """Initialization of  Base instance.

        Args:
            - id (str) : uuid  at instance creation
            - create_at(datetime) : datetime at instance creation
            - update_at (datetime): datetime at instance update
            - *args: list of argument
            - **kwargs: dict of key-values argument
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns returns printable string representation of an instance."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current
         datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance."""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = type(self).__name__
        inst_dict["created_at"] = inst_dict["created_at"].isoformat("T")
        inst_dict["updated_at"] = inst_dict["updated_at"].isoformat("T")
        return inst_dict
