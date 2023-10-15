#!/usr/bin/python3
"""Module for Base class
defines all common attributes/methods for other classes.
"""

from models import storage
from datetime import datetime
import uuid


class BaseModel:

    """Class for base model of objects."""

    def __init__(self, *args, **kwargs):
        """Initialization of  Base instance.

        Args:
            - *args: list of argument
            - **kwargs: dict of key-values argument
        """

        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns returns printable string representation of an instance."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current
         datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat("T")
        my_dict["updated_at"] = my_dict["updated_at"].isoformat("T")
        return my_dict
