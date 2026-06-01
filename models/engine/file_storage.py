#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects.

        Returns:
            dict: All objects stored in __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key <class name>.id.

        Args:
            obj: The object to store.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for key, value in data.items():
                class_name = value.get("__class__")
                if class_name in classes:
                    FileStorage.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass
