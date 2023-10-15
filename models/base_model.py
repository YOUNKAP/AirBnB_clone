#!/usr/bin/python3
"""Module for Base class
defines all common attributes/methods for other classes.
"""

from datetime import datetime
import uuid


class BaseModel:

    """Class for base model of objects.
        Args:
            - id (str) : uuid  at instance creation
            - create_at(datetime) : datetime at instance creation
            - update_at (datetime): datetime at instance update
    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    @classmethod
    def __str__(baseModel):
        """Returns returns printable string representation of an instance."""
        return "[{}] ({}) {}".\
            format(type(baseModel).__name__, baseModel.id, baseModel.__dict__)

    @classmethod
    def save(baseModel):
        """updates the public instance attribute updated_at with the current
         datetime."""
        baseModel.updated_at = datetime.now()

    @classmethod
    def to_dict(baseModel):
        """returns a dictionary containing all keys/values of the instance."""
        inst_dict = baseModel.__dict__.copy()
        inst_dict["__class__"] = type(baseModel).__name__
        inst_dict["created_at"] = inst_dict["created_at"].isoformat("T")
        inst_dict["updated_at"] = inst_dict["updated_at"].isoformat("T")
        return inst_dict
