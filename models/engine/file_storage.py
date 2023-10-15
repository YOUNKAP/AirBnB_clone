#!/usr/bin/python3
"""Module for FileStorage class."""
import os
import json
from datetime import datetime


class FileStorage:

    """Serialize instance to a JSON file and deserialize JSON file to instance.
        Args:
        - __file_path (str) : path to the JSON file
        - __objects (dict) :empty but will store all object by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as jsonfile:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, jsonfile)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as jsonfile:
            obj_dict = json.load(jsonfile)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime}
        }
        return attributes
