#!/usr/bin/python3
"""File storage engine"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Handles storage of objects in JSON file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes objects from JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    cls = v['__class__']
                    if cls in HBNBCommand.classes:
                        FileStorage.__objects[k] = HBNBCommand.classes[cls](**v)
